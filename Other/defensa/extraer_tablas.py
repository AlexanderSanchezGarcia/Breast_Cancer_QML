#!/usr/bin/env python3
"""
Extrae los 36 cuadros (tablas) de Docs/Technical_Report.pdf como imágenes PNG
a 200 dpi (fondo blanco), genera Other/defensa/tablas_anexos/manifiesto.json
y las hojas de contacto en Other/defensa/tablas_anexos/revision/hoja_*.png.
"""

import json
import re
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parents[2]
PDF_PATH = REPO_ROOT / "Docs" / "Technical_Report.pdf"
LOT_PATH = REPO_ROOT / "Docs" / "Technical_Report.lot"
OUT_DIR = REPO_ROOT / "Other" / "defensa" / "tablas_anexos"
REV_DIR = OUT_DIR / "revision"

DPI = 200
MARGIN_PT = 10.0
TEXTBOX_X0 = 85.0
TEXTBOX_X1 = 555.3


def clean_latex_title(raw: str) -> str:
    """Limpia comandos LaTeX del título extraído del .lot."""
    s = raw.strip()
    s = re.sub(r"\\ignorespaces\s*", "", s)
    while re.search(r"\\(?:textit|textbf|textrm|emph)\s*\{([^{}]*)\}", s):
        s = re.sub(r"\\(?:textit|textbf|textrm|emph)\s*\{([^{}]*)\}", r"\1", s)
    while re.search(r"\\mathbf\s*\{([^{}]*)\}", s):
        s = re.sub(r"\\mathbf\s*\{([^{}]*)\}", r"\1", s)

    def replace_math(match: re.Match) -> str:
        m = match.group(1)
        m = m.replace(r"\phi", "φ")
        m = m.replace(r"\theta", "θ")
        m = m.replace(r"\alpha", "α")
        m = m.replace(r"\le", "≤")
        m = m.replace(r"\ge", "≥")
        m = m.replace(r"\langle", "⟨")
        m = m.replace(r"\rangle", "⟩")
        m = m.replace("_i", "ᵢ")
        m = re.sub(r"\s+", " ", m).strip()
        m = m.replace("φ (", "φ(").replace("⟨ ", "⟨").replace(" ⟩", "⟩")
        return m

    s = re.sub(r"\$([^$]+)\$", replace_math, s)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([.,:;)])", r"\1", s)
    return s


def parse_lot(lot_path: Path) -> dict[int, dict]:
    """Parsea Docs/Technical_Report.lot y devuelve {numero: {'titulo': ..., 'pagina_reporte': ...}}."""
    entries = {}
    pattern = re.compile(
        r"\\contentsline\s*\{table\}\{\\numberline\s*\{(\d+)\}\{(.*)\}\}\{(\d+)\}"
    )
    for line in lot_path.read_text(encoding="utf-8").splitlines():
        m = pattern.search(line)
        if m:
            num = int(m.group(1))
            raw_title = m.group(2)
            page_rep = int(m.group(3))
            entries[num] = {
                "numero": num,
                "titulo": clean_latex_title(raw_title),
                "pagina_reporte": page_rep,
            }
    return entries


