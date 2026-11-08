# Ronda 9 · «Defensa TT 2026-B039»: el primer índice, por título y por tema, y una aclaración en la diapositiva 20

Esta ronda tiene tres cambios pequeños:
1. El índice de la diapositiva 24 pasa a llamarse **«Índice de anexos»**. Sus entradas son **títulos**, no preguntas, y se agrupan **por tema**. Desaparece el grupo «Preguntas difíciles».
2. En la diapositiva 20, el rótulo «Kernel 200×200» se aclara.
3. Dos frases de notas que mencionaban el «índice de respuestas».

Todo lo demás se queda igual: los números de anexo, los otros dos índices, los cuadros y las 169 diapositivas. Las reglas de las rondas anteriores siguen vigentes; en particular, cada entrada de índice es **un solo bloque de texto «N · título»** y no se dibujan enlaces ni botones (los pone el script del autor).

**Importante sobre los videos:** no cambies el texto alternativo de las imágenes de los siete videos.

---

## 24 · «Índice de anexos» (antes «Índice de respuestas»)

- Título visible y `data-label`: exactamente **«Índice de anexos»**.
- Mismo diseño que hoy: etiqueta «Anexos», varias columnas, títulos de grupo en versalitas grises sin número, entradas «N · título» con el número en `CLASICO` y negritas, esquina superior derecha libre y el mismo pie.
- Ocho grupos, en este orden. Son 50 entradas y cada anexo aparece exactamente una vez:

**Planteamiento y respuesta**
- 1 · Estado del arte: tabla completa
- 10 · Pregunta de investigación completa
- 24 · Respuesta a la pregunta

**Fundamentos**
- 2 · Qubit: superposición de 0 y 1
- 3 · Entrelazamiento
- 4 · Feature map: de vector a estado
- 5 · Kernel y SVM
- 6 · Medición de un qubit
- 8 · AUC-ROC

**Datos y características**
- 9 · Las 67 características radiómicas
- 22 · Corrección de las 80 máscaras
- 23 · Particiones por paciente
- 35 · Masas frente a calcificaciones
- 48 · Selección de 12 de 67 características

**Diseño del circuito**
- 11 · θ fijo: justicia, pregunta y costo
- 12 · θ entrenado
- 13 · Las tres arquitecturas
- 15 · Número de qubits: 12 y 8
- 16 · Repeticiones del circuito
- 17 · Ángulos en [0, π] por cuantiles
- 18 · C4 frente a C5

**Diseño experimental**
- 7 · Simulación exacta, sin ruido
- 14 · Modelos comparados
- 19 · C2, control nulo
- 20 · Separabilidad sobre 200 lesiones
- 21 · Número de folds
- 46 · Descarte de una CNN

**Resultados**
- 25 · Métricas de clasificación en prueba
- 26 · AUC con intervalos de confianza
- 27 · Resumen completo (Cuadro 23)
- 28 · Significancia de la separabilidad
- 29 · t-SNE
- 30 · QSVM frente a SVM clásico
- 31 · Búsqueda simétrica de ventaja
- 32 · Robustez: θ, k y muestra
- 33 · Separabilidad y clasificación (Spearman)
- 34 · Escala de los ángulos
- 36 · Métricas de separabilidad
- 37 · Umbral α* de cada kernel

**Alcance y limitaciones**
- 45 · Valor de un resultado negativo
- 47 · Intensidades no calibradas
- 49 · Generalización
- 50 · Cuándo convendría el hardware

**Fórmulas**
- 38 · Codificación
- 39 · Las dos lecturas
- 40 · Alineamiento, Fisher y Davies-Bouldin
- 41 · Diferencia geométrica y su cota
- 42 · Medición, disparos y parameter-shift
- 43 · Pérdida, AUC y Spearman
- 44 · Kernels clásicos de referencia

- **Notas** de la 24, la 25 y la 26: «Índice. Clic en una entrada para ir al anexo; desde cualquier anexo, el botón ↩ Índice regresa aquí. Tecla I para cambiar de índice; un número y Enter va directo a ese anexo.» (sin cambio).

## 20 · «Simular cabe; medir en hardware sería el problema»: aclarar el kernel

- En la gráfica de barras, el rótulo **«Kernel 200×200»** pasa a **«Kernel entre 200 lesiones · 19,900 pares»**. Si no cabe en un renglón, en dos: «Kernel entre 200 lesiones» y, debajo y más pequeño, «19,900 pares». El valor de la barra («hasta ~22 qubits») no cambia.
- **Notas:** después de la primera frase añade: «El kernel de 200 lesiones es la matriz de parecidos de la diapositiva de separabilidad: 200 por 200 valores, de los cuales 19,900 son pares distintos, y en hardware cada par es un circuito.» El resto de las notas, igual.

## 23 · Gracias, notas
- «(Anexos: siguen tres índices, de respuestas, figuras y tablas. …)» pasa a «(Anexos: siguen tres índices, de anexos, figuras y tablas. …)». El resto, igual.

## Comprobación final antes de exportar
- [ ] La diapositiva 24 se llama «Índice de anexos», también en su `data-label`.
- [ ] Ocho grupos, sin «Preguntas difíciles»; 50 entradas «N · título», sin signos de interrogación; cada anexo una sola vez.
- [ ] El rótulo de la diapositiva 20 dice «Kernel entre 200 lesiones · 19,900 pares».
- [ ] Siguen siendo 169 diapositivas y las imágenes de los siete videos conservan su texto alternativo «Video…».
