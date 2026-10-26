# Cambios a «Defensa TT 2026-B039»

Hay que actualizar la presentación con dos experimentos nuevos (X10 y X11), corregir algunas cifras y añadir apoyos visuales para un jurado que, salvo el director, no se especializa en computación cuántica.

## Reglas generales

1. **Respeta el sistema visual actual:** fondo `#fbfaf7`, tipografías Source Serif 4, Inter y JetBrains Mono, el pie «TT 2026-B039 · ESCOM-IPN» y la numeración. El código de color es fijo en todas las gráficas: **azul = clásico (C1–C3, RBF), naranja = C4, verde = C5**. Rosa/magenta solo para cifras destacadas, como ya está.
2. **Analogías solo como dibujo**, con un texto de apoyo de una línea como máximo. La explicación la doy yo en voz alta y va en las notas del orador.
3. **Dibujos y gráficas nativos** (SVG o HTML del propio deck, no imágenes pegadas), para poder animarlos.
4. **Animaciones por pasos que avanzan con la flecha** (fade, rise, pop, *magic move*). Nada interactivo, nada en bucle ni automático.
5. **No inventes ni redondees cifras.** Usa solo las de este documento y del archivo `kernel_40x40_masas.json`. Si un dibujo es esquemático y no proviene de datos, ponle la leyenda pequeña «esquema ilustrativo».
6. Todo el texto visible en español.
7. Duración objetivo: **unos 18 minutos** para la parte principal. Respeta los tiempos de las notas del orador.

## Nuevo orden

| # | Diapositiva | Estado | Tiempo (acumulado) |
|---|---|---|---|
| 1 | Portada | corregir fecha | 0:15 (0:15) |
| 2 | Contexto | sin cambios; notas más cortas | 0:40 (0:55) |
| 3 | Pregunta | sin cambios | 0:50 (1:45) |
| 4 | **NUEVA** · El qubit como flecha en una esfera; 12 qubits | nueva | 1:15 (3:00) |
| 5 | Las dos formas de leer el estado (antes 4) | añadir íconos | 1:00 (4:00) |
| 6 | Pipeline (antes 5) | sin cambios | 1:15 (5:15) |
| 7 | Cinco representaciones (antes 6) | añadir ícono a C2 | 0:45 (6:00) |
| — | Métricas (antes 7) | **pasa a respaldo R10** | — |
| 8 | Concentración del kernel | **rehacer con mapas de calor** | 2:00 (8:00) |
| 9 | Ninguna representación cuántica aumentó la separabilidad | textos de apoyo | 1:15 (9:15) |
| 10 | El mismo MLP clasifica peor | sin cambios | 1:00 (10:15) |
| 11 | **NUEVA** · ¿Y si fuera el clasificador? (X10) | nueva | 1:15 (11:30) |
| 12 | La pérdida está en la lectura (antes 11) | añadir ícono | 1:15 (12:45) |
| 13 | **REHECHA** · ¿Cuándo habría ventaja? (X11, sustituye la 12) | rehacer | 1:45 (14:30) |
| 14 | Viabilidad (antes 13) | añadir la encuesta | 1:15 (15:45) |
| 15 | Respuesta (antes 14) | actualizar puntos | 1:15 (17:00) |
| 16 | Limitaciones y trabajo futuro (antes 15) | corregir | 0:40 (17:40) |
| R1–R7 | Respaldos actuales | R4 y R5 con correcciones | — |
| R8 | **NUEVO** · ¿Por qué 5 folds? | nuevo | — |
| R9 | **NUEVO** · ¿Y si se reduce la escala de los ángulos? | nuevo | — |
| R10 | Métricas de separabilidad (la antigua 7, sin cambios) | movida | — |

Actualiza los contadores «n / 16» y «Rn / R10».

---

## Diapositivas

### 1 · Portada
- Fecha: **24 de noviembre de 2026** (en lugar de «Noviembre de 2026»).
- Notas: quita «PENDIENTE: CONFIRMAR título definitivo y fecha». El título ya coincide con el del reporte.

