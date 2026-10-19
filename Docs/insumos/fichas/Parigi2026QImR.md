# Parigi2026QImR · Analysis of quantum image representations for supervised classification

- Autores y año: Parigi, M., Khosrojerdi, M., Caruso, F., & Banchi, L. (2026).
- Versión leída: Docs/fuentes/pdf/Parigi2026QImR.pdf · preprint de arXiv (arXiv:2507.22039v2, 14 de enero de 2026; publicado en AVS Quantum Science, 8(1), 013801, 2026) · 9 páginas
- Tipo: experimental (simulación numérica de kernels cuánticos y SVM)

## Qué concluye
- Examina y compara las propiedades de compresión de cuatro representaciones cuánticas de imágenes: TNR (Tensor Network Representation), FRQI, NEQR y QPIE (Quantum Probability Image Encoding) — «In this work, we compare and examine the compression properties of four different Quantum Image Representations (QImRs): namely, Tensor Network Representation (TNR), Flexible Representation of Quantum Image (FRQI), Novel Enhanced Quantum Representation NEQR, and Quantum Probability Image Encoding (QPIE).» (p. 1)
- Las representaciones FRQI y QPIE comprimen la información de la imagen en mucha mayor medida que TNR y NEQR — «Our simulations show that FRQI and QPIE perform a higher compression of image information than TNR and NEQR.» (p. 1)
- El solapamiento entre estados en las matrices de Gram refleja directamente esta diferencia de compresión: los elementos fuera de la diagonal de FRQI y QPIE se sitúan en $[0.8, 1]$, los de NEQR en $[0, 0.4]$ y los de TNR en un nivel intermedio $[0.4, 0.7]$ — «In fact, the most off-diagonal elements of FRQI and QPIE Gram matrices are in the range [0.8,1], while for NEQR case they are in the interval [0,0.4]. The TNR Gram matrix shows an intermediate level of compression with respect to FRQI, QPIE, and NEQR, and its elements are in the range [0.4,0.7].» (p. 7)
- Los kernels cuánticos basados en QImR alcanzan en promedio una precisión de clasificación comparable a la del kernel lineal clásico, pero reducen exponencialmente los recursos requeridos para almacenar la imagen — «Our results indicate that quantum kernels provide comparable classification average accuracy but require exponentially fewer resources for image storage.» (p. 1)
- La precisión promedio en clasificación binaria es idéntica entre los kernels cuánticos y el lineal clásico — «Quantum kernels on average perform binary classification with the same accuracy as the classical linear kernel, but with exponentially lower storage cost.» (p. 7)
- En MNIST, todos los kernels (FRQI, NEQR, QPIE y lineal) alcanzan $0.99 \pm 0.00$ de accuracy (TNR logra $0.99 \pm 0.04$); en Fashion-MNIST, QPIE y lineal logran $0.96 \pm 0.02$, TNR y FRQI $0.95 \pm 0.02$, y NEQR $0.94 \pm 0.02$ (Tabla IV, p. 7).
- La exactitud media obtenida con kernels cuánticos es equiparable a la clásica, con menores requerimientos de memoria — «We find that the mean accuracy of quantum kernels is comparable to the classical one, but quantum kernels require exponentially fewer computational resources to store the image than their classical counterpart.» (p. 8)

## Qué deja como trabajo futuro o limitación declarada
- El costo de preparación del estado cuántico desafía directamente la aceleración potencial: los mejores protocolos conocidos para cargar datos exactos en $n$ qubits requieren $O(2^n)$ compuertas, lo que predomina en la complejidad y compromete la ventaja cuántica — «However, we highlight that to date the best known protocols for loading an exact representation of the data into an n-qubit state require a number of quantum gates equal to O(2n), which predominates the complexity of quantum algorithms and compromises its potential quantum advantage7.» (p. 8)
- La carga eficiente de datos clásicos en un estado cuántico sigue siendo un problema abierto — «An efficient loading of the classical date into a quantum state is still an open question.» (p. 8)
- La supuesta aceleración exponencial de transformadas como Fourier o Wavelet en imágenes se ve comprometida por el costo de preparación de los estados iniciales — «Furthermore, quantum operations3,4 such as Fourier, Hadamard, and Haar wavelet transforms, which are usually included as subroutines in image processing tasks, provide exponential speed-up over their classical counterparts2,5,6, which is nonetheless challenged by state preparation costs7.» (p. 1)
- Plantea como trabajo futuro extender la comparación a imágenes en color RGB y frente a otros kernels clásicos no lineales — «A future research direction could be to extend the study to RGB images and compare them with other types of classical kernels.» (p. 8)
- Señala como perspectiva relevante evaluar el desempeño de los kernels QImR directamente en hardware cuántico bajo la presencia de ruido — «Finally, another interesting perspective could be the possibility of studying the accuracy performance of QImR kernels when they are implemented on quantum hardware and noise effects occur.» (p. 8)

