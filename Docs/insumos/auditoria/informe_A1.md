# Informe de Auditoría A1 · Referencias cruzadas, etiquetas y bibliografía

## Alcance revisado

- `Docs/Technical_Report.tex` (documento maestro raíz).
- Todos los archivos `.tex` incluidos en `Docs/capitulos/` (95 archivos incluidos recursivamente; excluyendo `borrador_*.tex` y `comun/`).
- `Docs/bibliografia.tex` (bibliografía unificada del documento, 80 entradas `\bibitem`).
- Todos los archivos de tablas en `Docs/tablas/*.tex` (19 archivos `.tex`).
- Total de archivos `.tex` analizados en alcance: 115 archivos.
- Log de compilación y auxiliares generados en `/tmp/aud_A1/` (`Technical_Report.log`, `Technical_Report.toc`, `Technical_Report.aux`).

## Comandos ejecutados y salida final

### 1. Compilación LaTeX en `/tmp/aud_A1`
Comando:
```sh
mkdir -p /tmp/aud_A1 && export PATH="/Library/TeX/texbin:$PATH" && pdflatex -interaction=nonstopmode -output-directory /tmp/aud_A1 Technical_Report.tex && pdflatex -interaction=nonstopmode -output-directory /tmp/aud_A1 Technical_Report.tex && pdflatex -interaction=nonstopmode -output-directory /tmp/aud_A1 Technical_Report.tex
```
Salida final:
```
Output written on /tmp/aud_A1/Technical_Report.pdf (194 pages, 14857345 bytes).
Transcript written on /tmp/aud_A1/Technical_Report.log.
Exit code: 0
```

