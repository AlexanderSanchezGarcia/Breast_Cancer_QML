# Guion de la presentación · TT 2026-B039

Presentación: martes 24 de noviembre de 2026, 16:00. Duración objetivo: **unos 19 minutos** de exposición, con margen dentro de los 20. Con todo el texto son 19:35; sin las frases ✂, unos 18:55.

## Cómo leer este guion

- El texto en bloque (`>`) es lo que se dice, en primera persona. No hay que memorizarlo palabra por palabra: lo importante son las cifras en **negritas** y el orden de las ideas.
- **[CLIC]** = flecha → (o espacio, o el control remoto). Cada uno revela el siguiente elemento de la diapositiva; el guion lo pone en el momento en que conviene decir lo que aparece.
- **[▶ VIDEO]** = en las diapositivas con video, la primera flecha → reproduce el video; la siguiente avanza.
- ✂ marca una frase que se puede omitir si se va tarde.
- ① y ② son las dos partes de la pregunta; aparecen como insignias en las diapositivas de resultados.
- Cada diapositiva tiene su tiempo y el acumulado, medidos sobre este texto a unas 130 palabras por minuto (total 19:35; sin las frases ✂, unos 18:55). Los **puntos de control** sirven para saber, durante el ensayo, si se va bien de tiempo. Si en el ensayo hablas más rápido o más lento, ajusta con las frases ✂, no acelerando.

## Antes de empezar

- Abrir `Other/defensa/Defensa TT 2026-B039.html` en Chrome y poner pantalla completa con la tecla **f**. Funciona sin internet: videos, figuras y fuentes van incrustados.
- Probar en esa misma computadora, con el proyector, al menos: un video, un número + Enter (por ejemplo **46** + Enter) y la tecla **I**.
- Tener a la mano el PDF (`Defensa TT 2026-B039.pdf`) por si falla el navegador. En el PDF no hay videos: se ve su último fotograma, que resume cada clip.
- Llevar impresa la tarjeta de preguntas del final de este guion.

---

## 01 · Contexto y pregunta

### 1 · Portada · 0:20 (0:20)

> Buenas tardes. Soy Miguel Alexander Sánchez García y presento el Trabajo Terminal 2026-B039, dirigido por el doctor Jesús Yaljá Montiel Pérez y la doctora Ana María Winfield Reyes. En los próximos minutos les mostraré qué pasa cuando se codifican características de mamografías en un circuito cuántico.

### 2 · Detectar a tiempo cambia la supervivencia · 0:55 (1:15)

> **[CLIC]** El cáncer de mama sumó **2.3 millones** de casos nuevos en el mundo en 2022, y en México causó **8,451** defunciones en 2024.
>
> **[CLIC]** Lo que más pesa es cuándo se detecta. Si sigue dentro de la mama, la supervivencia a cinco años supera el **99 %**; si ya llegó a ganglios cercanos, baja a **87 %**; con metástasis, a **33 %**.
>
> **[CLIC]** La herramienta de la detección temprana es la mamografía: con tamizaje regular, la mortalidad puede bajar hasta un 40 %. Pero su lectura varía entre radiólogos, y por eso se desarrollan apoyos computacionales; el aprendizaje automático clásico ya clasifica lesiones. Este trabajo no supone que lo cuántico sea mejor: pregunta si una codificación cuántica representa las lesiones de forma más separable, y lo mide.

### 3 · Estado del arte · 1:00 (2:15)

