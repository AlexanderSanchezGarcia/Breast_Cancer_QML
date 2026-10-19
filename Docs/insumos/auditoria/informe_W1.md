# Informe de auditoría y verificación · Tarea W1 (Borrador del artículo técnico IEEE)

## 1. Alcance revisado y entregables producidos

- **Fuentes revisadas (solo lectura):**
  - `CLAUDE.md`, `Docs/insumos/auditoria/reglas.md`, `Docs/insumos/auditoria/W1_articulo.md`, `Docs/insumos/noche/reglas.md`.
  - `Other/ESCOM/Ejemplo Articulo Tecnico.pdf` (formato de referencia CATT ESCOM-IPN).
  - `Docs/capitulos/0_Preliminares/resumen.tex`.
  - `Docs/capitulos/1_Panorama_General/1.1_contexto_motivacion.tex`, `1.2_planteamiento_problema.tex`, `1.3_objetivos.tex`, `1.4_preguntas_investigacion.tex`, `1.5_justificacion.tex`, `1.6_alcance_limitaciones.tex`.
  - `Docs/capitulos/5_Metodologia/5.1_diseno_experimental.tex` a `5.11_experimentos_complementarios.tex`.
  - `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex` a `6.8_sintesis.tex` y `Docs/tablas/m7_clasificacion.tex`.
  - `Docs/capitulos/7_Conclusiones/7.1_respuesta_pregunta.tex` a `7.5_trabajo_futuro.tex`.
  - `Docs/bibliografia.tex`.
- **Archivos creados (únicos archivos escritos en el repositorio):**
  - `Docs/articulo/articulo.tex` (249 líneas; clase `\documentclass[conference,letterpaper]{IEEEtran}`, dos columnas, en español, 6 páginas incluyendo las 17 referencias en formato IEEE).
  - `Docs/insumos/auditoria/informe_W1.md` (este informe).
- **Verificación de cumplimiento del formato y contenido (`Docs/insumos/auditoria/W1_articulo.md`):**
  - Clase y paquetes: `\documentclass[conference,letterpaper]{IEEEtran}`, `\usepackage[utf8]{inputenc}`, `\usepackage[T1]{fontenc}`, `\usepackage[spanish,es-tabla,es-nodecimaldot,es-noshorthands]{babel}`.
  - Extensión: **6 páginas exactas** incluyendo referencias (máximo permitido: 6 cuartillas).
  - Título exacto: «Modelo de transformación cuántica variacional de características de cáncer de mama para un sistema híbrido de prediagnóstico».
  - Autores en una línea: `Miguel Alexander Sánchez García, Jesús Yaljá Montiel Pérez, Ana María Winfield Reyes`, seguidos de «Escuela Superior de Cómputo, Instituto Politécnico Nacional, Ciudad de México» y «Tel. 57-29-6000 ext. 52000 y 52021. E-mail: msanchezg1904@alumno.ipn.mx», con el comentario `% [VERIFICAR: correo de los directores]` en `Docs/articulo/articulo.tex:44`.
  - Orden exacto de secciones: `Resumen` (`\begin{abstract}`), `Palabras clave` (`\begin{IEEEkeywords}`), `I. Introducción`, `II. Metodología`, `III. Resultados`, `IV. Conclusiones`, `Referencias` (`\begin{thebibliography}{99}`).
  - Figuras tomadas de `../Figures/` mediante `\graphicspath{{../Figures/}}` sin copiar ni generar archivos nuevos: `M5_kernel_concentration.png` (Fig. 1) y `M7_roc_test.png` (Fig. 2). Se descartaron para el artículo las figuras de `../Figures/` cuyos ejes o leyendas internos contienen identificadores de bitácora `(D-027)` (`M6_kernel_metrics.png`, `X4_qsvm_vs_readout.png`, `M8_classical_vs_quantum.png`), garantizando cero identificadores `D-xxx`/`H-xxx` visibles tanto en el texto como dentro de las figuras incluidas.
  - Tabla compacta (Tabla I) de desempeño clasificatorio en validación cruzada y prueba para masas y calcificaciones por separado, con todos los valores copiados literalmente de `Docs/tablas/m7_clasificacion.tex` (`Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10-21`).

