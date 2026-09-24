# Bitácora de decisiones · TT 2026-B039

> Registro vivo del desarrollo. Cada entrada dice **por qué** se hizo algo, no solo qué.
> En noviembre esto alimenta las secciones 6–8 del reporte técnico, y es lo que se defiende ante el jurado.

**Cómo usar esto.** Tres tipos de entrada, porque no son lo mismo:

| Tipo | Es | Lo que no puede faltar |
|---|---|---|
| **D** · Decisión | Elegiste entre opciones | Las alternativas y el porqué |
| **H** · Hallazgo | Descubriste algo que no sabías | La evidencia numérica y la consecuencia |
| **Q** · Pregunta abierta | Aún no está resuelto | La fecha límite para resolverla |

Numeración correlativa, nunca se reutiliza. Si una decisión se revierte, **no se borra**: se marca `Revertida` y se enlaza la que la reemplaza — el jurado valora más un cambio de rumbo justificado que un historial impecable. Las plantillas están al final.

---

## Índice

### Decisiones

| # | Fecha | Decisión | Módulo | Estado | → Reporte |
|---|---|---|---|---|---|
| D-001 | 2026-05 | SelectKBest + MinMaxScaler en lugar de PCA antes del circuito | M4 | Firme | §4.6, §7.2 |
| D-002 | 2026-05 | ZZFeatureMap y PauliFeatureMap como condiciones separadas | M5 | **Revertida** (ver H-012, Q-008) | §4.7, §7.2 |
| D-003 | 2026-05 | Geometric difference como métrica de ventaja cuántica potencial | M7 | Firme | §3.4.2, §7.2 |
| D-004 | 2026-05 | Escalado angular a [0,π] y no a [0,2π] | M4 | Firme | §4.6 |
| D-005 | 2026-05 | Masas y calcificaciones como subproblemas independientes | todos | Firme | §4.4 |
| D-006 | 2026-05 | PyRadiomics (Estrategia A) en lugar de encoder CNN | M3 | Firme | §4.5 |
| D-007 | 2026-08-25 | Entorno `radiomics` separado, compilado desde GitHub | infra | Firme | §8.x |
| D-008 | 2026-08-25 | `binCount=32` en lugar de `binWidth` | M3 | Firme | §8.x |
| D-009 | 2026-08-25 | Sin resize a 224×224 en la ruta radiómica | M2 | Firme | §4.4, §8.x |
| D-010 | 2026-08-25 | CLAHE fuera de la ruta radiómica | M2 | Firme (2026-09-22) | §4.4 |
| D-011 | 2026-08-25 | Unidad de análisis = lesión/ROI, no paciente | M4 | Firme (2026-09-22) | §4.6 |
| D-012 | 2026-09-21 | Descargar por la API REST de TCIA, no con NBIA Data Retriever | M1 | Firme | §8.x |
| D-013 | 2026-09-22 | Punto de operación: k=12 qubits, reps=1 | M4, M5 | Firme | §4.6, §4.7 |
| D-014 | 2026-09-22 | Arquitectura B: embedding precomputado con θ fijo (semilla 42) | M5, M6 | Firme | §4.7, §4.8 |
| D-015 | 2026-09-22 | C5 usa `pauli_feature_map(paulis=['X','ZZ'])` | M5 | Firme | §4.7 |
| D-016 | 2026-09-22 | C2 se declara control nulo; se mantienen cinco condiciones | M5, M7 | Firme | §4.7, §6.x |
| D-017 | 2026-09-22 | La *geometric difference* se calcula con `FidelityQuantumKernel` | M7 | Firme | §3.4.2, §4.9 |
| D-018 | 2026-09-22 | Validación cruzada 5-fold estratificada sobre el conjunto de entrenamiento | M6 | Firme | §4.8, §4.9 |
| D-019 | 2026-09-23 | Las líneas de trabajo futuro se atribuyen a Azevedo et al. (2022) | reporte | Firme | §1.3, §2.1.5 |

### Hallazgos

| # | Fecha | Hallazgo | Impacto |
|---|---|---|---|
| H-001 | 2026-08-24 | 86 mamografías faltantes; cobertura real 97.6 %, no 100 % | Corrige una cifra del reporte de TT1 |
| H-002 | 2026-08-24 | `PixelSpacing` y `Manufacturer` ausentes en el 100 % de los DICOM | Limitación metodológica, insumo del OE-6 |
| H-003 | 2026-08-25 | Los 5 features más discriminativos en masas son todos `shape2D` | Justifica D-009 con datos |
| H-004 | 2026-08-25 | 80 casos (2.3 %) con máscara de dimensiones distintas a la imagen | Requisito nuevo de M2 |
| H-005 | 2026-08-24 | 0 fuga de pacientes intra-subproblema; 31 cruzan si se juntan | Defiende D-005 ante el jurado |
| H-006 | 2026-08-25 | El sdist de PyRadiomics en PyPI es incompilable | Justifica D-007 |
| H-007 | 2026-08-25 | `binWidth` sobre 16 bits: 38 h contra 8 min | Justifica D-008 |
| H-008 | 2026-08-24 | 2.28 ROIs por paciente; 56 pacientes con ambas etiquetas | Obliga a declarar la unidad de análisis |
| H-009 | 2026-08-24 | Defectos verificables en el PDF de TT1 | Lista de correcciones para la Fase 7 |
| H-010 | 2026-09-21 | El manifiesto NBIA original nunca se guardó y la vía oficial de descarga falla | Justifica D-012; reproducibilidad del dataset |
| H-011 | 2026-09-21 | El entrenamiento conjunto VQC↔MLP no escala más allá de k=8 | Obliga a decidir Q-007; RNF-07 es inalcanzable tal como está |
| H-012 | 2026-09-22 | C4 y C5 son el mismo circuito: fidelidad 1.000000000000 | Invalida D-002; bloquea M5 hasta resolver Q-008 |
| H-013 | 2026-09-22 | Sin ansatz, ⟨Zᵢ⟩ = 0 para toda entrada | θ debe quedar fijo con semilla, no ausente; separa kernel de ⟨Z⟩ |
| H-014 | 2026-09-22 | La precisión de shots se ignora si se fija en el estimador | Invalidó la primera corrida de shots; riesgo de reproducibilidad |
| H-015 | 2026-09-22 | SPSA es ~10× más rápido que parameter-shift; lin-comb es 5× más lento | Ningún gradiente rescata la Arquitectura A |
| H-016 | 2026-09-23 | AerSimulator tiene un sesgo sistemático de ~0.013 frente a statevector | Invalidaba la figura del OE-6; obliga a medir el ruido de otra forma |
| H-017 | 2026-09-23 | Un solo sorteo de θ no permite concluir nada sobre concentración del embedding | Obliga a promediar; advertencia metodológica general |
| H-018 | 2026-09-23 | El embedding se concentra con el número de qubits, no con la profundidad | Respalda reps=1 por dispersión, no solo por coste; material del OE-6 |

### Preguntas abiertas

| # | Pregunta | Bloquea | Límite |
|---|---|---|---|
| Q-001 | ¿C2 se declara control nulo o se añade C2′? | Fase 4 | **RESUELTA** → D-016 |
| Q-002 | ¿Con qué θ se mide la separabilidad? | Fase 4 | **RESUELTA** → D-014 |
| Q-003 | ¿Sobre qué kernel se calcula la *geometric difference*? | Fase 3 | **RESUELTA** → D-017 |
| Q-004 | ¿Azevedo et al. (2022) o Incudini et al. (2022)? | Fase 7 | **RESUELTA** → D-019 |
| Q-005 | ¿Validación cruzada o justificación de su ausencia? | Fase 6 | **RESUELTA** → D-018 |
| Q-006 | ¿Qué k y reps finales? | Fase 3 | **RESUELTA** → D-013 |
| Q-007 | ¿Entrenamiento conjunto o embedding precomputado? | Fases 4 y 5 | **RESUELTA** → D-014 |
| Q-008 | ¿Qué conjunto de Pauli usa C5? | M5, Fase 4 | **RESUELTA** → D-015 |

