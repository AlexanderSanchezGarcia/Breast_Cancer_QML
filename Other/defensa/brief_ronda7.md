# Ronda 7 · «Defensa TT 2026-B039»: portada, contexto, hilo de la pregunta, nuevo orden, separabilidad en dos, la curva ROC explicada y despedida aparte

Esta ronda tiene ocho cambios:
1. Portada: los directores en dos renglones y los logos más grandes.
2. Contexto rediseñado en tres pasos, con una gráfica de supervivencia por etapa.
3. Los círculos ① y ② de la pregunta se vuelven un **hilo conductor** que reaparece en los resultados.
4. «Cinco representaciones» pasa antes del qubit.
5. La diapositiva de separabilidad de las representaciones se divide en dos (métricas y t-SNE).
6. Una diapositiva nueva con un video que explica cómo se lee una curva ROC.
7. El trabajo futuro y la despedida quedan en diapositivas separadas.
8. Tiempos, contadores y referencias cruzadas.

Las reglas de los briefs anteriores siguen vigentes. **No inventes ni redondees cifras:** todas salen de este documento. **Los anexos no cambian en esta ronda**, salvo las cuatro referencias cruzadas de la sección final.

**Importante sobre los videos:** no cambies el texto alternativo de las imágenes de los seis videos; debe seguir empezando con «Video…». El video nuevo de esta ronda (`roc_umbral.mp4`, adjunto) también lleva un texto alternativo que empieza con «Video…» (abajo). Ninguna otra imagen debe empezar con «Video».

---

## Nuevo orden y tiempos

| # | Diapositiva | Cambio | Tiempo (acumulado) |
|---|---|---|---|
| 1 | Portada | directores en dos renglones, logos más grandes | 0:15 (0:15) |
| 2 | Contexto | **rediseño en tres pasos** | 0:50 (1:05) |
| 3 | Estado del arte | — | 0:50 (1:55) |
| 4 | Pregunta | **① y ② como hilo conductor** | 0:50 (2:45) |
| 5 | Proceso | — | 1:10 (3:55) |
| 6 | Cinco representaciones (antes 8) | **sube**; nota sobre el ansatz | 0:45 (4:40) |
| 7 | Qubit (antes 6) | — | 1:00 (5:40) |
| 8 | Dos lecturas (antes 7) | — | 0:50 (6:30) |
| 9 | Concentración | insignia ① | 1:20 (7:50) |
| 10 | Separabilidad (kernels) | insignia ① | 1:00 (8:50) |
| 11 | Separabilidad (representaciones) | **solo las métricas**; insignia ① | 0:50 (9:40) |
| 12 | **NUEVA · t-SNE** | sale de la 11; insignia ① | 0:30 (10:10) |
| 13 | **NUEVA · Cómo se lee una curva ROC** | video nuevo; insignia ② | 0:35 (10:45) |
| 14 | El mismo MLP (antes 12) | insignia ②; notas más cortas | 0:50 (11:35) |
| 15 | Árboles (antes 13) | insignia ② | 0:50 (12:25) |
| 16 | La lectura (antes 14) | insignia ② | 1:00 (13:25) |
| 17 | Resumen (antes 15) | insignias ① ② | 0:50 (14:15) |
| 18 | La ventaja sí existe (antes 16) | — | 0:55 (15:10) |
| 19 | X11 (antes 17) | — | 1:05 (16:15) |
| 20 | Viabilidad (antes 18) | — | 1:00 (17:15) |
| 21 | Objetivos cumplidos (antes 19) | ① ② en la respuesta | 0:55 (18:10) |
| 22 | Trabajo futuro (antes 20) | **sin la despedida** | 0:35 (18:45) |
| 23 | **NUEVA · Despedida** | nueva | 0:10 (18:55; quedan ~1:05) |

- La parte principal pasa a **23 diapositivas**: actualiza los contadores a «n / 23».
- Actualiza el «Tiempo objetivo» y el «acumulado» de todas las notas según la tabla. En la 9, la 19 y la 20 el recorte es de lo que se dice: el texto de sus notas no cambia.

---

## 1 · Portada
- **Directores en dos renglones**, uno por director, con el mismo tamaño y estilo de texto que hoy:
  - Dr. Jesús Yaljá Montiel Pérez
  - Dra. Ana María Winfield Reyes
- **Logos del IPN y de ESCOM más grandes**, más o menos al doble de su alto actual (de ~100 px a ~190–200 px de alto en el lienzo de 1920×1080), en las mismas esquinas. Ajusta el espacio vertical para que el título no se mueva hacia abajo de la línea divisoria ni se encime con los logos.
- Lo demás, igual.