---

## 2. Comandos ejecutados y salida final

### 2.1 Compilación LaTeX en dos pasadas (fuera del repositorio, en `/tmp/aud_W1`)

Comando ejecutado:
```sh
cd /Users/alexander_san/TT/Docs/articulo && export PATH="/Library/TeX/texbin:$PATH" && pdflatex -interaction=nonstopmode -output-directory /tmp/aud_W1 articulo.tex && pdflatex -interaction=nonstopmode -output-directory /tmp/aud_W1 articulo.tex
```

Salida final e inspección de `/tmp/aud_W1/articulo.log`:
```text
Output written on /tmp/aud_W1/articulo.pdf (6 pages, 579017 bytes).
Transcript written on /tmp/aud_W1/articulo.log.
```
- **Número de páginas:** `6` (dentro del límite máximo de 6 cuartillas).
- **Referencias o citas sin resolver (`Undefined references` / `Citation ... undefined`):** `0`.
- **Cajas horizontales desbordadas (`Overfull \hbox`):** `0`.
- **Cajas horizontales subllenas (`Underfull \hbox`):** `0`.
- **Cajas verticales (`Underfull \vbox`):** `2` avisos benignos de ajuste de página de `IEEEtran` al inicio de las figuras flotantes; `0` `Overfull \vbox`.
- **Archivos auxiliares o PDF en el repositorio:** `0` (todos los archivos `.pdf`, `.log`, `.aux` se escribieron únicamente en `/tmp/aud_W1`).

### 2.2 Verificador de cifras contra bitácora y CSVs (`verificar_cifras_capitulos.py`)

Comando ejecutado:
```sh
/opt/anaconda3/envs/qml_cancer/bin/python Code/tools/verificar_cifras_capitulos.py Docs/articulo
```

Salida:
```text
359 cifras: EN_BITACORA 235, EN_CSV 122, NO_ENCONTRADO 0, SIN_FUENTE 2
SIN_FUENTE      articulo.tex                     2403.07059  []  …um machine learning models,'' \textit{arXiv preprint} arXiv:2403.07059, 2024, doi: \url{https://doi.org/10.485…
SIN_FUENTE      articulo.tex                     1809.1936  []  …p. 179--188, 1936, doi: \url{https://doi.org/10.1111/j.1469-1809.1936.tb02137.x}.…
```
*(Nota: `NO_ENCONTRADO 0`; las 2 entradas `SIN_FUENTE` corresponden exclusivamente al identificador `arXiv:2403.07059` y al sufijo de DOI `1809.1936` dentro de `\begin{thebibliography}`).*

### 2.3 Estado del repositorio (`git status --short`)

Comando ejecutado:
```sh
git -C /Users/alexander_san/TT status --short
```
Se confirma que en esta tarea únicamente se crearon `Docs/articulo/articulo.tex` y `Docs/insumos/auditoria/informe_W1.md`, sin modificar ningún archivo existente y sin dejar artefactos de compilación en el árbol de trabajo.

---

## 3. Hallazgos y notas de verificación

Durante la elaboración del artículo y la verificación cruzada contra `Docs/capitulos/0_Preliminares/resumen.tex`, `Docs/capitulos/5_Metodologia/*.tex`, `Docs/capitulos/6_Resultados/*.tex` y `Docs/bibliografia.tex`, se documentan los siguientes puntos:

### W1-1 · BAJA · verificación pendiente declarada por instrucción
- Ubicación: `Docs/articulo/articulo.tex:44`
- Texto: `% [VERIFICAR: correo de los directores]`
- Problema: La plantilla de ejemplo (`Other/ESCOM/Ejemplo Articulo Tecnico.pdf`) incluye correos electrónicos de los coautores en el bloque de afiliación, pero el reporte técnico (`Docs/Technical_Report.tex`) no declara los correos institucionales de los directores.
- Evidencia: Instrucción explícita en `Docs/insumos/auditoria/W1_articulo.md:10` («No inventes correos de los directores: deja `[VERIFICAR: correo de los directores]` en un comentario»).
- Propuesta: Sustituir el comentario en `Docs/articulo/articulo.tex:44` por los correos institucionales verificados de los directores antes de la entrega final a la CATT.

