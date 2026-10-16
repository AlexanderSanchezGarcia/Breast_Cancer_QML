#!/usr/bin/env python3
r"""
verificar_literal_s2.py — Verificación de copia literal de §2 de Technical_Report.tex.
Comprueba que los archivos de Docs/capitulos/2_Antecedentes/ coincidan línea a línea
con los rangos correspondientes del reporte original, tras omitir cabeceras de comentario
y la etiqueta añadida \label{sec:antecedentes}.
"""
import os
import sys

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    tr_path = os.path.join(repo_root, "Docs/Technical_Report.tex")
    sec2_dir = os.path.join(repo_root, "Docs/capitulos/2_Antecedentes")

    if not os.path.isfile(tr_path):
        print(f"ERROR: No se encontró {tr_path}", file=sys.stderr)
        sys.exit(1)

    with open(tr_path, "r", encoding="utf-8") as f:
        tr_lines = f.readlines()

    checks = [
        ("2.0_introduccion.tex", 692, 700, True),
        ("2.1.1_ml_clasico.tex", 701, 725, False),
        ("2.1.2_deep_learning.tex", 726, 750, False),
        ("2.1.3_fundamentos_qml.tex", 751, 798, False),
        ("2.1.4_hibridos_salud.tex", 799, 814, False),
        ("2.1.5_cbis_ddsm.tex", 815, 830, False),
    ]

    total_diffs = 0
    print("=" * 65)
    print("Verificación de literalidad de §2 (Technical_Report.tex vs 2_Antecedentes)")
    print("=" * 65)

    for filename, start_l, end_l, has_added_label in checks:
        file_path = os.path.join(sec2_dir, filename)
        if not os.path.isfile(file_path):
            print(f"FAIL: Archivo faltante {filename}")
            total_diffs += 1
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            f_lines = f.readlines()

        # Remove header comment lines (from start until first non-comment line)
        idx = 0
        while idx < len(f_lines) and f_lines[idx].strip().startswith("%"):
            idx += 1
        # Also skip leading blank lines right after header
        while idx < len(f_lines) and f_lines[idx].strip() == "":
            idx += 1

        body_lines = f_lines[idx:]

        # If has_added_label, remove \label{sec:antecedentes}
        if has_added_label:
            body_lines = [l for l in body_lines if l.strip() != "\\label{sec:antecedentes}"]

        expected_lines = tr_lines[start_l - 1 : end_l]

        diffs = []
        if len(body_lines) != len(expected_lines):
            diffs.append(f"Número de líneas diferente: obtenido {len(body_lines)}, esperado {len(expected_lines)}")
        else:
            for line_no, (got, exp) in enumerate(zip(body_lines, expected_lines), start=start_l):
                if got != exp:
                    diffs.append(f"Línea {line_no}:\n  obtenido: {repr(got)}\n  esperado: {repr(exp)}")

        if not diffs:
            print(f"OK   {filename:<26} (líneas {start_l:3d}–{end_l:3d}, {len(expected_lines):2d} líneas coincidentes)")
        else:
            print(f"FAIL {filename:<26} (líneas {start_l:3d}–{end_l:3d}):")
            for d in diffs[:5]:
                print(f"     {d}")
            total_diffs += len(diffs)

    # Check 2.1.6_tabla_ampliada.tex lines 831-838
    t6_path = os.path.join(sec2_dir, "2.1.6_tabla_ampliada.tex")
    if os.path.isfile(t6_path):
        with open(t6_path, "r", encoding="utf-8") as f:
            t6_content = f.read()
        expected_t6 = "".join(tr_lines[830:838])
        if expected_t6 in t6_content:
            print(f"OK   2.1.6_tabla_ampliada.tex   (líneas 831–838 previas a landscape: coincidencia exacta)")
        else:
            print(f"FAIL 2.1.6_tabla_ampliada.tex   (líneas 831–838 no coinciden literalmente)")
            total_diffs += 1
    else:
        print(f"FAIL 2.1.6_tabla_ampliada.tex   (no encontrado)")
        total_diffs += 1

    print("-" * 65)
    if total_diffs == 0:
        print("Resultado: ÉXITO COMPLETO — Todas las líneas coinciden literalmente.")
        return 0
    else:
        print(f"Resultado: FALLO — Se encontraron {total_diffs} discrepancias.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
