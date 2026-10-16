# Xiang2024QuantumCNN · Quantum classical hybrid convolutional neural networks for breast cancer diagnosis

- Autores y año: Xiang, Q., Li, D., Hu, Z., Yuan, Y., Sun, Y., Zhu, Y., Fu, Y., Jiang, Y., et al. (2024).
- Versión leída: Docs/fuentes/pdf/Xiang2024QuantumCNN.pdf · versión publicada (Scientific Reports, 14(1), 24699, 2024; recibida en mayo 2024, publicada en línea el 18 de octubre de 2024) · 13 páginas
- Tipo: experimental (simulación numérica con PennyLane y PyTorch en hardware clásico)

## Qué concluye
- Propone el modelo QCCNN (Quantum Classical Hybrid Convolutional Neural Network), integrando una capa convolucional cuántica variacional con capas completamente conectadas clásicas para el diagnóstico de cáncer de mama — «In this work, we present a quantum hybrid classical convolutional neural network (QCCNN) based breast cancer diagnosis approach with the goal of utilizing quantum computing’s high-dimensional data processing power and parallelism to increase diagnosis efficiency and accuracy.» (p. 1)
- Reporta que los experimentos de simulación en tres conjuntos de datos (GBSG, SEER y WDBC) muestran que QCCNN supera en exactitud de clasificación a modelos de CNN clásica y regresión logística — «Simulation experiments on three breast cancer datasets, GBSG, SEER and WDBC, validate the robustness and generalization of QCCNN and significantly outperform CNN and logistic regression models in classification accuracy.» (p. 1)
- En el conjunto GBSG, QCCNN reporta un promedio de exactitud de 74.375% en entrenamiento y 70.498% en validación, frente a 58.944% de CNN y 60.583% de regresión logística (Tabla 2) — «The results show that QCCNN has the best performance among all models with an average accuracy of 74.375% and 70.498% on the training and validation sets, respectively.» (p. 9)
- En el conjunto SEER, QCCNN alcanza una exactitud promedio de 89.544% en entrenamiento y 90.088% en validación, frente a 89.091% de CNN y 89.125% de regresión logística (Tabla 3) — «The results show that QCCNN has the best performance among all models with an average accuracy of 89.544% and 90.088% on the training and validation sets, respectively.» (p. 9)
- En el conjunto WDBC, QCCNN obtiene una exactitud promedio de 97.099% en entrenamiento y 96.155% en validación, frente a 92.822% de CNN y 91.184% de regresión logística (Tabla 4) — «The results show that the average accuracy of QCCNN is 97.099% and 96.155% on the training and validation sets, respectively, which is significantly higher than that of CNN and logistic regression models.» (p. 10)
- Concluye que QCCNN obtiene el mejor desempeño de clasificación en todos los casos analizados — «The results show that QCCNN performs the best in terms of classification accuracy in all cases, significantly outperforming both the logistic regression model and CNN, confirming its superior performance in breast cancer diagnosis.» (p. 11)

## Qué deja como trabajo futuro o limitación declarada
- El diseño del circuito cuántico se evaluó en un estado ideal sin considerar los efectos del ruido en entornos NISQ realistas — «The design of current quantum circuits has not yet fully taken into account the effects of noise in realistic Noisy Intermediate Scale Quantum (NISQ) environments, as studied by Erik B. Terres Escudero et al.45, which may have an impact on the performance of the quantum model in practical applications.» (p. 11)
- Los experimentos se ejecutaron exclusivamente en un computador convencional clásico con aceleración GPU, admitiendo que no se evaluó en una QPU real y dejándolo como trabajo futuro — «In addition, the experiments in this study were conducted on a conventional computer, and although GPUs are able to accelerate some of the computations, their computational speed for quantum circuits is not yet comparable to that of a real quantum computer (QPU), and the use of QPUs will be further explored in future studies to fully evaluate the performance of the QCCNN in practical applications.» (p. 11)

