# Fuentes del cronograma TT 2026-B039

Archivo: [`cronograma.tex`](cronograma.tex). Las fechas de TT2 son fechas de registro en la bitácora y en Git, no fechas de un plan.

## Panel TT1 · enero a mayo de 2026

La fuente es `Docs/Figures/cronograma.jpeg`; la escala mensual se expresa como el primer y el último día del mes sombreado. Las once barras conservan las fechas ya usadas en el reporte de TT1.

| Barra | Inicio | Fin | Fuente |
|---|---:|---:|---|
| 1. Requerimientos técnicos | 2026-01-01 | 2026-01-31 | imagen `cronograma.jpeg`, ENE |
| 1. Revisión bibliográfica QC/QML/mama | 2026-01-01 | 2026-01-31 | imagen `cronograma.jpeg`, ENE |
| 1. Revisión del dataset y sus atributos | 2026-01-01 | 2026-02-28 | imagen `cronograma.jpeg`, ENE--FEB |
| 1. Pipeline cuántico-clásico (definición) | 2026-02-01 | 2026-02-28 | imagen `cronograma.jpeg`, FEB |
| 2. Limpieza y preparación del dataset | 2026-02-01 | 2026-02-28 | imagen `cronograma.jpeg`, FEB |
| 2. Visualización y análisis exploratorio | 2026-03-01 | 2026-03-31 | imagen `cronograma.jpeg`, MAR |
| 3. Selección del método de encoding | 2026-03-01 | 2026-03-31 | imagen `cronograma.jpeg`, MAR |
| 3. Diseño matemático de la transformación | 2026-03-01 | 2026-04-30 | imagen `cronograma.jpeg`, MAR--ABR |
| 3. Pruebas en simulador | 2026-03-01 | 2026-04-30 | imagen `cronograma.jpeg`, MAR--ABR |
| Evaluación TT1 | 2026-04-01 | 2026-05-31 | imagen `cronograma.jpeg`, ABR--MAY |
| 7. Documentación y reporte de TT1 | 2026-01-01 | 2026-05-31 | imagen `cronograma.jpeg`; tramo del panel TT1 |

## Panel TT2 · 24 de agosto a 17 de noviembre de 2026

| Barra | Inicio | Fin | Fuente |
|---|---:|---:|---|
| F2 · Desbloqueo de entorno y datos | 2026-08-24 | 2026-09-23 | Bitácora: H-001 (24 ago), D-012 (21 sep), H-029 (23 sep) |
| F3 · Benchmark y verificaciones de diseño (B1--B3) | 2026-09-21 | 2026-09-24 | Bitácora: H-011--H-019 (21--23 sep), D-013--D-018 (22 sep); últimos commits B1--B3 (24 sep) |
| M2 · Preprocesamiento | 2026-09-23 | 2026-09-23 | Bitácora: D-020--D-022 y H-020--H-022 |
| M3 · Extracción de características | 2026-09-23 | 2026-09-24 | Bitácora: D-023 y H-023--H-025; commits del 23 y 24 sep |
| M4 · Selección y escalado | 2026-09-23 | 2026-09-24 | Bitácora: D-024--D-026 y H-026--H-028; commits del 23 y 24 sep |
| M5 · Transformación cuántica | 2026-09-24 | 2026-09-24 | Bitácora: D-027--D-030 y H-031--H-034 |
| X1--X2 y C5 = (Y, ZZ) | 2026-10-04 | 2026-10-05 | Bitácora: H-035, H-036 (4 oct), D-031 y H-037 (5 oct) |
| M6 · Separabilidad y X3 | 2026-10-06 | 2026-10-06 | Bitácora: D-032--D-035 y H-038--H-041 |
| M7 · Clasificación | 2026-10-06 | 2026-10-06 | Bitácora: D-036, D-037, H-042 y H-043 |
| X4--X6 · Exploratorios | 2026-10-07 | 2026-10-07 | Bitácora: D-038 y H-044--H-048 |
| M8 · Evaluación comparativa | 2026-10-07 | 2026-10-07 | Bitácora: D-039, D-040 y H-049--H-052 |
| Revisión, re-ejecución y X7--X8 | 2026-10-08 | 2026-10-11 | Bitácora: H-053 (10 oct) y H-054 (11 oct) |
| F7 · Redacción del reporte técnico | 2026-10-12 | 2026-10-20 | `Other/plan_trabajo.html`, 12--20 oct |
| F7 · Revisión de los directores | 2026-10-21 | 2026-10-23 | `Other/plan_trabajo.html`, 21--23 oct |
| F7 · Correcciones de la revisión | 2026-10-24 | 2026-11-02 | `Other/plan_trabajo.html`, 24 oct--2 nov |
| F7 · INDAUTOR y presentación (ventana) | 2026-10-21 | 2026-11-03 | `Other/plan_trabajo.html`: «Del 21 oct al 3 nov quedan la revisión de los directores, las correcciones, INDAUTOR y la presentación» |
| Hito: reporte completo | 2026-10-20 | 2026-10-20 | `Other/plan_trabajo.html` |
| Hito: congelamiento | 2026-10-23 | 2026-10-23 | `Other/plan_trabajo.html` |
| Hito: entrega a sinodales | 2026-11-03 | 2026-11-03 | `Other/plan_trabajo.html` |
| Hito: abre ventana de presentaciones | 2026-11-17 | 2026-11-17 | `Other/plan_trabajo.html` |

## Notas de la revisión del coordinador (2026-10-11)

- M1 y el EDA no aparecen en TT2: se hicieron en TT1 (`Code/1_EDA.ipynb`, commits del 27 abr y 4 may de 2026).
- La fila «Normalización y selección de características» del plan de TT1 (FEB–MAR) no se dibuja en el panel TT1: se hizo en TT2 como M4 (23 sep).
- El eje de TT2 llega al 19 nov solo para que el rombo del 17 nov quepa dentro del gráfico; ninguna fecha se movió.
- Compila con pdflatex sin errores ni *Overfull* en carta con márgenes de 2.5 cm. Para incluirlo: `\begin{figure}[H]\centering\input{insumos/cronograma}\caption{…}\end{figure}`, con `\usepackage{pgfgantt}` en el preámbulo.
