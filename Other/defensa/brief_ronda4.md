# Ronda 4 · «Defensa TT 2026-B039»: menos texto, más dinámica y respaldos completos

Esta ronda tiene cuatro partes:
- **A.** Una regla general para recortar texto.
- **B.** Cambios en la parte principal, con la diapositiva nueva del proceso general y seis clips de video.
- **C.** La sección de respaldos, que pasa de 10 a unos 45 y se organiza por tipo de pregunta.
- **D.** Cómo insertar los videos.

Las reglas de los briefs anteriores siguen vigentes: paleta, tipografías, «esquema ilustrativo» en los dibujos que no vienen de datos, ninguna cifra distinta de las de este documento, y animaciones que avanzan con la flecha.

---

## A. Regla general: menos texto

- **En pantalla solo van el título (una afirmación), las etiquetas de las gráficas y como mucho una frase de apoyo.** Unas 20 palabras visibles por diapositiva, sin contar los ejes ni las etiquetas de los datos.
- Las explicaciones, las notas al pie largas y los matices **pasan a las notas del orador**. No se pierde nada: se mueve.
- Las notas al pie que deban quedarse (fuente o advertencia) van en **un solo renglón**.
- Donde haya un recuadro con viñetas, conviértelo en **íconos con 2 a 4 palabras cada uno**.

---

## B. Parte principal

### Nuevo orden y tiempos

| # | Diapositiva | Cambio | Tiempo (acumulado) |
|---|---|---|---|
| 1 | Portada | sin cambios | 0:15 (0:15) |
| 2 | Contexto | sin cambios | 0:40 (0:55) |
| 3 | Pregunta | **recortar** | 0:45 (1:40) |
| 4 | **NUEVA · El proceso del trabajo** | clip `mapa_trabajo` | 1:15 (2:55) |
| 5 | El qubit | clip `qubit_bloch` | 1:15 (4:10) |
| 6 | Las dos lecturas | clip `dos_lecturas` | 1:00 (5:10) |
| 7 | Cinco representaciones | miniatura del mapa | 0:45 (5:55) |
| 8 | Concentración | clip `concentracion` | 2:00 (7:55) |
| 9 | Separabilidad | recortar | 1:15 (9:10) |
| 10 | El mismo MLP | miniatura del mapa | 1:00 (10:10) |
| 11 | Árboles (X10) | recortar | 1:15 (11:25) |
| 12 | La pérdida está en la lectura | sin cambios | 1:15 (12:40) |
| 13 | La ventaja sí existe | **recortar mucho** | 1:15 (13:55) |
| 14 | X11, la curva | clip `x11_curva` | 1:30 (15:25) |
| 15 | Viabilidad | clip `disparos` | 1:15 (16:40) |
| 16 | Respuesta | recortar y miniatura del mapa | 1:15 (17:55) |
| 17 | Limitaciones y trabajo futuro | recortar | 0:40 (18:35; quedan ~1:25) |

La antigua diapositiva 6 (el pipeline M1–M8) **sale de la parte principal**: el clip del mapa la sustituye. Su galería de imágenes pasa al respaldo B12.

### 3 · Pregunta (recortar)
- Título: «¿Una codificación cuántica separa mejor lo benigno de lo maligno?».
- En lugar del párrafo de la pregunta, dos íconos grandes:
  - dos nubes de puntos que se separan, con «1 · ¿Cambia la separabilidad?»;
  - una red pequeña, con «2 · ¿Se nota al clasificar?».
- Abajo, igual que hoy: «Objetivo: viabilidad, no superar a una CNN · Simulación ideal (Qiskit Aer)».
- La pregunta completa pasa a las notas del orador y al respaldo B0.

### 4 · NUEVA · «Del mamograma a la comparación: el proceso del trabajo»
- Etiqueta de sección: «02 · Método».
- El clip `mapa_trabajo.mp4` a lo ancho de la diapositiva. Arranca con un clic sobre el video; la imagen fija es su último fotograma.
- Debajo del video, una frase: «Masas y calcificaciones recorren el camino por separado».
- **Notas:** *Tiempo objetivo: 1:15 (acumulado 2:55).* Este es el camino completo del trabajo. Partimos de 3,568 lesiones de 1,566 pacientes del CBIS-DDSM. De cada mamografía recortamos la región de la lesión a su resolución original y le medimos 67 características radiómicas de forma, intensidad y textura. Nos quedamos con 12 y las convertimos en ángulos entre 0 y π, porque un circuito cuántico recibe ángulos de giro. Con ese mismo vector construimos cinco representaciones, tres clásicas y dos cuánticas. Medimos qué tan separables son benigno y maligno en cada una, y entrenamos el mismo clasificador sobre todas. Al final comparamos las dos cosas. Masas y calcificaciones recorren el camino por separado.

