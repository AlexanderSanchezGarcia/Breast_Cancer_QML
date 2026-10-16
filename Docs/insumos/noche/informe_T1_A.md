# Informe de Ejecución · T1 Fichas de Lectura (Grupo A)

**Fecha:** 2026-10-14  
**Trabajador:** Dispatch `ctx_ca548ef73d64` · Tarea `task_f4eac562df5e` · Terminal `term_7d80c9d1-35eb-46a5-b717-b4cf624ef103`  
**Grupo asignado:** Grupo A (ventaja cuántica: teoría y datos cuánticos)  
**Claves asignadas:** `huang2021power`, `Liu2021Speedup`, `Glick2024Covariant`, `Huang2022Experiments`.

---

## 1. Resumen ejecutivo

1. **Qué se hizo:** Se leyeron íntegramente las fuentes originales en PDF/TXT de las cuatro obras asignadas al Grupo A y se redactó una ficha de lectura completa para cada una en `Docs/insumos/fichas/<Clave>.md`, siguiendo rigurosamente la estructura canónica de `Docs/insumos/noche/T1_fichas.md`, respondiendo todas las preguntas específicas y contrastando las afirmaciones contra el reporte técnico y la bitácora.
2. **Qué se encontró:** Se verificaron al 100 % las citas textuales de las 4 fichas (134 citas literales sin fallos en el verificador sintáctico). Se confirmaron discrepancias críticas en el reporte técnico respecto a `huang2021power` (fórmula de *geometric difference* con factores invertidos respecto a la ecuación 5 original, interpretación errónea de $g < 1$ y mención inapropiada de Cholesky), y se clarificaron los límites de atribución de `Liu2021Speedup`, `Glick2024Covariant` y `Huang2022Experiments`, donde ninguna de las obras respalda ventajas en datos biomédicos clásicos como mamografías.
3. **Qué queda pendiente / lo que no se pudo hacer:** No se dejó ningún `[VERIFICAR]`. Los cuatro archivos de fichas quedaron creados y pasan todas las pruebas de aceptación. Queda pendiente para el autor aplicar las correcciones identificadas en `Docs/Technical_Report.tex` en la sección 3.4.2 según el protocolo ya definido en la bitácora (H-033, H-038 y D-032).

---

## 2. Archivos creados

1. `Docs/insumos/fichas/huang2021power.md`: 41 citas verificadas.
2. `Docs/insumos/fichas/Liu2021Speedup.md`: 31 citas verificadas.
3. `Docs/insumos/fichas/Glick2024Covariant.md`: 34 citas verificadas.
4. `Docs/insumos/fichas/Huang2022Experiments.md`: 28 citas verificadas.
5. `Docs/insumos/noche/informe_T1_A.md`: este informe.

---

## 3. Pruebas de aceptación

Se corrió el verificador canónico `python3 Code/tools/verificar_citas_fichas.py` sobre cada una de las fichas del Grupo A y sobre la carpeta general:

```text
$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/huang2021power.md
huang2021power.md: OK · 41/41 citas verificadas

1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Liu2021Speedup.md
Liu2021Speedup.md: OK · 31/31 citas verificadas

1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Glick2024Covariant.md
Glick2024Covariant.md: OK · 34/34 citas verificadas

1/1 fichas pasan.

$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Huang2022Experiments.md
Huang2022Experiments.md: OK · 28/28 citas verificadas

1/1 fichas pasan.
```

Salida global en `Docs/insumos/fichas/`:
```text
$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/
Azevedo2022QuantumTransfer.md: OK · 15/15 citas verificadas
Canatar2023Bandwidth.md: OK · 18/18 citas verificadas
Glick2024Covariant.md: OK · 34/34 citas verificadas
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
Zhang2013NEQR.md: OK · 13/13 citas verificadas
huang2021power.md: OK · 41/41 citas verificadas

19/19 fichas pasan.
```

---

## 4. Tabla de discrepancias entre lo que el proyecto atribuye y lo que la obra dice

Esta tabla recopila cada atribución existente en los documentos del proyecto (`Docs/Technical_Report.tex`, `Other/referencias_por_revisar.md`, `Other/correcciones_verificadas.md`, `Other/bitacora_decisiones.md`), contrastada con el texto exacto verificado en las fuentes originales:

