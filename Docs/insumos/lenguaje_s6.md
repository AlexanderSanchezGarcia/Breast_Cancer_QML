# Auditoría de lenguaje calibrado · Capítulo 6 (Resultados)

Este documento contiene la revisión crítica de estilo y calibración epistémica sobre los archivos de `Docs/capitulos/6_Resultados/`. Conforme a las reglas metodológicas del proyecto (Regla 1 de `CLAUDE.md` y `reglas.md`), los resultados deben presentarse en lenguaje estrictamente calibrado: descriptivo («muestra», «indica», «es consistente con», «sugiere») frente a evidencia observacional, reservando «demuestra» o «confirma» únicamente para derivaciones formales o pruebas de hipótesis estadísticamente significativas. Se identifican a continuación las frases que sobreafirman respecto a lo que sus datos respaldan, señalando el archivo, la línea, la cita literal, la justificación cuantitativa del exceso y una propuesta de redacción calibrada. Conforme a las instrucciones, estas frases no han sido modificadas en los archivos `.tex` existentes para preservar la integridad del texto original hasta la revisión final del autor.

---

## 1. `6.1_datos_caracteristicas.tex`

### Caso 1.1

- **Archivo:** `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex`
- **Línea:** 29
- **Frase literal:**
  > «La distancia del píxel descartado más lejano al borde de la componente mayor presentó una mediana de 3.6 píxeles, un percentil 99 de 9.2 píxeles y un máximo de 14 píxeles, confirmando que las islas corresponden a artefactos inmediatos al contorno.»
- **Por qué sobreafirma:** El verbo «confirmando» establece una conclusión categórica y causal sobre la naturaleza física del hallazgo. La proximidad geométrica de los píxeles descartados (mediana de 3.6 px, máximo 14 px) es consistente con artefactos de segmentación o digitalización, pero no descarta de forma analítica que pudieran corresponder a microestructuras biológicas o calcificaciones adyacentes.
- **Propuesta de redacción:**
  > «La distancia del píxel descartado más lejano al borde de la componente mayor presentó una mediana de 3.6 píxeles, un percentil 99 de 9.2 píxeles y un máximo de 14 píxeles, lo que resulta consistente con la hipótesis de que las islas corresponden  a artefactos periféricos inmediatos al contorno.»

---

### Caso 1.2

- **Archivo:** `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex`
- **Línea:** 34
- **Frase literal:**
  > «...la evaluación univariante mediante la distancia estandarizada de Cohen ($|d|$) evidenció que las calcificaciones constituyen el subconjunto con mayor separabilidad individual.»
- **Por qué sobreafirma:** El verbo «evidenció» otorga carácter demostrativo definitivo a un cálculo univariante descriptivo sobre el conjunto de entrenamiento. La métrica $|d|$ muestra que en este conjunto de datos y bajo estas 67 características radiómicas específicas las calcificaciones alcanzan mayores tamaños de efecto univariante (máximo de 0.82 frente a 0.50 en masas), pero no demuestra una propiedad intrínseca universal de la patología ni evalúa separabilidad multivariante.
- **Propuesta de redacción:**
  > «...la evaluación univariante mediante la distancia estandarizada de Cohen ($|d|$) mostró que, en las características extraídas para este conjunto de entrenamiento, las calcificaciones alcanzan tamaños de efecto individual superiores a los de las masas.»

---

## 2. `6.2_separabilidad.tex`

### Caso 2.1

- **Archivo:** `Docs/capitulos/6_Resultados/6.2_separabilidad.tex`
- **Línea:** 117
- **Frase literal:**
  > «Las métricas de C1 y C2 coincidieron con discrepancias menores a $10^{-14}$, confirmando la validez del control nulo ante rotaciones ortogonales.»
- **Por qué sobreafirma:** El uso de «confirmando la validez» formula como hallazgo empírico lo que en realidad es una identidad matemática exacta: PCA ($k \to k$) es una rotación ortogonal que por definición preserva distancias euclidianas y dispersiones espaciales. La discrepancia inferior a $10^{-14}$ es únicamente verificación de precisión numérica de punto flotante en la computadora, no una confirmación metodológica sustantiva.
- **Propuesta de redacción:**
  > «Las métricas de C1 y C2 coincidieron con discrepancias numéricas del orden del límite de precisión  ($< 10^{-14}$), lo cual concuerda con la invarianza teórica de las distancias y dispersiones ante rotaciones ortogonales bajo la condición de control nulo.»