> ¿Qué se había hecho?
>
> **[CLIC]** El aprendizaje profundo ya clasifica mamografías con AUC alrededor de 0.9, pero sin circuitos cuánticos.
>
> **[CLIC]** Los trabajos cuánticos usan datos tabulares o imágenes sencillas, no mamografías.
>
> **[CLIC]** El único que aplica aprendizaje cuántico a la mamografía, Azevedo et al., no analiza la separabilidad ni separa masas y calcificaciones.
>
> **[CLIC]** Ninguno combina las cuatro cosas: un circuito de codificación, el CBIS-DDSM, un análisis explícito de la separabilidad y masas y calcificaciones por separado.
>
> **[CLIC]** Y es justo lo que Azevedo y sus coautores dejaron como trabajo futuro: separar masas y calcificaciones, probar otros conjuntos de datos, ver cómo quedan los datos en el espacio de Hilbert y probar otras codificaciones. Este trabajo parte de ahí. ✂ Los desempeños de la tabla no son comparables entre sí: la tabla ubica el trabajo, no lo compite.

### 4 · La pregunta de investigación · 0:45 (3:00)

> **[CLIC]** Esta es la pregunta de investigación. *(Pausa de dos o tres segundos para que la lean.)* Tiene dos partes. La uno: si la transformación cuántica cambia qué tan separables son las lesiones benignas y malignas. La dos: si ese cambio se nota cuando una misma red neuronal clasifica sobre cada representación.
>
> **[CLIC]** Voy a marcar estas dos partes con estos números durante los resultados. Todo parte del mismo vector de características, para que la única diferencia sea la transformación. Y una aclaración: el objetivo es evaluar viabilidad, no superar a una red convolucional, y todo se hizo en simulación ideal.

**Punto de control: 3:00.**

---

## 02 · Método e idea

### 5 · El proceso del trabajo · 0:50 (3:50)

> **[▶ VIDEO]** Este es el camino completo. Partimos de **3,568 lesiones** de **1,566 pacientes** del CBIS-DDSM. De cada mamografía recortamos la región de la lesión a su resolución original y le medimos **67 características radiómicas** de forma, intensidad y textura. Nos quedamos con **12** y las convertimos en ángulos entre 0 y π, porque un circuito cuántico recibe ángulos de giro. Con ese mismo vector construimos cinco representaciones, tres clásicas y dos cuánticas. En cada una medimos qué tan separables son benigno y maligno, y entrenamos el mismo clasificador. Al final comparamos las dos cosas. Masas y calcificaciones recorren todo el camino por separado, como dos problemas independientes.

### 6 · Cinco representaciones · 0:50 (4:40)

> Estas son las cinco representaciones del mismo vector. En azul, las clásicas. C1 es el vector sin transformar: la referencia. C2 es PCA lineal, que solo gira los datos.
>
> **[CLIC]** Es como girar una foto: lo que hay en ella no cambia. Por eso C2 es un control nulo; si una métrica premiara a C2 sobre C1, la métrica estaría mal. C3 es Kernel PCA con RBF, no lineal y clásico. En naranja y verde, las cuánticas: C4 con ZZFeatureMap y C5 con PauliFeatureMap, ambas seguidas del mismo ansatz fijo. Mismo MLP, mismos hiperparámetros, misma semilla: la única variable es la transformación. Este código de color se mantiene en todas las gráficas.

### 7 · Un qubit es una flecha en una esfera · 1:10 (5:50)

> **[▶ VIDEO]** ¿Qué es un qubit? Se puede imaginar como una flecha dentro de un globo: arriba es 0, abajo es 1, y en medio hay infinitos estados. Hadamard lleva la flecha al ecuador, y luego la giramos un ángulo que depende de una característica de la lesión. Ahí está la diferencia entre C4 y C5: con el mismo ángulo, girando en Z la flecha se queda en el ecuador; girando en Y, sale de él.
>
> Con 12 qubits hay 2 a la 12, es decir **4,096** combinaciones de ceros y unos, y el estado le asigna a cada una una amplitud, que tiene tamaño y fase. El bloque ZZ acopla los qubits por pares, como engranes: el giro de cada par depende de dos características a la vez. Ese acoplamiento es el entrelazamiento, y por eso ya no basta una flecha por qubit: hay que usar las 4,096 dimensiones.

### 8 · Dos formas de leer el estado · 0:50 (6:40)

