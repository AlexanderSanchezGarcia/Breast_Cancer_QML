# Informe de Ejecución · T1 Fichas de Lectura (Grupo C)

**Fecha:** 2026-10-14  
**Trabajador:** Dispatch `ctx_d8b6673870a1` · Tarea `task_5fa40680a242` · Terminal `term_52d6733d-8ecc-412a-8231-f8a7e8eb3804`  
**Grupo asignado:** Grupo C (imágenes cuánticas y trabajos aplicados a cáncer)  
**Claves asignadas:** `Parigi2026QImR`, `Le2011FRQI`, `Zhang2013NEQR`, `Azevedo2022QuantumTransfer`, `Xiang2024QuantumCNN`, `ElHafidi2025`.

---

## 1. Resumen ejecutivo

1. **Qué se hizo:** Se analizaron en profundidad las fuentes primarias en PDF y texto extraído de las seis obras del Grupo C y se redactaron las fichas correspondientes en `Docs/insumos/fichas/<Clave>.md`, dando respuesta exhaustiva a todas las preguntas específicas, completando la auditoría metodológica de las cuatro preguntas de H-046 y contrastando cada afirmación previa del reporte técnico, la bitácora de decisiones y los documentos de auditoría.
2. **Qué se encontró:** Se verificó el 100 % de las citas textuales de las seis fichas (86 citas literales exactas sin ningún fallo en el verificador sintáctico `verificar_citas_fichas.py`). Se identificaron y documentaron discrepancias críticas en el Technical Report:
   - En `Azevedo2022QuantumTransfer`: se corroboró que las dos líneas de trabajo futuro asumidas por la tesis (separación por masas/calcificaciones y estudio de la distribución en el espacio de Hilbert) provienen textualmente de la p. 12 de Azevedo et al., pero el Technical Report nombra erróneamente el dataset BCDR como «Barcelona Digital Breast Cancer Dataset» (el nombre real es *Breast Cancer Digital Repository*), omite que el 84 % de exactitud lo obtiene por igual la ResNet clásica con *transfer learning* (el mérito es del preentrenamiento, no del circuito cuántico) y omite que en hardware físico (`ibm_lagos`) la exactitud desciende al 81 %.
   - En `Xiang2024QuantumCNN`: se descubrió que los autores no trabajan en el dominio de la mamografía sino con datos tabulares clínicos y citológicos (GBSG, SEER, WDBC); que la frase «mejoras de hasta 5 %» no es literal de la obra sino un cálculo del tesista sobre WDBC; y que el trabajo presenta las falencias metodológicas típicas de H-046 (simulación sin ruido, sin intervalos de confianza y con fuga de datos en validación).
   - En `ElHafidi2025`: se confirmaron las cifras de ZZ (0.91) y Pauli (0.96), pero se descubrió que el reporte omitió que el SVM clásico con kernel RBF alcanzó 0.95 de exactitud (empate técnico con Pauli), que los datos son tabulares clínicos de encuesta y no imágenes, y que fue ejecutado en `qasm_simulator`.
   - En `Parigi2026QImR`: se constató que la obra sostiene taxativamente que el coste exponencial de carga de estados ($O(2^n)$) predomina y compromete la ventaja cuántica, y que los kernels cuánticos no superan en exactitud al kernel lineal clásico.
   - En `Le2011FRQI` y `Zhang2013NEQR`: se verificaron las complejidades exactas ($O(2^{4n})$ con $2n+1$ qubits para FRQI; $O(qn2^{2n})$ con $q+2n$ qubits para NEQR), demostrando por qué ambas codificaciones son inviables para mamografías completas en hardware NISQ.
3. **Qué queda pendiente / lo que no se pudo hacer:** No se dejó ningún marcador `[VERIFICAR]`. Las seis fichas están completas y aprobadas por el script de aceptación. Queda pendiente para el autor corregir en `Docs/Technical_Report.tex` el nombre de BCDR (§2.1.5, línea 828), matizar la atribución de exactitud de Azevedo et al. y Xiang et al., e incorporar la cita formal a El Hafidi et al. (2025) en la línea 783.

---

## 2. Archivos creados