---

## Decisiones

### D-007 · Entorno `radiomics` separado, compilado desde GitHub
**Fecha:** 2026-08-25 · **Módulo:** infraestructura · **Estado:** Firme · **→ Reporte:** §8.x

**Contexto.** PyRadiomics no estaba instalado y M2/M3 no podían empezar. Los tres caminos habituales fallaron (ver H-006).

**Alternativas.**
- *conda-forge* — descartada: no existe feedstock de PyRadiomics.
- *`pip install pyradiomics`* — descartada: el sdist de PyPI no compila.
- *Instalar en `qml_cancer`* — descartada: mezcla el stack cuántico con uno que exigía restricciones distintas de numpy, y un fallo contaminaría el entorno que ya funciona.
- *Compilar desde el repo de GitHub en un entorno aparte* — **elegida**.

**Decisión.** Entorno conda `radiomics` (Python 3.10) con PyRadiomics compilado desde el commit `8ed5793` (2025-06-16) del repo AIM-Harvard/pyradiomics. M2 y M3 viven ahí y escriben `.parquet`; `qml_cancer` lee ese parquet y se encarga de M4–M7.

**Por qué.** Desacopla el riesgo: si PyRadiomics se rompe, el stack cuántico sigue intacto. Master ya migró a `scikit-build-core` y declara soporte para `numpy>=2.0`, así que el entorno quedó en numpy 2.2.6 — la misma versión de `qml_cancer` y la configuración que upstream realmente prueba.

**Evidencia.** Extracción validada sobre casos reales del CBIS-DDSM: 67 features (firstorder 18, shape2D 9, GLCM 24, GLRLM 16), 0 NaN, escritura a parquet correcta.

**Consecuencias.** Hay que cambiar de kernel entre M3 y M4. La versión reporta `0.1.dev1+g8ed579383` porque el clon es *shallow* y `setuptools_scm` no ve los tags: **lo que ancla la reproducibilidad es el commit, no ese número**, y debe quedar escrito en el reporte.

---

### D-008 · `binCount=32` en lugar de `binWidth`
**Fecha:** 2026-08-25 · **Módulo:** M3 · **Estado:** Firme · **→ Reporte:** §8.x

**Contexto.** La primera extracción tardaba 30–53 s por caso, lo que daba ~38 h para los 3,482 casos.

**Alternativas.** `binWidth` fijo (habitual en TC, donde las unidades Hounsfield están calibradas) contra `binCount` fijo (número fijo de niveles).

**Decisión.** `binCount=32`.

**Por qué.** No es solo velocidad. El CBIS-DDSM tiene intensidades **arbitrarias y no calibradas**: película digitalizada, sin `PixelSpacing`, convertida por MATLAB a Secondary Capture (ver H-002). IBSI recomienda número fijo de bins precisamente para modalidades de intensidad arbitraria. `binWidth` supone unidades con significado físico que aquí no existen.

**Evidencia.** Ver H-007. Con `binWidth=25` sobre datos de 16 bits salen 1,139 niveles de gris y una GLCM de 1139×1139.

**Consecuencias.** Los valores de GLCM/GLRLM no son comparables con literatura que use `binWidth`. Hay que declarar el parámetro explícitamente en el reporte.

---

### D-009 · Sin resize a 224×224 en la ruta radiómica
**Fecha:** 2026-08-25 · **Módulo:** M2 · **Estado:** Firme · **→ Reporte:** §4.4, §8.x

**Contexto.** El reporte de TT1 dice que M2 entrega 224×224 y que M3 opera sobre esa imagen. Eso es herencia de la Estrategia B (encoder CNN), que fue descartada en D-006.

**Decisión.** PyRadiomics opera sobre el recorte ROI a **resolución original**, con la máscara alineada. El 224×224 solo aplicaría si algún día se retoma la Estrategia B.

**Por qué.** Redimensionar iguala artificialmente el tamaño de las lesiones. Los *bounding boxes* reales van de 41×65 px a 1137×1641 px: una microcalcificación y una masa grande acabarían del mismo tamaño.

**Evidencia.** H-003 — los 5 features más discriminativos en masas son todos de tamaño, con |d| de Cohen ≈ 1.41–1.43. El resize destruye justo la señal más fuerte disponible.

**Consecuencias.** Contradice el texto de TT1; hay que corregirlo en §4.4 y explicar el cambio en §8.x. El coste computacional no sube de forma apreciable (0.14 s/caso).

---

### D-010 · CLAHE fuera de la ruta radiómica
**Fecha:** 2026-08-25 · **Módulo:** M2 · **Estado:** Provisional · **→ Reporte:** §4.4

**Contexto.** El diseño de TT1 aplica CLAHE antes de extraer características.

**Decisión provisional.** Extraer las features del recorte crudo. Generar además la variante con CLAHE y **reportar el efecto de ambas**.

**Por qué.** CLAHE es correcto para entrada a CNN o para visualización, pero es una ecualización local dependiente del contenido: rompe la reproducibilidad de *first-order* y GLCM bajo IBSI.

**Por qué sigue provisional.** Correr ambas variantes cuesta poco y convierte una objeción potencial en media sección de resultados. Se cierra cuando existan los dos conjuntos de features.

---

### D-011 · Unidad de análisis = lesión/ROI
**Fecha:** 2026-08-25 · **Módulo:** M4 · **Estado:** Provisional · **→ Reporte:** §4.6

**Contexto.** El reporte de TT1 nunca declara si la unidad de análisis es la lesión o el paciente.

**Decisión provisional.** La unidad es la **lesión (ROI)**. Las métricas se reportan por lesión, no por paciente.

**Por qué.** Es lo que corresponde al problema planteado (clasificar hallazgos) y lo que hace comparable el trabajo con la literatura sobre CBIS-DDSM. La alternativa por paciente exigiría una regla de agregación que el diseño actual no define.

**Evidencia.** H-008 — hay 2.28 ROIs por paciente (máx. 24) y 56 pacientes con lesiones benignas y malignas a la vez, así que la etiqueta a nivel paciente sería ambigua.

**Consecuencias.** Hay que declararlo explícitamente; es una pregunta previsible del jurado.

---

### D-013 · Punto de operación: k=12 qubits, reps=1
**Fecha:** 2026-09-22 · **Módulo:** M4, M5 · **Estado:** Firme · **→ Reporte:** §4.6, §4.7 · *cierra Q-006*

**Contexto.** RNF-07 declara k ∈ [8,16] y reps ∈ [1,6]. El benchmark midió qué parte de ese rango es alcanzable.

**Decisión.** k = 12 qubits, reps = 1.

**Por qué k=12.** El coste total de la etapa cuántica bajo Arquitectura B es 0.29 h a k=8, **2.95 h a k=12** y 41.25 h a k=16. No crece linealmente: de 8 a 12 se multiplica por 10, de 12 a 16 por 14. k=12 es el último escalón pagable.

Hay además un argumento de contenido. H-003 mostró que los features más discriminativos en masas son todos `shape2D`, y PyRadiomics entrega nueve de esa familia. Con k=8, `SelectKBest` elegiría ocho medidas de forma fuertemente correlacionadas entre sí, y los productos $x_i x_j$ que codifica el *feature map* serían en buena parte redundantes. Con k=12 entran también features de textura, y las interacciones forma×textura sí tienen contenido.