> **[▶ VIDEO]** Esta es la idea central. La tira es el estado real de una lesión del estudio: sus 4,096 componentes tienen todas la misma probabilidad; la información está en las fases. Ese estado se puede leer de dos formas. Una: comparar los estados completos de dos lesiones. Eso es el kernel; en este par da **0.0035**. Dos: resumir cada estado en 12 números, los valores esperados después del ansatz, y dárselos al perceptrón. Comparar estados es como comparar dos huellas dactilares completas; los 12 valores, como describir una película con 12 fotogramas. En la Arquitectura B, θ no se entrena: los 12 valores se calculan una sola vez.

**Punto de control: 6:40.**

---

## 03 · Resultados

### 9 · ① El kernel cuántico ve casi todos los pares como ortogonales · 1:20 (8:00)

> **[▶ VIDEO]** Primera parte de la pregunta: la separabilidad. Cada celda dice qué tan parecidas son dos lesiones; las primeras 20 son benignas y las siguientes 20, malignas. A la izquierda, el kernel clásico: hay toda una gama de parecidos. A la derecha, el cuántico: empieza con una escala de ángulos muy pequeña, c = 0.02, y la subimos hasta c = 1, la del diseño. Fíjense cómo se vacía hasta quedar solo la diagonal: cada lesión se parece a sí misma y a casi nadie más. La mediana fuera de la diagonal es **0.0022**, contra **0.60** del RBF.
>
> **[CLIC]** Es como un mapa con tanto zoom que cada casa llena la pantalla: ya no se distinguen las colonias.
>
> **[CLIC]** Si todas las lesiones están igual de lejos, el parecido no distingue benignas de malignas. Esto se llama concentración del kernel. Huang et al. describen justo este caso, en el que todas las entradas quedan demasiado lejos, como el típico de los modelos cuánticos que no superan a los clásicos. ✂ C5 está todavía más concentrado.

### 10 · ① Los kernels cuánticos no separan mejor · 1:00 (9:00)

> ¿Cuánto de la estructura de cada kernel se explica por benigno contra maligno? Eso mide el alineamiento, ya descontado el que darían etiquetas al azar. El RBF clásico llega a **0.049** en masas y **0.151** en calcificaciones; C4 y C5 quedan entre **0.003 y 0.007**: prácticamente cero.
>
> **[CLIC]** La segunda métrica es la diferencia geométrica g de Huang et al.: pregunta si el mapa cuántico tiene caminos que el clásico no puede trazar. Solo habría ventaja potencial si g se acercara a la raíz de N, unos **14** aquí. Observamos g entre **1.40 y 1.70**: casi un orden de magnitud por debajo. Ningún kernel cuántico separa mejor que el clásico, y eso se mantiene en 20 submuestras y en todo el entrenamiento.

### 11 · ① Las representaciones tampoco separan mejor · 0:45 (9:45)

> La diapositiva anterior medía los kernels; esta mide los vectores que de verdad recibe el clasificador.
>
> **[CLIC]** En Davies-Bouldin, menor es mejor: en masas, C1 da **4.30**, C4 **5.90** y C5 **13.35**, que no se distingue de etiquetas al azar. En Fisher, mayor es mejor: C3 es el más alto en los dos subconjuntos y C4 el más bajo. En alineamiento lineal, C1 llega a 0.070 y 0.181, y las cuánticas quedan por debajo. ✂ Y fíjense: C1 y C2 dan exactamente lo mismo, que es lo que debe pasar con el control nulo.

### 12 · ① t-SNE · 0:25 (10:10)

> Esto es solo una ayuda visual, no una métrica: el t-SNE aplana cada representación a dos dimensiones. En C1 las malignas, los círculos morados, tienden a agruparse hacia un extremo; en C5 quedan mezcladas. C2 se ve como C1 girada o reflejada, porque el PCA solo gira los datos.

**Punto de control: 10:10.**

### 13 · ② Cómo se lee una curva ROC · 0:50 (11:00)

