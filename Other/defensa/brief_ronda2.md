# Ronda 2 · cambios a «Defensa TT 2026-B039»

La versión que exportaste está muy bien: contenido, cifras, colores y el mapa de calor son correctos. Esta ronda añade **una diapositiva nueva** y ajusta **cuatro animaciones**. Las reglas generales del primer brief siguen vigentes.

**Sobre tus notas de la ronda anterior:**
- **Diapositiva 4, la cuadrícula:** déjala como está, todas las etapas en un solo clic. No vale la pena añadir cinco clics para esto.
- **Las líneas de X11:** como el editor no tiene un efecto de trazado, divide cada curva en dos tramos que entren en pasos distintos (abajo, en la diapositiva 14). Con eso basta.
- **Diapositiva 5:** tu suposición es correcta. Los «8 pasos» eran los 8 estados.
- **R8:** estática está bien.

## Nuevo orden

Entra una diapositiva entre la actual 12 («La pérdida está en la lectura…») y la actual 13 (X11). La parte principal pasa de 16 a **17 diapositivas**; actualiza los contadores a «n / 17».

| # | Diapositiva | Tiempo (acumulado) |
|---|---|---|
| 1–12 | Sin cambios | igual (12:45) |
| 13 | **NUEVA** · La ventaja cuántica sí existe | 1:00 (13:45) |
| 14 | X11, la curva de transición (antes 13) | 1:30 (15:15) |
| 15 | Viabilidad (antes 14) | 1:15 (16:30) |
| 16 | Respuesta (antes 15) | 1:15 (17:45) |
| 17 | Limitaciones y trabajo futuro (antes 16) | 0:40 (18:25) |

Actualiza el «Tiempo objetivo» y el «acumulado» de las notas 13 a 17 con esta tabla. La nota de la 17 debe decir «quedan ~1:35 de margen».

---

## 13 · NUEVA · «La ventaja cuántica sí existe: Huang et al. la construyeron y aquí se reproduce»
Etiqueta de sección: «03 · Resultados».

**Contenido**, en tres bloques de izquierda a derecha:

1. **Tarjeta «Huang et al. (2021)»**, con el estilo de las tarjetas claras del deck:
   - «Con etiquetas diseñadas para seguir la geometría del circuito, los kernels cuánticos proyectados superan a todos los modelos clásicos probados.»
   - Debajo, en pequeño: «la ventaja sigue a *g* y supera el 20 % en los sistemas más grandes · *Nature Communications* 12, 2631 (2021)».
2. **El dibujo de los dos libros** (el que hoy está al final de la diapositiva X11; muévelo aquí): «libro clásico», «libro del circuito» y una hoja de examen con todas las preguntas del color del libro del circuito. Texto de apoyo: «tarea diseñada: todas las preguntas salen del libro del circuito».
3. **Gráfica de barras «Mismas lesiones y mismas 12 características, etiquetas diseñadas»**, con el estilo de la antigua diapositiva del control positivo. Un grupo por subconjunto y, en cada grupo, una barra naranja «kernel cuántico proyectado (QSVM)» y una azul «mejor clásico (12 SVM y 4 XGBoost)»:

   | | Cuántico | Mejor clásico | Diferencia [IC 95 %] |
   |---|---|---|---|
   | Masas | 0.998 | 0.857 | +0.141 [0.119, 0.163] |
   | Calcificaciones | 0.994 | 0.876 | +0.118 [0.100, 0.140] |

   Eje Y: «AUC-ROC (validación cruzada)», de 0 a 1.

Debajo de la gráfica, en pequeño: «Con el kernel de fidelidad de C4 la ventaja es pequeña (+0.035 y +0.024): su *g* es pequeña, como anticipan Huang et al.»

Pie, en pequeño: «Etiquetado diseñado según Huang et al. (2021), sección 7 del suplemento. Huang et al. miden exactitud de predicción; aquí, AUC-ROC en validación cruzada sobre el entrenamiento. No usa el conjunto de prueba.»

Frase final, en negritas: «**La pregunta deja de ser si la ventaja existe y pasa a ser si el diagnóstico es una de esas tareas.**»

**Pasos:**
1. Título y tarjeta de Huang et al.
2. *(paso)* El dibujo de los libros.
3. *(paso)* Las barras de masas.
4. *(paso)* Las barras de calcificaciones y la nota de C4.
5. *(paso)* La frase final.

**Notas:** *Tiempo objetivo: 1:00 (acumulado 13:45).* Que aquí no haya ventaja no quiere decir que la ventaja cuántica no exista. Huang et al. mostraron cómo construirla: diseñaron etiquetas que siguen la geometría del circuito, y con ellas los kernels cuánticos proyectados superaron a todos los modelos clásicos que probaron, por más de un 20 % en los sistemas más grandes. Ellos mismos aclaran que es una tarea diseñada y que falta encontrar casos de uso en datos de interés práctico. Es como un examen redactado con el libro que estudió el circuito: quien estudió ese libro gana. Repetimos esa construcción sobre nuestras mismas lesiones y nuestras mismas 12 características, y la ventaja aparece: 0.998 contra 0.857 en masas y 0.994 contra 0.876 en calcificaciones, aun dejando que el lado clásico elija entre 16 modelos, XGBoost incluido. Con el kernel de fidelidad de C4 la ventaja es pequeña, porque su *g* es pequeña, que es lo que predice la teoría. Así que el método sí detecta una ventaja cuando existe. La pregunta pasa a ser si el diagnóstico benigno o maligno es una de esas tareas, y eso es lo que mide la siguiente gráfica.