### 5 · El qubit
- Sustituye la esfera estática por el clip `qubit_bloch.mp4`, a la izquierda.
- A la derecha se quedan, estáticos, los 12 interruptores con «12 qubits = 2¹² = 4,096 combinaciones» y los engranes «ZZ: cada par gira según sus dos características».
- Quita los textos «Hadamard: al ecuador» y «el giro es la característica»: ya están dentro del clip.
- Notas: las actuales, añadiendo al final: «El video muestra también la diferencia entre C4 y C5: el mismo ángulo, girando en Z se queda en el ecuador y girando en Y sale de él».

### 6 · Las dos lecturas
- Sustituye el diagrama de cajas por el clip `dos_lecturas.mp4`, que usa el estado real de una lesión.
- Se queda una sola frase: «Arquitectura B: θ fijo; los 12 valores se calculan una vez».
- Notas: las actuales, añadiendo: «La tira de arriba es el estado real de una lesión del estudio: sus 4,096 componentes».

### 7 · Cinco representaciones
- Arriba a la derecha, la miniatura `mapa_mini_5.png` (estación 5 resaltada), pequeña.

### 8 · Concentración
- Sustituye los dos mapas de calor estáticos por el clip `concentracion.mp4`, que usa datos reales. Su último fotograma muestra el RBF y el C4 a c = 1, así que el PDF queda igual que hoy.
- Se quedan a la derecha el dibujo del mapa con zoom y la frase final en negritas.
- Quita la nota de C5 debajo del mapa; va a las notas del orador.
- Miniatura `mapa_mini_6.png` arriba a la derecha.
- Notas: las actuales, añadiendo al principio: «En el video, el mapa de la derecha empieza con una escala de ángulos muy pequeña, c = 0.02, y la vamos subiendo hasta c = 1, que es la del diseño. Fíjense cómo se vacía hasta quedar solo la diagonal».

### 9 · Separabilidad
- Quita la frase de abajo («C1–C3 también superan…»); va a las notas.
- Las dos preguntas de apoyo en cursiva se quedan.

### 10 · El mismo MLP
- Miniatura `mapa_mini_6.png` arriba a la derecha.

### 11 · Árboles (X10)
- Quita el pie «AUC-ROC en prueba · punto = estimación…» y deja solo «AUC-ROC en prueba · IC 95 %».
- Quita el subtexto de «0 de 24»; el detalle va a las notas.

### 13 · La ventaja sí existe (recortar mucho)
Es la diapositiva más cargada. Quedan solo tres cosas:
1. **Izquierda arriba, la tarjeta de Huang en dos renglones:** «Huang et al. (2021): con etiquetas diseñadas, el kernel cuántico supera a todos los clásicos». Debajo, pequeño, «*Nature Communications* 12, 2631».
2. **Derecha, la gráfica de barras**, igual que hoy, sin la leyenda larga: basta con «cuántico» y «clásico» bajo cada barra. La nota de C4 sale.
3. **Izquierda abajo, «¿Por qué no se usa siempre?» como tres íconos en fila**, cada uno con 3 o 4 palabras:
   - un ícono de diagnóstico: «las etiquetas no se eligen»;
   - un ícono de candado o círculo: «diseñadas = ventaja asegurada»;
   - una flecha hacia abajo con «0.566 vs 0.677»: «con etiquetas reales, pierde».

**Salen de la diapositiva:** los libros (pasan a la 14), la nota al pie larga, la nota de C4 y el recuadro de viñetas. Todo su contenido se queda en las notas del orador actuales, que no cambian. La frase final en negritas se queda.

### 14 · X11, la curva
- Sustituye la gráfica construida por pasos por el clip `x11_curva.mp4`: las curvas se trazan de α = 0 a 1.
- Se quedan los libros pequeños con «α = cuántas preguntas salen del libro del circuito».
- **La tabla de umbrales α\* pasa al respaldo C10.**
- La nota al pie queda en un renglón: «Etiquetas intermedias artificiales: instrumento de medida, no tarea clínica».

### 15 · Viabilidad
- Sustituye la cuadrícula de 1,024 puntos por el clip `disparos.mp4`, que simula rondas reales de 1,024 disparos.
- Se quedan las barras de qubits a la izquierda y la línea «Los ⟨Zᵢ⟩ sí toleran 1,024 disparos…».

### 16 · Respuesta
- Cada punto en un renglón:
  1. «C4 y C5 separan peor que C1–C3 en todas las métricas».
  2. «Se nota al clasificar: −0.07 a −0.14 de AUC; 0 de 24 a favor».
  3. «Causa: concentración y lectura de 12 números».
  4. «La ventaja existe con etiquetas diseñadas; el diagnóstico está en α = 0».
  5. «Viable en simulación; en hardware, el kernel sería inmedible».
- Miniatura `mapa_mini_7.png` arriba a la derecha.
- Las notas actuales no cambian.

