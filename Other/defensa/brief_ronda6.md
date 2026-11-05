# Ronda 6 · «Defensa TT 2026-B039»: más separabilidad, curvas ROC, tabla resumen y las figuras del reporte como anexos

Esta ronda tiene cinco cambios:
1. Una diapositiva nueva con la separabilidad de las representaciones vectoriales y el t-SNE (Figs. 6.2.4 y 6.2.5 del reporte).
2. La diapositiva del MLP pasa a mostrar las curvas ROC en prueba (Fig. 6.3.2).
3. Una diapositiva nueva con la tabla resumen de resultados (Tabla 23 del reporte, simplificada).
4. Un bloque de anexos con las figuras del reporte técnico, una por diapositiva, con su número original.
5. Tiempos nuevos para que todo quepa en 20 minutos.

Las reglas de los briefs anteriores siguen vigentes. **No inventes ni redondees cifras:** todas salen de este documento o de `datos_ronda6.json`, que va adjunto. Las figuras del bloque de anexos van adjuntas como PNG.

**Importante sobre los videos:** no cambies el texto alternativo de las imágenes de los seis videos; debe seguir empezando con «Video…». Las imágenes nuevas de esta ronda **no** deben empezar con «Video».

---

## Nuevo orden y tiempos

| # | Diapositiva | Cambio | Tiempo (acumulado) |
|---|---|---|---|
| 1 | Portada | — | 0:15 (0:15) |
| 2 | Contexto | — | 0:40 (0:55) |
| 3 | Estado del arte | — | 0:50 (1:45) |
| 4 | Pregunta | — | 0:50 (2:35) |
| 5 | Proceso | — | 1:10 (3:45) |
| 6 | Qubit | — | 1:00 (4:45) |
| 7 | Dos lecturas | — | 0:50 (5:35) |
| 8 | Cinco representaciones | — | 0:45 (6:20) |
| 9 | Concentración | — | 1:30 (7:50) |
| 10 | Separabilidad (kernels) | título nuevo | 1:00 (8:50) |
| 11 | **NUEVA · Separabilidad (representaciones) y t-SNE** | nueva | 1:15 (10:05) |
| 12 | El mismo MLP (antes 11) | **curvas ROC** | 1:05 (11:10) |
| 13 | Árboles (antes 12) | — | 0:50 (12:00) |
| 14 | La lectura (antes 13) | — | 1:00 (13:00) |
| 15 | **NUEVA · Resumen de resultados** | nueva | 0:50 (13:50) |
| 16 | La ventaja sí existe (antes 14) | — | 0:55 (14:45) |
| 17 | X11 (antes 15) | — | 1:10 (15:55) |
| 18 | Viabilidad (antes 16) | — | 1:05 (17:00) |
| 19 | Objetivos cumplidos (antes 17) | — | 0:55 (17:55) |
| 20 | Trabajo futuro (antes 18) | — | 0:40 (18:35; quedan ~1:25) |

- La parte principal pasa a **20 diapositivas**: actualiza los contadores «n / 20».
- Actualiza el «Tiempo objetivo» y el «acumulado» de todas las notas según la tabla. Los recortes de tiempo son de lo que se dice, no del contenido de las diapositivas.

---

## 10 · Título nuevo: «Los kernels cuánticos no separan mejor las clases»
- Solo cambia el título, para distinguirla de la 11. El contenido (alineamiento y *g*) se queda igual.
- **Notas:** *Tiempo objetivo: 1:00 (acumulado 8:50).* Sin otros cambios.

