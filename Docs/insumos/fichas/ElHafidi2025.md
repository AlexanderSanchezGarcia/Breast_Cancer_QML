# ElHafidi2025 · Investigating Quantum Feature Maps in Quantum Support Vector Machines for Lung Cancer Classification

- Autores y año: El Hafidi, M. Y., Toufah, A., & Kadim, M. A. (2025). (En el preprint de arXiv:2506.03272v1: Toufah, A., Kadim, M. A., & El Hafidi, My Y.)
- Versión leída: Docs/fuentes/pdf/ElHafidi2025.pdf · preprint de arXiv (arXiv:2506.03272v1, 3 de junio de 2025) · 14 páginas
- Tipo: experimental (simulación con Qiskit sobre `qasm_simulator`)

## Qué concluye
- Evalúa el impacto de tres mapas de características cuánticos (ZFeatureMap, ZZFeatureMap y PauliFeatureMap) en Quantum Support Vector Machines (QSVM) para la clasificación binaria de cáncer de pulmón sobre el simulador cuántico `qasm_simulator` — «QSVM models were implemented using Qiskit and executed on the qasm simulator, employing three distinct quantum feature maps: ZFeatureMap, ZZFeatureMap, and PauliFeatureMap.» (p. 1)
- Para lidiar con el desbalance de clases de un conjunto de datos real de 309 pacientes (39 sin cáncer vs. 270 con cáncer), construye seis subconjuntos balanceados de 78 muestras cada uno — «Using a real-world dataset of 309 patient records with significant class imbalance (39 non-cancer vs. 270 cancer cases), we constructed six balanced subsets for robust evaluation.» (p. 1)
- El mapa PauliFeatureMap supera a los demás mapas cuánticos, logrando clasificación perfecta en tres de los subconjuntos y un promedio superior en general — «Results show that the PauliFeatureMap consistently outperformed the others, achieving perfect classification in three subsets and strong performance overall.» (p. 1)
- El modelo QSVM con ZZFeatureMap alcanza una exactitud de 0.91 y F1-score de 0.91, mientras que con PauliFeatureMap alcanza un valor consistente de 0.96 en todas las métricas evaluadas — «for ZZFeatureMap, the results were an accuracy of 0.91, precision of 0.87, recall of 0.96, specificity of 0.85, and F1-score of 0.91; and for PauliFeatureMap, the model achieved a consistent performance of 0.96 across all metrics, including accuracy, precision, recall, specificity, and F1-score.» (p. 9)
- El modelo clásico SVM con kernel RBF (función de base radial) obtiene una exactitud de 0.95, precisión de 0.98, recall de 0.92, especificidad de 0.98 y F1-score de 0.95 (p. 9) — «The radial basis function (RBF) kernel provided the best results, with an accuracy of 0.95, precision of 0.98, recall of 0.92, specificity of 0.98, and F1-score of 0.95.» (p. 9)
- La elección del mapa cuántico adecuado depende de dos factores determinantes: la estructura de correlación de los datos y la tolerancia al ruido del hardware cuántico — «The choice of an appropriate feature map depends on two major factors: the nature of the data and the noise resilience of the quantum device.» (p. 6)
- El ZZFeatureMap resulta idóneo para características correlacionadas por pares, aunque con un mayor coste computacional — «ZZFeatureMap is ideal for pairwise correlated features, albeit with higher computational cost.» (p. 6)

## Qué deja como trabajo futuro o limitación declarada
- El mapa PauliFeatureMap, a pesar de ser teóricamente el más expresivo, presenta una alta sensibilidad al ruido cuántico — «PauliFeatureMap, while powerful, requires careful noise mitigation strategies due to its complexity.» (p. 6)
- Su susceptibilidad al ruido se debe a compuertas que alteran la base computacional, induciendo errores de volteo de bit (bit flips) — «PauliFeatureMap is the most expressive in theory but suffers from high noise sensitivity, particularly bit flips, due to basis-altering operations.» (p. 12)
- Plantea como trabajo futuro explorar mapas de características adaptativos o codificaciones híbridas clásico-cuánticas que combinen las fortalezas de cada enfoque minimizando sus desventajas frente al ruido — «Future work may explore adaptive feature maps or hybrid classical-quantum encodings that better leverage the benefits of each approach while minimizing their drawbacks.» (p. 12)

