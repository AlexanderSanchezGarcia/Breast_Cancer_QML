# Informe de Tarea T5 · El EDA como Capítulo 4 y Puente hacia la Metodología

**Fecha de ejecución:** 2026-10-14  
**Trabajador:** Dispatch `ctx_a190f90b0e2a` · Tarea `task_ce04b6313725` · Terminal `term_0ed1a3d0-b383-4668-93ac-d45aa0af5d90`  
**Objetivo:** Consolidar el Análisis Exploratorio de Datos (EDA) como Capítulo 4 del reporte técnico, funcionando como puente justificativo hacia la Metodología (Capítulo 5), acortar el cuerpo trasladando figuras no esenciales al Anexo A.3.2, y auditar todas las referencias cruzadas.

---

## 1. Resumen de Actividades Realizadas

1. **Reescritura de `4.0_introduccion.tex` como puente metodológico:**
   - Se reorientó la introducción para dejar de presentar el EDA como un ejercicio histórico o descriptivo aislado, articulándolo como la caracterización cuantitativa y técnica empírica que condiciona directamente el diseño experimental de la Metodología (`capítulo~\ref{sec:metodologia}`).
   - Se explicitaron tres preguntas rectoras: (1) grado de asimetría y desbalance de clases, (2) capacidad predictiva nula de metadatos clínicos frente a características de imagen, y (3) factibilidad de la representación cuántica dadas las dimensiones de imagen y particularidades de los archivos DICOM.
   - Se verificó que `5_Metodologia/5.0_introduccion.tex` cuenta con `\label{sec:metodologia}`, permitiendo el enlace LaTeX directo.

2. **Estandarización de cabeceras en `Docs/capitulos/4_EDA/*.tex`:**
   - Se añadió la línea `% Capítulo 4 desde el 2026-10-14 (antes §5).` en las cabeceras de los 6 archivos del capítulo (`4.0` a `4.5`), preservando las líneas de reemplazo de `Technical_Report.tex` y los identificadores de respaldo.

3. **Reestructuración de `4.5_hallazgos.tex` («Implicaciones para el diseño»):**
   - Se renombró la subsección a `\subsection{Implicaciones para el diseño}\label{sec:implicaciones_diseno}`.
   - Se conservaron íntegramente los 5 hallazgos analíticos principales.
   - Se incorporó la tabla de síntesis `\begin{table}[htbp]` (`Tabla~\ref{tab:eda_implicaciones_diseno}`) en formato `booktabs` con las 8 filas obligatorias, mapeando cada hallazgo con su decisión de diseño y la subsección exacta de la Metodología (`\ref{sec:descripcion_general}`, `\ref{sec:modulo2}`, `\ref{sec:modulo3}`, `\ref{sec:modulo4}`, `\ref{sec:modulo7}`), respaldada por su comentario de trazabilidad `% fuente:`.

4. **Acortamiento del cuerpo del capítulo y traslado de figuras a Anexo A.3.2:**
   - De las 14 figuras del EDA (13 en el texto y D2 en inventario), se conservaron en el cuerpo las 6 que sustentan directamente decisiones de diseño:
     - `B2_imbalance_by_finding.png` (`fig:imbalance_by_finding`) en `4.2`
     - `C3_mass_morphology.png` (`fig:mass_morphology`) en `4.3`
     - `C4_calc_morphology.png` (`fig:calc_morphology`) en `4.3`
     - `C5_correlation_matrix.png` (`fig:correlation_matrix`) en `4.3`
     - `D1_image_dimensions.png` (`fig:image_dimensions`) en `4.4`
     - `D5_roi_overlays.png` (`fig:roi_overlays`) en `4.4`
   - Se trasladaron las 8 figuras restantes a `Docs/capitulos/A_Anexos/A.3.2_figuras_eda.tex`:
     - `B1_class_distribution.png` (`fig:class_distribution`)
     - `B3_birads_distribution.png` (`fig:birads_distribution`)
     - `B4_subtlety_distribution.png` (`fig:subtlety_distribution`)
     - `C1_breast_density.png` (`fig:breast_density`)
     - `C2_laterality_view.png` (`fig:laterality_view`)
     - `D2_manufacturers.png` (`fig:manufacturers`)
     - `D3_pixel_intensities.png` (`fig:pixel_intensities`)
     - `D4_sample_gallery.png` (`fig:sample_gallery`)
   - En el cuerpo del capítulo, donde se ubicaban las figuras trasladadas, se mantuvieron intactos todos los párrafos de análisis e interpretación clínica/geométrica, reemplazando los entornos de figura por remisiones explícitas («véase la Figura~\ref{…} del Anexo~\ref{anx:figuras_eda}»).