### 2. Ejecución del script de auditoría `a1_refs.py`
Comando:
```sh
/opt/anaconda3/envs/qml_cancer/bin/python Docs/insumos/auditoria/a1_refs.py
```
Salida final:
```
======================================================================
AUDITORÍA A1: REFERENCIAS, ETIQUETAS, BIBLIOGRAFÍA Y COMPILACIÓN
======================================================================

[+] Archivos .tex en alcance analizados: 115
    - Etiquetas definidas: 234
    - Referencias en texto: 165
    - Claves bibliográficas (bibitem): 80
    - Citas en texto (cite): 231

==================================================
1. ETIQUETAS Y REFERENCIAS CRUZADAS
==================================================

[1.1] Etiquetas duplicadas: 0

[1.2] Referencias a etiquetas inexistentes: 0

[1.3] Etiquetas de figuras y tablas NUNCA referenciadas en el texto: 39
  - fig:MexicoBreastCancerStatsByState (capitulos/1_Panorama_General/1.1_introduccion.tex:65)
  - fig:anx_e1_complexity (capitulos/A_Anexos/A.3.1_figuras.tex:62)
  - fig:anx_e2_training_cost (capitulos/A_Anexos/A.3.1_figuras.tex:70)
  - fig:anx_e3_shots (capitulos/A_Anexos/A.3.1_figuras.tex:78)
  - fig:anx_e4_concentration (capitulos/A_Anexos/A.3.1_figuras.tex:86)
  - fig:anx_m2_alignment (capitulos/A_Anexos/A.3.1_figuras.tex:24)
  - fig:anx_m2_examples (capitulos/A_Anexos/A.3.1_figuras.tex:32)
  - fig:anx_m5_circuit_12q (capitulos/A_Anexos/A.3.1_figuras.tex:43)
  - fig:anx_m5_embeddings (capitulos/A_Anexos/A.3.1_figuras.tex:51)
  - fig:anx_m8_spearman_null (capitulos/A_Anexos/A.3.1_figuras.tex:121)
  - fig:anx_x2_pairs (capitulos/A_Anexos/A.3.1_figuras.tex:97)
  - fig:anx_x3_k8_k12 (capitulos/A_Anexos/A.3.1_figuras.tex:105)
  - fig:anx_x4_qsvm_scale (capitulos/A_Anexos/A.3.1_figuras.tex:113)
  - fig:bloch (capitulos/3_Marco_Teorico/3.1.1_qubit.tex:53)
  - fig:circuitos_k4 (capitulos/5_Metodologia/5.7_M5_transformacion.tex:126)
  - fig:m3_clahe_effect (capitulos/6_Resultados/6.1_datos_caracteristicas.tex:80)
  - fig:m3_effect_sizes (capitulos/6_Resultados/6.1_datos_caracteristicas.tex:72)
  - fig:m4_selection_angles (capitulos/6_Resultados/6.1_datos_caracteristicas.tex:132)
  - fig:m5_kernel_concentration (capitulos/6_Resultados/6.2_separabilidad.tex:47)
  - fig:m6_embedding_metrics (capitulos/6_Resultados/6.2_separabilidad.tex:127)
  - fig:m6_geometric_difference (capitulos/6_Resultados/6.2_separabilidad.tex:99)
  - fig:m6_kernel_metrics (capitulos/6_Resultados/6.2_separabilidad.tex:91)
  - fig:m6_tsne (capitulos/6_Resultados/6.2_separabilidad.tex:135)
  - fig:m7_auc (capitulos/6_Resultados/6.3_clasificacion.tex:29)
  - fig:m7_roc_test (capitulos/6_Resultados/6.3_clasificacion.tex:36)
  - fig:m7_sensitivity (capitulos/6_Resultados/6.3_clasificacion.tex:49)
  - fig:m8_classical_vs_quantum (capitulos/6_Resultados/6.5_comparacion.tex:29)
  - fig:m8_oe6_qubits (capitulos/6_Resultados/6.6_restricciones_simulador.tex:19)
  - fig:m8_oe6_shots (capitulos/6_Resultados/6.6_restricciones_simulador.tex:32)
  - fig:m8_spearman (capitulos/6_Resultados/6.5_comparacion.tex:22)
  - fig:x1_selection_auc_vs_k (capitulos/6_Resultados/6.1_datos_caracteristicas.tex:153)
  - fig:x4_67_features (capitulos/6_Resultados/6.4_qsvm_ventaja.tex:29)
  - fig:x4_qsvm_vs_readout (capitulos/6_Resultados/6.4_qsvm_ventaja.tex:19)
  - fig:x6_built_labels (capitulos/6_Resultados/6.4_qsvm_ventaja.tex:63)
  - fig:x6_nested_auc (capitulos/6_Resultados/6.4_qsvm_ventaja.tex:47)
  - fig:x7_theta_draws (capitulos/6_Resultados/6.3_clasificacion.tex:62)
  - fig:x8_trained_theta (capitulos/6_Resultados/6.3_clasificacion.tex:78)
  - tab:req_funcionales (capitulos/5_Metodologia/5.2_requerimientos.tex:37)
  - tab:req_no_funcionales (capitulos/5_Metodologia/5.2_requerimientos.tex:256)

[1.4] Otras etiquetas nunca referenciadas (ecuaciones, secciones, anexos): 102
  - Prefijo 'eq:': 61 etiquetas
  - Prefijo 'sec:': 36 etiquetas
  - Prefijo 'anx:': 5 etiquetas

==================================================
2. BIBLIOGRAFÍA (CITAS Y BIBITEMS)
==================================================

[2.1] Citas a claves sin bibitem: 0

[2.2] Bibitems que NADIE cita: 12
  - BCRF2025 (bibliografia.tex:18)
  - CancerMexico2025 (bibliografia.tex:33)
  - Cristianini2001 (bibliografia.tex:287)
  - Gao2023MammographyReview (bibliografia.tex:113)
  - GlobalCancerStatistics2024_2 (bibliografia.tex:63)
  - Radhi2025QuantumDeepLearning (bibliografia.tex:176)
  - SaezOrtuño2026QuantumKernel (bibliografia.tex:95)
  - StopBreastCancer2025 (bibliografia.tex:23)
  - WHO2025 (bibliografia.tex:5)
  - Windsong2026_EarlyDetection (bibliografia.tex:53)
  - ibmquantum2024learning (bibliografia.tex:268)
  - powers2011evaluation (bibliografia.tex:232)

[2.3] Bibitems con el mismo DOI: 1
  - DOI 10.1103/physrevlett.122.040504: ['Schuld2019QuantumML', 'schuld2019quantum']

[2.4] Bibitems con la misma URL: 3
  - URL https://pressroom.cancer.org/GlobalCancerStatistics2024: ['GlobalCancerStatistics2024', 'GlobalCancerStatistics2024_2']
  - URL https://doi.org/10.1103/PhysRevLett.122.040504: ['Schuld2019QuantumML', 'schuld2019quantum']
  - URL https://proceedings.neurips.cc/paper/2001/hash/1f71e393b3809197ed66df836fe833e5-Abstract.html: ['cristianini2002kernel', 'Cristianini2001']

==================================================
3. PREFIJOS DE REFERENCIAS Y FORMULACIÓN
==================================================

[3.1] Problemas de prefijo detectados: 0
  (No se encontraron referencias del tipo «sección ??», prefijos discordantes tipo «Figura~\\ref{tab:...}», ni ecuaciones referenciadas con \\ref en lugar de \\eqref).

==================================================
4. MENCIONES A SECCIONES ESCRITAS A MANO Y TABLA DE CONTENIDOS
==================================================

Entradas numeradas cargadas del .toc: 137
[4.1] Menciones a mano encontradas: 60
[4.2] Menciones DISCORDANTES o fuera de TOC: 26 (todas en tablas/anexo_e_decisiones.tex correspondientes a numeración desactualizada de TT1: \S\,4.6, \S\,4.7, \S\,4.8, \S\,4.9, \S\,4.10, \S\,6.x, \S\,8.x).
[4.3] Menciones existentes en TOC (pero escritas a mano sin \ref): 34

==================================================
5. VERIFICACIÓN DE RUTAS Y SENSIBILIDAD A MAYÚSCULAS
==================================================

[5.1] Problemas en rutas o diferencias de mayúsculas: 0
  (60 includegraphics, 114 inputs, 14 lstinputlistings verificados existiendo con exacta coincidencia de mayúsculas/minúsculas).

==================================================
6. EXTRACCIÓN DEL LOG DE COMPILACIÓN (/tmp/aud_A1/Technical_Report.log)
==================================================

[6.1] Float too large: 1
  - Float too large by 145.11188pt on input line 68 (capitulos/A_Anexos/A.3.2_figuras_eda.tex:68)

[6.2] Overfull \hbox >= 10pt: 23
  - 14 desbordes (28.7 pt a 134.6 pt) en títulos del Índice de Listados (líneas 2 a 15 de Technical_Report.lol, generados por captions de A.1_codigo.tex en Technical_Report.tex:402).
  - 9 desbordes (10.4 pt a 48.1 pt) en párrafos de texto (3.4.2:87, 3.2.4:28, 3.3.3:19, 3.3.4:10, 3.3.4:19 [x2], 4.4:36, 4.5:28, 6.7:88).
```