---

## 14 · X11, la curva de transición (antes 13) · cambiar los pasos

El dibujo de los libros pasa a la diapositiva 13. Aquí queda una versión pequeña (los dos libros y la hoja, ahora con **algunas** preguntas del color del libro del circuito), con el texto de apoyo «α = cuántas preguntas salen del libro del circuito».

**Hoy** las dos curvas aparecen completas en un solo paso y los libros salen al final, cuando el eje X ya se mostró sin explicación. **Nuevo orden:**
1. El dibujo pequeño de los libros, que define α.
2. *(paso)* Ejes y los dos puntos de α = 0, con «diagnóstico real».
3. *(paso)* Las dos curvas solo de α = 0 a α = 0.3: el clásico va delante o empatado.
4. *(paso)* Las dos curvas de α = 0.4 a α = 1, con «tarea diseñada» en el extremo: el cuántico se despega.
5. *(paso)* La zona sombreada α ≥ 0.4, con «α* = 0.4» y «ventaja cuántica (IC 95 % > 0)».
6. *(paso)* La llave «distancia del diagnóstico a la zona de ventaja».
7. *(paso)* La tabla de umbrales α* y «el diagnóstico real está en α = 0».

Cada curva se divide en dos tramos (dos trazados distintos, que se tocan en α = 0.3–0.4) para que los pasos 3 y 4 los muestren por separado con un fundido.

**Notas:** *Tiempo objetivo: 1:30 (acumulado 15:15).* Quita del principio la frase «La pregunta natural es: ¿hay algún caso en el que lo cuántico gane? Sí, y lo medimos sobre estas mismas lesiones», porque eso ya lo dijo la diapositiva 13. Empieza así: «Ahora mezclamos las dos tareas: α es la fracción de lesiones que toma la etiqueta diseñada; el resto conserva su diagnóstico real.» El resto de la nota se queda igual.

---

## 16 · Respuesta (antes 15) · punto 4

Sustituye el punto 4 por: «La ventaja cuántica sí existe con etiquetas diseñadas (Huang et al.), y aparece cuando el 40–70 % de las etiquetas sigue la geometría del kernel cuántico; el diagnóstico real está en el 0 %.»

En las notas, el punto cuatro se lee así: «Cuatro: la ventaja cuántica sí existe, y el método la detecta: con las etiquetas diseñadas de Huang et al. el kernel proyectado gana con claridad. Aparece cuando entre el 40 y el 70 % de las etiquetas sigue la geometría del circuito, y el diagnóstico real está en el 0 %.»

---

## Otras animaciones

### 4 · El qubit
- **La flecha hoy salta:** una se apaga y aparece otra (polo → ecuador → giro). Si la herramienta lo permite, divide la diapositiva en tres copias idénticas unidas por una transición *magic move*, para que la flecha rote de forma continua. Si no, deja la posición anterior de la flecha como una estela tenue, con 25 % de opacidad, para que se vea el recorrido.
- En el ecuador, etiqueta el punto de llegada como `|+⟩`, igual que en R3.
- La cuadrícula se queda como está (ver tus notas).

### 6 · Pipeline
- Hoy no tiene animación. Que entre en **tres clics**, siguiendo lo que voy explicando:
  1. M1 y M2, con la galería de imágenes: los datos y el recorte.
  2. *(paso)* M3 y M4: las 67 características y la selección de 12.
  3. *(paso)* M5 y M6–M8, con el recuadro inferior: las cinco condiciones y la evaluación.

### 15 · Viabilidad (antes 14)
- La cuadrícula de 1,024 puntos se ve muy tenue y en un proyector se perdería. Oscurece los puntos grises un 30 % para que los dos puntos naranjas resalten.

---

## Una corrección de texto
- **Nota de la portada:** «Buenos días» → «**Buenas tardes**». La presentación es a las 16:00.

## Comprobación final antes de exportar
- [ ] 17 diapositivas principales y 10 respaldos, con contadores correctos.
- [ ] Tiempos de las notas 13 a 17 según la tabla de arriba.
- [ ] Los libros grandes en la 13 y los pequeños en la 14; en la 14 ya no salen al final.
- [ ] En la diapositiva 13, Huang et al. aparecen como quienes construyen la ventaja, sin atribuirles nada sobre datos clínicos.
- [ ] Ninguna cifra distinta de las de este documento y del primer brief.
- [ ] Todas las animaciones avanzan con la flecha; ninguna es automática.