1. `Docs/insumos/fichas/Parigi2026QImR.md`: 17 citas verificadas.
2. `Docs/insumos/fichas/Le2011FRQI.md`: 16 citas verificadas.
3. `Docs/insumos/fichas/Zhang2013NEQR.md`: 13 citas verificadas.
4. `Docs/insumos/fichas/Azevedo2022QuantumTransfer.md`: 15 citas verificadas.
5. `Docs/insumos/fichas/Xiang2024QuantumCNN.md`: 13 citas verificadas.
6. `Docs/insumos/fichas/ElHafidi2025.md`: 12 citas verificadas.
7. `Docs/insumos/noche/informe_T1_C.md`: este informe.

---

## 3. Pruebas de aceptación

Se ejecutó el script oficial `python3 Code/tools/verificar_citas_fichas.py` sobre cada una de las fichas del Grupo C:

```text
$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Parigi2026QImR.md
Parigi2026QImR.md: OK · 17/17 citas verificadas
1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Le2011FRQI.md
Le2011FRQI.md: OK · 16/16 citas verificadas
1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Zhang2013NEQR.md
Zhang2013NEQR.md: OK · 13/13 citas verificadas
1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Azevedo2022QuantumTransfer.md
Azevedo2022QuantumTransfer.md: OK · 15/15 citas verificadas
1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Xiang2024QuantumCNN.md
Xiang2024QuantumCNN.md: OK · 13/13 citas verificadas
1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/ElHafidi2025.md
ElHafidi2025.md: OK · 12/12 citas verificadas
1/1 fichas pasan.
```

Salida colectiva sobre el directorio general `Docs/insumos/fichas/`:
```text
$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/
Azevedo2022QuantumTransfer.md: OK · 15/15 citas verificadas
Bowles2024Benchmarking.md: OK · 19/19 citas verificadas
Canatar2023Bandwidth.md: OK · 18/18 citas verificadas
ElHafidi2025.md: OK · 12/12 citas verificadas
Glick2024Covariant.md: OK · 34/34 citas verificadas
Guyon2003.md: OK · 14/14 citas verificadas
Huang2022Experiments.md: OK · 28/28 citas verificadas
Hubregtsen2022.md: OK · 10/10 citas verificadas
Kubler2021Inductive.md: OK · 21/21 citas verificadas
Le2011FRQI.md: OK · 16/16 citas verificadas
Lee2017CBISDDSM.md: OK · 20/20 citas verificadas
Liu2021Speedup.md: OK · 31/31 citas verificadas
Mari2020Transfer.md: OK · 12/12 citas verificadas
McClean2018Barren.md: OK · 13/13 citas verificadas
Parigi2026QImR.md: OK · 17/17 citas verificadas
Preskill2018NISQ.md: OK · 17/17 citas verificadas
Schuld2021Encoding.md: OK · 10/10 citas verificadas
SchuldKilloran2022Advantage.md: OK · 13/13 citas verificadas
Shaydulin2022Bandwidth.md: OK · 25/25 citas verificadas
Thanasilp2024.md: OK · 22/22 citas verificadas
Xiang2024QuantumCNN.md: OK · 13/13 citas verificadas
Zhang2013NEQR.md: OK · 13/13 citas verificadas
huang2021power.md: OK · 41/41 citas verificadas

23/23 fichas pasan.
```

---

## 4. Tabla de discrepancias entre lo que el proyecto atribuye y lo que la obra dice

Esta tabla detalla cada referencia o afirmación identificada en `Docs/Technical_Report.tex`, `Other/verificacion/referencias_por_revisar.md`, `Other/verificacion/correcciones_verificadas.md` y `Other/bitacora_decisiones.md`, contrastada con el contenido real de la obra (citada según la regla de citas externas con clave explícita):

