# Informe de Auditoría A3 · Terminología, notación y estilo

**Auditoría nocturna del Trabajo Terminal 2026-B039 (2026-10-18/19)**  
**Repositorio:** `/Users/alexander_san/TT`  
**Documento auditado:** `Docs/Technical_Report.tex` y todos los archivos `.tex` incluidos (115 archivos en total).  
**Modalidad:** Solo lectura del repositorio; informe generado exclusivamente en `Docs/insumos/auditoria/informe_A3.md`.

---

## 1. Alcance revisado

Se verificaron la totalidad de los archivos `.tex` compilados en `Docs/Technical_Report.tex`:
- **Documento maestro y preliminares:** `Docs/Technical_Report.tex`, `Docs/capitulos/0_Preliminares/resumen.tex`, `Docs/capitulos/0_Preliminares/abstract.tex`.
- **Capítulo 1 (Panorama General):** `1.0_introduccion.tex`, `1.1_introduccion.tex`, `1.2_planteamiento.tex`, `1.3_justificacion.tex`, `1.4_objetivos.tex`, `1.5_alcance.tex`.
- **Capítulo 2 (Antecedentes):** `2.0_introduccion.tex`, `2.1.1_ml_clasico.tex` a `2.1.9_tabla_comparativa.tex`.
- **Capítulo 3 (Marco Teórico):** `3.0_introduccion.tex`, `3.1.1_qubit.tex` a `3.1.4_medicion.tex`, `3.2.1_pqc.tex` a `3.2.7_parameter_shift.tex`, `3.3.1_mlp.tex` a `3.3.4_implementacion_qiskit.tex`, `3.4.0_metricas.tex` a `3.4.8_spearman.tex`, `3.5.0_representaciones_clasicas.tex` a `3.5.6_kernel_proyectado.tex`.
- **Capítulo 4 (Análisis Exploratorio de Datos):** `4.0_introduccion.tex` a `4.5_hallazgos.tex`.
- **Capítulo 5 (Metodología):** `5.0_introduccion.tex` a `5.11_experimentos_complementarios.tex`.
- **Capítulo 6 (Resultados):** `6.0_introduccion.tex` a `6.8_sintesis.tex`.
- **Capítulo 7 (Conclusiones):** `7.0_introduccion.tex` a `7.6_limitaciones.tex`.
- **Capítulo 8 (Trabajo Futuro):** `8.0_introduccion.tex`, `8.1_lineas.tex`.
- **Referencias y Glosario:** `Docs/bibliografia.tex`, `Docs/capitulos/G_Glosario/glosario.tex`.
- **Anexos:** `Docs/capitulos/A_Anexos/A.0_introduccion.tex` a `A.5_decisiones.tex`.
- **Tablas de resultados e índices:** `Docs/tablas/*.tex` (19 archivos de tabla incluidos con `\input`).

---

## 2. Comandos ejecutados y salida resumida

1. **Rastreo y consolidación de archivos en alcance:**
   - Comando: `python3 scratch/check_terms.py`
   - Salida: 95 archivos incluidos directamente en `Docs/Technical_Report.tex` + 19 tablas anidadas + documento principal = 115 archivos `.tex` en alcance.
2. **Auditoría de módulos (M1–M8), condiciones (C1–C5) y objetivos (OE-1–OE-6):**
   - Comandos: `python3 scratch/check_point1.py`, `python3 scratch/check_modules.py`, `python3 scratch/check_c5.py`, `python3 scratch/check_oes.py`.
   - Salida: D-030 rige la estructura de módulos (M6 separabilidad, M7 clasificación, M8 evaluación). Se detectó uso de «distancia de Fisher» en lugar de «razón de Fisher» en `resumen.tex:4` y `6.8_sintesis.tex:31` (en conflicto con D-033 y §1.4).
3. **Auditoría de nombres de API (Qiskit 2.x):**
   - Comando: `python3 scratch/check_point2.py`
   - Salida: Se identificaron usos de las clases deprecadas `ZZFeatureMap` y `PauliFeatureMap` en texto visible de objetivos (§1.4), títulos de sección (§3.2.3, §3.2.4), síntesis (§6.8), conclusiones (§7.1) y bibliografía (`bibliografia.tex:196`). `TorchConnector` y `EstimatorQNN` se emplean exclusivamente como opciones descartadas y comparativas.
