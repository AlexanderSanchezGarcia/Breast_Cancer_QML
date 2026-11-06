# Ronda 8 · «Defensa TT 2026-B039»: tres índices después de «Gracias» y los cuadros del reporte como anexos

Esta ronda solo toca la sección de anexos. Tiene cuatro cambios:
1. **Tres índices** justo después de «Gracias»: respuestas (agrupadas por tema y redactadas como preguntas), figuras y tablas.
2. **Un bloque nuevo de anexos con los 36 cuadros (tablas) del reporte**, uno por diapositiva, como imagen, igual que las figuras.
3. Se quita el índice de figuras que hoy está a la mitad de los anexos (sustituido por el nuevo).
4. «Tabla 23» pasa a «Cuadro 23», que es como se llama en el reporte.

Las 23 diapositivas principales no cambian, salvo una frase en las notas de la 23 y el pie de la 17. **La numeración de los anexos 1 a 86 no cambia.** Los cuadros son los anexos 87 a 122 (ver la lista de abajo).

Los enlaces de los índices, el botón «↩ Índice» de cada anexo y los atajos de teclado **los añade el autor después de exportar, con un script**. No los dibujes. Sí respeta los formatos de texto de esta ronda, porque el script los usa para encontrar cada cosa:
- el `data-label` exacto de los tres índices;
- el formato «N · texto» de cada entrada;
- los títulos que empiezan con «Figura X.Y.Z ·» o «Cuadro N ·»;
- el pie «… Anexo N / 122».

**Importante sobre los videos:** no cambies el texto alternativo de las imágenes de los siete videos. Ninguna imagen nueva puede empezar con «Video».

---

## Orden nuevo del final del deck

| Diapositivas | Contenido |
|---|---|
| 1–23 | Parte principal, sin cambios |
| 24 | **Índice de respuestas** (sustituye a «Anexos») |
| 25 | **Índice de figuras** (sustituye a «Índice de figuras del reporte», que hoy está entre los anexos 50 y 51 y sale de ahí) |
| 26 | **Índice de tablas** (nuevo) |
| 27–76 | Anexos 1–50, sin cambios |
| 77–112 | Anexos 51–86, las figuras, sin cambios salvo el pie |
| 113–169 | **Anexos 87–122, los cuadros (nuevos): 57 diapositivas, porque 11 cuadros van en varias partes** |

- Los índices **no llevan número de anexo**.
- En el pie de todos los anexos, «Anexo N / 86» pasa a **«Anexo N / 122»**.

## Diseño común de los tres índices

- Etiqueta de sección: «Anexos». Título: «Índice de respuestas», «Índice de figuras» o «Índice de tablas». El `data-label` de cada diapositiva debe ser **exactamente** ese título.
- **Deja libre la esquina superior derecha** (unos 520 × 80 px a partir de x = 1280, y = 30): el script pone ahí tres fichas «Respuestas · Figuras · Tablas» para pasar de un índice a otro. Tampoco pongas ahí el mapa miniatura.
- **Cada entrada es un solo bloque de texto** que empieza con el número de anexo, un punto medio y el texto: «46 · ¿Por qué no una CNN?». El número en `CLASICO` (azul) y en negritas; el resto en `TINTA`. No separes el número del texto en dos bloques.
- Los títulos de grupo, en versalitas pequeñas grises (como las etiquetas de sección), **no** empiezan con número.
- Varias columnas, sin rejilla, letra de 18–20 px. Todo debe caber en una diapositiva sin cortar ninguna entrada.
- Pie: «TT 2026-B039 · ESCOM-IPN» a la izquierda y, a la derecha, «Tecla I: índices · número + Enter: ir al anexo».
- Sin pasos ni animaciones.
- Notas del orador de los tres: «Índice. Clic en una entrada para ir al anexo; desde cualquier anexo, el botón ↩ Índice regresa aquí. Tecla I para cambiar de índice; un número y Enter va directo a ese anexo.»

## 24 · Índice de respuestas

Siete grupos, en este orden y con estas entradas (el número es el del anexo, que no cambia):

**Pregunta y respuesta**
- 1 · ¿Qué hicieron los trabajos previos?
- 10 · ¿Cuál es la pregunta completa?
- 24 · ¿Cuál es la respuesta?

**Preguntas difíciles**
- 45 · ¿Vale un resultado negativo?
- 46 · ¿Por qué no una CNN?
- 47 · ¿Las intensidades no calibradas meten el efecto del digitalizador?
- 48 · ¿Cuánto se pierde al quedarse con 12 de 67 características?
- 49 · ¿El resultado se generaliza?
- 50 · ¿Cuándo valdría la pena el hardware?

**Fundamentos**
- 2 · ¿Qué es un qubit?
- 3 · ¿Qué es el entrelazamiento?
- 4 · ¿Qué hace un feature map?
- 5 · ¿Qué es un kernel y cómo separa una SVM?
- 6 · ¿Qué significa medir un qubit?
- 8 · ¿Qué mide el AUC-ROC?
- 9 · ¿Qué son las 67 características radiómicas?

