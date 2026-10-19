# Auditoría de §1 (Panorama General) y §2 (Antecedentes) — TT 2026-B039

> **Documento de diagnóstico para la reescritura de §1 y §2 del Reporte Técnico.**  
> **Alcance de revisión:** `Docs/Technical_Report.tex`, líneas 421–468 (Abstract) y líneas 470–978 (§1 Panorama General y §2 Antecedentes, hasta antes de `\section{Marco Teórico}`). **Modo solo lectura.**  
> **Criterio de referencia canónico:** `CLAUDE.md`, `Other/bitacora_decisiones.md`, `Other/verificacion/correcciones_verificadas.md` y los textos fuente en `Docs/fuentes/txt/`.

---

## 1. Resumen ejecutivo

La presente auditoría exhaustiva de §1, §2 y el Abstract de `Docs/Technical_Report.tex` identifica desacoples metodológicos severos entre el texto redactado en la fase de propuesta (TT1) y la realidad experimental consolidada en TT2, así como omisiones bibliográficas críticas, paráfrasis no atribuidas y citas dudosas.

### Conteo de problemas identificados

| Tipo de problema | Descripción | Ocurrencias |
|:---|:---|:---:|
| **SIN_CITA** | Afirmación factual, cifra o autor nombrado en el texto sin comando `\cite` | 31 |
| **PARAFRASIS?** | Párrafo traducido o adaptado directamente de un artículo sin citarlo | 8 |
| **CONTRADICE_PROYECTO** | El texto describe el propio proyecto contradiciendo decisiones cerradas (D-xxx) | 16 |
| **SOBREAFIRMA** | Se afirma como hecho lo que es hipótesis o lo que los resultados del proyecto refutan | 11 |
| **CITA_DUDOSA** | La cita existe en el `.tex`, pero la fuente citada no respalda la afirmación | 6 |
| **FUERA_DE_TEMA** | Párrafo o digresión que no sostiene el argumento científico del capítulo | 3 |
| **CIFRA** | Valor numérico discrepante, no verificado o atribuido a fuente secundaria | 14 |
| **Total incidencias registradas** | *(Algunos párrafos acumulan más de una etiqueta)* | **89** |

### Conteo por nivel de gravedad

- **Gravedad alta (42 incidencias):** Falsedades metodológicas sobre el propio diseño (p. ej., `TorchConnector`, optimización conjunta con *parameter-shift*, rotaciones multi-eje en PauliFeatureMap), citas a páginas web comerciales de clínicas para revisiones sistemáticas de QML, atribuciones falsas de nombres de datasets (BCDR), omisión de `\cite` a autores con entradas ya existentes en el `.tex` (Wang, Xiang, Azevedo, Baccouche) y paráfrasis literales sin atribución.
- **Gravedad media (33 incidencias):** Cifras epidemiológicas con ligeras discrepancias entre secciones, afirmaciones dogmáticas sobre la superioridad cuántica o la "insuficiencia" de la geometría euclidiana desmentidas por los hallazgos experimentales (H-039, H-042), presuposición de mejora en la pregunta de investigación y objetivos específicos, y fuentes secundarias citadas en lugar de primarias (GLOBOCAN 2022).
- **Gravedad baja (14 incidencias):** Erratas tipográficas en encabezados (`Quantum embeddigs`, `cuántico.clasico`, `reportadoos`, `brechaa`, `kernerls`), espaciado en comandos LaTeX (`\cite {Key}`) y fórmulas sintácticas menores.

---

### Las 10 correcciones prioritarias en orden de importancia

1. **Eliminar la mención a `TorchConnector` y al entrenamiento de $\theta$ por *parameter-shift* (Abstract l. 443; §2.1.3 l. 766–768, 793).**  
   *Motivo:* En D-014 se adoptó la Arquitectura B: $\theta$ está fijo con semilla 42 y no se entrena; los embeddings $\langle Z_i \rangle$ se precalculan una sola vez. No hay backpropagation a través del circuito ni `TorchConnector` en el bucle del MLP. H-051 y H-054 demuestran que entrenar $\theta$ por *parameter-shift* era computacionalmente inviable en el simulador a $k=12$.
2. **Subsanar las citas dudosas de `Windsong2026_EarlyDetection` (l. 557) y `GlobalCancerStatistics2024_2` (l. 527).**  
   *Motivo:* En la l. 557 se cita la página web de un centro mamográfico privado local de Nueva York (*Windsong Radiology*) como si fuera una «revisión sistemática de aplicaciones oncológicas de QML». En la l. 527 se cita una nota de prensa de estadísticas globales de cáncer de la American Cancer Society para fundamentar la «variabilidad inter-observador entre radiólogos».
3. **Corregir la descripción de `PauliFeatureMap` en C5 (Abstract l. 435–436; OE-2 l. 652; §2.1.3 l. 779; §2.1.6 l. 835).**  
   *Motivo:* El texto afirma que PauliFeatureMap aplica rotaciones multi-eje en $X, Y, Z$. La decisión D-031 fijó de forma definitiva C5 como `pauli_feature_map(paulis=['Y', 'ZZ'])` con `reps=1` (tras descartar $X$ en D-015 y H-034 porque sobre $|+\rangle$ no codificaba información).
4. **Asignar `\cite` a las 4 obras del estado del arte que tienen `\bibitem` huérfano en el reporte (l. 529, 559, 805, 821, 825).**  
   *Motivo:* Wang et al. (2020) (`Wang2020DeepLearning`), Xiang et al. (2024) (`Xiang2024QuantumCNN`), Azevedo et al. (2022) (`Azevedo2022QuantumTransfer`) y Baccouche et al. (2022) (`Baccouche2022ResidualNN`) están extensamente discutidos con datos y tablas pero carecen de `\cite` en el texto, dejando sus `\bibitem` huérfanos (`bibliografia_revision.md` §3).
5. **Atribuir las paráfrasis literales detectadas (Xiang et al. 2024 en l. 559; Mari et al. 2020 en l. 563; El Hafidi et al. 2025 en l. 783; Shaydulin & Wild 2022 en l. 591).**  
   *Motivo:* Son traducciones casi textuales del inglés al español sin comillas ni referencia bibliográfica. En un reporte técnico y tesis universitaria esto constituye una falta ética grave de integridad académica.
6. **Corregir el nombre del dataset BCDR y matizar el resultado del 84 % de Azevedo et al. 2022 (l. 825; Tabla 2.1 l. 940).**  
   *Motivo:* El texto llama al BCDR «Barcelona Digital Breast Cancer Dataset», cuando su nombre formal es *Breast Cancer Digital Repository*. Además, presenta el 84 % de exactitud como logro cuántico, cuando la propia Tabla 4 de Azevedo et al. muestra que la ResNet clásica con *transfer learning* (C+TL) obtuvo exactamente el mismo 84 % (empate), y en hardware real cayó a 81 %.
7. **Reemplazar la fuente secundaria de GLOBOCAN 2022 (`GLOBOCAN2022` / Freihat et al. 2025) por la fuente primaria oficial Bray et al. (2024) (`Bray2024GLOBOCAN`) en la l. 484.**  
   *Motivo:* El texto atribuye las cifras directamente a la IARC, pero la cita apunta a un análisis secundario de 2025. La entrada primaria ya está verificada en `Docs/insumos/bibitems_nuevos.tex`.
8. **Neutralizar los sesgos de presuposición en la pregunta de investigación (l. 598) y objetivos (l. 641, 655).**  
   *Motivo:* Expresiones como «y qué impacto tiene dicha mejora» o «evaluar si la mejora observada en OE-3» presuponen a priori un resultado positivo. Los hallazgos del proyecto (H-039, H-042) demuestran que las transformaciones cuánticas no superaron a las representaciones clásicas en separabilidad ni en clasificación sobre este dataset.
9. **Eliminar digresiones fuera de tema: el algoritmo de Grover (l. 686) y la analogía del ENIAC (l. 676–680).**  
   *Motivo:* El algoritmo de búsqueda no estructurada de Grover ($O(\sqrt{N})$) no guarda relación matemática ni funcional con la clasificación supervisada mediante VQC ni con los métodos kernel. La analogía histórica del ENIAC carece de rigor y sustento bibliográfico.
10. **Alinear la capacidad computacional reportada en viabilidad técnica (l. 623).**  
    *Motivo:* El texto dice «circuitos de hasta 16 qubits», lo cual contradice las mediciones reales del proyecto en H-051 (donde se comprobó viabilidad en Apple Silicon M3 de 16 GiB hasta $\approx 25$ qubits para embedding de vector de estado y $\approx 22$ para kernel compute-uncompute, habiéndose fijado $k=12$ en D-013).

---

## 2. Tablas de auditoría por subsección