## Diseño experimental (solo obras experimentales)
- Datos: tres conjuntos de datos tabulares obtenidos del repositorio Kaggle:
  - GBSG: 686 muestras y 11 variables clínicas — «The dataset has 11 distinctive features and 686 samples in its format.» (p. 3)
  - SEER: 4\,024 registros de pacientes con cáncer invasivo y 16 variables — «The dataset contains 4024 samples and 16 characteristic variables.» (p. 3)
  - WDBC: 569 muestras con 30 características morfométricas de núcleos celulares de aspiración con aguja fina — «The WDBC dataset contains digitized images of breast cancer masses acquired by fine needle aspiration (FNA) from which tumor features have been calculated. The dataset contains 30 features, 10 of which are real features calculated based on the geometry of the cell nucleus boundaries in the image. The dataset has 569 samples.» (p. 3)
- Plataforma: biblioteca PennyLane integrada con PyTorch — «In the experiment, we use the PyTorch framework to build and train the classical neural network part and integrate the PennyLane library to implement the quantum convolutional layer.» (p. 8)
- Partición: 70% entrenamiento y 30% validación — «70% of each dataset was used as the training set and the remaining 30% as the validation set, and accuracy was chosen as the key metric to measure the diagnostic performance of the model.» (p. 9)
- Métrica: porcentaje de exactitud de clasificación (Accuracy).
- Modelos comparados: QCCNN, CNN clásica y Regresión Logística.

## Las cuatro preguntas de H-046 (solo obras que reportan una ventaja o un resultado cuántico frente a clásico)
1. *¿El modelo clásico recibió el mismo ajuste y las mismas features?*
   Parcial. Los modelos recibieron las mismas características normalizadas al rango $[-\pi, \pi]$ mediante scikit-learn y la misma partición 70/30 (p. 3, p. 9). No obstante, los modelos clásicos de referencia (una CNN 1D y regresión logística) son arquitecturas no optimizadas para datos tabulares clínicos; no se compararon contra clasificadores de gradiente (XGBoost, LightGBM) ni redes neuronales tabulares estándar.
2. *¿La diferencia supera su incertidumbre (hay intervalos, desviaciones, pruebas)?*
   No. El artículo no reporta desviaciones estándar, intervalos de confianza ni pruebas de significación estadística (valores $p$) para las diferencias de exactitud en ninguna de las tablas (pp. 9–10). En el conjunto SEER, la diferencia en validación entre QCCNN (90.088%) y regresión logística (89.125%) es de apenas 0.963%, una variación mínima que carece de respaldo estadístico contra la variabilidad muestral.
3. *¿El test se usó una sola vez?*
   No. Solo se utilizó una partición de 70% entrenamiento y 30% validación, y a lo largo de las iteraciones de optimización los autores seleccionan y reportan explícitamente la «highest accuracy» alcanzada en el conjunto de validación (p. 9, p. 10), lo que evidencia fuga de datos (data leakage) y parada temprana sin un conjunto de prueba ciego independiente.
4. *¿El kernel o el circuito cuántico es realmente difícil de simular clásicamente?*
   No. El circuito cuántico consta de un número reducido de compuertas monoqubit ($R_x$, $R_y$) y compuertas de entrelazamiento $CR_z$, simulado en PennyLane sobre una computadora clásica convencional («conducted on a conventional computer», p. 11). No existe ninguna complejidad computacional que impida su simulación exacta clásica.

## Preguntas específicas
- **Conjuntos de datos (GBSG, SEER, WDBC):**
  Todos son conjuntos tabulares clínicos o patológicos descargados de Kaggle («The Kaggle website (a machine learning repository) provided the breast cancer diagnosis GBSG dataset, SEER dataset, and WDBC dataset used in this study.» p. 3):
  - GBSG: datos clínicos de supervivencia y pronóstico (686 pacientes, 11 variables).
  - SEER: registro epidemiológico poblacional (4\,024 pacientes, 16 variables).
  - WDBC: mediciones geométricas y de textura de núcleos celulares en frotis de aspiración con aguja fina (569 muestras, 30 variables).
  Ninguno de los tres conjuntos contiene imágenes mamográficas directas (DICOM).