### 3. Verificación de estado Git
Comando:
```sh
git -C /Users/alexander_san/TT status --short
```
Salida final:
```
 M Other/orquestacion_noche_2026-10-19.md
?? Docs/insumos/auditoria/W1_articulo.md
?? Docs/insumos/auditoria/a1_refs.py
?? Docs/insumos/auditoria/informe_A1.md
```
Se confirma que únicamente se crearon archivos dentro de `Docs/insumos/auditoria/` (`a1_refs.py` e `informe_A1.md`).

---

## Lista de Hallazgos

### A1-01 · ALTA · Referencias cruzadas desactualizadas
- Ubicación: `Docs/tablas/anexo_e_decisiones.tex:30` (y ss., líneas 30--57)
- Texto: «`D-013 & Firme & Punto de operación: k=12 qubits, reps=1 & \S\,4.6, \S\,4.7 \\`» (así como menciones a `\S\,4.8`, `\S\,4.9`, `\S\,4.10`, `\S\,6.x`, `\S\,8.x`, `\S\,4.1–\S\,4.9`)
- Problema: La columna de ubicación en el reporte dentro de la tabla de decisiones metodológicas cita la numeración de capítulos de TT1 (donde Metodología correspondía al capítulo 4). En TT2 el capítulo 4 es EDA (que concluye en §4.5) y Metodología es el capítulo 5, por lo que las referencias apuntan a subsecciones inexistentes y mantienen comodines sin resolver («§6.x», «§8.x»).
- Evidencia: En `Technical_Report.toc`, las subsecciones del capítulo 4 son únicamente 4.1 a 4.5; los módulos experimentales M2 a M8 se localizan en las secciones 5.4 a 5.10 del capítulo 5.
- Propuesta: Reemplazar las menciones por las secciones vigentes de TT2 (§5.4 para M2, §5.5 para M3, §5.6 para M4, §5.7 para M5, §5.8 para M6, §5.9 para M7, §5.10 para M8) y desglosar los comodines «§6.x» en las secciones respectivas de Resultados (§6.1 a §6.8).