### Abstract (líneas 421–468)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 424 | Cáncer de mama como primera causa de muerte con 8,451 defunciones en 2024 en México | No | CIFRA / SIN_CITA | Cifra oficial INEGI 2024/2025 (`CancerMexico2025` / `INEGI2025`). Discrepa con la l. 490 que dice «aproximadamente 8,500». En un Abstract formal en inglés no suele llevar `\cite`, pero debe coincidir exactamente con el cuerpo del texto. | Media |
| 428–429 | Caídas de AUC-ROC de hasta 0.44 puntos en modelos de deep learning evaluados en datos externos | No | CIFRA / SIN_CITA | Alude directamente al estudio de Wang et al. (2020) (`Wang2020DeepLearning`). | Media |
| 430–431 | Revela limitaciones estructurales en la calidad de las representaciones morfológicas clásicas | No | SOBREAFIRMA | Wang et al. evaluaron CNN de píxeles extremo a extremo, no descriptores radiómicos morfológicos clásicos. Extrapolación no justificada. | Media |
| 435–436 | Implementación de ZZFeatureMap y PauliFeatureMap en Qiskit Aer | No | CONTRADICE_PROYECTO | En Qiskit 2.x `PauliFeatureMap` es clase deprecada en favor de `pauli_feature_map()`. C5 usa rotaciones en $Y$ y acoplamiento $ZZ$ (`['Y', 'ZZ']`, D-031), no el mapa general de Pauli. | Alta |
| 440–441 | Vectores de valores de expectativa $\langle Z_i \rangle \in [-1, 1]^n$ | No | CONTRADICE_PROYECTO | La dimensión fija del proyecto es $k = 12$ (D-013), no un genérico $n$. | Baja |
| 442–443 | Integración a un clasificador PyTorch MLP vía `TorchConnector` | No | CONTRADICE_PROYECTO | **Falso respecto a la implementación.** D-014 descartó `TorchConnector`: $\theta$ se fijó con semilla 42 (Arquitectura B), los embeddings se cachearon en disco y el MLP se entrena directamente sobre la matriz en PyTorch sin Qiskit en el bucle. | Alta |
| 444–448 | Cinco condiciones experimentales con PCA lineal como baseline | No | CONTRADICE_PROYECTO | Metodológicamente, C2 (PCA lineal) se formalizó como **control nulo** (D-016), dado que PCA preserva la separabilidad lineal y métricas afines como la distancia Fisher. | Baja |
| 451–452 | Diferencia geométrica respecto al kernel RBF clásico | No | CONTRADICE_PROYECTO | La fórmula descrita en el reporte (§3.4.2) invierte $K_C$ y $K_Q$ (H-033) y requirió regularización bajo el protocolo de Huang et al. (D-032, H-038). | Media |
| 457–460 | Determinar si el espacio de Hilbert ofrece mayor separabilidad intrínseca | No | SOBREAFIRMA | Debe matizarse: los resultados experimentales finales (H-039, H-042) demostraron que no hubo mayor separabilidad intrínseca en las transformaciones evaluadas. | Media |
| 465 | `% [Contenido del abstract — pendiente de redacción]` | No | CONTRADICE_PROYECTO | Comentario residual de plantilla sin borrar. | Baja |

---

### §1.1.1 Contexto clínico del cáncer de mama (líneas 480–517)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 482 | Cáncer más frecuente en mujeres en el mundo y principal causa de muerte, superando al de pulmón | No | SIN_CITA | Afirmación epidemiológica global factual sin respaldo. Requiere `\cite{Bray2024GLOBOCAN}` o `\cite{WHO2025}`. | Media |
| 484 | GLOBOCAN 2022: 2.3 millones casos nuevos y 670,000 defunciones en 2022 | Sí (`\cite{GLOBOCAN2022}`) | CITA_DUDOSA / CIFRA | La clave `GLOBOCAN2022` apunta a Freihat et al. (2025), un análisis secundario de proyecciones, no a la publicación oficial de la IARC. Debe sustituirse por `\cite{Bray2024GLOBOCAN}` (Bray et al., 2024, *CA Cancer J Clin*, 74(3), 229–263; datos exactos: 2,296,840 casos y 666,103 muertes). Falta punto final al párrafo. | Alta |
| 484 | Proyecciones a 2050 de incremento de más de 50 % y 70 % en casos y muertes | Sí (`\cite{StopBreastCancer2025}`) | CIFRA | Fuente web secundaria. La misma proyección está modelada en Freihat et al. (2025). | Baja |
| 486 | Tasa de mortalidad en países de bajos ingresos puede ser el doble que en desarrollados | Sí (`\cite{GlobalCancerStatistics2024}`) | CITA_DUDOSA | Entrada duplicada de `GlobalCancerStatistics2024_2` (`bibliografia_revision.md` §2.2). Ambas son notas de prensa en URL web. Typos: «diagnóstivo», «paises», «unicamente», «tambien». | Media |
| 490 | INEGI 2024: 8,500 defunciones, 99.2 % mujeres, tasa de 18.7 por 100,000 | Sí (`\cite{CancerMexico2025}`) | CIFRA | Discrepa de la l. 424 (8,451) y l. 617 (8,451). `CancerMexico2025` es nota secundaria; `INEGI2025` se cita dos veces en la misma oración. Unificar a 8,451 con `\cite{INEGI2025}`. | Media |
| 509 | Supervivencia a 5 años del 99 % en etapa localizada según American Cancer Society | Sí (`\cite{NBCF2026_EarlyDetection}`) | CITA_DUDOSA / SIN_CITA | Atribuye el dato a la *American Cancer Society*, pero cita a la *National Breast Cancer Foundation* (`NBCF2026_EarlyDetection`). La caída al 30 % en etapa avanzada y la reducción del 26 % por tamizaje carecen de `\cite`. Typos: «supervicencia», «metastátis», «somente». | Media |
| 511 | Reducción del 42 % de mortalidad entre 1989 y 2021 según ACR; variabilidad entre radiólogos | Sí (`\cite{Windsong2026_EarlyDetection}`) | CITA_DUDOSA | Cita un artículo de blog comercial de *Windsong Radiology* para estadísticas del American College of Radiology. Debe citarse una fuente primaria o institucional. | Alta |
| 513 | 1,281 mastógrafos en México en 2021 y distribución por sector | Sí (`\cite{INEGI2023}`) | CIFRA | Cifras oficiales de INEGI (comunicado 2023). Correcto en cita, revisar exactitud de porcentajes (41.1 %, 36.1 %, 22.8 %). | Baja |
| 515 | Propuesta de transformaciones cuánticas variacionales para mejorar separación de clases | No | SOBREAFIRMA | Lenguaje prospectivo no calibrado; debe formularse como evaluación rigurosa de viabilidad, no como asunción de mejora. | Media |

---

### §1.1.2 Limitaciones de los métodos clásicos de diagnóstico asistido (líneas 521–540)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 523 | Dos décadas de evolución de sistemas CADx y avance de CNN | No | SIN_CITA | Afirmación histórica de contextualización sin referencia. Se puede respaldar con `\cite{TandFOnline2021}` (Zebari et al., 2021). | Baja |
| 527 | Variabilidad entre lectores y dificultad de interpretar características sutiles | Sí (`\cite{GlobalCancerStatistics2024_2}`) | CITA_DUDOSA | **Cita espuria documentada.** Una nota de prensa de estadísticas globales de incidencia de cáncer de la ACS se usa para justificar la variabilidad visual entre radiólogos (`bibliografia_revision.md` §2.2). Debe citarse literatura médica radiológica o revisiones CAD (p. ej. Zebari et al. 2021). | Alta |
| 529 | Estudio de Wang et al. (2020) en JACR: AUC train 0.88–0.95 y caída a 0.44–0.65 en tres datasets externos | No | SIN_CITA / CIFRA | Cita faltante crítica. Se describe con detalle el artículo pero no lleva comando `\cite`. Corresponde a la entrada huérfana `\cite{Wang2020DeepLearning}` (línea 3661 del `.tex`). | Alta |
| 533 | Necesidad de mejorar interpretabilidad de CNN frente a la naturaleza de caja negra | Sí (`\cite{Kim2025GlobalBreastCancer}`) | Formato | La cita a Kim et al. respalda la frase. Error tipográfico en encabezado: `\textbf{\\ Limitaciones de interpretabilidad}{}`. | Baja |
| 537 | Sobreajuste en imágenes mamográficas de alta dimensionalidad y tamaño moderado de CBIS-DDSM | No | SIN_CITA | Concepto teórico de aprendizaje automático presentado sin soporte bibliográfico formal. | Baja |
| 539 | Necesidad de nuevos paradigmas de representación para superar restricciones del aprendizaje clásico | No | SOBREAFIRMA | Afirmación categórica que presupone que los paradigmas cuánticos superan a los clásicos, contradicha por los resultados negativos del propio proyecto. | Media |

---