### 2 · Contexto
- Sin cambios visuales.
- Notas: *Tiempo objetivo: 0:40 (acumulado 0:55).* El cáncer de mama sumó 2.3 millones de casos nuevos en el mundo en 2022 y en México causó 8,451 defunciones en 2024. Detectado a tiempo, la supervivencia a cinco años supera el 99 %; con metástasis cae a cerca de 33 %. El aprendizaje automático clásico ya clasifica lesiones; este trabajo no supone que lo cuántico sea mejor, lo mide.

### 3 · Pregunta
- Sin cambios visuales.
- Notas: quita «PENDIENTE: CONFIRMAR redacción final de la pregunta (D-041)». *Tiempo objetivo: 0:50 (acumulado 1:45).* El resto igual.

### 4 · NUEVA · «Un qubit es una flecha en una esfera; 12 qubits combinan 4,096 posibilidades»
Etiqueta de sección: «02 · Idea».

**Dibujo y pasos:**
1. Una esfera tipo globo terráqueo (reutiliza el estilo de las esferas de R3) con una flecha hacia el polo norte, etiquetada `|0⟩`.
2. *(paso)* La flecha baja al ecuador. Etiqueta: «Hadamard: al ecuador».
3. *(paso)* La flecha gira a lo largo del ecuador un ángulo marcado `2xᵢ`. Etiqueta: «el giro es la característica». Texto de apoyo: «xᵢ ∈ [0, π] → como mucho una vuelta».
4. *(paso)* A la derecha, una fila de 12 interruptores y una cuadrícula que se duplica en secuencia: 2 → 4 → 8 → … → **4,096** casillas. Muestra 4–5 etapas y salta a la final. Texto de apoyo: «12 qubits = 2¹² = 4,096 combinaciones».
5. *(paso)* Dos engranes acoplados entre dos qubits. Etiqueta: «ZZ: cada par gira según sus dos características a la vez».

**Notas:** *Tiempo objetivo: 1:15 (acumulado 3:00).* Un qubit se puede imaginar como una flecha dentro de un globo: arriba es 0, abajo es 1, y en medio hay infinitos estados. Hadamard lleva la flecha al ecuador, y luego la giramos un ángulo que depende de una característica de la lesión. Así cada característica se convierte en una posición del globo. Con 12 qubits hay 2¹², es decir 4,096 combinaciones de ceros y unos, y el estado asigna un peso a cada una: es como una receta con 4,096 ingredientes. El bloque ZZ acopla los qubits por pares, como engranes: el giro de cada par depende de las dos características a la vez, y así el circuito codifica sus interacciones. Ese acoplamiento es el entrelazamiento, y por eso ya no basta una flecha por qubit para describir el estado: hay que usar las 4,096 dimensiones.

### 5 · Las dos formas de leer el estado (antes 4)
- Conserva el diagrama y sus 8 pasos.
- Añade dos íconos pequeños: junto a «(a) Kernel de fidelidad», dos huellas dactilares superpuestas; junto a «(b) Valores esperados», una tira de película con 12 fotogramas.
- Textos de apoyo bajo cada ícono: (a) «compara dos estados completos»; (b) «resume el estado en 12 números».
- Notas: *Tiempo objetivo: 1:00 (acumulado 4:00).* Las mismas, más: (a) es como comparar dos huellas dactilares completas; (b) es como describir una película con 12 fotogramas.

### 6 · Pipeline (antes 5)
- Sin cambios. Solo actualiza el tiempo de las notas: *1:15 (acumulado 5:15).*

### 7 · Cinco representaciones (antes 6)
- Junto a C2, un ícono pequeño de una foto girada 30°. Texto de apoyo: «girar no cambia la información».
- Notas: *Tiempo objetivo: 0:45 (acumulado 6:00).* Añade: C2 es como girar una foto, porque lo que hay en ella no cambia; si una métrica premiara a C2 sobre C1, la métrica estaría mal.