### 17 · Limitaciones y trabajo futuro
- Tres limitaciones y tres líneas de trabajo futuro, de 4 a 8 palabras cada una:
  - **Limitaciones:** «Simulación sin ruido» · «Intensidades no calibradas, sin escala física» · «Separabilidad sobre 200 lesiones».
  - **Trabajo futuro:** «Codificaciones sin concentración» · «Lecturas intermedias: ⟨ZᵢZⱼ⟩» · «Hardware con mitigación de errores».
- Los detalles actuales pasan a las notas del orador.

---

## C. Respaldos: unos 45, ordenados por tipo de pregunta

**R0 · Índice de respaldos.** Una diapositiva con las cinco familias y el número de cada respaldo, para encontrarlo rápido durante las preguntas: A · Básicas, B · Diseño, C · Resultados, D · Fórmulas, E · Preguntas difíciles. Cada respaldo lleva su código (por ejemplo «B2») en la etiqueta de sección y en el pie, como hoy «R4 / R10».

Formato de todos: título como afirmación, un elemento visual, como mucho 20 palabras visibles, y las notas del orador con la respuesta completa. Las cifras y las fórmulas de esta sección están verificadas contra la bitácora y §3 del reporte. **Cópialas tal cual.**

### A · Básicas, para quien no es de cuántica

**A1 · «Un qubit puede estar en una mezcla de 0 y 1»**
- Visual: la esfera de Bloch (puedes reutilizar el último fotograma del clip `qubit_bloch`) y la fórmula $|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\varphi}\sin\frac{\theta}{2}|1\rangle$.
- Notas: un bit vale 0 o 1. Un qubit es un vector de norma 1 en un espacio complejo de dimensión 2, y se dibuja como un punto en la esfera: el polo norte es |0⟩, el sur es |1⟩, y los demás puntos son superposiciones. Al medirlo sale 0 o 1 con probabilidades cos²(θ/2) y sin²(θ/2).

**A2 · «Entrelazar es acoplar los qubits: el todo no se describe por partes»**
- Visual: los engranes de la diapositiva 5 y «12 qubits → 2¹² = 4,096 dimensiones».
- Notas: con entrelazamiento el estado de 12 qubits no se puede escribir como 12 estados de un qubit; hace falta un vector de 4,096 componentes. En el mapa ZZ, cada par de qubits recibe una fase que depende del producto (π − xᵢ)(π − xⱼ), y así el circuito codifica interacciones entre características.

**A3 · «Un *feature map* convierte un vector de números en un estado cuántico»**
- Visual: «x ∈ [0, π]¹² → U(x) → |φ(x)⟩», en tres cajas.
- Notas: es como un cambio de representación. Las 12 características entran como ángulos de giro y salen como un estado de 4,096 dimensiones. En este trabajo, C4 usa `zz_feature_map` y C5 `pauli_feature_map` con los términos Y y ZZ, con una repetición.

**A4 · «Un kernel mide el parecido entre dos lesiones; una SVM separa con ese parecido»**
- Visual: dos huellas que se superponen («k = parecido») y, al lado, una frontera entre puntos azules y naranjas.
- Notas: el kernel de fidelidad mide cuánto se solapan dos estados: 1 si son iguales, 0 si son ortogonales. Una SVM traza la frontera de máximo margen usando solo esos parecidos; con un kernel cuántico se llama QSVM.

**A5 · «Medir un qubit es como hacer una encuesta»**
- Visual: la cuadrícula de 1,024 puntos (último fotograma de `disparos`) y $\operatorname{Var}(\hat Z_i) = \frac{1 - \langle Z_i\rangle^2}{n_{\text{shots}}}$.
- Notas: medir colapsa el estado y da un solo 0 o 1. Para estimar un valor esperado se repite el circuito muchas veces (disparos) y se promedia, igual que una encuesta estima un porcentaje. El error baja con la raíz del número de disparos.

**A6 · «Todo se hizo en simulación exacta, a propósito»**
- Visual: dos columnas, «Simulador: exacto, sin ruido» y «Hardware: ruido y disparos».
- Notas: la pregunta es si la codificación ayuda en condiciones ideales; el ruido del hardware solo la empeoraría. Si no hay ventaja sin ruido, no la habrá con ruido. Además, en hardware el kernel concentrado sería inmedible (diapositiva 15).

**A7 · «AUC-ROC: 0.5 es azar, 1 es perfecto»**
- Visual: una curva ROC esquemática con la diagonal del azar y el área sombreada; $\text{AUC} = \int_0^1 \text{TPR}\, d\,\text{FPR}$.
- Notas: el AUC es la probabilidad de que el modelo ordene a una lesión maligna por encima de una benigna elegidas al azar. No depende de un umbral, por eso es la métrica principal.