4. **Auditoría de notación matemática ($k$ vs $n$, $K_Q$ vs $k_Q$, $g$, $\boldsymbol\theta$):**
   - Comandos: `python3 scratch/check_math.py`, `python3 scratch/check_knN.py`, `python3 scratch/check_sample_size.py`.
   - Salida: Conflicto notacional severo en §3.2 ($n$ qubits y $n$ dimensiones en lugar de $k=12$); $k_Q$ minúscula en eq. (34) de §3.2.2; índice $k$ mudo de suma hasta $n$ en §3.5.6; uso indistinto de $g_{CQ}$ para la fórmula regularizada en RF-16; $\theta$ escalar en leyendas de tablas x7 y x8.
5. **Auditoría de identificadores internos visibles (D-xxx, H-xxx, Q-xxx, X1–X9, B1–B3):**
   - Comandos: `python3 scratch/check_point4.py`, `python3 scratch/check_ids_main.py`.
   - Salida: Cero D-xxx, H-xxx o Q-xxx en capítulos 0 a 8. D-001 a D-040 aparecen únicamente en Anexo E, pero con referencias a secciones del esquema obsoleto del reporte (`\S 4.x` en lugar de `\S 5.x`). B1, B3, X1, X3 aparecen en prosa de Resultados (§6) sin referencia cruzada explícita.
6. **Auditoría de comillas, guiones y rayas:**
   - Comandos: `python3 scratch/check_point5.py`, `python3 scratch/check_unicode_dashes.py`.
   - Salida: Sin comillas angulares «» ni rectas " en texto principal. Carácter Unicode `–` (U+2013) en `anexo_e_decisiones.tex:47` y `—` (U+2014) en celdas de tablas de resultados y paquetes. Sin incisos no permitidos en prosa.
7. **Auditoría de lenguaje sobredimensionado:**
   - Comandos: `python3 scratch/check_point6.py`, `python3 scratch/check_high_overstated.py`.
   - Salida: Cero usos de «de manera contundente», «revolucionario» o «sin excepción». Términos «ventaja cuántica» acotados rigurosamente como potencial o ausente. En §3.1.2 se afirma incorrectamente que $\theta$ son «parámetros entrenables», en contradicción con Arquitectura B.
8. **Auditoría de restos de TT1 y diseño anterior:**
   - Comandos: `python3 scratch/check_point7.py`, `python3 scratch/check_future_verbs.py`.
   - Salida: No hay verbos en tiempo futuro para trabajo concluido. WDBC, CLAHE y 224x224 aparecen únicamente como referencias de descarte o literatura. Detección de duplicación textual consecutiva de párrafos de t-SNE en §3.4.6.
9. **Auditoría de ortografía, concordancia y términos en inglés:**
   - Comandos: `python3 scratch/check_point8.py`, `python3 scratch/check_more_accents.py`, `python3 scratch/check_concordance.py`, `python3 scratch/check_point9.py`.
   - Salida: Acentuación y concordancia correctas. Alternancia no uniforme de «features» sin cursiva en §4.5 y §5.2 frente a «características». Términos en inglés (`ansatz`, `baseline`, `pipeline`) sin cursiva en figuras y párrafos iniciales.

---

## 3. Lista de hallazgos