> Segunda parte de la pregunta: ¿se nota al clasificar? Primero, cómo se lee una curva ROC.
>
> **[▶ VIDEO]** El MLP le da a cada lesión una probabilidad de ser maligna. Un umbral decide: a la derecha, se predice maligno. Al bajarlo detectamos más malignas, pero también marcamos más benignas. Cada umbral es un punto, y todos juntos forman la curva. El área bajo ella, el AUC, es la probabilidad de que una maligna al azar reciba una puntuación mayor que una benigna al azar: 1 es perfecto y 0.5 es el azar. Con C1, **0.651**; con C4 las clases se enciman y la curva se pega a la diagonal: **0.530**.

### 14 · ② El mismo MLP clasifica peor sobre los embeddings cuánticos · 0:40 (11:40)

> Ahora las cinco condiciones, en los dos subconjuntos.
>
> **[CLIC]** Primero las clásicas: C1, C2 y C3 casi se superponen; alrededor de 0.65 en masas y entre 0.76 y 0.79 en calcificaciones.
>
> **[CLIC]** Ahora las cuánticas. C4 y C5 quedan por debajo en los dos subconjuntos: de **0.07 a 0.14** de AUC menos que C1. En masas, C4 va casi sobre la diagonal. Las cuatro diferencias contra C1 son significativas; la de C2 contra C1 no lo es, como debe ser en un control nulo.

### 15 · ② Con árboles, bosques y boosting, tampoco · 0:45 (12:25)

> ¿Y si el problema fuera la red neuronal? Probamos cinco clasificadores de árboles sobre las mismas cinco representaciones, con hiperparámetros elegidos por validación cruzada anidada.
>
> **[CLIC]** En masas, los ensambles leen mejor los valores esperados…
>
> **[CLIC]** …pero no alcanzan a C1.
>
> **[CLIC]** En total, **0 de 24** comparaciones a favor de C4 o C5.
>
> **[CLIC]** Hay una razón de fondo: C4 y C5 se calculan a partir de x, como una fotocopia se saca de un original, y una fotocopia no puede tener más información que el original. ✂ Un clasificador sí puede aprovechar mejor una forma que otra con datos finitos; por eso había que medirlo.

### 16 · ② La pérdida está en la lectura, no en la codificación · 1:00 (13:25)

> Entonces, ¿dónde se pierde la información? Comparamos las dos lecturas del mismo estado: una SVM sobre el kernel completo, el círculo relleno, y el MLP sobre los 12 valores esperados, el cuadro hueco.
>
> **[CLIC]** En C4, pasar del MLP a la SVM cuántica recupera **0.10** de AUC en masas y **0.13** en calcificaciones, y la deja prácticamente al nivel de la SVM clásica, la línea punteada. En C5 la recuperación es menor.
>
> **[CLIC]** Leído a través de su kernel, el estado cuántico iguala al clásico; resumido en 12 números, pierde información. Es la película completa contra 12 fotogramas. El cuello de botella está en la lectura, no en la codificación. Aclaro que este análisis es exploratorio, posterior al diseño, y no sustituye la comparación principal.

### 17 · ① ② Resumen · 0:40 (14:05)

> Esta tabla junta las dos partes de la pregunta.
>
> **[CLIC]** En separabilidad, la mejor columna siempre la gana una condición clásica. La única celda que podría parecer cuántica, Fisher de C5 en masas, **0.668**, está empatada con C1, **0.669**. Al clasificar con el mismo MLP, C4 y C5 quedan por debajo.
>
> **[CLIC]** Y el QSVM, que usa el kernel completo, empata con la SVM clásica: **0.628** contra **0.649** en masas, y **0.759** contra **0.769** en calcificaciones. La información está en el estado; se pierde al leer 12 números.

**Punto de control: 14:05.**

### 18 · La ventaja cuántica sí existe · 1:15 (15:20)

