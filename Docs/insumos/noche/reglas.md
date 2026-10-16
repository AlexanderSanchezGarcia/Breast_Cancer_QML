# Reglas comunes · trabajo nocturno 2026-10-14

Repositorio: `/Users/alexander_san/TT`. Tesis de licenciatura (ESCOM-IPN) sobre transformaciones cuánticas variacionales aplicadas a features radiómicas del CBIS-DDSM. Lee `CLAUDE.md` en la raíz antes de empezar: describe el proyecto, las decisiones cerradas (D-xxx) y los hallazgos (H-xxx). El registro canónico es `Other/bitacora_decisiones.md`.

## Prohibido

1. **No edites** `Docs/Technical_Report.tex`, `Docs/Technical_Report.bib`, `Other/bitacora_decisiones.md`, `CLAUDE.md`, los notebooks (`*.ipynb`) ni nada de `Data/`.
2. **No hagas commits**, ni `git add`, ni `git mv`, ni `git checkout`/`reset`/`stash`. El coordinador revisa y versiona.
3. **Escribe solo en los archivos y carpetas que tu especificación te asigna.** Otros trabajadores escriben en paralelo en otras carpetas.
4. **No inventes nada.** Ni cifras, ni citas, ni páginas, ni autores, ni años, ni firmas de funciones. Si algo no está en una fuente que puedas abrir, escribe `[VERIFICAR: motivo]` en su lugar. Un `[VERIFICAR]` honesto vale más que un dato plausible: un dato inventado en una tesis es una falta grave.
5. **No reformules el proyecto como un benchmark de rendimiento.** El objetivo es la viabilidad y la separabilidad; un resultado negativo es evidencia válida (regla 1 de `CLAUDE.md`).
6. **No pidas confirmación al usuario ni abras diálogos interactivos.** Si una duda te bloquea, usa el comando `ask` de tu preámbulo de Orca; si no te bloquea, decide lo más conservador y anótalo en tu informe.

## Fuentes

- PDF: `Docs/fuentes/pdf/<Clave>.pdf`. Texto por página: `Docs/fuentes/txt/<Clave>/pNNN.txt` (NNN = página del **archivo PDF**, empezando en 001; no es la paginación impresa de la revista). Lee el texto con `cat`/`grep` sobre esos `.txt`.
- Metadatos bibliográficos verificados: `Docs/insumos/bibitems_nuevos.tex` y `Docs/insumos/bibitems_noche.tex`. Usa **solo** las claves que aparecen ahí o en el `\begin{thebibliography}` de `Docs/Technical_Report.tex`. No crees `\bibitem` nuevos: si necesitas una referencia que no está, escribe `[VERIFICAR: falta referencia a …]`.
- Cifras del proyecto: la bitácora (`Other/bitacora_decisiones.md`) y los CSV de `Code/results/`. Cada cifra que escribas en un `.tex` debe ir en un párrafo precedido de un comentario `% fuente: H-0xx, D-0xx; archivo.csv` (así lo comprueba `Code/tools/verificar_cifras_capitulos.py`).

## Cómo citar literalmente

- En las fichas (`Docs/insumos/fichas/<Clave>.md`): `«texto literal en el idioma original» (p. N)` o `(pp. N–M)`.
- En cualquier otro archivo: `«texto literal» (Clave, p. N)`. En un `.tex`, como comentario: `% respaldo: «texto literal» (Clave, p. N)`.
- La cita debe ser **copia exacta** del texto del `.txt` (puedes saltarte saltos de línea y guiones de corte de línea; nada más). Máximo dos oraciones por cita. **No traduzcas dentro de las comillas.**
- `python3 Code/tools/verificar_citas_fichas.py <archivo o carpeta>` comprueba cada cita contra la página declarada. Tu trabajo no está terminado hasta que pase sin fallos.

## LaTeX

- Español académico formal, en tercera persona o impersonal. Sin anglicismos innecesarios; los términos técnicos en inglés van en `\textit{}` la primera vez.
- Cifras con punto decimal y `\,` como separador de miles en el texto (`1\,318`), como en los capítulos existentes.
- **Lenguaje calibrado**: «muestra», «indica», «es consistente con» cuando la evidencia es descriptiva; «demuestra» o «confirma» solo con una prueba formal significativa. Nunca «sin excepción», «estrictamente» o «de manera contundente» si el dato no lo exige. Nunca «ventaja cuántica» como algo observado aquí: no la hubo.
- No muestres identificadores internos D-xxx ni H-xxx en el texto visible ni en los pies; van solo en los comentarios `% fuente:`.
- Cada archivo nuevo empieza con una cabecera de comentario: qué es, qué sección del reporte ocupa y qué entradas de la bitácora lo respaldan (mira cualquier archivo de `Docs/capitulos/6_Resultados/` como modelo).
- Prueba de compilación: `bash Docs/capitulos/compilar_prueba.sh <carpeta>` (las carpetas `A_Anexos` y `2_Antecedentes` hay que pasarlas por nombre). Debe decir «Compila sin errores» y «Referencias o citas sin resolver: ninguna».
- El código del Anexo A se incluye con `\lstinputlisting[style=tt, caption={…}, label={lst:…}]{codigo/<nombre>.py}`. El estilo `tt` ya está definido en `Docs/insumos/preambulo_extra.tex`.

## Python

- `python3` del sistema es 3.9 y no tiene numpy. Para scripts que lean CSV con pandas usa `/opt/anaconda3/envs/qml_cancer/bin/python`.
- `verificar_cifras_capitulos.py` se corre con `/opt/anaconda3/envs/qml_cancer/bin/python`.

## Al terminar

1. Corre todas tus pruebas de aceptación y copia su salida final en tu informe.
2. Escribe tu informe en `Docs/insumos/noche/informe_<TU_TAREA>.md`: qué hiciste, qué archivos creaste o cambiaste, la salida de las pruebas, cada `[VERIFICAR]` que dejaste y por qué, y lo que no pudiste hacer. **No declares «todo verificado» si alguna prueba falló o no la corriste.**
3. Envía `worker_done` según tu preámbulo de Orca, con `--report-path` apuntando a tu informe.