### A3-01 · MEDIA · Nombres de módulos, condiciones y objetivos específicos
- Ubicación: `Docs/capitulos/0_Preliminares/resumen.tex:4` (y `Docs/capitulos/0_Preliminares/abstract.tex:2`, `Docs/capitulos/6_Resultados/6.8_sintesis.tex:31`)
- Texto: «la dimensión efectiva, el índice de Davies-Bouldin y la distancia de Fisher;»
- Problema: Emplea la denominación «distancia de Fisher» (y «Fisher distance») en lugar del término formal «razón de Fisher» (o «razón multivariante de Fisher») adoptado en D-033 y formalizado en §1.4.
- Evidencia: En `Docs/capitulos/1_Panorama_General/1.4_objetivos.tex:8`, el autor registró explícitamente: `«distancia Fisher» → «razón de Fisher» (D-033)`. En §1.4.1 (l. 25-26), §1.4.2 (OE-3, l. 54), §3.4.5 y §5.2 (RF-17), se define unívocamente como «razón de Fisher» ($J = \Delta\boldsymbol\mu^\top S_W^{-1}\Delta\boldsymbol\mu$), ya que es un cociente adimensional de varianzas y no una métrica de distancia euclidiana.
- Propuesta: Sustituir «distancia de Fisher» por «razón de Fisher» en `resumen.tex:4` y `6.8_sintesis.tex:31`, y «the Fisher distance» por «the Fisher ratio» en `abstract.tex:2`.

### A3-02 · MEDIA · Nombres de API (Qiskit 2.x)
- Ubicación: `Docs/capitulos/1_Panorama_General/1.4_objetivos.tex:22` (y líneas 44, 46)
- Texto: «implementadas mediante \textit{ZZFeatureMap} y \textit{PauliFeatureMap} en Qiskit»
- Problema: Cita las clases en PascalCase deprecadas de Qiskit como tecnología en uso en los objetivos general y específicos, en lugar de las funciones `zz_feature_map` y `pauli_feature_map` vigentes en Qiskit 2.x.
- Evidencia: `Docs/capitulos/3_Marco_Teorico/3.3.4_implementacion_qiskit.tex:19` y `Docs/capitulos/6_Resultados/6.7_lecciones_implementacion.tex:88-89` declaran que `ZZFeatureMap` y `PauliFeatureMap` están deprecadas en Qiskit 2.x en favor de las funciones `zz_feature_map()` y `pauli_feature_map()`.
- Propuesta: Modificar la línea 22 para referir «las funciones \texttt{zz\_feature\_map} y \texttt{pauli\_feature\_map} en Qiskit», y en líneas 44 y 46 referir «circuito de mapa de características ZZ (\texttt{zz\_feature\_map})» y «circuito de mapa de Pauli (\texttt{pauli\_feature\_map})».

### A3-03 · BAJA · Nombres de API (Qiskit 2.x)
- Ubicación: `Docs/capitulos/3_Marco_Teorico/3.2.3_zzfeaturemap.tex:6` y `Docs/capitulos/3_Marco_Teorico/3.2.4_paulifeaturemap.tex:6`
- Texto: `\subsubsection{\textit{ZZFeatureMap}: evolución de Pauli-Z de segundo orden}` y `\subsubsection{\textit{PauliFeatureMap}: generalización por elección de los operadores de Pauli}`
- Problema: Los títulos de las subsubsecciones utilizan la nomenclatura de clase obsoleta en lugar del nombre funcional o conceptual del circuito.
- Evidencia: En la línea 12 de `3.2.3_zzfeaturemap.tex` se indica que el circuito está disponible en Qiskit como `zz_feature_map`.
- Propuesta: Renombrar los encabezados a «Mapa de características ZZ (\texttt{zz\_feature\_map})» y «Mapa de características de Pauli generalizado (\texttt{pauli\_feature\_map})».

### A3-04 · BAJA · Nombres de API (Qiskit 2.x)
- Ubicación: `Docs/bibliografia.tex:196`
- Texto: «IBM Quantum. (2024). Qiskit Circuit Library: \texttt{zz\_feature\_map} and \texttt{PauliFeatureMap}. IBM Quantum Documentation.»
- Problema: Combina en una misma entrada bibliográfica el nombre funcional en minúsculas `zz_feature_map` con la clase deprecada en PascalCase `PauliFeatureMap`.
- Evidencia: La documentación oficial de Qiskit Circuit Library titula de manera uniforme `zz_feature_map` y `pauli_feature_map`.
- Propuesta: Reemplazar `\texttt{PauliFeatureMap}` por `\texttt{pauli\_feature\_map}`.