### 8 · «El kernel cuántico ve casi todos los pares de lesiones como ortogonales» (rehacer)
Sustituye la gráfica de puntos por **dos mapas de calor de 40 × 40** con los datos de `kernel_40x40_masas.json`.

- Izquierda, «RBF clásico», matriz `RBF`; derecha, «C4 · ZZ», matriz `C4`.
- La escala de color es lineal, 0 = fondo crema y 1 = azul marino oscuro, la misma para ambos. Añade una barra de color pequeña de 0 a 1.
- Filas y columnas 0–19 son benignas y 20–39 malignas. Marca la división con una línea fina y rótulos «benignas» y «malignas» en los ejes.
- Bajo cada mapa: «mediana fuera de la diagonal: **0.60**» (RBF) y «**0.002**» (C4).
- Texto pequeño: «C5 está aún más concentrado: mediana 0.00003; el 26–28 % de los pares queda por debajo de 10⁻⁶». Esto vale para masas y calcificaciones.
- Leyenda: «40 lesiones de masas de la submuestra de 200 · cada celda = parecido entre dos lesiones».

**Pasos:**
1. El mapa RBF, con su mediana.
2. *(paso)* El mapa C4: solo se ve la diagonal.
3. *(paso)* Dibujo de la analogía, abajo o a la derecha: dos recuadros de mapa urbano. En el primero se ven colonias y calles; en el segundo, el zoom es tan grande que una sola casa llena el recuadro. Texto de apoyo: «demasiado zoom: todo queda igual de lejos».
4. *(paso)* Frase de cierre en negritas: «**Si todas las lesiones están igual de lejos, el parecido no distingue clases: concentración.**»

**Notas:** *Tiempo objetivo: 2:00 (acumulado 8:00).* Cada celda dice qué tan parecidas son dos lesiones; las primeras 20 son benignas y las siguientes 20 malignas. Con el kernel clásico hay toda una gama de parecidos. Con el cuántico solo queda la diagonal: cada lesión se parece a sí misma y a casi nadie más, y la mediana fuera de la diagonal es 0.002. Es como un mapa con tanto zoom que cada casa llena la pantalla: ya no se distinguen colonias. Si todas las lesiones están igual de lejos entre sí, la matriz se parece a la identidad y no puede distinguir benignas de malignas. Esto se conoce como concentración del kernel. Huang et al. describen este caso como el típico de los modelos cuánticos que no superan a los clásicos: «all inputs are too far apart». Si preguntan por reducir la escala, ir al respaldo R9.

### 9 · Ninguna representación cuántica aumentó la separabilidad
- Sin cambios en las gráficas.
- Texto de apoyo bajo el título del panel izquierdo: «¿el parecido entre lesiones coincide con el diagnóstico?».
- Texto de apoyo bajo el panel de *g*: «¿el mapa cuántico tiene caminos que el clásico no puede trazar?».
- Notas: *Tiempo objetivo: 1:15 (acumulado 9:15).* Las mismas.

### 10 · El mismo MLP clasifica peor sobre los embeddings cuánticos
- Sin cambios. Notas: *Tiempo objetivo: 1:00 (acumulado 10:15).*

### 11 · NUEVA · «Con árboles, bosques y *boosting*, ninguna representación cuántica supera a C1»
Etiqueta de sección: «03 · Resultados». Mismo estilo de gráfica que la diapositiva 10: puntos = AUC en prueba, barras = IC 95 % por *bootstrap* por paciente, línea punteada en 0.5 = azar. Dos paneles, Masas y Calcificaciones. En cada panel, tres grupos en el eje X (MLP, *Random forest* y XGBoost) y, dentro de cada grupo, C1 (azul), C4 (naranja) y C5 (verde).

