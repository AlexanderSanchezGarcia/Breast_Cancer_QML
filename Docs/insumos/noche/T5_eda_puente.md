# T5 · El EDA como capítulo 4, puente hacia la Metodología

Lee primero `Docs/insumos/noche/reglas.md`.

## Contexto

El autor decidió mover el Análisis Exploratorio de Datos **antes** de la Metodología. El orden del reporte queda: 1 Panorama general, 2 Antecedentes, 3 Marco teórico, **4 EDA**, **5 Metodología**, 6 Resultados, 7 Conclusiones. Las carpetas ya se renombraron: `Docs/capitulos/4_EDA/` (archivos `4.0_…` a `4.5_…`) y `Docs/capitulos/5_Metodologia/` (`5.0_…` a `5.10_…`). Los `\section`/`\subsection` se numeran solos; los textos escritos a mano («sección 4.3», «§5», «capítulo anterior») no.

El EDA ya no es «el trabajo de TT1»: es la caracterización de los datos que **justifica** las decisiones de diseño del capítulo 5. El lector debe terminar el capítulo 4 sabiendo por qué la Metodología hace lo que hace.

## Tú escribes solo en

- `Docs/capitulos/4_EDA/*.tex` (los existentes y nuevos con prefijo `4.`).
- `Docs/capitulos/A_Anexos/A.3.2_figuras_eda.tex` (figuras del EDA que salen del cuerpo).
- `Docs/insumos/referencias_cruzadas.md` (informe de referencias escritas a mano en **otras** carpetas; no las edites tú).

## Cambios

1. **`4.0_introduccion.tex`**: reescribe la introducción como puente. Qué datos se caracterizan, con qué preguntas, y que los hallazgos condicionan el diseño del capítulo~\ref{sec:metodologia}. Si `5_Metodologia/5.0_introduccion.tex` no tiene `\label{sec:metodologia}` tras su `\section`, **no lo añadas tú**: anótalo en tu informe y usa el texto «el capítulo de Metodología».
2. **Cabeceras**: en cada archivo de `4_EDA/`, la cabecera de comentario dice qué líneas de `Technical_Report.tex` reemplaza; añade una línea `% Capítulo 4 desde el 2026-10-14 (antes §5).`
3. **`4.5_hallazgos.tex` → «Implicaciones para el diseño»**: conserva los hallazgos, pero termina con una tabla (`booktabs`) de tres columnas: *Hallazgo del EDA* | *Decisión de diseño* | *Dónde se aplica* (con `\ref` a la subsección de la Metodología, p. ej. `\ref{…}`; busca las etiquetas existentes con `grep -n '\\label' Docs/capitulos/5_Metodologia/*.tex`). Filas mínimas, verificando cada una en `CLAUDE.md` y la bitácora:
   - masas y calcificaciones con morfología y desbalance distintos → subproblemas independientes en todo el pipeline;
   - desbalance 1.16:1 en masas y 1.78:1 en calcificaciones → ponderación de clases en la pérdida;
   - `breast_density` y `subtlety` sin correlación con la patología → la información está en la imagen → features radiómicas (M3);
   - mamografías de ~5\,037×2\,960 px → recorte de la ROI y extracción de features, no la imagen al circuito;
   - `PixelSpacing` ausente en todos los DICOM → features de forma en píxeles, sin escala física (limitación);
   - 80 máscaras con dimensiones distintas → alineación en M2 (dos tipos);
   - todas `MONOCHROME2`, 16 bits → sin inversión, `binCount=32` en vez de ancho fijo;
   - estructura por paciente → folds agrupados por paciente.
   Cada fila con su `% fuente:` en un comentario encima de la tabla. Las cifras, solo las que estén en `CLAUDE.md`/bitácora o en los propios archivos del EDA.
4. **Acortar**: el capítulo tiene 14 figuras. Deja en el cuerpo las que sostienen una fila de la tabla anterior (como mínimo `B2_imbalance_by_finding`, `C3_mass_morphology`, `C4_calc_morphology`, `C5_correlation_matrix`, `D1_image_dimensions`, `D5_roi_overlays`) y mueve las demás a `A.3.2_figuras_eda.tex`, como `\subsection{Figuras del análisis exploratorio}` con las mismas leyendas y etiquetas. En el cuerpo, donde estaba una figura movida, deja una frase con `\ref` a ella («véase la Figura~\ref{…} del Anexo~\ref{…}»). No borres texto de análisis; solo mueve figuras.
5. **Referencias escritas a mano**: `grep -rnE '(sección|Sección|capítulo|Capítulo|§) ?[0-9]' Docs/capitulos/` y en `Other/bitacora_decisiones.md`. Corrige las que estén en `4_EDA/`. Para las demás, escribe en `Docs/insumos/referencias_cruzadas.md` una tabla: archivo, línea, texto, a qué apunta ahora, propuesta (`\ref{…}` o número nuevo). En la bitácora, no propongas reescribir entradas: el coordinador añadirá una nota de equivalencias.

## Aceptación

- `bash Docs/capitulos/compilar_prueba.sh 4_EDA 5_Metodologia A_Anexos` compila sin errores y sin referencias sin resolver (si `A_Anexos` aún no existe completo porque otro trabajador lo está escribiendo, compila `4_EDA 5_Metodologia` y anota el resultado; cualquier `\ref` a tus figuras de `A.3.2` debe resolverse en la compilación con `A_Anexos`).
- `/opt/anaconda3/envs/qml_cancer/bin/python Code/tools/verificar_cifras_capitulos.py Docs/capitulos/4_EDA` sin `NO_ENCONTRADO` nuevos respecto a la línea base (córrelo antes de empezar y guarda la salida en tu informe).
- Informe en `Docs/insumos/noche/informe_T5.md`.
