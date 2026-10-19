# Auditoría de Afirmaciones del Reporte Técnico (TT 2026-B039)

> **Insumo para la reescritura del reporte técnico.**  
> Este documento identifica de forma exhaustiva las afirmaciones de `Docs/Technical_Report.tex` que contradicen las decisiones canónicas de `Other/bitacora_decisiones.md`, las correcciones de `Other/verificacion/correcciones_verificadas.md` o que han sido modificadas en `Docs/borrador_secciones_4.md`.
> 
> **Regla canónica:** Lo que establece la bitácora manda. Todas las citas textuales y números de línea fueron verificados de manera exacta contra el repositorio.

---

## Subsección: Métricas de separabilidad y evaluación (Marco Teórico)

**Ubicación en el reporte:** Marco Teórico, líneas 1710–2008.  
**Alcance:** Formaliza las métricas de evaluación del espacio de representación (KTA, Geometric difference, Davies-Bouldin, Fisher, t-SNE) y de clasificación (Accuracy, Precision, Recall, F1, AUC-ROC, correlación de Spearman).

| Línea .tex | Cita literal del .tex | Decisión / Hallazgo (ID) | Línea bitácora | Cita literal de la bitácora | ¿Corregido en borrador? |
|:---|:---|:---|:---|:---|:---|
| 1740 | "\frac{\langle K,\,\mathbf{y}\mathbf{y}^\top\rangle_F}" | D-033 | 643 | "- **KTA centrada** (Cortes, Mohri y Rostamizadeh, 2012, *JMLR* 13:795–828) como principal, y **sin centrar** (Cristianini, Shawe-Taylor, Elisseeff y Kandola, *NIPS 14*, 2001) como complemento." | No |
| 1776 | "\sqrt{K_C}\;K_Q^{-1}\;\sqrt{K_C}" | H-033 | 1601 | "y la cantidad que evalúa el potencial de ventaja cuántica es **g_CQ = g(K_C‖K_Q)**. Es decir, el kernel **cuántico** va en las raíces y el **clásico** es el que se invierte: g_CQ = √‖√K_Q · K_C⁻¹ · √K_Q‖∞." | No |
| 1783 | "matricial de $K_C$ obtenida por descomposición de Cholesky." | H-033 | 1607 | "- El reporte dice que √K_C se obtiene «por descomposición de Cholesky». El factor de Cholesky L no es la raíz cuadrada simétrica, aunque Lᵀ(·)L da la misma norma espectral." | No |
| 1769 | "kernel clásico de referencia $K_C$ (kernel RBF en el" | H-038, D-032 | 627 | "- g_gen (F19) con la condición g_tra < 0.045 (L9) y las mallas de λ (L10) y de kernels clásicos (L11) sin cambios. Para cada kernel se toma el mayor λ admisible, y se reporta el mínimo sobre la batería." | No |
| 1800 | "de 150--200 casos por subconjunto (masas y calcificaciones)." | D-028 | 531 | "200 lesiones por subconjunto, estratificadas por clase, tomadas del train con semilla 42." | No |
| 1865 | "calcula por dimensión y se reporta como el promedio sobre" | D-033 | 645 | "- **Fisher:** J = Δμᵀ S_W⁻¹ Δμ, la distancia de Mahalanobis al cuadrado entre las medias de clase, con la covarianza intraclase combinada." | No |
| 1913 | "calculadas sobre el conjunto de prueba:" | D-018 | 354 | "Validación cruzada **5-fold estratificada por clase** sobre el conjunto de entrenamiento. El conjunto de prueba oficial del CBIS-DDSM **no se toca**: sigue siendo la evaluación final, sin reordenar (RNF-03)." | No |
| 1982 | "  \frac{6\sum_{i=1}^{5} d_i^2}{5(5^2 - 1)}" | D-039, H-049 | 767 | "- **Cálculo.** ρ_s es la correlación de Pearson de los rangos promedio. Es la definición general; la fórmula del reporte, 1 − 6Σd²/(n(n²−1)), es su caso sin empates y no vale con el empate C1 = C2." | No |

---

## Subsección: Módulo 1: Lectura de datos (Metodología)

**Ubicación en el reporte:** Metodología, líneas 2578–2631.  
**Alcance:** Adquisición, lectura DICOM, unificación tabular y resolución de rutas del dataset CBIS-DDSM.