## 11 · NUEVA · «Las representaciones que recibe el clasificador tampoco separan mejor»
- Etiqueta de sección: «03 · Resultados». Pie: «Fig. 6.2.4 y 6.2.5 del reporte · 200 lesiones de entrenamiento por subconjunto».
- **Paso 1, tres métricas.** Una cuadrícula de 2 filas (Masas, Calcificaciones) × 3 columnas (Davies-Bouldin, Fisher, alineamiento lineal). En cada panel, una barra por condición C1–C5 con la paleta del deck y, detrás de cada barra, una franja gris con la banda del 95 % de las etiquetas permutadas. Rótulos de columna:
  - «Davies-Bouldin · menor = más separado»;
  - «Razón de Fisher J · mayor = más separado»;
  - «Alineamiento lineal · mayor = más alineado».
  - Datos en `datos_ronda6.json` → `metricas_representacion_fig_6_2_4` (`davies_bouldin`, `fisher_j`, `kta_lineal` y sus `*_banda95_permutacion`). Escribe el valor encima de cada barra con tres decimales.

| | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|
| Masas · Davies-Bouldin | 4.301 | 4.301 | 5.564 | 5.898 | 13.346 |
| Masas · Fisher J | 0.669 | 0.669 | 0.781 | 0.449 | 0.668 |
| Masas · alineamiento lineal | 0.070 | 0.070 | 0.059 | 0.041 | 0.012 |
| Calcif. · Davies-Bouldin | 2.387 | 2.387 | 2.995 | 6.890 | 6.247 |
| Calcif. · Fisher J | 1.284 | 1.284 | 1.390 | 0.399 | 0.753 |
| Calcif. · alineamiento lineal | 0.181 | 0.181 | 0.161 | 0.031 | 0.041 |

  - Marca con un rótulo pequeño «como el azar» la barra de C5 en masas en Davies-Bouldin y en alineamiento lineal (cae dentro de la banda de permutación, p = 0.41), y la de C4 en calcificaciones en Fisher (p = 0.15).
- **Paso 2, t-SNE.** Las barras se atenúan y entra una cuadrícula de 2 × 5 diagramas de dispersión: filas Masas y Calcificaciones, columnas C1–C5. Benignas como triángulos verdes, malignas como círculos morados (los colores de clase de las figuras del reporte), sin ejes ni números.
  - Datos en `datos_ronda6.json` → `tsne_fig_6_2_5`: coordenadas ya normalizadas a [0, 1] en el orden de `clase` (0 = benigna, 1 = maligna). Masas: 103 benignas y 97 malignas; calcificaciones: 130 y 70.
  - Rótulo bajo la cuadrícula: «t-SNE: solo ayuda visual; no es una métrica».
- **Notas:** *Tiempo objetivo: 1:15 (acumulado 10:05).*
  - La diapositiva anterior medía los kernels; esta mide los vectores que de verdad recibe el clasificador. La conclusión es la misma.
  - Davies-Bouldin, menor es mejor: en masas C1 da 4.30, C4 5.90 y C5 13.35. C5 no se distingue de etiquetas al azar.
  - Fisher, mayor es mejor: C3 es el más alto en los dos subconjuntos; C4 el más bajo, 0.45 y 0.40.
  - Alineamiento lineal: C1 0.070 y 0.181; C4 0.041 y 0.031; C5 0.012 y 0.041.
  - C1 y C2 dan exactamente lo mismo: el PCA solo gira los datos, y por eso es el control nulo.
  - En el t-SNE, en C1 las malignas tienden a agruparse hacia un extremo; en C5 quedan mezcladas. C2 se ve como C1 girada o reflejada. Es solo una ayuda visual: las métricas son las de arriba.

## 12 · «El mismo MLP clasifica peor sobre los embeddings cuánticos» → con curvas ROC
- El título y el subtítulo «−0.07 a −0.14 de AUC frente a C1» no cambian. Pie: «Fig. 6.3.2 del reporte · conjunto de prueba oficial, usado una vez».
- **Visual:** sustituye la gráfica de puntos por dos paneles de curvas ROC lado a lado, Masas (378 lesiones, 147 malignas) y Calcificaciones (326, 129). Eje x «1 − especificidad», eje y «sensibilidad», diagonal punteada «azar».
  - Datos en `datos_ronda6.json` → `roc_prueba_fig_6_3_2` (`fpr`, `tpr`; dibuja la curva en escalera uniendo los puntos en orden).
  - Leyenda en cada panel, con el AUC y su intervalo:

| | Masas | Calcificaciones |
|---|---|---|
| C1 | 0.651 [0.578, 0.724] | 0.769 [0.694, 0.836] |
| C2 | 0.641 [0.572, 0.710] | 0.788 [0.719, 0.851] |
| C3 | 0.646 [0.572, 0.721] | 0.758 [0.685, 0.826] |
| C4 | 0.530 [0.473, 0.587] | 0.633 [0.558, 0.700] |
| C5 | 0.581 [0.521, 0.644] | 0.652 [0.571, 0.725] |

- **Pasos:** primero entran C1–C3 juntas; con el siguiente clic entran C4 y C5, con trazo más grueso, y un rótulo «más cerca de la diagonal del azar».
- La gráfica de puntos con intervalos que había aquí pasa a anexo (ver abajo).
- **Notas:** *Tiempo objetivo: 1:05 (acumulado 11:10).* Cada curva recorre todos los umbrales: arriba a la izquierda es mejor, la diagonal es el azar. Las tres clásicas casi se superponen. C4 y C5 quedan por debajo en los dos subconjuntos; en masas, C4 va casi sobre la diagonal entre 0.2 y 0.6 de 1 − especificidad. Las cuatro diferencias contra C1 son significativas, y C2 contra C1 no lo es.

## 15 · NUEVA · «Resumen: lo clásico va delante en separabilidad y en clasificación; el QSVM solo empata»
- Etiqueta de sección: «03 · Resultados». Pie: «Tabla 23 del reporte (versión completa en anexos) · cada celda: masas / calcificaciones».
- **Visual:** una tabla limpia, sin rejilla vertical. Las filas cuánticas (C4, C5, QSVM) con fondo naranja muy claro. En negritas, el mejor valor de cada columna en cada subconjunto (ya marcado abajo con **).

| | Exceso de KTA ↑ | *g* | Davies-Bouldin ↓ | Fisher J ↑ | AUC en prueba |
|---|---|---|---|---|---|
| C1 · sin transformar | — | — | **4.301** / **2.387** | 0.669 / 1.284 | **0.651** / 0.769 |
| C2 · PCA (control nulo) | — | — | **4.301** / **2.387** | 0.669 / 1.284 | 0.641 / **0.788** |
| C3 · Kernel PCA RBF | **0.049** / **0.151** | — | 5.564 / 2.995 | **0.781** / **1.390** | 0.646 / 0.758 |
| C4 · ZZ | 0.003 / 0.006 | 1.433 / 1.400 | 5.898 / 6.890 | 0.449 / 0.399 | 0.530 / 0.633 |
| C5 · Y + ZZ | 0.005 / 0.007 | 1.511 / 1.701 | 13.346 / 6.247 | 0.668 / 0.753 | 0.581 / 0.652 |
| SVM sobre el kernel RBF | | | | | 0.649 / 0.769 |
| QSVM sobre el kernel de C4 | | | | | 0.628 / 0.759 |

- Debajo, en gris: «Exceso de KTA de C3 = kernel RBF. *g* muy por debajo de √N ≈ 14.1. AUC de C1–C5 con el mismo MLP; SVM y QSVM del experimento X4.»
- **Pasos:** primero la tabla sin las dos últimas filas; luego entran SVM y QSVM con un recuadro: «el QSVM empata con el SVM clásico: la información está en el estado, se pierde al leer 12 números».
- **Notas:** *Tiempo objetivo: 0:50 (acumulado 13:50).* Esta tabla junta todo lo anterior. En separabilidad, la mejor columna siempre la gana una condición clásica. Al clasificar con el mismo MLP, C4 y C5 quedan de 0.07 a 0.14 por debajo. Y el QSVM, que usa el kernel completo, empata con el SVM clásico: el cuello de botella es la lectura. La única fila que podría parecer cuántica, Fisher de C5 en masas (0.668), está empatada con C1 (0.669).

---