### §1.1.3 Computación cuántica como alternativa (líneas 544–569)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 546 | Computación cuántica como paradigma complementario para enriquecer la codificación | No | SIN_CITA | Afirmación programática sin respaldo de literatura fundacional (p. ej. Schuld & Killoran 2019, 2022). | Baja |
| 550 | Mapeo cuántico $\phi: \mathbb{R}^n \rightarrow \mathcal{H}$ y geometría regida por productos internos cuánticos | No | SIN_CITA | Formalismo matemático estándar de embedding cuántico sin citar a Havlíček et al. (2019) (`havlicek2019supervised`) ni a Schuld & Killoran (2019) (`Schuld2019QuantumML`). | Media |
| 553 | El mapeo $\phi$ introduce correlaciones de orden superior que los métodos clásicos no capturan | No | SOBREAFIRMA | **Dogma no calibrado.** Thanasilp et al. (2024), Kübler et al. (2021) y Huang et al. (2021) demuestran que las correlaciones cuánticas sin regularización sufren concentración exponencial ($K \approx I$), perdiendo toda ventaja inductiva sobre kernels clásicos. Matizado por H-031 y H-048. | Alta |
| 557 | Revisión sistemática de aplicaciones oncológicas de QML en mamografía, radioterapia y clasificación | Sí (`\cite{Windsong2026_EarlyDetection}`) | CITA_DUDOSA | **Grave error de citación.** Cita el blog de la clínica radiológica *Windsong* para una revisión sistemática de computación cuántica oncológica. La referencia real corresponde a revisiones especializadas como Radhi et al. (2025) (`\cite{Radhi2025QuantumDeepLearning}`). | Alta |
| 559 | Trabajo de Xiang et al. (2024) sobre modelo QCCNN para diagnóstico de cáncer de mama | No | PARAFRASIS? / SIN_CITA | **Traducción literal del abstract de Xiang et al. (2024)**, p. 1 («with the goal of utilizing quantum computing’s high-dimensional data processing power and parallelism...»). Falta `\cite{Xiang2024QuantumCNN}` (entrada huérfana en línea 3675). | Alta |
| 561 | Título de subpárrafo: `\textbf{Quantum embeddigs...}` | No | Formato | Errata ortográfica en «embeddigs». | Baja |
| 563 | Codificación variacional y red cuántica completa mapeando espacios clásicos análoga a red profunda | No | PARAFRASIS? / SIN_CITA | **Traducción literal de Mari et al. (2020)**, *Quantum* 4, 340, pp. 2–3 (ecuaciones 5 y 7). No tiene cita. Corresponde a `\cite{Mari2020Transfer}` (`bibitems_noche.tex` línea 46). | Alta |
| 567 | Algoritmos QML logran resultados comparables e identifican biomarcadores novedosos en cáncer | No | SIN_CITA / SOBREAFIRMA | Afirmación sobre «biomarcadores novedosos» sin evidencia ni cita. El proyecto no analiza biomarcadores moleculares sino features radiómicas estandarizadas por IBSI. | Media |

---

### §1.2 Planteamiento del problema (líneas 573–603)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 578 | La geometría euclidiana es insuficiente para capturar correlaciones de orden superior morfológicas | No | SOBREAFIRMA | Afirmación axiomática no probada. Los métodos clásicos no lineales (SVM con kernel RBF) operan en espacios de Hilbert de dimensión infinita y superaron holgadamente a los kernels cuánticos en KTA y AUC en este dataset (H-039, H-042). | Alta |
| 578 | Caída de AUC-ROC de hasta 0.44 puntos en datos externos | No | SIN_CITA / CIFRA | Cita implícita a Wang et al. (2020) sin colocar `\cite{Wang2020DeepLearning}`. | Media |
| 584–586 | El mapeo $\phi$ introduce correlaciones de orden superior que los métodos clásicos no capturan | No | SOBREAFIRMA | Repetición textual de la afirmación no calibrada de la l. 553. | Media |
| 591 | Resultados mixtos en benchmarks; experimentos cuestionan el valor añadido de optimizar kernels | No | PARAFRASIS? / SIN_CITA | Paráfrasis de Shaydulin & Wild (2022, p. 8) y Bowles et al. (2024, p. 3) sobre optimización de hiperparámetros y elección del feature map. Corresponde a `\cite{Shaydulin2022Bandwidth}` y `\cite{Bowles2024Benchmarking}`. | Alta |
| 598 | Formulación de la pregunta de investigación («¿En qué medida... y qué impacto tiene dicha mejora...?») | No | SOBREAFIRMA / SESGO | **Presuposición de resultado:** La frase «y qué impacto tiene dicha mejora» asume que la transformación cuántica mejora la separabilidad. Ver análisis detallado en la Sección 5. | Alta |
| 601 | Las tres dimensiones (representación, clasificación, viabilidad) corresponden a OE-3, OE-5 y OE-6 | No | Vínculo metodológico | Correspondencia formal correcta, pero debe actualizarse con las respuestas empíricas obtenidas en el proyecto. | Baja |

---

### §1.3 Justificación (líneas 607–631)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 611 | Mayoría de estudios QML usan datos sintéticos o tabulares de baja dimensión | No | SIN_CITA | Diagnóstico correcto del estado del arte, pero sin citas a revisiones (p. ej. Radhi et al. 2025 o Bowles et al. 2024). | Baja |
| 613 | Retoma las dos líneas de trabajo futuro de Azevedo et al. (2022): masas/calcificaciones y espacio de Hilbert | No | SIN_CITA | Mención explícita de Azevedo et al. (2022) sin comando `\cite`. Corresponde a `\cite{Azevedo2022QuantumTransfer}` (línea 3682 del `.tex`). | Alta |
| 617 | 8,451 defunciones registradas en México en 2024; supervivencia 99 % vs 30 % | No | CIFRA / SIN_CITA | Reitera cifras de l. 424 y 509 sin añadir citas directas. | Baja |
| 622 | CBIS-DDSM: 1,566 participantes, partición train/test por categoría BI-RADS | No | SIN_CITA / CONTRADICE_PROYECTO | Falta citar a Lee et al. (2017) (`Lee2017CBISDDSM`) y Clark et al. (2013) (`Clark2013TCIA`). Además, 1,566 son pacientes pero corresponden a 3,568 registros/casos. La partición oficial de train/test es por caso/paciente, no por BI-RADS en el pipeline de la tesis. | Media |
| 623 | Simulación en Qiskit Aer con «circuitos de hasta 16 qubits» | No | CONTRADICE_PROYECTO | **Inconsistencia con mediciones reales.** H-051 comprobó viabilidad hasta $\approx 25$ qubits para embedding y $\approx 22$ para kernel en la máquina del proyecto (M3, 16 GiB). El diseño fijó $k = 12$ por costo y balance de familias radiómicas (D-013), no por tope de 16 qubits. | Alta |
| 627 | Dominios tabulares comparativos: Wisconsin, SEER, GBSG | No | SIN_CITA | Menciona los datasets tabulares clásicos utilizados por Xiang et al. (2024) sin citarlos. | Baja |

---

### §1.4 Objetivos (líneas 635–658)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 641 | Objetivo general: «para determinar si la mejora en separabilidad se traduce en una mejora en la capacidad de clasificación...» | No | SOBREAFIRMA / SESGO | Presupone la existencia de una «mejora en separabilidad». | Media |
| 651 | OE-1: «normalización... extracción mediante features radiómicas (PyRadiomics) o un encoder CNN preentrenado» | No | CONTRADICE_PROYECTO | **Doble discordancia:** 1) La normalización a [0, 1] en M2 fue eliminada en favor de intensidades crudas de 16 bits (D-009, D-010, D-022) y el escalado angular por cuantiles se trasladó a M4 (D-025). 2) La opción de encoder CNN fue descartada formalmente en D-006 a favor exclusivo de PyRadiomics (Estrategia A). | Alta |
| 652 | OE-2: Cincondiciones; «asegurando que todas las condiciones produzcan vectores de representación de dimensión $k$» | No | CONTRADICE_PROYECTO | En M5, C5 usa `['Y', 'ZZ']` (D-031). Además, los kernels cuánticos evaluados en M6 y en el QSVM (X4) operan sobre matrices de Gram $N \times N$, no sobre vectores de dimensión $k$. Solo el MLP del M7 recibe vectores $\langle Z_i \rangle \in \mathbb{R}^k$. | Media |
| 653 | OE-3: Métrica de *geometric difference* para cuantificar si el espacio cuántico captura estructura inaccesible | No | CONTRADICE_PROYECTO | La fórmula teórica de $g$ en el reporte (§3.4.2) invierte $K_C$ y $K_Q$ (H-033) y requirió regularización (D-032, H-038). | Media |
| 655 | OE-5: «Evaluar si la mejora en separabilidad observada en OE-3 se traduce en una mejora...» | No | SOBREAFIRMA / SESGO | Presupone la «mejora en separabilidad observada en OE-3». Al no haber mejora cuántica en OE-3, la evaluación comprueba la hipótesis nula/consistencia del ordenamiento. | Media |
| 656 | OE-6: Evaluar restricciones computacionales del simulador cuántico para viabilidad en salud | No | Correcto | Se alinea con los hallazgos de viabilidad de H-051 y H-052. | Baja |

---