| Clave | Archivo y línea | Qué afirma el proyecto | Lo que la obra sostiene realmente | Estado de verificación | Cita literal de respaldo en la fuente |
|---|---|---|---|---|---|
| `Azevedo2022QuantumTransfer` | `Docs/Technical_Report.tex:828` | Llama al dataset «BCDR (Barcelona Digital Breast Cancer Dataset)» | El dataset se llama «Breast Cancer Digital Repository» (o Breast Cancer Digital Repository). No tiene relación con Barcelona; fue desarrollado por un consorcio portugués-español (INEGI, FMUP-CHSJ Universidade do Porto, CETA-CIEMAT, Universidade de Aveiro). | **Discrepancia / Erróneo en el reporte** | «Breast Cancer Data Repository (BCDR) dataset (Lopez et al. 2012).» (Azevedo2022QuantumTransfer, p. 4) y «Guevara MA (2020) Breast cancer digital repository.» (Azevedo2022QuantumTransfer, p. 13) |
| `Azevedo2022QuantumTransfer` | `Docs/Technical_Report.tex:829` | «obteniendo 84\% de accuracy» (atribuido a la red cuántica) | El 84 % de exactitud en el conjunto de prueba lo obtienen **tanto** el modelo clásico con transfer learning (`C+TL`) como los modelos híbridos cuánticos `CQ1` y `CQ4`. El modelo clásico sin TL obtiene 67 %. La ventaja cuántica observada en simulación no es de exactitud, sino de **AUC (0.77 frente a 0.58)**. En procesador físico (`ibm_lagos`), la exactitud cae a **81 %**. | **Parcial / Matiz crítico** | «The classical residual neural network, without resourcing to TL, achieved a maximum of 67% accuracy while our other experiments» (Azevedo2022QuantumTransfer, p. 11), «using TL achieved 84%.» (Azevedo2022QuantumTransfer, p. 12), «The results for every metric are far more consistent between training and testing and between epochs when using the dressed quantum circuit, so much so that AUC value went from 58 to 77%, leading us to believe that a hybrid-quantum network does present some advantage as AUC measures how well the model separates two classes.» (Azevedo2022QuantumTransfer, p. 12), y «It is too soon to say whether or not QML can be an advantage. Our results only point to a good generalization of complex data which needs further testing.» (Azevedo2022QuantumTransfer, p. 11) |
| `Azevedo2022QuantumTransfer` | `Docs/Technical_Report.tex:613, 830` y `Other/bitacora_decisiones.md:44, 366` (D-019) | Señala como trabajo futuro separar por tipo de hallazgo mamográfico y evaluar la distribución de los datos en el espacio de Hilbert | Azevedo et al. señalan textualmente ambas líneas de trabajo futuro en la p. 12: evaluar masas y calcificaciones por separado, y analizar cómo aparecen los datos en el espacio de Hilbert como conglomerados compactos. | **Sí lo sostiene palabra por palabra** | «As future work, an interesting approach could be to separate the dataset into masses and calcifications and only then perform classification. That way, we would be evaluating different specific features in a similar scenario and would probably get clearer results.» (Azevedo2022QuantumTransfer, p. 12) y «Lastly, the best way to know how well this model performs would be to see how the data appears in our Hilbert space. Ideally, both classes would appear very separately in it, as tight clusters.» (Azevedo2022QuantumTransfer, p. 12) |
| `Xiang2024QuantumCNN` | `Docs/Technical_Report.tex:805` | «En el dominio de la mamografía, Xiang et al. (2024) propusieron el modelo QCCNN evaluado sobre datasets tabulares (GBSG, SEER, WDBC)...» | Xiang et al. no trabajan con imágenes mamográficas. Los tres conjuntos son tabulares: GBSG son 11 variables clínicas de ensayo clínico; SEER son 16 variables epidemiológicas; WDBC son 30 características morfométricas de núcleos celulares obtenidos por punción con aguja fina (FNA). No hay mamografías DICOM ni proyecciones radiológicas. | **Discrepancia en el reporte** | «The Kaggle website (a machine learning repository) provided the breast cancer diagnosis GBSG dataset, SEER dataset, and WDBC dataset used in this study.» (Xiang2024QuantumCNN, p. 3) y «The WDBC dataset contains digitized images of breast cancer masses acquired by fine needle aspiration (FNA) from which tumor features have been calculated. The dataset contains 30 features, 10 of which are real features calculated based on the geometry of the cell nucleus boundaries in the image. The dataset has 569 samples.» (Xiang2024QuantumCNN, p. 3) |
| `Xiang2024QuantumCNN` | `Docs/Technical_Report.tex:805` | «reportando mejoras de hasta 5\% en accuracy respecto a CNN y regresión logística clásicas» | La frase «hasta 5 %» no aparece en el texto del artículo. Corresponde a una deducción realizada por el autor de la tesis al restar la exactitud de validación de Regresión Logística (91.184 %) de la de QCCNN (96.155 %) en WDBC (+4.971 % $\approx$ 5 %). En GBSG la mejora promedio frente a CNN en validación es mayor (+11.55 %), mientras que en SEER es menor a 1 % (+0.963 %). | **Parcial / Cifra derivada por el autor** | «The results show that the average accuracy of QCCNN is 97.099% and 96.155% on the training and validation sets, respectively, which is significantly higher than that of CNN and logistic regression models.» (Xiang2024QuantumCNN, p. 10) |
| `Xiang2024QuantumCNN` | `Other/verificacion/referencias_por_revisar.md:88` y `Docs/Technical_Report.tex:927` | QCCNN evaluado en simulación con PennyLane | Es exactamente el entorno experimental utilizado (PennyLane con PyTorch en CPU/GPU convencional, sin hardware cuántico físico QPU). No reportan intervalos de confianza ni pruebas estadísticas de significancia. | **Sí lo sostiene** | «In addition, the experiments in this study were conducted on a conventional computer, and although GPUs are able to accelerate some of the computations, their computational speed for quantum circuits is not yet comparable to that of a real quantum computer (QPU), and the use of QPUs will be further explored in future studies to fully evaluate the performance of the QCCNN in practical applications.» (Xiang2024QuantumCNN, p. 11) |
| `ElHafidi2025` | `Docs/Technical_Report.tex:783` | «ZZFeatureMap alcanzó una accuracy de 0.91 y F1-score de 0.91, mientras que PauliFeatureMap logró un rendimiento consistente de 0.96 en todas las métricas incluyendo accuracy, precisión, recall y F1-score; la elección del mapa apropiado depende de dos factores principales, la naturaleza de los datos y la resiliencia al ruido del dispositivo cuántico.» | Las cifras 0.91 y 0.96 son exactas y la afirmación de los dos factores proviene textualmente del artículo. Sin embargo, el reporte omite que el modelo clásico **SVM con kernel RBF alcanzó 0.95 de exactitud** (prácticamente igual a Pauli y superior a ZZ), que el conjunto de datos es tabular clínico de encuesta (309 pacientes, 15 variables) y no imágenes mamográficas, y que fue ejecutado en simulación (`qasm_simulator`), no en hardware físico. | **Sí lo sostiene en las cifras / Omisión crítica de contexto** | «for ZZFeatureMap, the results were an accuracy of 0.91, precision of 0.87, recall of 0.96, specificity of 0.85, and F1-score of 0.91; and for PauliFeatureMap, the model achieved a consistent performance of 0.96 across all metrics, including accuracy, precision, recall, specificity, and F1-score.» (ElHafidi2025, p. 9), «The radial basis function (RBF) kernel provided the best results, with an accuracy of 0.95, precision of 0.98, recall of 0.92, specificity of 0.98, and F1-score of 0.95.» (ElHafidi2025, p. 9) y «The choice of an appropriate feature map depends on two major factors: the nature of the data and the noise resilience of the quantum device.» (ElHafidi2025, p. 6) |
| `Parigi2026QImR` | Hipótesis de uso en el TT (`T1_fichas.md` p. 70) | ¿Sostiene que «el coste de carga anula la ventaja»? | Sí, lo sostiene de forma terminante: los protocolos conocidos para cargar datos en $n$ qubits demandan $O(2^n)$ compuertas cuánticas, lo que predomina en la complejidad y compromete la ventaja cuántica. Además, los kernels cuánticos basados en representaciones de imagen (FRQI, NEQR, QPIE, TNR) empatan en exactitud con el kernel lineal clásico ($0.99 \pm 0.00$ en MNIST). | **Sí lo sostiene plenamente** | «However, we highlight that to date the best known protocols for loading an exact representation of the data into an n-qubit state require a number of quantum gates equal to O(2n), which predominates the complexity of quantum algorithms and compromises its potential quantum advantage7.» (Parigi2026QImR, p. 8) y «Quantum kernels on average perform binary classification with the same accuracy as the classical linear kernel, but with exponentially lower storage cost.» (Parigi2026QImR, p. 7) |
| `Le2011FRQI` | `Other/verificacion/referencias_por_revisar.md:55` | «Dato a confirmar en la fuente original de FRQI: la complejidad de preparación O(2⁴ⁿ) que reporta la búsqueda» | Verificado: la fórmula exacta de compuertas elementales es $2^{4n} - 3 \cdot 2^{2n} + 2n$, cuyo término dominante es efectivamente $O(2^{4n})$. Los autores la llaman "polinomial" porque es cuadrática respecto al número de píxeles $N = 2^{2n}$ ($O(N^2)$), pero en función de los qubits es estrictamente exponencial ($O(2^{4n})$). Qubits necesarios: $2n+1$. | **Sí lo sostiene** | «The total number of simple operations used to prepare FRQI state is 2n + 22n × 22n−1 −1 + 22n−1 −2 = 24n −3.22n + 2n.» (Le2011FRQI, p. 7) y «This number is quadratic to the total 22n angle values, θi, i = 0, 1, . . . , 22n −1. This indicates the effiency of the preparation process.» (Le2011FRQI, p. 7) |
| `Zhang2013NEQR` | `Other/verificacion/referencias_por_revisar.md:60` | Fuente original de NEQR y comparación con FRQI | Verificado: NEQR reduce la complejidad temporal de preparación de $O(2^{4n})$ a $O(qn2^{2n})$ (reducción cuadrática), permite recuperación determinista y emplea $q+2n$ qubits ($q-1$ qubits adicionales frente a FRQI). Sigue siendo exponencial en el número de qubits de posición. | **Sí lo sostiene** | «Theorem 2 The whole preparation of NEQR costs no more than O(qn22n) for a 2n × 2n image with gray range 2q. This is equivalent to an approximately quadratic decrease compared to FRQI.» (Zhang2013NEQR, p. 10) y «NEQR needs q + 2n qubits to represent a 2n × 2n image with gray range 2q.» (Zhang2013NEQR, p. 6) |

