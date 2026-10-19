#!/usr/bin/env bash
# Compila los archivos de Docs/capitulos/ con el preámbulo y la bibliografía reales del reporte.
# No toca Technical_Report.tex. Uso: bash Docs/capitulos/compilar_prueba.sh [carpeta ...]
# Sin argumentos compila todas las carpetas de capítulo, en orden.
set -euo pipefail
export PATH="/Library/TeX/texbin:$PATH"
DOCS="$(cd "$(dirname "$0")/.." && pwd)"
CAP="$DOCS/capitulos"
TMP="${TMPDIR_PRUEBA:-$(mktemp -d)}"
REPORT="$DOCS/Technical_Report.tex"
if [ "$#" -eq 0 ]; then set -- $(cd "$CAP" && ls -d [0-9]*_*/ | sed 's#/##' | sort -n); fi
{
  awk '/\\begin\{document\}/{exit} {print}' "$REPORT"
  # preambulo_extra.tex ya está dentro del preámbulo del reporte desde el 2026-10-18
  grep -q 'lstdefinestyle{tt}' "$REPORT" || { [ -f "$DOCS/insumos/preambulo_extra.tex" ] && cat "$DOCS/insumos/preambulo_extra.tex"; }
  echo '\begin{document}'
  for dir in "$@"; do
    echo "% ===== $dir"
    for f in $(cd "$CAP/$dir" && ls *.tex 2>/dev/null | grep -v '^borrador_' | sort -t_ -k1,1V); do
      echo "\\input{$CAP/$dir/$f}"
    done
  done
  # Bibliografía única (TT1 + bibitems_nuevos + bibitems_noche), fusionada el 2026-10-18
  cat "$DOCS/bibliografia.tex"
  echo '\end{document}'
} > "$TMP/prueba.tex"
cd "$DOCS"
for pass in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$TMP" "$TMP/prueba.tex" > "$TMP/salida.txt" 2>&1 || {
    echo "ERROR de compilación (pasada $pass):"; grep -n -A4 '^!' "$TMP/prueba.log" | head -40; exit 1; }
done
echo "Compila sin errores. PDF: $TMP/prueba.pdf"
echo "Referencias o citas sin resolver:"
grep -E "Reference .* undefined|Citation .* undefined|multiply defined" "$TMP/prueba.log" | sort -u || echo "  ninguna"
echo "Cajas desbordadas (Overfull > 10pt):"
grep -E "Overfull \\\\hbox \(([1-9][0-9]+)" "$TMP/prueba.log" | head -20 || echo "  ninguna"