---

## 3. `6.3_clasificacion.tex`

### Caso 3.1

- **Archivo:** `Docs/capitulos/6_Resultados/6.3_clasificacion.tex`
- **Línea:** 16
- **Frase literal:**
  > «El control nulo confirma la consistencia del procedimiento: la diferencia pareada entre C2 y C1 en el conjunto de prueba es de $-0.011$ [$-0.061$, $0.038$] ($p = 0.659$) en masas y de $0.020$ [$-0.026$, $0.067$] ($p = 0.377$) en calcificaciones.»
- **Por qué sobreafirma:** El verbo «confirma» interpreta erróneamente la no significancia estadística ($p = 0.659$ y $p = 0.377$) como una prueba positiva de igualdad o consistencia. En inferencia estadística clásica, un valor de $p > 0.05$ representa únicamente la no existencia de evidencia suficiente para rechazar la hipótesis nula, no su confirmación afirmativa.
- **Propuesta de redacción:**
  > «El comportamiento del control nulo resulta consistente con lo esperado: las diferencias pareadas entre C1 y C2 en el conjunto de prueba ($-0.011$ con $p = 0.659$ en masas y $0.020$ con $p = 0.377$ en calcificaciones) no resultan estadísticamente distinguibles de cero, mostrando que la rotación ortogonal no introduce alteraciones medibles en la capacidad de clasificación del modelo.»

---

### Caso 3.2

- **Archivo:** `Docs/capitulos/6_Resultados/6.3_clasificacion.tex`
- **Línea:** 40
- **Frase literal:**
  > «El análisis de sensibilidad confirma que este resultado es robusto frente a variaciones en el procedimiento de entrenamiento.»
- **Por qué sobreafirma:** El verbo «confirma» generaliza en exceso la evidencia observada en un barrido discreto de parámetros. Explorar cinco semillas de red, dos variantes de tamaño de capa y dos regímenes de épocas muestra estabilidad en el rango específico evaluado, pero no permite afirmar de forma absoluta la invarianza universal del resultado.
- **Propuesta de redacción:**
  > «El análisis de sensibilidad indica que la brecha observada entre condiciones clásicas y cuánticas se mantiene estable ante las variaciones evaluadas en la inicialización estocástica, la arquitectura de capas y el régimen de épocas de entrenamiento.»

---

### Caso 3.3

- **Archivo:** `Docs/capitulos/6_Resultados/6.3_clasificacion.tex`
- **Línea:** 43
- **Frase literal:**
  > «En este régimen de $k = 8$, las condiciones cuánticas se ubican entre 0.07 y 0.19 por debajo de C1 en el conjunto de prueba, evidenciando que un espacio de estados más disperso no se traduce necesariamente en mayor separabilidad clasificatoria.»
- **Por qué sobreafirma:** El participio «evidenciando» presenta una inferencia inductiva como demostración formal. El hecho de que a $k = 8$ la dispersión de $\langle Z_i \rangle$ aumente (de 0.058 a 0.099 en C4 masas) mientras que el AUC de prueba desciende (a 0.561 en calcificaciones) sugiere que dispersión no equivale a separabilidad diagnóstica, pero no descarta que con otros clasificadores o arquitecturas pudiera existir traslación.
- **Propuesta de redacción:**
  > «En este régimen de $k = 8$, las condiciones cuánticas se ubican entre 0.07 y 0.19 por debajo de C1 en el conjunto de prueba, lo cual es consistente con la observación de que una mayor dispersión geométrica en el espacio de expectativas no garantiza una mejora en la capacidad de discriminación del clasificador supervisado.»

---

## 4. `6.4_qsvm_ventaja.tex`

### Caso 4.1

- **Archivo:** `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex`
- **Línea:** 13
- **Frase literal:**
  > «Esta evidencia demuestra que la codificación cuántica en el espacio de Hilbert preserva prácticamente la totalidad de la información diagnóstica; la degradación ocurre en la etapa de lectura al proyectar un estado de 4,096 amplitudes complejas en solo 12 valores esperados locales tras un circuito variacional fijo.»