### A1-02 · ALTA · Entrada bibliográfica duplicada
- Ubicación: `Docs/bibliografia.tex:180` y `Docs/bibliografia.tex:242`
- Texto: «`\bibitem{Schuld2019QuantumML}`» (línea 180) y «`\bibitem{schuld2019quantum}`» (línea 242)
- Problema: Existe una referencia bibliográfica idéntica duplicada con distinta clave para el artículo de Schuld & Killoran (2019), compartiendo título (*Quantum machine learning in feature Hilbert spaces*), autores, revista (*Physical Review Letters*, 122(4), 040504) e idéntico DOI (`10.1103/PhysRevLett.122.040504`).
- Evidencia: Comparación literal de las líneas 180--184 y 242--246 de `Docs/bibliografia.tex`. Ambas claves se citan por separado en el texto (`Schuld2019QuantumML` en §2.1.3 y `schuld2019quantum` en §2.1.6).
- Propuesta: Eliminar la entrada duplicada `\bibitem{schuld2019quantum}` de `Docs/bibliografia.tex` y sustituir sus citas en el texto por `\cite{Schuld2019QuantumML}`.

### A1-03 · MEDIA · Entrada bibliográfica redundante no citada
- Ubicación: `Docs/bibliografia.tex:63`
- Texto: «`\bibitem{GlobalCancerStatistics2024_2}`»
- Problema: La entrada es una variante casi idéntica de `GlobalCancerStatistics2024` (línea 28) que referencia la misma fuente y URL de la American Cancer Society, y nunca es citada en ningún capítulo del documento.
- Evidencia: `Docs/bibliografia.tex:28` define `GlobalCancerStatistics2024`; `Docs/bibliografia.tex:63` define `GlobalCancerStatistics2024_2` con la misma URL (`https://pressroom.cancer.org/GlobalCancerStatistics2024`); búsqueda de `\cite{GlobalCancerStatistics2024_2}` arroja 0 ocurrencias.
- Propuesta: Suprimir la entrada huérfana y duplicada `GlobalCancerStatistics2024_2` de `Docs/bibliografia.tex`.

### A1-04 · MEDIA · Entrada bibliográfica duplicada no citada
- Ubicación: `Docs/bibliografia.tex:287`
- Texto: «`\bibitem{Cristianini2001}`»
- Problema: Registra el mismo trabajo de Cristianini et al. sobre *kernel-target alignment* que la entrada `cristianini2002kernel` (línea 218), con idéntica URL de NeurIPS, pero la clave `Cristianini2001` no recibe ninguna cita en el reporte.
- Evidencia: `Docs/bibliografia.tex` líneas 218 y 287 comparten la URL `https://proceedings.neurips.cc/paper/2001/hash/1f71e393b3809197ed66df836fe833e5-Abstract.html`; el texto técnico cita exclusivamente `cristianini2002kernel` en §3.4.1.
- Propuesta: Eliminar la entrada redundante `Cristianini2001` de `Docs/bibliografia.tex`.