## Diseño experimental (solo obras experimentales)
- Datos: conjunto clínico tabular de cáncer de pulmón obtenido de Kaggle, consistente en 309 registros de pacientes con 15 variables (14 binarias y 1 continua: edad estandarizada con puntuación z).
- Tamaño y partición: 6 subconjuntos balanceados sin reemplazo de la clase mayoritaria (cada uno con los 39 casos negativos y 39 casos positivos seleccionados aleatoriamente, totalizando 78 muestras por subconjunto) — «To address the substantial class imbalance, six balanced subsets were constructed. Each subset contains all 39 negative samples and 39 unique positive samples selected randomly without replacement, as summarized in Table 1.» (p. 8)
- Métricas: exactitud (accuracy), precisión, sensibilidad (recall), especificidad y F1-score promediados a lo largo de los 6 subconjuntos.
- Simulador / hardware: simulación clásica mediante el simulador cuántico `qasm_simulator` de Qiskit (no se utilizó procesador cuántico físico).
- Comparación clásica: SVM clásico en scikit-learn con tres funciones de kernel: lineal (accuracy 0.91), polinomial (accuracy 0.94) y RBF (accuracy 0.95).

## Las cuatro preguntas de H-046 (solo obras que reportan una ventaja o un resultado cuántico frente a clásico)
1. *¿El modelo clásico recibió el mismo ajuste y las mismas features?*
   Sí. Cada modelo cuántico fue evaluado sobre los mismos seis subconjuntos balanceados con las mismas 15 variables normalizadas para asegurar una comparación justa — «Each quantum model was evaluated on the same six balanced subsets to ensure a fair comparison with its classical counterpart.» (p. 9).
2. *¿La diferencia supera su incertidumbre (hay intervalos, desviaciones, pruebas)?*
   No. La diferencia en exactitud promedio entre el mejor modelo cuántico (PauliFeatureMap, 0.96) y el mejor modelo clásico (SVM RBF, 0.95) es de apenas 0.01 (1%). El artículo no reporta desviaciones estándar, intervalos de confianza ni pruebas de significancia estadística entre ambos modelos (p. 9, Tabla 2). Dado que cada subconjunto de prueba comprende aproximadamente 16 casos, una diferencia de 1 punto porcentual corresponde a menos de un caso clasificado de forma diferente y cae dentro del error estocástico. Por su parte, ZZFeatureMap (0.91) empata con SVM lineal (0.91) y resulta inferior a SVM polinomial (0.94) y SVM RBF (0.95).
3. *¿El test se usó una sola vez?*
   No lo especifica claramente. Se reportan promedios sobre los 6 subconjuntos balanceados creados a partir del dataset original de 309 pacientes, pero no se describe un conjunto de prueba final independiente y no visto para validar los hiperparámetros seleccionados de los clasificadores.
4. *¿El kernel o el circuito cuántico es realmente difícil de simular clásicamente?*
   No. Todos los modelos cuánticos fueron simulados en computación clásica utilizando el simulador `qasm_simulator` de Qiskit («QSVM models were implemented using Qiskit and executed on the qasm simulator», p. 1). Con 15 variables de entrada, el circuito cuántico es completamente simulable de forma clásica sin complejidad intratable.

## Preguntas específicas
- **Las cifras de ZZ (0.91) y Pauli (0.96) y en qué métrica:**
  Ambas cifras corresponden a los promedios obtenidos a través de los 6 subconjuntos balanceados (p. 9):
  - *ZZFeatureMap:* exactitud (accuracy) de 0.91, precisión de 0.87, recall de 0.96, especificidad de 0.85 y F1-score de 0.91.
  - *PauliFeatureMap:* alcanzó exactamente 0.96 de forma consistente en todas las métricas: exactitud de 0.96, precisión de 0.96, recall de 0.96, especificidad de 0.96 y F1-score de 0.96 («for ZZFeatureMap, the results were an accuracy of 0.91, precision of 0.87, recall of 0.96, specificity of 0.85, and F1-score of 0.91; and for PauliFeatureMap, the model achieved a consistent performance of 0.96 across all metrics, including accuracy, precision, recall, specificity, and F1-score.» p. 9).