| Subconjunto | Clasificador | C1 | C4 | C5 |
|---|---|---|---|---|
| Masas | MLP | 0.651 [0.578, 0.724] | 0.530 [0.473, 0.587] | 0.581 [0.521, 0.644] |
| Masas | Random forest | 0.636 [0.566, 0.704] | 0.591 [0.526, 0.658] | 0.614 [0.553, 0.679] |
| Masas | XGBoost | 0.630 [0.556, 0.704] | 0.590 [0.525, 0.654] | 0.611 [0.548, 0.674] |
| Calcificaciones | MLP | 0.769 [0.694, 0.836] | 0.633 [0.558, 0.700] | 0.652 [0.571, 0.725] |
| Calcificaciones | Random forest | 0.768 [0.698, 0.833] | 0.651 [0.581, 0.717] | 0.624 [0.548, 0.701] |
| Calcificaciones | XGBoost | 0.779 [0.707, 0.845] | 0.640 [0.570, 0.705] | 0.621 [0.543, 0.698] |

**Pasos:**
1. Solo el grupo MLP, que es lo que ya vieron.
2. *(paso)* Aparecen *random forest* y XGBoost.
3. *(paso)* Resalta en masas los puntos C4 y C5 de RF y XGB, con la etiqueta: «leen mejor los ⟨Zᵢ⟩, pero no alcanzan a C1».
4. *(paso)* Cifra destacada en magenta: «**0 de 24** comparaciones a favor de C4/C5». Debajo, en pequeño: «6 clasificadores × 2 subconjuntos × 2 condiciones cuánticas, mismo clasificador contra C1».
5. *(paso)* Dibujo pequeño: una hoja original y su fotocopia, con flecha «x → C4, C5». Texto de apoyo: «C4 y C5 se calculan a partir de x: no contienen más información que x».

**Notas:** *Tiempo objetivo: 1:15 (acumulado 11:30).* En la revisión se preguntó si el resultado dependía de haber usado una red neuronal, y si árboles o XGBoost, que modelan interacciones no lineales, aprovecharían mejor las representaciones cuánticas. Lo probamos con cinco clasificadores de árboles sobre las mismas cinco representaciones, eligiendo hiperparámetros con validación cruzada anidada, y comparando siempre con el mismo clasificador. El resultado: en ninguna de las 24 comparaciones una representación cuántica supera a C1. En calcificaciones la brecha es la misma con cualquier clasificador. En masas, los ensambles leen mejor los valores esperados y la brecha deja de ser significativa, pero no alcanzan a C1. Hay una razón de fondo: C4 y C5 se calculan a partir de x, como una fotocopia se saca de un original, y una fotocopia no puede tener más información que el original. Un clasificador puede aprovechar mejor una forma que otra con datos finitos, y por eso había que medirlo. Además, las interacciones aportan poco: un XGBoost que solo suma funciones de cada entrada rinde casi igual que el completo.

### 12 · La pérdida está en la lectura de 12 números (antes 11)
- Junto al texto de la derecha, la misma tira de 12 fotogramas de la diapositiva 5 frente a una película completa.
- Notas: *Tiempo objetivo: 1:15 (acumulado 12:45).* Las mismas.

### 13 · REHECHA · «La ventaja cuántica aparece cuando la tarea sigue la geometría del circuito; el diagnóstico no la sigue»
Sustituye la gráfica de barras actual. Etiqueta de sección: «03 · Resultados».

**Gráfica:** una sola, de líneas.
- Eje X: «α: fracción de lesiones cuya etiqueta sigue la geometría del kernel cuántico», de 0 a 1.
- Eje Y: «AUC-ROC (validación cruzada)», de 0.5 a 1.0.
- Dos líneas: naranja «kernel cuántico proyectado (QSVM)» y azul «mejor clásico (12 SVM y 4 XGBoost)». Título del panel: «Masas».