### §1.5 Alcance y limitaciones (líneas 662–688)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 666 | Simulación clásica sin ruido cuántico físico como decisión deliberada de diseño experimental | No | Correcto | Planteamiento metodológico impecable acorde a la regla 3 de `CLAUDE.md`. | Baja |
| 670 | «El objetivo no es superar lo existente, sino explorar lo posible... el objetivo no es superar a una CNN de última generación» | No | PARAFRASIS? / SIN_CITA | Desarrolla la misma postura crítica expuesta por Schuld & Killoran (2022) (*PRX Quantum* 3, 030101) sobre la futilidad de buscar "quantum advantage" inmediata en benchmarks clásicos. Conviene respaldar con `\cite{SchuldKilloran2022Advantage}`. | Media |
| 676–680 | Analogía histórica con la máquina ENIAC (1945/1946) y mención del chip IBM Osprey de 433 qubits | No | FUERA_DE_TEMA / SIN_CITA | Digresión retórica sin citas ni relación con el pipeline radiómico-cuántico. Osprey (433 q) no se usó ni simula en este trabajo. Eliminar o condensar severamente. | Media |
| 684 | Limitaciones del hardware NISQ (qubits, fidelidad de compuertas y conectividad limitada) | No | PARAFRASIS? / SIN_CITA | Concepto y terminología acuñados por Preskill (2018). Falta `\cite{Preskill2018NISQ}` (`bibitems_noche.tex` línea 33). | Media |
| 686 | Algoritmo de Grover y búsqueda no estructurada $O(\sqrt{N})$ en dispositivos NISQ | No | FUERA_DE_TEMA / SIN_CITA | **Párrafo completamente ajeno al tema de la tesis.** El algoritmo de Grover resuelve búsqueda no estructurada en bases de datos con aceleración cuadrática; no tiene aplicación ni relevancia alguna en transformaciones variacionales ni en kernels supervisados sobre imágenes médicas. | Alta |

---

### §2.1.1 Machine Learning clásico en el diagnóstico mamográfico (líneas 701–722)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 703 | Sistemas CAD desarrollados desde 1990 en dos etapas: extracción manual y clasificación | No | SIN_CITA | Afirmación histórica estándar que requiere cita a revisiones consolidadas (p. ej. Zebari et al. 2021). | Baja |
| 707 | GLCM como técnica más utilizada en CAD mamográfico; descriptores de forma, margen y distribución espacial | Sí (`\cite{TandFOnline2021}`) | CITA_DUDOSA / Metadata | En el `.tex` original, `TandFOnline2021` (l. 3701) era una plantilla vacía de *AI Magazine*. Corregida en `bibitems_nuevos.tex` como Zebari et al. (2021), *Applied Artificial Intelligence*, 35(15), 2157–2203 (`bibliografia_revision.md` §1). | Media |
| 711 | 44 % de estudios entre 2020 y 2025 emplearon SVM como clasificador predominante en mamografía | Sí (`\cite{Mashekova2025AIBreastCancer}`) | CIFRA | Cifra específica del 44 % reportada por Mashekova et al. (2025). | Baja |
| 713 | Comparación de SVM, RF, ANN, NB y DT con features GLCM y GLRLM | Sí (`\cite{Avci2023MammographyEnhancement}`) | CIFRA | Respalda la afirmación. Correcto. | Baja |
| 718 | Evaluación en CBIS-DDSM: ResNet-50 AUC 0.95, XGBoost 0.90, SVM 0.84 | Sí (`\cite{Anez2025AIPipeline}`) | CIFRA | Cifras comparativas de Anez et al. (2025). | Baja |
| 720 | Capacidad discriminativa limitada por la extracción manual; emergencia de deep learning y QML | No | SOBREAFIRMA | Typo: «impresindible». Asume que la extracción manual es deficiente per se, cuando las features radiómicas con SVM clásico alcanzaron AUC de 0.80 en calcificaciones en el propio proyecto. | Media |

---

### §2.1.2 Deep Learning en el diagnóstico mamográfico (líneas 726–748)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 730 | CNN desde 1995 y auge desde 2012 con AlexNet; VGG, ResNet, DenseNet, InceptionV3 | Sí (`\cite{Abdelhafiz2019DeepCNN}`) | Formato | Typos: «paradignma», «Alex-Net». | Baja |
| 734 | Shen et al. (2019) en CBIS-DDSM: AUC individual 0.88 y ensamble 0.91 con sensibilidad 86.1 % | Sí (`\cite{Shen2019DeepLearning}`) | Formato / CIFRA | Typo: «Shen et. al \cite{Shen2019DeepLearning}». Las cifras coinciden con la fuente. | Baja |
| 736 | Microcalcificaciones: variantes EfficientNet superan a ResNet en F1-score; EfficientNet-B3 en CBIS-DDSM | Sí (`\cite{Shia2025MicrocalcClassification}`) | Formato / CIFRA | Typo: «performace». Refuerza la separación de masas y calcificaciones. | Baja |
| 740 | Wang et al. (2020): evaluación sistemática de 6 modelos sobre 4 datasets; caídas a 0.44–0.65 en datos externos | No | SIN_CITA / CIFRA | **Falta cita crítica a `\cite{Wang2020DeepLearning}`** (línea 3661 del `.tex`). Además, repite casi textualmente la frase espuria de la l. 527 sobre variabilidad entre lectores. | Alta |
| 742 | Investigación futura: interpretabilidad, privacidad y generalización en programas de tamizaje | No | PARAFRASIS? / SIN_CITA | Paráfrasis directa de la frase de Kim et al. (2025) citada en la l. 533, aquí dejada sin autor ni cita. | Media |
| 746 | Motivación de proyectar a espacio de Hilbert para generar representaciones con mayor separabilidad | No | SOBREAFIRMA | Debe matizarse conforme a la regla 1 de `CLAUDE.md`: el objetivo es evaluar la viabilidad de la representación, no dar por sentado que produce mayor separabilidad. | Media |

---

### §2.1.3 Fundamentos de quantum machine learning y codificación cuántica de datos (líneas 751–795)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 753 | Título de subsección: `\textbf{El origen teórico, QML como extensión de kernerls}` | No | Formato | Errata ortográfica en «kernerls». | Baja |
| 755–756 | Schuld y Killoran (2019): computación cuántica análoga a métodos kernel en espacios de Hilbert intratables | Sí (`\cite{Schuld2019QuantumML}`) | CITA_DUDOSA | **Duplicado bibliográfico.** `Schuld2019QuantumML` (l. 3757) es idéntico a `schuld2019quantum` (l. 3831) (`bibliografia_revision.md` §2.1). Unificar a una sola clave. | Media |
| 758 | Havlíček et al. (2019) en IBM Nature: formalización operacional de ZZFeatureMap y ventaja cuántica | No | SIN_CITA | **Falta cita indispensable.** Havlíček et al. (2019) es el artículo seminal que introduce el circuito ZZFeatureMap utilizado en el proyecto. Requiere `\cite{havlicek2019supervised}` (línea 3816 del `.tex`). | Alta |
| 762 | Definición de VQC y optimización híbrida cuántico-clásica | Sí (`\cite{Long2025HybridQCQ}`) | Correcto | Respalda la definición general de VQC en la era NISQ. | Baja |
| 764 | Estructura de 3 bloques: mapa $U(x)$, ansatz $W(\theta)$ y medición $\langle Z_i \rangle$ | No | Correcto | Coincide con el esquema experimental del proyecto. | Baja |
| 766–768 | Optimización de $\theta$ por *parameter-shift* y entrenamiento conjunto con PyTorch mediante backpropagation | No | CONTRADICE_PROYECTO | **Grave falsedad metodológica respecto a la tesis.** En Arquitectura B (D-014), $\theta$ **no se entrena**, se fija con semilla 42. Los embeddings $\langle Z_i \rangle$ se calculan una sola vez. No se usa *parameter-shift* en el entrenamiento ni optimización conjunta. H-051 y H-054 demuestran que entrenar $\theta$ por parameter-shift tardaba $\approx 3,600$ veces más y no era viable en simulación a $k=12$. | Alta |
| 772 | Integración de codificación cuántica contribuye a mejorar precisión y F1 | No | SIN_CITA / SOBREAFIRMA | Afirmación genérica optimista sin sustento bibliográfico ni experimental en el proyecto. | Media |
| 774 | Título de subpárrafo: «Los tres tipos de codifiacación...» | No | Formato | Errata ortográfica en «codifiacación». | Baja |
| 777 | Angle encoding: codifica componentes como rotaciones unarias $R_y(x_i)$ | No | Correcto | Definición matemática estándar de la literatura. | Baja |
| 778 | ZZFeatureMap: compuertas de entrelazamiento con productos $e^{i x_i x_j Z_i Z_j}$ | No | Correcto | Definición formal acorde a Havlíček et al. (2019). | Baja |
| 779 | PauliFeatureMap descrito como rotaciones alrededor de los tres ejes $(X, Y, Z)$ y entrelazamiento complejo | No | CONTRADICE_PROYECTO | **Inconsistencia con la decisión de diseño.** C5 no usa rotaciones en $X, Y, Z$; tras revertir $Z$ (D-002, H-012) y $X$ (D-015, H-034), D-031 fijó C5 como `pauli_feature_map(paulis=['Y', 'ZZ'])` con `reps=1`. | Alta |
| 783 | Estudio de cáncer de pulmón con QSVM: ZZ 0.91 y Pauli 0.96; factores de naturaleza de datos y resiliencia | No | PARAFRASIS? / SIN_CITA / CIFRA | **Paráfrasis casi literal de El Hafidi, Toufah & Kadim (2025)** (arXiv:2506.03272, pp. 6 y 9). Falta `\cite{ElHafidi2025}` (`bibitems_nuevos.tex` l. 111). Omite que su SVM clásico con RBF también obtuvo 0.95 (`correcciones_verificadas.md` §2). Typo: «codifiación». | Alta |
| 788 | Fenómeno de *barren plateau* en VQC profundos: gradientes convergen exponencialmente a cero | No | SIN_CITA | Concepto teórico fundamental de McClean et al. (2018) y Arrasmith et al. (2021). Falta `\cite{McClean2018Barren}` y `\cite{Arrasmith2021}`. | Alta |
| 789 | Justifica profundidad moderada e «inicialización cuidadosa de los parámetros $\theta$» | No | CONTRADICE_PROYECTO | En el proyecto $\theta$ no se optimiza con gradientes (D-014), por lo que el barren plateau en el entrenamiento de $\theta$ no es el obstáculo real. El fenómeno que impacta al proyecto es la **concentración exponencial del kernel** (Thanasilp et al. 2024, H-031). | Media |
| 793 | Qiskit Machine Learning: `EstimatorQNN` y `TorchConnector` como capa `nn.Module` de PyTorch | No | CONTRADICE_PROYECTO | **Falso respecto a la implementación.** Ni `TorchConnector` ni `EstimatorQNN` forman parte del flujo de M5 ni M7 (D-014). M5 usa `Statevector` exacto directo y M7 entrena el MLP estándar de PyTorch sobre tensores cacheados. | Alta |