5. **Auditoría de referencias cruzadas y numeración:**
   - Se corrigieron todas las referencias internas de `4_EDA/`: `4.0_introduccion.tex` (sección a capítulo), `4.4_imagenes_dicom.tex` (enlace formal a Metodología y Módulo 3, y cita a Figura D2).
   - Se elaboró el informe exhaustivo `Docs/insumos/referencias_cruzadas.md` con la tabla de referencias en otros archivos del repositorio y la propuesta de nota de equivalencia para `Other/bitacora_decisiones.md`.

---

## 2. Archivos Modificados y Creados

### Modificados:
- `Docs/capitulos/4_EDA/4.0_introduccion.tex`
- `Docs/capitulos/4_EDA/4.1_validacion.tex`
- `Docs/capitulos/4_EDA/4.2_variable_objetivo.tex`
- `Docs/capitulos/4_EDA/4.3_variables_clinicas.tex`
- `Docs/capitulos/4_EDA/4.4_imagenes_dicom.tex`
- `Docs/capitulos/4_EDA/4.5_hallazgos.tex`

### Creados:
- `Docs/capitulos/A_Anexos/A.3.2_figuras_eda.tex`
- `Docs/insumos/referencias_cruzadas.md`
- `Docs/insumos/noche/informe_T5.md`

---

## 3. Salida de Pruebas de Aceptación

### A. Verificación de Cifras (`verificar_cifras_capitulos.py`)