### A3-05 · MEDIA · Nombres de API (Qiskit 2.x)
- Ubicación: `Docs/capitulos/6_Resultados/6.8_sintesis.tex:29` y `Docs/capitulos/7_Conclusiones/7.1_respuesta.tex:11`
- Texto: `(C1 crudo, C2 PCA lineal, C3 Kernel PCA RBF, C4 ZZFeatureMap, C5 PauliFeatureMap)` en `6.8_sintesis.tex:29`, y `implementadas con \textit{ZZFeatureMap} y \textit{PauliFeatureMap}` en `7.1_respuesta.tex:11`
- Problema: Identifica las condiciones C4 y C5 y formula la conclusión de la tesis usando las clases deprecadas en lugar de los nombres de función o la descripción conceptual de los mapas cuánticos.
- Evidencia: Regla 2 de `Docs/insumos/auditoria/A3_terminologia.md` (`ZZFeatureMap`/`PauliFeatureMap` solo si se habla de la clase deprecada).
- Propuesta: Cambiar en `6.8_sintesis.tex:29` a `(C1 crudo, C2 PCA lineal, C3 Kernel PCA RBF, C4 mapa ZZ, C5 mapa Pauli Y-ZZ)` y en `7.1_respuesta.tex:11` a `implementadas con los mapas cuánticos \texttt{zz\_feature\_map} y \texttt{pauli\_feature\_map}`.

### A3-06 · ALTA · Notación matemática
- Ubicación: `Docs/capitulos/3_Marco_Teorico/3.2.2_feature_map.tex:13-20`, `3.2.5_ansatz.tex:25`, `3.2.6_quantum_embedding.tex:16-18` y `Docs/capitulos/1_Panorama_General/1.1_introduccion.tex:151`
- Texto: `\phi: \mathbb{R}^k \rightarrow \mathcal{H}, \qquad \mathbf{x} \mapsto |\phi(\mathbf{x})\rangle = U(\mathbf{x})\,|0\rangle^{\otimes n}` (eq. 13-16 de 3.2.2); `$n = 12$ qubits` (l. 25 de 3.2.5); `\mathbf{e}(\mathbf{x}, \boldsymbol{\theta}) \in [-1, 1]^n` (eq. 18 de 3.2.6); `\phi: \mathbb{R}^n \rightarrow \mathcal{H}` (l. 151 de 1.1)
- Problema: Se utiliza la letra $n$ para denotar el número de qubits y la dimensión del vector de embedding en el Marco Teórico, mientras que en todo el resto del reporte el número de características seleccionadas y de qubits del circuito se define unívocamente con el símbolo $k$ ($k = 12$). En `3.2.2_feature_map.tex:13-16` se mezclan $k$ y $n$ en la misma ecuación.
- Evidencia: En §1.4.2 (OE-1 y OE-2), §5.1 (l. 44, 146), §5.2 (RF-08, RF-13), §6.1, §6.8 y en las decisiones D-013 y D-030, la dimensión de entrada y el registro de qubits es $k = 12$. La mezcla con $n$ induce a pensar que el número de qubits es distinto al número de variables seleccionadas.
- Propuesta: Unificar la notación en §1.1 y §3.2 reemplazando $n$ por $k$ como número de qubits y longitud del vector de embedding ($|0\rangle^{\otimes k}$, $\mathcal{H} = \mathbb{C}^{2^k}$, $k = 12$ qubits, $\mathbf{e} \in [-1, 1]^k$, $\phi: \mathbb{R}^k \to \mathcal{H}$).

### A3-07 · MEDIA · Notación matemática
- Ubicación: `Docs/capitulos/3_Marco_Teorico/3.2.2_feature_map.tex:34`
- Texto: `k_Q(\mathbf{x}, \mathbf{x}') = \left|\langle\phi(\mathbf{x})|\phi(\mathbf{x}')\rangle \right|^2`
- Problema: Define la función de kernel cuántico con minúscula $k_Q$, mientras que en `3.1.4_medicion.tex:46`, `3.2.6_quantum_embedding.tex:28`, `3.4.2_geometric_difference.tex:9` y en todo el resto del reporte se utiliza sistemáticamente la mayúscula $K_Q$ para la función y matriz de kernel cuántico.
- Evidencia: `3.1.4_medicion.tex:46` escribe `K_Q(\mathbf{x}, \mathbf{x}') = |\langle \phi(\mathbf{x}) | \phi(\mathbf{x}') \rangle|^2`; `5.1_descripcion_general.tex:67, 72, 137` y `tablas/m6_separabilidad_kernels.tex:24` usan $K_Q$.
- Propuesta: Reemplazar $k_Q(\mathbf{x}, \mathbf{x}')$ por $K_Q(\mathbf{x}, \mathbf{x}')$ en la ecuación~\eqref{eq:quantum_kernel}.