**Diseño**
- 7 · ¿Por qué solo simulación sin ruido?
- 11 · ¿Por qué θ fijo?
- 12 · ¿Y si se entrenaba θ?
- 13 · ¿Cuáles son las tres arquitecturas?
- 14 · ¿Qué modelos se compararon y dónde?
- 15 · ¿Por qué 12 qubits? ¿Y con 8?
- 16 · ¿Por qué una sola repetición del circuito?
- 17 · ¿Por qué ángulos en [0, π] por cuantiles?
- 18 · ¿En qué se diferencian C4 y C5?
- 19 · ¿Para qué sirve C2?
- 20 · ¿Por qué 200 lesiones para la separabilidad?
- 21 · ¿Por qué 5 folds?

**Datos**
- 22 · ¿Qué se corrigió en las máscaras?
- 23 · ¿Hay pacientes a la vez en entrenamiento y prueba?
- 35 · ¿Por qué las masas separan menos con radiómica?

**Resultados**
- 25 · ¿Y las demás métricas de clasificación?
- 26 · ¿Con qué intervalos de confianza?
- 27 · ¿Dónde está el resumen completo (Cuadro 23)?
- 28 · ¿Son significativas las métricas de separabilidad?
- 29 · ¿Qué muestra el t-SNE?
- 30 · ¿Un QSVM lo haría mejor?
- 31 · ¿Se buscó la ventaja de forma justa?
- 32 · ¿La conclusión resiste cambios en θ, k y la muestra?
- 33 · ¿Separabilidad y clasificación ordenan igual?
- 34 · ¿Y si se reduce la escala de los ángulos?
- 36 · ¿Qué métricas de separabilidad se usaron?
- 37 · ¿Desde qué α aparece la ventaja?

**Fórmulas**
- 38 · La codificación
- 39 · Las dos lecturas
- 40 · Separabilidad: alineamiento, Fisher y Davies-Bouldin
- 41 · La diferencia geométrica y su cota
- 42 · Medición, disparos y parameter-shift
- 43 · Pérdida, AUC y Spearman
- 44 · Los kernels clásicos de referencia

Son 50 entradas, cada anexo exactamente una vez.

## 25 · Índice de figuras

Las 36 figuras de los anexos 51 a 86, en el orden del reporte, en cuatro grupos. Formato de cada entrada: «51 · Figura 3.4.1 · Geometría de los kernels clásico y cuántico». Usa los mismos títulos cortos de los anexos de figura que ya existen, sin el «(Huang et al., 2021)».
- **Marco teórico:** 51 (Fig. 3.4.1).
- **Datos y diseño:** 52–55 (Figs. 4.3.1 a 5.7.1).
- **Resultados:** 56–83 (Figs. 6.1.1 a 6.6.2).
- **Apéndice C:** 84–86 (Figs. C.1.1, C.1.2 y C.4.1).

## 26 · Índice de tablas

Los 36 cuadros, anexos 87 a 122, con el formato «87 · Cuadro 1 · Estado del arte». Primero los del trabajo y al final, en su propio grupo, los administrativos.

| Anexo | Cuadro | Título corto | p. del reporte | Grupo |
|---|---|---|---|---|
| 87 | 1 | Estado del arte | 48 | Marco y diseño |
| 88 | 2 | Tres formas de leer el estado | 77 | Marco y diseño |
| 89 | 3 | Composición del CBIS-DDSM | 78 | Marco y diseño |
| 90 | 4 | Del EDA a las decisiones de diseño | 86 | Marco y diseño |
| 91 | 5 | Clasificadores del trabajo | 89 | Marco y diseño |
| 92 | 9 | Las cinco condiciones (M5) | 101 | Marco y diseño |
| 93 | 10 | Diseño de los experimentos X1 a X11 | 108 | Marco y diseño |
| 94 | 11 | Las 12 características seleccionadas (M4) | 116 | Resultados |
| 95 | 12 | Separabilidad de los kernels (M6) | 121 | Resultados |
| 96 | 13 | Separabilidad de los embeddings (M6) | 123 | Resultados |
| 97 | 14 | Separabilidad con k = 12 y k = 8 | 127 | Resultados |
| 98 | 15 | Clasificación con el mismo MLP (M7) | 129 | Resultados |
| 99 | 16 | Diferencias pareadas de AUC (M7) | 130 | Resultados |
| 100 | 17 | Diez sorteos de θ | 132 | Resultados |
| 101 | 18 | θ entrenado frente a θ fijo | 134 | Resultados |
| 102 | 19 | Árboles y MLP sobre C1–C5 (X10) | 136 | Resultados |
| 103 | 20 | Tres lecturas del mapa ZZ | 143 | Resultados |
| 104 | 21 | De las etiquetas reales a las diseñadas (X11) | 144 | Resultados |
| 105 | 22 | Spearman entre separabilidad y clasificación (M8) | 145 | Resultados |
| 106 | 23 | Resumen de resultados por condición | 154 | Resultados |
| 107 | 24 | Mapa de las comparaciones | 155 | Resultados |
| 108 | 25 | Evidencia por objetivo específico | 157 | Resultados |
| 109 | 26 | Preprocesamiento y control de calidad (M2) | 192 | Apéndices |
| 110 | 27 | Características seleccionadas, conjunto completo (M4) | 193 | Apéndices |
| 111 | 28 | Características descartadas por redundancia (M4) | 194 | Apéndices |
| 112 | 29 | Balance por fold (M4) | 195 | Apéndices |
| 113 | 30 | Coste de los kernels cuánticos (M5) | 195 | Apéndices |
| 114 | 31 | Escalamiento con el número de qubits (OE-6) | 196 | Apéndices |
| 115 | 32 | Coste de los gradientes (X8) | 196 | Apéndices |
| 116 | 33 | Verificaciones automáticas | 197 | Apéndices |
| 117 | 34 | Auditoría independiente (X5) | 198 | Apéndices |
| 118 | 6 | Requerimientos funcionales | 90 | Administrativos |
| 119 | 7 | Requerimientos no funcionales | 93 | Administrativos |
| 120 | 8 | Fases CRISP-DM y módulos | 95 | Administrativos |
| 121 | 35 | Versiones de los paquetes | 211 | Administrativos |
| 122 | 36 | Índice de decisiones de la bitácora | 213 | Administrativos |