### A1-05 · MEDIA · Entradas bibliográficas huérfanas
- Ubicación: `Docs/bibliografia.tex:5, 18, 23, 33, 53, 95, 113, 176, 232, 268`
- Texto: «`\bibitem{WHO2025}`, `\bibitem{BCRF2025}`, `\bibitem{StopBreastCancer2025}`, `\bibitem{CancerMexico2025}`, `\bibitem{Windsong2026_EarlyDetection}`, `\bibitem{SaezOrtuño2026QuantumKernel}`, `\bibitem{Gao2023MammographyReview}`, `\bibitem{Radhi2025QuantumDeepLearning}`, `\bibitem{powers2011evaluation}`, `\bibitem{ibmquantum2024learning}`»
- Problema: Diez referencias bibliográficas se encuentran compiladas en `Docs/bibliografia.tex` pero no son referenciadas mediante `\cite` en ninguna parte del texto.
- Evidencia: Análisis de citas cruzadas en los 115 archivos `.tex` del alcance; recuento de citas para estas 10 claves es exactamente cero.
- Propuesta: Vincular cada referencia en la sección correspondiente (p. ej. datos epidemiológicos en §1.1, métricas en §3.4.7) o retirarlas de `bibliografia.tex` para depurar el listado final.

### A1-06 · ALTA · Figuras no referenciadas en capítulos principales
- Ubicación: `Docs/capitulos/6_Resultados/` (y `Docs/capitulos/5_Metodologia/5.7_M5_transformacion.tex:126`, `Docs/capitulos/1_Panorama_General/1.1_introduccion.tex:65`, `Docs/capitulos/3_Marco_Teorico/3.1.1_qubit.tex:53`)
- Texto: «`\label{fig:m3_effect_sizes}`, `\label{fig:m3_clahe_effect}`, `\label{fig:m4_selection_angles}`, `\label{fig:x1_selection_auc_vs_k}`, `\label{fig:m5_kernel_concentration}`, `\label{fig:m6_kernel_metrics}`, `\label{fig:m6_geometric_difference}`, `\label{fig:m6_embedding_metrics}`, `\label{fig:m6_tsne}`, `\label{fig:m7_auc}`, `\label{fig:m7_roc_test}`, `\label{fig:m7_sensitivity}`, `\label{fig:x7_theta_draws}`, `\label{fig:x8_trained_theta}`, `\label{fig:x4_qsvm_vs_readout}`, `\label{fig:x4_67_features}`, `\label{fig:x6_nested_auc}`, `\label{fig:x6_built_labels}`, `\label{fig:m8_spearman}`, `\label{fig:m8_classical_vs_quantum}`, `\label{fig:m8_oe6_qubits}`, `\label{fig:m8_oe6_shots}`, `\label{fig:circuitos_k4}`, `\label{fig:MexicoBreastCancerStatsByState}`, `\label{fig:bloch}`»
- Problema: 25 figuras centrales del desarrollo experimental y marco teórico están insertadas en los capítulos correspondientes pero ninguna es referenciada en la prosa mediante `\ref`.
- Evidencia: Registro de `a1_refs.py` sección 1.3; de 57 figuras con etiqueta en el documento, 37 no tienen ninguna llamada `\ref` (25 en capítulos 1 a 6 y 12 en Anexos).
- Propuesta: Incorporar en el texto explicativo de cada subsección la llamada a la figura correspondiente (p. ej. «(Figura~\ref{fig:m5_kernel_concentration})»).

### A1-07 · MEDIA · Figuras complementarias del Anexo C no referenciadas
- Ubicación: `Docs/capitulos/A_Anexos/A.3.1_figuras.tex:24, 32, 43, 51, 62, 70, 78, 86, 97, 105, 113, 121`
- Texto: «`\label{fig:anx_m2_alignment}`, `\label{fig:anx_m2_examples}`, `\label{fig:anx_m5_circuit_12q}`, `\label{fig:anx_m5_embeddings}`, `\label{fig:anx_e1_complexity}`, `\label{fig:anx_e2_training_cost}`, `\label{fig:anx_e3_shots}`, `\label{fig:anx_e4_concentration}`, `\label{fig:anx_x2_pairs}`, `\label{fig:anx_x3_k8_k12}`, `\label{fig:anx_x4_qsvm_scale}`, `\label{fig:anx_m8_spearman_null}`»
- Problema: Las 12 figuras del Anexo C (Figuras complementarias) tienen etiquetas asignadas pero ninguna es citada ni en el cuerpo principal del reporte ni en el texto introductorio de cada subsección del anexo.
- Evidencia: `a1_refs.py` sección 1.3.
- Propuesta: Citar explícitamente cada figura en los párrafos introductorios del anexo o mediante referencias de apoyo en los capítulos 5 y 6.