**A8 · «67 características radiómicas de forma, intensidad y textura»**
- Visual: cuatro bloques, «forma 2D», «primer orden (intensidad)», «GLCM (textura)» y «GLRLM (textura)», y la lista de las 12 elegidas en masas: Maximum, 90Percentile, Energy, MinorAxisLength, MaximumDiameter, Perimeter, MeshSurface, PerimeterSurfaceRatio, GrayLevelNonUniformity (GLRLM), 10Percentile, Correlation (GLCM) y RunLengthNonUniformity (GLRLM).
- Notas: PyRadiomics, con 32 niveles de gris (`binCount=32`) porque las intensidades no están calibradas, sobre la región recortada a resolución original. Se eligen 12 por prueba F, descartando pares con correlación mayor que 0.95.

### B · Diseño: «¿por qué así?»

**B0 · La pregunta y los objetivos completos**
- La pregunta textual: «¿En qué medida las transformaciones cuánticas variacionales implementadas mediante ZZFeatureMap y PauliFeatureMap en Qiskit modifican la separabilidad de clases benigno/maligno de características radiómicas extraídas de mamografías del CBIS-DDSM, y hasta qué punto esa diferencia se refleja en la capacidad de clasificación de una misma red neuronal clásica, en comparación con representaciones clásicas construidas a partir del mismo vector de características?».

**B1 · «θ se fijó por tres razones: justicia, pregunta y costo»**
- Visual: tres columnas con ícono:
  1. **Justicia:** C2 y C3 no ven las etiquetas; un θ entrenado sí. La comparación dejaría de ser pareja.
  2. **Pregunta:** se mide el efecto de la codificación, no de un modelo entrenado.
  3. **Costo:** entrenar θ por *parameter-shift* costaba 22.4 h a k = 8 y 2,689 h a k = 16, por condición.
- Notas: es la Arquitectura B frente a la A. Con θ fijo, el circuito es una transformación determinista y los valores esperados se calculan una sola vez. Ojo, matiz honesto: en simulación existe un atajo, la retropropagación sobre el vector de estado, que entrena θ en minutos; pero no existe en hardware, porque medir colapsa el estado. Las otras dos razones no dependen del costo y se sostienen. Además, el sorteo de θ se probó: con 10 sorteos (X7) ninguno alcanza a C1, y el déficit va de 0.03 a 0.18 según el sorteo.

**B2 · «¿Y si se entrenaba θ? Como mucho igualaría a lo clásico; en la práctica, ni eso»**
- Visual: una tabla pequeña, AUC en prueba:

  | | θ fijo | θ entrenado | Entrenado − C1 |
  |---|---|---|---|
  | Masas, C4 | 0.530 | 0.533 | −0.118 |
  | Masas, C5 | 0.581 | 0.585 | −0.066 |
  | Calcif., C4 | 0.633 | 0.674 | −0.094 |
  | Calcif., C5 | 0.652 | 0.671 | −0.098 |

  Debajo: «C4 y C5 se calculan a partir de x: no pueden saber más que x».
- Notas: lo medimos en X8: θ se entrenó junto con el MLP. La ganancia fue de 0.00 a 0.04 en el test, sin significancia, y las cuatro combinaciones siguen por debajo de C1, con intervalos que excluyen el cero. Tampoco alcanzan al QSVM, que lee el kernel completo sin ningún θ. Hay además una cota de fondo: C4 y C5 son funciones de las mismas 12 características, así que no pueden contener más información sobre el diagnóstico que ellas (desigualdad de procesamiento de datos). En el mejor caso, con un clasificador lo bastante flexible, entrenar θ podría acercarse a lo clásico, pero no superarlo. θ se movió poco: de 0.13 a 0.39 radianes en promedio.

**B3 · «Las tres arquitecturas del trabajo»**
- Visual, de izquierda a derecha:
  1. el circuito de 12 qubits (la figura `M5_circuit_12q.png` del reporte), con «H · P(2xᵢ) · ZZ · `real_amplitudes` (reps = 1, 24 parámetros)»;
  2. el MLP «12 → 32 → 16 → 1»;
  3. el QSVM: «kernel cuántico → SVM».
- Notas: el MLP usa ReLU, Adam con tasa 10⁻³ y *weight decay* 10⁻⁴, lotes de 128, entropía cruzada binaria ponderada por clase y parada temprana con paciencia 40 sobre el 15 % de los pacientes. El *ansatz* tiene n(r + 1) = 12 × 2 = 24 parámetros, fijos con la semilla 42.

**B4 · «Qué modelos se compararon y dónde»**
- Visual, una tabla:

  | Modelo | Sobre | Dónde |
  |---|---|---|
  | MLP 12-32-16-1 | C1–C5 | M7 (principal), X7, X8, X10 |
  | SVM clásica (lineal, polinomial, RBF) | x | X4, X6, X11 |
  | QSVM (kernel de C4/C5, ZZ lineal, proyectado) | kernel cuántico | X4, X6, X11 |
  | Árbol de decisión, *random forest*, XGBoost | C1–C5 | X10 |
  | Regresión logística | 67 o 12 características, descriptores del radiólogo | X1, M8 |