## Anexos 87–122 · un cuadro por diapositiva

Mismo formato que los anexos de figura:
- Etiqueta de sección: «Anexo N».
- Título: **«Cuadro C · título corto»**, con el título de la tabla de arriba (por ejemplo «Cuadro 12 · Separabilidad de los kernels (M6)»). El `data-label` debe empezar igual, con «Cuadro C ·».
- Un marco de imagen vacío que ocupe todo el espacio disponible, centrado, `contain`, fondo blanco. **El autor lo llena con su script**; no hace falta que adjuntes nada.
- Pie: «Reporte técnico, p. P · Anexo N / 122».
- **Deja libre una franja abajo al centro** (unos 220 × 50 px, centrada, con el borde inferior a ~30 px del borde de la diapositiva): ahí el script pone el botón «↩ Índice». Esto vale para **todos** los anexos, 1 a 122. Si algún anexo actual tiene contenido en esa zona, súbelo un poco.
- Sin animaciones. Notas del orador: «Cuadro C del reporte, p. P».
- **Cuadros en varias diapositivas.** Los que no caben legibles en una diapositiva van en varias partes, cortadas entre filas. Cada parte es su propia diapositiva, con el título «Cuadro C · título corto (parte k de n)». Todas las partes de un cuadro llevan **el mismo número de anexo** y van seguidas. En el índice de tablas el cuadro aparece **una sola vez**.

| Anexo | Cuadro | Partes | p. del reporte (pie) |
|---|---|---|---|
| 90 | 4 | 2 | 86 |
| 91 | 5 | 2 | 89 |
| 93 | 10 | 2 | 108 |
| 99 | 16 | 2 | 130 |
| 106 | 23 | 2 | 154 |
| 107 | 24 | 2 | 155 |
| 108 | 25 | 2 | 157 |
| 117 | 34 | 2 | 198 |
| 118 | 6 | 7 | 90–93 |
| 119 | 7 | 3 | 93–94 |
| 122 | 36 | 6 | 213–215 |

  Los demás cuadros van en una sola diapositiva. En total, los cuadros ocupan **57 diapositivas** (anexos 87 a 122), y el deck queda en **169 diapositivas**.

## Otros cambios
- **23 · Gracias**, notas: sustituye «(Anexos: el índice está en la diapositiva que sigue; cada anexo lleva su número en la etiqueta y en el pie.)» por «(Anexos: siguen tres índices, de respuestas, figuras y tablas. Tecla I para ir a los índices; un número y Enter va directo a ese anexo.)».
- **17 · Resumen**, pie: «Tabla 23 del reporte (versión completa en anexos)» pasa a «Cuadro 23 del reporte (versión completa en el Anexo 27)».
- **Anexo 27**: en el título y en las notas, «Tabla 23» pasa a «Cuadro 23».

## Comprobación final antes de exportar
- [ ] Los índices son las diapositivas 24, 25 y 26, con `data-label` exactamente «Índice de respuestas», «Índice de figuras» e «Índice de tablas».
- [ ] Ya no existe el índice «Anexos» viejo ni el «Índice de figuras del reporte» entre los anexos 50 y 51.
- [ ] Cada entrada de índice es un solo bloque «N · texto». El índice de respuestas tiene 50 entradas, el de figuras 36 y el de tablas 36.
- [ ] Los anexos 1–86 conservan su número; los cuadros son 87–122, en el orden de la tabla, con las partes indicadas (57 diapositivas, 169 en total).
- [ ] Todos los pies dicen «Anexo N / 122».
- [ ] La esquina superior derecha de los índices y la franja inferior central de los anexos están libres.
- [ ] Las imágenes de los siete videos conservan su texto alternativo, que empieza con «Video…».