| α | Cuántico | Mejor clásico | Diferencia [IC 95 %] |
|---|---|---|---|
| 0.0 | 0.566 | 0.677 | −0.111 [−0.150, −0.070] |
| 0.1 | 0.600 | 0.665 | −0.065 [−0.100, −0.030] |
| 0.2 | 0.637 | 0.667 | −0.030 [−0.061, 0.002] |
| 0.3 | 0.671 | 0.669 | +0.003 [−0.024, 0.031] |
| 0.4 | 0.711 | 0.668 | +0.043 [0.021, 0.066] |
| 0.5 | 0.756 | 0.675 | +0.081 [0.059, 0.103] |
| 0.6 | 0.796 | 0.701 | +0.095 [0.076, 0.114] |
| 0.7 | 0.839 | 0.740 | +0.099 [0.081, 0.117] |
| 0.8 | 0.893 | 0.780 | +0.114 [0.095, 0.133] |
| 0.9 | 0.950 | 0.813 | +0.137 [0.116, 0.157] |
| 1.0 | 0.998 | 0.857 | +0.141 [0.119, 0.163] |

**Pasos:**
1. Ejes y solo los dos puntos de α = 0, con la etiqueta «diagnóstico real»: el clásico va delante.
2. *(paso)* Las dos líneas se dibujan de izquierda a derecha hasta α = 1. El punto final lleva la etiqueta «tarea diseñada».
3. *(paso)* Se sombrea la zona α ≥ 0.4 con la línea vertical «α* = 0.4» y la etiqueta «ventaja cuántica (IC 95 % > 0)».
4. *(paso)* Una llave entre α = 0 y α = 0.4: «distancia del diagnóstico a la zona de ventaja».
5. *(paso)* A la derecha, una tabla pequeña del umbral α*:

   | Kernel cuántico | Masas | Calcificaciones |
   |---|---|---|
   | ZZ completo (C4) | 0.6 | 0.7 |
   | ZZ lineal | 0.5 | 0.6 |
   | Proyectado | 0.4 | 0.5 |

   Debajo: «el diagnóstico real está en α = 0».
6. *(paso)* Dibujo de la analogía: dos libros de texto, «libro clásico» y «libro del circuito», y una hoja de examen cuyas preguntas se colorean poco a poco del color del segundo libro. Texto de apoyo: «α = cuántas preguntas salen del libro del circuito».

Leyenda fija al pie, en pequeño: «Etiquetas intermedias artificiales: instrumento de medida, no tarea clínica. Etiquetado diseñado según Huang et al. (2021), sección 7 del suplemento. 5 máscaras aleatorias por α; no usa el conjunto de prueba.»

**Notas:** *Tiempo objetivo: 1:45 (acumulado 14:30).* La pregunta natural es: ¿hay algún caso en el que lo cuántico gane? Sí, y lo medimos sobre estas mismas lesiones. Siguiendo a Huang et al., construimos etiquetas que siguen la geometría del kernel cuántico, y fuimos mezclándolas con el diagnóstico real: α es la fracción de lesiones que toma la etiqueta diseñada. Es como un examen: si las preguntas salen del libro que estudió el circuito, el circuito gana; el diagnóstico es un examen de otro libro. Con α = 0, el diagnóstico real, el clásico va delante. La ventaja cuántica aparece a partir de α = 0.4 con el kernel proyectado, y entre 0.5 y 0.7 con los demás, y llega a +0.14 de AUC con la tarea diseñada, incluso contra XGBoost. Dos lecturas: el protocolo sí detecta una ventaja cuando existe, y el diagnóstico benigno o maligno con estas características está en el extremo opuesto. Además, el kernel con la *g* más grande cruza antes y gana más, que es lo que predice la teoría. Las etiquetas intermedias son artificiales: es un instrumento de medida, no una tarea clínica.