- Notas: la comparación principal usa un solo clasificador para que la única variable sea la representación. Los demás comprueban que la conclusión no dependa de esa elección: con 6 clasificadores, 0 de 24 comparaciones a favor de lo cuántico.

**B5 · «12 qubits por costo y por diversidad de características; con 8, la conclusión es la misma»**
- Visual: «k = 12» y debajo «k = 8: misma conclusión».
- Notas: k = 12 se fijó por costo de simulación y para incluir características de varias familias. Con k = 8 (X3), la concentración baja y el exceso de alineamiento cuántico crece de 1.7 a 4.6 veces, y *g* sube a 1.7–3.2, todavía muy por debajo de √N, pero los embeddings clásicos siguen delante. En masas, con k = 8 se pierden todas las características de textura.

**B6 · «Una repetición del circuito; con dos, C4 y C5 siguen por debajo»**
- Notas: reps = 1 se fijó por costo. Con reps = 2 en el *ansatz*, C5 mejora un poco sin cerrar la brecha, y la dispersión de C4 no aumenta con el θ del diseño.

**B7 · «Ángulos en [0, π] por cuantiles»**
- Visual: un arco de 0 a π y dos histogramas, «min-max: casi constante» y «cuantiles: uniforme».
- Notas: [0, π] y no [0, 2π] por estabilidad numérica y para evitar redundancias por periodicidad. Cuantiles y no min-max porque con min-max las características de cola pesada quedaban casi constantes en ángulo; con cuantiles todas tienen un rango intercuartílico de π/2. El escalador se ajusta solo con el entrenamiento.

**B8 · «Por qué ZZ y Pauli(Y, ZZ)»** (el R3 actual, ampliado)
- Agrega debajo de las esferas: «(Z, ZZ) es el mismo circuito que ZZ · (X, ZZ) no codifica nada con una repetición».
- Notas: la primera elección, Pauli con Z y ZZ, resultó ser el mismo circuito que `zz_feature_map`, con fidelidad 1.000000000000. La segunda, X y ZZ, tampoco servía: tras Hadamard cada qubit está en |+⟩, que es autoestado de X, así que el término X solo añade una fase global. Con Y, el giro saca al qubit del ecuador, y C4 contra C5 compara el eje de la codificación con el mismo acoplamiento ZZ.

**B9 · «C2 es un control nulo: rotar no cambia la información»**
- Visual: la foto girada de la diapositiva 7.
- Notas: el PCA de 12 a 12 dimensiones es una rotación, que conserva distancias. Por eso las métricas de separabilidad deben dar lo mismo para C1 y C2: si no, estarían mal implementadas. En clasificación, C2 − C1 no es significativo con ningún clasificador.

**B10 · «Separabilidad sobre 200 lesiones: el tamaño repetible en hardware»**
- Visual: «200 lesiones → 19,900 circuitos por matriz · todo el entrenamiento → 0.87–1.19 millones».
- Notas: en simulación el entrenamiento completo cuesta unos 20 s por kernel, así que no es por costo de cómputo; es por el costo del protocolo físico. Se comprobó con 20 submuestras y con todo el entrenamiento (X9): el RBF va delante en el 100 % de las submuestras.

**B11 · ¿Por qué 5 folds?** (el R8 actual, sin cambios)

**B12 · Preprocesamiento** (el R2 actual, más la galería de la antigua diapositiva 6)

**B13 · Sin fuga de información** (el R6 actual, sin cambios)

### C · Resultados y robustez

**C1 · «Todas las métricas de clasificación, en prueba»**
- Visual, una tabla. Masas y calcificaciones; AUC, F1, exactitud, precisión y sensibilidad (recall):

  | | AUC | F1 | Exactitud | Precisión | Sensibilidad |
  |---|---|---|---|---|---|
  | Masas C1 | 0.651 | 0.519 | 0.638 | 0.536 | 0.503 |
  | Masas C2 | 0.641 | 0.512 | 0.616 | 0.507 | 0.517 |
  | Masas C3 | 0.646 | 0.502 | 0.606 | 0.493 | 0.510 |
  | Masas C4 | 0.530 | 0.386 | 0.529 | 0.392 | 0.381 |
  | Masas C5 | 0.581 | 0.456 | 0.571 | 0.450 | 0.463 |
  | Calcif. C1 | 0.769 | 0.665 | 0.666 | 0.551 | 0.837 |
  | Calcif. C2 | 0.788 | 0.669 | 0.693 | 0.584 | 0.783 |
  | Calcif. C3 | 0.758 | 0.652 | 0.653 | 0.541 | 0.822 |
  | Calcif. C4 | 0.633 | 0.504 | 0.607 | 0.504 | 0.504 |
  | Calcif. C5 | 0.652 | 0.565 | 0.571 | 0.472 | 0.705 |