## 2 · Contexto: rediseño en tres pasos
- Título: «Detectar a tiempo cambia la supervivencia de 33 % a más de 99 %» (sin cambio).
- **Paso 1, magnitud.** A la izquierda, en columna, las dos cifras grandes de hoy con su fuente:
  - «2.3 M» · «nuevos casos en el mundo, 2022» · OMS;
  - «8,451» · «defunciones en México, 2024» · INEGI.
- **Paso 2, gráfica de barras horizontales** a la derecha: «Supervivencia relativa a 5 años según la etapa al diagnóstico». Tres barras, de arriba abajo, con la etiqueta de la etapa a la izquierda, una aclaración breve debajo y el valor al final de la barra:
  - **Localizada** · «no ha salido de la mama» · **>99 %** (barra en `DESTACADO`, magenta);
  - **Regional** · «llegó a ganglios cercanos» · **87 %** (gris medio);
  - **Distante** · «metástasis» · **33 %** (gris oscuro / `TINTA`).
  - Eje de 0 a 100 %, sin rejilla. Fuente bajo la gráfica: «American Cancer Society · datos SEER (National Breast Cancer Foundation, 2026)».
- **Paso 3, cadena hacia la pregunta.** Abajo, a todo el ancho, cuatro recuadros unidos por flechas:
  1. «Mamografía de tamizaje» · debajo, pequeño: «hasta 40 % menos mortalidad con tamizaje regular · ACR»;
  2. «La lectura varía entre radiólogos» · debajo, pequeño: «Elmore et al., 1994»;
  3. «El aprendizaje automático clásico ya clasifica lesiones»;
  4. «¿Una codificación cuántica las representa de forma más separable?», con borde en `C4` (naranja): es la pregunta del trabajo.
- Sale la frase en cursiva de abajo («El aprendizaje automático clásico ya clasifica lesiones; la pregunta abierta…»): la sustituye la cadena.
- **Notas:** *Tiempo objetivo: 0:50 (acumulado 1:05).* El cáncer de mama sumó 2.3 millones de casos nuevos en el mundo en 2022 y en México causó 8,451 defunciones en 2024. Lo que más pesa es cuándo se detecta: si sigue dentro de la mama, la supervivencia a cinco años supera el 99 %; si ya llegó a ganglios cercanos, baja a 87 %; con metástasis a distancia, a 33 %. La herramienta de la detección temprana es la mamografía: con tamizaje regular la mortalidad puede bajar hasta un 40 %. Pero su lectura varía entre radiólogos, y por eso se desarrollan apoyos computacionales; el aprendizaje automático clásico ya clasifica lesiones. Este trabajo no supone que lo cuántico sea mejor: pregunta si una codificación cuántica representa las lesiones de forma más separable, y lo mide.

## 4 · Pregunta: ① y ② como hilo conductor
- La pregunta completa y sus colores se quedan como están.
- **Los círculos ya no flotan bajo el texto.** Cada número va **en línea, justo antes de su frase**, alineado con la línea base del texto: «① modifican la separabilidad» y «② se refleja en la capacidad de clasificación». Círculo relleno en `TINTA` con el número en blanco, del alto de la letra minúscula más o menos, para que se lea como parte de la frase.
- **Paso nuevo:** entre la pregunta y la línea «Objetivo: …» entran dos fichas lado a lado, que son la **clave** que se repetirá en los resultados:
  - «① Separabilidad · ¿la transformación cuántica separa mejor benignas y malignas?»
  - «② Clasificación · ¿se nota al clasificar con la misma red neuronal?»
  Cada ficha: el círculo con el número, la palabra en negritas y la pregunta corta en gris. Fondo `TARJETA`, sin colores de condición.
- **Notas:** *Tiempo objetivo: 0:50 (acumulado 2:45).* Esta es la pregunta de investigación. Tiene dos partes, y las voy a marcar con estos dos números durante los resultados. La uno: si la transformación cuántica cambia qué tan separables son las lesiones benignas y malignas. La dos: si ese cambio se nota cuando la misma red neuronal clasifica sobre cada representación. Todo parte del mismo vector de características, para que la única diferencia sea la transformación. El objetivo es evaluar viabilidad, no superar a una red convolucional, y todo se hizo en simulación ideal.

## Insignias ① y ② en los resultados
- En las diapositivas de abajo, junto a la etiqueta de sección («03 · Resultados»), en el mismo renglón, va una insignia pequeña con el círculo y la palabra: «① Separabilidad» o «② Clasificación». Mismo estilo que las fichas de la 4, en pequeño (del alto de la etiqueta de sección). No debe chocar con el mapa miniatura de la esquina superior derecha.
  - **① Separabilidad:** 9 (Concentración), 10 (kernels), 11 (métricas), 12 (t-SNE).
  - **② Clasificación:** 13 (curva ROC), 14 (el mismo MLP), 15 (árboles), 16 (la lectura).
  - **① ② juntas:** 17 (Resumen).
  - Sin insignia: 18 y 19 (ventaja diseñada y X11 no responden la pregunta, la contextualizan), 20 (viabilidad).