### 14 · Simular cabe; medir en hardware sería el problema (antes 13)
- Reduce el panel de barras de qubits a la mitad izquierda y conserva sus datos.
- A la derecha, sustituye el bloque «16–74 %» por **la encuesta**:
  1. Una cuadrícula de 32 × 32 = 1,024 puntos grises, rotulada «1,024 disparos».
  2. *(paso)* Se encienden **2** puntos. Texto de apoyo: «valor real ≈ 0.002 → se esperan ~2 “sí” de 1,024».
  3. *(paso)* Los 2 puntos se apagan. Texto: «a veces salen 0: el valor se lee como cero».
  4. *(paso)* Cifras destacadas en magenta: «C4: **21 %** (masas) y **16 %** (calcificaciones) de los pares se leen exactamente 0 · C5: **74 %** y **72 %**».
  5. *(paso)* La línea actual: «Los ⟨Zᵢ⟩ sí toleran 1,024 disparos: el MLP queda a menos de 0.02 del AUC exacto».
- Leyenda: «esquema ilustrativo» en la cuadrícula; las cifras son medidas.
- Notas: *Tiempo objetivo: 1:15 (acumulado 15:45).* En simulación exacta todo cupo: usamos 12 qubits, y en esta laptop el embedding cabe hasta unos 25 y el kernel de 200 × 200 hasta unos 22. El problema está en el hardware. Un valor del kernel se estima como una encuesta: se repite el circuito 1,024 veces y se cuenta cuántas veces sale cero en todos los qubits. Si el valor real es 0.002, se esperan unas 2 respuestas «sí» de 1,024, y muchas veces no sale ninguna. Con C4, entre uno de cada cinco y uno de cada seis pares se leería exactamente como cero; con C5, tres de cada cuatro. El kernel sería inmedible. En cambio, los valores esperados sí toleran 1,024 disparos.

### 15 · Respuesta (antes 14)
Título igual. Los cinco puntos:
1. Con k = 12, una repetición y c = 1, C4 y C5 separan peor que C1–C3 en todas las métricas.
2. La pérdida se refleja en la clasificación: −0.07 a −0.14 de AUC con el MLP; con 6 clasificadores, 0 de 24 comparaciones a favor de lo cuántico.
3. Causa identificada: concentración del kernel y lectura por 12 valores esperados.
4. La ventaja aparece cuando el 40–70 % de las etiquetas sigue la geometría del kernel cuántico; el diagnóstico real está en el 0 %.
5. Viable en simulación; en hardware, la concentración haría inmedible el kernel.

Cada punto entra en un paso; la cita final, al último.

Notas: *Tiempo objetivo: 1:15 (acumulado 17:00).* Ajusta los puntos 2 y 4 a lo anterior; el resto igual.

### 16 · Limitaciones y trabajo futuro (antes 15)
**Limitaciones:**
- Simulación sin ruido.
- Intensidades no calibradas y sin escala física (PixelSpacing ausente).
- Separabilidad sobre 200 lesiones por subconjunto: el tamaño repetible en hardware (19,900 circuitos por matriz); la conclusión se mantiene con todo el entrenamiento.

**Trabajo futuro:**
- Codificaciones que eviten la concentración sin perder la interacción (ancho de banda por característica, conocimiento del problema).
- Lecturas intermedias del estado: correlaciones ⟨ZᵢZⱼ⟩ (66 valores) y lectores más profundos.
- Ejecución en procesadores cuánticos con mitigación de errores.

Notas: *Tiempo objetivo: 0:40 (acumulado 17:40; quedan ~2:20 de margen).* En la limitación de las 200 lesiones, di «es el tamaño que se podría repetir en un procesador real: 19,900 circuitos por matriz, contra cerca de un millón con todo el entrenamiento; con todo el entrenamiento la conclusión es la misma». En la lista de respaldos, añade R8 a R10.

---

## Respaldos

### R4 · Diferencia geométrica (correcciones)
- «Protocolo de Huang et al. (2021), Apéndice L.3» → «Protocolo de Huang et al. (2021), suplemento, sección 12 C».
- En la leyenda de K_C: «kernel clásico (RBF)» → «kernel clásico: lineal y 9 gaussianos; se toma el mínimo».

### R5 · Robustez (añadir una fila)
- «6 clasificadores (árboles, *random forest*, XGBoost, MLP)» → «0 de 24 comparaciones a favor de C4/C5».

