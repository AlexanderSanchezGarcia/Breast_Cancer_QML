#!/usr/bin/env python3
"""
analizar_logs.py — TT 2026-B039
Analiza los archivos .log, .aux y .pdf generados para cada documento (borrador_completo
y cada borrador_<carpeta>), reportando:
- Páginas
- Primera sección en el PDF
- Referencias o citas sin resolver
- Etiquetas duplicadas (multiply defined)
- Cajas desbordadas (Overfull > 10pt)
Imprime una tabla de resumen en formato Markdown y texto claro.
"""
import os
import sys
import re

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

def get_page_count(pdf_path, log_path):
    # Try fitz first
    if fitz and os.path.isfile(pdf_path):
        try:
            doc = fitz.open(pdf_path)
            return len(doc)
        except Exception:
            pass
    # Try log file
    if os.path.isfile(log_path):
        try:
            with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
                log_text = f.read()
            m = re.search(r"Output written on .*?\(([0-9]+)\s+pages", log_text, re.DOTALL)
            if m:
                return int(m.group(1))
        except Exception:
            pass
    return "N/D"

def get_first_section(pdf_path, aux_path, is_completo=False):
    # Try aux file first for canonical section number and title
    if os.path.isfile(aux_path):
        try:
            with open(aux_path, "r", encoding="utf-8", errors="ignore") as f:
                aux_text = f.read()
            # Match \@writefile{toc}{\contentsline {section}{\numberline {N}Title}
            matches = re.findall(r"\\contentsline\s*\{section\}\{\\numberline\s*\{([^}]+)\}([^}]+)\}", aux_text)
            if matches:
                num, title = matches[0]
                # Clean up any TeX macros in title
                title = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?\{?", "", title).replace("}", "").strip()
                return f"{num}. {title[:20]}"
        except Exception:
            pass

    # Try fitz PDF inspection
    if fitz and os.path.isfile(pdf_path):
        try:
            doc = fitz.open(pdf_path)
            start_p = 4 if is_completo else 0
            for page_num in range(start_p, min(start_p + 10, len(doc))):
                page_text = doc[page_num].get_text()
                lines = [l.strip() for l in page_text.splitlines() if l.strip()]
                for i, line in enumerate(lines):
                    m = re.match(r"^([0-9]+|[A-Z])\.\s*(.*)", line)
                    if m:
                        num = m.group(1)
                        title = m.group(2).strip()
                        if not title and i + 1 < len(lines):
                            title = lines[i+1].strip()
                        return f"{num}. {title[:20]}"
        except Exception:
            pass

    return "N/D"

def analyze_log(log_path):
    if not os.path.isfile(log_path):
        return {
            "unresolved_refs": "Log no encontrado",
            "unresolved_cites": "Log no encontrado",
            "duplicate_labels": "Log no encontrado",
            "overfull_boxes": "Log no encontrado"
        }

    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        log_content = f.read()

    unresolved_refs = re.findall(r"LaTeX Warning: Reference `([^`]+)\' on page \d+ undefined", log_content)
    unresolved_cites = re.findall(r"Citation `([^`]+)\' on page \d+ undefined", log_content)
    dup_labels = re.findall(r"LaTeX Warning: Label `([^`]+)\' multiply defined", log_content)
    overfull_matches = re.findall(r"Overfull \\hbox \(([0-9.]+)pt too wide\)", log_content)
    overfull_gt_10 = [float(x) for x in overfull_matches if float(x) > 10.0]

    return {
        "unresolved_refs": len(unresolved_refs),
        "unresolved_cites": len(unresolved_cites),
        "duplicate_labels": len(dup_labels),
        "overfull_boxes": len(overfull_gt_10)
    }

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    docs_dir = os.path.join(repo_root, "Docs")
    cap_dir = os.path.join(docs_dir, "capitulos")
    build_dir = os.path.join(cap_dir, "_build")

    documents = []

    # 1. borrador_completo
    comp_pdf = os.path.join(cap_dir, "borrador_completo.pdf")
    comp_log = os.path.join(build_dir, "borrador_completo.log")
    comp_aux = os.path.join(build_dir, "borrador_completo.aux")
    documents.append(("borrador_completo", comp_pdf, comp_log, comp_aux, True))

    # 2. Chapters
    all_dirs = [
        d for d in os.listdir(cap_dir)
        if os.path.isdir(os.path.join(cap_dir, d))
        and not d.startswith((".", "_", "comun"))
    ]
    def sort_key(d):
        if d.startswith("A"): return (1, 0, d)
        m = re.match(r"^(\d+)", d)
        if m: return (0, int(m.group(1)), d)
        return (2, 0, d)
    all_dirs.sort(key=sort_key)

    for d in all_dirs:
        pdf_path = os.path.join(cap_dir, d, f"borrador_{d}.pdf")
        log_path = os.path.join(build_dir, d, f"borrador_{d}.log")
        aux_path = os.path.join(build_dir, d, f"borrador_{d}.aux")
        if not os.path.isfile(log_path):
            log_path = os.path.join(build_dir, f"borrador_{d}.log")
            aux_path = os.path.join(build_dir, f"borrador_{d}.aux")
        documents.append((f"borrador_{d}", pdf_path, log_path, aux_path, False))

    print("=" * 114)
    print("RESUMEN DE COMPILACIÓN DE BORRADORES (Docs/capitulos/)")
    print("=" * 114)
    
    header = f"| {'Documento':<26} | {'Págs':>5} | {'1ª Sección':<22} | {'Refs sin resolver':>17} | {'Citas sin resolver':>18} | {'Etiquetas dup.':>14} | {'Overfull > 10pt':>15} |"
    sep = f"|{'-'*28}|{'-'*7}|{'-'*24}|{'-'*19}|{'-'*20}|{'-'*16}|{'-'*17}|"
    print(header)
    print(sep)

    all_passed = True
    for doc_name, pdf_path, log_path, aux_path, is_comp in documents:
        pages = get_page_count(pdf_path, log_path)
        first_sec = get_first_section(pdf_path, aux_path, is_completo=is_comp)
        stats = analyze_log(log_path)
        
        u_refs = stats["unresolved_refs"]
        u_cites = stats["unresolved_cites"]
        dups = stats["duplicate_labels"]
        over = stats["overfull_boxes"]

        if u_refs != 0 or u_cites != 0 or dups != 0:
            all_passed = False

        print(f"| {doc_name:<26} | {str(pages):>5} | {first_sec:<22} | {str(u_refs):>17} | {str(u_cites):>18} | {str(dups):>14} | {str(over):>15} |")

    print(sep)
    print()
    if all_passed:
        print("ESTADO: ACEPTACIÓN SATISFECHA (Cero referencias sin resolver, cero citas sin resolver, cero etiquetas duplicadas).")
        return 0
    else:
        print("ESTADO: FALLO (Existen referencias, citas o etiquetas no resueltas).", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