---

### §2.1.4 Modelos híbridos cuántico-clásico en el sector salud (líneas 799–811)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 799 | Título: `\subsubsection{Modelos híbridos cuántico.clasico en el sector salud}` | No | Formato | Errata ortográfica: punto en lugar de guion (`cuántico.clasico`). | Baja |
| 801 | Revisión sistemática de 28 estudios (2018–2024) en tumores cerebrales, piel y COVID-19 | Sí (`\cite {Radhi2025QuantumDeepLearning}`) | Formato | Espacio innecesario en `\cite {Key}`. Contenido respaldado por la fuente. | Baja |
| 805 | Xiang et al. (2024): modelo QCCNN sobre GBSG, SEER, WDBC con mejoras de hasta 5 % en accuracy | No | SIN_CITA / CIFRA | Falta comando `\cite{Xiang2024QuantumCNN}` (entrada huérfana en línea 3675 del `.tex`). | Alta |
| 805 | Trabajo en BreastMNIST con ResNet50 y QNN: 69 % de accuracy frente a 67 % de métodos híbridos | No | SIN_CITA / CIFRA | **Trabajo sin nombrar autores ni cita.** Se trata de Rifat et al. (2024), *ICCIT*, IEEE, pp. 1464–1469 (`Docs/insumos/fuentes_bib/Rifat2024.json`). El «frente a 67 %» no está verificado en la fuente primaria (`correcciones_verificadas.md` §2). | Alta |
| 807 | Título de subpárrafo: `\textbf{Limitaciones comunes reportadoos}` | No | Formato | Errata ortográfica en «reportadoos». | Baja |
| 809 | Tres limitaciones: simulación sin ruido, datasets tabulares o imágenes 28×28, falta de análisis de separabilidad | No | Correcto | Diagnóstico certero que justifica la aportación del proyecto. | Baja |

---

### §2.1.5 Trabajos específicos sobre el dataset CBIS-DDSM (líneas 815–827)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 817 | CBIS-DDSM como dataset de referencia con partición train-test predefinida y máscaras ROI validadas | No | SIN_CITA | Falta citar a Lee et al. (2017) (`Lee2017CBISDDSM`). Typo de redacción: «se ha convertido como» en vez de «se ha convertido en». | Media |
| 821 | Shen et al. (2019): línea base con CNN sobre CBIS-DDSM alcanzando AUC de 0.91 con ensamble | No | SIN_CITA | Se nombró y citó previamente en l. 734, pero en este párrafo no lleva `\cite{Shen2019DeepLearning}`. | Baja |
| 821 | Baccouche et al. (2022): ensamble ResNet alcanza 95.13 % en patología y 90.02 % en forma sobre CBIS-DDSM | No | SIN_CITA / CIFRA | Cita faltante de primer orden. Describe exhaustivamente el artículo pero no incluye `\cite{Baccouche2022ResidualNN}` (entrada huérfana en l. 3745 del `.tex`). | Alta |
| 825 | Azevedo et al. (2022): quantum transfer learning con angle embedding sobre BCDR (84 % accuracy) | No | SIN_CITA | **Falta cita crítica a `\cite{Azevedo2022QuantumTransfer}`** (entrada huérfana en l. 3682 del `.tex`). | Alta |
| 825 | BCDR denominado «Barcelona Digital Breast Cancer Dataset» | No | CONTRADICE_PROYECTO | **Nombre falso de dataset.** Las siglas BCDR corresponden a *Breast Cancer Digital Repository* (repositorio portugués/español de la Universidade do Porto). Documentado en `CLAUDE.md` y `correcciones_verificadas.md` §2. | Alta |
| 825 | Se destaca el 84 % de accuracy como logro del modelo híbrido cuántico-clásico | No | SOBREAFIRMA / CIFRA | En la Tabla 4 (p. 10–11) de Azevedo et al. (2022), la ResNet clásica con *transfer learning* (C+TL) también obtuvo exactamente 84 % (empate); la diferencia estuvo en AUC (0.77 vs 0.58), y en hardware real cayó a 81 %. La conclusión de los autores fue: «*It is too soon to say whether or not QML can be an advantage*». | Alta |
| 825 | Trabajo futuro de Azevedo: evaluar distribución en el espacio de Hilbert para verificar separabilidad | No | PARAFRASIS? | Cita casi textual de las conclusiones de Azevedo et al. (p. 12). | Media |

---

### §2.1.6 Tabla comparativa y brechas identificadas (líneas 831–974)

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |
|:---:|:---|:---:|:---|:---|:---:|
| 833 | Texto introductorio a la Tabla 2.1 | No | Formato | Typos en el párrafo: «caractericticas», «brechaa». | Baja |
| 835 | Uso de Qiskit con ZZFeatureMap y PauliFeatureMap en contraste con PennyLane | No | CONTRADICE_PROYECTO | Debe precisarse que C5 es `pauli_feature_map(paulis=['Y','ZZ'])` con `reps=1` (D-031). | Media |
| 863 | Fila Shen et al. (2019) en Tabla `tab:estado_arte` | No | SIN_CITA | Debe incluir `\cite{Shen2019DeepLearning}`. | Baja |
| 873 | Fila Wang et al. (2020) en Tabla `tab:estado_arte` | No | SIN_CITA | Debe incluir `\cite{Wang2020DeepLearning}`. | Alta |
| 883 | Fila Baccouche et al. (2022) en Tabla `tab:estado_arte` | No | SIN_CITA | Debe incluir `\cite{Baccouche2022ResidualNN}`. | Alta |
| 895 | Fila Bilal et al. (2025) (Q-BGWO + SqueezeNet + SVM) | No | SIN_CITA / Huérfana | No tiene `\cite` y no existe `\bibitem` en `Technical_Report.tex` ni en insumos. Falta agregar referencia completa (`bibliografia_revision.md` §3). | Alta |
| 905 | Fila Singh et al. (2025) (SeQTLBOGA + SVM) | No | SIN_CITA / Huérfana | No tiene `\cite` ni `\bibitem` en la bibliografía del proyecto. | Alta |
| 917 | Fila Ajlouni et al. (2023) (Hybrid QCNN en Brain MRI) | No | SIN_CITA / Huérfana | No tiene `\cite` ni `\bibitem` en la bibliografía del proyecto. | Alta |
| 927 | Fila Xiang et al. (2024) en Tabla `tab:estado_arte` | No | SIN_CITA | Debe incluir `\cite{Xiang2024QuantumCNN}`. | Alta |
| 939 | Fila Azevedo et al. (2022) en Tabla `tab:estado_arte` | No | SIN_CITA | Debe incluir `\cite{Azevedo2022QuantumTransfer}`. | Alta |
| 953–961 | Fila de Sánchez García (2026) (el presente trabajo): columna AUC-ROC reporta «Por det.» | No | CONTRADICE_PROYECTO / CIFRA | Los resultados de clasificación ya están completamente determinados desde el 2026-10-06 en M7 y M8 (H-042, H-049). Masas: C1 0.651, C3 0.646, C4 0.530, C5 0.581. Calcificaciones: C1 0.769, C3 0.758, C4 0.633, C5 0.652. | Alta |

---

## 3. Paráfrasis localizadas con citas textuales verificadas

A continuación se detallan las paráfrasis literales y conceptuales detectadas en §1 y §2. Cada caso incluye la cita textual original verificada contra los archivos de texto de las fuentes (`Docs/fuentes/txt/<Clave>/pNNN.txt`) mediante el algoritmo de normalización de `verificar_citas_fichas.py`.

### 1. Xiang et al. (2024) — §1.1.3 (l. 559)

- **Texto en el reporte (.tex):**  
  *«Se presenta un enfoque de diagnóstico de cáncer de mama basado en redes neuronales convolucionales híbridas cuántico-clásicas, con el objetivo de aprovechar la capacidad de procesamiento de datos de alta dimensión y el paralelismo de la computación cuántica para incrementar la eficiencia y precisión del diagnóstico; cuando se trabaja con conjuntos de datos a gran escala y complejos, las CNN clásicas generalmente demandan grandes recursos computacionales y tiempo, y su capacidad limitada de generalización dificulta mantener un rendimiento consistente entre múltiples conjuntos de datos.»*