## Diseño experimental (solo obras experimentales)
- Datos y tamaño: imágenes de MNIST y Fashion-MNIST redimensionadas a $16 \times 16$ píxeles en escala de grises — «Grayscale images resized to 16×16 pixels.» (p. 6)
- Tarea y partición: clasificación binaria emparejada (clase 0 frente a clases 1–9) evaluada con 1\,000 imágenes de entrenamiento y 100 de prueba mediante validación cruzada k-fold — «We perform binary classification using a SVM with training and testing sets consisting of 103 and 102 images, respectively.» (p. 6)
- Modelos: Support Vector Machine (SVM) con kernels precomputados en scikit-learn con parámetros por defecto (Tabla II, p. 6).
- Parámetros de TNR: representación en Matrix Product States (MPS) con dimensión de enlace $\chi = 6$ — «The bond dimension for the TNR is equal to 6.» (p. 7)
- Métricas: media y error estándar de la media (SEM) de la exactitud de clasificación (accuracy).
- Simulador / hardware: todos los experimentos se realizaron en simulación clásica numérica (no se ejecutó en procesadores cuánticos físicos).
- Comparación clásica: kernel lineal clásico ($K(x_i, x_j) = x_i^T x_j$), requiriendo 2\,048 bits frente a 8–16 qubits de los modelos cuánticos para imágenes de $16 \times 16$.

## Las cuatro preguntas de H-046 (solo obras que reportan una ventaja o un resultado cuántico frente a clásico)
1. *¿El modelo clásico recibió el mismo ajuste y las mismas features?*
   Sí. Tanto el clasificador lineal clásico como los modelos cuánticos utilizaron la misma implementación de SVM en scikit-learn con hiperparámetros estándar, sobre exactamente las mismas imágenes preprocesadas y normalizadas de $16 \times 16$ (Tabla II, p. 6).
2. *¿La diferencia supera su incertidumbre (hay intervalos, desviaciones, pruebas)?*
   No aplica / No. No se reporta ninguna ventaja en exactitud a favor de los modelos cuánticos. En MNIST hay empate exacto ($0.99 \pm 0.00$), y en Fashion-MNIST el kernel clásico lineal ($0.96 \pm 0.02$) empata con QPIE ($0.96 \pm 0.02$) y supera numéricamente a TNR ($0.95 \pm 0.02$), FRQI ($0.95 \pm 0.02$) y NEQR ($0.94 \pm 0.02$), todas diferencias comprendidas dentro del margen de error estándar (Tabla IV, p. 7).
3. *¿El test se usó una sola vez?*
   Sí. Se evaluó mediante validación cruzada k-fold con conjuntos de prueba separados de 100 imágenes por par de clases (p. 6).
4. *¿El kernel o el circuito cuántico es realmente difícil de simular clásicamente?*
   No. Todos los kernels cuánticos fueron simulados en computadoras clásicas mediante contracciones tensoriales o fórmulas analíticas cerradas (p. ej. cálculo escalar del solapamiento para FRQI y QPIE, y contracción MPS para TNR con dimensión de enlace $\chi=6$). Ninguno presenta intratabilidad clásica.