**Por qué reps=1.** Bajo D-014 θ no se entrena, de modo que capas adicionales no aportan capacidad aprendible: solo una rotación fija más complicada. reps=1 es el mínimo que hace el embedding no trivial, y dado H-013 «no trivial» es exactamente el requisito.

**Evidencia.** `Code/results/5_benchmark_resultados.csv`, `5_benchmark_arquitectura.csv`, `5_benchmark_kernel_proyeccion.csv`.

**Consecuencias.** M4 fija k=12 en `SelectKBest`. **Verificar en M4 qué familias de features sobreviven a la selección y reportarlo**: si salen doce variables de tamaño casi idénticas, el argumento de contenido se debilita y habría que forzar diversidad de familias.

---

### D-014 · Arquitectura B: embedding precomputado con θ fijo
**Fecha:** 2026-09-22 · **Módulo:** M5, M6 · **Estado:** Firme · **→ Reporte:** §4.7, §4.8 · *cierra Q-007 y Q-002*

**Contexto.** §4.8 especifica integrar el VQC con el MLP vía `TorchConnector` y optimizar θ junto con los pesos.

**Alternativas.**
- *Arquitectura A, entrenamiento conjunto* — descartada.
- *Arquitectura B, θ fijo y embeddings precomputados* — **elegida**.

**Decisión.** θ se fija con **semilla 42** y no se entrena. Los embeddings ⟨Zᵢ⟩ se calculan una sola vez para todo el dataset, se guardan en disco, y el MLP se entrena sobre esa matriz como sobre cualquier conjunto tabular. `TorchConnector` deja de usarse.

**Por qué.** Tres razones independientes, y esto importa porque ninguna depende de las otras:

1. **Coste.** H-011: 48 h a k=8, 382 h a k=12 y 5,304 h a k=16 bajo A, contra 2 min, 12 min y 148 min bajo B. Entre 1,472× y 2,155× más barato. H-015 confirma que ningún método de gradiente alternativo cambia el veredicto.
2. **Validez interna.** C2 y C3 son no supervisados. Si C4 y C5 ajustan θ contra las etiquetas, cualquier ventaja podría venir del ajuste supervisado y no de la codificación cuántica. Bajo B las cinco condiciones son transformaciones que no miran las etiquetas. **Esto cierra Q-002 por construcción.**
3. **Correspondencia con la pregunta de investigación.** §1.2 pregunta si el mapeo φ produce mayor separabilidad intrínseca. Eso es sobre la *codificación*, no sobre un procedimiento de optimización. B aísla φ; A lo mezclaba.

**Evidencia.** `Code/results/5_benchmark_arquitectura.csv`; H-011 y H-015.

**Consecuencias.** Hay que reescribir §4.8 y §4.9. θ pasa a ser un **parámetro reportable del experimento**, no un detalle: por H-013 determina qué proyección de la información de fase resulta visible. Como beneficio colateral, entrenar toma segundos, lo que vuelve viable D-018.

---

### D-015 · C5 usa `pauli_feature_map(paulis=['X','ZZ'])`
**Fecha:** 2026-09-22 · **Módulo:** M5 · **Estado:** Firme · **→ Reporte:** §4.7 · *cierra Q-008; reemplaza D-002*

**Contexto.** H-012 demostró que C4 y C5, tal como las definía §4.7, son el mismo circuito: fidelidad 1.000000000000.

**Alternativas**, promediadas sobre 200 entradas aleatorias:

| Conjunto | Fidelidad media vs ZZ | Máximo |
|---|---|---|
| `['Z','Y','ZZ']` | 0.332 | 0.962 |
| `['Y','ZZ']` | 0.315 | 0.992 |
| `['Z','YY']` | 0.109 | 0.706 |
| **`['X','ZZ']`** | **0.071** | 0.727 |

**Decisión.** C5 = `pauli_feature_map(paulis=['X','ZZ'])`.

**Por qué.** Es el más alejado de ZZ en todo el rango de entrada. `['Z','Y','ZZ']` queda descartado pese a la primera impresión: promedia 0.332 con máximo 0.962, es decir, sobre buena parte del espacio de entrada codifica casi lo mismo que ZZ y no constituiría una condición independiente. Todos los candidatos mantienen 12 CX, así que la elección no tiene coste computacional.

**Qué afirma la comparación.** `['X','ZZ']` sustituye la codificación de primer orden en Z por una en X, manteniendo el término de entrelazamiento ZZ. C4 contra C5 mide por tanto el efecto del **eje de codificación de primer orden**, con el acoplamiento de segundo orden fijo. Eso es lo que hay que escribir en §4.7; no vale decir genéricamente «el efecto del diseño del feature map».

**Consecuencias.** D-002 queda revertida. Hay que actualizar §4.7 y la tabla de condiciones experimentales.

---

### D-016 · C2 se declara control nulo; cinco condiciones
**Fecha:** 2026-09-22 · **Módulo:** M5, M7 · **Estado:** Firme · **→ Reporte:** §4.7, §6.x · *cierra Q-001*

**Contexto.** M4 entrega x ∈ [0,π]^k, y C2 aplica PCA de k → k. Eso no es una reducción sino una **rotación ortogonal**: preserva las distancias euclidianas, de modo que Davies-Bouldin, Fisher y KTA son invariantes, y el MLP absorbe la rotación en su primera capa. C2 dará los mismos números que C1 por álgebra, no por casualidad.

**Alternativas.** Añadir C2′ con PCA desde el vector radiómico completo (n ≈ 100–300 → k); reemplazar C2 por C2′; o declarar C2 control nulo.

**Decisión.** C2 se mantiene y se declara **control nulo**. Se conservan cinco condiciones. No se añade C2′.

**Por qué.** El principio de diseño «todas las condiciones parten del mismo vector» es precisamente lo que causa la degeneración: si la entrada ya está en k dimensiones, no queda reducción que hacer. No se pueden tener ambas cosas. C2′ rompería la simetría al partir de un vector de dimensión distinta, y una condición que no se pueda defender ante esa pregunta es peor que no tenerla.

El comparador clásico real es **C3**: Kernel PCA con RBF de k → k es genuinamente no lineal, no una rotación. Y es el comparador conceptualmente correcto, porque el marco de Schuld contrapone kernels cuánticos contra kernels clásicos, siendo el RBF el kernel clásico de referencia.

C2 además aporta algo: si las métricas de separabilidad dieran valores distintos para C1 y C2, estarían mal implementadas. Es un **control positivo del instrumento de medición**.

**Consecuencias.** §6 debe explicar por qué C1 y C2 coinciden, presentándolo como validación de las métricas y no como un resultado nulo. C2′ queda anotado como análisis de robustez opcional si hay holgura tras el congelamiento del 23 de octubre.

---

### D-017 · La *geometric difference* se calcula con `FidelityQuantumKernel`
**Fecha:** 2026-09-22 · **Módulo:** M7 · **Estado:** Firme · **→ Reporte:** §3.4.2, §4.9 · *cierra Q-003*

**Contexto.** $g(K_C, K_Q)$ de Huang et al. está definida **entre dos kernels**. M5 produce ⟨Zᵢ⟩ ∈ [-1,1]^k, que es un vector: construir un RBF sobre él no da $K_Q$ y el marco de Huang no aplica.

**Decisión.** El kernel cuántico $K_Q(x,x') = |\langle\phi(x)|\phi(x')\rangle|^2$ se calcula aparte con `FidelityQuantumKernel`, usando **solo el feature map**, sin ansatz, sobre submuestras de 150–200 casos por subconjunto (RNF-06).

**Por qué.** Es la única lectura técnicamente correcta. Y usar solo el feature map es coherente con D-014: el kernel es una propiedad de la codificación.