### W1-2 · BAJA · redondeo en `resumen.tex` frente a cifras literales de `6_Resultados/`
- Ubicación: `Docs/capitulos/0_Preliminares/resumen.tex:25` y `Docs/capitulos/0_Preliminares/resumen.tex:30`
- Texto: «frente a 0.61 del kernel gaussiano» (`resumen.tex:25`); «por debajo del umbral $\sqrt{N} = 14$» (`resumen.tex:26`); «entre el 16 y el 74\,\% de las entradas fuera de la diagonal del kernel cuántico se leerían como cero.» (`resumen.tex:30`)
- Problema: El resumen del reporte redondea a dos cifras significativas cuatro cantidades que en `Docs/capitulos/6_Resultados/` aparecen con mayor precisión (`0.607`, `14.1`, `15.7\,\%` y `74.5\,\%`). Para cumplir simultáneamente la regla de `W1_articulo.md:21` («Cada cifra del artículo debe aparecer tal cual en un archivo de `Docs/capitulos/6_Resultados/` o `5_Metodologia/`»), en `Docs/articulo/articulo.tex` se emplearon siempre las cifras literales de `Docs/capitulos/6_Resultados/`.
- Evidencia: `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:17` (`0.607`), `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:78` (`14.1`) y `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:26` / `6.8_sintesis.tex:37` (`15.7\,\%` y `74.5\,\%`).
- Propuesta: Mantener en `Docs/articulo/articulo.tex` las cifras exactas de `6_Resultados/`; opcionalmente si se desea alinear `resumen.tex` con `6.8_sintesis.tex`, actualizar esos cuatro redondeos en `resumen.tex`.

### Conteo por severidad
- **ALTA:** 0
- **MEDIA:** 0
- **BAJA:** 2

---

## 4. Lista de referencias utilizadas en `Docs/articulo/articulo.tex`

Todas las referencias provienen exclusivamente de `Docs/bibliografia.tex`, reformateadas al estilo IEEE y numeradas por orden estricto de aparición en el texto (17 referencias, dentro del rango requerido de 10 a 18):

| Nº IEEE en `articulo.tex` | Clave original en `Docs/bibliografia.tex` | Ubicación en `articulo.tex` | Ubicación en `Docs/bibliografia.tex` |
|---|---|---|---|
| `[1]` | `Bray2024GLOBOCAN` | `Docs/articulo/articulo.tex:197` | `Docs/bibliografia.tex:275` |
| `[2]` | `INEGI2025` | `Docs/articulo/articulo.tex:200` | `Docs/bibliografia.tex:38` |
| `[3]` | `Wang2020DeepLearning` | `Docs/articulo/articulo.tex:203` | `Docs/bibliografia.tex:69` |
| `[4]` | `havlicek2019supervised` | `Docs/articulo/articulo.tex:206` | `Docs/bibliografia.tex:246` |
| `[5]` | `schuld2019quantum` | `Docs/articulo/articulo.tex:209` | `Docs/bibliografia.tex:240` |
| `[6]` | `Mari2020Transfer` | `Docs/articulo/articulo.tex:212` | `Docs/bibliografia.tex:410` |
| `[7]` | `Bowles2024Benchmarking` | `Docs/articulo/articulo.tex:215` | `Docs/bibliografia.tex:440` |
| `[8]` | `huang2021power` | `Docs/articulo/articulo.tex:218` | `Docs/bibliografia.tex:252` |
| `[9]` | `Thanasilp2024` | `Docs/articulo/articulo.tex:221` | `Docs/bibliografia.tex:296` |
| `[10]` | `Azevedo2022QuantumTransfer` | `Docs/articulo/articulo.tex:224` | `Docs/bibliografia.tex:90` |
| `[11]` | `Lee2017CBISDDSM` | `Docs/articulo/articulo.tex:227` | `Docs/bibliografia.tex:380` |
| `[12]` | `Zwanenburg2020IBSI` | `Docs/articulo/articulo.tex:230` | `Docs/bibliografia.tex:392` |
| `[13]` | `vanGriethuysen2017` | `Docs/articulo/articulo.tex:233` | `Docs/bibliografia.tex:264` |
| `[14]` | `Guyon2003` | `Docs/articulo/articulo.tex:236` | `Docs/bibliografia.tex:332` |
| `[15]` | `Cortes2012` | `Docs/articulo/articulo.tex:239` | `Docs/bibliografia.tex:283` |
| `[16]` | `davies1979cluster` | `Docs/articulo/articulo.tex:242` | `Docs/bibliografia.tex:215` |
| `[17]` | `fisher1936use` | `Docs/articulo/articulo.tex:245` | `Docs/bibliografia.tex:221` |