**Línea base previa a la intervención:**
```text
20 cifras: EN_BITACORA 1, EN_CSV 0, NO_ENCONTRADO 19, SIN_FUENTE 0
NO_ENCONTRADO   4.1_validacion.tex                     1.3  [H-001, D-005, H-038]  …dataset CBIS-DDSM unificado} \renewcommand{\arraystretch}{1.3} \begin{tabularx}{\textwidth}{@{}Xrr@{}…
NO_ENCONTRADO   4.1_validacion.tex                    59.2  [D-005, H-001; 1_EDA.ipynb]  …ndo en la codificación binaria 0\,=\,benigno (2\,111 casos, 59.2\,\%) y 1\,=\,maligno (1\,457 casos, 40.…
NO_ENCONTRADO   4.1_validacion.tex                    40.8  [D-005, H-001; 1_EDA.ipynb]  …gno (2\,111 casos, 59.2\,\%) y 1\,=\,maligno (1\,457 casos, 40.8\,\%).…
NO_ENCONTRADO   4.2_variable_objetivo.tex             1.45  [D-005; 1_EDA.ipynb]  … El dataset presenta un desbalance global moderado de 1.45:1 (benigno/maligno), que se distribuye …
NO_ENCONTRADO   4.2_variable_objetivo.tex             1.16  [D-005; 1_EDA.ipynb]  … Las masas presentan un balance casi simétrico (ratio 1.16:1), con 912 casos benignos y 784 malign…
NO_ENCONTRADO   4.2_variable_objetivo.tex             1.78  [D-005; 1_EDA.ipynb]  …lcificaciones muestran un desbalance más pronunciado (ratio 1.78:1), con 1\,199 casos benignos frente a …
NO_ENCONTRADO   4.2_variable_objetivo.tex              3.1  [D-005; 1_EDA.ipynb]  … La media de \textit{subtlety} en casos malignos (3.1 para masas, 2.8 para calcificaciones) e…
NO_ENCONTRADO   4.2_variable_objetivo.tex              2.8  [D-005; 1_EDA.ipynb]  …dia de \textit{subtlety} en casos malignos (3.1 para masas, 2.8 para calcificaciones) es ligeramente in…
NO_ENCONTRADO   4.2_variable_objetivo.tex              3.4  [D-005; 1_EDA.ipynb]  …ficaciones) es ligeramente inferior a la de casos benignos (3.4 y 3.2 respectivamente), aunque la difer…
NO_ENCONTRADO   4.2_variable_objetivo.tex              3.2  [D-005; 1_EDA.ipynb]  …ones) es ligeramente inferior a la de casos benignos (3.4 y 3.2 respectivamente), aunque la diferencia …
NO_ENCONTRADO   4.3_variables_clinicas.tex           -0.03  [D-005; 1_EDA.ipynb]  …na correlación casi nula con la etiqueta de patología ($r = -0.03$ para masas, $r = +0.09$ para calcifica…
NO_ENCONTRADO   4.3_variables_clinicas.tex            0.09  [D-005; 1_EDA.ipynb]  …con la etiqueta de patología ($r = -0.03$ para masas, $r = +0.09$ para calcificaciones), lo que indica q…
NO_ENCONTRADO   4.3_variables_clinicas.tex           -0.31  [D-005; 1_EDA.ipynb]  … negativa moderada entre densidad y \textit{subtlety} ($r = -0.31$ para masas), confirmando que las lesio…
NO_ENCONTRADO   4.3_variables_clinicas.tex            1.04  [D-005; 1_EDA.ipynb]  …étrica (1\,819 casos izquierdos vs.\ 1\,749 derechos, ratio 1.04:1), lo que indica ausencia de sesgo de …
NO_ENCONTRADO   4.3_variables_clinicas.tex            0.51  [D-005; 1_EDA.ipynb]  …la correlación más alta con la etiqueta de patología ($r = +0.51$ para masas, $r = +0.43$ para calcifica…
NO_ENCONTRADO   4.3_variables_clinicas.tex            0.43  [D-005; 1_EDA.ipynb]  …con la etiqueta de patología ($r = +0.51$ para masas, $r = +0.43$ para calcificaciones), lo cual es espe…
NO_ENCONTRADO   4.3_variables_clinicas.tex            0.12  [D-005, D-006; 1_EDA.ipynb]  …es prácticamente nulas con la etiqueta de patología ($|r| < 0.12$ en todos los casos), confirmando que e…
NO_ENCONTRADO   4.5_hallazgos.tex                     1.16  [D-005, RF-19; 1_EDA.ipynb]  …alance de clases diferenciado.} El ratio benigno/maligno es 1.16:1 para masas y 1.78:1 para calcificacio…
NO_ENCONTRADO   4.5_hallazgos.tex                     1.78  [D-005, RF-19; 1_EDA.ipynb]  …erenciado.} El ratio benigno/maligno es 1.16:1 para masas y 1.78:1 para calcificaciones. La ponderación …
```