**Nota que debe ir al reporte (de H-013).** El kernel de fidelidad compara estados completos, fases incluidas; los ⟨Zᵢ⟩ no ven fases. Las métricas basadas en kernel (KTA, *geometric difference*) y las basadas en ⟨Zᵢ⟩ (Davies-Bouldin, Fisher, y el MLP) miden por tanto **objetos distintos y pueden discrepar**. Si KTA sale alto y la clasificación mediocre, esa es la explicación y conviene anticiparla.

**Coste.** A k=12, unos 41 min por matriz y 2.75 h las cuatro (dos feature maps × dos subconjuntos). Fuente: `Code/results/5_benchmark_kernel_proyeccion.csv`.

---

### D-018 · Validación cruzada 5-fold estratificada
**Fecha:** 2026-09-22 · **Módulo:** M6 · **Estado:** Firme · **→ Reporte:** §4.8, §4.9 · *cierra Q-005*

**Contexto.** La validación cruzada figura en el cronograma del reporte y en el acta de los directores, pero no existía en la metodología (§4.9). Bajo Arquitectura A no era costeable.

**Decisión.** Validación cruzada **5-fold estratificada por clase** sobre el conjunto de entrenamiento. El conjunto de prueba oficial del CBIS-DDSM **no se toca**: sigue siendo la evaluación final, sin reordenar (RNF-03).

**Por qué.** D-014 vuelve el entrenamiento un problema clásico de segundos sobre una matriz en caché, así que el único coste real es escribir el código. Cumple un compromiso explícito ante el jurado y aporta barras de error en las métricas, que hoy se reportarían como valores puntuales.

**Consecuencias.** Estratificar por clase, no por paciente: la unidad de análisis es la lesión (D-011). **Verificar que ningún paciente quede repartido entre folds**, ya que hay 2.28 ROIs por paciente (H-008); si se detecta, pasar a `StratifiedGroupKFold` agrupando por `patient_id`. Hay que añadir la validación cruzada a §4.9, que hoy no la menciona.

---

### D-019 · Las líneas de trabajo futuro se atribuyen a Azevedo et al. (2022)
**Fecha:** 2026-09-23 · **Módulo:** reporte · **Estado:** Firme · **→ Reporte:** §1.3, §2.1.5 · *cierra Q-004*

**Contexto.** El reporte atribuye a Azevedo et al. (2022) las dos líneas de trabajo futuro sobre las que se construye el proyecto (§1.3 y §2.1.5). El contexto del proyecto decía Incudini et al. (2022), que es otro paper.

**Alternativas.** Azevedo et al. (2022), que es lo que dice el reporte, o Incudini et al. (2022), que era lo que decía el contexto del proyecto.

**Decisión.** La atribución correcta es **Azevedo et al. (2022)**. El texto de §1.3 y §2.1.5 se mantiene.

**Por qué.** Lo resolvió el autor. El reporte ya era internamente consistente con esta atribución, de modo que no hay que cambiar el texto.

**Consecuencias.** La mención a Incudini et al. se retira del contexto del proyecto. Sigue pendiente un defecto de H-009: `Azevedo2022QuantumTransfer` se discute por nombre sin `\cite`, así que al corregir el reporte hay que añadir la cita en ambos puntos.

---

### D-012 · Descargar por la API REST de TCIA, no con NBIA Data Retriever
**Fecha:** 2026-09-21 · **Módulo:** M1 · **Estado:** Firme · **→ Reporte:** §8.x

**Contexto.** Faltaban 84 series del dataset (H-001) y la vía oficial de descarga no funcionaba (H-010).

**Alternativas.**
- *Relanzar el manifiesto original* — imposible: nunca se guardó.
- *Reconstruir un manifiesto `.tcia`* — se hizo, con los `Series UID` de `metadata.csv`, pero el Data Retriever lo rechaza con *"incorrect response from the server"*.
- *Re-descargar el dataset completo* — descartada: son 148 GB y solo había 30 GB libres.
- *Descargar por la API REST de TCIA* — **elegida**.

**Decisión.** Un script pide cada serie a `nbia-api/services/v1/getImage?SeriesInstanceUID=…`, que devuelve un ZIP, extrae el `.dcm` y lo coloca en la carpeta que el índice del proyecto ya espera.

**Por qué.** Descarga solo lo que falta (4.77 GB en vez de 148 GB), permite reintentos por serie y controla el nombre final del archivo, que es crítico: el ZIP entrega `00000001.dcm` mientras las rutas del índice esperan `1-1.dcm`. Con el nombre del ZIP, la descarga habría sido inútil.

**Evidencia.** 84/84 series en 21.4 min, 0 fallidas. Cobertura verificada: **3,568 / 3,568 = 100.0 %**. Los DICOM nuevos leen con `pydicom` como MG de 16 bits en MONOCHROME2, consistentes con el resto.

**Consecuencias.** El endpoint `v2/getImage` devuelve HTTP 500 y no sirve. El procedimiento queda como la forma reproducible de obtener el dataset y debe documentarse en §8.x, ya que el reporte no describe hoy cómo se obtuvieron los datos.

---

> Las decisiones **D-001 a D-006** se tomaron durante TT1 y ya están documentadas en el reporte (§7.2 · *Decisiones metodológicas aprendidas*). Se listan en el índice para tener la traza completa; si alguna se revisa en TT2, se le abre entrada propia aquí.
>
> **D-002 quedó revertida el 2026-09-22.** Su premisa era falsa: ZZFeatureMap y PauliFeatureMap con `['Z','ZZ']` son el mismo circuito (H-012), de modo que no podían ser condiciones separadas. La decisión que la reemplaza saldrá de Q-008.

---

## Hallazgos

### H-001 · Cobertura real del dataset: 97.6 %, no 100 %
**Fecha:** 2026-08-24 · **→ Reporte:** §5.1

El reporte de TT1 afirma cobertura DICOM del 100 % (3,568/3,568), y la columna `dicom_found` vale `True` en las 3,568 filas. La verificación contra disco lo desmiente:

```
path_full_mammo : 3568 no-nulos -> 3482 existen,  86 ROTAS
path_roi_mask   : 3568 no-nulos -> 3568 existen,   0 rotas
path_cropped    :  115 NULOS    -> 3453 existen
Usables (completa + máscara): 3482 / 3568 = 97.6 %
```

Las 86 rutas rotas apuntan a **carpetas que existen pero están vacías**: descarga incompleta del NBIA Data Retriever, no un error del índice. Se corrige re-ejecutando el manifiesto.

**Impacto.** Hay que corregir la cifra en §5.1 y re-validar antes de M2.

**Resuelto el 2026-09-21.** Las 84 series se re-descargaron por la API de TCIA (ver D-012): 84/84 en 21.4 min, 0 fallidas. **Cobertura actual: 3,568 / 3,568 = 100.0 %**, verificada leyendo los DICOM nuevos con `pydicom` (MG, 16 bits, MONOCHROME2). La cifra del reporte de TT1 era falsa cuando se escribió, pero hoy sí es correcta.

---

### H-002 · Sin `PixelSpacing` ni `Manufacturer` en todo el dataset
**Fecha:** 2026-08-24 · **→ Reporte:** §5.4, OE-6

Sobre muestra de 25 mamografías: `PixelSpacing` e `ImagerPixelSpacing` **ausentes en el 100 %**, `Manufacturer` también. Son conversiones de MATLAB a Secondary Capture; `Modality` = MG, `BitsStored` = 16, `PhotometricInterpretation` = MONOCHROME2 en todos.

**Impacto.** PyRadiomics asume espaciado (1,1), así que las *shape features* salen en píxeles sin escala física. Como el DDSM original se digitalizó con escáneres de distinta resolución (µm/píxel distintos) y `Manufacturer` es UNKNOWN, **no hay forma de corregirlo**: el mismo tumor en mm da distinto número de píxeles según el digitalizador. Es una limitación real que conviene declarar como aportación del OE-6, no esconder. El reporte ya documenta el `Manufacturer` UNKNOWN en §5.4.2 pero no saca esta consecuencia.