| Línea .tex | Cita literal del .tex | Decisión / Hallazgo (ID) | Línea bitácora | Cita literal de la bitácora | ¿Corregido en borrador? |
|:---|:---|:---|:---|:---|:---|
| 2618 | "NBIA Data Retriever, identificando para cada caso el" | D-012, H-001 | 820 | "- *Descargar por la API REST de TCIA* — **elegida**." | No |
| 2620 | "y la imagen recortada. La clasificación entre máscara" | H-001, H-020 | 848 | "path_cropped    :  115 NULOS    -> 3453 existen" | No |

---

## Subsección: Módulo 2: Preprocesamiento de imagen (Metodología)

**Ubicación en el reporte:** Metodología, líneas 2632–2665.  
**Alcance:** Alineación de máscaras, ecualización y recorte de la región de interés (ROI).

| Línea .tex | Cita literal del .tex | Decisión / Hallazgo (ID) | Línea bitácora | Cita literal de la bitácora | ¿Corregido en borrador? |
|:---|:---|:---|:---|:---|:---|
| 2641 | "La primera etapa aplica \textbf{ecualización de histograma" | D-010 | 218 | "Extraer las features del recorte crudo. Generar además la variante con CLAHE y **reportar el efecto de ambas**." | Sí |
| 2636 | "DICOM crudas en representaciones visuales normalizadas" | D-022, D-009 | 426 | "**16 bits crudos** de la mamografía" | Sí |
| 2654 | "extrae el recorte cuadrado mínimo que contiene la región" | D-022 | 425 | "caja de la lesión + **20 px** por lado, cortado en el borde de la imagen" | Sí |
| 2652 | "la máscara binaria asociada a cada caso se" | D-020, D-021, H-020 | 1256 | "hay exactamente **80** máscaras con dimensiones distintas a las de su imagen: las mismas de H-004." | Sí |

---

## Subsección: Módulo 3: Extracción de características (Metodología)

**Ubicación en el reporte:** Metodología, líneas 2666–2721.  
**Alcance:** Extracción de descriptores morfológicos y de textura con PyRadiomics y CNN encoder alternativo.

| Línea .tex | Cita literal del .tex | Decisión / Hallazgo (ID) | Línea bitácora | Cita literal de la bitácora | ¿Corregido en borrador? |
|:---|:---|:---|:---|:---|:---|
| 2670 | "la imagen recortada y normalizada de 224$\times$224" | D-009, D-022 | 199 | "PyRadiomics opera sobre el recorte ROI a **resolución original**, con la máscara alineada." | No |
| 2698 | "Esta estrategia produce típicamente entre 100 y 300" | D-023 | 443 | "En 2D y sobre la imagen original, esas cuatro familias dan 67: 18 + 9 + 24 + 16." | No |
| 2702 | "\textbf{Estrategia B: CNN encoder preentrenado.}" | D-006, D-009 | 197 | "Eso es herencia de la Estrategia B (encoder CNN), que fue descartada en D-006." | No |

---

## Subsección: Módulo 4: Selección y escalado (Metodología)

**Ubicación en el reporte:** Metodología, líneas 2722–2770.  
**Alcance:** Selección de características y mapeo angular al rango [0, π].

| Línea .tex | Cita literal del .tex | Decisión / Hallazgo (ID) | Línea bitácora | Cita literal de la bitácora | ¿Corregido en borrador? |
|:---|:---|:---|:---|:---|:---|
| 2733 | "Se aplica SelectKBest con criterio $F$-test de ANOVA," | D-024 | 466 | "Sin la restricción, el procedimiento es exactamente `SelectKBest(k=12)`, de modo que D-001 se mantiene: la selección sigue siendo por F-test, ahora con una restricción de redundancia." | No |
| 2738 | "circuito cuántico ($k \in [8, 16]$), de forma que cada" | D-013 | 248 | "k = 12 qubits, reps = 1." | No |
| 2746 | "mediante MinMaxScaler:" | D-025 | 490 | "§4.6 debe describir la transformación por cuantiles en lugar del `MinMaxScaler`." | No |

---

## Subsección: Módulo 5: Transformación (Metodología)

**Ubicación en el reporte:** Metodología, líneas 2771–2843.  
**Alcance:** Definición de las cinco condiciones experimentales C1 a C5 y ejecución de circuitos cuánticos.