## Anexos: cambios

### Anexos nuevos de resultados
Inserta estos tres justo después de «Todas las métricas de clasificación, en prueba», y renumera los siguientes:
1. **«AUC en prueba con intervalos de confianza»**: la gráfica de puntos que salía de la diapositiva del MLP, sin cambios.
2. **«Resumen completo de resultados (Tabla 23 del reporte)»**: la tabla de la diapositiva 15 con dos columnas más, dimensión efectiva y AUC en validación cruzada, y la fila del QSVM de C5. Datos en `datos_ronda6.json` → `tabla_resumen_tabla_23`.

| | d_eff (de 200) | AUC en VC |
|---|---|---|
| C1 | — | 0.652 / 0.742 |
| C2 | — | 0.641 / 0.758 |
| C3 (RBF) | 2.8 / 2.6 | 0.648 / 0.739 |
| C4 | 184.0 / 187.7 | 0.565 / 0.640 |
| C5 | 171.3 / 167.6 | 0.563 / 0.667 |
| QSVM sobre el kernel de C5 (AUC en prueba) | | 0.599 / 0.701 |

3. **«Métricas de separabilidad con su significancia»**: la tabla de la diapositiva 11 con el valor p de cada métrica frente a las 1,000 permutaciones (`p_db`, `p_fisher`, `p_kta_lineal` en el JSON).

### Bloque nuevo: «Figuras del reporte técnico»
Al final de los anexos, después del último actual, una diapositiva por figura, **en el orden del reporte** y con el número original de la figura. Sirve para que, si un sinodal pregunta por «la figura 6.2.3», el autor salte a ella.

- **Formato de cada diapositiva:** etiqueta de sección «Anexo N». Título: «Figura X.Y.Z · título corto» (de la tabla de abajo). La imagen adjunta ocupa todo el espacio disponible, centrada, sin recortar ni deformar (`contain`), sobre fondo blanco. Pie: «Reporte técnico, p. P · Anexo N / total».
- **Texto alternativo de la imagen:** «Figura del reporte X.Y.Z». No debe empezar con «Video».
- **Sin animaciones ni pasos.** Notas del orador: solo «Figura X.Y.Z del reporte, p. P».
- Las figuras están en inglés porque así salen de los notebooks; no traduzcas ni redibujes su contenido.