### R8 · NUEVO · «¿Por qué 5 folds? Es el mayor número que mantiene equilibradas las clases»
Tabla o tres columnas con el estilo de R2:

| Folds | Entrena con | Desviación máx. de la proporción de malignas (masas / calc.) | Malignas en el fold más pobre (masas / calc.) | Peso del paciente más grande (calc.) |
|---|---|---|---|---|
| 3 | 67 % | 0.003 / 0.003 | 200 / 167 | 5 % |
| **5** | **80 %** | **0.011 / 0.019** | **122 / 96** | **9 %** |
| 10 | 90 % | 0.044 / 0.045 | 57 / 49 | 17 % |

Debajo, una tira de sensibilidad «C4 − C1 en validación cruzada con 5 y con 3 folds»:

| | C4−C1 (5) | C4−C1 (3) | C5−C1 (5) | C5−C1 (3) |
|---|---|---|---|---|
| Masas | −0.087 | −0.123 | −0.089 | −0.098 |
| Calcificaciones | −0.102 | −0.119 | −0.075 | −0.092 |

Texto de apoyo: «Con 3 folds la conclusión no cambia».

Notas: Respaldo R8, para cuando pregunten por el número de folds. El número de folds no depende del número de características, sino de cuántos pacientes quedan en cada fold. Con más folds, cada modelo entrena con más datos, pero cada fold de validación es más pequeño y, como los pacientes son bloques indivisibles, cuesta equilibrar las clases: en calcificaciones hay una paciente con 24 lesiones, todas benignas. Cinco es el mayor número con el que la proporción de malignas de cada fold se aparta menos de 0.02 de la global en ambos subconjuntos. Con 3 folds, la conclusión del M7 es la misma.

### R9 · NUEVO · «Reducir la escala de los ángulos quita la concentración, pero también la interacción»
Gráfica de puntos o línea en escala logarítmica en Y: la mediana del kernel C4 (masas) contra c.

| c | 1 | 0.5 | 0.2 | 0.1 | 0.05 | 0.02 |
|---|---|---|---|---|---|---|
| Mediana del kernel C4, masas | 0.0022 | 0.0060 | 0.032 | 0.069 | 0.199 | 0.555 |

**Pasos:**
1. Los puntos de c = 1 a c = 0.02.
2. *(paso)* En c = 0.02, la etiqueta: «idéntico al kernel sin el término xᵢxⱼ (correlación 1.0000)».
3. *(paso)* Reutiliza el dibujo del mapa de la diapositiva 8, ahora con el zoom tan alejado que se ve una mancha sin calles. Texto de apoyo: «demasiado lejos: se pierden las calles (las interacciones)».

Notas: Respaldo R9. Con c más pequeño los giros son más cortos y los estados se parecen más: la mediana sube de 0.002 a 0.55. Pero el término de interacción xᵢxⱼ escala con c² y el de cada característica con c, así que al reducir c las interacciones desaparecen primero. Con c = 0.02 el kernel es idéntico al de un mapa sin el término de producto. Es como alejar el zoom del mapa: dejas de ver casas sueltas, pero también pierdes las calles. El entrelazamiento lineal en xᵢ + xⱼ persiste. Con c elegido por validación cruzada, el QSVM igualó al mejor clásico, pero en ese régimen la interacción apenas influye.

### R10 · Métricas de separabilidad
- La antigua diapositiva 7, sin cambios de contenido. Etiqueta «Respaldo · R10».

---

## Comprobación final antes de exportar
- [ ] 16 diapositivas principales y 10 respaldos, con contadores correctos.
- [ ] Ninguna cifra distinta de las de este documento.
- [ ] Colores: azul clásico, naranja C4, verde C5 en las gráficas nuevas.
- [ ] Cada dibujo esquemático lleva «esquema ilustrativo».
- [ ] Todas las animaciones avanzan con la flecha; ninguna es automática.
- [ ] No quedan «PENDIENTE» en las notas.