- **Texto original en la fuente:**  
  «we present a quantum hybrid classical convolutional neural network (QCCNN) based breast cancer diagnosis approach with the goal of utilizing quantum computing’s high-dimensional data processing power and parallelism to increase diagnosis efficiency and accuracy.» (Xiang2024QuantumCNN, p. 1)  
  «When working with large-scale and complicated datasets, classical convolutional neural network (CNN) and other machine learning techniques generally demand a large amount of computational resources and time. Their restricted capacity for generalization makes it challenging to maintain consistent performance across multiple data sets.» (Xiang2024QuantumCNN, p. 1)
- **Diagnóstico:** Traducción literal directa del resumen del artículo de Xiang et al., colocada en el reporte sin comillas y sin comando `\cite`. Corresponde a `\cite{Xiang2024QuantumCNN}`.

---

### 2. Mari et al. (2020) — §1.1.3 (l. 563)

- **Texto en el reporte (.tex):**  
  *«El proceso de codificación de un vector real en un estado cuántico puede realizarse mediante una capa de embedding variacional aplicada a un estado de referencia; la red cuántica completa, incluyendo la capa de embedding inicial y la medición final, mapea un espacio vectorial clásico a otro espacio vectorial clásico dependiente de pesos clásicos, y aunque contiene un cómputo cuántico oculto en el circuito cuántico, es funcionalmente análoga a una red clásica profunda.»*
- **Texto original en la fuente:**  
  «In order to inject classical data in a quantum network we need to embed a real vector x into a quantum state |x⟩. This can also be done by a variational embedding layer depending on x and applied to some reference state» (Mari2020Transfer, p. 2)  
  «The full network is a map from a classical vector space to a classical vector space depending on classical weights. Therefore, even though it may contain a quantum computation hidden in the quantum circuit, if considered from a global point of view, Q is simply a black-box analogous to the classical deep network» (Mari2020Transfer, p. 3)
- **Diagnóstico:** Traducción directa consecutiva de las ecuaciones 5 y 7 y de sus explicaciones en Mari et al. (2020) sobre redes neuronales híbridas y transfer learning cuántico. No se incluye cita. Corresponde a `\cite{Mari2020Transfer}` (`bibitems_noche.tex`).

---

### 3. Shaydulin & Wild (2022) — §1.2 (l. 591)

- **Texto en el reporte (.tex):**  
  *«...los experimentos cuestionan el valor añadido general de aplicar optimización cuántica de kernels, para la cual el costo computacional adicional no necesariamente se traduce en mejor desempeño de clasificación. En cambio, se sugiere que una elección cuidadosa del feature map cuántico en conexión con una hiperparametrización apropiada puede resultar más efectiva.»*
- **Texto original en la fuente:**  
  «Careful consideration of hyperparameters of quantum kernels may enable the tuning of the inductive bias of the model in a way that is infeasible classically, providing a potential path to quantum advantage in machine learning.» (Shaydulin2022Bandwidth, p. 8)
- **Diagnóstico:** Paráfrasis conceptual de la discusión de Shaydulin & Wild sobre el ancho de banda (*bandwidth*) y la optimización de hiperparámetros en kernels cuánticos frente a mapas entrenables costosos. Debe citarse `\cite{Shaydulin2022Bandwidth}`.

---

### 4. Azevedo et al. (2022) — §1.3 (l. 613) y §2.1.5 (l. 825)

- **Texto en el reporte (.tex):**  
  *«Tercero, retoma y ejecuta las dos líneas de trabajo futuro identificadas por Azevedo et al. (2022) como pendientes: la separación del análisis por tipo de hallazgo mamográfico y la evaluación de la distribución de datos en el espacio cuántico resultante... señalando como trabajo futuro explícito la necesidad de evaluar la distribución de los datos en el espacio de Hilbert resultante para verificar la separabilidad de clases.»*
- **Texto original en la fuente:**  
  «As future work, an interesting approach could be to separate the dataset into masses and calcifications and only then perform classification.» (Azevedo2022QuantumTransfer, p. 12)  
  «Lastly, the best way to know how well this model performs would be to see how the data appears in our Hilbert space. Ideally, both classes would appear very separately in it, as tight clusters.» (Azevedo2022QuantumTransfer, p. 12)  
  «It is too soon to say whether or not QML can be an advantage. Our results only point to a good generalization of complex data which needs further testing.» (Azevedo2022QuantumTransfer, p. 11)
- **Diagnóstico:** Las líneas de trabajo futuro están exactamente tomadas de la p. 12 de Azevedo et al. (2022), lo cual es metodológicamente correcto (cierra la discrepancia con Incudini en D-019), pero se omitió colocar `\cite{Azevedo2022QuantumTransfer}`. Asimismo, la afirmación sobre el 84 % omite la conclusión de los autores en la p. 11 que relativiza el hallazgo como un empate con la línea base clásica.

---

### 5. El Hafidi, Toufah & Kadim (2025) — §2.1.3 (l. 783)

- **Texto en el reporte (.tex):**  
  *«Un estudio reciente aplicó los tres métodos a la clasificación de cáncer de pulmón con QSVM, obteniendo que ZZFeatureMap alcanzó una accuracy de 0.91 y F1-score de 0.91, mientras que PauliFeatureMap logró un rendimiento consistente de 0.96 en todas las métricas incluyendo accuracy, precisión, recall y F1-score; la elección del mapa apropiado depende de dos factores principales, la naturaleza de los datos y la resiliencia al ruido del dispositivo cuántico.»*
- **Texto original en la fuente:**  
  «The choice of an appropriate feature map depends on two major factors: the nature of the data and the noise resilience of the quantum device.» (ElHafidi2025, p. 6)  
  «for ZZFeatureMap, the results were an accuracy of 0.91, precision of 0.87, recall of 0.96, specificity of 0.85, and F1-score of 0.91; and for PauliFeatureMap, the model achieved a consistent performance of 0.96 across all metrics, including accuracy, precision, recall, specificity, and F1-score.» (ElHafidi2025, p. 9)
- **Diagnóstico:** Traducción literal de los resultados numéricos y de la conclusión de diseño de El Hafidi et al. (arXiv:2506.03272). Debe añadirse `\cite{ElHafidi2025}` (`bibitems_nuevos.tex` l. 111).

---

### 6. Preskill (2018) — §1.5 (l. 684)

- **Texto en el reporte (.tex):**  
  *«Las limitaciones inherentes del hardware NISQ (número restringido de qubits, fidelidad imperfecta de compuertas y conectividad limitada entre qubits) imponen obstáculos fundamentales, y lograr una ventaja cuántica definitiva sobre los métodos clásicos para problemas prácticos permanece sin resolver.»*
- **Texto original en la fuente:**  
  «We care about the connectivity among the qubits — for which pairs of qubits in our device can we perform an accurate two-qubit gate?» (Preskill2018NISQ, p. 5)  
  «Whether that quantum advantage really exists is currently an open question, but we will soon have the opportunity to explore the question experimentally using quantum hardware.» (Preskill2018NISQ, p. 7)
- **Diagnóstico:** Paráfrasis directa de las definiciones y limitaciones del cómputo NISQ acuñadas por John Preskill en 2018. Requiere `\cite{Preskill2018NISQ}` (`bibitems_noche.tex`).

---

### 7. McClean et al. (2018) — §2.1.3 (l. 788)

- **Texto en el reporte (.tex):**  
  *«A medida que el circuito aumenta en número de qubits y capas, la optimización se vuelve exponencialmente plana, con gradientes que convergen a cero. Esto hace el entrenamiento prácticamente imposible para circuitos de gran profundidad con una inicialización aleatoria de parámetros.»*
- **Texto original en la fuente:**  
  «Specifically, we show that for a wide class of reasonable parameterized quantum circuits, the probability that the gradient along any reasonable direction is non-zero to some fixed precision is exponentially small as a function of the number of qubits.» (McClean2018Barren, p. 1)
- **Diagnóstico:** Paráfrasis del teorema fundacional de *barren plateaus* de McClean et al. (2018) sin citar la obra. Corresponde a `\cite{McClean2018Barren}` (`bibitems_noche.tex`).

---

### 8. Lee et al. (2017) — §1.3 (l. 622)

- **Texto en el reporte (.tex):**  
  *«Sus 1,566 participantes, partición train/test por categoría BI-RADS, y metadatos clínicos estructurados en archivos CSV representan una base de datos suficientemente robusta...»*
- **Texto original en la fuente:**  
  «The data were split into a training set and a testing set based on the BI-RADS category. This allows for an appropriate stratification for researchers working on CADe as well as CADx.» (Lee2017CBISDDSM, p. 5)
- **Diagnóstico:** La mención de la «partición train/test por categoría BI-RADS» proviene directamente de la descripción metodológica de Lee et al. (2017) sobre la curación del CBIS-DDSM. Falta `\cite{Lee2017CBISDDSM}` (`bibitems_noche.tex`).

---

### 9. Thanasilp et al. (2024) — §2.1.3 (l. 780, 789)

- **Texto en el reporte (.tex):**  
  *«Su mayor expresividad tiene como contrapartida una mayor sensibilidad al ruido cuántico, relevante incluso en simulación cuando el número de shots es limitado...»*