### A3-08 · MEDIA · Notación matemática
- Ubicación: `Docs/capitulos/3_Marco_Teorico/3.5.6_kernel_proyectado.tex:19`
- Texto: `k^{\mathrm{PQ}}(\mathbf{x}, \mathbf{x}') = \exp\!\left(-\gamma \sum_{k=1}^{n} \bigl\lVert \rho_k(\mathbf{x}) - \rho_k(\mathbf{x}') \bigr\rVert_F^2\right)`
- Problema: Emplea la letra $k$ como índice mudo de sumatoria y la letra $n$ como límite superior (número total de qubits), invirtiendo la convención establecida en el resto del reporte donde $k$ es el número total de qubits.
- Evidencia: En todo el informe, $k$ representa la dimensión total ($k = 12$ qubits). Usar $k$ como índice de suma hasta $n$ choca con la convención del trabajo.
- Propuesta: Cambiar el índice de sumatoria a $j = 1$ hasta $k$: `\sum_{j=1}^{k} \bigl\lVert \rho_j(\mathbf{x}) - \rho_j(\mathbf{x}') \bigr\rVert_F^2`.

### A3-09 · MEDIA · Notación matemática
- Ubicación: `Docs/capitulos/5_Metodologia/5.2_requerimientos.tex:189` (RF-16) frente a `Docs/capitulos/3_Marco_Teorico/3.4.2_geometric_difference.tex:36, 63`
- Texto: `$g_{CQ}=\sqrt{\bigl\|\sqrt{K_Q}\,\sqrt{K_C}\,(K_C+\lambda I)^{-2}\sqrt{K_C}\,\sqrt{K_Q}\bigr\|_\infty}$`
- Problema: Asigna el símbolo $g_{CQ}$ a la fórmula regularizada en RF-16, mientras que en la teoría (§3.4.2, ec. 14) $g_{CQ}$ representa exclusivamente la versión no regularizada (con $K_C^{-1}$), y la versión regularizada se define como $g_{\text{gen}}$ y la métrica mínima final como $g$.
- Evidencia: En `3.4.2_geometric_difference.tex:14`, $g_{CQ} = \sqrt{\|\sqrt{K_Q} K_C^{-1} \sqrt{K_Q}\|_\infty}$, mientras que en ec. 36 la versión regularizada es $g_{\text{gen}}(K_C, K_Q; \lambda)$ y en ec. 63 el mínimo sobre la batería es $g$.
- Propuesta: Sustituir $g_{CQ}$ por $g_{\text{gen}}$ (o $g$) en RF-16 para mantener coherencia con la sección 3.4.2.

### A3-10 · BAJA · Notación matemática
- Ubicación: `Docs/tablas/x7_sorteos_theta.tex:5`, `Docs/tablas/x8_theta_entrenado.tex:5, 22`, y `Docs/tablas/anexo_e_decisiones.tex:31`
- Texto: `sorteo de $\theta$`, `entrenar $\theta$ junto con el MLP`, `$\theta$ fijo`
- Problema: Emplea la letra escalar $\theta$ sin negrita en los títulos y notas de tablas para referirse al vector de 24 parámetros del ansatz, cuando en el texto teórico y metodológico se define unívocamente como vector en negrita $\boldsymbol{\theta} \in \mathbb{R}^{24}$.
- Evidencia: `Docs/capitulos/3_Marco_Teorico/3.2.5_ansatz.tex:27` define $\boldsymbol{\theta} \in \mathbb{R}^{24}$, y `5.1_descripcion_general.tex:66, 71` usa $\boldsymbol{\theta}$.
- Propuesta: Escribir $\boldsymbol{\theta}$ en negrita en las leyendas de las tablas `x7_sorteos_theta.tex`, `x8_theta_entrenado.tex` y en `anexo_e_decisiones.tex`.