| Línea .tex | Cita literal del .tex | Decisión / Hallazgo (ID) | Línea bitácora | Cita literal de la bitácora | ¿Corregido en borrador? |
|:---|:---|:---|:---|:---|:---|
| 2780 | "en M6. La Tabla~\ref{tab:condiciones} resume las" | D-030 | 574 | "El flujo es un grafo con ramas paralelas: M5 → {M6, M7} → M8." | Sí |
| 2824 | "sirve como piso mínimo; C2 como referencia de la" | D-016 | 322 | "C2 se mantiene y se declara **control nulo**. Se conservan cinco condiciones. No se añade C2′." | Sí |
| 2803 | "  ($\gamma = 1/k$)," | D-027 | 516 | "γ = 1 / (2 · mediana de ‖x − x'‖² sobre los pares del train), calculado por subconjunto sobre el mismo x ∈ [0, π]¹² que recibe el circuito." | Sí |
| 2812 | "  VQC con PauliFeatureMap (operadores Z, ZZ)" | D-031 | 600 | "Con Y, C4 frente a C5 vuelve a comparar el eje de la codificación de primer orden con el mismo acoplamiento ZZ, que era la intención de D-015." | Sí |
| 2839 | "\textit{shots} $\geq 1024$ para garantizar estimaciones" | D-014, H-019, D-040 | 1243 | "3. **Regla para M5:** «exacto» significa `Statevector` directo o una primitiva llamada con precisión 0 explícita. La Arquitectura B no necesita gradientes, así que no necesita `EstimatorQNN`." | Sí |

---

## Subsección: Módulo 6: Clasificación (Metodología)

**Ubicación en el reporte:** Metodología, líneas 2844–2871.  
**Alcance:** Arquitectura y optimización del clasificador MLP sobre representaciones clásicas y cuánticas.

| Línea .tex | Cita literal del .tex | Decisión / Hallazgo (ID) | Línea bitácora | Cita literal de la bitácora | ¿Corregido en borrador? |
|:---|:---|:---|:---|:---|:---|
| 2844 | "\subsection{Módulo 6: Clasificación}" | D-030 | 581 | "renumerar las secciones de módulos, con una nueva sección para M6;" | Sí |
| 2866 | "\texttt{TorchConnector}, que permite la optimización" | D-014, H-054 | 273 | "θ se fija con **semilla 42** y no se entrena. Los embeddings ⟨Zᵢ⟩ se calculan una sola vez para todo el dataset, se guardan en disco, y el MLP se entrena sobre esa matriz como sobre cualquier conjunto tabular. `TorchConnector` deja de usarse." | Sí |
| 2847 | "El módulo de clasificación entrena y evalúa un mismo" | D-018, D-026 | 354 | "Validación cruzada **5-fold estratificada por clase** sobre el conjunto de entrenamiento. El conjunto de prueba oficial del CBIS-DDSM **no se toca**: sigue siendo la evaluación final, sin reordenar (RNF-03)." | Sí |

---

## Subsección: Módulo 7: Evaluación comparativa (Metodología)

**Ubicación en el reporte:** Metodología, líneas 2872–2923.  
**Alcance:** Evaluación comparativa de separabilidad, clasificación, correlación de Spearman y viabilidad computacional.

| Línea .tex | Cita literal del .tex | Decisión / Hallazgo (ID) | Línea bitácora | Cita literal de la bitácora | ¿Corregido en borrador? |
|:---|:---|:---|:---|:---|:---|
| 2872 | "\subsection{Módulo 7: Evaluación comparativa}" | D-030 | 582 | "reagrupar la tabla de requisitos: RF-15 a RF-17 van a M6 y los de clasificación a M7;" | No |
| 2894 | "Recall sobre el conjunto de prueba para cada condición," | D-018 | 354 | "Validación cruzada **5-fold estratificada por clase** sobre el conjunto de entrenamiento. El conjunto de prueba oficial del CBIS-DDSM **no se toca**: sigue siendo la evaluación final, sin reordenar (RNF-03)." | No |
| 2905 | "AUC-ROC (ecuación~\eqref{eq:spearman}), para determinar" | D-039, H-049 | 2080 | "- **Corrección para §3.4.** La ecuación `spearman` del reporte, 1 − 6Σd²/(n(n²−1)), solo vale sin empates. Con el empate C1 = C2 se usa la correlación de Pearson de los rangos promedio." | No |
| 2915 | "número máximo viable de qubits, impacto del número de" | D-040, H-019 | 797 | "Para cada lesión se sortean n cadenas de bits a partir de las probabilidades exactas, con un sorteo multinomial. Es la estadística de un *sampler* ideal." | No |

---

## Afirmaciones no verificadas contra la bitácora

Las siguientes afirmaciones extraídas de las secciones auditadas de `Technical_Report.tex` no pudieron verificarse contra decisiones (D-xxx) o hallazgos (H-xxx) de `bitacora_decisiones.md`. Se consignan aquí para que el autor confirme si deben mantenerse, actualizarse o sustituirse:

| Línea .tex | Cita literal del .tex | Motivo por el cual no se verificó en bitácora |
|:---|:---|:---|
| 1728 | "de clase \cite{cristianini2002kernel}. Un valor elevado de" | La cita bibliográfica en el .tex apunta a cristianini2002kernel (2002), mientras que la bitácora (D-033, l. 643) registra la referencia primaria como Cristianini, Shawe-Taylor, Elisseeff y Kandola, NIPS 14 (2001). |
| 1818 | "  \frac{s_i + s_j}{d(c_i, c_j)}" | La formulación explícita de dispersión intra-cluster s_i y de la distancia L2 euclidiana entre centroides para el índice Davies-Bouldin. La bitácora (D-033, l. 646) solo declara «Davies-Bouldin con las clases como clusters (sklearn)», sin documentar las fórmulas matemáticas explícitas de la dispersión L2. |
| 1893 | "si la proyección t-SNE muestra clusters compactos y bien" | La interpretación cualitativa de discriminabilidad visual mediante t-SNE. La bitácora (D-033, l. 648) solo fija parámetros técnicos («t-SNE (perplejidad 30, inicialización PCA, semilla 42), solo como visualización»), sin justificar el comportamiento cualitativo en el marco teórico. |
| 1917 | "  \text{Acc} =" | Fórmulas canónicas de métricas de clasificación estándar (Accuracy, Precision, Recall, F1, integral continua del AUC-ROC). La bitácora asume estas métricas estándar de scikit-learn pero no incluye sus definiciones teóricas. |
| 2594 | "confirmó que la totalidad de las imágenes del dataset" | La deducción de que la totalidad de mamografías usan MONOCHROME2 y que ello «elimina la necesidad de inversión de píxeles en el preprocesamiento» (l. 2598–2599). H-002 (l. 863) y D-012 (l. 826) confirman MONOCHROME2 en muestras y en las series nuevas, pero no formulan dicha consecuencia operativa explícita. |
| 2622 | "las máscaras presentan exactamente dos valores únicos" | La regla heurística de discriminación automática entre máscara y recorte basada en que «las máscaras presentan exactamente dos valores únicos (0 y 255) mientras que las imágenes recortadas presentan cientos de valores distintos» (l. 2622–2624). La bitácora (H-020) analiza los recortes y máscaras, pero no documenta esta regla de clasificación de píxeles. |
| 2683 | "  \item \textit{First-order statistics}: estadísticas de" | El listado de descriptores morfológicos y texturales específicos de cada una de las cuatro familias radiómicas en el texto (media, varianza, asimetría, curtosis, energía, contraste, homogeneidad, etc.). D-023 fija el número total de 67 features (18 + 9 + 24 + 16), pero no lista los nombres individuales en el texto. |
| 2851 | "dos capas ocultas con activación ReLU, y una" | La topología exacta y funciones de activación del perceptrón multicapa («dos capas ocultas con activación ReLU, y una capa de salida con activación sigmoide», l. 2851–2853). La bitácora fija que el MLP es idéntico entre condiciones y entrena en segundos (D-014, D-036), pero no valida la topología exacta de capas del texto de TT1. |
| 2859 | "el desbalance observado en el EDA (ratio 1.78:1 en" | La cifra exacta del ratio de desbalance reportado para calcificaciones: «ratio 1.78:1 en calcificaciones» (l. 2859). La bitácora registra proporciones de clase y balance en folds (H-027, D-026: ~35% de malignas), pero el ratio específico 1.78:1 no aparece registrado textualmente. |

---

## Revisión del coordinador (2026-10-13)

- Las 32 filas se comprobaron con un script: cada cita aparece literal en la línea indicada (±3 líneas) del `.tex` y de la bitácora.
- Dos de las «no verificadas» sí tienen respaldo:
  - **Línea 2851** (dos capas ocultas ReLU y salida sigmoide): D-036 fija la red k → 32 → 16 → 1, con ReLU y salida sigmoide.
  - **Línea 2859** (1.78:1 en calcificaciones): 1,199 benignas frente a 673 malignas en `Data/cbis_ddsm_unified.csv`, 1.782.
- Una más ya está verificada: la línea 2594 (MONOCHROME2 en todas). `Code/results/1_metadatos_dicom.csv` lo confirma sobre las 3,103 mamografías.
- Las demás son definiciones estándar (Davies-Bouldin, métricas de clasificación, familias de PyRadiomics) que no necesitan una entrada en la bitácora.