- **Texto original en la fuente:**  
  «We show that, under certain conditions, values of quantum kernels over different input data can be exponentially concentrated (in the number of qubits) towards some fixed value. Thus on training with a polynomial number of measurements, one ends up with a trivial model where the predictions on unseen inputs are independent of the input data.» (Thanasilp2024, p. 1)
- **Diagnóstico:** El reporte alude vagamente a "sensibilidad", pero omite el fundamento formal de concentración exponencial en kernels cuánticos que Thanasilp et al. demostraron y que condicionó los hallazgos H-031 y H-052 de este proyecto. Debe citarse `\cite{Thanasilp2024}` (`bibitems_nuevos.tex`).

---

### 10. Huang et al. (2021) — §1.1.3 (l. 550) y §1.2 (l. 584)

- **Texto en el reporte (.tex):**  
  *«...determinar si esta propiedad se cumple para las características morfológicas del dataset CBIS-DDSM... la geometría está determinada por los productos internos cuánticos...»*
- **Texto original en la fuente:**  
  «Following these constructions, in numerical experiments, we find that a variety of common quantum models in the literature perform similarly or worse than classical ML on both classical and quantum datasets due to a small geometric difference. The small geometric difference is a consequence of the exponentially large Hilbert space employed by existing quantum models, where all inputs are too far apart.» (huang2021power, p. 2)
- **Diagnóstico:** El concepto de que en espacios de Hilbert exponenciales las entradas quedan demasiado alejadas (*"where all inputs are too far apart"*) y la métrica de *geometric difference* provienen de Huang et al. (2021). Debe citarse `\cite{huang2021power}` en §1.

---

### 11. Schuld & Killoran (2022) — §1.5 (l. 670)

- **Texto en el reporte (.tex):**  
  *«Un error frecuente en la evaluación de trabajos de QML aplicado consiste en juzgar su validez en función de si el modelo cuántico supera en precisión a los mejores modelos clásicos disponibles... El objetivo del presente trabajo no es demostrar que los quantum embeddings superan a una CNN de última generación en AUC-ROC.»*
- **Texto original en la fuente:**  
  «Almost all branches of quantum machine learning research have been heavily framed by the question of “beating” classical machine learning in some figure of merit» (SchuldKilloran2022Advantage, p. 5)
- **Diagnóstico:** La postura epistemológica sobre no limitar la investigación en QML a "vencer" a los modelos clásicos en benchmarks comerciales es el argumento central de Schuld & Killoran (2022). Corresponde a `\cite{SchuldKilloran2022Advantage}` (`bibitems_noche.tex`).

---

## 4. Lista de `\cite` faltantes y correspondencia de claves

La siguiente tabla consolida todas las referencias que deben ser incorporadas a §1, §2 o a la tabla comparativa `tab:estado_arte`, indicando la clave exacta verificada y el archivo donde se encuentra su `\bibitem`.

| Obra / Autores | Clave verificada | Líneas afectadas en `Technical_Report.tex` | Archivo de origen del `\bibitem` |
|:---|:---|:---:|:---|
| Wang et al. (2020) | `Wang2020DeepLearning` | 428, 529, 740, 873 | `Docs/Technical_Report.tex` (l. 3661) |
| Xiang et al. (2024) | `Xiang2024QuantumCNN` | 559, 805, 927 | `Docs/Technical_Report.tex` (l. 3675) |
| Azevedo et al. (2022) | `Azevedo2022QuantumTransfer` | 613, 825, 939 | `Docs/Technical_Report.tex` (l. 3682) |
| Baccouche et al. (2022) | `Baccouche2022ResidualNN` | 821, 883 | `Docs/Technical_Report.tex` (l. 3745) |
| Havlíček et al. (2019) | `havlicek2019supervised` | 758 | `Docs/Technical_Report.tex` (l. 3816) |
| Lee et al. (2017) (CBIS-DDSM) | `Lee2017CBISDDSM` | 438, 622, 651, 817 | `Docs/insumos/bibitems_noche.tex` (l. 11) |
| Clark et al. (2013) (TCIA) | `Clark2013TCIA` | 622, 817 | `Docs/insumos/bibitems_noche.tex` (l. 18) |
| Mari et al. (2020) | `Mari2020Transfer` | 563 | `Docs/insumos/bibitems_noche.tex` (l. 46) |
| El Hafidi et al. (2025) | `ElHafidi2025` | 783 | `Docs/insumos/bibitems_nuevos.tex` (l. 111) |
| Preskill (2018) (NISQ) | `Preskill2018NISQ` | 684 | `Docs/insumos/bibitems_noche.tex` (l. 32) |
| McClean et al. (2018) | `McClean2018Barren` | 788 | `Docs/insumos/bibitems_noche.tex` (l. 39) |
| Arrasmith et al. (2021) | `Arrasmith2021` | 788 | `Docs/insumos/bibitems_nuevos.tex` (l. 119) |
| Shaydulin & Wild (2022) | `Shaydulin2022Bandwidth` | 591 | `Docs/insumos/bibitems_noche.tex` (l. 60) |
| Bowles et al. (2024) | `Bowles2024Benchmarking` | 591, 670 | `Docs/insumos/bibitems_noche.tex` (l. 82) |
| Thanasilp et al. (2024) | `Thanasilp2024` | 780, 789 | `Docs/insumos/bibitems_nuevos.tex` (l. 53) |
| Huang et al. (2021) | `huang2021power` | 550, 584 | `Docs/Technical_Report.tex` (l. 3843) / `bibitems_nuevos.tex` (l. 29) |
| Schuld & Killoran (2022) | `SchuldKilloran2022Advantage` | 670 | `Docs/insumos/bibitems_noche.tex` (l. 53) |
| Bray et al. (2024) (GLOBOCAN) | `Bray2024GLOBOCAN` | 484 | `Docs/insumos/bibitems_nuevos.tex` (l. 21) |
| Guyon & Elisseeff (2003) | `Guyon2003` | 651, 707 | `Docs/insumos/bibitems_nuevos.tex` (l. 101) |
| Shen et al. (2019) (en tabla) | `Shen2019DeepLearning` | 821, 863 | `Docs/Technical_Report.tex` (l. 3737) |
| Rifat et al. (2024) (BreastMNIST) | `[VERIFICAR: falta referencia]` | 805 | Falta entrada en `.tex` (`fuentes_bib/Rifat2024.json`) |
| Bilal et al. (2025) (en tabla) | `[VERIFICAR: falta referencia]` | 895 | Falta entrada bibliográfica en `.tex` |
| Singh et al. (2025) (en tabla) | `[VERIFICAR: falta referencia]` | 905 | Falta entrada bibliográfica en `.tex` |
| Ajlouni et al. (2023) (en tabla) | `[VERIFICAR: falta referencia]` | 917 | Falta entrada bibliográfica en `.tex` |

---

## 5. Análisis crítico de la pregunta de investigación (líneas 593–601)

### Texto literal citado

El párrafo de formulación en las líneas 597–599 de `Docs/Technical_Report.tex` establece:

> «¿En qué medida las transformaciones cuánticas variacionales implementadas mediante ZZFeatureMap y PauliFeatureMap en Qiskit mejoran la separabilidad de características morfológicas extraídas de imágenes mamográficas del dataset CBIS-DDSM, y qué impacto tiene dicha mejora en la capacidad de clasificación binaria (benigno/maligno) de una red neuronal clásica entrenada con estos quantum embeddings, en comparación con una red entrenada con representaciones clásicas equivalentes?»

Y en las líneas 601–602 añade:

> «Esta pregunta de investigación reconoce tres dimensiones del problema que deben abordarse de forma integrada: la dimensión de representación (¿el espacio de Hilbert ofrece mayor separabilidad?), la dimensión de clasificación (¿esa separabilidad se traduce en mejor desempeño del clasificador?), y la dimensión de viabilidad práctica (¿las restricciones del simulador cuántico permiten una implementación reproducible sobre datos reales?). Estas tres dimensiones se corresponden directamente con los objetivos específicos 3, 5 y 6 del presente trabajo.»

### Análisis de presuposición y sesgo de resultado

1. **Presuposición sintáctica y metodológica:**  
   La subordinada *«y qué impacto tiene dicha mejora en la capacidad de clasificación binaria...»* contiene una **presuposición existencial**: da por sentado que la transformación cuántica produce una *mejora* en la separabilidad de las clases.  
   - Si la separabilidad cuántica no supera a la clásica (o si resulta inferior, como efectivamente ocurrió en los experimentos), la segunda parte de la pregunta queda sintácticamente rota o formulada sobre una premisa falsa.  
   - Respetando la decisión del autor de conservar la **forma de pregunta** (sin convertirla en hipótesis), la redacción debe formularse de manera neutral: p. ej., evaluar *«si las transformaciones... modifican la separabilidad»* y *«qué impacto tiene el cambio en la separabilidad de la representación sobre la capacidad de clasificación binaria...»*.

