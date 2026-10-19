# Le2011FRQI · A flexible representation of quantum images for polynomial preparation, image compression, and processing operations

- Autores y año: Le, P. Q., Dong, F., & Hirota, K. (2011).
- Versión leída: Docs/fuentes/pdf/Le2011FRQI.pdf · versión publicada (Quantum Information Processing, 10(1), 63–84, 2011; en línea desde 2010) · 22 páginas
- Tipo: teórico y simulación

## Qué concluye
- Propone FRQI (Flexible Representation of Quantum Images) para representar imágenes digitales en computadoras cuánticas como un estado cuántico normalizado que codifica simultáneamente color y posición — «A Flexible Representation of Quantum Images (FRQI) is proposed to provide a representation for images on quantum computers in the form of a normalized state which captures information about colors and their corresponding positions in the images.» (p. 1)
- Formula el Teorema de Preparación Polinomial (PPT), que permite generar el estado FRQI a partir del estado base $|0\rangle^{\otimes 2n+1}$ mediante una secuencia de compuertas Hadamard y rotaciones controladas — «Theorem 1 (Polynomial preparation theorem) Given a vector θ = (θ0, θ1, . . . , θ22n−1), (n ∈N) of angles, there is a unitary transform P that turns quantum computers from the initialized state, |0⟩⊗2n+1 to the FRQI state» (p. 7)
- El número exacto de operaciones elementales para preparar el estado FRQI sin comprimir es $2^{4n} - 3 \cdot 2^{2n} + 2n$, que los autores describen como cuadrático respecto al número total de píxeles ($2^{2n}$ ángulos) — «The total number of simple operations used to prepare FRQI state is 2n + 22n × 22n−1 −1 + 22n−1 −2 = 24n −3.22n + 2n.» (p. 7)
- Define el algoritmo QIC (Quantum Image Compression), que reduce el número de compuertas cuánticas elementales necesarias agrupando píxeles con el mismo valor de color mediante minimización de expresiones booleanas — «Therefore, the process, which decreases the number of simple quantum gates in the preparation and reconstruction of quantum images, is called Quantum Image Compression (QIC).» (p. 7)
- Clasifica las operaciones unitarias de procesamiento de imágenes en tres categorías (G1 que afecta solo colores con complejidad $O(1)$, G2 que afecta colores en posiciones específicas con complejidad $O(N)$, y G3 que transforma color y posición con complejidad dependiente del operador como QFT) — «The number of simple gates used for an operation in the G1 category is one gate as in Fig. 12 that means the complexity of the G1 operation is O(1).» (p. 14)
- La complejidad de las operaciones G2 es lineal respecto al número de píxeles $N$ — «The number of controlled rotations used for an operator in the G2 category depends linearly on the number of positions involving the operator, O(N), where N is the number of positions in the whole image.» (p. 14)

## Qué deja como trabajo futuro o limitación declarada
- Reconoce que preparar una imagen de tamaño mediano requiere un número astronómico de compuertas simples (por ejemplo, $2^{32}$ compuertas para $2^{16}$ posiciones) — «For example a 216 position image needs 232 simple gates for preparation.» (p. 8)
- Plantea como trabajo futuro explorar operadores unitarios alternativos sustituyendo la QFT por wavelets cuánticas o transformada de coseno discreta — «The investigation on each of three types of image processing operations explores new operators on quantum images. For example, the quantum Wavelet transform, the quantum discrete cosine transform, etc. are able to replace quantum Fourier transform in the type-3 operation.» (p. 20)
- Señala la necesidad de analizar sistemáticamente las razones de compresión de QIC en bases de datos de imágenes más amplias — «Secondly, the systematic analysis of the compression ratios of QIC algorithm, presented in Sect. 3, on a larger database of images will provide more insights into the efﬁciency of the algorithm.» (p. 20)
- Identifica como pendiente el estudio de aspectos de teoría de la información y tolerancia a fallos mediante códigos de corrección de errores cuánticos para aplicaciones prácticas — «Thirdly, information-theoretic aspects on FRQI considering the existence of errors such as error-correcting codes are required for a robust representation for practical applications.» (p. 20)
- Sugiere extender el estudio a operaciones entre múltiples estados FRQI simultáneos, como búsqueda y coincidencia de patrones — «There are interesting questions on quantum operations having impacts on multiple images such as image matching, image searching» (p. 20)

