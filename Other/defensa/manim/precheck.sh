#!/bin/sh
# Precheck de la automatización «TT ronda 4: retomar si se corta la sesión».
# Sale con 0 (correr) solo si el trabajo sigue EN CURSO y ESTADO.md lleva más de 75 minutos
# sin actualizarse, señal de que la sesión que coordinaba se quedó sin cuota o se cerró.
# Sale con 1 (no correr) en cualquier otro caso.
E="$(dirname "$0")/ESTADO.md"
[ -f "$E" ] || exit 1
grep -q '^ESTADO: EN CURSO' "$E" || exit 1
edad=$(( $(date +%s) - $(stat -f %m "$E") ))
[ "$edad" -gt 4500 ] || exit 1
exit 0