- **Por qué sobreafirma:** Doble sobreafirmación severa:
  1. «demuestra que... preserva prácticamente la totalidad»: Que el QSVM sobre el núcleo de C4 obtenga un AUC de 0.628 en masas y 0.759 en calcificaciones (a $-0.02$ y $-0.01$ del SVM RBF clásico) no es una demostración matemática de que se preserve «la totalidad de la información», sino una equivalencia empírica de desempeño puntual sobre este conjunto de prueba.
  2. Afirmación causal categórica sin aislamiento experimental estricto («la degradación ocurre en la etapa de lectura al proyectar...»): Si bien la proyección de $2^{12}$ amplitudes a 12 expectativas $\langle Z_i \rangle$ implica una reducción drástica de dimensión, la diferencia de rendimiento entre QSVM y MLP también involucra la naturaleza del algoritmo clasificador (SVM basado en márgenes sobre vectores de soporte frente a MLP optimizado por descenso de gradiente) y la elección de los parámetros $\boldsymbol\theta$.
- **Propuesta de redacción:**
  > «Esta comparación sugiere que la codificación en el núcleo cuántico retiene un nivel de información diagnóstica comparable al del núcleo clásico en la muestra evaluada, mientras que la formulación basada en expectativas locales $\langle Z_i \rangle$ bajo la Arquitectura~B presenta una capacidad de generalización marcadamente inferior al ser procesada por el perceptrón multicapa.»

---

### Caso 4.2

- **Archivo:** `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex`
- **Línea:** 39
- **Frase literal:**
  > «...confirmando que una separación geométrica elevada es condición necesaria pero no suficiente para obtener ventaja en generalización.»
- **Por qué sobreafirma:** El gerundio «confirmando» trata el resultado empírico como una demostración formal de un principio teórico. La necesidad matemática de $g \gg 1$ es un teorema probado formalmente por Huang et al. (2021); el hecho empírico de que los núcleos proyectados alcancen $g \in [6, 9]$ y fracasen en clasificación clínica ilustra la no-suficiencia de dicha métrica en este problema específico, pero un experimento particular no «confirma» una condición lógica universal.
- **Propuesta de redacción:**
  > «...lo cual concuerda con el marco teórico de Huang et al. \\cite{huang2021power}, que establece que una diferencia geométrica elevada constituye una condición necesaria pero no suficiente para alcanzar ventaja en generalización.»

---

### Caso 4.3

- **Archivo:** `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex`
- **Línea:** 52
- **Frase literal:**
  > «Este contraste experimental demuestra que la ausencia de ventaja cuántica observada en este estudio es una propiedad de estas etiquetas diagnósticas clínicas al combinarse con estas 12 características radiómicas y estas familias de kernels cuánticos evaluadas... y no una limitación del protocolo experimental.»
- **Por qué sobreafirma:** «demuestra que... es una propiedad de estas etiquetas... y no una limitación del protocolo». El contraste con etiquetas sintéticas construidas según el Apéndice G de Huang et al. (donde el QSVM proyectado alcanza AUC $> 0.99$ frente a $0.80$--$0.82$ clásico) es una prueba metodológica de control positivo muy valiosa, pero no constituye una demostración deductiva estricta de que la ausencia de ventaja sea exclusivamente una propiedad ontológica de las etiquetas reales.
- **Propuesta de redacción:**
  > «Este contraste experimental proporciona evidencia sólida de que la ausencia de ventaja cuántica observada se vincula a la falta de alineación entre las etiquetas diagnósticas clínicas reales, las 12 características radiómicas seleccionadas y las familias de núcleos cuánticos evaluadas, respaldando la capacidad del protocolo experimental para detectar ventajas cuando los datos se alinean con la geometría del espacio de Hilbert.»

---

## 5. `6.5_comparacion.tex`

### Caso 5.1

- **Archivo:** `Docs/capitulos/6_Resultados/6.5_comparacion.tex`
- **Línea:** 16
- **Frase literal:**
  > «Al considerar el análisis de sensibilidad exhaustivo sobre los 48 coeficientes de correlación calculados... la totalidad de los valores se mantiene estrictamente positiva en el rango de 0.67 a 0.97. En todas las instancias evaluadas, los ordenamientos sitúan sin excepción al bloque de las tres condiciones clásicas (C1, C2 y C3) por delante del bloque de representaciones cuánticas (C4 y C5).»