---

### H-003 · La discriminación en masas está dominada por el tamaño
**Fecha:** 2026-08-25 · **→ Reporte:** §6.x

Sobre 20 masas, tamaño de efecto (|d| de Cohen) benigno contra maligno:

```
original_shape2D_MaximumDiameter    1.427
original_shape2D_MinorAxisLength    1.418
original_shape2D_MajorAxisLength    1.413
original_shape2D_MeshSurface        1.412
original_shape2D_PixelSurface       1.412
```

Los cinco primeros son medidas de tamaño, con efectos muy fuertes.

**Impacto.** Confirma D-009 con datos. Advertencia para M4: `SelectKBest` va a elegir casi puro `shape2D`, lo que puede dejar al circuito cuántico sin información textural. Vale la pena reportar qué familias sobreviven a la selección.

---

### H-004 · 80 casos con máscara desalineada
**Fecha:** 2026-08-25 · **→ Reporte:** §8.x

Auditoría de dimensiones sobre los 3,482 casos usables:

```
mass            78 / 1650  (4.7 %)
calcification    2 / 1832  (0.1 %)
TOTAL           80 / 3482  (2.3 %)
```

**Impacto.** PyRadiomics exige geometría idéntica entre imagen y máscara. M2 tiene que resamplear la máscara al espacio de la imagen con vecino más cercano; descartarlos perdería 78 masas.

---

### H-005 · Sin fuga de pacientes dentro de cada subproblema
**Fecha:** 2026-08-24 · **→ Reporte:** §4.6

```
[mass]          train=691  test=201  SOLAPADOS=0
[calcification] train=602  test=151  SOLAPADOS=0
[GLOBAL]        train=1248 test=349  SOLAPADOS=31
```

Los 31 solapes globales existen porque el split oficial del CBIS-DDSM se hizo por separado para cada tipo de hallazgo: un paciente puede tener masas en train y calcificaciones en test.

**Impacto.** Es **evidencia a favor de D-005**. Tratar masas y calcificaciones como subproblemas independientes elimina la fuga por construcción; juntarlos la introduciría. Conviene ponerlo en el reporte como defensa preparada ante la pregunta previsible sobre *data leakage*.

---

### H-006 · El sdist de PyRadiomics en PyPI es incompilable
**Fecha:** 2026-08-25 · **→ Reporte:** §8.x

Tres bugs encadenados de empaquetado, ninguno atribuible al proyecto:
1. No existe feedstock en conda-forge.
2. `pyproject.toml` declara `version = "3.0.1a1"` mientras `PKG-INFO` dice `3.1.0`; pip lo rechaza por *inconsistent version*.
3. `MANIFEST.in` dice `recursive-include src/radiomics *` cuando la ruta real es `radiomics/src` — **invertida**. El tarball trae `cmatrices.c` pero no `cmatrices.h`, y la compilación muere en el `#include`.

**Impacto.** Justifica D-007. Vale la pena mencionarlo en §8.x como parte del análisis de viabilidad práctica: la reproducibilidad de un pipeline radiómico depende de dependencias frágiles.

---

### H-007 · El binning dominaba el coste, no la E/S
**Fecha:** 2026-08-25 · **→ Reporte:** §8.x, OE-6

| Config | Niveles de gris | Tiempo/caso | ETA 3,482 casos |
|---|---|---|---|
| `binWidth=25` | 1,139 | 29.8 s | ~38 h |
| `binCount=32` | 32 | **0.14 s** | **8 min** |
| `binCount=64` | 64 | 0.1 s | ~10 min |

Leer el DICOM completo cuesta 0.01 s: la E/S era irrelevante. El coste estaba en construir una GLCM de 1139×1139 sobre datos de 16 bits con rango 0–65535.

**Impacto.** Justifica D-008. Es también un dato citable para el OE-6 sobre coste computacional del pipeline.

---

### H-008 · Estructura por paciente del dataset
**Fecha:** 2026-08-24 · **→ Reporte:** §5.1

3,568 registros sobre 1,566 pacientes: media de **2.28 ROIs por paciente**, máximo 24. **56 pacientes** tienen lesiones benignas y malignas a la vez.

**Impacto.** Obliga a declarar la unidad de análisis (D-011) y descarta agregar por paciente sin una regla explícita.

---

### H-009 · Defectos verificables en el PDF de TT1
**Fecha:** 2026-08-24 · **→ Reporte:** Fase 7

- `sección ??` literal en la p. 56 — falta `\label{sec:metricas}` en la subsección 3.4
- 11 `\bibitem` nunca citados, entre ellos `Wang2020DeepLearning`, `Azevedo2022QuantumTransfer`, `Xiang2024QuantumCNN` y `Baccouche2022ResidualNN`, todos discutidos por nombre en el texto sin `\cite`
- Label `eq:embedding_vector` duplicado; *float* de 33 pt en la línea 973; 12 `Overfull \hbox`; `RNF- 9` con espacio
- "BCDR (Barcelona Digital Breast Cancer Dataset)" — es el **Breast Cancer Digital Repository**, portugués
- `Logos/ipn_logo.png` en minúsculas contra `IPN_logo.png` real: compila en macOS, revienta en Overleaf o Linux
- `Technical_Report.bib` tiene una llave `}` de más y solo 2 entradas, mientras la bibliografía real es un `thebibliography` manual de 47

---

### H-010 · El manifiesto NBIA nunca se guardó y la vía oficial de descarga falla
**Fecha:** 2026-09-21 · **→ Reporte:** §8.x

No existe ningún archivo `.tcia` en el disco: la descarga original del dataset se hizo y el manifiesto no se conservó. Sin él, NBIA Data Retriever no arranca — la aplicación no tiene interfaz para elegir qué bajar, se lanza haciendo doble clic sobre el manifiesto.

Reconstruir uno a partir de los `Series UID` de `metadata.csv` tampoco funcionó: el Data Retriever responde *"incorrect response from the server"*. El `downloadServerUrl` de un manifiesto apunta a un servlet cuyo protocolo no coincide con el de la API REST pública, aunque ese endpoint responda HTTP 200 por separado.

**Impacto.** Justifica D-012. Es además un dato citable sobre reproducibilidad: la obtención del dataset no está documentada en ningún punto del reporte, y la ruta oficial de descarga no es reproducible hoy. Conviene añadir a §8.x el procedimiento real que sí funciona.

---

### H-011 · El entrenamiento conjunto VQC↔MLP no escala
**Fecha:** 2026-09-21 · **→ Reporte:** §6.x, §8.x, OE-6

Coste del *backward* por `parameter-shift`, medido con `StatevectorEstimator` exacto e `input_gradients=False`:

| Configuración | backward | 50 épocas, ambos subconjuntos |
|---|---|---|
| k=8, reps=1 (16 pesos) | 548 ms/muestra | **22.4 h** |
| k=16, reps=1 (32 pesos) | 66.6 s/muestra | **2,689 h** |
| k=16, reps=3 (64 pesos) | 146.8 s/muestra | **5,883 h** |

Son horas por *condición*; C4 y C5 duplican la cifra. El coste no lo domina el álgebra lineal sino la sobrecarga por evaluación de la primitiva: el *forward* a k=16 tarda 1.0 s, pero el gradiente exige 2 × n_pesos × k evaluaciones por muestra.

Con θ **fijo**, el circuito pasa a ser una transformación determinista y los embeddings se calculan una sola vez:

