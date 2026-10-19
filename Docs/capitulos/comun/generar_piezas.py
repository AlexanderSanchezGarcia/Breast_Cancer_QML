#!/usr/bin/env python3
"""
generar_piezas.py — TT 2026-B039
Genera comun/preambulo.tex, comun/bibliografia_completa.tex,
las bibliografías por capítulo comun/bibliografia_<carpeta>.tex,
borrador_completo.tex, cada borrador_<carpeta>.tex, y asegura
el .latexmkrc en cada carpeta de capítulo.
"""
import os
import sys
import re
import subprocess
import glob

def get_chapter_sort_key(d):
    if d.startswith("A"):
        return (1, 0, d)
    m = re.match(r"^(\d+)", d)
    if m:
        return (0, int(m.group(1)), d)
    return (2, 0, d)

def natural_sort_files(file_list):
    if not file_list:
        return []
    p = subprocess.run(["sort", "-t_", "-k1,1V"], input="\n".join(file_list), text=True, capture_output=True)
    return [f for f in p.stdout.splitlines() if f]

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    docs_dir = os.path.join(repo_root, "Docs")
    cap_dir = os.path.join(docs_dir, "capitulos")
    comun_dir = os.path.join(cap_dir, "comun")
    build_dir = os.path.join(cap_dir, "_build")

    os.makedirs(comun_dir, exist_ok=True)
    os.makedirs(build_dir, exist_ok=True)

    tr_path = os.path.join(docs_dir, "Technical_Report.tex")
    if not os.path.isfile(tr_path):
        print(f"ERROR: {tr_path} no encontrado", file=sys.stderr)
        sys.exit(1)

    with open(tr_path, "r", encoding="utf-8") as f:
        tr_text = f.read()

    # ----------------------------------------------------
    # 1. comun/preambulo.tex
    # ----------------------------------------------------
    preamble_part = tr_text.split("\\begin{document}")[0]
    if "\\usepackage{xr-hyper}" not in preamble_part:
        preamble_part = preamble_part.replace(
            "\\usepackage{hyperref}",
            "\\usepackage{xr-hyper}\n\\usepackage{hyperref}"
        )
    if "\\graphicspath" not in preamble_part:
        preamble_part = preamble_part.replace(
            "\\usepackage{graphicx}",
            "\\usepackage{graphicx}\n\\graphicspath{{../../}{../}{./}}"
        )
    extra_path = os.path.join(docs_dir, "insumos/preambulo_extra.tex")
    if os.path.isfile(extra_path):
        with open(extra_path, "r", encoding="utf-8") as f:
            preamble_part += "\n" + f.read()

    preambulo_out = os.path.join(comun_dir, "preambulo.tex")
    with open(preambulo_out, "w", encoding="utf-8") as f:
        f.write("% ============================================================\n")
        f.write("% comun/preambulo.tex — Preámbulo unificado para borradores\n")
        f.write("% Generado automáticamente por compilar_borradores.sh. No editar.\n")
        f.write("% ============================================================\n\n")
        f.write(preamble_part)

    # ----------------------------------------------------
    # 2. comun/bibliografia_completa.tex y parseo de bibitems
    # ----------------------------------------------------
    # Desde la integración del 2026-10-18 la bibliografía única está en Docs/bibliografia.tex
    # (ya fusiona TT1, bibitems_nuevos y bibitems_noche); se copia tal cual.
    with open(os.path.join(docs_dir, "bibliografia.tex"), "r", encoding="utf-8") as f:
        full_bib_content = f.read()
    with open(os.path.join(comun_dir, "bibliografia_completa.tex"), "w", encoding="utf-8") as f:
        f.write(full_bib_content)

    # Parse all individual bibitems
    pattern = re.compile(r"(\\bibitem(?:\[.*?\])?\{([^}]+)\}.*?)(?=\\bibitem|\Z)", re.DOTALL)
    bib_dict = {}
    for match in pattern.finditer(full_bib_content):
        key = match.group(2).strip()
        block = match.group(1).strip()
        block = re.sub(r"\\end\{thebibliography\}.*$", "", block, flags=re.DOTALL).strip()
        bib_dict[key] = block

    # ----------------------------------------------------
    # 3. Descubrir capítulos y procesar cada uno
    # ----------------------------------------------------
    all_dirs = [
        d for d in os.listdir(cap_dir)
        if os.path.isdir(os.path.join(cap_dir, d))
        and not d.startswith((".", "_", "comun"))
    ]
    all_dirs.sort(key=get_chapter_sort_key)

    for d in all_dirs:
        chap_path = os.path.join(cap_dir, d)
        chap_build_dir = os.path.join(build_dir, d)
        os.makedirs(chap_build_dir, exist_ok=True)

        # Garantizar .latexmkrc en la carpeta de capítulo
        chap_latexmkrc = os.path.join(chap_path, ".latexmkrc")
        if not os.path.isfile(chap_latexmkrc):
            with open(chap_latexmkrc, "w", encoding="utf-8") as f:
                f.write("do '../.latexmkrc';\n")

        # Extraer citas del capítulo
        cited_keys = set()
        tex_files = [f for f in os.listdir(chap_path) if f.endswith(".tex") and not f.startswith("borrador_")]
        for f in tex_files:
            with open(os.path.join(chap_path, f), "r", encoding="utf-8") as fp:
                for line in fp:
                    clean = re.sub(r"(?<!\\)%.*$", "", line)
                    for match in re.finditer(r"\\cite[tp]?\{([^}]+)\}", clean):
                        for k in match.group(1).split(","):
                            k = k.strip()
                            if k:
                                cited_keys.add(k)

        # Validar citas
        missing_keys = [k for k in sorted(cited_keys) if k not in bib_dict]
        if missing_keys:
            print(f"ERROR: En el capítulo '{d}', las siguientes claves citadas no tienen \\bibitem:", file=sys.stderr)
            for k in missing_keys:
                print(f"  - {k}", file=sys.stderr)
            sys.exit(1)

        # Escribir comun/bibliografia_<carpeta>.tex
        chap_bib_file = os.path.join(comun_dir, f"bibliografia_{d}.tex")
        chap_blocks = [bib_dict[k] for k in sorted(cited_keys)]
        with open(chap_bib_file, "w", encoding="utf-8") as f:
            f.write(f"% Bibliografía para {d} (solo claves citadas: {len(cited_keys)})\n")
            f.write("\\begin{thebibliography}{99}\n")
            if chap_blocks:
                f.write("\n\n".join(chap_blocks) + "\n")
            f.write("\\end{thebibliography}\n")

        # Generar <carpeta>/borrador_<carpeta>.tex
        sorted_subfiles = natural_sort_files(tex_files)
        sec_num_match = re.match(r"^(\d+)", d)
        
        borrador_lines = [
            "% ============================================================",
            f"% borrador_{d}.tex — Borrador independiente de {d}",
            "% Generado automáticamente por compilar_borradores.sh. No editar a mano.",
            f"% Compilación: cd Docs/capitulos/{d} && latexmk -pdf borrador_{d}.tex",
            "% ============================================================",
            "\\input{../comun/preambulo}",
            f"\\externaldocument{{../_build/externo_{d}}}",
            "",
            "\\begin{document}",
            ""
        ]

        if sec_num_match:
            sec_num = int(sec_num_match.group(1))
            borrador_lines.append(f"\\setcounter{{section}}{{{sec_num - 1}}}")
            borrador_lines.append("")

        for sf in sorted_subfiles:
            borrador_lines.append(f"\\input{{{sf}}}")

        borrador_lines.append("")
        borrador_lines.append(f"\\input{{../comun/bibliografia_{d}}}")
        borrador_lines.append("")
        borrador_lines.append("\\end{document}\n")

        with open(os.path.join(chap_path, f"borrador_{d}.tex"), "w", encoding="utf-8") as f:
            f.write("\n".join(borrador_lines))

    # ----------------------------------------------------
    # 4. Generar borrador_completo.tex
    # ----------------------------------------------------
    completo_lines = [
        "% ============================================================",
        "% borrador_completo.tex — Borrador completo con todos los capítulos",
        "% Generado automáticamente por compilar_borradores.sh. No editar a mano.",
        "% ============================================================",
        "\\input{comun/preambulo}",
        "",
        "\\begin{document}",
        "",
        "\\tableofcontents",
        "\\newpage",
        ""
    ]

    for d in all_dirs:
        completo_lines.append(f"% ===== Capítulo: {d}")
        sec_num_match = re.match(r"^(\d+)", d)
        if sec_num_match:
            sec_num = int(sec_num_match.group(1))
            completo_lines.append(f"\\setcounter{{section}}{{{sec_num - 1}}}")
        
        chap_path = os.path.join(cap_dir, d)
        tex_files = [f for f in os.listdir(chap_path) if f.endswith(".tex") and not f.startswith("borrador_")]
        sorted_subfiles = natural_sort_files(tex_files)
        for sf in sorted_subfiles:
            completo_lines.append(f"\\input{{{d}/{sf}}}")
        completo_lines.append("\\newpage\n")

    completo_lines.append("% ===== Bibliografía completa")
    completo_lines.append("\\input{comun/bibliografia_completa}")
    completo_lines.append("")
    completo_lines.append("\\end{document}\n")

    with open(os.path.join(cap_dir, "borrador_completo.tex"), "w", encoding="utf-8") as f:
        f.write("\n".join(completo_lines))

    print(f"OK: Piezas compartidas y borradores generados para {len(all_dirs)} capítulos.")

if __name__ == "__main__":
    main()