> Que aquí no haya ventaja no significa que la ventaja cuántica no exista. Huang et al. mostraron cómo construirla: diseñaron etiquetas que siguen la geometría del circuito. Es como un examen redactado con el libro que estudió el circuito.
>
> **[CLIC]** Repetimos esa construcción con nuestras mismas lesiones y características, y la ventaja aparece: **0.998** contra **0.857** en masas…
>
> **[CLIC]** …y **0.994** contra **0.876** en calcificaciones, aun dejando que el lado clásico elija entre 16 modelos. El método sí detecta una ventaja cuando existe.
>
> **[CLIC]** ¿Por qué no se usa siempre? Porque en un problema real las etiquetas no se eligen: las define el diagnóstico. Las diseñadas se construyen con el propio kernel, así que la ventaja está asegurada de antemano. ✂ Y ese mismo kernel, con las etiquetas reales, pierde: 0.566 contra 0.677 en masas.
>
> **[CLIC]** La pregunta deja de ser si la ventaja existe y pasa a ser si el diagnóstico es una de esas tareas.

### 19 · La ventaja aparece cuando la tarea sigue la geometría del circuito · 1:00 (16:20)

> **[▶ VIDEO]** Para responderlo, mezclamos las dos tareas: α es la fracción de lesiones que toma la etiqueta diseñada; el resto conserva su diagnóstico real. Con α = 0, el diagnóstico real, el clásico va delante. La ventaja cuántica aparece a partir de **α = 0.4** con el kernel proyectado, y entre 0.5 y 0.7 con los demás, y llega a **+0.14** de AUC con la tarea diseñada, incluso contra XGBoost. Dos lecturas: el protocolo sí detecta la ventaja cuando existe, y el diagnóstico benigno o maligno, con estas características, está en el extremo opuesto. ✂ El kernel con la g más grande cruza antes y gana más, que es lo que predice la teoría. Las etiquetas intermedias son artificiales: son un instrumento de medida, no una tarea clínica.

---

## 04 · Viabilidad · 05 · Conclusiones · 06 · Cierre

### 20 · Simular 12 qubits fue barato; entrenar θ, no · 0:55 (17:15)

> **[CLIC]** ¿Cuánto costó simular? Con 12 qubits, poco; todo se ejecutó en esta laptop. La transformación clásica tarda **0.2 segundos**; el kernel de 200 lesiones, **1.5 segundos** con el atajo de la simulación, y el embedding cuántico de todas las lesiones, unos **14 segundos**. El eje es logarítmico.
>
> **[CLIC]** Calcular el kernel como en un procesador real, un circuito por par, llevaría **46 minutos**.
>
> **[CLIC]** Y entrenar θ por parameter-shift costaría unas **191 horas** por mapa: ocho días. Por eso θ quedó fijo: la Arquitectura B es unas **1,900 veces** más barata.
>
> **[CLIC]** ✂ Además, cada qubit extra casi duplica el costo: un estado tarda 2.9 milisegundos con 12 qubits y 75 segundos con 28.

### 21 · Medir en hardware sería el problema · 0:50 (18:05)

> Una matriz de 200 lesiones son **19,900 circuitos**, y cada valor se estima como una encuesta: se repite el circuito 1,024 veces y se cuenta cuántas veces salen todos los qubits en cero. Son unos **20 millones** de ejecuciones.
>
> **[▶ VIDEO]** Si el valor real es 0.002, se esperan unas dos respuestas «sí», y muchas veces no sale ninguna. Con C4, uno de cada cinco o seis pares se leería como cero; con C5, tres de cada cuatro. El kernel sería inmedible.
>
> **[CLIC]** En cambio, los valores esperados sí toleran 1,024 disparos: el MLP queda a menos de **0.02** del AUC exacto.

**Punto de control: 18:05.**

### 22 · Los seis objetivos se cumplieron · 0:50 (18:55)