| k | forward | dataset completo, ambos *feature maps* |
|---|---|---|
| 8 | 15.6 ms | 1.8 min |
| 12 | 84.7 ms | 10.1 min |
| 16 | 1001 ms | 119 min |

**Impacto.** RNF-07 declara k ∈ [8,16], pero la mitad superior de ese rango es inalcanzable con la arquitectura de M6 tal como está escrita. Obliga a resolver Q-007. Es también evidencia central para el OE-6: la restricción práctica del simulador no está en el número de qubits que puede simular, sino en el coste del gradiente.

---

### H-012 · C4 y C5 son el mismo circuito
**Fecha:** 2026-09-22 · **→ Reporte:** §4.7, §6.x

En Qiskit, `zz_feature_map` **está definido** como un `pauli_feature_map` con `paulis=['Z','ZZ']`. Pedir ese conjunto devuelve literalmente el mismo circuito. Medido por fidelidad entre los estados que preparan:

```
k=4:  |<phi_zz | phi_pauli>|^2 = 1.000000000000
k=8:  |<phi_zz | phi_pauli>|^2 = 1.000000000000
```

Evidencia concurrente: las 18 filas de `Code/results/5_benchmark_complejidad.csv` son idénticas entre ambos *feature maps* en profundidad, CX y número de puertas; y las diferencias de tiempo entre ellos en `5_benchmark_resultados.csv` (23.06 h contra 24.03 h a k=8) son ruido de medición, no señal.

Conjuntos alternativos, promediando sobre **200 entradas aleatorias** porque la fidelidad depende del vector de entrada:

| Conjunto | Media | Desv. est. | Máximo | CX |
|---|---|---|---|---|
| `['Z','ZZ']` | 1.000 | 0.000 | 1.000 | 12 |
| `['Z','Y','ZZ']` | 0.332 | 0.332 | 0.962 | 12 |
| `['X','ZZ']` | **0.071** | 0.134 | 0.727 | 12 |
| `['Z','YY']` | 0.109 | 0.129 | 0.706 | 12 |
| `['Y','ZZ']` | 0.315 | 0.151 | 0.992 | 12 |

**Impacto.** **Invalida D-002**, que separaba C4 y C5 para aislar el efecto del diseño del *feature map*: tal como están especificadas son una sola condición y esa comparación no mide nada. Todos los candidatos mantienen 12 CX, así que una segunda condición genuina no cuesta nada extra. Abre Q-008 y bloquea la escritura de M5.

**Nota metodológica.** La primera medición usó una sola entrada aleatoria y dio fidelidades de 0.000 para `['Z','Y','ZZ']` y `['X','ZZ']`. Era inestable: promediando, `['Z','Y','ZZ']` resulta ser de los **más parecidos** a ZZ, no de los más distintos. Un solo sorteo no caracteriza una codificación.

---

### H-013 · Sin ansatz, el embedding es idénticamente cero
**Fecha:** 2026-09-22 · **→ Reporte:** §3.2, §4.7

El ZZFeatureMap aplica únicamente Hadamards y puertas **diagonales**: los $R_Z$ y los bloques $CX\!-\!R_Z\!-\!CX$ son todos diagonales en la base computacional. Una puerta diagonal multiplica cada amplitud por una fase y no puede alterar su **magnitud**.

Partiendo de $H^{\otimes k}|0\rangle$, toda amplitud tiene magnitud $2^{-k/2}$. Como las diagonales la preservan, $P(\text{qubit}_i = 0) = 1/2$ exactamente, y por tanto:

$$\langle Z_i \rangle = 0 \quad \text{para todo } x$$

Verificado numéricamente: ceros con cualquier entrada. Con el ansatz de θ fijo aleatorio, los valores se separan de cero con normalidad.

**Impacto.** Tres consecuencias:

1. Bajo Arquitectura B (Q-007) **no se puede prescindir del ansatz**: θ debe quedar *fijo con semilla declarada*, no ausente. Es un parámetro reportable del experimento, no un detalle.
2. La información que inyecta el *feature map* vive en las **fases**, y una medición en Z es ciega a ellas. El ansatz es lo que rota esas fases hacia poblaciones medibles.
3. El **kernel de fidelidad no comparte esta limitación**, porque compara estados completos, fases incluidas. Por tanto las métricas basadas en kernel (KTA, *geometric difference*) y las basadas en ⟨Zᵢ⟩ (Davies-Bouldin, Fisher, y el MLP) miden **objetos genuinamente distintos** y pueden discrepar. Eso merece explicación explícita en §6 si KTA sale alto y la clasificación mediocre.

---

### H-014 · La precisión de los shots se ignora si se fija en el estimador
**Fecha:** 2026-09-22 · **→ Reporte:** §8.x

La primera corrida del estudio de shots dio un error prácticamente plano entre 512 y 8192 shots, lo cual es imposible: el error de muestreo debe decaer como $1/\sqrt{n}$.

Causa: `EstimatorQNN._forward` ejecuta

```python
job = self.estimator.run(circuit_observable_params, precision=self._default_precision)
```

y **pisa** cualquier `default_precision` con el que se haya construido el estimador. Configurarla en `AerEstimator(options=...)` no tiene efecto alguno.

Dispersión medida entre corridas repetidas, según dónde se fije la precisión:

| shots | en el estimador | en el QNN | esperada |
|---|---|---|---|
| 256 | 0.01644 | 0.06039 | 0.06250 |
| 1024 | 0.01585 | 0.02667 | 0.03125 |
| 8192 | 0.01347 | 0.01179 | 0.01105 |
| 65536 | 0.01623 | 0.00350 | 0.00391 |

La columna del estimador es plana; la del QNN sigue $1/\sqrt{n}$ como debe.

**Impacto.** Hay que separar dos cosas al redactar: que la precisión mejore como $1/\sqrt{n}$ es una **propiedad de la estadística de la medición cuántica** y va en el marco teórico; que el parámetro deba ir en un constructor concreto y se ignore silenciosamente en el otro es un **detalle de implementación de la librería** y va en §8.x. Sin documentarlo, los resultados no son reproducibles por terceros.

---

### H-015 · Coste de las alternativas a parameter-shift
**Fecha:** 2026-09-22 · **→ Reporte:** §8.x, OE-6

Coste del *backward* por muestra, con expectativas exactas e `input_gradients=False`:

| k | parameter-shift | lin-comb | SPSA |
|---|---|---|---|
| 4 | 91.4 ms | 494.8 ms | **12.8 ms** |
| 8 | 970.0 ms | excede 90 s | **98.5 ms** |

**SPSA es ~10× más rápido**; `lin-comb` es ~5× **más lento** que parameter-shift y a k=8 no termina en 90 segundos para dos muestras. A k=8, SPSA baja el entrenamiento de 38.6 h a 3.9 h por condición.

Para optimización sin gradiente (PSO), el coste por iteración es *enjambre × un forward sobre los datos*. Con 30 partículas y 200 iteraciones, sobre masas:

| k | PSO conjunto completo | PSO lote 128 | parameter-shift |
|---|---|---|---|
| 8 | 36.4 h | 3.5 h | 12.0 h |
| 12 | 205.3 h | 19.9 h | 95.4 h |
| 16 | 2,320.6 h | 225.4 h | 1,326.0 h |

**Impacto.** Ningún método rescata la Arquitectura A. SPSA extrapolado a k=12 daría ~19 h contra las 2.95 h del embedding precomputado, y además solo *aproxima* el gradiente, así que necesita más iteraciones para converger y la ganancia efectiva es menor que el 10×. PSO con mini-lotes gana ~5× sobre parameter-shift pero sigue un orden de magnitud por encima de no entrenar θ.