**Salida final tras los cambios:**
```text
21 cifras: EN_BITACORA 2, EN_CSV 2, NO_ENCONTRADO 17, SIN_FUENTE 0
NO_ENCONTRADO   4.1_validacion.tex                     1.3  [H-001, D-005, H-038]  …dataset CBIS-DDSM unificado} \renewcommand{\arraystretch}{1.3} \begin{tabularx}{\textwidth}{@{}Xrr@{}…
NO_ENCONTRADO   4.1_validacion.tex                    59.2  [D-005, H-001; 1_EDA.ipynb]  …ndo en la codificación binaria 0\,=\,benigno (2\,111 casos, 59.2\,\%) y 1\,=\,maligno (1\,457 casos, 40.…
NO_ENCONTRADO   4.1_validacion.tex                    40.8  [D-005, H-001; 1_EDA.ipynb]  …gno (2\,111 casos, 59.2\,\%) y 1\,=\,maligno (1\,457 casos, 40.8\,\%).…
NO_ENCONTRADO   4.2_variable_objetivo.tex             1.45  [D-005; 1_EDA.ipynb]  … El dataset presenta un desbalance global moderado de 1.45:1 (benigno/maligno), que se distribuye …
NO_ENCONTRADO   4.2_variable_objetivo.tex             1.16  [D-005; 1_EDA.ipynb]  … Las masas presentan un balance casi simétrico (ratio 1.16:1), con 912 casos benignos y 784 malign…
NO_ENCONTRADO   4.2_variable_objetivo.tex             1.78  [D-005; 1_EDA.ipynb]  …lcificaciones muestran un desbalance más pronunciado (ratio 1.78:1), con 1\,199 casos benignos frente a …
NO_ENCONTRADO   4.2_variable_objetivo.tex              3.1  [D-005; 1_EDA.ipynb]  … La media de \textit{subtlety} en casos malignos (3.1 para masas, 2.8 para calcificaciones) e…
NO_ENCONTRADO   4.2_variable_objetivo.tex              2.8  [D-005; 1_EDA.ipynb]  …dia de \textit{subtlety} en casos malignos (3.1 para masas, 2.8 para calcificaciones) es ligeramente in…
NO_ENCONTRADO   4.2_variable_objetivo.tex              3.4  [D-005; 1_EDA.ipynb]  …ficaciones) es ligeramente inferior a la de casos benignos (3.4 y 3.2 respectivamente), aunque la difer…
NO_ENCONTRADO   4.2_variable_objetivo.tex              3.2  [D-005; 1_EDA.ipynb]  …ones) es ligeramente inferior a la de casos benignos (3.4 y 3.2 respectivamente), aunque la diferencia …
NO_ENCONTRADO   4.3_variables_clinicas.tex           -0.03  [D-005; 1_EDA.ipynb]  …na correlación casi nula con la etiqueta de patología ($r = -0.03$ para masas, $r = +0.09$ para calcifica…
NO_ENCONTRADO   4.3_variables_clinicas.tex            0.09  [D-005; 1_EDA.ipynb]  …con la etiqueta de patología ($r = -0.03$ para masas, $r = +0.09$ para calcificaciones), lo que indica q…
NO_ENCONTRADO   4.3_variables_clinicas.tex           -0.31  [D-005; 1_EDA.ipynb]  … negativa moderada entre densidad y \textit{subtlety} ($r = -0.31$ para masas), confirmando que las lesio…
NO_ENCONTRADO   4.3_variables_clinicas.tex            1.04  [D-005; 1_EDA.ipynb]  …étrica (1\,819 casos izquierdos vs.\ 1\,749 derechos, ratio 1.04:1), lo que indica ausencia de sesgo de …
NO_ENCONTRADO   4.3_variables_clinicas.tex            0.51  [D-005; 1_EDA.ipynb]  …la correlación más alta con la etiqueta de patología ($r = +0.51$ para masas, $r = +0.43$ para calcifica…
NO_ENCONTRADO   4.3_variables_clinicas.tex            0.43  [D-005; 1_EDA.ipynb]  …con la etiqueta de patología ($r = +0.51$ para masas, $r = +0.43$ para calcificaciones), lo cual es espe…
NO_ENCONTRADO   4.3_variables_clinicas.tex            0.12  [D-005, D-006; 1_EDA.ipynb]  …es prácticamente nulas con la etiqueta de patología ($|r| < 0.12$ en todos los casos), confirmando que e…
EN_CSV(revisar) 4.5_hallazgos.tex                     1.16  [D-005, D-006, D-008, D-009, D-011, D-018]  …o el pipeline experimental. & Sec.~ y M1--M8 \\ Desbalance 1.16:1 en masas y 1.78:1 en calcificaciones …
EN_CSV(revisar) 4.5_hallazgos.tex                     1.78  [D-005, D-006, D-008, D-009, D-011, D-018]  …rimental. & Sec.~ y M1--M8 \\ Desbalance 1.16:1 en masas y 1.78:1 en calcificaciones & Ponderación de c…
```
*Evaluación:* No hay ningún `NO_ENCONTRADO` nuevo. De hecho, los `NO_ENCONTRADO` se redujeron de 19 a 17, `0.870` se validó directamente como `EN_BITACORA` (H-020), y `SIN_FUENTE` se mantiene estrictamente en 0.