### A3-11 · MEDIA · Notación matemática
- Ubicación: `Docs/capitulos/3_Marco_Teorico/3.5.2_pca.tex:13` y `Docs/capitulos/6_Resultados/6.7_lecciones_implementacion.tex:64`
- Texto: `\Sigma = \frac{1}{n-1}\,\tilde{X}^{\top}\tilde{X}` en 3.5.2; `decae como $1/\sqrt{n}$ con varianza $(1 - \langle Z_i \rangle^2)/n$` en 6.7
- Problema: En 3.5.2 se utiliza $n$ para el número de muestras de entrenamiento ($N$ en §3.4 y §5); en 6.7 se utiliza $n$ para el número de disparos de medición (mientras que en §3.1.4 y §5.2 se definió como $n_{\text{shots}}$); y en §3.4.8 se utiliza $n = 5$ para el número de condiciones.
- Evidencia: En `3.4.1_kta.tex:9` el tamaño muestral es $N$; en `3.1.4_medicion.tex:34` el número de disparos es $n_{\text{shots}}$. El uso de $n$ aislado para tres conceptos distintos en capítulos cercanos resta rigor.
- Propuesta: Reemplazar $n$ por $N$ en la ecuación de covarianza de PCA (ec. 13 de 3.5.2), y por $n_{\text{shots}}$ en la descripción del ruido de disparos en 6.7:64.

### A3-12 · MEDIA · Identificadores internos visibles
- Ubicación: `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex:167`, `6.2_separabilidad.tex:30`, `6.7_lecciones_implementacion.tex:22, 70, 72, 77`, y `6.8_sintesis.tex:58`
- Texto: «en el experimento X1» (6.1:167); «caracterizado en el estudio B3» (6.2:30); «complejidad de circuitos en B1» (6.7:22); «sección de disparos de B1» (6.7:70); «en B3 y OE-6» (6.7:72); «en B1 proyectaba» (6.7:77); «o la reducción a 8 qubits (X3)» (6.8:58)
- Problema: Se emplean los identificadores internos de cuadernos de Jupyter (B1, B3, X1, X3) en la redacción de resultados sin acompañarlos de una remisión a la sección de experimentos complementarios (§5.11) o al estudio de benchmark correspondiente, dificultando la lectura para un evaluador que desconoce el esquema interno de archivos.
- Evidencia: La regla 4 de `A3_terminologia.md` restringe los identificadores internos visibles fuera de comentarios. En Metodología (§5.11) están formalmente tabulados, pero en §6 aparecen como nombres propios sin enlace ni contextualización.
- Propuesta: Añadir referencias cruzadas explícitas (e.g. «en el experimento X1 (sección~\ref{sec:experimentos_complementarios})» o «en el estudio de caracterización del simulador (sección~\ref{sec:restricciones_simulador})»).