### A1-08 · MEDIA · Tablas de requerimientos del sistema no referenciadas
- Ubicación: `Docs/capitulos/5_Metodologia/5.2_requerimientos.tex:37` y `Docs/capitulos/5_Metodologia/5.2_requerimientos.tex:256`
- Texto: «`\label{tab:req_funcionales}`» y «`\label{tab:req_no_funcionales}`»
- Problema: Las tablas que consolidan los 16 requerimientos funcionales y 8 no funcionales no son citadas como entidad tabular en el texto de la sección.
- Evidencia: `a1_refs.py` sección 1.3; el texto describe cada requerimiento individualmente («RF-01...») pero omite referenciar la tabla («Tabla~\ref{tab:req_funcionales}»).
- Propuesta: Agregar en los párrafos introductorios de las subsecciones 5.2.1 y 5.2.2 la referencia a la tabla correspondiente.

### A1-09 · MEDIA · Duplicación de entradas en la Tabla de Contenidos (TOC)
- Ubicación: `Docs/capitulos/6_Resultados/6.0_introduccion.tex:8`, `Docs/capitulos/7_Conclusiones/7.0_introduccion.tex:9`, `Docs/capitulos/8_Trabajo_Futuro/8.0_introduccion.tex:10`
- Texto: «`\section{Resultados}\addcontentsline{toc}{section}{Resultados}`», «`\section{Conclusiones}\addcontentsline{toc}{section}{Conclusiones}`», «`\section{Trabajo a Futuro}\addcontentsline{toc}{section}{Trabajo a Futuro}`»
- Problema: Los capítulos 6, 7 y 8 ejecutan un comando `\addcontentsline{toc}{section}{...}` inmediatamente posterior al comando estándar numerado `\section{...}`, produciendo una entrada doble (una con numeración de capítulo y otra sin número) en el índice de contenido del reporte.
- Evidencia: En `/tmp/aud_A1/Technical_Report.toc`, las líneas 95--96, 105--106 y 113--114 duplican consecutivamente cada uno de los tres capítulos.
- Propuesta: Retirar la línea `\addcontentsline{toc}{section}{...}` en `6.0_introduccion.tex`, `7.0_introduccion.tex` y `8.0_introduccion.tex`.

### A1-10 · MEDIA · Menciones de secciones escritas a mano sin `\ref`
- Ubicación: `Docs/capitulos/2_Antecedentes/2.0_introduccion.tex:12`
- Texto: «`Las secciones~2.1.1 y 2.1.2 resumen el aprendizaje automático clásico... Las secciones~2.1.3 y 2.1.4 presentan los fundamentos... sección~2.1.5... Las secciones~2.1.6 y 2.1.7... La sección~2.1.8... y la sección~2.1.9...`»
- Problema: Se escribieron a mano seis referencias a secciones del capítulo 2 en lugar de vincularlas mediante el comando `\ref` a sus respectivas etiquetas (`sec:ml_clasico`, `sec:deep_learning`, etc.).
- Evidencia: `Docs/capitulos/2_Antecedentes/2.0_introduccion.tex:12`.
- Propuesta: Sustituir los números estáticos por `\ref{sec:...}` para preservar la consistencia dinámica del documento ante eventuales reordenamientos.

### A1-11 · MEDIA · Elemento flotante desborda la altura de página
- Ubicación: `Docs/capitulos/A_Anexos/A.3.2_figuras_eda.tex:68`
- Texto: «`\includegraphics[width=0.7\textwidth]{Figures/D4_sample_gallery.png}`»
- Problema: El entorno `figure` que alberga a `fig:sample_gallery` excede la altura vertical útil de la página en 145.11 pt durante la compilación, generando desbordamiento hacia el margen inferior.
- Evidencia: `Technical_Report.log`: `LaTeX Warning: Float too large for page by 145.11188pt on input line 68.`
- Propuesta: Ajustar la escala de la imagen (p. ej., `width=0.62\textwidth` o fijar `max height=0.42\textheight`) para que el bloque completo quepa holgadamente en la página.

