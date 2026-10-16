# Azevedo2022QuantumTransfer · Quantum transfer learning for breast cancer detection

- Autores y año: Azevedo, V., Silva, C., & Dutra, I. (2022).
- Versión leída: Docs/fuentes/pdf/Azevedo2022QuantumTransfer.pdf · versión publicada (Quantum Machine Intelligence, 4(1), 5, 2022; recibida en julio 2021, publicada en línea el 28 de febrero de 2022) · 14 páginas
- Tipo: experimental (simulación y ejecución en QPU física IBM Quantum)

## Qué concluye
- Implementa un esquema de aprendizaje por transferencia clásico-a-cuántico (Quantum Transfer Learning, QTL) inspirado en Mari et al. (2020) para clasificar mamografías completas en benignas o malignas — «Based on the work of Mari et al., we train a set of hybrid classical-quantum neural networks using transfer learning (TL).» (p. 1)
- La tarea experimental consiste en clasificar imágenes mamográficas completas provistas por el repositorio BCDR — «Our task was to solve the problem of classifying full-image mammograms into malignant and benign, provided by BCDR.» (p. 1)
- La red neuronal clásica residual sin transferencia de aprendizaje alcanza un máximo de 67% de exactitud, mientras que los experimentos con transferencia alcanzan 84% — «The classical residual neural network, without resourcing to TL, achieved a maximum of 67% accuracy while our other experiments» (p. 11) «using TL achieved 84%.» (p. 12)
- El resultado de 84% de exactitud es alcanzado tanto por la red clásica con transferencia (C+TL) como por los modelos híbridos clásico-cuánticos CQ1 y CQ4 (Tabla 4, p. 12). La ventaja cuántica observada en simulación no radica en la exactitud, sino en el AUC, que sube de 0.58 a 0.77 — «The results for every metric are far more consistent between training and testing and between epochs when using the dressed quantum circuit, so much so that AUC value went from 58 to 77%, leading us to believe that a hybrid-quantum network does present some advantage as AUC measures how well the model separates two classes.» (p. 12)
- Al comparar con la literatura previa que utilizó transferencia clásica, reportan superar los resultados del estado del arte en exactitud y AUC — «accuracy of 84% against 76.9%, AUC of 77% against 74.9% and specificity of 100% surpassed 64.91%.» (p. 12)
- En el procesador cuántico físico real (`ibm_lagos`, 7 qubits Falcon), la exactitud desciende a 81% (Tabla 5, p. 12), obteniendo resultados estables a lo largo de 20 repeticiones.

## Qué deja como trabajo futuro o limitación declarada
- Afirman con cautela que es prematuro determinar si el QML confiere una ventaja real y que sus resultados solo sugieren buena capacidad de generalización sujeta a comprobaciones adicionales — «It is too soon to say whether or not QML can be an advantage. Our results only point to a good generalization of complex data which needs further testing.» (p. 11)
- Declaran literalmente como trabajo futuro separar el conjunto de datos por tipo de lesión (masas y calcificaciones) antes de clasificar — «As future work, an interesting approach could be to separate the dataset into masses and calcifications and only then perform classification. That way, we would be evaluating different specific features in a similar scenario and would probably get clearer results.» (p. 12)
- Declaran textualmente como trabajo futuro evaluar cómo se distribuyen los datos en el espacio de Hilbert para verificar si las clases se agrupan en conglomerados compactos y separados — «Lastly, the best way to know how well this model performs would be to see how the data appears in our Hilbert space. Ideally, both classes would appear very separately in it, as tight clusters.» (p. 12)
- Señalan como limitación que emplearon únicamente angle embedding porque permite entrenar las compuertas y calcular gradientes factibles, dejando abiertos otros esquemas de embedding — «In addition, in this research we conduct the experiments using the angle embedding technique since with this method the features can be learned.» (p. 12)

## Diseño experimental (solo obras experimentales)
- Datos: mamografías completas (vistas CC y MLO) provenientes de las colecciones BCDR-D01 y BCDR-D02 del repositorio BCDR (Breast Cancer Data Repository; la bibliografía del artículo lo titula «Breast cancer digital repository»).
- Tamaño y preprocesamiento: imágenes redimensionadas y normalizadas con estadísticas de ImageNet, data augmentation mediante volteos aleatorios horizontales y verticales.
- Partición: misma partición entrenamiento/prueba y semilla fija para la comparación entre modelos («These results were on the same dataset, same train-test split and with a fixed seed.» p. 12).
- Métricas evaluadas: Loss, Precision, Recall, F1-score, Accuracy, Specificity y AUC (Tabla 4, p. 12).
- Simulador y hardware: PennyLane sobre CPU clásica (Intel Core i7-10510U, 16 GB RAM) para simulación; para validación física se utilizó el computador cuántico superconductor IBM Quantum `ibm_lagos` (7 qubits, quantum volume 32, procesador Falcon r5.11H).
- Comparación clásica: modelo C (ResNet18 entrenada desde cero, accuracy 67%, AUC 0.70) y modelo C+TL (ResNet18 preentrenada con clasificador lineal, accuracy 84%, AUC 0.58).