### A3-13 · ALTA · Identificadores internos y referencias cruzadas
- Ubicación: `Docs/tablas/anexo_e_decisiones.tex:18-57`
- Texto: Columnas «Sección»: `\S\,4.4`, `\S\,4.5`, `\S\,4.6`, `\S\,4.7`, `\S\,4.8`, `\S\,4.9`, `\S\,4.10`, `\S\,8.x` en prácticamente las 40 filas de la tabla
- Problema: Las secciones citadas corresponden a la numeración antigua del reporte técnico de TT1 (cuando Metodología era el Capítulo 4 e Implementación el Capítulo 8). En el reporte final, el Capítulo 4 es el Análisis Exploratorio de Datos (EDA), Metodología es el Capítulo 5 (con secciones 5.1 a 5.11), y el entorno de software está en el Anexo D / Anexo A.4, por lo que todas las referencias de la tabla están desfasadas.
- Evidencia: `Docs/Technical_Report.tex` incluye `capitulos/4_EDA/` (secciones 4.1 a 4.5) y `capitulos/5_Metodologia/` (secciones 5.1 a 5.11). D-005 cita `\S 4.4` (que en el reporte es `4.4_imagenes_dicom.tex`, no preprocesamiento); D-006 cita `\S 4.5` (`4.5_hallazgos.tex`, no extracción M3); D-030 cita `\S 4.1–\S 4.9`; D-040 cita `\S 4.10`.
- Propuesta: Actualizar sistemáticamente los números de sección en la tabla: `\S\,4.4` $\to$ `\S\,5.4`, `\S\,4.5` $\to$ `\S\,5.5`, `\S\,4.6` $\to$ `\S\,5.6`, `\S\,4.7` $\to$ `\S\,5.7`, `\S\,4.8` $\to$ `\S\,5.9`, `\S\,4.9` $\to$ `\S\,5.8`, `\S\,4.10` $\to$ `\S\,5.10`, y `\S\,8.x` $\to$ `Anexo~\ref{sec:anx_entorno}` o `\S\,5.4/\S\,5.5`.

### A3-14 · BAJA · Comillas y rayas
- Ubicación: `Docs/tablas/anexo_e_decisiones.tex:47`
- Texto: `\S\,4.1–\S\,4.9, RF, CRISP-DM`
- Problema: Contiene el carácter Unicode U+2013 (`–`) en vez de los dos guiones estándar de LaTeX (`--`) para rangos numéricos.
- Evidencia: Regla 5 de `A3_terminologia.md` («los rangos numéricos sí pueden usar `--`»).
- Propuesta: Reemplazar `\S\,4.1–\S\,4.9` por `\S\,5.1--\S\,5.10`.

### A3-15 · BAJA · Comillas y rayas
- Ubicación: `Docs/tablas/m6_separabilidad_kernels.tex:13, 17` y `Docs/tablas/anexo_d_paquetes.tex:14, 16, 22, 23, 24, 25`
- Texto: `& 2.8 & — \\` en `m6_separabilidad_kernels.tex`; `\texttt{—}` en `anexo_d_paquetes.tex`
- Problema: Introduce el carácter Unicode U+2014 (`—`) como símbolo de celda vacía o no aplicable en lugar de `---` o `\textemdash`.
- Evidencia: Regla 5 de `A3_terminologia.md`.
- Propuesta: Cambiar por `---` o `\textemdash` en el código fuente de LaTeX.

### A3-16 · MEDIA · Lenguaje y consistencia teórica
- Ubicación: `Docs/capitulos/3_Marco_Teorico/3.1.2_compuertas.tex:47`
- Texto: «donde los ángulos $\theta$ son los parámetros entrenables del circuito.»
- Problema: Afirma de manera categórica que los ángulos $\theta$ son entrenables, lo cual contradice la decisión metodológica central D-014 (Arquitectura B), donde $\boldsymbol{\theta}$ se fija deterministamente y no se entrena en todo el diseño principal.
- Evidencia: D-014 en `Other/bitacora_decisiones.md` y `Docs/capitulos/3_Marco_Teorico/3.2.6_quantum_embedding.tex:21-23` («el vector de parámetros $\boldsymbol{\theta}$ no se entrena... se fija de forma determinista una sola vez con semilla declarada 42»).
- Propuesta: Matizar la frase: «donde los ángulos $\theta$ corresponden a los parámetros variacionales del circuito (que en este trabajo se fijan de antemano bajo la Arquitectura B)».

### A3-17 · MEDIA · Restos de TT1 o del diseño anterior
- Ubicación: `Docs/capitulos/3_Marco_Teorico/3.4.6_tsne.tex:8-20`
- Texto: Líneas 8-10: «El algoritmo \textit{t-Distributed Stochastic Neighbor Embedding} (t-SNE) \cite{vandermaaten2008tsne} proyecta vectores de alta dimensionalidad...»; Líneas 18-20: «se emplea el algoritmo \textit{t-Distributed Stochastic Neighbor Embedding} (t-SNE) \cite{vandermaaten2008tsne} como herramienta de exploración cualitativa.»
- Problema: Dos párrafos consecutivos definen y expanden las siglas de t-SNE y repiten la misma cita bibliográfica casi textualmente, evidenciando un solapamiento de redacción al fusionar textos de TT1 y TT2.
- Evidencia: La lectura secuencial de `3.4.6_tsne.tex` muestra que las líneas 18-20 repiten exactamente lo expuesto en las líneas 8-11.
- Propuesta: Eliminar el primer párrafo (l. 8-16) o refundir ambos párrafos suprimiendo la segunda definición redundante.