- **21 · Objetivos cumplidos:** en la franja de la respuesta, el círculo ① antes de la primera mitad y el ② antes de la segunda: «① La codificación cuántica no aumentó la separabilidad; la redujo, ② y la diferencia se nota al clasificar.» El resto de la diapositiva no cambia.

## 6 · Cinco representaciones (antes 8): sube antes del qubit
- Contenido visual sin cambios; solo se mueve de lugar, con su mapa miniatura.
- **Notas:** *Tiempo objetivo: 0:45 (acumulado 4:40).* Las de hoy, con un cambio: después de «ambas seguidas del mismo ansatz fijo» añade «; el ansatz es un bloque de giros con parámetros fijos que va después de la codificación, y lo veremos en dos diapositivas».

## 7 · Qubit (antes 6) y 8 · Dos lecturas (antes 7)
- Sin cambios de contenido; solo el número, el contador y el tiempo (1:00 → acumulado 5:40; 0:50 → acumulado 6:30).

## 11 · Separabilidad de las representaciones: solo las métricas
- Título y etiqueta, sin cambio. Pie: «Fig. 6.2.4 del reporte · 200 lesiones de entrenamiento por subconjunto».
- **Quita el paso del t-SNE de esta diapositiva**: hoy la cuadrícula de t-SNE se dibuja encima de las barras atenuadas y se ven encimadas, sobre todo en el PDF. Las barras con su banda de permutación y sus rótulos «como el azar» se quedan tal cual, ahora sin atenuarse, y pueden usar todo el alto disponible.
- **Notas:** *Tiempo objetivo: 0:50 (acumulado 9:40).* Las de hoy sin el último punto (el del t-SNE), que pasa a la 12.

## 12 · NUEVA · «Las mismas representaciones vistas en dos dimensiones (t-SNE)»
- Etiqueta: «03 · Resultados» + insignia «① Separabilidad». Pie: «Fig. 6.2.5 del reporte · 200 lesiones de entrenamiento por subconjunto».
- **Visual:** la cuadrícula de t-SNE de 2 × 5 que hoy es el paso 2 de la 11, con los mismos datos (`datos_ronda6.json` → `tsne_fig_6_2_5`), ahora ocupando toda la diapositiva: filas Masas y Calcificaciones, columnas C1–C5 con su color. Benignas como triángulos verdes y malignas como círculos morados, sin ejes ni números.
- Bajo la cuadrícula: «▲ benigna · ● maligna · t-SNE: solo ayuda visual; no es una métrica».
- Sin pasos.
- **Notas:** *Tiempo objetivo: 0:30 (acumulado 10:10).* Esto es solo una ayuda visual: el t-SNE aplana cada representación a dos dimensiones. En C1 las malignas tienden a agruparse hacia un extremo; en C5 quedan mezcladas. C2 se ve como C1 girada o reflejada, porque el PCA solo gira los datos. Las métricas son las de la diapositiva anterior.

## 13 · NUEVA · «Cómo se lee una curva ROC: un umbral recorre todas las puntuaciones»
- Etiqueta: «03 · Resultados» + insignia «② Clasificación». Pie: «Predicciones reales del MLP · 378 masas de prueba, 147 malignas».
- **Visual:** el video adjunto `roc_umbral.mp4` ocupa el área de contenido, centrado, sin recortar. Como imagen fija usa su **último fotograma**.
  - Texto alternativo: «Video: cómo se traza una curva ROC con las predicciones reales de C1 y C4 en masas».
- Sin otro texto en la diapositiva: el video trae sus rótulos.
- **Notas:** *Tiempo objetivo: 0:35 (acumulado 10:45).* Antes de ver las cinco condiciones, cómo se lee una curva ROC. El MLP le da a cada lesión una probabilidad de ser maligna: arriba las benignas, abajo las malignas. Un umbral decide: a la derecha se predice maligno. Al bajarlo detectamos más malignas, y sube la sensibilidad, pero también marcamos más benignas, y sube uno menos la especificidad. Cada umbral es un punto, y todos juntos forman la curva. El área bajo ella, el AUC, es la probabilidad de que una maligna al azar reciba una puntuación mayor que una benigna al azar: 1 es perfecto y 0.5 es el azar, la diagonal. Con C1 el AUC es 0.651; con C4 las dos clases se enciman y la curva se pega a la diagonal: 0.530. [El video arranca con un clic.]