def get_page_lines(page: fitz.Page) -> list[dict]:
    """Extrae todas las líneas de texto con su bbox, tamaños de fuente, dirección y texto."""
    lines = []
    d = page.get_text("dict")
    for b in d["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            txt = "".join(s["text"] for s in l["spans"]).strip()
            if not txt:
                continue
            sizes = sorted(
                set(round(s["size"], 1) for s in l["spans"] if s["text"].strip())
            )
            bbox = l["bbox"]
            lines.append(
                {
                    "x0": bbox[0],
                    "y0": bbox[1],
                    "x1": bbox[2],
                    "y1": bbox[3],
                    "sizes": sizes,
                    "dir": l["dir"],
                    "text": txt,
                }
            )
    lines.sort(key=lambda item: (round(item["y0"], 1), round(item["x0"], 1)))
    return lines


def is_page_number_line(line: dict, page_rect: fitz.Rect) -> bool:
    """Detecta si una línea es el número de página en el pie (o margen izquierdo en apaisada)."""
    if not line["text"].strip().isdigit():
        return False
    # En páginas verticales, el número de página está abajo al centro (y > 748, x ~ 311..329)
    if line["y0"] > 748.0 and 290.0 <= line["x0"] <= 345.0:
        return True
    # En página apaisada tras remove_rotation (792x612), el número de página queda a la izquierda (x < 42)
    if page_rect.width > page_rect.height and line["x1"] < 42.0:
        return True
    return False


def build_table_page_Index(doc: fitz.Document) -> dict[int, list[int]]:
    """Recorre el PDF una sola vez y devuelve {numero_cuadro: [paginas_pdf_1based]}."""
    start_pages: dict[int, int] = {}
    cont_pages: dict[int, list[int]] = {n: [] for n in range(1, 37)}

    cap_re = re.compile(r"^Cuadro\s+(\d+)\s*:")
    cont_re = re.compile(
        r"^(?:Cuadro|Tabla)\s+(\d+)\s*[–-]\s*continuaci[oó]n", re.IGNORECASE
    )

    for pno in range(len(doc)):
        page = doc[pno]
        if page.rotation != 0:
            page.remove_rotation()
        for l in get_page_lines(page):
            m_cap = cap_re.match(l["text"])
            if m_cap:
                n = int(m_cap.group(1))
                if 1 <= n <= 36 and n not in start_pages:
                    start_pages[n] = pno + 1
            m_cont = cont_re.match(l["text"])
            if m_cont:
                n = int(m_cont.group(1))
                if 1 <= n <= 36 and (pno + 1) not in cont_pages[n]:
                    cont_pages[n].append(pno + 1)

    result = {}
    for n in range(1, 37):
        if n not in start_pages:
            raise RuntimeError(f"No se encontró el pie 'Cuadro {n}:' en el PDF.")
        result[n] = [start_pages[n]] + sorted(cont_pages[n])
    return result


def compute_crop_rect(page: fitz.Page, num: int, is_continuation: bool) -> fitz.Rect:
    """
    Calcula el rectángulo de recorte (fitz.Rect) para el Cuadro `num` en `page`.
    Asume que si la página tenía rotación (p. ej. pág. 48), ya se aplicó remove_rotation().
    """
    lines = get_page_lines(page)
    if not is_continuation:
        header_re = re.compile(rf"^Cuadro\s+{num}\s*:")
    else:
        header_re = re.compile(
            rf"^(?:Cuadro|Tabla)\s+{num}\s*[–-]\s*continuaci[oó]n", re.IGNORECASE
        )

    header_line = None
    for l in lines:
        if header_re.match(l["text"]):
            header_line = l
            break
    if header_line is None:
        raise RuntimeError(
            f"No se encontró cabecera para Cuadro {num} (cont={is_continuation}) en pág {page.number + 1}"
        )

    any_cap_re = re.compile(
        r"^(?:Cuadro\s+\d+\s*:|(?:Cuadro|Tabla)\s+\d+\s*[–-]\s*continuaci[oó]n)",
        re.IGNORECASE,
    )
    next_cap_y = 9999.0
    for l in lines:
        if l["y0"] > header_line["y0"] + 5.0 and any_cap_re.match(l["text"]):
            next_cap_y = l["y0"]
            break

    drawings = page.get_drawings()
    hlines = sorted(
        [
            d["rect"]
            for d in drawings
            if abs(d["rect"].y1 - d["rect"].y0) < 3.0
            and (d["rect"].x1 - d["rect"].x0) > 50.0
            and header_line["y0"] < d["rect"].y0 < next_cap_y
        ],
        key=lambda r: r.y0,
    )
    if not hlines:
        raise RuntimeError(f"Sin reglas horizontales para Cuadro {num} en pág {page.number + 1}")

    # El primer hline tras el pie es el \toprule de la tabla; su ancho define el ancho de las reglas principales
    tw0, tw1 = hlines[0].x0, hlines[0].x1
    main_hlines = [
        r for r in hlines if abs(r.x0 - tw0) < 2.5 and abs(r.x1 - tw1) < 2.5
    ]
    bot_rule_y = main_hlines[-1].y1

    # Determinar hasta dónde llega la nota o el aviso de continuación debajo de bot_rule_y
    y_bot_content = bot_rule_y
    cont_footer_re = re.compile(r"^Contin[uú]a\s+en\s+la\s+siguiente\s+p[aá]gina", re.IGNORECASE)

    for l in lines:
        if l["y0"] < bot_rule_y - 2.0 or l["y0"] >= next_cap_y:
            continue
        if is_page_number_line(l, page.rect):
            continue
        if cont_footer_re.match(l["text"]) and l["y0"] <= y_bot_content + 20.0:
            y_bot_content = max(y_bot_content, l["y1"])
            continue
        # Las notas de tabla están en letra <= 10.5 pt (8.0 pt en pág 48 con x0>=59.8, 10.0 pt en el resto con x0>=96.8)
        max_sz = max(l["sizes"]) if l["sizes"] else 12.0
        min_note_x = 58.0 if page.rect.width > page.rect.height else 94.0
        if max_sz <= 10.5 and l["x0"] >= min_note_x and l["y0"] <= y_bot_content + 22.0:
            y_bot_content = max(y_bot_content, l["y1"])
            continue
        if l["y0"] > bot_rule_y:
            break

    # Calcular margen superior sin invadir líneas previas
    prev_lines = [
        l
        for l in lines
        if l["y1"] <= header_line["y0"] and not is_page_number_line(l, page.rect)
    ]
    y_top = header_line["y0"] - MARGIN_PT
    if prev_lines:
        prev_y1 = max(l["y1"] for l in prev_lines)
        if y_top < prev_y1 + 2.0:
            y_top = max(prev_y1 + 2.0, (prev_y1 + header_line["y0"]) / 2.0)

    # Calcular margen inferior sin invadir líneas posteriores
    next_lines = [
        l
        for l in lines
        if l["y0"] > y_bot_content + 0.5
        and not is_page_number_line(l, page.rect)
    ]
    y_bot = y_bot_content + MARGIN_PT
    if next_lines:
        next_y0 = min(l["y0"] for l in next_lines)
        if y_bot > next_y0 - 2.0:
            y_bot = min(next_y0 - 2.0, (y_bot_content + next_y0) / 2.0)

    # Evitar incluir el número de página inferior salvo colisión física en el PDF original (Cuadro 34, pág. 198)
    bot_page_nums = [
        l for l in lines if is_page_number_line(l, page.rect) and l["y0"] > 748.0
    ]
    if bot_page_nums and y_bot_content < bot_page_nums[0]["y0"] - 1.0:
        y_bot = min(y_bot, bot_page_nums[0]["y0"] - 2.0)

    # Ancho completo de la caja de texto + dibujos de la tabla
    table_drawings = [
        d["rect"]
        for d in drawings
        if header_line["y0"] - 2.0 <= d["rect"].y0 <= y_bot_content + 2.0
    ]
    min_draw_x = min((r.x0 for r in table_drawings), default=tw0)
    max_draw_x = max((r.x1 for r in table_drawings), default=tw1)

    if page.rect.width > page.rect.height:
        # Página apaisada (Cuadro 1 en pág. 48)
        x_left = min(tw0, min_draw_x) - MARGIN_PT
        x_right = max(tw1, max_draw_x) + MARGIN_PT
    else:
        x_left = min(TEXTBOX_X0, tw0, min_draw_x) - MARGIN_PT
        x_right = max(TEXTBOX_X1, tw1, max_draw_x) + MARGIN_PT

    rect = fitz.Rect(
        max(0.0, x_left),
        max(0.0, y_top),
        min(page.rect.width, x_right),
        min(page.rect.height, y_bot),
    )
    return rect


def check_white_borders(img: Image.Image) -> dict[str, bool]:
    """Verifica que los 4 bordes exteriores (2 px) del PNG sean completamente blancos."""
    w, h = img.size
    px = img.load()
    top_ok = all(px[x, y] == (255, 255, 255) for x in range(w) for y in range(2))
    bot_ok = all(px[x, y] == (255, 255, 255) for x in range(w) for y in range(h - 2, h))
    left_ok = all(px[x, y] == (255, 255, 255) for x in range(2) for y in range(h))
    right_ok = all(px[x, y] == (255, 255, 255) for x in range(w - 2, w) for y in range(h))
    return {"top": top_ok, "bottom": bot_ok, "left": left_ok, "right": right_ok}


def build_contact_sheets(crops_info: list[dict]) -> list[Path]:
    """Genera hojas de contacto con 6 recortes por hoja (2 columnas x 3 filas)."""
    REV_DIR.mkdir(parents=True, exist_ok=True)
    per_sheet = 6
    cols, rows = 2, 3
    cell_w, cell_h = 900, 620
    header_h = 44
    pad = 24
    sheet_w = cols * cell_w + (cols + 1) * pad
    sheet_h = rows * cell_h + (rows + 1) * pad

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 22)
    except Exception:
        font = ImageFont.load_default()

    sheet_paths = []
    for s_idx in range(0, len(crops_info), per_sheet):
        batch = crops_info[s_idx : s_idx + per_sheet]
        sheet_num = (s_idx // per_sheet) + 1
        canvas = Image.new("RGB", (sheet_w, sheet_h), (242, 244, 248))
        draw = ImageDraw.Draw(canvas)

        for i, item in enumerate(batch):
            r = i // cols
            c = i % cols
            x0 = pad + c * (cell_w + pad)
            y0 = pad + r * (cell_h + pad)

            draw.rectangle(
                [x0, y0, x0 + cell_w, y0 + cell_h],
                fill=(255, 255, 255),
                outline=(180, 186, 200),
                width=2,
            )
            draw.rectangle(
                [x0, y0, x0 + cell_w, y0 + header_h],
                fill=(20, 28, 68),
            )
            label = f"Cuadro {item['numero']} ({item['archivo']}) — pág. PDF {item['pagina_pdf']} — {item['width']}x{item['height']} px"
            draw.text((x0 + 12, y0 + 10), label, fill=(255, 255, 255), font=font)

            img = Image.open(OUT_DIR / item["archivo"]).convert("RGB")
            avail_w = cell_w - 20
            avail_h = cell_h - header_h - 20
            scale = min(avail_w / img.width, avail_h / img.height, 1.0)
            new_w = max(1, int(round(img.width * scale)))
            new_h = max(1, int(round(img.height * scale)))
            thumb = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

            tx = x0 + 10 + (avail_w - new_w) // 2
            ty = y0 + header_h + 10 + (avail_h - new_h) // 2
            canvas.paste(thumb, (tx, ty))
            draw.rectangle(
                [tx - 1, ty - 1, tx + new_w, ty + new_h],
                outline=(220, 50, 50),
                width=1,
            )

        out_path = REV_DIR / f"hoja_{sheet_num}.png"
        canvas.save(out_path, "PNG")
        sheet_paths.append(out_path)
    return sheet_paths


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    REV_DIR.mkdir(parents=True, exist_ok=True)

    lot_entries = parse_lot(LOT_PATH)
    if len(lot_entries) != 36:
        raise RuntimeError(f"Se esperaban 36 entradas en .lot y se hallaron {len(lot_entries)}")

    # Orden en el deck: 1..5 y 9..34 primero (1..31), luego 6, 7, 8, 35, 36 (32..36)
    deck_sequence = [1, 2, 3, 4, 5] + list(range(9, 35)) + [6, 7, 8, 35, 36]
    orden_deck_map = {num: idx + 1 for idx, num in enumerate(deck_sequence)}

    doc = fitz.open(PDF_PATH)
    page_index = build_table_page_Index(doc)

    manifest = []
    all_crops_for_sheets = []
    verification_rows = []

    for num in range(1, 37):
        lot_info = lot_entries[num]
        pdf_pages = page_index[num]
        multipage = len(pdf_pages) > 1
        filenames = []
        part_verifications = []

        for p_idx, pno in enumerate(pdf_pages):
            page = doc[pno - 1]
            if page.rotation != 0:
                page.remove_rotation()
            is_cont = p_idx > 0
            rect = compute_crop_rect(page, num, is_cont)

            if multipage:
                suffix = chr(ord("a") + p_idx)
                fname = f"Cuadro_{num}_{suffix}.png"
            else:
                fname = f"Cuadro_{num}.png"

            out_png = OUT_DIR / fname
            pix = page.get_pixmap(clip=rect, dpi=DPI, alpha=False)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            img.save(out_png, "PNG")

            borders = check_white_borders(img)
            borders_ok = all(borders.values())

            clip_text = page.get_text("text", clip=rect).strip()
            clip_flat = re.sub(r"\s+", " ", clip_text).strip()
            starts_ok = clip_flat.startswith(f"Cuadro {num}:") if p_idx == 0 else True

            filenames.append(fname)
            all_crops_for_sheets.append(
                {
                    "numero": num,
                    "archivo": fname,
                    "pagina_pdf": pno,
                    "width": img.width,
                    "height": img.height,
                }
            )
            part_verifications.append(
                {
                    "archivo": fname,
                    "pagina_pdf": pno,
                    "width": img.width,
                    "height": img.height,
                    "starts_ok": starts_ok,
                    "borders_ok": borders_ok,
                    "first_70": clip_flat[:70],
                    "last_70": clip_flat[-70:],
                }
            )

        manifest.append(
            {
                "numero": num,
                "titulo": lot_info["titulo"],
                "pagina_reporte": lot_info["pagina_reporte"],
                "paginas_pdf": pdf_pages,
                "archivos": filenames,
                "multipagina": multipage,
                "orden_deck": orden_deck_map[num],
            }
        )
        verification_rows.append((num, part_verifications))

    manifest_path = OUT_DIR / "manifiesto.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    sheet_paths = build_contact_sheets(all_crops_for_sheets)

    print("=== VERIFICACIÓN AUTOMÁTICA DE LOS 36 CUADROS ===")
    all_ok = True
    for num, parts in verification_rows:
        for p_idx, pv in enumerate(parts):
            if (p_idx == 0 and not pv["starts_ok"]) or not pv["borders_ok"]:
                all_ok = False
            status = "OK" if pv["starts_ok"] else "FALLO_INICIO"
            b_status = "OK" if pv["borders_ok"] else "BORDE_TOCA"
            print(
                f"Cuadro {num:2d} | {pv['archivo']:16s} | pág {pv['pagina_pdf']:3d} | "
                f"{pv['width']:4d}x{pv['height']:4d} px | empieza_Cuadro_N={status} | bordes_blancos={b_status}"
            )
            print(f"   inicio(~70): {pv['first_70']!r}")
            print(f"   final (~70): {pv['last_70']!r}")
    print(
        f"\nTotal cuadros: {len(manifest)} | Total PNGs: {len(all_crops_for_sheets)} | "
        f"Hojas de contacto: {len(sheet_paths)} | Todo OK: {all_ok}"
    )


if __name__ == "__main__":
    main()