## Las cuatro preguntas de H-046 (solo obras que reportan una ventaja o un resultado cuántico frente a clásico)
1. *¿El modelo clásico recibió el mismo ajuste y las mismas features?*
   Sí. Se garantizó paridad experimental al evaluar sobre el mismo conjunto y la misma partición con semilla idéntica («These results were on the same dataset, same train-test split and with a fixed seed.» p. 12). Ambos modelos (C+TL y CQ1–CQ4) compartieron el mismo extractor ResNet18 preentrenado en ImageNet que genera 512 características; C+TL acopló una capa lineal clásica final, mientras que CQ1–CQ4 utilizaron una capa lineal de reducción a 4 dimensiones seguida del circuito cuántico variacional DressedQuantumNet.
2. *¿La diferencia supera su incertidumbre (hay intervalos, desviaciones, pruebas)?*
   No. En exactitud (accuracy) no existe diferencia: tanto el modelo clásico C+TL como los híbridos CQ1 y CQ4 obtienen idéntico 84% (0.84) en el conjunto de prueba (Tabla 4, p. 12). La ventaja en AUC reportada en simulación (0.77 frente a 0.58) carece de intervalos de confianza, desviaciones estándar o pruebas de hipótesis estadísticas en la Tabla 4. En hardware físico (`ibm_lagos`), el accuracy decrece al 81% (Tabla 5). Los autores enfatizan: «It is too soon to say whether or not QML can be an advantage. Our results only point to a good generalization of complex data which needs further testing.» (p. 11).
3. *¿El test se usó una sola vez?*
   No / Parcialmente. Los autores seleccionaron la mejor configuración (CQ1, profundidad 1) evaluando el rendimiento en test dentro del simulador («CQ1 has the higher overall results between training and test, namely precision, specificity and AUC score.» p. 10), y reutilizaron ese estado óptimo para evaluarlo en el procesador cuántico `ibm_lagos` a lo largo de 20 repeticiones con aumentación de datos reportando la mejor clasificación obtenida («Due to the waiting times, IBM Quantum experiments were done using the best model state that resulted from training in the simulator. This means that only the test part was done in the quantum machine.» p. 10).
4. *¿El kernel o el circuito cuántico es realmente difícil de simular clásicamente?*
   No. El circuito cuántico posee únicamente 4 qubits y una profundidad variacional de 1 a 4 capas («CQ1, CQ2, CQ3 and CQ4: the hybrid classical-\nquantum ResNet models using transfer learning, whose variational quantum circuits have a depth of 1, 2, 3, and 4, respectively (using the simulator).» p. 10). Dicho circuito es analíticamente tratable y se simula en fracciones de segundo en un procesador clásico para portátiles.

## Preguntas específicas
- **El trabajo futuro que declaran, literal:**
  - *Separación por tipo de hallazgo (masas y calcificaciones):*
    «As future work, an interesting approach could be to separate the dataset into masses and calcifications and only then perform classification. That way, we would be evaluating different specific features in a similar scenario and would probably get clearer results.» (p. 12).
  - *Evaluación de la distribución de los datos en el espacio de Hilbert:*
    «Lastly, the best way to know how well this model performs would be to see how the data appears in our Hilbert space. Ideally, both classes would appear very separately in it, as tight clusters.» (p. 12).
  Ambas afirmaciones coinciden palabra por palabra con los compromisos metodológicos asumidos en el Technical Report del proyecto.
- **Qué significa BCDR en el artículo:**
  En el artículo significa **Breast Cancer Data Repository** — «Breast Cancer Data Repository (BCDR) dataset (Lopez et al. 2012).» (p. 4) y «Breast cancer digital repository» (p. 13, p. 14). El reporte técnico de la tesis incurre en una denominación errónea al llamarlo «Barcelona Digital Breast Cancer Dataset» en la línea 828.
- **El 84 %:**
  Corresponde a la exactitud alcanzada sobre el conjunto de prueba en la Tabla 4 (p. 12). Este 84% es obtenido por el modelo clásico con transfer learning (`C+TL`), así como por los modelos híbridos `CQ1` y `CQ4`. Por tanto, el 84% es mérito de la transferencia de aprendizaje de la CNN (ResNet18 preentrenada), no de un salto cuántico en exactitud.