---

## 5. Recomendaciones específicas para el autor del Technical Report

1. **Corregir el nombre de BCDR en `Docs/Technical_Report.tex` (línea 828):**  
   Reemplazar «BCDR (Barcelona Digital Breast Cancer Dataset)» por «BCDR (Breast Cancer Digital Repository)» o «Breast Cancer Digital Repository». El dataset fue producido por el consorcio IMED en Portugal y España (INEGI, Universidad de Oporto, CETA-CIEMAT, Universidad de Aveiro).
2. **Calibrar la afirmación sobre el 84 % de Azevedo et al. (línea 829):**  
   Aclarar que el 84 % de exactitud fue obtenido por igual mediante el modelo clásico ResNet con *transfer learning* (`C+TL`), y que la aportación del circuito variacional se observó en el AUC (0.77 frente a 0.58 en simulación), mientras que en el hardware cuántico físico (`ibm_lagos`) la exactitud fue del 81 %.
3. **Calibrar la contextualización de Xiang et al. (línea 805):**  
   Modificar la frase «En el dominio de la mamografía, Xiang et al. (2024)...» para indicar con precisión que evaluaron conjuntos tabulares clínicos y citológicos de biopsia por aspiración (GBSG, SEER, WDBC), y que la cifra de mejora de «hasta 5 %» corresponde a la comparación puntual con regresión logística en WDBC, en un entorno de simulación sin ruido ni intervalos de confianza.