Sobre las mesetas áridas: los métodos sin gradiente **no las esquivan**, porque en una meseta las *diferencias de costo* entre puntos son ellas mismas exponencialmente pequeñas y un enjambre acaba moviéndose por ruido. **PENDIENTE DE VERIFICAR** antes de citar: Arrasmith, Cerezo, Czarnik, Cincio y Coles, *Effect of barren plateaus on gradient-free optimization*, Quantum 5, 558 (2021).

El único valor propio de PSO es poder optimizar objetivos **no diferenciables** —AUC-ROC, KTA, razón de Fisher—, capacidad que ningún método basado en gradiente tiene. Ninguna de las métricas de separabilidad de este trabajo es naturalmente diferenciable.

**Nota.** Las cifras absolutas de esta tabla son ~2× más lentas que una medición previa de los mismos métodos, por carga de la máquina. Valen como comparación **relativa** entre métodos, no como tiempos absolutos.

---

### H-016 · Sesgo sistemático entre AerSimulator y statevector
**Fecha:** 2026-09-23 · **→ Reporte:** §8.x, OE-6

El estudio de shots comparaba el estimador con muestreo contra el valor exacto por *statevector*, y la pendiente log-log salía −0.31 en vez de −0.5, incluso promediando 10 repeticiones por punto con barras de error de ±0.001. No era ruido.

Forzando el número de shots muy por encima del rango de trabajo, el error **se estanca y no converge a cero**:

| shots | MAE vs statevector | 1/√n esperado | razón |
|---|---|---|---|
| 8,192 | 0.014989 | 0.011049 | 1.36 |
| 65,536 | 0.013128 | 0.003906 | 3.36 |
| 262,144 | 0.013043 | 0.001953 | 6.68 |
| 1,048,576 | 0.012826 | 0.000977 | 13.13 |

Hay un **suelo de ~0.013** que no depende del muestreo: es una diferencia determinista entre los dos backends, no varianza estadística.

**Impacto.** La comparación «Aer con shots contra statevector exacto» **no mide la ley $1/\sqrt{n}$**: a partir de unos 8,000 shots queda dominada por la diferencia entre backends. La figura del OE-6 construida así habría sido engañosa.

**Corrección.** El ruido de muestreo se mide correctamente como la **dispersión del estimador entre repeticiones** con el mismo número de shots, que aísla la varianza estadística del sesgo de backend:

| shots | dispersión entre repeticiones | 1/√n esperado | sesgo vs statevector |
|---|---|---|---|
| 512 | 0.04140 | 0.04419 | 0.01699 |
| 1,024 | 0.02838 | 0.03125 | 0.01507 |
| 2,048 | 0.02108 | 0.02210 | 0.01407 |
| 4,096 | 0.01438 | 0.01562 | 0.01322 |
| 8,192 | 0.01006 | 0.01105 | 0.01264 |

Pendiente log-log de la dispersión: **−0.5065**, contra la teórica −0.5. La columna de sesgo apenas se mueve, lo que confirma que son dos fenómenos distintos.

**Para el reporte.** Conviene presentarlo como dos observaciones separadas, porque lo son: el ruido de muestreo sigue la estadística esperada, y además el simulador introduce un sesgo constante respecto al cálculo exacto. Lo segundo es una restricción práctica del simulador y por tanto material directo del OE-6. **Queda sin identificar la causa del sesgo** (transpilación interna de Aer, redondeo del número de shots derivado de `default_precision`, u otra); investigarla si hay holgura, o declararla como limitación si no.

**Datos.** `Code/results/7_shots_repetido.csv`, figura `Docs/Figures/E3_shots_sensitivity.png`.

---

### H-017 · Un solo sorteo de θ no sostiene ninguna conclusión sobre concentración
**Fecha:** 2026-09-23 · **→ Reporte:** §8.x, OE-6

Bajo Arquitectura B, θ queda fijo y aleatorio, lo que abre una pregunta legítima: ¿se concentra el embedding al aumentar la profundidad o el número de qubits, como haría esperar el fenómeno de mesetas áridas? Se midió la desviación estándar de ⟨Zᵢ⟩ entre 200 entradas, con **un** sorteo de θ por configuración:

| k | reps=1 | reps=2 | reps=3 |
|---|---|---|---|
| 8 | 0.0544 | 0.0732 | 0.0908 |
| 12 | 0.0337 | 0.0493 | 0.0301 |
| 16 | 0.0373 | 0.0560 | 0.0248 |

**No hay patrón.** A k=8 la dispersión *crece* con la profundidad; a k=12 y k=16 sube y luego baja. Tampoco es consistente entre valores de k.

**Impacto.** La variación observada está dominada por **el sorteo de θ**, no por la profundidad ni por el número de qubits. Con una sola realización por configuración el experimento no distingue señal de ruido, y una figura construida así invitaría a leer una tendencia que los datos no sostienen.

**Corregido.** Se repitió promediando 10 sorteos de θ por configuración; el resultado está en H-018. El promediado confirma el diagnóstico: a k=8, `reps=1` y `reps=2` resultan indistinguibles (0.0854 contra 0.0849), cuando el sorteo único indicaba un aumento del 35 %.

**Advertencia general que conviene retener.** Este es el segundo caso en el mismo día en que una medición de una sola realización produjo un número engañoso; el primero fueron las fidelidades de los conjuntos de Pauli en H-012, donde un único vector de entrada dio 0.000 para un candidato que promediando resulta ser de los más parecidos a ZZ. **Cualquier cantidad que dependa de un sorteo aleatorio —θ, el vector de entrada, la partición— debe reportarse como distribución, no como valor puntual.**

---

### H-018 · El embedding se concentra con el número de qubits, no con la profundidad
**Fecha:** 2026-09-23 · **→ Reporte:** §6.x, OE-6

Repetición de H-017 promediando **10 sorteos de θ** por configuración, sobre 100 entradas. Desviación estándar de ⟨Zᵢ⟩ entre muestras, media ± desviación entre sorteos:

| k | reps=1 | reps=2 | reps=3 |
|---|---|---|---|
| 8 | 0.0854 ± 0.0128 | 0.0849 ± 0.0092 | 0.0735 ± 0.0049 |
| 12 | 0.0456 ± 0.0064 | 0.0573 ± 0.0033 | 0.0349 ± 0.0041 |
| 16 | 0.0412 ± 0.0082 | 0.0412 ± 0.0039 | 0.0240 ± 0.0015 |

Tres lecturas, y conviene no mezclarlas:

**1. La concentración con el número de qubits es clara.** A reps=1 la dispersión cae de 0.0854 (k=8) a 0.0456 (k=12) y 0.0412 (k=16). El salto de k=8 a k=12 excede holgadamente las barras de error; el de k=12 a k=16 queda dentro de ellas. Es el comportamiento que anticipa el fenómeno de mesetas áridas: al crecer el espacio de Hilbert, los valores de expectativa se concentran.

**2. La concentración con la profundidad NO es monótona en el rango probado.** `reps=1` y `reps=2` son indistinguibles a k=8 y a k=16, y a k=12 la dispersión *aumenta* de 0.0456 a 0.0573, con barras que apenas se solapan. Solo `reps=3` queda consistentemente por debajo en los tres valores de k. No se puede afirmar que más capas concentren el embedding entre 1 y 3.

**3. La variabilidad entre sorteos de θ sí colapsa con la profundidad.** A k=16 la desviación entre sorteos pasa de 0.0082 a 0.0039 y a 0.0015. Es decir, circuitos más profundos producen una dispersión más uniforme **con independencia de θ**. Esa pérdida de sensibilidad a los parámetros es la firma característica de la meseta árida, y es una observación más sólida que la del punto 2.

**Impacto sobre D-013.** Refuerza `reps=1` con un argumento positivo y no solo de coste: `reps=1` entrega la **máxima dispersión del embedding** —empatada con `reps=2`— al mínimo coste computacional. Un embedding más disperso porta más información discriminable, de modo que la elección barata coincide aquí con la mejor.