- **El SVM clásico con RBF:**
  El clasificador clásico SVM con kernel RBF alcanzó un rendimiento prácticamente idéntico al de PauliFeatureMap: accuracy de 0.95, precisión de 0.98, recall de 0.92, especificidad de 0.98 y F1-score de 0.95 («The radial basis function (RBF) kernel provided the best results, with an accuracy of 0.95, precision of 0.98, recall of 0.92, specificity of 0.98, and F1-score of 0.95.» p. 9).
- **Tamaño y partición:**
  Conjunto clínico de 309 pacientes (39 benignos / no cáncer y 270 malignos / con cáncer). Para compensar el desbalance severo, construyeron 6 subconjuntos balanceados de 78 pacientes cada uno (los 39 casos negativos emparejados con 39 casos positivos distintos sin reemplazo por subconjunto) (p. 8, Tabla 1).
- **Qué PauliFeatureMap usan (qué Paulis):**
  El circuito de PauliFeatureMap incorpora rotaciones de un solo qubit alrededor de los ejes $X$, $Y$ y $Z$, y términos de entrelazamiento con compuertas $Z_j \otimes X_k$ («The PauliFeatureMap was configured with Pauli rotations on the Z, X and Y axes, enabling the encoding of complex feature correlations.» p. 9; y en la p. 6, ec. 14: $U_{\text{Pauli}}(\vec{x}) = \prod_{j=1}^n e^{-i x_j X_j} e^{-i x_j Y_j} e^{-i x_j Z_j} \prod_{j < k} e^{-i x_j x_k Z_j \otimes X_k}$).

## Relevancia para el TT
- Se conecta con §2.1.3 (línea 783) del Technical Report:
  1) Es el antecedente en el que se basa el proyecto para justificar la comparación directa entre `ZZFeatureMap` y `PauliFeatureMap` en mamografía.
  2) Corrobora experimentalmente que la mayor expresividad del `PauliFeatureMap` frente a `ZZFeatureMap` se traduce en una mayor capacidad de ajuste en simulación ideal, pero advierte con rigor que su sensibilidad al ruido de inversión de bit (bit flips) en hardware NISQ real es considerablemente mayor.
- **Qué NO se puede afirmar con esta fuente:**
  No se puede afirmar que el trabajo haya demostrado una ventaja cuántica real sobre el aprendizaje clásico: el SVM clásico con kernel RBF obtuvo una exactitud de 0.95 (a solo 0.01 de Pauli y muy por encima del 0.91 de ZZ). Tampoco se puede afirmar que el trabajo analice imágenes de cáncer ni mamografías (analizaron un dataset tabular clínico de 15 variables de encuesta/historial médico). Asimismo, no se ejecutó en hardware cuántico físico (se empleó exclusivamente `qasm_simulator`).

## Contraste con lo que el proyecto ya le atribuye
- `Docs/Technical_Report.tex:783`: «Un estudio reciente aplicó los tres métodos a la clasificación de cáncer de pulmón con QSVM, obteniendo que ZZFeatureMap alcanzó una accuracy de 0.91 y F1-score de 0.91, mientras que PauliFeatureMap logró un rendimiento consistente de 0.96 en todas las métricas incluyendo accuracy, precisión, recall y F1-score; la elección del mapa apropiado depende de dos factores principales, la naturaleza de los datos y la resiliencia al ruido del dispositivo cuántico. Estos resultados motivan la estrategia del presente trabajo de comparar ambos métodos de codifiación sobre características morfológicas mamográficas.»
  - *¿Lo sostiene la obra?* Sí en las cifras y conclusiones citadas: las cifras 0.91 para ZZ y 0.96 para Pauli son exactas y provienen de la p. 9; la afirmación sobre los dos factores proviene literalmente de la p. 6.
  - *Matiz crítico omitido en el reporte:* El reporte omite que el SVM clásico con kernel RBF alcanzó 0.95 de accuracy (casi idéntico a Pauli y superior a ZZ), que los datos no son imágenes sino datos tabulares de 15 variables clínicas, y que el estudio se realizó en simulación clásica (`qasm_simulator`), no en procesadores cuánticos físicos.
- `Other/correcciones_verificadas.md:56`: «Línea 783, cáncer de pulmón con QSVM, sin cita. El trabajo es arXiv:2506.03272: El Hafidi, Toufah y Kadim (2025), Investigating Quantum Feature Maps in Quantum Support Vector Machines for Lung Cancer Classification.»
  - *¿Lo sostiene la obra?* Sí. Confirma la autoría y la referencia pendiente en el reporte.