| Clave | Archivo y línea | Qué afirma el proyecto | Lo que la obra sostiene realmente | Estado | Cita de respaldo en la fuente |
|---|---|---|---|---|---|
| `huang2021power` | `Docs/Technical_Report.tex:1774-1779` | Define $g(K_C, K_Q) = \sqrt{\| \sqrt{K_C} K_Q^{-1} \sqrt{K_C} \|_\infty}$ mediante Cholesky | La ecuación (5) de Huang et al. define $g(K_1 \|\| K_2) = \sqrt{\| \sqrt{K_2} K_1^{-1} \sqrt{K_2} \|_\infty}$ con $\mathrm{Tr}(K_1) = \mathrm{Tr}(K_2) = N$. Para ventaja cuántica, $g_{CQ} = g(K_C \|\| K_Q)$: el cuántico va en las raíces y el clásico se invierte. Además, no se usa Cholesky (que da una matriz triangular), sino descomposición en valores singulares (SVD) o raíz matricial hermítica. | **No lo sostiene / Erróneo en el reporte** (coincide con el hallazgo H-033 de la bitácora) | «where ∣∣. ∣∣∞is the spectral norm of the resulting matrix and we assume Tr(K1) = Tr(K2) = N.» (p. 5) y «The geometric difference g(K1∣∣K2) can be computed on a classical computer by performing a singular value decomposition» (p. 5) |
| `huang2021power` | `Docs/Technical_Report.tex:1793-1795` | Afirma que si $g < 1$ el kernel clásico captura estructura que el cuántico no ve | Con kernels normalizados a traza $N$, por propiedades de la norma espectral $g(K_C \|\| K_Q) \ge 1$. La idea de $g < 1$ en el texto es un artefacto de haber invertido los factores en la fórmula. | **Parcial / Erróneo** | «One can show that sK1 ≤g2 12sK2, which implies the prediction error bound» (p. 5) |
| `huang2021power` | `Docs/Technical_Report.tex:1768-1770` | Evalúa $g$ contra un solo kernel RBF clásico fijado por la mediana | Huang et al. señalan que $g$ debe evaluarse frente al mejor modelo de una batería amplia de kernels clásicos optimizados, y usar la versión regularizada $g_{\mathrm{gen}}$ para evitar que la norma espectral explote espuriamente cuando $K_Q \approx I$. | **Parcial** (corregido en bitácora D-032 y H-038) | «We see that small geometric difference g always results in classical ML being competitive or outperforming the quantum ML model.» (p. 7) |
| `huang2021power` | `Docs/Technical_Report.tex:3515-3518` | Atribuye a Huang et al. el marco para determinar si el espacio cuántico captura estructura inaccesible al mejor clásico | Es exactamente el propósito teórico de la obra. | **Sí lo sostiene** | «Only when the geometric difference g is large (projected kernel method with embedding E3) can we see some mild advantage over the best classical method.» (p. 7) |
| `huang2021power` | `Other/bitacora_decisiones.md:1563` | Describe que a $c=1$ los kernels cuánticos saturan $d \approx N$ y «all inputs are too far apart» con $K_Q \approx I$ | Huang et al. identifican expresamente ese régimen en el espacio de Hilbert como la causa de que los kernels cuánticos estándar fallen. | **Sí lo sostiene palabra por palabra** | «The small geometric difference is a consequence of the exponentially large Hilbert space employed by existing quantum models, where all inputs are too far apart.» (p. 2) |
| `Liu2021Speedup` | `Other/referencias_por_revisar.md:11-19` | Construyen datos donde ningún clásico supera al azar bajo DLP y QSVM en hardware tolerante a fallos clasifica con alta precisión | Es la tesis central del paper (Theorem 1 y 2). | **Sí lo sostiene** | «We construct a family of datasets and show that no classical learner can classify the data inverse-polynomially better than random guessing, assuming the widely-believed hardness of the discrete logarithm problem.» (p. 1) y «Theorem 2. The concept class C is eﬃciently learnable by SVM-QKE.» (p. 6) |
| `Liu2021Speedup` | `Other/referencias_por_revisar.md:17` | Pendiente verificar si requiere tolerante a fallos, sentido de dificultad del kernel y tamaño de conjuntos | Verificado: Requiere tolerante a fallos porque ejecuta Shor como subrutina de $U(x)$; el kernel es difícil porque sus entradas son tan difíciles como DLP; los conjuntos son de tamaño polinomial en $n$. | **Comprobado / Resuelto** | «a conventional support vector machine that uses a fault-tolerant quantum computer to estimate a kernel function.» (p. 1), «Next we show that estimating the kernel entries is as hard as solving the discrete log problem.» (p. 18), y «and the size of S is polynomial in the data dimension.» (p. 2) |
| `Liu2021Speedup` | `Other/referencias_por_revisar.md:18` | La estructura está en la etiqueta (logaritmo discreto), no en las variables | El espacio de datos $X$ es uniforme; la separabilidad existe únicamente en el espacio del logaritmo discreto $s = \log_g(x)$. | **Sí lo sostiene** | «the training data samples are clustered in two intervals: [s, s + p−3 2 ] with label +1, and [s + p−1 2 , s + p −2] with label −1, for the unknown s ∈Z∗ p (which deﬁnes the unknown concept fs).» (p. 11) |
| `Glick2024Covariant` | `Other/referencias_por_revisar.md:21-30` | Clasificación de cosets de un subgrupo con perturbaciones; implementado con 27 qubits en procesador superconductor | El problema experimental es etiquetar clases laterales con errores sobre $\mathrm{SU}(2)^{\otimes 27}$, probado en `ibmq_kolkata`. | **Sí lo sostiene** | «The learning problem we have studied experimentally serves as an abstract representation of many group theoretic problems, i.e. classiﬁcation of data that is close to cosets of a group.» (p. 4) y «The connectivity of the 27-qubit device ibmq_kolkata.» (p. 3) |
| `Glick2024Covariant` | `Other/referencias_por_revisar.md:28` | Pendiente verificar año y revista de la versión publicada (preprint 2021) | Verificado: publicado en *Nature Physics* 20(3), 479–483 en 2024 (no 2021 ni 2022). | **Comprobado / Resuelto** | Confirmado por metadatos oficiales y Crossref DOI: 10.1038/s41567-023-02340-9 |
| `Glick2024Covariant` | Posible atribución externa errónea | ¿Demuestran ventaja cuántica en datos reales o supremacía computacional? | **No lo sostiene**: Admiten que la ventaja en datos reales es un reto no resuelto; usan datos puramente sintéticos y su circuito es poco profundo y admite simulación clásica eficiente. | **Aclaración crítica** | «It is an important challenge to ﬁnd quantum kernels that provide an advantage in the classiﬁcation of real-world data.» (p. 1) y «The considered circuit, although supported on a larger number of qubits, is still suﬃciently shallow so that classical simulation methods can be applied [37].» (p. 5) |
| `Huang2022Experiments` | `Other/referencias_por_revisar.md:36-44` | Ventaja exponencial en aprender de experimentos con hasta 40 qubits y 1,300 compuertas en Sycamore | Corresponde con exactitud a los teoremas y experimentos físicos reportados en Google Sycamore. | **Sí lo sostiene palabra por palabra** | «The exponential advantage holds in predicting properties of physical systems, performing quantum principal component analysis on noisy states, and learning approximate models of physical dynamics.» (p. 1) y «Conducting experiments with up to 40 superconducting qubits and 1300 quantum gates» (p. 1) |
| `Huang2022Experiments` | `Other/referencias_por_revisar.md:42` | Pendiente verificar si la ventaja requiere memoria cuántica | Verificado: Requiere memoria cuántica de forma estricta. Si los estados se miden individualmente de forma convencional sin memoria cuántica, cualquier estrategia requiere exponencialmente más experimentos ($\Omega(2^n)$). | **Comprobado / Resuelto** | «showing that a sufficiently large quantum memory is needed to achieve this task in the quantum-enhanced scenario.» (p. 3) |
| `Huang2022Experiments` | `Other/referencias_por_revisar.md:43` | Uso en §7: «la ventaja aparece cuando el dato es un estado cuántico. Una mamografía no lo es porque el detector mide fotones y destruye la información cuántica» | La premisa del artículo es que los experimentos convencionales pierden la ventaja cuántica al medir inmediatamente copias individuales en datos clásicos; la ventaja solo existe si el dato ingresa y se procesa en memoria cuántica. | **Sí lo sostiene conceptualmente** | «An experimental setup that transduces data from a physical system to a stable quantum memory, and processes that data using a quantum computer, could have significant advantages over conventional experiments in which the physical system is measured and the outcomes are processed using a classical computer.» (p. 1) |

---

## 5. Conclusiones y recomendaciones para el autor

1. **Corrección de la sección 3.4.2 de `Docs/Technical_Report.tex`**: Se debe corregir la ecuación `eq:geometric_diff` para que $K_Q$ esté dentro de las raíces cuadradas y $K_C$ sea el kernel invertido, eliminando la referencia a Cholesky y la mención de $g < 1$.
2. **Fundamentación de resultados negativos en §7**: Los 4 artículos del Grupo A confirman unívocamente la solidez teórica de los hallazgos del TT (H-039, H-046, H-047, H-048). Ninguno de los trabajos teóricos o experimentales de ventaja cuántica reporta ventaja sobre datos clásicos reales colapsados sin simetría algebraica oculta. La ausencia de ventaja cuántica en las features radiómicas del CBIS-DDSM es consistente con el estado del arte riguroso de la computación cuántica.