2. **Respuestas empíricas ya obtenidas para las tres dimensiones:**  
   El texto del reporte plantea las tres dimensiones como interrogantes abiertas. Al cierre de TT2, el proyecto cuenta con evidencia cuantitativa conclusiva para responder cada una, registradas en `Other/bitacora_decisiones.md`:

   - **Dimensión de representación (OE-3 / Módulo 6):**  
     *¿El espacio de Hilbert ofrece mayor separabilidad?*  
     **Respuesta: No.**  
     En ninguna de las familias ni condiciones cuánticas probadas (C4 con `zz_feature_map` y C5 con `pauli_feature_map(['Y','ZZ'])`, a $k=12$ y $k=8$) se observó mayor separabilidad cuántica (H-039, H-041).  
     - El exceso de KTA centrado sobre la media de permutación fue de apenas **0.003–0.007** en C4/C5, frente a **0.049** (masas) y **0.151** (calcificaciones) del kernel clásico RBF (C3).  
     - La diferencia geométrica regularizada $g$ se situó entre **1.40 y 1.70**, muy por debajo del umbral de potencial ventaja $\sqrt{N} \approx 14$.  
     - En Davies-Bouldin, razón de Fisher y KTA lineal, los baselines clásicos C1, C2 y C3 superaron consistentemente a C4 y C5.  
     - El kernel cuántico a $c=1$ sufre de concentración severa: la mediana fuera de la diagonal es de $\approx 0.003$ en C4 y $\approx 0.00003$ en C5 (H-031, H-037), comportándose formalmente como un estado ortogonal donde todas las lesiones están aisladas (*"all inputs are too far apart"*, Huang et al. 2021; Thanasilp et al. 2024).

   - **Dimensión de clasificación (OE-5 / Módulos 7 y 8):**  
     *¿Esa separabilidad se traduce en mejor desempeño del clasificador?*  
     **Respuesta: Sí hay correlación, pero en dirección desfavorable para lo cuántico.**  
     - El clasificador MLP downstream entrenado sobre los embeddings cuánticos clasificó significativamente peor que sobre las representaciones clásicas en el conjunto de prueba oficial (H-042): en masas, C1 obtuvo AUC-ROC de **0.651** frente a **0.530** (C4) y **0.581** (C5); en calcificaciones, C1 obtuvo **0.769** frente a **0.633** (C4) y **0.652** (C5), con diferencias estadísticamente significativas ($p < 0.05$ en todas salvo C5 masas que queda en el límite, $p \approx 0.044$).  
     - La correlación de Spearman $\rho_s$ entre el ranking de separabilidad y el ranking de clasificación osciló entre **0.67 y 0.97** en todas las métricas (H-049): la calidad de la representación sí predice el desempeño del clasificador, pero dado que la separabilidad cuántica fue inferior, la clasificación downstream también lo fue. No hubo mejora que trasladar.

   - **Dimensión de viabilidad práctica (OE-6 / Módulo 8):**  
     *¿Las restricciones del simulador cuántico permiten una implementación reproducible sobre datos reales?*  
     **Respuesta: Sí en simulación exacta de vectores de estado, pero inviable bajo muestreo finito o entrenamiento de ansatz en hardware NISQ.**  
     - En el entorno de simulación (Apple Silicon M3, 16 GiB), el cálculo de embeddings por vector de estado exacto es viable hasta $k \approx 25$ qubits en 24 h, y el kernel compute-uncompute hasta $k \approx 22$ (H-051).  
     - Sin embargo, entrenar $\theta$ por *parameter-shift* supera las 24 h a partir de $k \ge 15$, lo que obligó a adoptar la Arquitectura B con $\theta$ fijo (D-014).  
     - Con muestreo finito (1,024 shots, RNF-05), el ruido por shot en $\langle Z_i \rangle$ representa entre el 55 % y 65 % de la dispersión de la señal en C4 (H-052). Más grave aún: debido a la concentración del kernel a $c=1$, entre el **16 % y el 74 %** de las entradas de la matriz de fidelidad leen exactamente 0 con 1,024 shots (H-052). Por ende, el cálculo de kernels cuánticos directos es inmedible en hardware cuántico NISQ sin mitigación de concentración o escalado angular agresivo ($c \le 0.02$).

---

## 6. Lo que no se pudo comprobar

En estricto apego a la regla 4 de `Docs/insumos/noche/reglas.md` («No inventes nada. Un `[VERIFICAR]` honesto vale más que un dato plausible»), se listan los elementos factuales que no pudieron ser contrastados contra un texto fuente íntegro en el repositorio:

1. **Artículos sin archivo de texto disponible en `Docs/fuentes/txt/`:**
   - `Anez2025AIPipeline` (l. 718): No se dispone del texto completo para verificar las cifras de AUC de ResNet-50 (0.95), XGBoost (0.90) y SVM (0.84).
   - `Mashekova2025AIBreastCancer` (l. 711): Cifra del 44 % de estudios con SVM sin archivo crudo de verificación.
   - `Avci2023MammographyEnhancement` (l. 713): Sin texto fuente en `Docs/fuentes/txt/`.
   - `Abdelhafiz2019DeepCNN` (l. 730): Sin texto fuente para contrastar la cronología de CNNs médicas.
   - `Shia2025MicrocalcClassification` (l. 736): Sin texto fuente para verificar los valores numéricos de F1 de EfficientNet-B3.
   - `Kim2025GlobalBreastCancer` (l. 533): Sin texto fuente en el repositorio.
2. **Cifras de fuentes secundarias y de pago:**
   - **Rifat et al. (2024)** (l. 805): El artículo primario (*ICCIT 2024*) está tras muro de pago de IEEE Xplore. Aunque la cifra de 69 % de accuracy en BreastMNIST fue confirmada a través de la revisión secundaria de Yurtseven (2025, arXiv:2512.02066), el valor de comparación «frente a 67 %» y la afirmación de que los autores reconocen las limitaciones del hardware **no pudieron ser verificados** en el texto primario.
   - **`GLOBOCAN2022` (Freihat et al. 2025)** frente a **Bray et al. (2024)** (l. 484): Se descargaron metadatos vía Crossref, pero no se abrió el PDF completo de Freihat et al. para contrastar si las cifras 2.3 millones y 670,000 provienen de su introducción o de sus modelos a 2050.
3. **Páginas web y notas de prensa no cacheadas:**
   - `StopBreastCancer2025`, `BCRF2025`, `CancerMexico2025`, `NBCF2026_EarlyDetection`, `Windsong2026_EarlyDetection`, `GlobalCancerStatistics2024`: Las URLs no cuentan con volcados en texto plano en `Docs/fuentes/txt/`, por lo que sus porcentajes (99 %, 30 %, 26 %, 42 %) se toman con reserva.
4. **Referencias huérfanas en la tabla comparativa (`tab:estado_arte`):**
   - `Bilal et al. (2025)` (l. 895), `Singh et al. (2025)` (l. 905) y `Ajlouni et al. (2023)` (l. 917) aparecen en las filas de la tabla pero **no tienen entrada `\bibitem`** en `Technical_Report.tex` ni archivos de metadatos asociados. Sus datos en la tabla no han sido contrastados.
5. **Origen de la digresión del ENIAC (l. 676–680):**
   - No se localizó ninguna fuente bibliográfica o documental en el repositorio que contenga la narración de la máquina ENIAC de 1945 ni el entrecomillado «cerebro gigante». Se asume redacción retórica no referenciada.

---

## Correcciones del coordinador (2026-10-14, madrugada)

- **La paráfrasis de la línea 591 no es de Shaydulin & Wild, sino de Álvarez-Estévez (2024)**, `\bibitem{AlvarezEstevez2024QuantumKernelBench}` (arXiv:2408.10274), que hoy está en la bibliografía sin ningún `\cite`. Comprobado contra el resumen de arXiv (`Docs/fuentes/meta/AlvarezEstevez2024.xml`, obtenido de la API de arXiv; no hay PDF):
  - l. 591: «se obtienen resultados mixtos para el caso general entre benchmarks clásicos; los experimentos cuestionan el valor añadido general de aplicar optimización cuántica de kernels … una elección cuidadosa del feature map cuántico en conexión con una hiperparametrización apropiada puede resultar más efectiva» ↔ «Despite outperforming classical methods in ad-hoc datasets, mixed results are obtained for the general case among standard classical benchmarks. Our experiments call into question a general added value of applying QKT optimization, for which the additional computational cost does not necessarily translate into improved classification performance. Instead, it is suggested that a careful choice of the quantum feature map in connection with proper hyperparameterization may prove more effective.»
  - **Segunda paráfrasis de la misma fuente, no detectada por la auditoría**, en §1.2 («La brecha en QML…», l. 587): «La aplicación práctica de estos métodos sigue siendo una pregunta abierta, particularmente más allá de problemas de prueba específicamente construidos y dadas las limitaciones actuales del hardware cuántico» ↔ «the practical applicability of these methods remains an open question, particularly beyond the context of specifically-crafted toy problems, and given the current limitations of quantum hardware.»
  - Nota: la «QKT optimization» del original es el *entrenamiento* del kernel cuántico (Quantum Kernel Training), no una «optimización cuántica de kernels» genérica; al citarlo conviene traducirlo con precisión.
  - La cita a Shaydulin & Wild propuesta por la auditoría para la l. 591 queda **descartada**: su frase (p. 8) habla de ajustar hiperparámetros para modificar el sesgo inductivo, no de los resultados mixtos de un *benchmark*.