### A1-12 · BAJA · Desbordes horizontales (Overfull `\hbox` > 10 pt) en Índice de Listados
- Ubicación: `Docs/capitulos/A_Anexos/A.1_codigo.tex:36, 44, 56, 67, 75, 83, 94, 102, 113, 121, 132, 140, 151, 159`
- Texto: «`\lstinputlisting[style=tt, caption={... (\texttt{Code/...})}, label={...}]{...}`»
- Problema: Los epígrafes de los listados 2 al 15 incluyen rutas de archivos con `\texttt` que no admiten guionado automático al maquetarse en el Índice de Listados (`\lstlistoflistings` en `Docs/Technical_Report.tex:402`), generando 14 desbordes horizontales de entre 28.7 pt y 134.6 pt.
- Evidencia: `Technical_Report.log` y reporte de `a1_refs.py` sección 6.2 (Overfull `\hbox` en líneas 2 a 15 de `Technical_Report.lol`).
- Propuesta: Configurar un título breve sin la ruta en monoespacio para la tabla de contenidos mediante el argumento opcional de caption: `caption={[Título corto]Título completo con ruta}`.

### A1-13 · BAJA · Desbordes horizontales (Overfull `\hbox` > 10 pt) en párrafos de texto
- Ubicación:
  - `Docs/capitulos/3_Marco_Teorico/3.4.2_geometric_difference.tex:87` (28.46 pt)
  - `Docs/capitulos/3_Marco_Teorico/3.2.4_paulifeaturemap.tex:28` (29.79 pt)
  - `Docs/capitulos/3_Marco_Teorico/3.3.3_integracion.tex:19` (10.39 pt)
  - `Docs/capitulos/3_Marco_Teorico/3.3.4_implementacion_qiskit.tex:10` (19.66 pt)
  - `Docs/capitulos/3_Marco_Teorico/3.3.4_implementacion_qiskit.tex:19` (48.07 pt y 20.75 pt)
  - `Docs/capitulos/4_EDA/4.4_imagenes_dicom.tex:36` (29.85 pt)
  - `Docs/capitulos/4_EDA/4.5_hallazgos.tex:28` (18.75 pt)
  - `Docs/capitulos/6_Resultados/6.7_lecciones_implementacion.tex:88` (14.13 pt)
- Texto: «`\texttt{pauli_feature_map(paulis=['Y', 'ZZ'], reps=1)}`», «`SecondaryCaptureDeviceManufacturer`», «`https://creativecommons.org/...`», entre otros términos monoespaciados extensos.
- Problema: Cadenas de código o identificadores técnicos extensos sin puntos de división provocan que 9 renglones sobresalgan del margen derecho de la caja de texto.
- Evidencia: `Technical_Report.log` y reporte detallado de `a1_refs.py` sección 6.2.
- Propuesta: Añadir `\allowbreak` dentro de las cadenas técnicas o reestructurar la frase para permitir un salto de línea natural antes del elemento indivisible.

### A1-14 · BAJA · Referencia ambigua a anexo en texto
- Ubicación: `Docs/capitulos/A_Anexos/A.3.1_figuras.tex:14`
- Texto: «`del conjunto de datos se presentan en el anexo correspondiente.`»
- Problema: Se formula una referencia vaga («anexo correspondiente») en lugar de emplear el comando `\ref` apuntando a la etiqueta formal del Anexo C o a la sección del EDA.
- Evidencia: `Docs/capitulos/A_Anexos/A.3.1_figuras.tex:14`.
- Propuesta: Sustituir por «en la sección~\ref{sec:eda_figuras}» o el anexo pertinente.

---

## Conteo por severidad

- **ALTA**: 3
- **MEDIA**: 8
- **BAJA**: 3
- **Total de hallazgos**: 14