4. **Incorporar la cita y matiz de El Hafidi et al. (línea 783):**  
   Añadir la cita formal `\cite{ElHafidi2025}` (definida en `bibitems_nuevos.tex`) al párrafo de la línea 783. Conviene explicitar que en dicho estudio el SVM clásico con kernel RBF alcanzó 0.95 de exactitud (frente a 0.96 de PauliFeatureMap y 0.91 de ZZFeatureMap), lo cual refuerza la conclusión del proyecto de que las transformaciones cuánticas deben evaluarse frente a kernels clásicos competitivos y no lineales.
5. **Aprovechar Parigi et al. (2026) y las obras fundacionales FRQI/NEQR en §2.1.3:**  
   Utilizar la cita verificada de Parigi et al. (2026) («However, we highlight that to date the best known protocols for loading an exact representation of the data into an n-qubit state require a number of quantum gates equal to O(2n), which predominates the complexity of quantum algorithms and compromises its potential quantum advantage7.» (Parigi2026QImR, p. 8)) para blindar la justificación teórica del pipeline: la codificación directa de imágenes en el espacio de Hilbert es impracticable en NISQ ($O(2^{4n})$ en FRQI y $O(qn2^{2n})$ en NEQR), lo que hace metodológicamente mandatorio el uso de radiomics y descriptores morfológicos compactos previa transformación cuántica variacional.
