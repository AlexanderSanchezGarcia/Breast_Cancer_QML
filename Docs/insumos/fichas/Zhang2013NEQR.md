# Zhang2013NEQR · NEQR: A novel enhanced quantum representation of digital images

- Autores y año: Zhang, Y., Lu, K., Gao, Y., & Wang, M. (2013).
- Versión leída: Docs/fuentes/pdf/Zhang2013NEQR.pdf · versión publicada (Quantum Information Processing, 12(8), 2833–2860, 2013) · 28 páginas
- Tipo: teórico y simulación

## Qué concluye
- Propone NEQR (Novel Enhanced Quantum Representation) como una mejora sustancial sobre FRQI, empleando por primera vez el estado base de una secuencia de qubits para almacenar los valores de escala de grises en lugar de amplitudes de probabilidad — «In this paper, based on analysis of existing quantum image representations, a novel enhanced quantum representation (NEQR) for digital images is proposed, which improves the latest ﬂexible representation of quantum images (FRQI).» (p. 1)
- La representación en base ortogonal permite distinguir determinísticamente diferentes escalas de grises — «The newly proposed quantum image representation uses the basis state of a qubit sequence to store the gray-scale value of each pixel in the image for the ﬁrst time, instead of the probability amplitude of a qubit, as in FRQI.» (p. 1)
- La preparación del estado NEQR requiere $O(q n 2^{2n})$ operaciones elementales con suficientes qubits ancilares, logrando una reducción aproximadamente cuadrática frente a $O(2^{4n})$ de FRQI — «Theorem 2 The whole preparation of NEQR costs no more than O(qn22n) for a 2n × 2n image with gray range 2q. This is equivalent to an approximately quadratic decrease compared to FRQI.» (p. 10)
- La reducción de complejidad en la preparación se confirma frente al límite dominante de FRQI — «Compared with the preparation complexity O(24n) for FRQI, the time complexity of constructing the quantum image for NEQR has experienced an approximately quadratic decrease.» (p. 10)
- La imagen clásica se recupera de manera exacta y determinista mediante mediciones cuánticas de base computacional, superando la recuperación puramente probabilística de FRQI — «Through quantum measurements, the original digital image can be accurately retrieved from the NEQR quantum image, not probabilistically as in FRQI.» (p. 27)
- La razón de compresión alcanzada con minimización de expresiones booleanas promedia 74.11%, lo que representa una mejora de 1.5X frente al 50% de FRQI — «The average compression ratio achieved by NEQR for the six images was approximately 74.11%, which represents a 1.5X improvement over the ratio achieved by FRQI (50%).» (p. 17)
- Permite operaciones complejas sobre el color que FRQI no soporta — «All three kinds of color operation described in Sect. 4.2 can be performed conveniently in the NEQR quantum model. However, FRQI can perform CC operations only.» (p. 27)

## Qué deja como trabajo futuro o limitación declarada
- Requiere $q-1$ qubits adicionales en comparación con FRQI para almacenar la secuencia de escala de grises — «Because NEQR uses a qubit sequence to store gray-scale information, NEQR needs an extra q−1 qubits (2q being the number of gray-scale values in the image) for storage compared to FRQI.» (p. 27)
- Aunque la complejidad temporal se reduce considerablemente frente a FRQI, cuando la imagen es grande la preparación continúa demandando un tiempo inaceptable — «It means when the image size is large, the whole preparation will still take unacceptable time consumption.» (p. 11)
- Plantea como línea abierta investigar si NEQR es adecuado para tareas complejas como el reconocimiento cuántico de patrones y la coincidencia de imágenes — «Whether it is suitable to use NEQR to perform complex image processing such as quantum pattern recognition and quantum image matching will be the topic of future research on quantum image processing.» (p. 27)