## Preguntas específicas
- **Las cuatro representaciones y su compresión:**
  Evalúa TNR, FRQI, NEQR y QPIE. FRQI y QPIE logran una compresión mucho mayor que NEQR y TNR («Our simulations show that FRQI and QPIE perform a higher compression of image information than TNR and NEQR.» p. 1). En las matrices de Gram sobre imágenes de Fashion-MNIST, los elementos fuera de la diagonal de FRQI y QPIE se concentran en $[0.8, 1.0]$, indicando que los estados cuánticos representativos colapsan hacia regiones estrechas del espacio de Hilbert, mientras que NEQR exhibe solapamientos en $[0.0, 0.4]$ y TNR en $[0.4, 0.7]$ (p. 7).
- **Si discuten el coste de preparar el estado (cítalo literal):**
  Sí lo discuten de forma explícita y contundente:
  «However, we highlight that to date the best known protocols for loading an exact representation of the data into an n-qubit state require a number of quantum gates equal to O(2n), which predominates the complexity of quantum algorithms and compromises its potential quantum advantage7.» (p. 8).
  Asimismo, en la introducción afirman: «Furthermore, quantum operations3,4 such as Fourier, Hadamard, and Haar wavelet transforms, which are usually included as subroutines in image processing tasks, provide exponential speed-up over their classical counterparts2,5,6, which is nonetheless challenged by state preparation costs7.» (p. 1).
- **Qué kernels comparan y con qué conclusión:**
  Comparan cuatro kernels cuánticos derivados de cada representación (kernel TNR basado en traza de MPS, kernel FRQI basado en cosenos de diferencias de ángulos, kernel NEQR basado en delta de Kronecker de amplitudes, y kernel QPIE basado en producto interno de amplitudes normalizadas) frente al kernel lineal clásico ($x_i^T x_j$). Concluyen que los kernels cuánticos alcanzan en promedio la misma precisión de clasificación que el kernel lineal clásico, sin mejora predictiva, aunque con menor espacio de almacenamiento teórico en qubits (p. 7, Tabla IV).
- **Si la obra sostiene que «el coste de carga anula la ventaja»:**
  Sí, la obra sostiene plenamente esta afirmación. Afirma explícitamente que los protocolos de carga de datos en estados cuánticos demandan $O(2^n)$ compuertas, lo que predomina sobre la complejidad del algoritmo y «compromises its potential quantum advantage» (p. 8).

## Relevancia para el TT
- Se conecta directamente con §2.1.3, §2.1.4 y el hallazgo H-046: respalda teórica y empíricamente la decisión del proyecto de no cargar directamente imágenes completas en estados cuánticos tipo FRQI/NEQR/QPIE. Demuestra que:
  1) Los kernels cuánticos de imagen directa no superan a un kernel lineal clásico básico en precisión de clasificación.
  2) La supuesta ventaja cuántica se anula en la práctica debido al costo exponencial de preparación de estados ($O(2^n)$).
  3) Respaldan que la extracción clásica de características (radiomics / morfología) previa a la codificación cuántica es la única vía viable y fundamentada.
- **Qué NO se puede afirmar con esta fuente:**
  No se puede afirmar que los kernels cuánticos de imágenes brinden una precisión superior a los métodos clásicos (hubo empate estricto en MNIST y ligera ventaja clásica en Fashion-MNIST). Tampoco se puede afirmar que hayan probado imágenes mamográficas ni datos médicos reales (usaron únicamente dígitos y prendas de $16 \times 16$).

## Contraste con lo que el proyecto ya le atribuye
- `Other/verificacion/referencias_por_revisar.md:52`: «Verificado: título y arXiv:2507.22039. Compara representaciones como FRQI y NEQR para clasificación supervisada».
  - *¿Lo sostiene la obra?* Sí. La obra compara TNR, FRQI, NEQR y QPIE en tareas de clasificación supervisada con SVM.
- `Other/verificacion/correcciones_verificadas.md:86`: «Parigi, Khosrojerdi, Caruso y Banchi, Analysis of quantum image representations for supervised classification (arXiv:2507.22039) | AVS Quantum Science 8(1), 013801 (2026)».
  - *¿Lo sostiene la obra?* Sí. Coincide exactamente con los metadatos bibliográficos y el contenido del preprint verificado.