- Pie: «MLP del M7, umbral 0.5 · fuente: 8_tabla_clasificacion.csv».

**C2 · «t-SNE: ninguna representación separa visualmente las clases»**
- La figura `Docs/Figures/M6_tsne.png` del reporte, sin texto adicional.
- Notas: el t-SNE es solo cualitativo. Las métricas cuantitativas son las de la diapositiva 9.

**C3 · «Un QSVM sobre el kernel de C4 iguala al SVM clásico»**
- Visual, una tabla, AUC en prueba:

  | | Masas | Calcificaciones |
  |---|---|---|
  | SVM RBF | 0.649 | 0.769 |
  | QSVM C4 | 0.628 | 0.759 |
  | QSVM C5 | 0.599 | 0.701 |
  | MLP sobre ⟨Zᵢ⟩ de C4 | 0.530 | 0.633 |

- Notas: QSVM C4 − SVM RBF: −0.02 y −0.01, sin diferencia significativa. QSVM C4 − MLP: +0.10 y +0.13. La codificación conserva la información; la lectura de 12 números la pierde.

**C4 · «Buscando ventaja con la misma búsqueda en los dos lados: ninguna»** (X6)
- Notas: con búsqueda anidada simétrica, ningún kernel cuántico supera a los clásicos en las etiquetas reales. El entrelazamiento lineal aumenta la concentración, al contrario de la hipótesis. Los kernels proyectados suben *g* a 6–9, pero son los peores con las etiquetas reales.

**C5 · Robustez** (el R5 actual, sin cambios)

**C6 · Separabilidad frente a clasificación** (el R7 actual, sin cambios)

**C7 · El barrido de c** (el R9 actual, sin cambios)

**C8 · Masas frente a calcificaciones** (el R1 actual, sin cambios)

**C9 · Métricas de separabilidad** (el R10 actual, sin cambios)

**C10 · «Umbral α\* de cada kernel»**
- La tabla de umbrales que sale de la diapositiva 14: ZZ completo (C4) 0.6 / 0.7; ZZ lineal 0.5 / 0.6; proyectado 0.4 / 0.5 (masas / calcificaciones), con «el diagnóstico real está en α = 0».

### D · Fórmulas del marco teórico

Escríbelas como fórmulas, con el mismo estilo de R4. Cada respaldo lleva solo las fórmulas y una etiqueta corta por símbolo; la explicación va en las notas.

**D1 · «La codificación»**
- $|\phi(\mathbf{x})\rangle = U(\mathbf{x})\,|0\rangle^{\otimes n}$
- $U_{\text{ZZ}}(\mathbf{x}) = \left[\mathcal{U}_\Phi(\mathbf{x})\,H^{\otimes n}\right]^r$, con $\mathcal{U}_\Phi(\mathbf{x}) = \exp\!\left(-i \sum_{|S|\leq 2} \phi_S(\mathbf{x}) \bigotimes_{j \in S} Z_j\right)$
- $\phi_{\{i\}}(\mathbf{x}) = x_i, \qquad \phi_{\{i,j\}}(\mathbf{x}) = (\pi - x_i)(\pi - x_j)$
- Notas: n = 12 qubits, r = 1. El término de un qubit codifica cada característica y el de pares codifica su producto: es el entrelazamiento.

**D2 · «Las dos lecturas»**
- Kernel: $K_Q(\mathbf{x}, \mathbf{x}') = \left|\langle\phi(\mathbf{x})|\phi(\mathbf{x}')\rangle\right|^2$
- Valores esperados: $\langle Z_i \rangle = \langle \psi(\mathbf{x}, \boldsymbol{\theta}) | Z_i | \psi(\mathbf{x}, \boldsymbol{\theta}) \rangle \in [-1, 1]$, con $|\psi(\mathbf{x},\boldsymbol\theta)\rangle = W(\boldsymbol\theta)\,U(\mathbf{x})\,|0\rangle^{\otimes n}$
- Parámetros del *ansatz*: $m = n\,(r+1) = 24$
- Notas: en el kernel el *ansatz* se cancela, porque un unitario conserva los productos internos: $W^\dagger W = I$. Por eso las métricas de kernel no dependen de θ y los valores esperados sí.

