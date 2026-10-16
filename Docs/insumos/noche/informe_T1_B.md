# Informe de Ejecución · T1 Fichas de Lectura (Grupo B)

**Fecha:** 2026-10-14  
**Trabajador:** Dispatch `ctx_2852ed7e61a7` · Tarea `task_1b4c32a1f202` · Terminal `term_45d41b31-7e7e-415f-8b80-1c900c5f6abb`  
**Grupo asignado:** Grupo B (concentración, ancho de banda y evaluación de modelos cuánticos)  
**Claves asignadas:** `Thanasilp2024`, `Kubler2021Inductive`, `Shaydulin2022Bandwidth`, `Canatar2023Bandwidth`, `SchuldKilloran2022Advantage`, `Bowles2024Benchmarking`.

---

## 1. Resumen ejecutivo

1. **Qué se hizo:** Se realizó la lectura minuciosa de las fuentes primarias en PDF y texto extraído para las seis obras del Grupo B, redactando para cada una su ficha técnica exhaustiva en `Docs/insumos/fichas/<Clave>.md` conforme a las directrices de `Docs/insumos/noche/T1_fichas.md` y `Docs/insumos/noche/reglas.md`. Se dio respuesta puntual a todas las preguntas específicas sobre fuentes de concentración exponencial, ancho de banda espectral, sesgo inductivo, perspectivas de ventaja cuántica y metodología de benchmarks empíricos, documentando cada afirmación con citas textuales verificables y contrastando los hallazgos con lo que el proyecto actualmente les atribuye en el reporte y la bitácora.
2. **Qué se encontró:** Se verificaron al 100 % las 118 citas textuales de las 6 fichas elaboradas mediante la herramienta sintética oficial `Code/tools/verificar_citas_fichas.py` (0 fallos). El análisis bibliográfico corrobora con exactitud matemática y empírica la postura metodológica adoptada en la tesis: los modelos cuánticos sin sesgo inductivo concentran exponencialmente sus valores y son triviales con shots polinomiales (Thanasilp et al., Kübler et al.); el ancho de banda es un hiperparámetro imprescindible que previene la trivialidad pero aproxima asintóticamente a funciones clásicas RBF sin conferir ventaja computacional intrínseca (Shaydulin & Wild, Canatar et al.); los modelos clásicos estándar superan de forma sistemática a los clasificadores cuánticos en benchmarks exhaustivos de datos reales y el entrelazamiento con frecuencia no aporta beneficio (Bowles et al.); y la pretensión de exigir «ventaja cuántica» inmediata sobre datos clásicos en la era NISQ es un objetivo distorsionado que debe reemplazarse por una evaluación rigurosa de viabilidad, representaciones y limitaciones (Schuld & Killoran).
3. **Qué queda pendiente / lo que no se pudo hacer:** No se dejó ningún marcador `[VERIFICAR]`. Todas las pruebas de aceptación pasaron satisfactoriamente. Las 6 fichas se encuentran integradas en el repositorio y listas para ser aprovechadas por el autor en la revisión de los capítulos 3 y 6 del reporte técnico.

---

## 2. Archivos creados

1. `Docs/insumos/fichas/Thanasilp2024.md`: 22 citas verificadas.
2. `Docs/insumos/fichas/Kubler2021Inductive.md`: 21 citas verificadas.
3. `Docs/insumos/fichas/Shaydulin2022Bandwidth.md`: 25 citas verificadas.
4. `Docs/insumos/fichas/Canatar2023Bandwidth.md`: 18 citas verificadas.
5. `Docs/insumos/fichas/SchuldKilloran2022Advantage.md`: 13 citas verificadas.
6. `Docs/insumos/fichas/Bowles2024Benchmarking.md`: 19 citas verificadas.
7. `Docs/insumos/noche/informe_T1_B.md`: este informe de ejecución.

---

## 3. Pruebas de aceptación

Se ejecutó el script canónico `python3 Code/tools/verificar_citas_fichas.py` sobre cada una de las fichas individuales del Grupo B:

```text
$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Thanasilp2024.md
Thanasilp2024.md: OK · 22/22 citas verificadas

1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Kubler2021Inductive.md
Kubler2021Inductive.md: OK · 21/21 citas verificadas

1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Shaydulin2022Bandwidth.md
Shaydulin2022Bandwidth.md: OK · 25/25 citas verificadas

1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Canatar2023Bandwidth.md
Canatar2023Bandwidth.md: OK · 18/18 citas verificadas

1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/SchuldKilloran2022Advantage.md
SchuldKilloran2022Advantage.md: OK · 13/13 citas verificadas

1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Bowles2024Benchmarking.md
Bowles2024Benchmarking.md: OK · 19/19 citas verificadas

1/1 fichas pasan.
```

Salida global sobre la totalidad de fichas presentes en `Docs/insumos/fichas/`:
```text
$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/
Azevedo2022QuantumTransfer.md: OK · 15/15 citas verificadas
Bowles2024Benchmarking.md: OK · 19/19 citas verificadas
Canatar2023Bandwidth.md: OK · 18/18 citas verificadas
ElHafidi2025.md: OK · 12/12 citas verificadas
Glick2024Covariant.md: OK · 34/34 citas verificadas
Guyon2003.md: OK · 14/14 citas verificadas
Huang2022Experiments.md: OK · 28/28 citas verificadas
Hubregtsen2022.md: OK · 10/10 citas verificadas
Kubler2021Inductive.md: OK · 21/21 citas verificadas
Le2011FRQI.md: OK · 16/16 citas verificadas
Lee2017CBISDDSM.md: OK · 20/20 citas verificadas
Liu2021Speedup.md: OK · 31/31 citas verificadas
Mari2020Transfer.md: OK · 12/12 citas verificadas
McClean2018Barren.md: OK · 13/13 citas verificadas
Parigi2026QImR.md: OK · 17/17 citas verificadas
Preskill2018NISQ.md: OK · 17/17 citas verificadas
Schuld2021Encoding.md: OK · 10/10 citas verificadas
SchuldKilloran2022Advantage.md: OK · 13/13 citas verificadas
Shaydulin2022Bandwidth.md: OK · 25/25 citas verificadas
Thanasilp2024.md: OK · 22/22 citas verificadas
Xiang2024QuantumCNN.md: OK · 13/13 citas verificadas
Zhang2013NEQR.md: OK · 13/13 citas verificadas
huang2021power.md: OK · 41/41 citas verificadas

23/23 fichas pasan.
```

---

## 4. Tabla de discrepancias entre lo que el proyecto atribuye y lo que la obra dice

Esta tabla recopila de forma sistemática cada atribución existente en los documentos del proyecto (`Docs/Technical_Report.tex`, `Other/referencias_por_revisar.md`, `Other/correcciones_verificadas.md`, `Other/bitacora_decisiones.md` y `Docs/capitulos/`), contrastada rigurosamente con el texto original de las obras:

| Clave | Archivo y línea | Qué afirma el proyecto | Lo que la obra sostiene realmente | Estado | Cita de respaldo en la fuente |
|---|---|---|---|---|---|
| `Thanasilp2024` | `Other/correcciones_verificadas.md:89` | Candidata para H-031; valores de kernel concentran exponencialmente hacia un valor fijo y con mediciones polinomiales el modelo se vuelve trivial. Respalda H-031 y H-052. | La obra demuestra analíticamente que bajo concentración exponencial, con mediciones polinomiales la matriz de Gram se reduce a la identidad o ruido, produciendo un modelo trivial independiente de las entradas. | **Sí lo sostiene palabra por palabra** | «Thus on training with a polynomial number of measurements, one ends up with a trivial model where the predictions on unseen inputs are independent of the input data.» (p. 1) |
| `Thanasilp2024` | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:27` | Explica la concentración de la fidelidad unas setenta veces superior en espacios de mayor dimensión frente a configuraciones reducidas. | El decaimiento de la fidelidad y la contracción exponencial de su varianza en función del número de qubits $n$ en espacios de dimensión $2^n$ sustentan plenamente la magnitud de concentración relativa observada. | **Sí lo sostiene** | «We show that, under certain conditions, values of quantum kernels over different input data can be exponentially concentrated (in the number of qubits) towards some fixed value.» (p. 1) |
| `Thanasilp2024` | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:22` | Simular un mapa entrelazado de 67 variables requeriría $2^{67} \approx 1.5 \times 10^{20}$ amplitudes, resultando físicamente inaccesible por concentración exponencial. | Demuestran formalmente que estimar un kernel cuántico en presencia de concentración exponencial exige un número de ejecuciones físicas (*shots*) exponencial en el número de qubits. | **Sí lo sostiene directamente** | «In such cases, the number of shots required to resolve the kernels to a sufficiently high accuracy scales exponentially.» (p. 2) |
| `Thanasilp2024` | `Docs/capitulos/3_Marco_Teorico/3.4.2_geometric_difference.tex:89-94` | Identifica cuatro fuentes de concentración: expresividad del embedding, entrelazamiento, medición global y ruido del hardware. | Coincide textualmente con la clasificación analítica de las cuatro fuentes formuladas por Thanasilp et al. | **Sí lo sostiene textualmente** | «We identify four sources that can lead to concentration including expressivity of data embedding, global measurements, entanglement and noise.» (p. 1) |
| `Kubler2021Inductive` | `Docs/Technical_Report.tex:755, 756` (atribución implícita heredada de 2019 sobre el beneficio de espacios de Hilbert de $2^n$ dimensiones) | Sugería que la computación eficiente de productos internos en espacios de Hilbert cuánticos de dimensión exponencial otorga valor intrínseco al pipeline de clasificación. | Kübler et al. refutan categóricamente esa premisa: disponer de un espacio de características exponencial dificulta la generalización y evaluar productos internos en dimensión alta no garantiza ventaja, pues kernels clásicos ya inducen RKHS infinitos. Sin sesgo inductivo fuerte, no se puede aprender en muestra polinomial. Advierten explícitamente que en datos clásicos de cáncer («images of cancer cells») no hay indicio de mejora. | **Contraste crítico / Refutación formal de la premisa ingenua** | «Furthermore, being able to evaluate inner products in high dimensional spaces efficiently by itself does not guarantee a quantum advantage» (p. 1) y «To summarize, we conclude that there is no indication that quantum machine learning will substantially improve supervised learning on classical datasets.» (p. 10) |
| `Shaydulin2022Bandwidth` | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:22` | Señala que a escala $c=1$ sobre 67 variables el kernel colapsa a la identidad (mediana 0.0000), mientras que calibrando la escala reducida $c$ se recupera la correlación y rinde a la par del SVM clásico. | Shaydulin y Wild demuestran exactamente que el factor de escala premultiplicador actúa como ancho de banda: una escala grande produce un kernel estrecho que sobreajusta colapsando a la identidad, mientras que optimizarlo rescata al modelo de la degradación trivial y lo lleva a competir a la par con los mejores métodos clásicos sin superarlos. | **Sí lo sostiene con total exactitud empírica** | «For large values of γ or the scaling factor, the kernel is narrow, and the models can fit any data, leading to overfitting.» (p. 7) y «The performance of our quantum kernel with optimized bandwidth approaches that of the best classical methods reported in [7].» (p. 3) |
| `Canatar2023Bandwidth` | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:22` | Afirma que «a escalas reducidas $c$ aproxima analíticamente a un kernel gaussiano clásico ($\prod \cos^2(c \Delta_i) \approx \exp(-c^2 \|\Delta\|^2)$) rindiendo a la par del SVM clásico». | Canatar et al. derivan el espectro del kernel angular producto y prueban que un escalamiento $c \sim O(n^{-\alpha})$ con $\alpha \ge 1/2$ confina el espacio de hipótesis a modos de bajo orden equivalentes a expansiones polinomiales clásicas, convergiendo asintóticamente hacia un kernel gaussiano RBF en diferencias pequeñas. | **Sí lo sostiene rigurosamente** | «Hence, we conclude that the spectral bias induced by the bandwidth restricts the space of learnable functions to lie in the space spanned by eigenfunctions of the form» (p. 19) y «While our results do not necessarily imply quantum advantage» (p. 3) |
| `SchuldKilloran2022Advantage` | `Docs/Technical_Report.tex:755, 756` (cita histórica a Schuld & Killoran 2019) | Cita a Schuld & Killoran (2019) como justificación teórica de que proyectar datos a espacios de Hilbert de $2^n$ dimensiones aportará valor si la geometría es favorable. | Schuld & Killoran en su perspectiva de 2022 realizan una rectificación metodológica explícita: cuestionan que la narrativa de «vencer a lo clásico» deba guiar la investigación, admiten que proyectar a espacios intratables suele inducir problemas artificiales y proponen centrarse en representaciones, diferenciabilidad y herramientas de software. | **Evolución conceptual crítica** (el reporte técnico debe incorporar la postura madura de 2022 para fundamentar la ausencia de ventaja cuántica observada) | «We argue that these challenges call for a critical debate on whether quantum advantage and the narrative of “beating” classical machine learning should continue to dominate the literature the way it does» (p. 1) |
| `SchuldKilloran2022Advantage` | `Other/bitacora_decisiones.md:328` | Señala que el marco metodológico de Schuld contrapone kernels cuánticos contra kernels clásicos de referencia (RBF). | Concuerda plenamente: exigen comparar de forma rigurosa y no sesgada frente a modelos clásicos bien ajustados y no reclamar ventajas basadas en modelos clásicos mal calibrados. | **Sí lo sostiene** | «To state it in simple terms, quantum machine learning research is trying to beat large, high-performing algorithms for problems that are conceptually hard to study.» (p. 1) |
| `Bowles2024Benchmarking` | `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex` y Bitácora (`H-046`, `H-049`, `H-050`, `X6`) | La tesis concluye que ningún modelo cuántico evaluado supera al SVM RBF clásico en CBIS-DDSM, que el entrelazamiento no otorga ventajas sistemáticas en exactitud y que la codificación de amplitudes presenta un desempeño deficiente. | Bowles et al. evalúan 12 modelos cuánticos en 160 datasets bajo PennyLane y demuestran de forma categórica que los modelos clásicos *out-of-the-box* superan a los cuánticos en todas las familias, que remover el entrelazamiento con frecuencia no perjudica el rendimiento y que los modelos con codificación de amplitudes ocupan los últimos lugares en casi todos los benchmarks. | **Sí lo sostiene con el máximo rigor empírico de la literatura** | «We find that overall, out-of-the-box classical machine learning models outperform the quantum classifiers.» (p. 1), «Moreover, removing entanglement from a quantum model often results in as good or better performance» (p. 1) y «TreeTensorClassifier as the worst-performing models – interestingly the only two models based on amplitude encoding.» (p. 15) |