| Archivo adjunto | Título corto | p. |
|---|---|---|
| Fig_3.4.1_Huang2021_Fig2.png | Geometría de los kernels clásico y cuántico (Huang et al., 2021) | 66 |
| Fig_4.3.1_C3_mass_morphology.png | Forma y margen de las masas por patología | 81 |
| Fig_4.3.2_C4_calc_morphology.png | Tipo y distribución de las calcificaciones por patología | 81 |
| Fig_5.6.1_X10_balance_folds.png | Costo del número de *folds* | 101 |
| Fig_5.7.1_M5_circuit_k4.png | Circuitos de C4 y C5 dibujados para k = 4 | 103 |
| Fig_6.1.1_M3_effect_sizes.png | Tamaños de efecto de las 67 características | 115 |
| Fig_6.1.2_M3_clahe_effect.png | Efecto de CLAHE en la capacidad discriminativa | 115 |
| Fig_6.1.3_M4_selection_and_angles.png | Selección y escalado angular por cuantiles | 117 |
| Fig_6.1.4_X1_selection_auc_vs_k.png | AUC en función del número de características k | 118 |
| Fig_6.2.1_M5_kernel_concentration.png | Concentración de los kernels cuánticos | 120 |
| Fig_6.2.2_M6_kernel_metrics.png | Alineamiento y dimensión efectiva de los kernels | 122 |
| Fig_6.2.3_M6_geometric_difference.png | Diferencia geométrica *g* frente a √N | 123 |
| Fig_6.2.4_M6_embedding_metrics.png | Davies-Bouldin, Fisher y alineamiento lineal | 124 |
| Fig_6.2.5_M6_tsne.png | t-SNE de las cinco representaciones | 125 |
| Fig_6.2.6_X9_sample_size.png | Métricas en 20 submuestras y en todo el entrenamiento | 126 |
| Fig_6.2.7_X2_pair_auc_sweep.png | AUC de pares contra la escala angular c | 126 |
| Fig_6.2.8_X3_kernel_metrics_k8_k12.png | Separabilidad con 12 y con 8 qubits | 128 |
| Fig_6.3.1_M7_auc.png | AUC en validación cruzada y en prueba | 130 |
| Fig_6.3.2_M7_roc_test.png | Curvas ROC en el conjunto de prueba | 131 |
| Fig_6.3.3_M7_sensitivity.png | Sensibilidad del MLP: semilla, red, escalado, reps y k | 132 |
| Fig_6.3.4_X7_theta_draws.png | Diez sorteos de θ | 133 |
| Fig_6.3.5_X8_trained_theta.png | θ entrenado frente a θ fijo | 135 |
| Fig_6.3.6_X10_auc.png | Árboles, *random forest* y XGBoost sobre C1–C5 | 137 |
| Fig_6.3.7_X10_stopping_curves.png | Criterios de parada de un árbol | 138 |
| Fig_6.4.1_X4_qsvm_vs_readout.png | QSVM, SVM RBF y MLP sobre ⟨Zᵢ⟩ | 139 |
| Fig_6.4.2_X4_67_features.png | Las 67 características con codificaciones alternativas | 140 |
| Fig_6.4.3_X6_nested_auc.png | Búsqueda anidada de ventaja cuántica | 141 |
| Fig_6.4.4_X6_built_labels.png | Etiquetado diseñado según Huang et al. | 143 |
| Fig_6.4.5_X11_transition.png | Transición hacia las etiquetas diseñadas (X11) | 145 |
| Fig_6.5.1_M8_spearman.png | Correlación de Spearman entre separabilidad y clasificación | 147 |
| Fig_6.5.2_M8_classical_vs_quantum.png | Separabilidad frente a AUC, clásico y cuántico | 147 |
| Fig_6.6.1_M8_oe6_qubits.png | Escalabilidad del simulador con el número de qubits | 149 |
| Fig_6.6.2_M8_oe6_shots.png | Efecto del número de disparos | 150 |
| Fig_C.1.1_M2_mask_alignment.png | Alineación de las 80 máscaras desajustadas | 199 |
| Fig_C.1.2_M2_preprocessing_examples.png | Etapas del preprocesamiento | 200 |
| Fig_C.4.1_X2_kernel_pairs_by_class.png | Valores del kernel dentro y entre clases | 205 |

### Índice
- El índice «Anexos» conserva la lista numerada de los anexos de texto, con los tres nuevos.
- El bloque de figuras ocupa **una sola línea** en ese índice: «N–M · Figuras del reporte técnico (3.4.1 a C.4.1)».
- Añade, justo antes del bloque, una diapositiva **«Índice de figuras del reporte»**: una tabla en tres columnas con «Figura X.Y.Z → Anexo N», para saltar rápido.

### Referencias cruzadas
- Revisa las notas del orador que mandan a un anexo: con los tres anexos nuevos, la numeración cambia a partir de ahí.

## Comprobación final antes de exportar
- [ ] 20 diapositivas principales con contadores «n / 20» y los tiempos de la tabla.
- [ ] Las curvas ROC se dibujan con los puntos del JSON, no a mano; la leyenda dice exactamente los AUC e intervalos de la tabla.
- [ ] El t-SNE usa las coordenadas del JSON, en su orden.
- [ ] La tabla resumen cabe completa y legible, con el mejor valor de cada columna en negritas.
- [ ] Los anexos de figuras siguen el orden del reporte y cada imagen tiene el texto alternativo «Figura del reporte X.Y.Z».
- [ ] Las imágenes de los seis videos conservan su texto alternativo, que empieza con «Video…».
- [ ] Las notas del orador apuntan a los números de anexo correctos.