**D3 · «Separabilidad»**
- $\widehat{\text{KTA}}_c(K, \mathbf{y}) = \dfrac{\langle K_c, (\mathbf{y}\mathbf{y}^\top)_c \rangle_F}{\|K_c\|_F\,\|(\mathbf{y}\mathbf{y}^\top)_c\|_F}$, con piso $\widehat{\text{KTA}}_c(I, \mathbf{y}) = \dfrac{1}{\sqrt{N-1}}$ y exceso $\Delta\text{KTA}_c = \widehat{\text{KTA}}_c(K,\mathbf{y}) - \mathbb{E}_\pi[\widehat{\text{KTA}}_c(K,\mathbf{y}_\pi)]$
- Fisher: $J = \Delta\boldsymbol{\mu}^\top S_W^{-1} \Delta\boldsymbol{\mu}$
- Davies-Bouldin: $\text{DB} = \frac{1}{C}\sum_{i} \max_{j \neq i} \frac{s_i + s_j}{d(c_i, c_j)}$
- Notas: la KTA cruda no es comparable entre kernels, porque la identidad ya da 1/√(N − 1) con cualquier etiquetado; por eso se reporta el exceso sobre etiquetas permutadas. J es invariante ante transformaciones afines, y por eso C1 y C2 coinciden.

**D4 · «La diferencia geométrica»** (el R4 actual, ampliado)
- Sin regularizar: $g_{CQ} = \sqrt{\left\| \sqrt{K_Q}\,K_C^{-1}\,\sqrt{K_Q} \right\|_\infty}$
- Regularizada: la fórmula actual de R4, con la condición $g_{\text{tra}}(K_C, K_Q; \lambda) = \lambda\sqrt{\| \sqrt{K_Q}(K_C + \lambda I)^{-2}\sqrt{K_Q}\|_\infty} < 0.045$
- Cota: $s_C \le g^2\, s_Q$ (Huang et al., 2021, p. 5)
- Dimensión efectiva: $d(K) = \sum_{k=1}^{N} \frac{1}{N-k+1}\sum_{l=k}^{N} t_l$, con $1 \le d \le N$
- Notas: s es la complejidad del modelo que aprende las etiquetas. Si g es pequeña, lo que aprende el kernel cuántico lo aprende el clásico con datos comparables. Solo hay ventaja potencial si g se acerca a √N; aquí g = 1.40–1.70 frente a √N ≈ 14.1, y d = 168–188 de 200.

**D5 · «Medición y gradiente»**
- Ruido de un valor esperado: $\operatorname{Var}(\hat{Z}_i) = \dfrac{1 - \langle Z_i \rangle^2}{n_{\text{shots}}}$
- Ruido de un valor del kernel: $\dfrac{K_Q(1 - K_Q)}{n_{\text{shots}}}$; probabilidad de leer exactamente 0: $(1 - K_Q)^{n_{\text{shots}}}$
- *Parameter-shift*: $\dfrac{\partial \langle Z_i \rangle}{\partial \theta_j} = \dfrac{1}{2}\left[ \langle Z_i \rangle_{\theta_j + \frac{\pi}{2}} - \langle Z_i \rangle_{\theta_j - \frac{\pi}{2}} \right]$
- Notas: con K_Q ≈ 0.002 y 1,024 disparos, la probabilidad de leer 0 es de alrededor del 11 %. Medido sobre todos los pares, entre el 16 y el 74 % de los valores se leerían 0. El *parameter-shift* da el gradiente exacto con dos circuitos por parámetro, y por eso funciona en hardware; pero son 2 × 24 evaluaciones por lesión.

**D6 · «Clasificación»**
- Pérdida ponderada: $\mathcal{L}_w = -\left[ w_1\,y\log\hat{y} + w_0\,(1-y)\log(1-\hat{y}) \right]$, con $w_c = \frac{N}{C \cdot N_c}$
- $\text{AUC} = \int_0^1 \text{TPR}(t)\,d\,\text{FPR}(t)$
- Spearman con empates: $\rho_s = \dfrac{\sum (R_i - \bar{R})(S_i - \bar{S})}{\sqrt{\sum (R_i - \bar{R})^2 \sum (S_i - \bar{S})^2}}$
- Notas: los pesos compensan el desbalance (1.16:1 en masas y 1.78:1 en calcificaciones). ρ_s es Pearson sobre rangos promedio, válido con empates.

**D7 · «Los kernels clásicos de referencia»**
- RBF: $k(\mathbf{x}, \mathbf{x}') = \exp(-\gamma \|\mathbf{x} - \mathbf{x}'\|^2)$, con $\gamma = \dfrac{1}{2\,\operatorname{med}_{i<j}\|\mathbf{x}_i - \mathbf{x}_j\|^2}$
- PCA conserva distancias: $\|\mathbf{z} - \mathbf{z}'\| = \|\mathbf{x} - \mathbf{x}'\|$
- Kernel proyectado: $k^{\mathrm{PQ}}(\mathbf{x}, \mathbf{x}') = \exp\!\left(-\gamma \sum_{k} \|\rho_k(\mathbf{x}) - \rho_k(\mathbf{x}')\|_F^2\right)$
- Notas: el RBF es el kernel clásico de C3 y de la comparación. El proyectado compara qubit por qubit en lugar del estado completo; es el que gana con las etiquetas diseñadas.