---

### B. Compilación de Prueba (`bash Docs/capitulos/compilar_prueba.sh 4_EDA 5_Metodologia A_Anexos`)

```text
Compila sin errores. PDF: /var/folders/0p/s82cs_hd6y38lrx5wgk261kr0000gn/T/tmp.Rlso8zjhlR/prueba.pdf
Referencias o citas sin resolver:
LaTeX Warning: Reference `eq:class_weights' on page 13 undefined on input line 
LaTeX Warning: Reference `eq:class_weights' on page 26 undefined on input line 
LaTeX Warning: Reference `eq:dim_efectiva' on page 25 undefined on input line 2
LaTeX Warning: Reference `eq:fisher_multivariate' on page 25 undefined on input
LaTeX Warning: Reference `eq:g_gen' on page 25 undefined on input line 33.
LaTeX Warning: Reference `eq:g_tra' on page 25 undefined on input line 33.
LaTeX Warning: Reference `eq:spearman' on page 27 undefined on input line 23.
LaTeX Warning: Reference `eq:weighted_bce' on page 26 undefined on input line 1
LaTeX Warning: Reference `sec:lecciones_implementacion' on page 31 undefined on
LaTeX Warning: Reference `sec:metricas' on page 25 undefined on input line 28.
LaTeX Warning: Reference `sec:metricas' on page 25 undefined on input line 33.
LaTeX Warning: Reference `sec:qsvm_ventaja' on page 29 undefined on input line 
LaTeX Warning: Reference `sec:qsvm_ventaja' on page 30 undefined on input line 
LaTeX Warning: Reference `sec:rendimiento_clasificacion' on page 30 undefined o
LaTeX Warning: Reference `sec:restricciones_simulador' on page 30 undefined on 
LaTeX Warning: Reference `sec:restricciones_simulador' on page 31 undefined on 
LaTeX Warning: Reference `sec:resultados' on page 27 undefined on input line 19
```
*Evaluación:* Compilación exitosa sin errores. Todas las referencias provenientes de `4_EDA` y hacia `A_Anexos` (`anx:figuras_eda` y las 8 figuras `fig:class_distribution`, `fig:birads_distribution`, etc.) quedaron **100 % resueltas**. Las advertencias restantes corresponden exclusivamente a ecuaciones de `3_Marco_Teorico` y secciones de `6_Resultados` referenciadas por `5_Metodologia`.

---

### C. Compilación Integral Multi-capítulo (`bash Docs/capitulos/compilar_prueba.sh 3_Marco_Teorico 4_EDA 5_Metodologia 6_Resultados A_Anexos`)

```text
Compila sin errores. PDF: /var/folders/0p/s82cs_hd6y38lrx5wgk261kr0000gn/T/tmp.np10nx2Uyc/prueba.pdf
Referencias o citas sin resolver:
  ninguna
```
*Evaluación:* Al incluir todos los capítulos disponibles junto con los Anexos, **no existe ninguna referencia ni cita sin resolver** en todo el documento consolidado.

---

## 4. Estado de `[VERIFICAR]` y Limitaciones

- **Marcadores `[VERIFICAR]`:** No se introdujo ningún `[VERIFICAR]` en los archivos asignados de `4_EDA/` ni en `A.3.2_figuras_eda.tex`. Todas las cifras, factores y etiquetas utilizadas provienen directamente de `CLAUDE.md`, las entradas D-xxx/H-xxx de la bitácora o los archivos base del EDA.
- **Limitaciones del dataset:** Se conservó y formalizó en el texto visible la declaración explícita de limitaciones estructurales derivadas del EDA (cálculo de características de forma en píxeles crudos ante la ausencia global de `PixelSpacing`, y solapamiento morfológico intrínseco en calcificaciones).