### A3-18 · BAJA · Términos en inglés y consistencia
- Ubicación: `Docs/capitulos/4_EDA/4.5_hallazgos.tex:77, 83` y `Docs/capitulos/5_Metodologia/5.2_requerimientos.tex:356`
- Texto: «extracción directa de features radiómicas» (4.5:77); «Cálculo de features de forma» (4.5:83); «extracción de features y selección/escalado» (5.2:356)
- Problema: Emplea el anglicismo «features» sin cursiva y como sustantivo común en español en lugar del término castellano normalizado «características».
- Evidencia: Regla 9 de `A3_terminologia.md` («consistencia, no alternar 'feature'/'característica' sin criterio»). En el resto del documento se utiliza «características radiómicas» o «características morfológicas».
- Propuesta: Reemplazar «features» por «características» en esos tres pasajes.

### A3-19 · BAJA · Términos en inglés y consistencia
- Ubicación: `Docs/capitulos/3_Marco_Teorico/3.1.2_compuertas.tex:47`, `3.1.3_multiples_qubits.tex:48`, `5.1_descripcion_general.tex:54, 62, 66, 71`
- Texto: `ansatz variacional` (sin `\textit`), `Baseline crudo`, `Baseline no lineal`, `ansatz con $\theta$ fijo`
- Problema: Se omiten las cursivas en términos en inglés (`ansatz`, `baseline`) en textos de figuras y párrafos teóricos, mientras que en otras secciones se escribe `\textit{ansatz}` o `\textit{baseline}`.
- Evidencia: Regla 9 de `A3_terminologia.md` («Términos en inglés: en `\textit{}` la primera vez; consistencia»).
- Propuesta: Estandarizar el uso de `\textit{ansatz}`, `\textit{baseline}`, `\textit{embedding}` y `\textit{pipeline}` en todas las apariciones en prosa y diagramas.

---

## 4. Conteo de hallazgos por severidad

| Severidad | Conteo | Descripción de impacto |
| :--- | :---: | :--- |
| **ALTA** | **2** | Conflicto notacional de dimensión $k$ vs $n$ (§3.2); referencias desfasadas a secciones del reporte en Anexo E (`tablas/anexo_e_decisiones.tex`). |
| **MEDIA** | **10** | «Distancia de Fisher» frente a «razón de Fisher»; clases deprecadas `ZZFeatureMap`/`PauliFeatureMap` en objetivos, síntesis y conclusiones; $k_Q$ frente a $K_Q$; inversión de índices en kernel proyectado; $g_{CQ}$ en fórmula regularizada; disparidad de símbolo $n$; identificadores B1/B3/X1 en §6 sin referencia cruzada; parámetros entrenables en §3.1.2 desfasado con Arq. B; duplicación de párrafo t-SNE. |
| **BAJA** | **7** | Encabezados de sección con nombres deprecados; inconsistencia en bibliografía; $\theta$ escalar en tablas; caracteres Unicode `–` y `—` en tablas; uso de «features» sin cursiva en §4.5 y §5.2; extranjerismos sin cursiva en diagramas y párrafos puntuales. |
| **TOTAL** | **19** | **Total de hallazgos documentados** |

---

## 5. Verificación de integridad del repositorio

Confirmación de estado mediante `git -C /Users/alexander_san/TT status --short`:
- No se modificó ningún archivo fuente (`.tex`, `.py`, `.ipynb`, `.csv`, `.md`).
- El único archivo creado en el repositorio para esta tarea es `Docs/insumos/auditoria/informe_A3.md`.
