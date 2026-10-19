# Reglas comunes · auditoría final del reporte, noche del 2026-10-18/19

Repositorio: `/Users/alexander_san/TT`. Tesis de licenciatura (ESCOM-IPN, TT 2026-B039) sobre transformaciones cuánticas variacionales aplicadas a características radiómicas del CBIS-DDSM. Lee `CLAUDE.md` en la raíz antes de empezar: describe el proyecto, las decisiones cerradas (D-xxx) y los hallazgos (H-xxx). El registro canónico de cifras y decisiones es `Other/bitacora_decisiones.md`.

**Esta noche es una auditoría de SOLO LECTURA.** El reporte ya está integrado: `Docs/Technical_Report.tex` incluye, con `\input`, los capítulos de `Docs/capitulos/<N>_<Nombre>/*.tex` y la bibliografía `Docs/bibliografia.tex`. El PDF compilado está en `Docs/Technical_Report.pdf` (195 páginas). Tu trabajo es **encontrar problemas y documentarlos**, no corregirlos.

## Prohibido

1. **No edites ningún archivo** salvo tu informe (`Docs/insumos/auditoria/informe_<TAREA>.md`) y, si tu especificación lo dice, un archivo de trabajo propio en `Docs/insumos/auditoria/`. Nada de `.tex`, `.md`, `.py`, `.ipynb` ni `.csv` ajenos.
2. **No hagas commits** ni `git add`, `git mv`, `git checkout`, `git reset`, `git stash`.
3. **No inventes nada.** Cada hallazgo debe citar el archivo y la línea (`Docs/capitulos/6_Resultados/6.2_separabilidad.tex:41`) y copiar literalmente el texto problemático. Si afirmas que una cifra no coincide con un CSV, copia la fila del CSV y el nombre exacto de la columna. Si no puedes comprobar algo, escríbelo como `[NO VERIFICADO: motivo]`. Un hallazgo inventado es peor que un hallazgo omitido: el coordinador verifica cada uno y descarta el informe entero si encuentra uno fabricado.
4. **No reformules el proyecto como un benchmark de rendimiento.** El objetivo es la viabilidad y la separabilidad; un resultado negativo es evidencia válida (regla 1 de `CLAUDE.md`).
5. **No pidas confirmación al usuario ni abras diálogos interactivos.** Si una duda te bloquea, usa el comando `ask` de tu preámbulo de Orca; si no te bloquea, decide lo más conservador y anótalo.
6. **No resumas con cifras propias.** Tu informe no lleva una sección de «resumen ejecutivo» con números agregados; solo la lista de hallazgos y un conteo por severidad.

## Formato de cada hallazgo

```
### <ID>-<n> · <severidad: ALTA | MEDIA | BAJA> · <categoría>
- Ubicación: `ruta/al/archivo.tex:línea`
- Texto: «copia literal del fragmento»
- Problema: una o dos oraciones.
- Evidencia: lo que lo demuestra (otra línea del reporte, fila de CSV, entrada de la bitácora, página de la fuente).
- Propuesta: corrección sugerida, sin reescribir párrafos enteros.
```

Severidad: **ALTA** = error de contenido (cifra, cita, afirmación falsa, contradicción entre secciones, referencia rota); **MEDIA** = incoherencia o ambigüedad que un sinodal señalaría; **BAJA** = estilo o forma.

## Herramientas

- Python con pandas: `/opt/anaconda3/envs/qml_cancer/bin/python`. El `python3` del sistema no tiene numpy.
- LaTeX: `export PATH="/Library/TeX/texbin:$PATH"`. Si compilas, hazlo **fuera del repositorio**: `pdflatex -interaction=nonstopmode -output-directory /tmp/aud_<TAREA> Technical_Report.tex` desde `Docs/` (dos pasadas).
- Texto de las fuentes por página: `Docs/fuentes/txt/<Clave>/pNNN.txt`. Fichas de lectura verificadas: `Docs/insumos/fichas/<Clave>.md`.
- Verificadores existentes: `Code/tools/verificar_cifras_capitulos.py <carpeta>`, `Code/tools/verificar_citas_fichas.py <archivo|carpeta>`.

## Al terminar

1. Escribe `Docs/insumos/auditoria/informe_<TAREA>.md` con: alcance revisado, comandos que corriste y su salida final, la lista de hallazgos en el formato de arriba y el conteo por severidad.
2. Corre `git -C /Users/alexander_san/TT status --short` y confirma en el informe que solo creaste archivos dentro de `Docs/insumos/auditoria/`.
3. Envía `worker_done` según tu preámbulo de Orca, con `--report-path` apuntando a tu informe.