> Respondo la pregunta. **Uno**: la codificación cuántica no aumentó la separabilidad; la redujo. **Dos**: y la diferencia se nota al clasificar. Los seis objetivos se cumplieron; el objetivo era medir, no ganar.
>
> **[CLIC]** General: sin mayor separabilidad, y de 0.07 a 0.14 menos de AUC.
> **[CLIC]** Uno: el pipeline, sin fuga entre pacientes.
> **[CLIC]** Dos: cinco representaciones del mismo vector.
> **[CLIC]** Tres: cuatro métricas de separabilidad.
> **[CLIC]** Cuatro: el mismo MLP en las cinco.
> **[CLIC]** Cinco: separabilidad y clasificación ordenan igual las condiciones.
> **[CLIC]** Seis: simular es viable; medir el kernel en hardware, no.
>
> **[CLIC]** Y como el método sí detecta la ventaja cuando existe, un resultado negativo, medido con rigor, es evidencia de viabilidad.

### 23 · Lo que sigue · 0:35 (19:30)

> Cada limitación abre una línea de trabajo.
> **[CLIC]** En la codificación: mapas que no se concentren sin perder la interacción.
> **[CLIC]** En la lectura: medir más que 12 valores, por ejemplo las 66 correlaciones entre pares de qubits.
> **[CLIC]** En hardware: primero simular con el ruido de un dispositivo real y luego medir en uno; con 200 lesiones, una matriz de kernel exige 19,900 circuitos.
> **[CLIC]** Y en datos: repetir el estudio con mamografía digital con escala física y validación externa.

### 24 · Gracias · 0:05 (19:35)

> Muchas gracias por su atención.

*(Quedarse en esta diapositiva y esperar la primera pregunta.)*

---

## Si se va tarde

En orden, lo primero que se puede quitar:
1. Las frases marcadas con ✂ (unos 40 s en total).
2. En la 3, leer solo la fila de «Este trabajo» y el recuadro de Azevedo.
3. En la 11, decir solo Davies-Bouldin y la frase final.
4. En la 22, no leer las filas: decir la respuesta, avanzar los siete clics seguidos y cerrar con la última frase.

Nunca recortar: la pregunta (4), la concentración (9), el 0 de 24 (15), la lectura (16), el control positivo (18) y la respuesta (22).

---

## Preguntas y respuestas

### Cómo moverse

- **I** lleva al **índice de anexos**, ordenado por tema; volver a pulsar **I** pasa al de figuras y luego al de tablas.
- **Número + Enter** va directo a ese anexo, desde cualquier diapositiva (por ejemplo, **46** + Enter).
- **↩ Índice**, abajo al centro de cada anexo, regresa al índice de su grupo.
- Si un sinodal pide «la figura 6.2.3» o «el cuadro 12» del reporte, ir al índice de figuras o de tablas: cada entrada dice el número del reporte y su anexo.

### Cómo responder

1. La respuesta en una frase.
2. La evidencia: «lo medimos en…», y mostrar el anexo si ayuda.
3. Cerrar con la consecuencia para la pregunta de investigación.

Si algo no se midió, decirlo: «Eso no lo medí; lo que sí medí es…».

### Tarjeta de preguntas probables