---

## 5. Tabla completa de trazabilidad de cifras (`cifra · fuente archivo:línea`)

Cada cifra de `Docs/articulo/articulo.tex` (tanto en el resumen, cuerpo del texto, pies de figura y Tabla I como en las conclusiones) aparece literalmente en `Docs/capitulos/5_Metodologia/*.tex`, `Docs/capitulos/6_Resultados/*.tex` o `Docs/tablas/m7_clasificacion.tex`:

| Cifra en `articulo.tex` | Línea(s) en `articulo.tex` | Fuente (`archivo.tex:línea`) |
|---|---|---|
| `3\,568` | 53, 68, 77 | `Docs/capitulos/5_Metodologia/5.3_M1_lectura.tex:62` |
| `67` | 53, 83 | `Docs/capitulos/5_Metodologia/5.5_M3_extraccion.tex:10` |
| `12` | 53, 68, 88 | `Docs/capitulos/5_Metodologia/5.6_M4_seleccion.tex:11` |
| `0` | 53, 88 | `Docs/capitulos/5_Metodologia/5.6_M4_seleccion.tex:17` |
| `1` | 53, 121, 127, 193 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:10` |
| `0.0022` | 53, 121, 193 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:12` |
| `0.0029` | 53, 121, 193 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:14` |
| `0.000031` | 53, 121, 193 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:15` |
| `0.000032` | 53, 121, 193 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:13` |
| `0.607` | 53, 121, 163 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:17` |
| `1.400` | 53, 132, 193 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:77` |
| `1.701` | 53, 132, 193 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:78` |
| `14.1` | 53, 132, 193 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:78` |
| `0.07` | 53, 193 | `Docs/capitulos/6_Resultados/6.8_sintesis.tex:35` |
| `0.14` | 53, 193 | `Docs/capitulos/6_Resultados/6.8_sintesis.tex:35` |
| `+0.10` | 53, 193 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:13` |
| `+0.13` | 53, 193 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:13` |
| `1\,024` | 53 | `Docs/capitulos/6_Resultados/6.8_sintesis.tex:37` |
| `15.7` | 53 | `Docs/capitulos/6_Resultados/6.8_sintesis.tex:37` |
| `74.5` | 53 | `Docs/capitulos/6_Resultados/6.8_sintesis.tex:37` |
| `2` | 65 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:115` |
| `1` | 77 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:23` |
| `16` | 77 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:34` |
| `84` | 77 | `Docs/capitulos/5_Metodologia/5.3_M1_lectura.tex:60` |
| `97.6` | 77 | `Docs/capitulos/5_Metodologia/5.3_M1_lectura.tex:59` |
| `100` | 77 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:31` |
| `3\,103` | 77 | `Docs/capitulos/5_Metodologia/5.3_M1_lectura.tex:29` |
| `1\,696` | 77 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:23` |
| `1\,318` | 77 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:20` |
| `637` | 77 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:33` |
| `681` | 77 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:33` |
| `1\,872` | 77 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:24` |
| `1\,546` | 77 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:20` |
| `544` | 77 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:33` |
| `1\,002` | 77 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:33` |
| `2\,864` | 77 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:13` |
| `0` | 77 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:24` |
| `2` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:17` |
| `80` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:13` |
| `3\,568` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:14` |
| `78` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:15` |
| `0.870` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:15` |
| `3\,206` | 80 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:16` |
| `3\,213` | 80 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:16` |
| `99.8` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:20` |
| `7` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:22` |
| `0.004` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:23` |
| `86.3` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:26` |
| `99.55` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:28` |
| `20` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:20` |
| `16` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:31` |
| `1.00` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:33` |
| `5.31` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:33` |
| `224` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:40` |
| `8` | 80 | `Docs/capitulos/5_Metodologia/5.4_M2_preprocesamiento.tex:20` |
| `3` | 83 | `Docs/capitulos/5_Metodologia/5.5_M3_extraccion.tex:35` |
| `18` | 83 | `Docs/capitulos/5_Metodologia/5.5_M3_extraccion.tex:15` |
| `9` | 83 | `Docs/capitulos/5_Metodologia/5.5_M3_extraccion.tex:17` |
| `24` | 83 | `Docs/capitulos/5_Metodologia/5.5_M3_extraccion.tex:19` |
| `16` | 83 | `Docs/capitulos/5_Metodologia/5.5_M3_extraccion.tex:20` |
| `1` | 83 | `Docs/capitulos/5_Metodologia/5.5_M3_extraccion.tex:31` |
| `32` | 83 | `Docs/capitulos/5_Metodologia/5.5_M3_extraccion.tex:26` |
| `4` | 88 | `Docs/capitulos/5_Metodologia/5.6_M4_seleccion.tex:36` |
| `2.95` | 88 | `Docs/capitulos/5_Metodologia/5.6_M4_seleccion.tex:17` |
| `41.25` | 88 | `Docs/capitulos/5_Metodologia/5.6_M4_seleccion.tex:18` |
| `16` | 88 | `Docs/capitulos/5_Metodologia/5.6_M4_seleccion.tex:18` |
| `0.95` | 88 | `Docs/capitulos/5_Metodologia/5.6_M4_seleccion.tex:32` |
| `2` | 88 | `Docs/capitulos/5_Metodologia/5.6_M4_seleccion.tex:17` |
| `1.569` | 88 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:104` |
| `1.572` | 88 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:104` |
| `200` | 88 | `Docs/capitulos/5_Metodologia/5.6_M4_seleccion.tex:55` |
| `125` | 88 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:112` |
| `0.011` | 88 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:113` |
| `168` | 88 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:111` |
| `0.019` | 88 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:113` |
| `5` | 91 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:17` |
| `0` | 91, 96 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:11` |
| `12` | 91, 94, 95, 96 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:11` |
| `66` | 96, 97 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:55` |
| `24` | 96 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:100` |
| `2` | 96 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:26` |
| `42` | 96 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:101` |
| `-1` | 96 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:19` |
| `1` | 96 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:19` |
| `1` | 101 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:61` |
| `2` | 101 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:61` |
| `0` | 101 | `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:96` |
| `6` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:7` |
| `200` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:12` |
| `42` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:13` |
| `19\,900` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:16` |
| `0.87` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:16` |
| `1.19` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:16` |
| `1` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:16` |
| `1\,000` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:21` |
| `2` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:25` |
| `3` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:44` |
| `0.045` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:40` |
| `0.25` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:47` |
| `0.5` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:47` |
| `4` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:47` |
| `8` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:47` |
| `16` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:47` |
| `32` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:47` |
| `64` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:47` |
| `128` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:49` |
| `256` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:49` |
| `512` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:49` |
| `10` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:48` |
| `-5` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:47` |
| `-4` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:47` |
| `-3` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:44` |
| `-2` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:25` |
| `0.025` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:48` |
| `0.05` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:48` |
| `0.1` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:48` |
| `0.2` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:54` |
| `0.02` | 106 | `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:54` |
| `7` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:8` |
| `12` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:11` |
| `32` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:11` |
| `16` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:11` |
| `1` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:16` |
| `10` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:14` |
| `-3` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:14` |
| `-4` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:15` |
| `128` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:15` |
| `40` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:19` |
| `15` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:18` |
| `2\,000` | 109, 168 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:25` |
| `205` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:36` |
| `8` | 109 | `Docs/capitulos/5_Metodologia/5.10_M8_evaluacion.tex:6` |
| `0.5` | 109, 168 | `Docs/capitulos/5_Metodologia/5.10_M8_evaluacion.tex:15` |
| `5` | 109 | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:31` |
| `120` | 109 | `Docs/capitulos/5_Metodologia/5.10_M8_evaluacion.tex:19` |
| `0.64` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:43` |
| `0.82` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:42` |
| `0.71` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:43` |
| `0.40` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:37` |
| `0.50` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:37` |
| `0.45` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:39` |
| `-0.002` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:61` |
| `-0.010` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:62` |
| `0.95` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:53` |
| `7` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:51` |
| `8` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:53` |
| `0.61` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:53` |
| `0.58` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:56` |
| `4` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:55` |
| `5` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:51` |
| `1` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:54` |
| `2` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:39` |
| `3` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:69` |
| `691` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:118` |
| `201` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:118` |
| `602` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:119` |
| `151` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:119` |
| `67` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:136` |
| `12` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:136` |
| `86.8` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:137` |
| `90.2` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:137` |
| `0.693` | 116, 161 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:141` |
| `0.039` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:141` |
| `0.650` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:141` |
| `0.056` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:141` |
| `0.800` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:141` |
| `0.028` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:141` |
| `0.758` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:141` |
| `0.025` | 116 | `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:141` |
| `200` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:11` |
| `95` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:12` |
| `0.011` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:13` |
| `23` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:13` |
| `10` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:13` |
| `-3` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:13` |
| `80` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:13` |
| `26` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:14` |
| `-6` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:14` |
| `0.014` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:15` |
| `16` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:15` |
| `76` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:15` |
| `28` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:15` |
| `0.180` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:22` |
| `0.178` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:22` |
| `0.056` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:21` |
| `0.048` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:22` |
| `0.0837` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:34` |
| `0.0131` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:34` |
| `8` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:34` |
| `0.0417` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:34` |
| `0.0068` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:34` |
| `12` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:34` |
| `0.0363` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:34` |
| `0.0090` | 121 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:34` |
| `1` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:58` |
| `1\,000` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:58` |
| `0.049` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:59` |
| `0.001` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:59` |
| `0.003` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:59` |
| `0.002` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:60` |
| `0.005` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:60` |
| `0.151` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:60` |
| `0.006` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:61` |
| `0.007` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:61` |
| `4` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:60` |
| `10` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:62` |
| `0.073` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:63` |
| `0.077` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:63` |
| `0.071` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:64` |
| `200` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:65` |
| `184.0` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:69` |
| `171.3` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:70` |
| `187.7` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:70` |
| `167.6` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:70` |
| `2.8` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:68` |
| `2.6` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:68` |
| `1.433` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:77` |
| `1.511` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:77` |
| `1.31` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:82` |
| `1.70` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:82` |
| `306` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:83` |
| `388` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:83` |
| `-1` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:58` |
| `410` | 132 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:84` |
| `4.301` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:111` |
| `5.898` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:112` |
| `13.346` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:112` |
| `0.669` | 135, 161 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:112` |
| `0.781` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:112` |
| `0.449` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:113` |
| `0.668` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:113` |
| `0.070` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:113` |
| `0.041` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:113` |
| `0.012` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:114` |
| `2.387` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:114` |
| `6.890` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:114` |
| `6.247` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:114` |
| `1.284` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:115` |
| `1.390` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:115` |
| `0.399` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:115` |
| `0.753` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:115` |
| `0.181` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:116` |
| `0.031` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:116` |
| `10` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:117` |
| `-14` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:117` |
| `20` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:142` |
| `200` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:110` |
| `0.055` | 135, 156 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:143` |
| `0.006` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:148` |
| `0.009` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:149` |
| `1\,318` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:148` |
| `0.148` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:149` |
| `0.018` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:149` |
| `0.020` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:149` |
| `1\,546` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:148` |
| `2.95` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:150` |
| `3.25` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:150` |
| `36.3` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:150` |
| `39.3` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:150` |
| `0.523` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:167` |
| `0.575` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:167` |
| `0.508` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:169` |
| `0.510` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:168` |
| `0.520` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:168` |
| `0.547` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:169` |
| `0.02` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:185` |
| `0.54` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:186` |
| `0.59` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:186` |
| `0.043` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:187` |
| `0.143` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:187` |
| `0.99997` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:192` |
| `0.99999` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:192` |
| `8` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:197` |
| `1.7` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:201` |
| `4.6` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:201` |
| `0.011` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:144` |
| `0.024` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:202` |
| `1.71` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:203` |
| `3.23` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:203` |
| `14.1` | 135 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:204` |
| `-0.011` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.061` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `0.038` | 140, 160 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.659` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `+0.020` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.026` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `0.067` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `0.377` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.122` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.202` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.044` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `0.003` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.070` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.140` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.004` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `0.044` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.135` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.208` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `0.001` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.118` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.182` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `-0.046` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.05` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:19` |
| `0.051` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `0.017` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:16` |
| `0.039` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:40` |
| `16` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `-8` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:40` |
| `64` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:40` |
| `-32` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `200` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:40` |
| `0.533` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:40` |
| `0.557` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:40` |
| `0.596` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:40` |
| `0.631` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:40` |
| `0.603` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:43` |
| `0.682` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:43` |
| `-0.048` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:43` |
| `-0.086` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:43` |
| `8` | 140 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:40` |
| `12` | 145 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:43` |
| `95` | 151 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.652` | 154, 162, 164 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.068` | 154 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.651` | 154 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.578` | 154 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.724` | 154 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.519` | 154 | `Docs/tablas/m7_clasificacion.tex:13` |
| `0.638` | 154 | `Docs/tablas/m7_clasificacion.tex:13` |
| `0.641` | 155 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.059` | 155 | `Docs/tablas/m7_clasificacion.tex:14` |
| `0.572` | 155, 156 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.710` | 155 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.512` | 155 | `Docs/tablas/m7_clasificacion.tex:14` |
| `0.616` | 155 | `Docs/tablas/m7_clasificacion.tex:14` |
| `0.648` | 156 | `Docs/tablas/m7_clasificacion.tex:15` |
| `0.646` | 156 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.721` | 156 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.502` | 156 | `Docs/tablas/m7_clasificacion.tex:15` |
| `0.606` | 156 | `Docs/tablas/m7_clasificacion.tex:15` |
| `0.565` | 157, 164 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.079` | 157 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.530` | 157 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.473` | 157 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.587` | 157 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.386` | 157 | `Docs/tablas/m7_clasificacion.tex:16` |
| `0.529` | 157 | `Docs/tablas/m7_clasificacion.tex:16` |
| `0.563` | 158 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.024` | 158 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.581` | 158 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.521` | 158 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.644` | 158 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.456` | 158 | `Docs/tablas/m7_clasificacion.tex:17` |
| `0.571` | 158, 164 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.742` | 160 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.769` | 160 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.694` | 160 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.836` | 160 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.665` | 160 | `Docs/tablas/m7_clasificacion.tex:19` |
| `0.666` | 160 | `Docs/tablas/m7_clasificacion.tex:19` |
| `0.758` | 161, 162 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.046` | 161 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.788` | 161 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.719` | 161 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.851` | 161 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.739` | 162 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.036` | 162 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.685` | 162 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.826` | 162 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.653` | 162 | `Docs/tablas/m7_clasificacion.tex:21` |
| `0.640` | 163 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.041` | 163 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.633` | 163 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.558` | 163 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.700` | 163 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.504` | 163 | `Docs/tablas/m7_clasificacion.tex:22` |
| `0.667` | 164 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.035` | 164 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `0.725` | 164 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:13` |
| `5` | 168 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:10` |
| `0.628` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:10` |
| `0.55` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:10` |
| `0.70` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:10` |
| `0.759` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:10` |
| `0.69` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:10` |
| `0.83` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:10` |
| `0.649` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:10` |
| `0.769` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:10` |
| `-0.02` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:56` |
| `-0.01` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:10` |
| `+0.10` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:69` |
| `0.03` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:56` |
| `0.17` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:13` |
| `+0.13` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:69` |
| `0.05` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:69` |
| `0.20` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:13` |
| `2` | 180, 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `12` | 180, 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `4\,096` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `7` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:56` |
| `42` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:56` |
| `51` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:56` |
| `0.040` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:56` |
| `0.110` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:56` |
| `40` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:56` |
| `0.18` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:56` |
| `+0.003` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:69` |
| `+0.041` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:69` |
| `-0.066` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:69` |
| `-0.118` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:69` |
| `25` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:33` |
| `81` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:33` |
| `10\,704` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:33` |
| `28` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:36` |
| `0.656` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:36` |
| `0.652` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:56` |
| `0.755` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:36` |
| `0.760` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:36` |
| `0.2` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:13` |
| `6` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:33` |
| `9` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:41` |
| `-0.11` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:41` |
| `-0.06` | 180 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:69` |
| `0.998` | 180, 193 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:54` |
| `0.994` | 180, 193 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:54` |
| `0.800` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:54` |
| `0.824` | 180 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:54` |
| `8` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:13` |
| `48` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:16` |
| `0.67` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:16` |
| `0.97` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:16` |
| `12` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:13` |
| `0.718` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:13` |
| `0.821` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:13` |
| `0.667` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:13` |
| `0.975` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:13` |
| `4` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:13` |
| `120` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:13` |
| `0.033` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:13` |
| `0.872` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:33` |
| `0.825` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:33` |
| `67` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:16` |
| `0.693` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:36` |
| `0.800` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:36` |
| `0.668` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:36` |
| `0.745` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:36` |
| `-0.12` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:36` |
| `-0.14` | 185 | `Docs/capitulos/6_Resultados/6.5_comparacion.tex:36` |
| `16` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:10` |
| `1.9` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:13` |
| `20` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:13` |
| `75` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:13` |
| `28` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:10` |
| `24` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:10` |
| `8` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `29` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:10` |
| `25` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:10` |
| `26` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:10` |
| `200` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:10` |
| `22` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:10` |
| `23` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:10` |
| `50` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `48` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `5.16` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:13` |
| `205` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `14` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:10` |
| `15` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `41` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:13` |
| `1.5` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:13` |
| `1.4` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `3\,600` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `1.8` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `10` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `-15` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `0.015625` | 188 | `Docs/capitulos/6_Resultados/6.7_lecciones_implementacion.tex:65` |
| `1\,024` | 188, 193 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:23` |
| `55` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:23` |
| `65` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:23` |
| `17` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:23` |
| `0.02` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:56` |
| `0.548` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:23` |
| `0.565` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:23` |
| `0.630` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:23` |
| `0.640` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:23` |
| `0.563` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:23` |
| `0.654` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:23` |
| `0.667` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:23` |
| `1` | 188 | `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:72` |
| `21.5` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:26` |
| `15.7` | 188, 193 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:26` |
| `74.5` | 188, 193 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:26` |
| `71.6` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:26` |
| `46\,000` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:26` |
| `35\,000` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:26` |
| `3.1` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:26` |
| `3.2` | 188 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:26` |
| `12` | 193 | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:13` |
| `2` | 193 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:68` |
| `7` | 193 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:70` |
| `3` | 193 | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:13` |
| `205` | 193 | `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex:13` |