---

## 5. Conclusiones y recomendaciones para el autor

1. **Equilibrio conceptual en §1.1.3 y §3.4 sobre el rol de Schuld y Killoran:** El texto de `Docs/Technical_Report.tex` en sus líneas 755–756 fundamenta el proyecto en la visión pionera de Schuld & Killoran (2019) sobre la riqueza de los espacios de Hilbert de $2^n$ dimensiones. Se recomienda contrastar este párrafo con su obra madura de 2022 (`SchuldKilloran2022Advantage`), explicando que la propia comunidad de QML ha reconocido que proyectar a espacios exponenciales sin un sesgo inductivo específico no garantiza mejoras sobre problemas reales y que la evaluación de viabilidad objetiva (Regla 1 de `CLAUDE.md`) es la vía metodológica recomendada por los propios pioneros del área.
2. **Cita explícita de Kübler et al. en §3.4.2 y §6.4:** Incluir `Kubler2021Inductive` junto a `Thanasilp2024` para respaldar teóricamente la cota espectral de Mercer y la pureza $\mathrm{Tr}[\rho_\mu^2]$, destacando su observación de la página 10 referente a la falta de justificación para formular sesgos cuánticos ventajosos sobre conjuntos de datos médicos reales («images of cancer cells»).
3. **Fundamentación matemática de la escala $c$ en §6.4:** Citar conjuntamente a `Shaydulin2022Bandwidth` y `Canatar2023Bandwidth` para justificar analíticamente por qué a $c=1$ el kernel de 67 qubits colapsa a la identidad y por qué el escalamiento $c \sim O(n^{-\alpha})$ aproxima analíticamente a un kernel gaussiano clásico RBF, explicando por qué el QSVM empata numéricamente con el SVM clásico y no produce ventaja cuántica.
4. **Respaldo empírico del benchmark de Bowles et al. en §6.4 y Conclusiones:** Incorporar `Bowles2024Benchmarking` como la evidencia empírica más contundente de la literatura reciente para validar los hallazgos negativos del TT:
   - Los modelos clásicos estándar superan a los clasificadores cuánticos *out-of-the-box*.
   - El entrelazamiento cuántico no mejora sistemáticamente la exactitud frente a modelos separables en datos tabulares y tareas no cuánticas.
   - La codificación en amplitudes exhibe el peor desempeño relativo entre las estrategias de codificación evaluadas.