- **Por qué sobreafirma:**
  1. «estrictamente positiva»: El énfasis absoluto es innecesario y oculta la falta de significancia estadística en gran parte de los coeficientes: con $n = 5$ condiciones y empates estructurales (C1 y C2), coeficientes como $\rho_s = 0.718$ ($p = 0.167$) y $\rho_s = 0.667$ ($p = 0.267$) distan de alcanzar el umbral convencional de significancia ($p < 0.05$).
  2. «sin excepción»: El uso de «sin excepción» convierte una regularidad empírica muestral sobre 48 combinaciones en una afirmación de universalidad categórica.
- **Propuesta de redacción:**
  > «En el análisis de sensibilidad sobre los 48 coeficientes de correlación de Spearman calculados, los valores observados resultaron sistemáticamente positivos (en el rango de 0.67 a 0.97), situando en todas las combinaciones analizadas a las tres condiciones clásicas (C1, C2 y C3) por delante de las representaciones cuánticas (C4 y C5), si bien debe tenerse en cuenta que en muestras pequeñas varios de estos coeficientes individuales presentan valores de $p$ que superan el umbral de 0.05.»

---

### Caso 5.2

- **Archivo:** `Docs/capitulos/6_Resultados/6.5_comparacion.tex`
- **Línea:** 16
- **Frase literal:**
  > «Estos resultados confirman que las métricas de separabilidad geométrica reflejan adecuadamente la capacidad clasificatoria ulterior, evidenciando de manera coherente la ausencia de beneficio clasificatorio derivado de la transformación cuántica.»
- **Por qué sobreafirma:** Cuádruple acumulación de verbos y adverbios de certeza excesiva: «confirman», «reflejan adecuadamente», «evidenciando» y «de manera coherente». Como se documenta en D-039 y H-049, la correlación de Spearman se reporta de forma **descriptiva** precisamente porque con $n = 5$ y empates solo un acuerdo perfecto alcanza $p < 0.05$. Declarar que «confirman» y «evidencian de manera coherente» contradice la naturaleza descriptiva estipulada en la metodología.
- **Propuesta de redacción:**
  > «Estos resultados muestran una coherencia descriptiva entre el ordenamiento espacial de separabilidad y el rendimiento del clasificador supervisado, siendo consistentes con la ausencia de mejoras diagnósticas derivadas de las transformaciones cuánticas analizadas.»

---

### Caso 5.3

- **Archivo:** `Docs/capitulos/6_Resultados/6.5_comparacion.tex`
- **Línea:** 36
- **Frase literal:**
  > «...demostrando que la asimetría observada entre patologías obedece a la señal radiómica clásica y no al comportamiento del circuito cuántico.»
- **Por qué sobreafirma:** Atribución causal concluyente («demostrando que... obedece a... y no a...»). El hecho de que la brecha cuántico-clásica sea similar en masas ($-0.12$) y calcificaciones ($-0.14$), y que las medianas del núcleo cuántico sean análogas en ambos subconjuntos, apoya la interpretación de que la dificultad diferencial reside en las características radiómicas clínicas, pero no constituye una demostración causal exhaustiva.
- **Propuesta de redacción:**
  > «...lo que indica que la asimetría de dificultad diagnóstica observada entre masas y calcificaciones se vincula primordialmente a la estructura de las variables radiómicas extraídas y no a una disparidad en la respuesta del circuito cuántico.»

---

## 6. `6.6_restricciones_simulador.tex`

### Caso 6.1

- **Archivo:** `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex`
- **Línea:** 13
- **Frase literal:**
  > «El factor que condicionó de forma determinante el diseño experimental no fue el número de qubits disponibles para almacenar el estado ($k = 12$ se sitúa holgadamente por debajo del límite de 25--26 qubits), sino el cálculo de gradientes.»
- **Por qué sobreafirma:** «condicionó de forma determinante». Aunque el cálculo de gradientes analíticos por *parameter-shift* representaba un coste prohibitivo (~~205 h a~~ $k=12$ ~~para 50 épocas), la elección de~~ $k=12$ ~~y de la Arquitectura~~B también obedeció a consideraciones de diversidad de familias radiómicas (evitar excluir textura, H-024/H-026) y a la validez interna de evaluar representaciones no sesgadas por optimización supervisada (D-014).
- **Propuesta de redacción:**
  > «Entre los factores computacionales evaluados, el cuello de botella más restrictivo para el diseño experimental no provino del número de qubits requeridos para almacenar el vector de estado ($k = 12$ se ubica por debajo del límite práctico de 25--26 qubits), sino del coste temporal del cálculo de gradientes mediante la regla de desplazamiento de parámetros.»