**Impacto sobre k.** Es un matiz relevante para D-013 que conviene declarar: el embedding a k=12 ya está notablemente más concentrado que a k=8. La elección de k=12 se justificó por coste y por diversidad de familias de features, no por dispersión; si en M4 la separabilidad a k=12 resultara pobre, este resultado sugiere que **k=8 merecería una comparación** antes de dar por buena la conclusión.

**Datos.** `Code/results/7_concentracion_embedding.csv`; figura `Docs/Figures/E4_embedding_concentration.png`. Medición sobre datos sintéticos uniformes en [0,π]^k, apropiada para caracterizar el circuito pero **no sustituye** la medición sobre features radiómicas reales una vez exista M3.

---

## Preguntas abiertas

### Q-001 · ¿C2 se declara control nulo o se añade C2′?
**Bloquea:** Fase 4 · **Límite:** 2 oct

M4 ya reduce a `k` features, así que C2 hace PCA de k → k: una rotación ortogonal invertible. Davies-Bouldin, Fisher y KTA son invariantes bajo rotación, de modo que **C2 dará métricas idénticas a C1**, y el MLP absorbe la rotación en su primera capa.

Salidas: (a) declararlo control nulo, que es defendible y hasta elegante — demuestra que las métricas no se dejan engañar por transformaciones lineales; (b) añadir C2′ con PCA desde el vector radiómico completo (n ≈ 100–300) → k, que es el baseline clásico honesto. Hacer las dos cuesta poco.

---

### Q-002 · ¿Con qué θ se mide la separabilidad?
**Bloquea:** Fase 4 · **Límite:** 25 sep

C4/C5 entrenan θ contra las etiquetas vía `TorchConnector`; C2 y C3 son no supervisados. Medir separabilidad post-entrenamiento haría salir la ventaja cuántica por construcción, y es atacable.

Propuesta: medir el OE-3 con el **feature map solo** (sin ansatz, o con θ aleatorio fijo por semilla), que además es literalmente la pregunta de investigación — si la *codificación* mejora la separabilidad. El entrenamiento end-to-end se queda para OE-4/OE-5. Reportar separabilidad pre y post sería un análisis adicional valioso.

---

### Q-003 · ¿Sobre qué kernel se calcula la *geometric difference*?
**Bloquea:** Fase 3 · **Límite:** 11 sep

`g(K_C, K_Q)` de Huang et al. está definida **kernel contra kernel**. M5 produce ⟨Zᵢ⟩ ∈ [-1,1]^k, que es un vector, no un kernel cuántico: construir un RBF sobre los ⟨Zᵢ⟩ ya no es K_Q y el marco de Huang no aplica.

Propuesta: calcular el kernel de fidelidad K_Q(x,x') = |⟨φ(x)|φ(x')⟩|² aparte, con `FidelityQuantumKernel`, usando solo el feature map — el mismo objeto que resuelve Q-002.

---

### Q-004 · ¿Azevedo et al. (2022) o Incudini et al. (2022)?
**Bloquea:** Fase 7 · **Límite:** 3 nov

El reporte atribuye a **Azevedo et al. (2022)** las dos líneas de trabajo futuro sobre las que se construye el proyecto (§1.3 y §2.1.5), y es internamente consistente. El contexto persistente del proyecto dice **Incudini et al. (2022)**. Son papers distintos. Hay que verificar contra la fuente cuál afirma qué y unificar.

**Resuelta el 2026-09-23 → D-019:** la atribución correcta es Azevedo et al. (2022).

---

### Q-005 · ¿Validación cruzada o justificación de su ausencia?
**Bloquea:** Fase 6 · **Límite:** 23 oct

Aparece en el cronograma del reporte (ago–sep) y en el acta de los directores como compromiso, pero **no existe en la metodología** (§4.9). O se implementa, o se justifica explícitamente por el coste del *parameter-shift*. No puede quedarse sin respuesta.

---

### Q-006 · ¿Qué k y reps finales?
**Bloquea:** Fase 3 · **Límite:** 11 sep

Depende del benchmark de la semana 1. El reporte declara k ∈ [8,16] y `reps` ∈ [1,6] (RNF-07). Hay que fijar el valor de trabajo con datos medidos, no por defecto.

---

---

### Q-007 · ¿Entrenamiento conjunto o embedding precomputado?
**Bloquea:** Fases 4 y 5 · **Límite:** 25 sep

H-011 midió que la arquitectura descrita en §4.8 —integrar el VQC con el MLP vía `TorchConnector` y optimizar θ junto con los pesos— cuesta 22.4 h a k=8 y 2,689 h a k=16, por condición. No es viable.

La alternativa es fijar θ y precomputar los embeddings: el mismo experimento baja a minutos y mantiene abierto todo el rango k ∈ [8,16] que declara RNF-07.

Lo relevante es que **las dos razones apuntan al mismo lado**. Q-002 ya pedía medir la separabilidad con θ no entrenado para que la comparación contra C2 y C3 —que son no supervisados— fuera justa. El coste computacional lleva de forma independiente a la misma arquitectura.

Si se opta por precomputar, hay que reescribir §4.8 y §4.9: `TorchConnector` deja de ser necesario y el MLP pasa a entrenarse sobre una matriz en caché. Decidir antes de escribir código de M5.

---

---

### Q-008 · ¿Qué conjunto de Pauli usa C5?
**Bloquea:** M5, Fase 4 · **Límite:** 25 sep

H-012 demostró que C4 y C5, tal como las define §4.7, son la misma condición. C5 necesita un conjunto de Pauli genuinamente distinto, y la elección cambia qué se afirma estar comparando.

El candidato más alejado de ZZ en todo el rango de entrada es **`['X','ZZ']`** (media 0.071, máximo 0.727). `['Z','Y','ZZ']` queda descartado: promedia 0.332 con máximo 0.962, o sea que sobre buena parte del espacio de entrada codifica casi lo mismo que ZZ.

Todos los candidatos mantienen 12 CX, así que la decisión no tiene coste computacional. Lo que sí cambia es el argumento: `['X','ZZ']` sustituye la codificación de primer orden en Z por una en X, mientras `['Z','YY']` mantiene Z y altera el término de entrelazamiento. Son afirmaciones distintas sobre qué aspecto del diseño del *feature map* se está aislando.

Al resolverla: convertir en D-013, actualizar §4.7 y la Tabla de condiciones experimentales, y dejar constancia de que D-002 quedó invalidada por H-012.

## Plantillas

```markdown
### D-0XX · <título en una línea>
**Fecha:** AAAA-MM-DD · **Módulo:** MX · **Estado:** Firme | Provisional | Revertida · **→ Reporte:** §X.X

**Contexto.** Qué problema apareció.
**Alternativas.** A (por qué no), B (por qué no), C (elegida).
**Decisión.** Qué se hace exactamente.
**Por qué.** El argumento. Si hay un supuesto, decirlo.
**Evidencia.** Número, medición o cita. Si no hay, escribir "ninguna todavía".
**Consecuencias.** Qué habilita y qué rompe.
```

```markdown
### H-0XX · <título en una línea>
**Fecha:** AAAA-MM-DD · **→ Reporte:** §X.X

Qué se descubrió, con el dato o la salida que lo respalda.

**Impacto.** Qué cambia en el diseño, en el reporte o en el calendario.
```

```markdown
### Q-0XX · <la pregunta, en forma de pregunta>
**Bloquea:** Fase X · **Límite:** DD mes

Por qué está abierta y cuáles son las salidas posibles.
Cuando se cierre: convertir en D-0XX y dejar aquí el enlace.
```