## Diseño experimental (solo obras experimentales)
- Los experimentos se realizaron mediante simulación teórica y análisis de circuitos cuánticos en ejemplos constructivos ($2 \times 2$ y $4 \times 4$, y 6 imágenes sintéticas de prueba con distintos niveles de regularidad en escala de grises de 8 bits, $q=8$).
- Métrica central: conteo de compuertas elementales ($C^n$-NOT) antes y después de compresión booleana, y razón de compresión porcentual.
- Comparación clásica: se compara contra la representación FRQI sobre las mismas imágenes, demostrando que en imágenes aleatorias e irregulares FRQI obtiene compresión cercana a cero mientras NEQR mantiene entre 40% y 50%.

## Las cuatro preguntas de H-046 (solo obras que reportan una ventaja o un resultado cuántico frente a clásico)
- No aplica: es una propuesta de representación cuántica de imagen y compresión algorítmica, no un modelo de clasificación supervisada con benchmark frente a clasificadores clásicos estándar.

## Preguntas específicas
- **Complejidad de preparación de NEQR y comparación con FRQI tal como la enuncian:**
  Los autores demuestran que la preparación total cuesta a lo sumo $O(q n 2^{2n})$ para una imagen $2^n \times 2^n$ con rango de grises $2^q$ disponiendo de suficientes qubits ancilares («Theorem 2 The whole preparation of NEQR costs no more than O(qn22n) for a 2n × 2n image with gray range 2q. This is equivalent to an approximately quadratic decrease compared to FRQI.» p. 10). En comparación con la complejidad $O(2^{4n})$ de FRQI, afirman literalmente: «Compared with the preparation complexity O(24n) for FRQI, the time complexity of constructing the quantum image for NEQR has experienced an approximately quadratic decrease.» (p. 10). Cabe notar que, aunque cuadráticamente inferior a FRQI, la complejidad sigue siendo lineal en el número de píxeles ($N = 2^{2n}$), lo que para imágenes de alta resolución resulta exponencial en el número de qubits de posición.
- **Qubits necesarios:**
  Requiere exactamente $q + 2n$ qubits para una imagen de $2^n \times 2^n$ con $2^q$ niveles de gris ($2n$ qubits de posición y $q$ qubits para el valor del píxel) — «NEQR needs q + 2n qubits to represent a 2n × 2n image with gray range 2q.» (p. 6). Esto representa un costo adicional de $q - 1$ qubits respecto a FRQI, que solo utiliza $2n + 1$ qubits — «Because NEQR uses a qubit sequence to store gray-scale information, NEQR needs an extra q−1 qubits (2q being the number of gray-scale values in the image) for storage compared to FRQI.» (p. 27).

## Relevancia para el TT
- Se conecta con §2.1.3 y la justificación metodológica del pipeline propuesto: muestra que incluso con la aceleración cuadrática de NEQR, codificar directamente una mamografía digital completa de resolución estándar (p. ej. $2048 \times 2048$ píxeles, $n=11, q=8$) requeriría $8 + 22 = 30$ qubits lógicos y un orden de $8 \times 11 \times 2^{22} \approx 3.7 \times 10^8$ operaciones de compuerta, lo cual resulta inviable en hardware NISQ. Esto justifica plenamente la estrategia de la tesis: extraer características morfológicas y radiómicas compactas clásicamente y codificar únicamente ese vector reducido en el circuito cuántico.
- **Qué NO se puede afirmar con esta fuente:**
  No se puede afirmar que NEQR resuelva el cuello de botella de carga de imágenes para mamografías de alta resolución, ni que proponga algoritmos de diagnóstico oncológico o kernels cuánticos para clasificación de lesiones.

## Contraste con lo que el proyecto ya le atribuye
- `Other/verificacion/referencias_por_revisar.md:60`: «De memoria: Le et al. (2011) para FRQI y Zhang et al. (2013) para NEQR. No citar sin verificar».
  - *¿Lo sostiene la obra?* Sí. La referencia verificada corresponde exactamente a Zhang, Lu, Gao y Wang (2013), *Quantum Information Processing* 12(8), 2833–2860.