---

### Caso 6.2

- **Archivo:** `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex`
- **Línea:** 26
- **Frase literal:**
  > «La concentración que deja al kernel sin información de clase es la misma propiedad que impide estimarlo con un número realista de disparos.»
- **Por qué sobreafirma:** La frase «deja al kernel sin información de clase» es empíricamente inexacta. En el Módulo 6 (H-038, H-039) y en X2 (H-036) se demostró que a $c = 1$ el exceso de KTA en C4 y C5 es estadísticamente significativo ($0.003$ a $0.007$, con $p \le 0.003$), y el AUC de pares se ubica entre 0.508 y 0.547 ($p \le 0.047$). El núcleo conserva información de clase, aunque residual y cuantitativamente inferior al RBF clásico (exceso de 0.049 a 0.151). Decir que queda «sin información» sobreafirma en sentido negativo.
- **Propuesta de redacción:**
  > «La concentración exponencial del espacio de estados, que reduce parcialmente la diferenciación de clase en el núcleo cuántico a escala nominal, constituye la misma propiedad que dificulta de forma crítica su estimación  mediante un número realista de disparos en dispositivos que añadirían ruido.»

---

## 7. Tabla síntesis de expresiones auditadas


| Archivo                           | Línea | Término crítico                                        | Sesgo identificado                                                           | Calificación                   |
| --------------------------------- | :-----: | ------------------------------------------------------ | ---------------------------------------------------------------------------- | ------------------------------ |
| `6.1_datos_caracteristicas.tex`   | 29    | `confirmando que`                                      | Inferencia geométrica tratada como prueba ontológica                         | Sobreafirmación causal         |
| `6.1_datos_caracteristicas.tex`   | 34    | `evidenció que`                                        | Métrica univariante tratada como evidencia concluyente                       | Certeza excesiva               |
| `6.2_separabilidad.tex`           | 117   | `confirmando la validez`                               | Identidad matemática trivial descrita como hallazgo empírico                 | Lenguaje descalibrado          |
| `6.3_clasificacion.tex`           | 16    | `confirma la consistencia`                             | No rechazo de hipótesis nula ($p > 0.3$) tratado como confirmación           | Error conceptual de inferencia |
| `6.3_clasificacion.tex`           | 40    | `confirma que... es robusto`                           | Barrido discreto tratado como demostración general                           | Certeza excesiva               |
| `6.3_clasificacion.tex`           | 43    | `evidenciando que`                                     | Observación particular tratada como principio general                        | Generalización apresurada      |
| `6.4_qsvm_ventaja.tex`            | 13    | `demuestra que... preserva prácticamente la totalidad` | Equivalencia empírica de AUC extrapolada a preservación total de información | Sobreafirmación severa         |
| `6.4_qsvm_ventaja.tex`            | 39    | `confirmando que... es condición necesaria`            | Resultado negativo tratado como confirmación de teorema                      | Confusión lógica               |
| `6.4_qsvm_ventaja.tex`            | 52    | `demuestra que... es una propiedad de estas etiquetas` | Inferencia empírica descrita como demostración necesaria                     | Certeza excesiva               |
| `6.5_comparacion.tex`             | 16    | `estrictamente positiva`, `sin excepción`              | Adverbios absolutos omitiendo que varios coeficientes tienen $p > 0.05$      | Lenguaje no calibrado          |
| `6.5_comparacion.tex`             | 16    | `confirman`, `evidenciando de manera coherente`        | Correlación descriptiva pequeña tratada como confirmación formal             | Sobreafirmación severa         |
| `6.5_comparacion.tex`             | 36    | `demostrando que... obedece a... y no a...`            | Observación de AUC pareados tratada como prueba causal                       | Causalidad no demostrada       |
| `6.6_restricciones_simulador.tex` | 13    | `condicionó de forma determinante`                     | Monocausalidad en una decisión multifactorial                                | Certeza excesiva               |
| `6.6_restricciones_simulador.tex` | 26    | `deja al kernel sin información de clase`              | Inexactitud cuantitativa (el kernel retiene exceso de KTA con $p < 0.05$)    | Sobreafirmación negativa       |
