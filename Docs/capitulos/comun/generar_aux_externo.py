#!/usr/bin/env python3
"""
generar_aux_externo.py — TT 2026-B039
Genera _build/externo_<carpeta>.aux a partir de _build/borrador_completo.aux,
filtrando las etiquetas definidas en cada capítulo para evitar avisos de duplicado.
Detecta etiquetas tanto de \\label{...} como de label={...} en listings y tablas.
"""
import os
import sys
import re
import glob

def get_labels_defined_in_files(file_paths):
    labels = set()
    for fp in file_paths:
        if not os.path.isfile(fp):
            continue
        with open(fp, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                clean = re.sub(r"(?<!\\)%.*$", "", line)
                # Standard \label{...}
                for m in re.finditer(r"\\label\{([^}]+)\}", clean):
                    labels.add(m.group(1).strip())
                # Listings label={...} or label=...
                for m in re.finditer(r"\blabel\s*=\s*\{?([a-zA-Z0-9_:\-]+)", clean):
                    labels.add(m.group(1).strip())
    return labels

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    docs_dir = os.path.join(repo_root, "Docs")
    cap_dir = os.path.join(docs_dir, "capitulos")
    build_dir = os.path.join(cap_dir, "_build")

    completo_aux = os.path.join(build_dir, "borrador_completo.aux")
    if not os.path.isfile(completo_aux):
        print(f"ERROR: {completo_aux} no existe. Compila borrador_completo primero.", file=sys.stderr)
        sys.exit(1)

    with open(completo_aux, "r", encoding="utf-8", errors="ignore") as f:
        aux_lines = f.readlines()

    all_dirs = [
        d for d in os.listdir(cap_dir)
        if os.path.isdir(os.path.join(cap_dir, d))
        and not d.startswith((".", "_", "comun"))
    ]

    for d in all_dirs:
        chap_dir = os.path.join(cap_dir, d)
        chap_build_dir = os.path.join(build_dir, d)
        os.makedirs(chap_build_dir, exist_ok=True)

        # 1. Encontrar archivos del capítulo
        tex_files = [
            os.path.join(chap_dir, f)
            for f in os.listdir(chap_dir)
            if f.endswith(".tex") and not f.startswith("borrador_")
        ]

        # 2. Encontrar tablas o archivos referenciados por este capítulo
        referenced_files = []
        for tf in tex_files:
            with open(tf, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    clean = re.sub(r"(?<!\\)%.*$", "", line)
                    for m in re.finditer(r"\\(?:input|lstinputlisting)(?:\[[^\]]*\])?\{([^}]+)\}", clean):
                        inp = m.group(1).strip()
                        # Posibles rutas
                        candidates = [
                            os.path.join(docs_dir, inp),
                            os.path.join(docs_dir, inp + ".tex"),
                            os.path.join(chap_dir, inp),
                            os.path.join(chap_dir, inp + ".tex"),
                        ]
                        for c in candidates:
                            if os.path.isfile(c):
                                referenced_files.append(c)

        own_labels = get_labels_defined_in_files(tex_files + referenced_files)

        # 3. Filtrar borrador_completo.aux
        ext_lines = ["\\relax\n"]
        for line in aux_lines:
            m = re.match(r"^\\newlabel\{([^}]+)\}", line)
            if m:
                lbl = m.group(1).strip()
                # subcaption define además sub@<etiqueta> para cada subfigura propia
                base = lbl[4:] if lbl.startswith('sub@') else lbl
                if base not in own_labels:
                    ext_lines.append(line)

        out_aux_1 = os.path.join(build_dir, f"externo_{d}.aux")
        out_aux_2 = os.path.join(chap_build_dir, f"externo_{d}.aux")

        with open(out_aux_1, "w", encoding="utf-8") as f:
            f.writelines(ext_lines)
        with open(out_aux_2, "w", encoding="utf-8") as f:
            f.writelines(ext_lines)

    print(f"OK: Archivos aux externos generados para {len(all_dirs)} capítulos.")

if __name__ == "__main__":
    main()