## Diseño experimental (solo obras experimentales)
- Los experimentos se realizaron mediante simulación clásica en MATLAB utilizando vectores y matrices unitarias — «A classical computer was used to simulate the experiments on quantum images. The simulations are based on linear algebra with complex vectors as quantum states and unitary matrices as unitary transforms using Matlab.» (p. 14)
- Datos evaluados: imágenes binarias de dígitos individuales ($8 \times 8$ y $16 \times 16$) y la imagen de Lena en escala de grises ($256 \times 256$, es decir $2^{16}$ píxeles).
- Métricas: razón de compresión del algoritmo QIC y verificación de recuperación mediante probabilidades de medición — «The compression ratios of the QIC algorithm on single digit binary images range from 68.75 to 90.63% and on groups having the same gray level in the Lena image range from 6.67 to 31.62%.» (p. 20)
- Comparación clásica: se compara contra la representación matricial convencional de píxeles en términos del número de qubits versus bits requeridos.

## Las cuatro preguntas de H-046 (solo obras que reportan una ventaja o un resultado cuántico frente a clásico)
- No aplica: es una propuesta teórica y de simulación de representación cuántica de imágenes y compresión elemental, no un benchmark comparativo de aprendizaje supervisado cuántico vs. clásico con métricas de clasificación.

## Preguntas específicas
- **Complejidad de preparación del estado FRQI tal como la enuncian:**
  Los autores derivan que el número de compuertas elementales es «24n −3.22n + 2n» (p. 7) y afirman: «This number is quadratic to the total 22n angle values, θi, i = 0, 1, . . . , 22n −1. This indicates the effiency of the preparation process.» (p. 7). Califican la preparación de "polinomial" porque la complejidad es cuadrática respecto al número de píxeles $N = 2^{2n}$ ($O(N^2)$), pero en términos del número de qubits ($2n+1$), dicha complejidad es estrictamente exponencial: $O(2^{4n})$.
- **Cuántos qubits para una imagen de $2^n \times 2^n$:**
  Requiere exactamente $2n + 1$ qubits: $2n$ qubits de posición para direccionar los $2^{2n}$ píxeles espaciales y 1 qubit de color para almacenar las amplitudes de rotación $\cos\theta_i|0\rangle + \sin\theta_i|1\rangle$ — «The proposed PPT achieves a unitary preparation process using a polynomial number of simple operators transforming quantum computers from the initial state to FRQI state.» (p. 19).

## Relevancia para el TT
- Se conecta con §2.1.3 y las discusiones teóricas sobre codificación cuántica de datos: ilustra el cuello de botella de la preparación de imágenes en computación cuántica. Si bien almacena una imagen de $2^n \times 2^n$ en solo $2n+1$ qubits, la preparación requiere $O(2^{4n})$ operaciones elementales.
- **Qué NO se puede afirmar con esta fuente:**
  No se puede afirmar que FRQI permita una preparación eficiente en tiempo polinomial respecto al número de qubits (es $O(2^{4n})$, exponencial en qubits). Tampoco se puede afirmar que FRQI clasifique patologías mamográficas ni que ofrezca ventaja computacional probada en aprendizaje automático sobre imágenes médicas.

## Contraste con lo que el proyecto ya le atribuye
- `Other/verificacion/referencias_por_revisar.md:55`: «Dato a confirmar en la fuente original de FRQI: la complejidad de preparación O(2⁴ⁿ) que reporta la búsqueda».
  - *¿Lo sostiene la obra?* Sí. En la p. 7, ecuación (10), la cantidad total de compuertas simples es $2^{4n} - 3 \cdot 2^{2n} + 2n$, cuyo orden dominante es $O(2^{4n})$.
- `Other/verificacion/referencias_por_revisar.md:60`: «De memoria: Le et al. (2011) para FRQI y Zhang et al. (2013) para NEQR. No citar sin verificar».
  - *¿Lo sostiene la obra?* Sí. La referencia verificada corresponde exactamente a Le, Dong y Hirota (2011), *Quantum Information Processing* 10(1), 63–84.
