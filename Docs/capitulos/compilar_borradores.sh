#!/usr/bin/env bash
# ============================================================
# compilar_borradores.sh — TT 2026-B039
# Compilación automatizada de borradores independientes por capítulo
# y borrador completo del Trabajo Terminal.
#
# Uso:
#   bash Docs/capitulos/compilar_borradores.sh
#   bash Docs/capitulos/compilar_borradores.sh 5_Metodologia 6_Resultados
# ============================================================
set -euo pipefail

export PATH="/Library/TeX/texbin:$PATH"
DOCS="$(cd "$(dirname "$0")/.." && pwd)"
CAP="$DOCS/capitulos"
BUILD="$CAP/_build"
COMUN="$CAP/comun"

# Seleccionar intérprete de Python (prioriza el que contiene PyMuPDF fitz)
PYTHON="python3"
if [ -x "/opt/anaconda3/bin/python" ]; then
    PYTHON="/opt/anaconda3/bin/python"
elif [ -x "/opt/anaconda3/envs/qml_cancer/bin/python" ]; then
    PYTHON="/opt/anaconda3/envs/qml_cancer/bin/python"
fi

mkdir -p "$BUILD" "$COMUN"

echo "============================================================"
echo "1. Regenerando comun/, borradores y borrador_completo.tex..."
echo "============================================================"
"$PYTHON" "$COMUN/generar_piezas.py"

echo "============================================================"
echo "2. Compilando borrador_completo.tex..."
echo "============================================================"
(
    cd "$CAP"
    latexmk -pdf -interaction=nonstopmode -halt-on-error borrador_completo.tex
) || {
    echo "ERROR: Falló la compilación de borrador_completo.tex" >&2
    if [ -f "$BUILD/borrador_completo.log" ]; then
        echo "Últimas líneas del log:" >&2
        grep -n -A4 '^!' "$BUILD/borrador_completo.log" | head -40 >&2 || true
    fi
    exit 1
}

echo "============================================================"
echo "3. Generando archivos .aux filtrados para referencias cruzadas..."
echo "============================================================"
"$PYTHON" "$COMUN/generar_aux_externo.py"

# Determinar qué capítulos compilar
if [ "$#" -eq 0 ]; then
    CHAPS=$(cd "$CAP" && ls -d [0-9]*_*/ A_*/ 2>/dev/null | sed 's#/##' | grep -v '^comun' | grep -v '^_build')
else
    CHAPS="$@"
fi

echo "============================================================"
echo "4. Compilando borradores por capítulo: $CHAPS"
echo "============================================================"
for chap in $CHAPS; do
    echo "--- Compilando $chap/borrador_${chap}.tex ---"
    (
        cd "$CAP/$chap"
        latexmk -pdf -interaction=nonstopmode -halt-on-error "borrador_${chap}.tex"
    ) || {
        echo "ERROR: Falló la compilación de $chap/borrador_${chap}.tex" >&2
        LOG_P="$BUILD/$chap/borrador_${chap}.log"
        [ -f "$LOG_P" ] || LOG_P="$BUILD/borrador_${chap}.log"
        if [ -f "$LOG_P" ]; then
            echo "Últimas líneas del log:" >&2
            grep -n -A4 '^!' "$LOG_P" | head -40 >&2 || true
        fi
        exit 1
    }
done

echo "============================================================"
echo "5. Verificación de literalidad de §2..."
echo "============================================================"
"$PYTHON" "$COMUN/verificar_literal_s2.py"

echo "============================================================"
echo "6. Resumen de compilación y aceptación de documentos..."
echo "============================================================"
"$PYTHON" "$COMUN/analizar_logs.py"

echo "Compilación de borradores finalizada exitosamente."