## 14 · El mismo MLP (antes 12)
- Contenido sin cambios; insignia «② Clasificación».
- **Notas:** *Tiempo objetivo: 0:50 (acumulado 11:35).* Sustituye la primera frase («Cada curva recorre todos los umbrales: arriba a la izquierda es mejor, la diagonal es el azar.») por «Ahora las cinco condiciones en los dos subconjuntos.» El resto, igual.

## 15, 16, 17 (antes 13, 14, 15)
- Contenido sin cambios. Insignias: 15 y 16 «② Clasificación»; 17 «① Separabilidad» y «② Clasificación» juntas.
- Tiempos: 0:50 (12:25), 1:00 (13:25), 0:50 (14:15).

## 18, 19, 20 (antes 16, 17, 18)
- Sin cambios de contenido. Tiempos: 0:55 (15:10), 1:05 (16:15), 1:00 (17:15).

## 21 · Objetivos cumplidos (antes 19)
- Solo las insignias ① ② en la franja de la respuesta (ver arriba). Tiempo: 0:55 (18:10).

## 22 · Trabajo futuro (antes 20): sin la despedida
- **Quita** «Gracias · ¿Preguntas?» y el nombre del autor de abajo. Los cuatro carriles pueden ocupar el espacio que queda, con un poco más de aire entre ellos.
- **Notas:** *Tiempo objetivo: 0:35 (acumulado 18:45).* Las de hoy, quitando «Muchas gracias; quedo atento a sus preguntas.» y la nota final sobre los anexos (pasa a la 23).

## 23 · NUEVA · Despedida
- Sin etiqueta de sección ni título de diapositiva. Composición sobria, del mismo estilo que la portada:
  - arriba, los logos del IPN y de ESCOM en las mismas esquinas y con el mismo tamaño nuevo que la portada;
  - al centro, en grande y en serif: **«Gracias»**;
  - debajo: «Miguel Alexander Sánchez García»;
  - debajo, en gris y en dos renglones, con el rótulo «Directores»: «Dr. Jesús Yaljá Montiel Pérez» / «Dra. Ana María Winfield Reyes»;
  - pie, como en la portada: «TT 2026-B039 · ESCOM-IPN» y «23 / 23».
- **No** pongas «¿Preguntas?» ni ninguna otra mención a preguntas.
- Sin pasos.
- **Notas:** *Tiempo objetivo: 0:10 (acumulado 18:55; quedan ~1:05 de margen).* Muchas gracias por su atención. (Anexos: el índice está en la diapositiva que sigue; cada anexo lleva su número en la etiqueta y en el pie.)

---

## Referencias cruzadas en los anexos
Con el nuevo orden cambian estas referencias a diapositivas principales:
- Anexo 7 («Todo se hizo en simulación exacta, a propósito»), notas: «(diapositiva 18)» → **«(diapositiva 20)»**.
- Anexo 27 («Resumen completo de resultados»), notas: «la de la diapositiva 15» → **«la de la diapositiva 17»**.
- Anexo 28 («Métricas de separabilidad con su significancia»), notas: «la diapositiva 11» se queda **igual** (sigue siendo la 11).
- Anexo 37 («Umbral α* de cada kernel»), notas: «la diapositiva 17» → **«la diapositiva 19»**.
- Anexo 45 («¿Un resultado negativo vale?…»), **texto visible** «diapositiva 16» → **«diapositiva 18»**.
- Revisa si alguna otra nota o texto menciona un número de diapositiva principal y ajústalo con la tabla de arriba.

## Comprobación final antes de exportar
- [ ] 23 diapositivas principales con contadores «n / 23» y los tiempos de la tabla.
- [ ] Portada y despedida: directores en dos renglones y logos al nuevo tamaño, sin encimarse con el título.
- [ ] Contexto: las tres barras dicen exactamente >99 %, 87 % y 33 %, con su fuente.
- [ ] Los círculos ① y ② de la pregunta van en línea antes de su frase, y las insignias aparecen exactamente en las diapositivas indicadas.
- [ ] La 11 ya no tiene el t-SNE encima; la 12 lo muestra sola, con las coordenadas del JSON.
- [ ] La 13 tiene el video `roc_umbral.mp4` con su texto alternativo «Video: …» y el último fotograma como imagen fija.
- [ ] La 22 ya no dice «Gracias · ¿Preguntas?»; la 23 no menciona preguntas.
- [ ] Las imágenes de los siete videos tienen un texto alternativo que empieza con «Video…»; ninguna otra imagen empieza así.
- [ ] Las referencias cruzadas de los anexos 7, 27, 37 y 45 apuntan a los números nuevos.