| Pregunta | Respuesta corta | Anexo |
|---|---|---|
| ¿Para qué sirve un resultado negativo? | El objetivo era medir viabilidad. Un negativo informa si el método podía detectar un positivo, y podía: con etiquetas diseñadas, 0.998 contra 0.857. La conclusión resiste θ, k, reps, semillas, clasificadores, muestra y folds. | **45** |
| ¿Por qué no una CNN? | Un circuito de 12 qubits recibe 12 números, no una imagen de ~5,037 × 2,960 px. Redimensionar a 224 × 224 destruye las medidas de tamaño, que están entre las más discriminativas. La pregunta es sobre la codificación, no sobre ganarle a una CNN. | **46** |
| ¿Por qué θ fijo? | Justicia: C2 y C3 no ven las etiquetas y un θ entrenado sí. Pregunta: se mide la codificación, no un modelo entrenado. Costo: por parameter-shift, 22.4 h a k = 8 y 2,689 h a k = 16 por condición. | **11** |
| ¿Y si se entrenaba θ? | Lo medimos (X8): gana de 0.00 a 0.04 en prueba, sin significancia, y sigue debajo de C1. C4 y C5 son funciones de las mismas 12 características: no pueden saber más que ellas. | **12** |
| ¿Por qué solo simulación? | La pregunta es si la codificación ayuda en condiciones ideales. El ruido solo empeora: si no hay ventaja sin ruido, no la habrá con ruido. Además, el kernel concentrado sería inmedible en hardware. | **7** |
| ¿Por qué 12 qubits? ¿Y con 8? | Por costo y para incluir varias familias de características. Con 8 baja la concentración, pero lo clásico sigue delante; la conclusión es la misma. | **15** |
| ¿Por qué solo 200 lesiones en la separabilidad? | Por el costo del protocolo físico: 19,900 circuitos por matriz, contra 0.87–1.19 millones con todo el entrenamiento. Se comprobó en 20 submuestras y en todo el entrenamiento: el RBF va delante en el 100 %. | **20** |
| ¿Hubo fuga de información? | No. Particiones por paciente (StratifiedGroupKFold), parada temprana con pacientes del entrenamiento, y el conjunto de prueba (704 lesiones) se usó una sola vez. | **23** |
| ¿Las intensidades no calibradas meten el digitalizador? | Es una limitación declarada; en masas lideran características de intensidad. Pero las cinco condiciones reciben el mismo vector: un sesgo, si existe, las afecta por igual. | **47** |
| ¿Cuánto se pierde con 12 de 67? | De 0.015 a 0.042 de AUC con clasificadores clásicos. Las cinco condiciones usan las mismas 12, y con las 67 tampoco hay ventaja cuántica. | **48** |
| ¿Se generaliza? | Es un solo conjunto, sin escala física. La conclusión vale para estas etiquetas, estas características y estas familias de kernels; otros datos y codificaciones son trabajo futuro. | **49** |
| ¿Cuándo valdría la pena el hardware? | Cuando se cumplan tres cosas a la vez: etiquetas que sigan la geometría del circuito, un kernel que no se concentre y una codificación difícil de simular. Aquí falla la primera. | **50** |
| ¿Por qué las masas salen peor que las calcificaciones? | Depende de la representación: con los descriptores del radiólogo las masas son más separables (0.872 contra 0.825); con radiómica, al revés (0.693 contra 0.800). Por eso son dos problemas independientes. | **35** |
| ¿Y si se reduce la escala de los ángulos? | La mediana sube de 0.002 a 0.55, pero con c = 0.02 el kernel es idéntico al de un mapa sin el término de interacción: se quita la concentración y también la interacción. | **34** |
| ¿Un QSVM lo haría mejor? | Empata con la SVM clásica (−0.02 y −0.01, sin diferencia significativa) y supera al MLP en 0.10 y 0.13. La información está en el estado; se pierde al leer 12 números. | **30** |
| ¿Se buscó la ventaja de forma justa? | Sí: la misma búsqueda anidada en los dos lados. Con etiquetas reales, ningún kernel cuántico supera a los clásicos. | **31** |
| ¿Por qué 5 folds? | Es el mayor número que mantiene equilibradas las clases por fold, porque los pacientes no se pueden partir. Con 3 folds la conclusión es la misma. | **21** |
| ¿Para qué sirve C2? | Es un control nulo: rotar no cambia la información. Si una métrica distinguiera C2 de C1, la métrica estaría mal; dan exactamente lo mismo. | **19** |
| Preguntas de fundamentos (qubit, entrelazamiento, feature map, kernel, medición, AUC) | Grupo «Fundamentos» del índice de anexos. | **2–6, 8** |
| Preguntas de fórmulas | Grupo «Fórmulas» del índice de anexos. | **38–44** |
