# T9 · Verificar contra la fuente las cifras de §1.1 (fuentes web y epidemiológicas)

Lee primero `Docs/insumos/noche/reglas.md`. Todas sus prohibiciones siguen vigentes. Esta tarea es de **verificación**: no escribes texto del reporte, solo descargas fuentes y produces un informe.

## Contexto

La introducción del reporte (§1.1, `Docs/Technical_Report.tex`, líneas 476–569) usa cifras epidemiológicas y clínicas tomadas de páginas web y de algunos artículos. La auditoría (`Docs/insumos/auditoria_s1_s2.md`, §1.1.1 y §1.1.2) encontró citas dudosas: blogs de clínicas, notas de prensa y una cifra atribuida a la American Cancer Society que cita a otra fundación. El coordinador está reescribiendo §1.1 y necesita saber, para cada cifra, **qué dice exactamente la fuente**.

## Tú escribes solo en

- `Docs/fuentes/pdf/<Clave>.pdf` y `Docs/fuentes/web/<Clave>.html` para las fuentes que descargues.
- `Docs/fuentes/txt/<Clave>/pNNN.txt`: el texto por página, con la misma convención que las demás fuentes. NNN es la página del archivo PDF, desde 001. Para una página HTML, un solo `p001.txt` con el texto visible.
- `Docs/insumos/noche/informe_T9.md`.

No toques ningún `.tex` ni la bibliografía, y no crees `\bibitem`.

## Afirmaciones a verificar

Para cada una: descarga la fuente citada (con `curl -L`, o como puedas), extrae el texto y busca el pasaje que respalda o contradice la cifra.

| # | Afirmación del reporte | Clave citada (URL en el `\bibitem` de `Technical_Report.tex`) |
|---|---|---|
| 1 | GLOBOCAN 2022: unos 2.3 millones de casos nuevos de cáncer de mama y unas 670,000 defunciones en el mundo en 2022 | `Bray2024GLOBOCAN` (DOI 10.3322/caac.21834; es de acceso abierto). Compara también con `GLOBOCAN2022` (Freihat et al. 2025) |
| 2 | Es el cáncer más diagnosticado en mujeres y la principal causa de muerte por cáncer en mujeres | `Bray2024GLOBOCAN`, `WHO2025` |
| 3 | Uno de cada cuatro cánceres en mujeres; desde 2008 la incidencia subió más del 20 % y la mortalidad un 14 % | `BCRF2025`. Busca además una fuente primaria (OMS o IARC) con esas cifras |
| 4 | Para 2050, los casos nuevos aumentarán más del 50 % y las defunciones más del 70 % | `StopBreastCancer2025`. Compáralo con `Kim2025GlobalBreastCancer` (Nature Medicine, 2025) y con `GLOBOCAN2022`, y anota las cifras exactas de cada una |
| 5 | En países de bajos ingresos la mortalidad puede ser el doble que en países desarrollados, con menor incidencia | `GlobalCancerStatistics2024` |
| 6 | México, 2024: unas 8,500 (u 8,451) defunciones por cáncer de mama, el 99.2 % mujeres, tasa de 18.7 por 100,000 mujeres de 20 años o más; la tasa pasó de 15.69 (2015) a 18.68 (2024) | `INEGI2025` (PDF del INEGI) y `CancerMexico2025` |
| 7 | Supervivencia relativa a cinco años del 99 % en etapa localizada y del 30 % en etapa con metástasis, «según la American Cancer Society» | `NBCF2026_EarlyDetection`. Busca la cifra de la propia ACS (*Breast Cancer Facts & Figures* o la página de la ACS) |
| 8 | Las mujeres con tamizaje regular tienen una mortalidad un 26 % menor | sin cita. Busca dónde aparece en `NBCF2026_EarlyDetection` o `Windsong2026_EarlyDetection` y una fuente primaria |
| 9 | La mamografía es el único método de tamizaje demostrado para reducir las muertes (American College of Radiology); la mortalidad bajó un 42 % entre 1989 y 2021 | `Windsong2026_EarlyDetection`. Busca la fuente primaria (ACS *Breast Cancer Facts & Figures*, ACR) y anota la cifra y el periodo exactos |
| 10 | México, 2021: 1,281 mastógrafos; el 41.1 % en instituciones de salud y seguridad social, el 36.1 % en establecimientos particulares y el 22.8 % en servicios para población sin derechohabiencia | `INEGI2023` |
| 11 | Wang et al. (2020): AUC de 0.88–0.95 en validación sobre el conjunto de entrenamiento y de 0.44–0.65 en tres conjuntos externos; cuántos modelos y cuántos conjuntos de datos | `Wang2020DeepLearning` (DOI 10.1016/j.jacr.2020.01.006). Busca la versión de arXiv |
| 12 | «La investigación futura debe enfocarse en mejorar la interpretabilidad de los modelos y garantizar su generalización para integrar el diagnóstico asistido por deep learning en programas de tamizaje» | `Kim2025GlobalBreastCancer`. **Comprueba si este artículo, que es epidemiológico, dice algo así.** Si no, dilo |
| 13 | La variabilidad entre lectores limita la precisión del diagnóstico mamográfico | Hoy cita `GlobalCancerStatistics2024_2`, una nota de prensa. Comprueba si lo dice; propón una fuente revisada por pares con cita literal, si la encuentras abierta |

## Formato del informe (`Docs/insumos/noche/informe_T9.md`)

Una tabla con una fila por afirmación y estas columnas: #, cifra del reporte, fuente consultada (URL), **cita literal** en el idioma original con página o sección, y veredicto. El veredicto es uno de:
- `COINCIDE`;
- `DIFIERE` (con el valor que da la fuente);
- `NO_ENCONTRADO` (la fuente se abrió y no lo dice);
- `NO_ACCESIBLE` (no se pudo descargar; anota el error).

Después de la tabla, para cada fuente primaria alternativa que propongas: autores, año, título, revista o institución, DOI o URL y la cita literal. El coordinador generará los `\bibitem`.

## Aceptación

1. Cada cita literal del informe tiene el formato `«…» (Clave, p. N)`, y su texto está en `Docs/fuentes/txt/<Clave>/`.
2. `python3 Code/tools/verificar_citas_fichas.py Docs/insumos/noche/informe_T9.md` pasa sin fallos.
3. Ninguna fila dice `COINCIDE` sin una cita literal verificable. Si una página web no se puede guardar, el veredicto es `NO_ACCESIBLE`, no una cifra de memoria.
4. Informe terminado y `worker_done` con `--report-path`.