- **Las variantes CQ1–CQ4 frente a C+TL:**
  - `C`: ResNet18 entrenada desde cero (accuracy 67%, AUC 0.70).
  - `C+TL`: ResNet18 preentrenada con clasificador lineal clásico (accuracy 84%, AUC 0.58).
  - `CQ1` a `CQ4`: modelos híbridos con transfer learning cuyos circuitos variacionales tienen profundidades de 1, 2, 3 y 4 respectivamente (accuracy de 84%, 83%, 83%, 84%; y AUC de 0.77, 0.77, 0.74, 0.69). La variante CQ1 muestra el mejor AUC (0.77), pero empata en exactitud con C+TL (0.84).
- **Embedding usado:**
  Utilizan *angle embedding* (codificación angular con compuertas de rotación sobre 4 qubits) — «In addition, in this research we conduct the experiments using the angle embedding technique since with this method the features can be learned.» (p. 12).

## Relevancia para el TT
- Se conecta de forma directa con la formulación del problema (§1.3), los antecedentes específicos en mamografía (§2.1.5, línea 825), la tabla comparativa de antecedentes (línea 939) y la decisión D-019 en la bitácora:
  1) Es el antecedente metodológico más cercano: aplica circuitos variacionales reales mediante transfer learning sobre imágenes mamográficas.
  2) Justifica explícitamente las dos líneas de investigación del TT: la separación por tipo de hallazgo mamográfico (masas vs. calcificaciones) y el análisis de la separabilidad geométrica en el espacio de Hilbert mediante distancias y alineamiento de kernel.
- **Qué NO se puede afirmar con esta fuente:**
  No se puede afirmar que Azevedo et al. hayan demostrado ventaja cuántica en exactitud diagnóstica (hubo empate en 84% con el modelo clásico C+TL). Tampoco se puede afirmar que hayan evaluado el dataset CBIS-DDSM (usaron BCDR), ni que hayan probado circuitos cuánticos puros o kernels variacionales directos sin el extractor convolucional clásico.

## Contraste con lo que el proyecto ya le atribuye
- `Docs/Technical_Report.tex:613`: «Tercero, retoma y ejecuta las dos líneas de trabajo futuro identificadas por Azevedo et al. (2022) como pendientes: la separación del análisis por tipo de hallazgo mamográfico y la evaluación de la distribución de datos en el espacio cuántico resultante.»
  - *¿Lo sostiene la obra?* Sí. En la p. 12, los autores identifican textualmente ambas propuestas como trabajo futuro.
- `Docs/Technical_Report.tex:825`: «Azevedo et al. (2022), que implementa quantum transfer learning mediante redes neuronales híbridas clásico-cuánticas con angle embedding sobre el dataset BCDR (Barcelona Digital Breast Cancer Dataset), obteniendo 84\% de accuracy y señalando como trabajo futuro explícito la necesidad de evaluar la distribución de los datos en el espacio de Hilbert resultante para verificar la separabilidad de clases.»
  - *¿Lo sostiene la obra?* Parcial:
    1. El nombre del dataset es erróneo en el reporte: es «Breast Cancer Data Repository» en el texto y «Breast cancer digital repository» en la bibliografía (BCDR), no «Barcelona Digital Breast Cancer Dataset».
    2. El 84% de exactitud lo obtiene tanto el modelo clásico C+TL como el cuántico CQ1; la ganancia reportada por Azevedo está en el AUC (0.77 vs. 0.58), no en la exactitud.
    3. En el computador cuántico real (`ibm_lagos`), la exactitud es de 81%, no 84%.
- `Other/bitacora_decisiones.md:44,366` (D-019): «Las líneas de trabajo futuro se atribuyen a Azevedo et al. (2022)».
  - *¿Lo sostiene la obra?* Sí. Se confirma plenamente que ambas líneas provienen de Azevedo et al. (2022), p. 12, y no de Incudini et al. (2022).
- `Other/correcciones_verificadas.md:54`: «El 84 % de exactitud lo alcanzan tanto la ResNet clásica con transfer learning (C+TL) como las híbridas CQ1 y CQ4 (Tabla 4, p. 11). La diferencia que destacan está en el AUC: 0.77 frente a 0.58. En ibm_lagos la exactitud baja a 81 % (Tabla 5). Y concluyen: It is too soon to say whether or not QML can be an advantage. El nombre correcto del dataset es Breast Cancer Digital Repository».
  - *¿Lo sostiene la obra?* Sí, exactamente como lo registró dicha auditoría interna.