- **El «hasta 5 %» de mejora:**
  La frase textual «hasta 5 %» no figura en el texto de Xiang et al. Proviene de una deducción realizada por el autor del Technical Report al restar la exactitud de validación de Regresión Logística (91.184%) de la de QCCNN (96.155%) en el dataset WDBC (diferencia de 4.971% $\approx 5\%$, Tabla 4, p. 10). En GBSG la diferencia promedio frente a CNN en validación es mayor (70.498% vs. 58.944%, +11.55%), mientras que en SEER es inferior al 1% (90.088% vs. 89.091%, Tabla 3, p. 9).
- **Frente a qué modelos:**
  Se compara contra dos modelos clásicos: una red neuronal convolucional clásica (CNN) y un modelo lineal de regresión logística (Logistic Regression).
- **Si hay incertidumbre reportada:**
  No hay incertidumbre reportada: no se proporcionan barras de error, intervalos de confianza, desviaciones estándar ni pruebas de hipótesis estadísticas.
- **Simulador o hardware:**
  Simulador clásico exclusivamente. Emplearon el framework PennyLane junto con PyTorch ejecutándose sobre una computadora clásica («In addition, the experiments in this study were conducted on a conventional computer», p. 11). No se utilizó ningún procesador cuántico físico (QPU).

## Relevancia para el TT
- Se conecta con §2.1.4 (línea 805) y la tabla de antecedentes (línea 927) del Technical Report.
- Ilustra un patrón metodológico recurrente identificado en H-046: reportes de supuesta superioridad cuántica en oncología que en realidad evalúan simuladores ideales sobre datos tabulares preexistentes, sin incertidumbre reportada, con fuga en la selección de validación y sin procesadores cuánticos físicos.
- **Qué NO se puede afirmar con esta fuente:**
  No se puede afirmar que Xiang et al. hayan trabajado con mamografías (el reporte dice «En el dominio de la mamografía, Xiang et al. (2024)...», lo cual es inexacto: evaluaron datos tabulares de biopsia por aspiración y registros clínicos). Tampoco se puede afirmar que hayan comprobado ventaja cuántica en hardware físico ni que hayan verificado significancia estadística.

## Contraste con lo que el proyecto ya le atribuye
- `Docs/Technical_Report.tex:559`: «El trabajo de Xiang et al. (2024), ilustra esta dirección. Se presenta un enfoque de diagnóstico de cáncer de mama basado en redes neuronales convolucionales híbridas cuántico-clásicas, con el objetivo de aprovechar la capacidad de procesamiento de datos de alta dimensión y el paralelismo de la computación cuántica para incrementar la eficiencia y precisión del diagnóstico...»
  - *¿Lo sostiene la obra?* Sí. Es una paráfrasis fiel del abstract y la introducción (p. 1).
- `Docs/Technical_Report.tex:805`: «En el dominio de la mamografía, Xiang et al. (2024) propusieron el modelo QCCNN evaluado sobre datasets tabulares (GBSG, SEER, WDBC), reportando mejoras de hasta 5\% en accuracy respecto a CNN y regresión logística clásicas.»
  - *¿Lo sostiene la obra?* Parcial:
    1. Xiang et al. no pertenecen al dominio de la mamografía por imagen; sus datos son tabulares (GBSG y SEER son registros clínicos, WDBC proviene de biopsia por aspiración con aguja fina, no mamografías).
    2. La cifra «hasta 5%» la calculó el autor de la tesis a partir de WDBC (96.16% vs. 91.18%), pero los autores de la obra no enuncian «hasta 5%» textualmente.
    3. No reportan intervalos de confianza ni pruebas de significación estadística, y la evaluación fue realizada en un simulador clásico (PennyLane).
- `Docs/Technical_Report.tex:927`: Entrada en la tabla de antecedentes indicando QCCNN (PennyLane) sobre GBSG / SEER / WDBC con simulación clásica.
  - *¿Lo sostiene la obra?* Sí. La tabla describe correctamente el entorno de simulación y los datasets empleados.
- `Other/referencias_por_revisar.md:88`: «Xiang et al. (2024), QCCNN sobre GBSG, SEER y WDBC (+5 % de accuracy)».
  - *¿Lo sostiene la obra?* Parcial (el +5% corresponde únicamente a la comparación con regresión logística en WDBC, no en los demás datasets).