### E · Preguntas difíciles

**E1 · «¿Un resultado negativo vale? Sí: el método detecta la ventaja cuando existe»**
- Visual: «Objetivo: viabilidad» y una flecha a la diapositiva 13: «control positivo: 0.998 vs 0.857».
- Notas: el objetivo registrado es evaluar viabilidad, no superar a lo clásico. Un resultado negativo es informativo si el método podía detectar uno positivo, y lo podía: con etiquetas diseñadas la ventaja aparece. La conclusión resiste θ, k, reps, semillas, clasificadores, tamaño de muestra y número de folds, y una auditoría independiente pasó 25 de 25 verificaciones.

**E2 · «¿Por qué no una CNN?»**
- Visual: «mamografía ~5,037 × 2,960 px → circuito de 12 qubits», tachado, y «→ 67 características → 12 ángulos».
- Notas: un circuito de 12 qubits recibe 12 números, no una imagen. Las características radiómicas son interpretables y miden el tamaño a escala original; redimensionar a 224 × 224, como pide una CNN, destruye las medidas de tamaño, que están entre las más discriminativas. La pregunta es sobre la codificación, no sobre ganarle a una CNN.

**E3 · «¿Las intensidades no calibradas meten el efecto del digitalizador?»**
- Notas: es una limitación declarada. En masas, las características que más separan son de intensidad (la mayor diferencia estandarizada es 0.50, de `firstorder_Maximum`), y el árbol legible de X10 decide con ellas. Pero las cinco condiciones reciben el mismo vector, así que el sesgo, si existe, las afecta a todas por igual y no cambia la comparación.

**E4 · «¿Cuánto se pierde al quedarse con 12 de 67?»**
- Visual: «67 → 12: de 2 a 4 puntos de AUC».
- Notas: en X1, la pérdida con clasificadores clásicos es de 0.015 a 0.042 de AUC, más o menos una desviación entre folds. Las 12 conservan el 86.8 % (masas) y el 90.2 % (calcificaciones) de la varianza de las 67. Como las cinco condiciones reciben las mismas 12, la pérdida no favorece a ninguna. Y con las 67 tampoco hay ventaja cuántica (X4).

**E5 · «¿El resultado se generaliza?»**
- Notas: es un solo conjunto de datos, el CBIS-DDSM, sin escala física (falta el PixelSpacing en el 100 % de los DICOM). La conclusión es sobre estas etiquetas, estas características y estas familias de kernels: mapas ZZ con entrelazamiento completo o lineal, una o dos repeticiones, y sus kernels proyectados. Probar otros conjuntos de datos y otras codificaciones es trabajo futuro.

**E6 · «¿Cuándo valdría la pena el hardware?»**
- Visual: tres condiciones con palomitas: «etiquetas que siguen la geometría del circuito» · «un kernel que no se concentre» · «una codificación difícil de simular».
- Notas: las tres a la vez. Con estas lesiones, la primera falla: el diagnóstico está en α = 0. Y a c = 1 el kernel sería inmedible con 1,024 disparos.

---

## D. Los videos

Te adjunto seis MP4 (H.264, menos de 20 MB cada uno):
- `mapa_trabajo.mp4` → diapositiva 4
- `qubit_bloch.mp4` → diapositiva 5
- `dos_lecturas.mp4` → diapositiva 6
- `concentracion.mp4` → diapositiva 8
- `x11_curva.mp4` → diapositiva 14
- `disparos.mp4` → diapositiva 15

Para cada uno:
- **Que arranque con un clic** sobre el video, **sin sonido** y, si se puede, **sin bucle**: que se reproduzca una vez y se quede en su último fotograma.
- **Imagen fija: el último fotograma del video**, no el primero, porque resume el clip y es la que sale en el PDF.

Además te adjunto tres imágenes PNG con fondo transparente, `mapa_mini_5.png`, `mapa_mini_6.png` y `mapa_mini_7.png` (de 1600 × 220 px), para las miniaturas «usted está aquí» de las diapositivas 7, 8, 10 y 16. Van arriba a la derecha y pequeñas, de unos 360 px de ancho.

## Comprobación final antes de exportar
- [ ] 17 diapositivas principales; R0 y unos 45 respaldos con su código (A1…E6) y contadores correctos.
- [ ] Ninguna diapositiva principal con más de unas 20 palabras visibles, además de las etiquetas de las gráficas.
- [ ] La 13 solo tiene la tarjeta de dos renglones, las barras, los tres íconos y la frase final.
- [ ] Los seis videos arrancan con un clic y su imagen fija es el último fotograma.
- [ ] Las cifras y las fórmulas de los respaldos son exactamente las de este documento.
- [ ] Tiempos de las notas según la tabla de la sección B.
