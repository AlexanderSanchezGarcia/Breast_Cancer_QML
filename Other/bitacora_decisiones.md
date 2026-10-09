# Bitácora de decisiones · TT 2026-B039

> Registro vivo del desarrollo. Cada entrada dice **por qué** se hizo algo, no solo qué.
> En noviembre esto alimenta las secciones 6–8 del reporte técnico, y es lo que se defiende ante el jurado.

**Cómo usar esto.** Tres tipos de entrada, porque no son lo mismo:

| Tipo | Es | Lo que no puede faltar |
|---|---|---|
| **D** · Decisión | Elegiste entre opciones | Las alternativas y el porqué |
| **H** · Hallazgo | Descubriste algo que no sabías | La evidencia numérica y la consecuencia |
| **Q** · Pregunta abierta | Aún no está resuelto | La fecha límite para resolverla |

**Rutas actualizadas el 2026-09-24:** los notebooks de benchmarking pasaron a `Code/benchmark/` como B1, B2 y B3, antes 5, 6 y 7, y sus resultados a `B1_*` y `B3_*`. Las entradas anteriores ya citan las rutas nuevas.

Numeración correlativa, nunca se reutiliza. Si una decisión se revierte, **no se borra**: se marca `Revertida` y se enlaza la que la reemplaza — el jurado valora más un cambio de rumbo justificado que un historial impecable. Las plantillas están al final.

---

## Índice

### Decisiones

| # | Fecha | Decisión | Módulo | Estado | → Reporte |
|---|---|---|---|---|---|
| D-001 | 2026-05 | SelectKBest + MinMaxScaler en lugar de PCA antes del circuito | M4 | Firme; el escalador pasa a cuantiles (D-025) | §4.6, §7.2 |
| D-002 | 2026-05 | ZZFeatureMap y PauliFeatureMap como condiciones separadas | M5 | **Revertida** (ver H-012, Q-008) | §4.7, §7.2 |
| D-003 | 2026-05 | Geometric difference como métrica de ventaja cuántica potencial | M7 | Firme | §3.4.2, §7.2 |
| D-004 | 2026-05 | Escalado angular a [0,π] y no a [0,2π] | M4 | Firme | §4.6 |
| D-005 | 2026-05 | Masas y calcificaciones como subproblemas independientes | todos | Firme | §4.4 |
| D-006 | 2026-05 | PyRadiomics (Estrategia A) en lugar de encoder CNN | M3 | Firme | §4.5 |
| D-007 | 2026-08-25 | Entorno `radiomics` separado, compilado desde GitHub | infra | Firme; PyRadiomics también en `qml_cancer` desde el 2026-09-23 | §8.x |
| D-008 | 2026-08-25 | `binCount=32` en lugar de `binWidth` | M3 | Firme | §8.x |
| D-009 | 2026-08-25 | Sin resize a 224×224 en la ruta radiómica | M2 | Firme | §4.4, §8.x |
| D-010 | 2026-08-25 | CLAHE fuera de la ruta radiómica | M2 | Firme (evidencia en H-025) | §4.4 |
| D-011 | 2026-08-25 | Unidad de análisis = lesión/ROI, no paciente | M4 | Firme (2026-09-22) | §4.6 |
| D-012 | 2026-09-21 | Descargar por la API REST de TCIA, no con NBIA Data Retriever | M1 | Firme | §8.x |
| D-013 | 2026-09-22 | Punto de operación: k=12 qubits, reps=1 | M4, M5 | Firme | §4.6, §4.7 |
| D-014 | 2026-09-22 | Arquitectura B: embedding precomputado con θ fijo (semilla 42) | M5, M6 | Firme | §4.7, §4.8 |
| D-015 | 2026-09-22 | C5 usa `pauli_feature_map(paulis=['X','ZZ'])` | M5 | **Revertida** por D-031 (H-034) | §4.7 |
| D-016 | 2026-09-22 | C2 se declara control nulo; se mantienen cinco condiciones | M5, M7 | Firme | §4.7, §6.x |
| D-017 | 2026-09-22 | La *geometric difference* se calcula con `FidelityQuantumKernel` | M7 | Firme; protocolo de cálculo en D-032 | §3.4.2, §4.9 |
| D-018 | 2026-09-22 | Validación cruzada 5-fold estratificada sobre el conjunto de entrenamiento | M6 | Firme | §4.8, §4.9 |
| D-019 | 2026-09-23 | Las líneas de trabajo futuro se atribuyen a Azevedo et al. (2022) | reporte | Firme | §1.3, §2.1.5 |
| D-020 | 2026-09-23 | Alinear cada máscara según su tipo de desajuste, no remuestrear las 80 | M2 | Provisional | §4.4, §8.x |
| D-021 | 2026-09-23 | Reducir cada máscara a su componente conexa mayor | M2 | Provisional | §4.4, §8.x |
| D-022 | 2026-09-23 | Contrato de salida de M2: caja + 20 px, intensidades crudas, NRRD | M2, M3 | Provisional | §4.4, §8.x |
| D-023 | 2026-09-23 | M3 extrae 67 features: cuatro familias sobre la imagen original, sin filtros | M3 | Firme | §4.5 |
| D-024 | 2026-09-23 | Selección por F-test con restricción de redundancia \|r\| ≤ 0.95 | M4 | Firme | §4.6 |
| D-025 | 2026-09-23 | Escalado angular por cuantiles (uniforme × π) en lugar de min-max | M4 | Firme | §4.6 |
| D-026 | 2026-09-23 | Semilla de los folds elegida por balance de clases | M4, M6 | Firme | §4.9 |
| D-027 | 2026-09-24 | γ del RBF por heurística de la mediana (C3 y kernel clásico de la *geometric difference*) | M5, M7 | Firme para C3; para *g*, enmendada por D-032 | §4.7, §4.9 |
| D-028 | 2026-09-24 | Separabilidad sobre 200 lesiones de train por subconjunto, estratificadas | M5, M7 | Firme | §4.9 |
| D-029 | 2026-09-24 | Kernel concentrado: se mantiene el diseño preregistrado y se añade un barrido del factor de escala | M5, M7 | Firme | §4.9, §6.x, OE-6 |
| D-030 | 2026-09-24 | La separabilidad pasa a ser el Módulo 6; la clasificación, el M7, y la evaluación comparativa, el M8 | todos | Firme | §4.1–§4.9, RF, CRISP-DM |
| D-031 | 2026-10-05 | C5 pasa a `pauli_feature_map(paulis=['Y','ZZ'])` | M5 | Firme | §4.7, §6.x |
| D-032 | 2026-10-06 | La *geometric difference* sigue el protocolo de Huang et al. (Apéndice L.3) | M6 | Firme | §3.4.2, §4.9, RF-16 |
| D-033 | 2026-10-06 | Definiciones de las demás métricas del M6 | M6 | Firme | §4.9 |
| D-034 | 2026-10-06 | Se reproduce la Fig. 2 de Huang et al. (2021) en el reporte | reporte | Firme | §3.4.2 |
| D-035 | 2026-10-06 | Se compara contra k = 8 antes de concluir el OE-3, como experimento X3 | M4–M6 | Firme | §6.x, §7, OE-6 |
| D-036 | 2026-10-06 | Protocolo de clasificación del M7: MLP 32-16, estandarización y parada temprana por paciente | M7 | Provisional | §4.8, §6.x |
| D-037 | 2026-10-06 | Análisis de sensibilidad del M7: reps = 2 en el ansatz, k = 8, semillas y configuraciones | M7 | Firme | §6.x, §7 |
| D-038 | 2026-10-07 | Análisis exploratorios X4 a X6: QSVM, auditoría y búsqueda de ventaja, con protocolo simétrico | X4–X6 | Firme | §6.x, §7 |
| D-039 | 2026-10-07 | El Spearman del M8 se reporta como descriptivo: por subconjunto, con su distribución exacta para n = 5 | M8 | Firme | §3.4, §4.10, §6.x |
| D-040 | 2026-10-07 | Contenido del M8: OE-6 medido (qubits, shots en el embedding y en el kernel) y referencia con los descriptores del radiólogo | M8 | Provisional | §4.10, §6.x, §7, OE-6 |

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
| H-016 | 2026-09-23 | ~~AerSimulator tiene un sesgo sistemático de ~0.013 frente a statevector~~ | **Invalidado por H-019**: el sesgo no existe, la referencia llevaba ruido |
| H-017 | 2026-09-23 | Un solo sorteo de θ no permite concluir nada sobre concentración del embedding | Obliga a promediar; advertencia metodológica general |
| H-018 | 2026-09-23 | El embedding se concentra con el número de qubits, no con la profundidad | Material del OE-6; a k=12 reps=2 dispersa un 30 % más que reps=1, así que reps=1 se sostiene por coste, no por dispersión · **cifras rehechas sin ruido (H-019)** |
| H-019 | 2026-09-23 | El «sesgo» de H-016 era ruido en la referencia, y el estimador de Aer no muestrea | Invalida H-016 y la figura E3; obliga a repetir H-018; regla de precisión 0 para M5 |
| H-020 | 2026-09-23 | Las 80 máscaras desalineadas son de dos tipos; los recortes oficiales verifican la alineación al píxel | Corrige el procedimiento de H-004; justifica D-020 |
| H-021 | 2026-09-23 | El 86.3 % de las máscaras de masas trae islas desconectadas | Justifica D-021; acota su efecto sobre las *shape features* |
| H-022 | 2026-09-23 | CLAHE de OpenCV sobre 16 bits con `clipLimit=2` es casi la identidad | La variante de D-010 se exporta en 8 bits; si no, la comparación de M3 sería un artefacto |
| H-023 | 2026-09-23 | Con el conjunto completo, el mayor \|d\| en masas es 0.50, no 1.42 | Corrige H-003; cambia la justificación numérica de D-009 |
| H-024 | 2026-09-23 | El top 12 de masas no tiene textura y contiene duplicados exactos | Debilita el argumento de contenido de D-013; M4 debe deduplicar antes de seleccionar |
| H-025 | 2026-09-23 | CLAHE cambia las features pero no su poder discriminativo | Cierra D-010 con evidencia |
| H-026 | 2026-09-23 | Con la restricción de redundancia entra textura en masas, de forma estable | Resuelve la objeción de H-024 a D-013 |
| H-027 | 2026-09-23 | Los folds deben agruparse por paciente, y la semilla 42 desbalancea los de calcificaciones | Aplica la regla de D-018; decisión pendiente sobre la semilla |
| H-028 | 2026-09-23 | Min-max deja casi constantes los ángulos de las features de cola pesada | Puede sesgar la comparación contra C3–C5; decisión pendiente |
| H-029 | 2026-09-23 | El procedimiento documentado para instalar PyRadiomics no funcionaba | Corrige `Code/env/README.md`; reproducibilidad del entorno |
| H-030 | 2026-09-24 | La selección univariante no ve interacciones, que es justo lo que codifica el bloque ZZ | Limitación a declarar en §7; análisis de robustez opcional |
| H-031 | 2026-09-24 | A 12 qubits, cambiar una sola feature deja el estado del feature map casi ortogonal | **Confirmado**: el kernel cuántico real está concentrado (mediana ~0.003); decisión pendiente (Q-011) |
| H-032 | 2026-09-24 | `FidelityStatevectorKernel` da el mismo kernel exacto ~1000× más rápido que `FidelityQuantumKernel` | El cuello de botella del kernel medido en B1 era de la implementación, no del cálculo |
| H-033 | 2026-09-24 | La ecuación de la *geometric difference* del reporte invierte K_C y K_Q respecto a Huang et al. | Corrección obligatoria en §3.4.2 y RF-16; la versión regularizada se extrajo en H-038 |
| H-034 | 2026-09-24 | Con reps=1, el término X de C5 no codifica nada: C5 es un mapa solo ZZ | C4 contra C5 no compara el eje Z frente a X; resuelto por D-031 |
| H-035 | 2026-10-04 | Pasar de 67 a 12 features cuesta de 2 a 4 puntos de AUC, y las 12 elegidas por F no superan a 12 al azar | Limitación a declarar en §7 y material del OE-6; no cambia el diseño; refuerza H-030 |
| H-036 | 2026-10-04 | Con c = 1, el kernel cuántico conserva poca de la información de clase que ve el RBF; achicar los ángulos la recupera solo hasta el nivel clásico | Anticipa el M6; material de §6 y OE-6; cifras de C5 rehechas con D-031 |
| H-037 | 2026-10-05 | Con `['Y','ZZ']`, C5 se dispersa tres veces más que C4 en ⟨Zᵢ⟩, pero su kernel se concentra unas setenta veces más | Caso concreto de H-013: el M6 debe reportar ambas familias de métricas; material del OE-6 |
| H-038 | 2026-10-06 | La *g* que reportan Huang et al. es regularizada y es el mínimo sobre una batería de kernels clásicos | Cierra el pendiente de H-033; justifica D-032 y D-033 |
| H-039 | 2026-10-06 | A c = 1 los kernels cuánticos apenas ven las clases, ocupan casi todo el espacio y quedan a g ≈ 1.4–1.7 del modelo clásico más cercano | Respuesta del OE-3 en la familia de kernels; material de §6 y OE-6 |
| H-040 | 2026-10-06 | Los embeddings cuánticos son menos separables que los clásicos, y C4 frente a C5 no tiene ganador | Respuesta del OE-3 en la familia de embeddings; anticipa el M7 |
| H-041 | 2026-10-06 | Con 8 qubits la concentración baja y los kernels cuánticos ven algo más las clases, pero la conclusión del M6 se mantiene | Cierra Q-013; la conclusión del OE-3 no depende de k = 12; material del OE-6 |
| H-042 | 2026-10-06 | El mismo MLP clasifica peor sobre las representaciones cuánticas: de 0.07 a 0.14 menos de AUC en el test | Respuesta del OE-4 y OE-5; coherente con el M6 |
| H-043 | 2026-10-06 | El resultado del M7 resiste semillas, red, escalado, parada temprana, reps = 2 y k = 8 | Descarta el subentrenamiento como explicación; corrige la lectura de H-018 sobre datos reales |
| H-044 | 2026-10-07 | Un QSVM sobre el kernel de C4 iguala al SVM clásico y supera al MLP sobre los ⟨Zᵢ⟩: la información se pierde en la lectura, no en la codificación | Matiza H-039 y H-042; material de §6 y §7 |
| H-045 | 2026-10-07 | Con las 67 features tampoco hay ventaja: los kernels cuánticos simulables son clásicos o se concentran | Responde la pregunta de las 67 features; material del OE-6 |
| H-046 | 2026-10-07 | La auditoría independiente del pipeline no encuentra errores (25 de 25) | Descarta que un error esconda una ventaja |
| H-047 | 2026-10-07 | Con la misma búsqueda anidada en ambos lados, ningún kernel cuántico supera a los clásicos en las etiquetas reales | Cierra la búsqueda de ventaja con el protocolo de D-038; dos hipótesis refutadas |
| H-048 | 2026-10-07 | Etiquetas construidas según el Apéndice G dan una ventaja cuántica grande sobre las mismas lesiones: la ausencia de ventaja es una propiedad de la tarea | Respuesta central para §7: por qué la literatura reporta ventajas y aquí no |
| H-049 | 2026-10-07 | Los rankings de separabilidad y de clasificación coinciden en lo esencial: lo clásico va delante en todos (ρ_s de 0.67 a 0.97) | Respuesta del OE-5 (RF-21); corrige la ecuación de Spearman del §3.4 |
| H-050 | 2026-10-07 | Con los descriptores del radiólogo las masas son más separables; con las features radiómicas, menos | La inversión respecto al EDA está en las features; material de §5, §6 y §7 |
| H-051 | 2026-10-07 | El simulador admite unos 25 qubits para el embedding y 22 para el kernel en esta máquina; el techo del diseño fue el gradiente | OE-6 (RF-22): tiempo por muestra, qubits y *parameter-shift* |
| H-052 | 2026-10-07 | Con 1,024 shots el MLP recupera casi todo el AUC exacto, pero a c = 1 entre el 16 y el 74 % de los valores del kernel leería 0 | OE-6 (RF-22, RNF-05): la concentración hace al kernel inmedible en hardware |

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
| Q-009 | ¿Min-max, logaritmo o cuantiles para las features de cola pesada? | M5, Fase 4 | **RESUELTA** → D-025 |
| Q-010 | ¿Semilla 42 para los folds, o una elegida por balance de clases? | M6, Fase 5 | **RESUELTA** → D-026 |
| Q-011 | ¿Qué se hace con el kernel cuántico concentrado? | M5, Fase 4 | **RESUELTA** → D-029 |
| Q-012 | ¿C5 se mantiene como mapa solo ZZ o se cambia por un conjunto con primer orden efectivo? | M5, M6 | **RESUELTA** → D-031 |
| Q-013 | ¿Se compara contra k = 8 antes de concluir, como pide H-018? | Conclusión del OE-3 | **RESUELTA** → D-035 |

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

**Ampliado el 2026-09-23, a petición del autor.** PyRadiomics se instala también en `qml_cancer`, compilado desde el mismo commit (`8ed579383b44806651c463d5e691f3b2b57522ab`), para que los notebooks lo resuelvan en cualquiera de los dos entornos. El riesgo que motivó la alternativa descartada, contaminar el stack cuántico, se controló así:

- Una prueba en seco confirmó que la instalación solo añadía paquetes. El único paquete existente que cambia es `packaging`, de 25.0 a 26.3, porque lo exige `setuptools_scm`; numpy sigue en 2.2.6.
- `pip check` no reporta conflictos, y Aer y Statevector siguen coincidiendo en 7×10⁻¹⁶.
- Las features extraídas en `qml_cancer` son **idénticas** a las de M3 extraídas en `radiomics`: diferencia relativa máxima 0 en 100 extracciones, aunque SimpleITK es 2.5.3 en un entorno y 2.5.6 en el otro.

`radiomics` sigue siendo el entorno de referencia de M2 y M3.

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

**Cifras actualizadas el 2026-09-23 (M2, conjunto completo).** El rango 41×65 a 1137×1641 venía de una muestra. Sobre las 3,568 lesiones, la caja de la lesión mide entre 86×55 y 1329×1365 px en masas (mediana 302×304) y entre 33×33 y 3801×2873 px en calcificaciones (mediana 273×289). Son las cifras que deben ir en §4.4.

**Evidencia revisada el 2026-09-23 (H-023).** El |d| ≈ 1.42 de H-003 no se sostiene con el conjunto completo: en masas las medidas de tamaño tienen |d| de 0.40 a 0.45, y cinco de ellas entran en el top 12. La decisión se mantiene, porque redimensionar igualaría esa señal a cero sea cual sea su magnitud, pero §4.4 no debe citar 1.42.

---

### D-010 · CLAHE fuera de la ruta radiómica
**Fecha:** 2026-08-25 · **Módulo:** M2 · **Estado:** Firme (cerrada con evidencia el 2026-09-23, H-025) · **→ Reporte:** §4.4

**Contexto.** El diseño de TT1 aplica CLAHE antes de extraer características.

**Decisión provisional.** Extraer las features del recorte crudo. Generar además la variante con CLAHE y **reportar el efecto de ambas**.

**Por qué.** CLAHE es correcto para entrada a CNN o para visualización, pero es una ecualización local dependiente del contenido: rompe la reproducibilidad de *first-order* y GLCM bajo IBSI.

**Por qué sigue provisional.** Correr ambas variantes cuesta poco y convierte una objeción potencial en media sección de resultados. Se cierra cuando existan los dos conjuntos de features.

**Cerrada el 2026-09-23 (H-025).** Ya existen los dos conjuntos de features. CLAHE reordena las lesiones (Spearman mediana ≈ 0.84 frente a la variante cruda), pero no cambia su poder discriminativo: la mediana del cambio en |d| es −0.002 en masas y −0.010 en calcificaciones. Dejarlo fuera no cuesta señal y preserva la reproducibilidad.

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

**Evidencia.** `Code/results/B1_benchmark_resultados.csv`, `B1_benchmark_arquitectura.csv`, `B1_benchmark_kernel_proyeccion.csv`.

**Consecuencias.** M4 fija k=12 en `SelectKBest`. **Verificar en M4 qué familias de features sobreviven a la selección y reportarlo**: si salen doce variables de tamaño casi idénticas, el argumento de contenido se debilita y habría que forzar diversidad de familias.

**Verificado en M3 (H-024).** En masas el argumento de contenido **no se cumple**: el top 12 tiene 7 features de primer orden, 5 de forma y ninguna de textura, e incluye duplicados exactos. En calcificaciones sí se cumple: 5 GLRLM, 4 GLCM, 2 de forma y 1 de primer orden. La respuesta, deduplicar o forzar diversidad, es una decisión de M4.

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

**Evidencia.** `Code/results/B1_benchmark_arquitectura.csv`; H-011 y H-015.

**Consecuencias.** Hay que reescribir §4.8 y §4.9. θ pasa a ser un **parámetro reportable del experimento**, no un detalle: por H-013 determina qué proyección de la información de fase resulta visible. Como beneficio colateral, entrenar toma segundos, lo que vuelve viable D-018.

---

### D-015 · C5 usa `pauli_feature_map(paulis=['X','ZZ'])`
**Fecha:** 2026-09-22 · **Módulo:** M5 · **Estado:** **Revertida** por D-031 (2026-10-05) · **→ Reporte:** §4.7 · *cierra Q-008; reemplaza D-002*

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

**Interpretación corregida el 2026-09-24 (H-034).** El párrafo «Qué afirma la comparación» era incorrecto. Con reps=1, el término X actúa sobre |+⟩, que es un autoestado de X, y solo añade una fase global, así que C5 prepara exactamente el estado de un mapa solo ZZ. C4 contra C5 compara **tener o no un término de primer orden** con el mismo acoplamiento ZZ, no el eje Z frente al eje X. La fidelidad media de 0.071 frente a ZZ se explica por eso: es exactamente Π cos²(xᵢ), con esperanza (1/2)^k. Los cálculos de C5 hechos con este conjunto siguen siendo válidos; lo que cambia es qué afirman. Q-012 decide si se mantiene.

**Revertida el 2026-10-05 (D-031):** C5 pasa a `['Y','ZZ']`, cuyo término de primer orden sí actúa sobre |+⟩.

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

**Coste.** A k=12, unos 41 min por matriz y 2.75 h las cuatro (dos feature maps × dos subconjuntos). Fuente: `Code/results/B1_benchmark_kernel_proyeccion.csv`.

---

### D-018 · Validación cruzada 5-fold estratificada
**Fecha:** 2026-09-22 · **Módulo:** M6 · **Estado:** Firme · **→ Reporte:** §4.8, §4.9 · *cierra Q-005*

**Contexto.** La validación cruzada figura en el cronograma del reporte y en el acta de los directores, pero no existía en la metodología (§4.9). Bajo Arquitectura A no era costeable.

**Decisión.** Validación cruzada **5-fold estratificada por clase** sobre el conjunto de entrenamiento. El conjunto de prueba oficial del CBIS-DDSM **no se toca**: sigue siendo la evaluación final, sin reordenar (RNF-03).

**Por qué.** D-014 vuelve el entrenamiento un problema clásico de segundos sobre una matriz en caché, así que el único coste real es escribir el código. Cumple un compromiso explícito ante el jurado y aporta barras de error en las métricas, que hoy se reportarían como valores puntuales.

**Consecuencias.** Estratificar por clase, no por paciente: la unidad de análisis es la lesión (D-011). **Verificar que ningún paciente quede repartido entre folds**, ya que hay 2.28 ROIs por paciente (H-008); si se detecta, pasar a `StratifiedGroupKFold` agrupando por `patient_id`. Hay que añadir la validación cruzada a §4.9, que hoy no la menciona.

**Regla aplicada el 2026-09-23 (H-027).** `StratifiedKFold` repartía entre folds el 59 % de los pacientes de masas y el 74 % de los de calcificaciones, así que M4 usa `StratifiedGroupKFold` por `patient_id`. Los folds quedan congelados en `Data/processed/m4/x_<finding_type>.parquet`, columna `fold`.

---

### D-019 · Las líneas de trabajo futuro se atribuyen a Azevedo et al. (2022)
**Fecha:** 2026-09-23 · **Módulo:** reporte · **Estado:** Firme · **→ Reporte:** §1.3, §2.1.5 · *cierra Q-004*

**Contexto.** El reporte atribuye a Azevedo et al. (2022) las dos líneas de trabajo futuro sobre las que se construye el proyecto (§1.3 y §2.1.5). El contexto del proyecto decía Incudini et al. (2022), que es otro paper.

**Alternativas.** Azevedo et al. (2022), que es lo que dice el reporte, o Incudini et al. (2022), que era lo que decía el contexto del proyecto.

**Decisión.** La atribución correcta es **Azevedo et al. (2022)**. El texto de §1.3 y §2.1.5 se mantiene.

**Por qué.** Lo resolvió el autor. El reporte ya era internamente consistente con esta atribución, de modo que no hay que cambiar el texto.

**Consecuencias.** La mención a Incudini et al. se retira del contexto del proyecto. Sigue pendiente un defecto de H-009: `Azevedo2022QuantumTransfer` se discute por nombre sin `\cite`, así que al corregir el reporte hay que añadir la cita en ambos puntos.

---

### D-020 · Alinear cada máscara según su tipo de desajuste
**Fecha:** 2026-09-23 · **Módulo:** M2 · **Estado:** Provisional (propuesta implementada en `2_Preprocessing.ipynb`, pendiente de validación del autor) · **→ Reporte:** §4.4, §8.x

**Contexto.** H-004 encontró 80 máscaras con dimensiones distintas a las de su mamografía y proponía remuestrearlas todas por vecino más cercano. H-020 muestra que son dos problemas distintos.

**Alternativas.**
- *Remuestrear las 80* (lo que decía H-004) — descartada: desplaza hasta 37 px los bordes de las dos máscaras de `P_00353`, cuyo desajuste no es de escala.
- *Descartar las 80* — descartada: pierde 78 masas, el 4.6 % del subconjunto.
- *Regla por tipo* — **elegida**.

**Decisión.**
- `scaled` (78 masas; la máscara mide 0.870 veces la imagen en ambos ejes): remuestreo al tamaño de la imagen con `cv2.INTER_NEAREST_EXACT`. Es vecino más cercano sin el desfase de medio píxel que tiene `INTER_NEAREST` en OpenCV.
- `offset` (2 calcificaciones de `P_00353`; diferencia de pocas decenas de píxeles y no proporcional): sin escalar, anclada en la esquina superior izquierda y recortada o rellenada al tamaño de la imagen.

**Por qué.** Cada regla se verificó con un criterio independiente (H-020): la de `offset` reproduce al píxel el recorte oficial del CBIS-DDSM, y la de `scaled` gana la prueba de contraste frente a la alternativa en 77 de 78 casos.

**Consecuencias.** Ningún caso se descarta. La columna `mismatch` del índice de M2 registra el tipo de cada caso. El borrador de §4.4 habla de «remuestrear las 80» y hay que corregirlo.

---

### D-021 · Reducir cada máscara a su componente conexa mayor
**Fecha:** 2026-09-23 · **Módulo:** M2 · **Estado:** Provisional (propuesta implementada, pendiente de validación del autor) · **→ Reporte:** §4.4, §8.x

**Contexto.** Cada registro anota **una** lesión, pero el 86.3 % de las máscaras de masas trae islas desconectadas de pocos píxeles (H-021). PyRadiomics calcula `Perimeter` sumando el borde de todas las componentes, y `MaximumDiameter` como la mayor distancia entre dos puntos cualesquiera de la máscara.

**Alternativas.**
- *Conservar todo* — descartada: contamina precisamente las *shape features*, que H-003 señala como las más discriminativas en masas.
- *Apertura morfológica* — descartada: elimina las islas, pero también erosiona el borde real, que es donde vive la espiculación.
- *Umbral de área* — descartada: exige un corte arbitrario, y los datos muestran que no hace falta.
- *Componente conexa mayor, conectividad 8* — **elegida**.

**Por qué.** La componente mayor contiene siempre más del 99.55 % del área, y ninguna máscara tiene dos componentes de 100 px o más: no hay ambigüedad sobre cuál es la lesión.

**Evidencia.** H-021.

**Consecuencias.** Se modifican 1,464 máscaras, todas de masas; en calcificaciones la regla no cambia nada. El índice registra, para cada caso, el área eliminada y la distancia de la isla más lejana. **El efecto esperado sobre las features es pequeño**: la isla más lejana está a 14 px de su lesión, lo que acota el cambio en `MaximumDiameter`. Saberlo de antemano descarta las islas como explicación si en M3 las *shape features* se comportan de forma inesperada.

---

### D-022 · Contrato de salida de M2
**Fecha:** 2026-09-23 · **Módulo:** M2, M3 · **Estado:** Provisional (propuesta implementada, pendiente de validación del autor) · **→ Reporte:** §4.4, §8.x

**Decisión y alternativas**, parámetro por parámetro:

| Parámetro | Elegido | Alternativa descartada y motivo |
|---|---|---|
| Margen del recorte | caja de la lesión + **20 px** por lado, cortado en el borde de la imagen | Sin margen o con otro valor. 20 px es la convención de los recortes oficiales del CBIS-DDSM (H-020), y PyRadiomics solo usa los píxeles de la máscara, así que el margen no altera las features |
| Intensidades | **16 bits crudos** de la mamografía | Normalizar a [0,1] (RF-04). Con `binCount=32` (D-008) las texturas ya son invariantes a un cambio lineal de intensidad, y un min–max por imagen ataría las features de primer orden al píxel más brillante y al más oscuro de toda la mamografía, que nada tienen que ver con la lesión |
| Origen del recorte | la mamografía completa | Los recortes oficiales: están reescalados en intensidad con una ganancia de 1.00 a 5.31 por caso (H-020) |
| Formato | NRRD comprimido, espaciado (1, 1), máscara 0/1 | DICOM o PNG. NRRD lo escribe SimpleITK y lo lee PyRadiomics directamente, y el espaciado unitario declara que todo está en píxeles (H-002) |
| Variante CLAHE | `clipLimit=2.0`, `tileGridSize=(8,8)` sobre la **mamografía completa convertida a 8 bits** (min–max propio de la imagen), después recortada | CLAHE sobre el recorte: el diseño de TT1 lo aplicaba a la imagen completa, así que la variante mide el efecto de ese diseño. CLAHE sobre 16 bits: es casi la identidad (H-022). El reporte de TT1 no fijaba parámetros; se usan los valores por defecto de OpenCV |

**Salida.**
- Archivos: `Data/processed/m2/<finding_type>/<case_id>_{image,mask,clahe}.nrrd`, 2.17 GB, no versionados.
- Índice: `Data/processed/m2_index.parquet`, que es la entrada de M3.
- Auditoría versionada: `Code/results/2_preprocesamiento_qa.csv` y `2_preprocesamiento_resumen.csv`.

**Consecuencias.** Además de §4.4, quedan desactualizados en el reporte **RF-04** (normalizar a [0,1]) y **RF-06** (redimensionar a 224×224). El borrador de §4.4 no los menciona.

---

### D-023 · M3 extrae 67 features: cuatro familias sobre la imagen original
**Fecha:** 2026-09-23 · **Módulo:** M3 · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §4.5

**Contexto.** §4.5 declara cuatro familias (first-order, shape, GLCM, GLRLM) y promete «entre 100 y 300 características». En 2D y sobre la imagen original, esas cuatro familias dan 67: 18 + 9 + 24 + 16.

**Alternativas.**
- *Añadir GLSZM, GLDM y NGTDM* (~102 features) — descartada: cumple el número, pero con tres familias que §4.5 no describe.
- *Añadir filtros LoG y wavelet* (cientos de features) — descartada: las features derivadas pierden la interpretación morfológica directa, que es el motivo por el que se eligió PyRadiomics (D-006).
- *Cuatro familias, imagen original* — **elegida**.

**Configuración.** `binCount=32` (D-008), `force2D=True`, distancia 1 con las cuatro direcciones 2D promediadas, sin normalización y sin remuestreo. Se extraen las dos variantes de M2.

**Consecuencias.** En §4.5 hay que cambiar «entre 100 y 300» por **67**. Salida: `Data/processed/m3/features_<finding_type>_<raw|clahe>.parquet`. Extracción de 3,568 × 2 en 6 minutos, sin fallos, sin NaN y sin columnas constantes.

---

### D-024 · Selección por F-test con restricción de redundancia |r| ≤ 0.95
**Fecha:** 2026-09-23 · **Módulo:** M4 · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §4.6 · *responde a H-024*

**Contexto.** Tomado tal cual, el top 12 por F contiene duplicados exactos por definición y casi-copias (H-024). Con ellos, varios qubits codificarían el mismo valor.

**Alternativas.**
- *Quitar solo los duplicados por definición* — descartada: deja casi-copias con r > 0.99 (Mean, Median y RootMeanSquared) y masas seguiría sin textura.
- *Forzar diversidad de familias con una cuota* — descartada: la cuota es arbitraria y más difícil de defender que un umbral de correlación.
- *Recorrer el ranking por F y aceptar una feature solo si su |r| de Pearson con todas las ya aceptadas es ≤ 0.95, hasta tener 12* — **elegida**.

**Decisión.** Correlaciones y ranking calculados **solo en train**. Sin la restricción, el procedimiento es exactamente `SelectKBest(k=12)`, de modo que D-001 se mantiene: la selección sigue siendo por F-test, ahora con una restricción de redundancia.

**Evidencia.** H-026.

**Consecuencias.** §4.6 debe describir el filtro. El notebook recoge la sensibilidad al umbral, de 0.80 a 0.99, para defender el 0.95.

---

### D-025 · Escalado angular por cuantiles en lugar de min-max
**Fecha:** 2026-09-23 · **Módulo:** M4 · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §4.6 · *cierra Q-009; modifica el escalador de D-001*

**Contexto.** H-028: el min-max deja casi constantes los ángulos de las features de cola pesada (IQR de 0.05 rad para `Energy` y `PixelSurface` en calcificaciones), lo que penaliza a C3–C5 por el escalado y no por la codificación.

**Alternativas.**
- *Mantener min-max y declararlo* — descartada: deja qubits casi inútiles.
- *Logaritmo sobre las features de cola pesada y después min-max* — descartada: conserva las distancias en escala logarítmica, pero exige un criterio adicional para decidir qué features son de cola pesada.
- *Transformación por cuantiles a una distribución uniforme × π* — **elegida**.

**Decisión.** `QuantileTransformer(output_distribution="uniform")` ajustado en train sobre las 12 features seleccionadas; θ = π·F̂(x), donde F̂ es la función de distribución empírica de train.

**Por qué.** Es la transformación integral de probabilidad: cada feature ocupa [0, π] de manera uniforme, por sesgada que sea. Conserva el orden de las lesiones y descarta las distancias dentro de cada feature, que es el precio de ser robusta a las colas. Se aplica igual a todas las features, sin criterio adicional, y las cinco condiciones siguen recibiendo el mismo x (D-001). D-004 se mantiene, porque el rango sigue siendo [0, π].

**Evidencia.** El IQR de los ángulos en train pasa de un mínimo de 0.14 rad (masas) y 0.05 rad (calcificaciones) a π/2 en las 24 features. Test fuera del rango de train: como mucho un 0.6 % en una feature.

**Consecuencias.** El escalador de D-001 cambia. §4.6 debe describir la transformación por cuantiles en lugar del `MinMaxScaler`. El JSON de M4 guarda los cuantiles para reaplicar o invertir la transformación.

---

### D-026 · Semilla de los folds elegida por balance de clases
**Fecha:** 2026-09-23 · **Módulo:** M4, M6 · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §4.9 · *cierra Q-010*

**Contexto.** H-027: agrupar por paciente es obligatorio (D-018), pero con la semilla 42 el fold 2 de calcificaciones quedaba con un 52 % de malignas frente al 35 % global. Era la peor de 200 semillas.

**Alternativas.** Mantener la semilla 42 y declararlo, o elegir la semilla de los folds con un criterio que solo mire las etiquetas (**elegida**).

**Decisión.** Entre las semillas 0 a 199 de `StratifiedGroupKFold` se elige, para cada subconjunto, la que minimiza la desviación máxima de la proporción de malignas entre folds; los empates van a la menor. Resultan 125 para masas y 168 para calcificaciones. La semilla 42 del proyecto se mantiene para todo lo demás (RNF-01).

**Por qué.** El criterio no usa features ni rendimiento, así que no puede ajustar el resultado. Un fold con un 52 % de malignas inflaría la varianza entre folds, que es precisamente lo que la validación cruzada debe estimar.

**Consecuencias.** Desviación máxima de 0.011 en masas y 0.019 en calcificaciones. Las semillas quedan en el JSON de M4 y en `Code/results/4_semilla_folds.csv`. §4.9 debe declarar el criterio.

---

### D-027 · γ del RBF por heurística de la mediana
**Fecha:** 2026-09-24 · **Módulo:** M5, M7 · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §4.7, §4.9

**Contexto.** C3 (Kernel PCA con núcleo RBF) y el kernel clásico K_C de la *geometric difference* (D-017) necesitan un ancho de banda, K(x, x') = exp(−γ‖x − x'‖²).

**Alternativas.** γ = 1/k, el valor por defecto de `KernelPCA` (≈ 0.083): simple, pero arbitrario respecto a la escala de los datos. O la **heurística de la mediana** (**elegida**).

**Decisión.** γ = 1 / (2 · mediana de ‖x − x'‖² sobre los pares del train), calculado por subconjunto sobre el mismo x ∈ [0, π]¹² que recibe el circuito. Con x uniforme en [0, π]¹² sale del orden de 0.026, con valores de kernel típicos cercanos a 0.6.

**Por qué.** Es un criterio estándar que no mira las etiquetas y se adapta a la escala de los datos. Usar el mismo γ en C3 y en K_C hace que la *geometric difference* compare el kernel cuántico con el mismo kernel clásico que define el comparador C3.

**Consecuencias.** El γ de cada subconjunto se reporta junto a los resultados.

---

### D-028 · Separabilidad sobre 200 lesiones de train por subconjunto
**Fecha:** 2026-09-24 · **Módulo:** M5, M7 · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §4.9

**Contexto.** RNF-06 limita los kernels de fidelidad a 150–200 casos por subconjunto por su coste O(N²): unos 41 min por matriz a k=12.

**Alternativas.** 150 de train (más barato y más ruidoso), 200 de test (usa el test fuera de la evaluación final) o **200 de train** (**elegida**).

**Decisión.** 200 lesiones por subconjunto, estratificadas por clase, tomadas del train con semilla 42. Las métricas basadas en kernel (KTA, *geometric difference*) y las basadas en el embedding (Davies-Bouldin, Fisher, t-SNE) se calculan sobre esa misma submuestra, para que las cinco condiciones y las dos familias de métricas sean comparables. Davies-Bouldin y Fisher son baratas y pueden repetirse sobre todo el train como análisis de robustez.

**Por qué.** El test queda reservado para la clasificación de M6 (RNF-03).

**Consecuencias.** Coste de los kernels: 4 matrices, unas 2.75 h en total. La lista de lesiones de la submuestra se guarda para que sea reproducible.

---

### D-029 · Kernel concentrado: diseño preregistrado más barrido del factor de escala
**Fecha:** 2026-09-24 · **Módulo:** M5, M7 · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §4.9, §6.x, OE-6 · *cierra Q-011*

**Contexto.** H-031: con el diseño actual, el kernel de fidelidad es casi la identidad (mediana ~0.003 fuera de la diagonal), y escalar los ángulos solo lo corrige cuando desaparecen los productos xᵢxⱼ.

**Alternativas.**
- *Adoptar un c pequeño como diseño principal* — descartada: con c ≈ 0.02 el kernel es indistinguible del de un mapa sin el término de producto (correlación 1.0000, H-031), y elegir el diseño después de ver los datos añade grados de libertad al investigador.
- *Cambiar la codificación* (entrelazamiento lineal o productos sin el desplazamiento de π) — descartada: redefine C4 y C5 tarde en el proyecto y obliga a revalidar D-015.
- *Mantener el diseño preregistrado (c = 1) como análisis principal y añadir un barrido de c* — **elegida**.

**Decisión.** C4 y C5 se calculan con el diseño tal como está: k = 12, reps = 1, entrelazamiento completo y ángulos en [0, π]. Como análisis de sensibilidad del OE-6, el kernel de fidelidad se recalcula con los ángulos escalados, x → c·x, para c ∈ {1, 0.5, 0.2, 0.1, 0.05, 0.02}.

**Por qué.** La concentración es en sí misma un resultado de viabilidad. El barrido cuantifica que un kernel informativo exige una escala en la que el término de producto xᵢxⱼ, la interacción entre features que la codificación ZZ debía aportar, ya no influye (H-031). Con `FidelityStatevectorKernel` (H-032), cada matriz del barrido cuesta segundos.

**Consecuencias.** La KTA y la *geometric difference* del análisis principal deben interpretarse junto a la concentración y al barrido, no solas. Si hay holgura, los embeddings ⟨Zᵢ⟩ del barrido pueden calcularse para algunos valores de c.

---

### D-030 · La separabilidad pasa a ser el Módulo 6
**Fecha:** 2026-09-24 · **Módulo:** todos · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §4.1–§4.9, tabla de requisitos, tabla CRISP-DM

**Contexto.** El diagrama del §4.1 dibuja el análisis de separabilidad como una caja **sin número** entre M5 y M6, con una flecha hacia M6. El texto, en cambio (§4.9 y la tabla CRISP-DM), lo coloca dentro del M7, «Evaluación comparativa». Además, esa flecha sugiere que la clasificación usa los resultados de separabilidad, y no es así: las dos consumen la salida de M5 en paralelo.

**Alternativas.**
- *(A)* Mantener la separabilidad dentro del M7 y corregir solo el diagrama — descartada por el autor.
- *(B)* Darle su propio módulo — **elegida**.

**Decisión.**

| Módulo | Nuevo contenido | Antes |
|---|---|---|
| M6 | **Análisis de separabilidad** (OE-3): KTA, *geometric difference*, Davies-Bouldin, Fisher, t-SNE | parte del M7 |
| M7 | **Clasificación** (MLP, validación cruzada, test) | M6 |
| M8 | **Evaluación comparativa**: métricas de clasificación, correlación de Spearman, masas frente a calcificaciones, OE-6 | M7 |

El flujo es un grafo con ramas paralelas: M5 → {M6, M7} → M8. Los notebooks siguen el número del módulo: `6_Separability`, `7_Classification`, `8_Comparison`.

**Por qué.** La separabilidad es la pregunta de investigación (OE-3). Con su propio módulo, el número de los notebooks coincide con el orden de ejecución y con el diagrama.

**Consecuencias.**
- En el reporte, que redacta el autor, hay que:
  - rehacer el diagrama del §4.1 y su pie (el borrador tiene una propuesta en TikZ);
  - renumerar las secciones de módulos, con una nueva sección para M6;
  - reagrupar la tabla de requisitos: RF-15 a RF-17 van a M6 y los de clasificación a M7;
  - rehacer la tabla CRISP-DM y cualquier mención de «M6» o «M7» en el texto.
- **En las entradas de esta bitácora anteriores al 2026-09-24, «M6» significa clasificación y «M7» evaluación**; desde D-030 rige la numeración nueva. Por ejemplo, la *geometric difference* de D-017 pertenece ahora al M6.

---

### D-031 · C5 pasa a `pauli_feature_map(paulis=['Y','ZZ'])`
**Fecha:** 2026-10-05 · **Módulo:** M5 · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §4.7, §6.x · *cierra Q-012; revierte D-015*

**Contexto.** H-034: con reps=1, el término X de `['X','ZZ']` actúa sobre |+⟩, autoestado de X, y solo añade una fase global. C5 era un mapa solo ZZ, y C4 frente a C5 no comparaba el eje de la codificación de primer orden, como afirmaba D-015.

**Alternativas.**
- *(a) Mantener C5 como ablación del término de primer orden* — descartada por el autor. No obligaba a recalcular nada, pero la condición dejaba de medir lo que D-015 prometía.
- *(b) Cambiar a un conjunto cuyo término de primer orden actúe sobre |+⟩* — **elegida**, con `['Y','ZZ']`.

**Decisión.** C5 = `pauli_feature_map(12, reps=1, paulis=['Y','ZZ'])`. El resto del diseño no cambia: reps=1, el mismo ansatz con el mismo θ (semilla 42), el mismo barrido de c (D-029) y la misma submuestra (D-028).

**Por qué.**
- Tras la capa de Hadamard, cada qubit está en |+⟩, sobre el ecuador de la esfera de Bloch. Un giro en Z lo mueve a lo largo del ecuador, un giro en Y lo saca del ecuador hacia los polos y un giro en X no lo mueve. Con Y, C4 frente a C5 vuelve a comparar el eje de la codificación de primer orden con el mismo acoplamiento ZZ, que era la intención de D-015.
- Qiskit lo implementa como √X · P(2xᵢ) · √X†, que equivale a RY(2xᵢ) salvo una fase global. Se verificó en 5a: fidelidad 1 en 20 lesiones reales.
- Coste: 12 √X y 12 √X† más, sin CX adicionales; profundidad 67 contra 65.
- La motivación es estructural, no un resultado. H-034 la planteó el 24 sep, antes de medir la separabilidad, y el M6 todavía no se ha calculado.

**Evidencia.** Celda de inspección de `Code/5a_Embeddings.ipynb`, sobre 5 masas reales. La fidelidad con el estado de un mapa solo ZZ es 1.000 con `['X','ZZ']` y como mucho 3×10⁻⁵ con `['Y','ZZ']`. Sin el ansatz, ⟨Zᵢ⟩ de C5 vale exactamente −sin(2xᵢ), con diferencia de 5×10⁻¹⁵.

**Consecuencias.**
- Se recalcularon C5 en 5a y 5b y el experimento X2. C1–C4, K_C y todas las matrices de C4 salieron idénticos bit a bit.
- El C5 nuevo cambia mucho la concentración, y en direcciones opuestas según el objeto (H-037).
- H-036 se actualizó con las cifras nuevas.
- El borrador de §4.7 y el pie del diagrama del §4.1 deben describir C5 como «codificación de primer orden en Y con acoplamiento ZZ». RF-14 sigue desactualizado.
- 5a dibuja ahora los dos circuitos completos: `Docs/Figures/M5_circuit_k4.png` (k = 4, legible) y `M5_circuit_12q.png` (C4 a tamaño real).

---

### D-032 · La *geometric difference* sigue el protocolo de Huang et al. (Apéndice L.3)
**Fecha:** 2026-10-06 · **Módulo:** M6 · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §3.4.2, §4.9, RF-16 · *precisa D-017; enmienda D-027 en lo que toca a g*

**Contexto.** D-017 y D-027 suponían un solo kernel clásico, el RBF con γ por la mediana. H-038 muestra que la *g* de Huang et al. es regularizada y que es el mínimo sobre una batería de kernels clásicos.

**Alternativas.**
- *Un solo K_C (D-027), sin regularizar* — descartada: da entre 306 y 388 a c = 1, un artefacto del condicionamiento de K_C.
- *Un solo K_C (D-027), regularizado* — descartada: ningún λ de la malla cumple g_tra < 0.045 para c ≥ 0.05, así que con el criterio del paper no hay valor que reportar.
- *El protocolo del Apéndice L.3* — **elegida**.

**Decisión.**
- g_gen (F19) con la condición g_tra < 0.045 (L9) y las mallas de λ (L10) y de kernels clásicos (L11) sin cambios. Para cada kernel se toma el mayor λ admisible, y se reporta el mínimo sobre la batería.
- Var[x] es la varianza de todas las coordenadas de las 200 lesiones. El kernel lineal se calcula sobre ángulos centrados, porque Huang et al. centraron sus datos.
- Como sensibilidad, gaussianos más estrechos (m = 128, 256 y 512), porque el mínimo cae en el borde de la malla.
- Se reportan además la fila del RBF de D-027, con su valor sin regularizar, y la referencia K_Q = I, que es el valor de un kernel que solo memoriza.
- Se calcula a c = 1, el análisis principal, y en todo el barrido de D-029.

**Por qué.** Es la definición operativa de la fuente; cualquier otra elección sería una métrica distinta con el mismo nombre. Las mallas del paper se usan sin cambios para no añadir grados de libertad elegidos con los datos a la vista.

**Consecuencias.** La *g* deja de depender de un solo γ. El γ de D-027 sigue definiendo C3.

---

### D-033 · Definiciones de las demás métricas del M6
**Fecha:** 2026-10-06 · **Módulo:** M6 · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §4.9

**Decisión.**
- **KTA centrada** (Cortes, Mohri y Rostamizadeh, 2012, *JMLR* 13:795–828) como principal, y **sin centrar** (Cristianini, Shawe-Taylor, Elisseeff y Kandola, *NIPS 14*, 2001) como complemento. Las dos referencias se verificaron. Entre kernels se compara el **exceso sobre la media de la permutación** (H-038).
- **Dimensión efectiva** de la ecuación (F12) con 1/(N−k+1), declarando la errata (H-038).
- **Fisher:** J = Δμᵀ S_W⁻¹ Δμ, la distancia de Mahalanobis al cuadrado entre las medias de clase, con la covarianza intraclase combinada.
- **Davies-Bouldin** con las clases como clusters (`sklearn`), y **KTA lineal** centrada de cada embedding.
- **Pruebas de permutación** unilaterales con 1,000 barajadas que conservan el número de lesiones por clase, las mismas para todas las métricas de un subconjunto.
- **t-SNE** (perplejidad 30, inicialización PCA, semilla 42), solo como visualización.

**Por qué.**
- La KTA sin centrar premia el desbalance: con etiquetas barajadas, su media para el RBF de calcificaciones es 0.087.
- La versión de Fisher por feature no es invariante ante rotaciones, y D-016 exige que C1 y C2 coincidan. La multivariante es invariante ante cualquier transformación afín invertible.
- Las permutaciones dan la referencia de azar sin suponer independencia entre pares.

**Evidencia.** Pasan las 20 verificaciones de `6_Separability` (2°c y 5°). Entre ellas, C1 y C2 coinciden con una diferencia de 3×10⁻¹⁴ o menos en todas las métricas.

---

### D-034 · Se reproduce la Fig. 2 de Huang et al. (2021) en el reporte
**Fecha:** 2026-10-06 · **Módulo:** reporte · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §3.4.2

**Decisión.** La figura se toma de la versión publicada y sin cambios: `Docs/Figures/Huang2021_Fig2.png`, de 1359 × 1076 px, descargada de Springer Nature. Pie sugerido: «Reproducida de Huang et al. (2021), *Nat. Commun.* 12, 2631, bajo licencia CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)».

**Por qué.**
- La licencia CC BY 4.0 de la versión publicada, verificada en Europe PMC (PMC8113501), permite reproducirla dando crédito, enlazando la licencia e indicando los cambios. La licencia de la copia de arXiv no se verificó.
- Se deja en inglés para no convertirla en una adaptación. Si se traduce, el pie debe decir «Adaptada de».

**Consecuencias.** Hay que añadir la referencia publicada a la bibliografía. Ubicación propuesta: §3.4.2, junto a la ecuación corregida de *g* (H-033).

---

### D-035 · Se compara contra k = 8 antes de concluir el OE-3, como experimento X3
**Fecha:** 2026-10-06 · **Módulo:** M4–M6 · **Estado:** Firme (elegida por el autor) · **→ Reporte:** §6.x, §7, OE-6 · *cierra Q-013*

**Contexto.** H-018 dejó la regla de comparar contra k = 8 si la separabilidad a k = 12 salía pobre, y salió pobre (H-039, H-040).

**Alternativas.** *(b)* No hacerlo y declararlo como limitación — descartada por el autor. *(a)* Hacer la comparación — **elegida**.

**Decisión.** Se repiten M4, M5 y M6 con k = 8 en `Code/experiments/X3_Fewer_Qubits_k8.ipynb`, cambiando solo el número de qubits.
- M4 con la regla de D-024 y D-025.
- M5 con las cinco condiciones, reps = 1, el mismo ansatz y θ de la semilla 42.
- M6 sobre las mismas 200 lesiones, con el mismo barrido de c y las mismas funciones, copiadas sin cambios de `6_Separability`.
- Los valores de k = 12 se recalculan con el mismo código como prueba de regresión.

Es un análisis de robustez: k = 12 sigue siendo el punto de operación (D-013).

**Por qué.** Era un compromiso previo. Sin la comparación, el resultado del M6 podía atribuirse al tamaño del registro y no a la codificación.

**Consecuencias.** Los datos de k = 8 quedan en `Data/processed/x3/` para todas las lesiones, por si el autor quiere repetir el M7 con k = 8. El resultado está en H-041.

---

### D-036 · Protocolo de clasificación del M7
**Fecha:** 2026-10-06 · **Módulo:** M7 · **Estado:** **Provisional**: fijada al implementar; la valida el autor · **→ Reporte:** §4.8, §6.x · *precisa RF-18, RF-19, D-018 y D-014*

**Contexto.** El reporte fija un MLP con al menos dos capas ocultas, BCE ponderada con w_c = N/(C·N_c), Adam, la misma semilla en todas las condiciones y las métricas sobre el test oficial. No fija los hiperparámetros.

**Decisión.**
- **Red:** k → 32 → 16 → 1, con ReLU y salida sigmoide. La sigmoide se integra en `BCEWithLogitsLoss`: es la misma función, calculada de forma numéricamente estable.
- **Entrenamiento:** BCE ponderada con los pesos calculados sobre los datos que se ajustan; Adam con lr 10⁻³, *weight decay* 10⁻⁴ y lotes de 128.
- **Estandarización** ajustada sobre la parte de entrenamiento de cada ajuste.
- **Parada temprana** con paciencia 40 sobre la pérdida ponderada del 15 % de los pacientes del entrenamiento, con un máximo de 400 épocas y restaurando los mejores pesos.
- **Umbral 0.5** para F1, *accuracy*, *precision* y *recall*. El AUC-ROC es la métrica principal.
- **Semilla 42** para los pesos, el orden de los lotes y la partición de parada.
- **Evaluación:** validación cruzada con los folds congelados de M4 y un único ajuste sobre todo el train, evaluado una vez en el test.
- **Incertidumbre:** bootstrap de 2,000 remuestreos **por paciente**, pareado entre condiciones.

**Por qué.**
- **La estandarización es necesaria para una comparación justa.** Las representaciones difieren en escala dos órdenes de magnitud: ángulos en [0, π] frente a ⟨Zᵢ⟩ con dispersión de 0.05. Sin ella, el optimizador favorecería las de escala grande por una razón ajena a su información. Es una transformación afín invertible, aplicada igual a todas las condiciones.
- **La parada temprana usa una partición por paciente** que no toca el fold de validación ni el test.
- **Los hiperparámetros se fijaron de antemano**, sin ajustarlos a ninguna condición. Ajustarlos por condición rompería el principio de «mismo clasificador»; ajustarlos sobre una condición sesgaría a favor de ella.

**Evidencia.** El MLP sobre C1 reproduce la regresión logística de X1 con las mismas 12 features (H-035): 0.652 contra 0.650 en masas y 0.742 contra 0.758 en calcificaciones. Pasan las 16 verificaciones de `7_Classification`, entre ellas que reentrenar con la misma semilla reproduce las predicciones bit a bit.

**Consecuencias.** D-037 comprueba que la conclusión no depende de estas elecciones.

---

### D-037 · Análisis de sensibilidad del M7
**Fecha:** 2026-10-06 · **Módulo:** M7 · **Estado:** Firme (reps = 2 y k = 8 elegidos por el autor) · **→ Reporte:** §6.x, §7

**Decisión.** Además del análisis principal (k = 12, reps = 1), se corren seis análisis de sensibilidad.
- **reps = 2 en el *ansatz*** para C4 y C5, con `real_amplitudes(12, reps=2)` y 36 parámetros de la semilla 42, cuyos primeros 24 son los de reps = 1. El *feature map* sigue con una repetición, como en H-018, así que el kernel del M6 no cambia (D-017). Validación cruzada y test.
- **k = 8** con los embeddings de X3 (D-035). Validación cruzada y test.
- **Cuatro semillas más** (43 a 46), solo en validación cruzada.
- **Cuatro configuraciones alternativas**, solo en validación cruzada: red 16-8, red 64-32, entradas sin estandarizar, y 200 épocas sin parada temprana.

**Por qué.**
- reps = 2 y k = 8 eran compromisos de H-018.
- Las semillas dan el tamaño del ruido del procedimiento de entrenamiento.
- Las configuraciones responden a la objeción de que la conclusión depende de la red, del escalado o de que algunos ajustes cuánticos paran en pocas épocas.

**Consecuencias.** Los embeddings de reps = 2 quedan en `Data/processed/m7/`, y las predicciones de todos los modelos en `Data/processed/m7/predicciones.parquet`, para el M8.

---

### D-038 · Análisis exploratorios X4 a X6, con un protocolo simétrico
**Fecha:** 2026-10-07 · **Módulo:** X4–X6 · **Estado:** Firme (pedidos por el autor) · **→ Reporte:** §6.x, §7

**Contexto.** El diseño preregistrado no mostró ventaja (H-039 a H-043). El autor pidió tres cosas: probar un modelo de QML sobre la codificación (X4), revisar si algún error podía esconder una ventaja (X5) y buscar activamente una ventaja con las herramientas de la literatura (X6).

**Decisión.** Los tres son exploratorios y *post hoc*, y no cambian el diseño. Para que la búsqueda no fabrique una ventaja por azar:
- **El mismo clasificador para todo kernel:** un SVM con pesos balanceados y C = 1. Se comprobó que C apenas influye.
- **La misma búsqueda de hiperparámetros para lo clásico y lo cuántico**, por validación cruzada anidada con los folds de M4.
- **Dos contendientes globales** (todo lo clásico frente a todo lo cuántico), elegidos con la misma regla.
- **El test se usa una vez por contendiente**, con bootstrap por paciente.
- **Todo se reporta**, incluidos los intentos que no funcionan.

**Por qué.** Probar muchas variantes cuánticas contra una sola clásica produciría una «ventaja» por selección. La simetría del protocolo es lo que permite interpretar el resultado en cualquier dirección.

---

### D-039 · El Spearman del M8 se reporta como descriptivo
**Fecha:** 2026-10-07 · **Módulo:** M8 · **Estado:** Firme (opción elegida por el autor) · **→ Reporte:** §3.4 (ec. `spearman`), §4.10, §6.x · *precisa RF-21*

**Contexto.**
- RF-21 pide correlacionar el ranking de separabilidad con el de clasificación de las cinco condiciones.
- Con n = 5, la distribución nula exacta de ρ_s se obtiene de los 5! = 120 órdenes, todos igual de probables. Sin empates, solo el acuerdo perfecto baja de p = 0.05 bilateral: p = 2/120 ≈ 0.017. Basta un intercambio entre vecinos para tener ρ = 0.9 y p ≈ 0.083.
- Además, toda métrica de separabilidad empata a C1 y C2 por construcción (D-016).

**Opciones.**
1. Reportar ρ_s de forma descriptiva, por subconjunto, con su distribución exacta.
2. Juntar masas y calcificaciones para tener n = 10. Choca con D-005.
3. Usar los análisis de sensibilidad (reps = 2, k = 8) como puntos extra. No son independientes del principal.

**Decisión.** Opción 1.
- **Cálculo.** ρ_s es la correlación de Pearson de los rangos promedio. Es la definición general; la fórmula del reporte, 1 − 6Σd²/(n(n²−1)), es su caso sin empates y no vale con el empate C1 = C2.
- **Empates numéricos.** Los valores que difieren solo por ruido de punto flotante cuentan como empate: es el caso de C1 y C2, que difieren en 10⁻¹⁴.
- **Valores primarios.** Las tres métricas de embedding (D-033) sobre la submuestra de 200 (D-028), contra el AUC del test, con k = 12. Son las métricas de la misma familia de vectores que recibe el MLP (H-013).
- **Sensibilidad.** Todo el train, el AUC de validación cruzada y k = 8.
- **Lectura por bloques.** Se reporta si cada ranking pone a las tres condiciones clásicas por encima de las dos cuánticas.
- **Familia de kernels.** Solo hay tres kernels, así que solo se compara su orden con el del SVM del X4. Con n = 3, el p mínimo es 1/3.

**Por qué.**
- Con n = 5 y el empate, la prueba solo puede rechazar con un único orden.
- Se calculan 48 valores de ρ sobre las mismas cinco condiciones, así que no son evidencia independiente.

---

### D-040 · Contenido del M8: el OE-6 medido y una referencia con los descriptores del radiólogo
**Fecha:** 2026-10-07 · **Módulo:** M8 · **Estado:** **Provisional**: propuesta al implementar; la valida el autor · **→ Reporte:** §4.10, §6.x, §7, OE-6 · *precisa RF-22*

**Contexto.**
- RF-22 pide documentar cuatro cosas: el tiempo por muestra, el máximo de qubits, el impacto de los shots y el coste del *parameter-shift*.
- B1 midió el tiempo y el *parameter-shift* hasta k = 16, y B3 la estabilidad de ⟨Zᵢ⟩ con muestreo real (H-019).
- Faltaban tres cosas:
  - el techo de qubits en esta máquina;
  - el efecto de los shots sobre lo que se usa después, el clasificador y el kernel;
  - una explicación de por qué el EDA esperaba que las masas fueran el subconjunto fácil, cuando el M7 encontró lo contrario.

**Decisión.**
- **Qubits.**
  - Se cronometra un estado del circuito de C4 (*feature map* y *ansatz*) con `AerSimulator` en modo statevector, para k par de 8 a 28. El circuito solo devuelve los k valores ⟨Zᵢ⟩, para no duplicar la memoria al devolver el estado.
  - Se proyectan cuatro tareas como cotas inferiores, sin la sobrecarga de las primitivas: el embedding, el kernel por *compute-uncompute*, el kernel con el atajo del vector de estado y el entrenamiento de θ.
  - Una tarea es viable si su memoria cabe en la mitad de la RAM y termina en 24 h.
- **Shots en el embedding.**
  - Para cada lesión se sortean n cadenas de bits a partir de las probabilidades exactas, con un sorteo multinomial. Es la estadística de un *sampler* ideal.
  - Con esas cadenas se reconstruyen los ⟨Zᵢ⟩ y se reentrena el MLP del M7 (D-036), solo en validación cruzada.
  - n ∈ {64, 256, 1,024, 4,096, 16,384, 65,536}, con tres sorteos por nivel.
- **Shots en el kernel.** No se simula nada. En hardware, el valor del kernel es la probabilidad de leer la cadena de ceros, así que su estimación es binomial y su coste se calcula de forma analítica sobre los kernels exactos del M5.
- **Descriptores del radiólogo.**
  - Regresión logística con los folds de M4 sobre los descriptores categóricos del CBIS-DDSM: forma y márgenes en masas, tipo y distribución en calcificaciones.
  - Es una referencia, no un competidor: los escribió un radiólogo viendo la imagen.
  - Se excluyen `assessment` (BI-RADS, que ya es un juicio de malignidad) y `subtlety`.
- **El test no se vuelve a usar.** Los números de test del M8 son los del M7, el X4 y el X6.

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

**Corregido el 2026-09-23 (H-023).** Sobre las 1,318 masas de entrenamiento, el mayor |d| es **0.50** y las shape features quedan entre 0.40 y 0.45. El 1.42 de esta entrada era un artefacto de la muestra de 20. Tampoco se cumple que la selección vaya a ser «casi puro `shape2D`»: el top 12 tiene 7 features de primer orden y 5 de forma (H-024).

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

**Actualizado el 2026-09-23 (H-020).** La re-auditoría sobre los 3,568 casos, incluidas las 86 mamografías recuperadas, confirma exactamente 80. Pero son **dos tipos**: 78 masas escaladas por 0.870 y 2 calcificaciones desplazadas. Remuestrear estas dos las habría desplazado; el procedimiento correcto está en D-020.

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

Evidencia concurrente: las 18 filas de `Code/results/B1_benchmark_complejidad.csv` son idénticas entre ambos *feature maps* en profundidad, CX y número de puertas; y las diferencias de tiempo entre ellos en `B1_benchmark_resultados.csv` (23.06 h contra 24.03 h a k=8) son ruido de medición, no señal.

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

**Precisión añadida el 2026-09-23 (H-019).** El valor en que se estanca la columna del estimador, ~0.016, es exactamente el `default_precision` con que se construye `EstimatorQNN`, 0.015625 = 1/√4096: cuando la precisión se fija en el estimador, el QNN la sustituye por la suya. Y ese mismo valor por defecto es el que contaminó la referencia de H-016.

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
**Fecha:** 2026-09-23 · **→ Reporte:** §8.x, OE-6 · **Estado: INVALIDADO por H-019**

> **Corrección del 2026-09-23.** El sesgo descrito aquí **no existe**. La referencia «exacta» se calculó con `EstimatorQNN` sin `default_precision=0`, de modo que llevaba ruido gaussiano de σ = 0.015625; el suelo de ~0.013 es exactamente σ·√(2/π) = 0.01247. Además, el `EstimatorV2` de Aer no muestrea, así que la pendiente de −0.5065 era circular. La explicación y la medición correcta están en H-019. El texto original se conserva como registro.

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

**Datos.** `Code/results/B3_shots_repetido.csv`, figura `Docs/Figures/E3_shots_sensitivity.png`.

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

**Corregido.** Se repitió promediando 10 sorteos de θ por configuración; el resultado está en H-018. El promediado confirma el diagnóstico: a k=8, `reps=1` y `reps=2` resultan indistinguibles (0.0854 contra 0.0849; con valores exactos, 0.0837 contra 0.0833, H-019), cuando el sorteo único indicaba un aumento del 35 %.

**Advertencia general que conviene retener.** Este es el segundo caso en el mismo día en que una medición de una sola realización produjo un número engañoso; el primero fueron las fidelidades de los conjuntos de Pauli en H-012, donde un único vector de entrada dio 0.000 para un candidato que promediando resulta ser de los más parecidos a ZZ. **Cualquier cantidad que dependa de un sorteo aleatorio —θ, el vector de entrada, la partición— debe reportarse como distribución, no como valor puntual.**

---

### H-018 · El embedding se concentra con el número de qubits, no con la profundidad
**Fecha:** 2026-09-23 · **→ Reporte:** §6.x, OE-6 · **Cifras rehechas el 2026-09-23 con valores exactos (H-019)**

> **Corrección.** La primera versión de esta entrada se midió con `EstimatorQNN` sin precisión 0, de modo que cada ⟨Zᵢ⟩ llevaba ruido gaussiano de σ = 0.015625 (H-019), y ese ruido infla la dispersión en cuadratura. La tabla de abajo es la repetición con valores exactos: mismas entradas, mismos sorteos de θ y precisión 0 como único cambio. Para comprobar el diagnóstico, se sumó a los valores exactos el ruido por defecto simulado: eso reproduce las cifras originales hasta la tercera cifra decimal. Las cifras originales se conservan en `Code/results/B3_concentracion_embedding_ruido_qnn.csv`.

Desviación estándar de ⟨Zᵢ⟩ entre 100 entradas, media ± desviación entre 10 sorteos de θ, con valores exactos:

| k | reps=1 | reps=2 | reps=3 |
|---|---|---|---|
| 8 | 0.0837 ± 0.0131 | 0.0833 ± 0.0091 | 0.0718 ± 0.0052 |
| 12 | 0.0417 ± 0.0068 | 0.0544 ± 0.0036 | 0.0305 ± 0.0044 |
| 16 | 0.0363 ± 0.0090 | 0.0367 ± 0.0043 | 0.0161 ± 0.0023 |

El ruido había inflado todas las dispersiones: un ~2 % a k=8, un 9 % a k=12 con reps=1 y un **49 % a k=16 con reps=3**, donde era el 43 % de la varianza medida. Cuanto menor la dispersión real, mayor la distorsión.

Tres lecturas, y conviene no mezclarlas. **Las tres sobreviven a la corrección:**

**1. La concentración con el número de qubits es clara.** A reps=1 la dispersión cae de 0.0837 (k=8) a 0.0417 (k=12) y 0.0363 (k=16). De 8 a 12 se reduce a la mitad, muy por encima de las barras de error; de 12 a 16 el cambio queda dentro de ellas. Es el comportamiento que anticipa el fenómeno de mesetas áridas: al crecer el espacio de Hilbert, los valores de expectativa se concentran.

**2. La concentración con la profundidad NO es monótona en el rango probado.** reps=1 y reps=2 son indistinguibles a k=8 y a k=16, y a k=12 la dispersión **aumenta un 30 %** de reps=1 a reps=2 (0.0417 ± 0.0068 contra 0.0544 ± 0.0036), con barras que no se solapan. Solo reps=3 queda consistentemente por debajo, y a k=16 reduce la dispersión a menos de la mitad.

**3. La variabilidad entre sorteos de θ sí colapsa con la profundidad.** A k=16 la desviación entre sorteos pasa de 0.0090 a 0.0043 y a 0.0023. Es decir, los circuitos más profundos producen una dispersión más uniforme **con independencia de θ**. Esa pérdida de sensibilidad a los parámetros es la firma característica de la meseta árida, y es una observación más sólida que la del punto 2. Sin el ruido se ve con más claridad que antes.

**Impacto sobre D-013. Corregido:** la primera versión afirmaba que reps=1 entrega la máxima dispersión, empatada con reps=2. **En el punto de operación, k=12, eso es falso**, y ya lo era con los datos originales (0.0456 contra 0.0573): reps=2 dispersa un 30 % más. reps=1 se sostiene por las razones propias de D-013, es decir, coste y que bajo D-014 θ no se entrena, así que capas adicionales no añaden capacidad aprendible. **No se sostiene por dispersión.** La dispersión además es solo un indicador indirecto: si se traduce en separabilidad lo mide M7. Bajo la Arquitectura B, un embedding con reps=2 a k=12 cuesta minutos, así que compararlo en M7 sería un análisis de robustez barato. **Decisión del autor.**

**Impacto sobre k.** El embedding a k=12 está notablemente más concentrado que a k=8: la mitad de dispersión, 0.042 contra 0.084. La elección de k=12 se justificó por coste y por diversidad de familias de features, no por dispersión. Si en M7 la separabilidad a k=12 resultara pobre, **k=8 merecería una comparación** antes de dar por buena la conclusión.

**Nota del 2026-10-06 (H-043).** Sobre datos reales y con el θ del diseño, reps = 2 en el *ansatz* no aumenta la dispersión de C4 (de 0.058 a 0.047 en masas); la de C5 sube de 0.180 a 0.196. El 30 % de esta entrada es un promedio sobre sorteos de θ con entradas sintéticas.

**Datos.** `Code/benchmark/B3_Sampling_and_Concentration.ipynb` §5; `Code/results/B3_concentracion_embedding.csv`, con la columna `std_media_con_ruido_simulado` como comprobación; figura `Docs/Figures/E4_embedding_concentration.png`, con la curva original punteada. Medición sobre datos sintéticos uniformes en [0,π]^k: sirve para caracterizar el circuito, pero **no sustituye** la medición sobre features radiómicas reales una vez exista M3.

---

### H-019 · El «sesgo» de H-016 era ruido en la referencia, y el estimador de Aer no muestrea
**Fecha:** 2026-09-23 · **→ Reporte:** §3.x (medición), §8.x, OE-6 · *invalida H-016; obliga a repetir H-018*

H-016 registró que el error entre Aer y el cálculo exacto se estancaba en ~0.013 hasta un millón de shots. La causa no es el simulador sino la referencia, por **dos valores por defecto de las librerías** que actúan juntos:

1. `EstimatorQNN` se construye con `default_precision=0.015625` (= 1/√4096) y lo pasa a `estimator.run()` en cada *forward*. Es la misma línea de código que explicó H-014.
2. `StatevectorEstimator`, si recibe una precisión distinta de cero, **no devuelve el valor exacto**: le suma ruido gaussiano 𝒩(0, precisión) para imitar un número finito de shots.

La referencia «exacta» de H-016, y la de la sección 5 de `benchmark/B1_Quantum_Benchmark.ipynb`, llevaba por tanto ruido de σ = 0.015625. Para un error gaussiano 𝔼|e| = σ√(2/π) = **0.01247**, que es el suelo observado.

**Evidencia.** k=12, reps=1, mismas 16 entradas y mismo θ que la corrida nocturna. «Verdad» es la evolución directa con `qiskit.quantum_info.Statevector`, sin primitivas:

| Evaluación | Comparada con | MAE | Predicción |
|---|---|---|---|
| QNN + `StatevectorEstimator`, precisión por defecto | verdad | 0.01310 | 0.01247 |
| la misma, dos llamadas idénticas | entre sí | 0.01684 | 0.01763 |
| QNN + `StatevectorEstimator`, precisión 0 | verdad | 0 | 0 |
| QNN + Aer, precisión 0 | verdad | 1.7×10⁻¹⁶ | 0 |
| QNN + Aer, 2²⁰ shots | referencia nocturna | 0.01315 | 0.01249 ← el suelo de H-016 |
| QNN + Aer, 2²⁰ shots | verdad | 0.00089 | 0.00078 |

**Segundo hallazgo: el `EstimatorV2` de Aer no simula shots.** Calcula el valor exacto con `save_expectation_value` y después ejecuta `evs = rng.normal(evs, precision)` (`qiskit_aer/primitives/estimator_v2.py`). Una medición real con n shots solo puede dar ⟨Z⟩ ∈ {−1, −1+2/n, …, 1}. Con 16 shots (precisión 0.25), los 192 valores que devuelve el estimador de Aer son todos distintos y **ninguno** cae en la malla de múltiplos de 1/8. Con el sampler, el 100 % cae en la malla y solo aparecen 11 valores distintos. Por eso la pendiente de −0.5065 de H-016 era circular: el ruido inyectado tiene σ = precisión = 1/√shots por definición, y la medición confirmaba el modelo, no la estadística.

**Medición correcta**, con muestreo real: `SamplerV2` de Aer y ⟨Zᵢ⟩ = P(bitᵢ=0) − P(bitᵢ=1) sobre las cadenas de bits, 10 repeticiones por punto. La teoría sale del postulado de medida, con Var(Ẑᵢ) = (1 − ⟨Zᵢ⟩²)/n:

| shots | dispersión entre repeticiones | teoría | MAE vs exacto | teoría |
|---|---|---|---|---|
| 512 | 0.04261 | 0.04416 | 0.03489 | 0.03524 |
| 8,192 | 0.01085 | 0.01104 | 0.00890 | 0.00881 |
| 65,536 | 0.00379 | 0.00390 | 0.00312 | 0.00311 |
| 1,048,576 | 0.00095 | 0.00098 | 0.00077 | 0.00078 |

Pendientes log-log: dispersión **−0.4986**, MAE **−0.4983**, sesgo de la media de las 10 repeticiones −0.5015. **No hay suelo** en todo el rango, y la media converge al valor exacto.

**Impacto.**

1. **H-016 queda invalidado** y la figura E3 se rehízo. La observación correcta para el OE-6 es la contraria: con muestreo real, el simulador reproduce la estadística de la medición cuántica sin sesgo hasta 2²⁰ shots.
2. **H-018 estaba contaminado** por el mismo ruido, porque la medición de dispersión también usaba `EstimatorQNN` sin precisión 0. Se repitió; ver la corrección en H-018.
3. **Regla para M5:** «exacto» significa `Statevector` directo o una primitiva llamada con precisión 0 explícita. La Arquitectura B no necesita gradientes, así que no necesita `EstimatorQNN`. Si se usa en algún punto, siempre con `default_precision=0.0`. Sin esto, cada ⟨Zᵢ⟩ del embedding llevaría ruido de σ = 0.0156 frente a una dispersión real de ~0.04–0.06 a k=12, y C4/C5 quedarían penalizadas artificialmente.
4. **Formalismo contra implementación.** La ley 1/√n, con varianza (1 − ⟨Z⟩²)/n, es una propiedad de la medición cuántica y va en el marco teórico. Que Aer la modele como ruido gaussiano aditivo y que `EstimatorQNN` inyecte 0.015625 por defecto, incluso sobre un estimador que se llama *statevector*, son detalles de implementación y van en §8.x.
5. `B1_benchmark_shots.csv` (pendiente −0.357) queda invalidado por el mismo motivo. Se conserva como registro, con una nota en el notebook B1.

**Advertencia que se suma a la de H-017.** Es el tercer número engañoso en dos días, y en los tres la causa fue un supuesto no verificado: una sola realización (H-012, H-017) y ahora una referencia «exacta» que no lo era. Antes de comparar contra una referencia, hay que comprobar que la referencia se compara bien consigo misma: dos llamadas idénticas deberían dar exactamente el mismo resultado.

**Datos.** `Code/benchmark/B3_Sampling_and_Concentration.ipynb` §2–4; `Code/results/B3_origen_suelo_h016.csv`, `Code/results/B3_shots_muestreo_real.csv`; figura `Docs/Figures/E3_shots_sensitivity.png`.

---

### H-020 · Dos tipos de máscara desalineada, y los recortes oficiales como verificación al píxel
**Fecha:** 2026-09-23 · **→ Reporte:** §4.4, §8.x

**Re-auditoría.** Sobre los 3,568 registros, incluidas las 86 mamografías recuperadas en D-012, hay exactamente **80** máscaras con dimensiones distintas a las de su imagen: las mismas de H-004. Pero son de dos tipos:

| Tipo | Casos | Máscara / imagen, filas | Máscara / imagen, columnas |
|---|---|---|---|
| `scaled` | 78 masas | 0.8700 – 0.8702 | 0.8700 – 0.8704 |
| `offset` | 2 calcificaciones (`P_00353`, CC y MLO) | 0.997 – 1.014 | 1.003 – 1.011 |

Un factor uniforme en ambos ejes significa el mismo campo de visión muestreado en una malla más gruesa. **Hipótesis, PENDIENTE DE VERIFICAR contra la documentación del DDSM:** 0.870 coincide con 43.5/50, la razón entre dos pasos de muestreo (µm por píxel) de los digitalizadores del DDSM.

**Los recortes oficiales como referencia independiente.** El CBIS-DDSM incluye, para 3,453 lesiones, un recorte hecho por los autores del dataset. Localizado por correlación cruzada normalizada, aparece en la mamografía en el 100 % de los casos (NCC mínima 0.989). Dos propiedades:

- **Su intensidad está reescalada**: recorte = ganancia × mamografía, con una ganancia de mediana 1.305 y rango de 1.000 a 5.306. Por eso no sirven para extraer features de primer orden (D-022).
- **Cuando imagen y máscara coinciden, el recorte es exactamente la caja de la máscara más 20 px por lado.**

Esa segunda propiedad es un test de alineación al píxel:

| Categoría | Casos | Lectura |
|---|---|---|
| Cumple la regla | 3,206 | alineación verificada al píxel |
| Lesión a menos de 20 px del borde | 162 | no verificable: el recorte oficial queda cortado por el borde |
| Discordante | 7 | el recorte oficial y la máscara describen extensiones distintas de la lesión |
| `scaled` | 78 | la regla no se cumple con ninguna hipótesis (ver abajo) |
| Sin recorte oficial | 115 | — |

Donde se puede comprobar, **la regla se cumple en 3,206 de 3,213 casos (99.8 %)**. Los 7 discordantes son masas y cuatro son asimetrías o distorsiones de la arquitectura, con máscaras amplias e irregulares. Se conservan y quedan marcados (`crop_check = "discordant"`). **Excluirlos es una decisión del autor.**

**`offset`.** Anclando la máscara sin escalar, la regla se cumple **exactamente** en los 2 casos. Remuestreándola, no se cumple, y los bordes de la máscara quedan desplazados hasta 37 px.

**`scaled`.** Sus recortes oficiales no siguen la regla con ninguna de las dos hipótesis: se cortaron con otra geometría, con cajas más grandes y descentradas. Hace falta otro test. Se desplazó la máscara ±40 px y se midió, en cada posición, el contraste entre su interior y un anillo de 15 px a su alrededor. Si la máscara está bien colocada, el máximo debe caer en desplazamiento cero. El contraste es un indicador indirecto, así que se calibró sobre 80 masas alineadas:

| Grupo | Contraste en la posición | Relativo al máximo | Distancia al óptimo (mediana) | Óptimo a ≤ 10 px |
|---|---|---|---|---|
| 80 masas alineadas (control) | 0.950 | 0.993 | 4.3 px | 59 % |
| 78 `scaled`, remuestreadas | 0.963 | 0.998 | **1.4 px** | 76 % |
| 78 `scaled`, sin escalar | 0.052 | 0.388 | 47.7 px | 0 % |

Las máscaras remuestreadas se comportan igual que las alineadas, o mejor, y superan a la alternativa sin escalar en 77 de 78 casos.

**Impacto.** Corrige el procedimiento de H-004 y justifica D-020. Es además un dato de reproducibilidad para §8.x: ni las dimensiones de las máscaras ni los recortes oficiales son homogéneos dentro del CBIS-DDSM.

**Datos.** `Code/2_Preprocessing.ipynb` §2–3; `Code/results/2_preprocesamiento_qa.csv` (columnas `mismatch`, `ncc`, `gain`, `crop_check`); figura `Docs/Figures/M2_mask_alignment.png`.

---

### H-021 · El 86.3 % de las máscaras de masas trae islas desconectadas
**Fecha:** 2026-09-23 · **→ Reporte:** §4.4, §8.x

| | Masas | Calcificaciones |
|---|---|---|
| Máscaras con más de una componente | **1,464 / 1,696 (86.3 %)** | 0 / 1,872 |
| Área en la componente mayor | ≥ 99.55 % | 100 % |
| Segunda componente | mediana 2 px, máximo 64 px | — |
| Máscaras con dos componentes de ≥ 100 px | 0 | 0 |

Tras la alineación, eliminar las islas quita una mediana de 5 px por máscara, con un máximo de 110 px (0.45 % del área). **Las islas están pegadas a la lesión**: el píxel descartado más lejano está a una mediana de 3.6 px, con percentil 99 de 9.2 px y máximo de 14 px.

**Impacto.** Justifica D-021 y acota su efecto. Un punto a distancia d de la lesión puede alargar `MaximumDiameter` como mucho en d, así que el cambio es de pocos píxeles: ~1 % en una masa típica de 300 px. La feature más expuesta es `Perimeter`, que suma el borde de todas las componentes. Las islas son casi seguramente residuos de rasterizar el contorno de la anotación.

**Datos.** `Code/2_Preprocessing.ipynb` §4; columnas `n_components`, `area_removed` y `speck_reach_px` de `Code/results/2_preprocesamiento_qa.csv`.

---

### H-022 · CLAHE de OpenCV sobre 16 bits con `clipLimit=2` es casi la identidad
**Fecha:** 2026-09-23 · **→ Reporte:** §4.4, §8.x

La primera exportación de la variante CLAHE (D-010) se hizo directamente sobre los 16 bits de la mamografía. Dentro de la lesión, el resultado era casi idéntico a la imagen cruda. En 30 lesiones al azar (semilla 42):

| Versión | Correlación con la cruda (mediana, mín.) | Ganancia de contraste de la lesión (mediana, máx.) |
|---|---|---|
| CLAHE sobre 16 bits, `clip=2` | 1.000 (0.987) | 1.02 (1.45) |
| CLAHE sobre 8 bits, `clip=2` | 0.972 (0.617) | **1.61** (2.64) |
| 8 bits sin CLAHE (solo cuantización) | 1.000 (0.988) | 1.00 (1.03) |

*Ganancia de contraste* = desviación de la lesión relativa a la de toda la mamografía, después contra antes.

**Causa.** Es un detalle de implementación de OpenCV. El `clipLimit` se expresa relativo a la altura de un histograma plano, que depende del número de bins. Con 65,536 bins, una ventana de la mamografía ocupa solo una fracción de ellos. El recorte elimina entonces la mayor parte del histograma y la reparte uniformemente sobre todo el rango, y una ecualización construida a partir de un histograma casi uniforme es casi la identidad.

**Impacto.** Con la configuración de 16 bits, M3 habría concluido que CLAHE no altera las features, y esa conclusión habría sido un artefacto de la configuración. La variante se exporta en 8 bits (D-022). La cuantización a 8 bits por sí sola no cambia nada medible, de modo que la comparación aísla el efecto de CLAHE. Para M3, la variante CLAHE está en 0–255 y la cruda en 16 bits: las features de primer orden **no son comparables en escala** entre ambas, mientras que las de textura con `binCount=32` y las de forma sí lo son.

**Datos.** `Code/2_Preprocessing.ipynb` §5b; `Code/results/2_clahe_configuracion.csv`.

---

### H-023 · Con el conjunto completo, el mayor |d| en masas es 0.50, no 1.42
**Fecha:** 2026-09-23 · **→ Reporte:** §4.4, §6.x · *corrige H-003*

Cohen's d entre malignas y benignas con la desviación estándar combinada, sobre el conjunto de **entrenamiento**:

| | Masas (637 M / 681 B) | Calcificaciones (544 M / 1,002 B) |
|---|---|---|
| Feature más discriminativa | `firstorder_Maximum`, \|d\| = 0.50 | `shape2D_MinorAxisLength`, \|d\| = 0.82 |
| Rango de \|d\| en el top 12 | 0.40 – 0.50 | 0.64 – 0.82 |
| Mejores shape features | MinorAxisLength 0.45, MaximumDiameter 0.44, MajorAxisLength 0.43 | MinorAxisLength 0.82, Perimeter 0.71 |

H-003 reportaba |d| ≈ 1.42 para cinco shape features de masas, medido sobre **20** masas. Con 1,318 el efecto es aproximadamente un tercio de eso. Es el tercer resultado engañoso por muestra pequeña o realización única, tras H-012 y H-017.

Dos lecturas más:

- **Calcificaciones sale como el subconjunto más separable**, al revés de lo que anticipaba el EDA a partir de los descriptores categóricos. Es una comparación univariante; lo que cuenta es la separabilidad multivariante que mide M7.
- **En masas lideran features de primer orden sobre intensidades crudas**: Maximum, 90Percentile, Energy, Median y Mean. Que las masas malignas sean más densas es clínicamente plausible. Pero las intensidades no están calibradas (D-008, H-002) y el DDSM mezcla digitalizadores, de modo que parte de la señal podría venir de la adquisición. Con los datos disponibles no se puede separar, porque `Manufacturer` falta en todos los DICOM. **Conviene declararlo como limitación**, o medirlo con un análisis de sensibilidad si el autor lo considera.

La relación con M4 es directa. Para dos clases, el F de `f_classif` es t², con t = d·√(n₀n₁/(n₀+n₁)), así que dentro de un subconjunto **ordenar por F es ordenar por |d|**. El notebook lo comprueba calculando F aparte: el top 12 coincide en los cuatro casos (2 variantes × 2 subconjuntos).

**Impacto.** H-003 queda corregido. D-009 se mantiene, pero §4.4 no debe citar 1.42. El borrador ya está actualizado.

**Datos.** `Code/3_Feature_Extraction.ipynb` §5; `Code/results/3_tamano_efecto.csv`; figura `Docs/Figures/M3_effect_sizes.png`.

---

### H-024 · El top 12 de masas no tiene textura y contiene duplicados exactos
**Fecha:** 2026-09-23 · **→ Reporte:** §4.6, §6.x

Composición del top 12 por |d| en entrenamiento, que es lo que `SelectKBest(k=12)` elegiría tal cual (H-023):

| | Primer orden | Forma | GLCM | GLRLM | \|r\| medio entre las 12 | Pares con \|r\| > 0.95 |
|---|---|---|---|---|---|---|
| Masas | 7 | 5 | **0** | **0** | 0.61 | 8 de 66 |
| Calcificaciones | 1 | 2 | 4 | 5 | 0.58 | 5 de 66 |

Entre las 67 features hay **tres duplicados exactos por definición**, en 2D con espaciado unitario:

- `Energy` = `TotalEnergy`: la razón es exactamente 1, porque el área del píxel es 1.
- `SumAverage` = 2 × `JointAverage`, para una GLCM simétrica.
- `MeshSurface` y `PixelSurface`, con r = 1.0000.

Además, hay 20 pares con |r| > 0.99 en masas y 11 en calcificaciones; por ejemplo Mean, Median y RootMeanSquared, o MajorAxisLength y MaximumDiameter. En el top 12 de masas entran a la vez `Energy` y `TotalEnergy` (rangos 3 y 4), y también Mean, Median y RootMeanSquared. En calcificaciones entran `JointAverage` y `SumAverage` (rangos 8 y 9). **Tal cual, varios qubits codificarían el mismo valor.**

**Impacto.**

1. **El argumento de contenido de D-013 no se cumple en masas**: con k=12 no entra ninguna feature de textura. Sí se cumple en calcificaciones.
2. **M4 debe deduplicar antes de seleccionar.** Quitar los tres duplicados por definición no requiere justificación adicional. Aplicar además un filtro por correlación, que quite una feature cuando tenga |r| > umbral con otra mejor clasificada ajustándolo solo en train, o forzar diversidad de familias, son decisiones metodológicas. **Decisión del autor.**
3. Afecta también a la geometric difference y a la KTA: dos entradas idénticas cambian el kernel sin aportar información.

**Datos.** `Code/3_Feature_Extraction.ipynb` §5b; `Code/results/3_tamano_efecto.csv`.

---

### H-025 · CLAHE cambia las features pero no su poder discriminativo
**Fecha:** 2026-09-23 · **→ Reporte:** §4.4, §6.x · *cierra D-010*

Comparación de la variante cruda contra la variante CLAHE (8 bits, H-022), en entrenamiento. Se excluyen las shape features, que son idénticas por construcción (diferencia máxima 0):

| Subconjunto | Familia | Spearman cruda–CLAHE (mediana) | Cambio en \|d\| (mediana) | Features que mejoran |
|---|---|---|---|---|
| Masas | primer orden | 0.836 | −0.031 | 1 / 18 |
| Masas | GLCM | 0.856 | +0.002 | 15 / 24 |
| Masas | GLRLM | 0.879 | +0.011 | 13 / 16 |
| Calcificaciones | primer orden | 0.834 | −0.054 | 6 / 18 |
| Calcificaciones | GLCM | 0.860 | +0.014 | 14 / 24 |
| Calcificaciones | GLRLM | 0.881 | −0.035 | 6 / 16 |

CLAHE **reordena** las lesiones (Spearman ~0.84), pero el cambio mediano en |d| es prácticamente nulo: −0.002 en masas y −0.010 en calcificaciones. Traslada poder discriminativo entre familias sin añadirlo. Las features de primer orden pierden, como cabe esperar de una ecualización que reescribe las intensidades, y algunas de textura ganan. Las features más discriminativas de cada subconjunto no mejoran.

**Impacto.** Cierra D-010 con evidencia: dejar CLAHE fuera de la ruta radiómica no cuesta señal y preserva la reproducibilidad bajo IBSI. Es material para §6: responde de antemano a la pregunta previsible de por qué se retiró CLAHE del diseño de TT1.

**Datos.** `Code/3_Feature_Extraction.ipynb` §6; `Code/results/3_efecto_clahe.csv`; figura `Docs/Figures/M3_clahe_effect.png`.

---

### H-026 · Con la restricción de redundancia entra textura en masas, de forma estable
**Fecha:** 2026-09-23 · **→ Reporte:** §4.6

| | Selección | Primer orden | Forma | GLCM | GLRLM | \|r\| medio | \|r\| máx. | Rango F más profundo |
|---|---|---|---|---|---|---|---|---|
| Masas | `SelectKBest` tal cual | 7 | 5 | 0 | 0 | 0.61 | 1.00 | 12 |
| Masas | con \|r\| ≤ 0.95 | 4 | 5 | **1** | **2** | 0.50 | 0.94 | 19 |
| Calcificaciones | `SelectKBest` tal cual | 1 | 2 | 4 | 5 | 0.58 | 1.00 | 12 |
| Calcificaciones | con \|r\| ≤ 0.95 | 2 | 3 | 4 | 3 | 0.50 | 0.94 | 20 |

Se descartan 7 features en masas y 8 en calcificaciones, entre ellas los tres duplicados por definición. Las 12 elegidas en masas son Maximum, 90Percentile, Energy, MinorAxisLength, MaximumDiameter, Perimeter, MeshSurface, PerimeterSurfaceRatio, GLRLM GrayLevelNonUniformity, 10Percentile, GLCM Correlation y GLRLM RunLengthNonUniformity.

**Sensibilidad al umbral.** En masas entra textura con cualquier umbral entre 0.99 y 0.80: 2 features a 0.99, 3 a 0.95, 5 a 0.90 y 5 a 0.80. La conclusión no depende de haber elegido exactamente 0.95.

**Impacto.** Resuelve la objeción de H-024 al argumento de contenido de D-013: con la restricción, también en masas se combinan forma, intensidad y textura.

**Datos.** `Code/4_Selection_and_Scaling.ipynb` §3; `Code/results/4_seleccion.csv`, `4_descartadas_redundancia.csv`, `4_sensibilidad_umbral.csv`; figura `Docs/Figures/M4_selection_and_angles.png`.

---

### H-027 · Los folds deben agruparse por paciente, y la semilla 42 desbalancea los de calcificaciones
**Fecha:** 2026-09-23 · **→ Reporte:** §4.9

Con `StratifiedKFold` (5 folds, semilla 42), **410 de 691 pacientes de masas (59 %) y 445 de 602 de calcificaciones (74 %)** quedan repartidos entre folds. La regla de D-018 se aplica, y con `StratifiedGroupKFold` agrupado por `patient_id` ninguno queda repartido.

El precio aparece en calcificaciones. Hay pacientes con hasta 24 lesiones, todas benignas, y un paciente no se puede dividir. Con la semilla 42, el fold 2 queda con un 52 % de malignas frente al 35 % global. Comparada con otras 200 semillas:

| | Desviación máx. de la proporción de malignas, semilla 42 | Mediana en 200 semillas | Mejor semilla |
|---|---|---|---|
| Masas | 0.038 | 0.060 | 0.011 (125) |
| Calcificaciones | **0.168** | 0.065 | 0.019 (168) |

En calcificaciones, la semilla 42 es la **peor** de las 200.

**Impacto.** **Decisión del autor.** Se puede conservar la semilla 42 del proyecto (RNF-01) y declarar el desbalance, o fijar la semilla de los folds por un criterio que solo mira las etiquetas, como la mínima desviación de la proporción de clases. Este segundo criterio no usa features ni rendimiento, así que no es ajustar el resultado, pero hay que declararlo.

**Resuelto el 2026-09-23 (D-026):** semilla 125 en masas y 168 en calcificaciones. La proporción de malignas de cada fold se aleja como mucho 0.011 y 0.019 de la global; en calcificaciones queda entre 0.33 y 0.37 por fold.

**Limitación a declarar en §4.9.** Bajo la Arquitectura B los embeddings se calculan una sola vez (D-014), así que el selector y el escalador se ajustan una vez sobre todo el train y no dentro de cada fold. Las estimaciones de la validación cruzada son por tanto algo optimistas. El test oficial no se toca y sigue siendo la estimación insesgada.

**Datos.** `Code/4_Selection_and_Scaling.ipynb` §5; `Code/results/4_folds.csv`.

---

### H-028 · Min-max deja casi constantes los ángulos de las features de cola pesada
**Fecha:** 2026-09-23 · **→ Reporte:** §4.6, §6.x

`MinMaxScaler` a [0, π] ajustado en train. Test recortado: 0.0 % de los valores en masas y 0.1 % en calcificaciones, así que el recorte no es problema. El problema es la **distribución** dentro del rango. Rango intercuartílico de los ángulos en train:

| Subconjunto | Feature | Mediana del ángulo | IQR (rad) |
|---|---|---|---|
| Calcificaciones | `firstorder_Energy` | 0.015 | **0.046** |
| Calcificaciones | `shape2D_PixelSurface` | 0.020 | **0.057** |
| Calcificaciones | `glcm_ClusterShade` | 1.089 | 0.155 |
| Masas | `shape2D_MeshSurface` | 0.135 | 0.144 |
| Masas | `firstorder_Energy` | 0.143 | 0.197 |
| Masas | `glcm_Correlation` | 2.969 | 0.227 |

Como referencia, la mediana del IQR es de 0.34 rad en masas y de 0.40 en calcificaciones. Las features que crecen con el área de la lesión tienen colas largas, y unos pocos valores extremos fijan el rango. En calcificaciones, la mitad de las lesiones tiene `Energy` a menos de 0.05 rad de cero, así que ese qubit recibe casi la misma rotación para todas las lesiones.

**Impacto.** El MLP de C1 apenas se ve afectado por el sesgo de una feature, pero la codificación angular (C4, C5) y el kernel RBF (C3) sí. La comparación podría quedar inclinada **en su contra por el escalado**, no por la codificación. **Decisión del autor.** Las opciones son conservar min-max y declararlo; aplicar un logaritmo a las features positivas de cola pesada antes de escalar; o aplicar una transformación por cuantiles a una distribución uniforme en [0, π], que reparte todas las features de manera homogénea. Las tres son compatibles con D-004, porque el rango sigue siendo [0, π]. Conviene decidirlo antes de calcular los embeddings.

**Resuelto el 2026-09-23 (D-025):** con la transformación por cuantiles, las 12 features de ambos subconjuntos tienen un IQR de π/2 (1.569–1.572 rad).

**Datos.** `Code/4_Selection_and_Scaling.ipynb` §4; columnas `angle_median` y `angle_iqr` de `Code/results/4_seleccion.csv`; figura `Docs/Figures/M4_selection_and_angles.png`.

---

### H-029 · El procedimiento documentado para instalar PyRadiomics no funcionaba
**Fecha:** 2026-09-23 · **→ Reporte:** §8.x

Al instalar PyRadiomics en `qml_cancer` siguiendo `Code/env/README.md`, el procedimiento falló en dos puntos:

1. `git fetch --depth 1 origin 8ed5793` → *couldn't find remote ref*. GitHub solo permite pedir un commit por su **hash completo**, `8ed579383b44806651c463d5e691f3b2b57522ab`.
2. Con `--no-build-isolation`, la compilación se detiene en la preparación de metadatos por falta de **`setuptools_scm`**, que calcula el número de versión. No estaba en la lista de dependencias de compilación del README.

Había además un paso de riesgo: `pip install --upgrade "numpy>=2.0"` actualiza numpy a la última versión disponible, y en `qml_cancer` eso podía romper la compatibilidad con Qiskit.

**Impacto.** El README queda corregido: hash completo, clon sin blobs, todas las dependencias fijadas con versión, `--no-deps` y ningún cambio de numpy. Con él, la compilación se reprodujo desde cero en un entorno distinto y dio features idénticas. Es el mismo tipo de hallazgo que H-006, y conviene citarlo junto a él en §8.x: la reproducibilidad de un pipeline radiómico depende de pasos de instalación que se rompen sin avisar.

---

### H-030 · La selección univariante no ve interacciones, que es justo lo que codifica el bloque ZZ
**Fecha:** 2026-09-24 · **→ Reporte:** §4.6, §7

`SelectKBest` y el filtro de redundancia (D-024) juzgan cada feature **por separado**: la F de ANOVA por su poder discriminativo individual, y la correlación de Pearson de dos en dos. Una feature cuyo valor está solo en combinación con otra se descarta antes de llegar al circuito.

**Ejemplo, un patrón XOR.** Benignas con (bajo, bajo) y (alto, alto), malignas con (bajo, alto) y (alto, bajo). Cada feature tiene por separado d = 0 y F = 0, y `SelectKBest` descarta las dos. Juntas, en cambio, separan las clases perfectamente, a través del signo del producto (x₁ − media)(x₂ − media).

**La tensión con el diseño.** El bloque ZZ del `zz_feature_map` codifica precisamente productos de pares, (π − xᵢ)(π − xⱼ): es donde está lo que la codificación cuántica podría aportar. La selección, en cambio, no mira interacciones.

**Impacto.**

- La comparación entre condiciones sigue siendo justa, porque las cinco reciben las mismas 12 features.
- Casos puros como el XOR son raros en features radiómicas; lo habitual es que una feature útil en combinación también tenga algo de señal por sí sola.
- Aun así hay que **declararlo en §7**, porque es la objeción natural: «si lo cuántico aporta interacciones, ¿por qué se seleccionó sin mirarlas?».
- Como análisis de robustez opcional, se puede comparar con una selección multivariante. **Decisión del autor.**

---

### H-031 · A 12 qubits, cambiar una sola feature deja el estado del feature map casi ortogonal
**Fecha:** 2026-09-24 · **→ Reporte:** §4.9, §6.x

Se tomó el estado de `zz_feature_map(12)` para la lesión `Mass-Training_P_00001_LEFT_CC_1` y se cambió solo `x_01`. La fidelidad |⟨φ(x)|φ(x')⟩|² entre los estados es **0.0000** en los tres casos: de 0 a π/2, de 0 a π y de π/2 a π.

**Por qué.**

- De 0 a π/2, la fase del qubit 1 cambia en π y el qubit pasa de |+⟩ a |−⟩, que son estados ortogonales.
- De 0 a π la fase individual da una vuelta completa, pero los 11 términos ZZ en los que participa ese qubit cambian, y eso basta para hacer el estado ortogonal.

La codificación es extremadamente sensible a cada feature.

**Impacto.** Dos lesiones distintas en las 12 features podrían tener fidelidad casi nula. En ese caso la matriz del kernel cuántico se acercaría a la identidad, y la KTA y la *geometric difference* dejarían de ser informativas. En la literatura esto se describe como concentración de los kernels cuánticos; **buscar y verificar la referencia antes de citarla**.

**Diagnóstico antes de M5.** Calcular el kernel sobre una muestra pequeña y mirar la distribución fuera de la diagonal, antes de invertir ~2.75 h en las cuatro matrices. Si está concentrado, la salida habitual es escalar los ángulos por un factor de ancho de banda, x → c·x con c < 1. Eso cambiaría el diseño angular (D-004, D-025), así que sería una **decisión del autor**.

**Datos.** Verificación puntual del 2026-09-24 con los ángulos de `Data/processed/m4/x_mass.parquet`.

**Confirmado el 2026-09-24 sobre la submuestra real de D-028** (200 lesiones de train por subconjunto, kernel exacto). Valores fuera de la diagonal:

| Subconjunto | Kernel | Mediana | Percentil 95 | Pares con fidelidad < 10⁻³ |
|---|---|---|---|---|
| Masas | C4 `zz_feature_map` | 0.0022 | 0.011 | 23 % |
| Masas | C5 `pauli(['X','ZZ'])` | 0.0028 | 0.015 | 20 % |
| Calcificaciones | C4 | 0.0029 | 0.014 | 16 % |
| Calcificaciones | C5 | 0.0041 | 0.018 | 10 % |
| Ambos | RBF clásico, γ por mediana (D-027) | 0.607 | — | — |

*Las filas de C5 corresponden al C5 original, `['X','ZZ']`, que era un mapa solo ZZ (H-034). Con el C5 actual, `['Y','ZZ']` (D-031), la mediana es 0.00003 en ambos subconjuntos (H-037).*

La matriz del kernel cuántico es casi la identidad. Con K ≈ I, la KTA tiende a 1/√n ≈ 0.07 para n = 200, independientemente de las etiquetas.

**Corregido el 2026-09-24 tras verificar la fuente.** La primera versión decía que la *geometric difference* crecería; Huang et al. (2021) dicen lo contrario. En el texto principal: *"a variety of common quantum models in the literature perform similarly or worse than classical ML […] due to a small geometric difference. The small geometric difference is a consequence of the exponentially large Hilbert space employed by existing quantum models, where all inputs are too far apart."* En el Apéndice I: *"the quantum kernel function […] will be exponentially close to zero for xᵢ ≠ xⱼ. In this case K_Q will be close to the identity matrix"*, y distinguir valores tan pequeños exigiría un número exponencial de mediciones en hardware. **Nuestro caso es exactamente el escenario que el paper describe como típico de los modelos cuánticos que no superan a los clásicos.**

Queda pendiente extraer del Apéndice F la versión regularizada de *g* antes de implementar M7. El paper propone además kernels cuánticos **proyectados**, que devuelven los estados a una representación clásica local. Es conceptualmente cercano a nuestros ⟨Zᵢ⟩, pero hay que verificar el paralelo antes de afirmarlo.

**Escalar los ángulos (x → c·x) apenas lo corrige.** Mediana del kernel fuera de la diagonal en masas, C4: 0.002 con c = 1; 0.006 con 0.5; 0.032 con 0.2; 0.069 con 0.1; 0.199 con 0.05. Calcificaciones y C5 dan valores análogos.

**Causa, corregida y verificada el 2026-09-24.** El término ZZ de Qiskit aplica una fase 2(π − xᵢ)(π − xⱼ) sobre ZᵢZⱼ, y cada qubit participa en 11 de los 66 pares. La fase del estado cambia con xᵢ a una tasa de 2 por su término propio más Σⱼ 2(π − xⱼ) por los pares. Sobre los datos reales, esa segunda parte vale una mediana de 37 (rango 2.8–66.7): **unas 18 veces el término propio**. El eigenvalor mínimo del RBF K_C es ~6×10⁻⁶, así que el cálculo de *g* en M6 necesitará la versión regularizada, no 70 como decía la primera versión, que usaba el caso extremo xⱼ ≈ 0.

Al escalar x → c·x, la fase del par vale 2π² − 2πc(xᵢ + xⱼ) + 2c²xᵢxⱼ. La parte constante es la misma para todas las entradas y se cancela en la fidelidad. El término lineal sigue multiplicando a ZᵢZⱼ, así que **el entrelazamiento dependiente de los datos persiste**, pero solo codifica sumas xᵢ + xⱼ. Lo que se anula, en orden c², es el **producto xᵢxⱼ, es decir, la interacción entre features**.

Comprobación: kernel con el mapa completo frente a un mapa idéntico sin el término de producto. La tabla es una verificación rápida del coordinador con 60 masas. Las cifras canónicas son las de `Code/5b_Quantum_Kernels.ipynb`, con las 200 lesiones de la submuestra: correlación de **0.700** (masas) y **0.691** (calcificaciones) con c = 1, y de **0.99997** y **0.99999** con c = 0.02. La razón mediana de sensibilidad es 18.2× y 17.6×.

| c | Mediana, mapa completo | Mediana, sin producto | Correlación |
|---|---|---|---|
| 1 | 0.0019 | 0.0002 | 0.920 |
| 0.2 | 0.031 | 0.031 | 0.983 |
| 0.05 | 0.186 | 0.181 | 0.9996 |
| 0.02 | 0.527 | 0.523 | **1.0000** |

**Conclusión precisa:** el kernel solo deja de estar concentrado en la escala en que el término de producto xᵢxⱼ ya no influye. Se pierde justo la interacción de segundo orden que el mapa ZZ debía codificar. Es material directo del OE-6.

---

### H-032 · `FidelityStatevectorKernel` da el mismo kernel exacto ~1000× más rápido
**Fecha:** 2026-09-24 · **→ Reporte:** §8.x, OE-6 · *corrige el coste del kernel de B1 y D-017*

Se temía que `FidelityQuantumKernel` muestreara con shots por defecto, igual que el problema de H-019. **No es así** en qiskit-machine-learning 0.9: su `ComputeUncompute` por defecto da valores exactos, con diferencia máxima 0.0000 frente al kernel exacto en una prueba de 6×6. Pero construye un circuito por par de lesiones, de modo que el coste es O(N²) simulaciones. `FidelityStatevectorKernel` calcula N vectores de estado una sola vez y obtiene todas las fidelidades como productos internos.

| | Tiempo |
|---|---|
| `FidelityQuantumKernel`, 6×6 | 1.7 s |
| `FidelityStatevectorKernel`, 200×200, exacto | **1.5 s** |
| Proyección de B1 para 200×200 con `FidelityQuantumKernel` | ~41 min |

**Impacto.** D-017 se mantiene, porque la definición del kernel es idéntica. Cambia la implementación: `FidelityStatevectorKernel`, que es exacto y rápido. El «cuello de botella del kernel» de B1 (sección 4) y las 2.75 h previstas en D-017 y D-028 eran un coste de la implementación compute-uncompute, no del cálculo. En hardware real no existe ese atajo, porque no se tiene acceso al vector de estado. Esa distinción entre lo que permite la simulación y lo que costaría en un dispositivo real es material del OE-6.

---

### H-033 · La ecuación de la *geometric difference* del reporte invierte K_C y K_Q
**Fecha:** 2026-09-24 · **→ Reporte:** §3.4.2 (`eq:geometric_diff`), RF-16 · Fase 7

**Fuente verificada.** Huang et al. (2021), *Power of data in quantum machine learning* (arXiv:2011.01938), ecuación (5):

  g₁₂ = g(K₁‖K₂) = √‖ √K₂ (K₁)⁻¹ √K₂ ‖∞,  con Tr(K₁) = Tr(K₂) = N,

y la cantidad que evalúa el potencial de ventaja cuántica es **g_CQ = g(K_C‖K_Q)**. Es decir, el kernel **cuántico** va en las raíces y el **clásico** es el que se invierte: g_CQ = √‖√K_Q · K_C⁻¹ · √K_Q‖∞.

**El reporte** (ecuación `eq:geometric_diff` y RF-16) escribe √‖√K_C · K_Q⁻¹ · √K_C‖∞, que es g(K_Q‖K_C), la dirección contraria. La interpretación que la acompaña («si g ≫ 1, el kernel cuántico captura estructura que el RBF no ve») corresponde a g_CQ, de modo que la fórmula y su lectura no coinciden entre sí.

**Detalles adicionales.**
- Falta la condición de normalización Tr(K_C) = Tr(K_Q) = N.
- El reporte dice que √K_C se obtiene «por descomposición de Cholesky». El factor de Cholesky L no es la raíz cuadrada simétrica, aunque Lᵀ(·)L da la misma norma espectral. Conviene decir «raíz cuadrada matricial», o precisar el orden de los factores.

**Impacto.** Corrección obligatoria antes de implementar M7 y de escribir §6. La redacción es del autor. M7 debe implementar g_CQ tal como la define la fuente, e incluir la versión regularizada del Apéndice F, pendiente de extraer.

---

### H-034 · Con reps=1, el término X de C5 no codifica nada: C5 es un mapa solo ZZ
**Fecha:** 2026-09-24 · **→ Reporte:** §4.7, §6.x · *corrige la interpretación de D-015*

Se detectó al revisar la descomposición del circuito en el notebook 5a. `pauli_feature_map(12, reps=1, paulis=['X','ZZ'])` aplica, por qubit, una capa de Hadamard, después el término X implementado como H·P(2xᵢ)·H, y después los bloques ZZ. Tras la capa de Hadamard cada qubit está en |+⟩, **autoestado de X**. La rotación en X solo lo multiplica por una fase, y sobre ese estado producto las 12 fases se combinan en una **fase global**, que no afecta a ninguna medición ni a ninguna fidelidad.

**Verificación numérica.**

| Comparación | Resultado |
|---|---|
| Fidelidad entre `pauli(['X','ZZ'])` y `pauli(['ZZ'])` con reps=1, 20 entradas al azar | mínimo 0.99999999999999 |
| Kernel de C5 frente al kernel solo ZZ, submuestra real de masas | diferencia máxima 5.9×10⁻¹⁵ |
| Lo mismo con reps=2 | los estados sí difieren (fidelidad media 0.0002) |

La fidelidad media de 0.071 que H-012 midió entre `['X','ZZ']` y ZZ a k=4 queda explicada: F = Π cos²(xᵢ), cuya esperanza con xᵢ uniforme es (1/2)^k = 0.0625 a k=4.

**Impacto.**

- La afirmación de D-015, que C4 contra C5 mide el eje de la codificación de primer orden, **es incorrecta**. Lo que mide es la presencia o ausencia de un término de primer orden, con el mismo acoplamiento ZZ.
- Los resultados ya calculados (5a y 5b) son válidos como «C5 = mapa solo ZZ».
- Sigue siendo una comparación legítima, porque es una ablación del término de primer orden, pero hay que describirla así.
- La otra salida es cambiar a un conjunto cuyo primer orden sí actúe, como `['Y','ZZ']` o `['Z','YY']`, a revisar con la tabla de H-012. **Decisión del autor (Q-012).**
- El texto del borrador de §4.7 y el pie del diagrama del §4.1 deben corregirse en consecuencia.

**Cómo se coló.** La afirmación sobre el eje se escribió en la noche del 22 a partir de los nombres de los operadores, sin comprobar cómo actúan sobre el estado que encuentran. Es el mismo tipo de error de H-013: una propiedad del formalismo, en este caso los autoestados, que ningún nombre de función revela.

---

### H-035 · Pasar de 67 a 12 features cuesta de 2 a 4 puntos de AUC, y las 12 elegidas por F no superan a 12 al azar
**Fecha:** 2026-10-04 · **→ Reporte:** §4.6, §7, OE-6 · *complementa H-030*

**Pregunta.** ¿Cuánta información se pierde al quedarse con 12 de las 67 features de M3? Aclaración previa: la figura `M3_effect_sizes.png` del notebook 3 dibuja las 25 features más discriminativas solo como contexto visual. Ningún paso conserva 25: la selección va de 67 a 12 directamente, en M4 (D-013, D-024).

**Método.** Se midieron dos sentidos de «información» distintos. Todo se calculó solo sobre train, con los folds congelados de M4, agrupados por paciente (D-026); el test no se tocó. La réplica de la regla de selección reproduce exactamente las 12 features de M4, en el mismo orden.

- **Información general.** Cuánta varianza de las 67 explican linealmente las 12, tras normalizarlas por cuantiles. Como cota se usa una PCA con 12 componentes. La R² lineal es una cota inferior: no cuenta la dependencia no lineal.
- **Información para la etiqueta.** AUC en validación cruzada de dos clasificadores clásicos sobre las features crudas: una regresión logística (LR), que solo ve efectos lineales, y un *random forest* (RF), que ve interacciones. Toda selección y todo preprocesamiento se ajustan dentro de cada fold.

**Información general: se pierde poco.**

| | Masas | Calcificaciones |
|---|---|---|
| Varianza de las 67 retenida por las 12 | 86.8 % | 90.2 % |
| Cota con 12 componentes de PCA | 98.0 % | 97.8 % |
| Descartadas que las 12 reconstruyen en más del 90 % | 26 de 55 | 28 de 55 |
| Lo peor reconstruido | ClusterShade (R² 0.44), Skewness (0.45) | Kurtosis (0.56), Maximum (0.66) |

Las features radiómicas describen muchas veces unas pocas propiedades de fondo: tamaño, intensidad y textura. Lo que las 12 recuperan peor es la *forma de la distribución de intensidades*.

**Información para la etiqueta: una pérdida modesta.** AUC media ± desviación entre folds. En «12 al azar», el ± es la dispersión entre 20 sorteos.

| Conjunto | Masas, LR | Masas, RF | Calcif., LR | Calcif., RF |
|---|---|---|---|---|
| Las 67 | 0.693 ± 0.039 | 0.695 ± 0.043 | 0.800 ± 0.028 | 0.796 ± 0.018 |
| Las 12 de M4 | 0.650 ± 0.056 | 0.680 ± 0.046 | 0.758 ± 0.025 | 0.773 ± 0.024 |
| 12 reseleccionadas dentro de cada fold | 0.653 | 0.675 | 0.757 | 0.774 |
| Top 12 por F sin filtro de redundancia | 0.645 | 0.649 | 0.744 | 0.763 |
| 12 al azar | 0.656 ± 0.019 | 0.659 ± 0.023 | 0.765 ± 0.015 | 0.775 ± 0.016 |

**Lecturas.**

1. **La pérdida es de 2 a 4 puntos de AUC.** Con LR es de 0.042 en ambos subconjuntos; con RF, de 0.015 en masas y 0.023 en calcificaciones. Eso es más o menos una desviación estándar entre folds. La curva del AUC contra k no se estanca en 12, así que la señal restante está repartida en muchas features, cada una con poco aporte. Con todas las que sobreviven al filtro de redundancia (39 en masas y 43 en calcificaciones), el AUC queda a 0.016 o menos del de las 67.
2. **Las 12 elegidas por F no superan a 12 al azar.** Las diferencias van de −0.007 a −0.002 y caen dentro del ruido, salvo con RF en masas (+0.021). Las mejores features individuales no forman el mejor conjunto. El ranking por F favorece las que separan las clases por sí solas, y esas tienden a medir la misma propiedad (lesión grande, lesión brillante). Un sorteo al azar es más diverso y sus features se complementan. Es la contraparte multivariante de H-030. La referencia clásica es Guyon y Elisseeff (2003), *An introduction to variable and feature selection*, JMLR 3; **verificar contra la fuente antes de citarla.**
3. **El filtro de redundancia ayuda.** El top 12 sin filtro es el peor conjunto en las cuatro columnas, lo que respalda D-024.
4. **Seleccionar una sola vez con todo el train no filtra nada medible.** Las 12 fijas y las 12 reseleccionadas dentro de cada fold difieren como mucho en 0.006 de AUC. La advertencia de H-027, que la validación cruzada es algo optimista, pesa muy poco en este punto.

**Impacto.**

- **La comparación entre condiciones sigue siendo justa.** C1–C5 reciben las mismas 12 features, así que la pérdida las afecta a todas por igual.
- **Material del OE-6.** El presupuesto de qubits obliga a descartar información que cuesta de 2 a 4 puntos de AUC con clasificadores clásicos. Hay que declararlo como limitación en §7.
- **No se cambia el diseño.** Cambiar la selección después de ver estos resultados añadiría un grado de libertad elegido con los datos a la vista, y obligaría a rehacer M4 y M5. Una selección multivariante (mRMR, L1) queda como análisis de robustez opcional después del congelamiento del 23 oct. **Decisión del autor.**
- **Alcance.** Son clasificadores clásicos sobre las features crudas: acotan la información disponible para todas las condiciones, pero no predicen el AUC del MLP de M7 sobre C1–C5.

**Datos.** `Code/experiments/X1_Selection_Information_Loss.ipynb`; `Code/results/X1_varianza_retenida.csv`, `X1_auc_por_condicion.csv`, `X1_auc_vs_k.csv`; figura `Docs/Figures/X1_selection_auc_vs_k.png`.

---

### H-036 · Con c = 1, el kernel cuántico conserva poca de la información de clase que ve el RBF; achicar los ángulos la recupera solo hasta el nivel clásico
**Fecha:** 2026-10-04 · **→ Reporte:** §6.x, OE-3, OE-6 · *complementa H-031*

**Pregunta.** La figura `M5_kernel_concentration.png` de 5b dice cuánto se parecen dos lesiones *cualesquiera*, sin usar las etiquetas. Lo que falta es saber si dos lesiones de la **misma clase** se parecen más que dos de **clases distintas**.

**Método.** Se usan los kernels del M5 tal como están, sobre las mismas 200 lesiones de train por subconjunto (D-028); las etiquetas entran aquí por primera vez. Cada par de lesiones distintas se cuenta una sola vez y se clasifica en benigna–benigna (B–B), maligna–maligna (M–M) o benigna–maligna (B–M).

El resumen es el **AUC de pares**: la probabilidad de que un par de la misma clase sea más parecido que un par de clases distintas. Vale 0.5 si el kernel ignora la clase. Como se basa en rangos, no le afecta que los valores cuánticos sean cien veces menores que los clásicos.

Los pares comparten lesiones y no son independientes, así que la referencia es una **prueba de permutación**: las etiquetas se barajan 1,000 veces, conservando el número de lesiones de cada clase. Es la misma idea del KTA del M6, que también contrasta similitudes de la misma clase y de clases distintas, ⟨K, yyᵀ⟩ = Σ_misma K − Σ_distinta K.

| Kernel | Masas: AUC de pares | p | Calcificaciones: AUC de pares | p |
|---|---|---|---|---|
| K_C (RBF) | 0.523 | 0.002 | 0.575 | 0.001 |
| C4, c = 1 | 0.510 | 0.012 | 0.520 | 0.021 |
| C5, c = 1 | 0.508 | 0.047 | 0.547 | 0.001 |
| C4, c = 0.02 | 0.522 | 0.002 | 0.577 | 0.001 |
| C5, c = 0.02 | 0.522 | 0.002 | 0.578 | 0.001 |

Con las etiquetas barajadas, la desviación estándar del AUC de pares es de 0.004 en masas y 0.008 en calcificaciones.

**Actualizado el 2026-10-05 (D-031).** Las filas de C5 son del C5 actual, `['Y','ZZ']`. Con el C5 original, un mapa solo ZZ, eran 0.505 (p = 0.088) en masas y 0.515 (p = 0.042) en calcificaciones a c = 1.

**Lecturas.**

1. **El kernel clásico sí ve las clases, aunque de forma modesta.** En calcificaciones el efecto viene sobre todo de que los pares B–M se parecen menos: mediana de 0.583, contra 0.652 en B–B y 0.663 en M–M. Las masas son difíciles para todos los kernels, de acuerdo con los tamaños de efecto moderados del M3 (H-023).
2. **Con el diseño preregistrado, el kernel cuántico conserva solo parte de esa información.** En masas, C4 y C5 quedan como mucho 0.01 por encima del azar. En calcificaciones, C4 conserva más o menos una cuarta parte del margen del RBF sobre el azar (0.020 contra 0.075) y C5 cerca del 60 % (0.047). En los histogramas de C4 los tres tipos de par se superponen casi por completo; en los de C5 en calcificaciones, los pares B–M quedan visiblemente a la izquierda.
3. **Achicar los ángulos la recupera, pero solo hasta el nivel clásico.** El AUC de pares sube al bajar c, y a c = 0.02 iguala al del RBF. A esa escala el kernel cuántico es prácticamente el de un mapa sin el término de producto xᵢxⱼ (H-031). La información de clase recuperada es la que un kernel clásico ya ve, no información nueva aportada por las interacciones.
4. **C4 contra C5 (D-031).** En masas son indistinguibles a c = 1. En calcificaciones C5 supera a C4 en 0.027, unas tres o cuatro desviaciones estándar de la permutación; como se prueban muchos kernels, es un indicio y no una prueba formal. Aun así, C5 queda por debajo del RBF. Con el C5 original, solo ZZ, los dos mapas eran indistinguibles.
5. **Valores irresolubles.** El 26–28 % de los pares de C5 tiene fidelidad menor que 10⁻⁶ (H-037). La señal no viene de ahí: restringido a los pares con fidelidad de 10⁻⁶ o más, el AUC de pares de C5 es 0.510 en masas y 0.570 en calcificaciones.

**Impacto.**

- **Con esta medida por pares no hay indicio** de que la codificación cuántica capture estructura de clase que el kernel clásico no vea; con el diseño preregistrado captura menos. Anticipa el resultado del KTA y de la *geometric difference* del M6, que siguen siendo las métricas formales.
- **Alcance.** El AUC de pares es una medida global sobre todos los pares. Valores de 0.52 a 0.58 son normales cuando las clases son heterogéneas, y no acotan el AUC de un clasificador, que puede aprovechar la estructura local.
- **Q-012 quedó cerrada por D-031** (C5 = `['Y','ZZ']`). Con el C5 original, C4 y C5 eran indistinguibles con esta medida; con el término Y difieren en calcificaciones. La conclusión principal no cambia: ningún kernel cuántico supera al RBF.
- Se corrige de paso un detalle de la figura de 5b: su eje y cuenta cada par dos veces, porque toma los dos triángulos de la matriz simétrica. En X2 cada par se cuenta una vez. La forma de la distribución no cambia.
- Los valores de p son indicativos, porque se prueban muchos kernels.

**Datos.** `Code/experiments/X2_Kernel_Class_Structure.ipynb`; `Code/results/X2_auc_pares.csv`; figuras `Docs/Figures/X2_kernel_pairs_by_class.png` y `X2_pair_auc_sweep.png`.

---

### H-037 · Con `['Y','ZZ']`, C5 se dispersa tres veces más que C4 en ⟨Zᵢ⟩, pero su kernel se concentra unas setenta veces más
**Fecha:** 2026-10-05 · **→ Reporte:** §4.7, §6.x, OE-6 · *consecuencia de D-031; caso concreto de H-013*

| | Masas | Calcificaciones |
|---|---|---|
| Desviación estándar media por dimensión de ⟨Zᵢ⟩, C4 | 0.057 | 0.048 |
| Lo mismo, C5 original (`['X','ZZ']`) | 0.055 | 0.046 |
| Lo mismo, C5 actual (`['Y','ZZ']`) | **0.180** | **0.178** |
| Mediana del kernel fuera de la diagonal, C4 | 0.0022 | 0.0029 |
| Lo mismo, C5 original | 0.0028 | 0.0041 |
| Lo mismo, C5 actual | **0.000032** | **0.000031** |
| Pares del C5 actual con fidelidad < 10⁻³ | 80 % | 76 % |
| Pares del C5 actual con fidelidad < 10⁻⁶ | 26 % | 28 % |

**Por qué el embedding se dispersa.** Sin el ansatz, ⟨Zᵢ⟩ de C4 es 0 para toda entrada (H-013), mientras que el de C5 vale −sin(2xᵢ): el giro en Y cambia directamente las probabilidades de 0 y 1. Esa contribución directa de cada feature, que el ansatz después mezcla entre qubits, es lo que dispersa el embedding.

**Por qué el kernel se concentra.** Los términos de primer orden solos dan el mismo kernel, sea en Z o en Y: diferencia máxima de 3×10⁻¹⁵ y mediana de ~2×10⁻⁷. Cada uno aporta un factor cos²(xᵢ − x′ᵢ) por qubit. La diferencia aparece al combinarlos con ZZ.
- En C4 todas las puertas tras los Hadamard son diagonales, así que el término Z solo añade una fase pequeña al patrón de fases ZZ (tasa 2 contra ~36, H-031) y C4 queda cerca de un mapa solo ZZ.
- En C5 el giro en Y no es diagonal: cambia las amplitudes antes de que actúen las fases ZZ, y dos lesiones pierden solapamiento tanto por las amplitudes como por las fases.

**El barrido de c** sigue llevando C5 al nivel del RBF a c = 0.02, con medianas de 0.54 y 0.58, pero no es monótono: entre c = 0.5 y c = 0.2 la mediana baja, de 0.0084 a 0.0049 en masas. El mecanismo de esa no monotonía no está establecido.

**Impacto.**
- **Es el caso que anticipaba H-013.** El kernel y los ⟨Zᵢ⟩ miden objetos distintos, y aquí van en direcciones opuestas. El M6 debe reportar ambas familias de métricas sin esperar que coincidan.
- **OE-6.** En hardware, un valor del kernel es la probabilidad del resultado «todo ceros», y verlo una sola vez exige del orden de 1/K disparos: 10⁶ para K = 10⁻⁶. Una cuarta parte de los pares de C5 solo se distingue en simulación exacta.
- **Para el M6.** La *geometric difference* de C5 se calculará sobre una matriz todavía más cercana a la identidad que la de C4, así que la versión regularizada del Apéndice F (H-033) es aún más necesaria.
- Pese a la concentración, el AUC de pares de C5 en calcificaciones es el mayor de los dos mapas cuánticos y no depende de los valores irresolubles (H-036).

**Datos.** `Code/5a_Embeddings.ipynb` (2°a, celda de inspección y 4°a); `Code/5b_Quantum_Kernels.ipynb` (6c y 7°); `Code/results/5a_resumen.csv` y `5b_concentracion_kernel.csv`.

---

### H-038 · La *g* que reportan Huang et al. es regularizada y es el mínimo sobre una batería de kernels clásicos
**Fecha:** 2026-10-06 · **→ Reporte:** §3.4.2, §4.9, RF-16 · *completa H-033*

**Fuente.** Huang et al. (2021), arXiv:2011.01938, en el PDF descargado por el autor: Apéndice F.3, ecuaciones (F19)–(F20), y Apéndice L.3, ecuaciones (L8)–(L11). La versión publicada es *Nat. Commun.* 12, 2631 (2021), DOI 10.1038/s41467-021-22539-9, con licencia CC BY 4.0, verificada en Europe PMC (PMC8113501). Su texto principal solo trae la ecuación (5) sin regularizar; los apéndices están en la Información Suplementaria, con una numeración que no se verificó.

**Lo que dice, en nuestra notación.**
- (F19): g_gen = √‖√K_Q √K_C (K_C + λI)⁻² √K_C √K_Q‖∞.
- (F20): g_tra = λ·√‖√K_Q (K_C + λI)⁻² √K_Q‖∞, la cota del error de entrenamiento que se le permite al modelo clásico.
- Con λ = 0 se recupera la ecuación (5). Cita textual: *"When λ is non-zero, the geometric difference can become much smaller."*
- Protocolo numérico (L.3): λ ∈ {10⁻⁵, 10⁻⁴, 10⁻³, 10⁻², 0.025, 0.05, 0.1}; K_C lineal o gaussiano con γ ∈ {0.25, …, 64}/(n·Var[x]); se exige g_tra < 0.045 y se reporta el mínimo de *g*. El texto principal (p. 5) pide considerar *g* *"with respect to a suite of optimized classical ML models"*.
- La primera prueba del diagrama de flujo de su Fig. 1 compara g_CQ con √N: si g_CQ ≪ √N, el aprendizaje clásico predice igual o mejor, sea cual sea el etiquetado.

**Tres trampas.**
1. **Notación.** En el Apéndice F.3, K₁ es el kernel de la función de origen y va fuera, mientras que K₂ se regulariza; en la ecuación (5) es al revés, porque K₁ es el que se invierte. En ambos casos, para g_CQ el kernel clásico es el que se invierte y el cuántico va en las raíces. Es el mismo tipo de confusión de H-033.
2. **Errata en (F12).** La dimensión efectiva impresa, Σₖ (1/(N−k)) Σ_{l≥k} t_l, divide entre cero en k = N. Solo con 1/(N−k+1) se cumplen las cotas 1 ≤ d ≤ N que enuncia el mismo párrafo.
3. **La *g* sin regularizar engaña.** Con nuestros kernels da entre 306 y 388 a c = 1, casi el valor de K_Q = I, que es 1/√λ_min(K_C) ≈ 410. Mide el condicionamiento del RBF, no la codificación, y sugeriría una ventaja que el criterio del paper descarta.

**Otra trampa, encontrada al calcular la KTA.** Para K = I, la KTA centrada vale exactamente 1/√(n−1) ≈ 0.071 con cualquier etiquetado; la sin centrar, 1/√n. Centrar no elimina el piso de los kernels casi identidad. Las KTA crudas de kernels con espectros tan distintos no son comparables entre sí: lo que se compara es el exceso sobre la media de la permutación. La primera versión del texto de `6_Separability` afirmaba lo contrario y se corrigió antes de concluir.

**Impacto.** Cierra el pendiente de H-033. D-032 adopta el protocolo y D-033 fija las demás definiciones.

**Datos.** `Code/6_Separability.ipynb`, sección 2°a; el PDF está en la carpeta de descargas del autor y no se versiona.

---

### H-039 · A c = 1 los kernels cuánticos apenas ven las clases, ocupan casi todo el espacio y quedan a g ≈ 1.4–1.7 del modelo clásico más cercano
**Fecha:** 2026-10-06 · **→ Reporte:** §6.x, OE-3, OE-6

| 200 lesiones de train por subconjunto, c = 1 | Masas | Calcificaciones |
|---|---|---|
| Exceso de KTA centrada sobre la permutación, RBF (D-027) | 0.049 | 0.152 |
| Lo mismo, C4 / C5 | 0.003 / 0.005 | 0.006 / 0.007 |
| Dimensión efectiva, RBF | 2.8 | 2.6 |
| Lo mismo, C4 / C5 (de 200) | 184 / 171 | 188 / 168 |
| *g* al modelo clásico más cercano, C4 / C5 | 1.43 / 1.51 | 1.40 / 1.70 |
| Lo mismo con la malla extendida | 1.31 / 1.48 | 1.38 / 1.70 |
| *g* sin regularizar contra el RBF de D-027, C4 / C5 | 306 / 309 | 376 / 388 |
| √N | 14.1 | 14.1 |

**Lecturas.**

1. **Alineamiento.** El exceso de los kernels cuánticos es significativo (p ≤ 0.003) pero pequeño: entre el 4 % y el 10 % del exceso del RBF. Leída en crudo, la KTA diría lo contrario en masas (0.073 de C4 contra 0.059 del RBF), pero 0.071 es el piso de cualquier kernel casi identidad (H-038).
2. **Dimensión.** Con d ≈ N, cada lesión parece no relacionada con las demás: es el régimen *"all inputs are too far apart"*. Por la ecuación (8) del paper, la cota de error del método de kernel cuántico crece con √(min(d, Tr O²)/N), así que no da garantía de generalización.
3. ***g* ≪ √N.** Es el caso de la primera prueba del diagrama de flujo (Fig. 1) en que el aprendizaje clásico predice igual o mejor, sea cual sea el etiquetado.
   - El modelo clásico más cercano es el gaussiano más estrecho de la malla (γ ≈ 6.3–6.8, λ = 0.01), un kernel clásico que también trata a las lesiones como casi aisladas.
   - El mínimo cae en el borde de la malla, y la malla extendida lo baja: la conclusión se refuerza.
4. **Barrido de c.** A c = 0.02, el exceso de KTA sube a 0.043 en masas y a 0.143 en calcificaciones (contra 0.049 y 0.152 del RBF), d baja a ~4 y *g* queda entre 2.1 y 2.5. El máximo de *g* en todo el barrido es 3.1 (C5, c = 0.5). Lo que se recupera es lo que ya ve el kernel clásico (H-031). En C5, d y *g* no son monótonos en c, como sus medianas (H-037).
5. **El RBF de D-027** no tiene ningún λ admisible para c ≥ 0.05: un kernel clásico suave no puede imitar a los cuánticos sin un error de entrenamiento grande.

**Impacto.** Es la respuesta del OE-3 en la familia de kernels: con el diseño preregistrado no hay indicio de ventaja cuántica potencial. Coincide con el AUC de pares de X2 (H-036). Bajo la regla 1 del proyecto es un resultado de viabilidad.

**Datos.** `Code/6_Separability.ipynb` (3°); `Code/results/6_alineamiento_kernel.csv`, `6_dimension_efectiva.csv`, `6_diferencia_geometrica.csv` y `6_diferencia_geometrica_resumen.csv`; figuras `Docs/Figures/M6_kernel_metrics.png` y `M6_geometric_difference.png`.

---

### H-040 · Los embeddings cuánticos son menos separables que los clásicos, y C4 frente a C5 no tiene ganador
**Fecha:** 2026-10-06 · **→ Reporte:** §6.x, OE-3

| Submuestra de 200 | C1 = C2 | C3 | C4 | C5 |
|---|---|---|---|---|
| Fisher J, masas | 0.67 | 0.78 | 0.45 (p = 0.05) | 0.67 |
| Fisher J, calcificaciones | 1.28 | 1.39 | 0.40 (p = 0.15) | 0.75 |
| Davies-Bouldin, masas (menor es mejor) | 4.30 | 5.56 | 5.90 | 13.35 (p = 0.41) |
| Davies-Bouldin, calcificaciones | 2.39 | 2.99 | 6.89 | 6.25 |
| KTA lineal, masas | 0.070 | 0.059 | 0.041 | 0.012 (p = 0.41) |
| KTA lineal, calcificaciones | 0.181 | 0.161 | 0.031 | 0.041 |
| Fisher J sobre todo el train, masas | 0.45 | 0.44 | 0.13 | 0.21 |
| Fisher J sobre todo el train, calcificaciones | 1.06 | 1.00 | 0.42 | 0.31 |

**Lecturas.**
1. **Las representaciones clásicas van delante en las tres métricas y en ambos subconjuntos.** Sobre todo el train (1,318 masas y 1,546 calcificaciones) todas las métricas son significativas y el orden se mantiene.
2. **En la submuestra, dos métricas de C5 en masas no se distinguen del azar:** Davies-Bouldin y la KTA lineal, ambas con p = 0.41. Su embedding está más disperso que el de C4 (H-037), pero esa dispersión no sigue a las clases.
3. **C4 frente a C5 no tiene un ganador consistente.** C5 va delante en el Fisher de la submuestra y en el de masas sobre todo el train, y detrás en el de calcificaciones sobre todo el train y en el Davies-Bouldin de masas.
4. **El control nulo funciona:** C1 y C2 coinciden con una diferencia de 10⁻¹⁴ en todas las métricas (D-016).

**Impacto.**
- **Las dos familias coinciden en la dirección, no en el detalle** (H-013, H-037). Ambas ponen delante a las representaciones clásicas. Pero C5 tiene solapamientos típicos menores que C4 y, aun así, una dimensión efectiva menor (171 contra 184 en masas), compatible con la distribución más ancha de sus valores de kernel en 5b.
- **Anticipa el M7, pero no lo predice:** el MLP puede aprovechar estructura local que estas métricas globales no ven.
- **La conclusión del OE-3 queda pendiente de Q-013.** *Actualizado el 2026-10-06: con k = 8 se mantiene (H-041).*

**Datos.** `Code/6_Separability.ipynb` (4°); `Code/results/6_metricas_embedding.csv`; figuras `Docs/Figures/M6_embedding_metrics.png` y `M6_tsne.png`.

---

### H-041 · Con 8 qubits la concentración baja y los kernels cuánticos ven algo más las clases, pero la conclusión del M6 se mantiene
**Fecha:** 2026-10-06 · **→ Reporte:** §6.x, §7, OE-3, OE-6 · *cierra Q-013; confirma H-018 sobre datos reales*

**Qué cambia con k = 8.**
- **Las features.** Son las 8 primeras de las 12 de M4, porque la selección es voraz, y sus ángulos son idénticos, porque el escalado por cuantiles actúa feature por feature; ambas cosas se verificaron. En masas salen tres de textura y una de primer orden (`GrayLevelNonUniformity`, `10Percentile`, `Correlation`, `RunLengthNonUniformity`), y quedan 3 de primer orden y 5 de forma. En calcificaciones salen `DifferenceEntropy`, `Energy`, `ClusterShade` y `PixelSurface`.
- **Los circuitos.** Tienen 28 bloques ZZ en lugar de 66, y el ansatz tiene 16 parámetros, que son los primeros 16 del mismo flujo de la semilla 42.

| c = 1, 200 lesiones | Masas, k = 12 | Masas, k = 8 | Calcif., k = 12 | Calcif., k = 8 |
|---|---|---|---|---|
| Mediana del kernel, C4 / C5 | 0.002 / 0.00003 | 0.010 / 0.0015 | 0.003 / 0.00003 | 0.008 / 0.0008 |
| Dimensión efectiva, C4 / C5 (de 200) | 184 / 171 | 140 / 103 | 188 / 168 | 170 / 131 |
| Exceso de KTA, C4 / C5 | 0.003 / 0.005 | 0.012 / 0.023 | 0.006 / 0.007 | 0.011 / 0.024 |
| Exceso de KTA del RBF | 0.049 | 0.049 | 0.151 | 0.150 |
| *g* mínima, C4 / C5 (√N = 14.1) | 1.43 / 1.51 | 2.40 / 3.23 | 1.40 / 1.70 | 1.71 / 2.16 |
| Dispersión del embedding, C4 / C5 | 0.057 / 0.180 | 0.099 / 0.276 | 0.048 / 0.178 | 0.076 / 0.267 |
| Fisher J sobre todo el train, C1 / C4 / C5 | 0.45 / 0.13 / 0.21 | 0.37 / 0.09 / 0.17 | 1.06 / 0.42 / 0.31 | 0.98 / 0.29 / 0.37 |

**Lecturas.**
1. **H-018 se confirma sobre datos reales.** Con menos qubits el kernel y el embedding se concentran menos; la dispersión de C4 casi se duplica.
2. **Los kernels cuánticos ven algo más las clases, sin alcanzar al clásico a c = 1.** El exceso de KTA crece entre 1.7 y 4.6 veces. Lo más alto es C5 en masas, con la mitad del exceso del RBF; en calcificaciones C5 llega al 16 %.
   - Solo a escalas pequeñas igualan al RBF: a c = 0.05 en masas y a c = 0.02 en calcificaciones, la diferencia es de 0.009 o menos, como mucho 1.3 desviaciones de la permutación.
   - A esas escalas el término de producto ya no influye (H-031).
3. ***g* sube un poco y sigue pequeña.** Va de 1.7 a 3.2 a c = 1 y llega como máximo a 4.6 en todo el barrido, siempre muy por debajo de √N.
4. **Los embeddings conservan el orden.** C1–C3 siguen muy por delante en todas las métricas y en ambos subconjuntos. Menos features también le cuestan a lo clásico: el Fisher de C1 baja de 0.45 a 0.37 en masas. La razón entre cuántico y clásico no mejora de forma sistemática:
   - C5/C1 pasa de 0.47 a 0.45 en masas y de 0.29 a 0.38 en calcificaciones;
   - C4/C1 baja en ambos subconjuntos.

   C5 mejora en Davies-Bouldin y en KTA lineal y C4 empeora, en línea con la dispersión que aporta el término Y (H-037).
5. **La prueba de regresión reproduce exactamente el M6** para k = 12, con una diferencia máxima de 3×10⁻¹⁴. Pasan 29 de 29 verificaciones.

**Impacto.**
- **La conclusión del OE-3 no depende de k = 12.** Con el diseño preregistrado, las transformaciones cuánticas no dan mayor separabilidad que las clásicas, ni con 12 ni con 8 qubits.
- **Material del OE-6.** La concentración tiene un coste medible: con 4 qubits menos, el alineamiento cuántico explicado por las etiquetas se multiplica por 1.7 a 4.6, aunque el punto de partida es muy bajo.
- **Alcance.** El cambio de k también cambia las features. El contraste mide el efecto conjunto del tamaño del registro y de las 4 features que k = 12 añade. En masas, esas 4 incluyen las tres de textura, así que con k = 8 no queda ninguna (cf. H-026).

**Datos.** `Code/experiments/X3_Fewer_Qubits_k8.ipynb`; `Code/results/X3_comparacion_k8_k12.csv`, `X3_alineamiento_kernel.csv`, `X3_dimension_efectiva.csv`, `X3_diferencia_geometrica_resumen.csv`, `X3_metricas_embedding.csv` y `X3_verificaciones.csv`; figuras `Docs/Figures/X3_kernel_metrics_k8_k12.png` y `X3_embedding_metrics_k8_k12.png`.

---

### H-042 · El mismo MLP clasifica peor sobre las representaciones cuánticas: de 0.07 a 0.14 menos de AUC en el test
**Fecha:** 2026-10-06 · **→ Reporte:** §6.x, OE-4, OE-5

| AUC-ROC | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|
| Masas, validación cruzada | 0.652 | 0.641 | 0.648 | 0.565 | 0.563 |
| Masas, test [IC 95 % por paciente] | 0.651 [0.58, 0.72] | 0.641 | 0.646 | 0.530 [0.47, 0.59] | 0.581 [0.52, 0.64] |
| Calcificaciones, validación cruzada | 0.742 | 0.758 | 0.739 | 0.640 | 0.667 |
| Calcificaciones, test | 0.769 [0.69, 0.84] | 0.788 | 0.758 | 0.633 [0.56, 0.70] | 0.652 [0.57, 0.73] |

**Lecturas.**
1. **Diferencias pareadas en el test frente a C1.**
   - Masas: −0.12 para C4 [−0.20, −0.04] y −0.07 para C5 [−0.14, −0.004].
   - Calcificaciones: −0.14 para C4 [−0.21, −0.06] y −0.12 para C5 [−0.18, −0.05].

   Frente a C3 el resultado es el mismo, salvo C5 en masas, cuyo intervalo roza el cero: −0.065 [−0.14, 0.002]. C4 en masas no se distingue del azar en el test.
2. **El control nulo funciona.** C2 − C1 da −0.011 [−0.06, 0.04] en masas y +0.020 [−0.03, 0.07] en calcificaciones: una rotación no cambia el resultado.
3. **C5 frente a C4.** C5 va delante en casi todos los análisis (las excepciones son dos corridas de validación cruzada de masas, con las semillas 42 y 44), pero sin una diferencia significativa: en masas, 0.051 [−0.03, 0.13] en el test.
4. **Coherente con el M6.** El orden coincide con el de la separabilidad: las condiciones clásicas van delante en ambas familias de métricas (H-039, H-040). La correlación formal entre ambos rankings (RF-21) corresponde al M8.

**Impacto.** Es la respuesta del OE-4 y el OE-5 con el diseño preregistrado: no hay mejora de clasificación atribuible a la transformación cuántica, y sí una pérdida significativa.

**Datos.** `Code/7_Classification.ipynb` (3°); `Code/results/7_cv_por_fold.csv`, `7_cv_resumen.csv`, `7_test.csv` y `7_test_diferencias.csv`; figuras `Docs/Figures/M7_auc.png` y `M7_roc_test.png`.

---

### H-043 · El resultado del M7 resiste semillas, red, escalado, parada temprana, reps = 2 y k = 8
**Fecha:** 2026-10-06 · **→ Reporte:** §6.x, §7, OE-6 · *corrige la lectura de H-018 sobre datos reales*

**Lecturas.**
1. **Semillas.** El AUC medio de una condición en validación cruzada se mueve como mucho 0.039 entre las cinco semillas. Es menos de la mitad de la brecha entre clásico y cuántico, que ronda 0.08–0.10.
2. **Configuraciones.** La red 16-8, la red 64-32 y las entradas sin estandarizar no cambian el orden.
3. **Entrenar más no ayuda a lo cuántico.** Con 200 épocas sin parada temprana, C4 y C5 pierden AUC (0.533 y 0.557 en masas; 0.596 y 0.631 en calcificaciones), mientras las clásicas se mantienen o ganan (C1 en masas: 0.680). Los ajustes cuánticos que paran pronto lo hacen porque su pérdida de validación deja de mejorar, no por falta de entrenamiento.
4. ***Ansatz* con dos capas.**
   - **Dispersión.** Sobre datos reales y con el θ del diseño, la dispersión de C4 baja (de 0.058 a 0.047 en masas) y la de C5 sube (de 0.180 a 0.196). El +30 % de H-018 venía de entradas sintéticas promediadas sobre sorteos de θ y no se reproduce aquí para C4.
   - **Clasificación.** C5 mejora (en el test, de 0.581 a 0.603 en masas y de 0.652 a 0.682 en calcificaciones), con intervalos que contienen el cero, y sigue por debajo de C1: −0.048 [−0.093, −0.005] y −0.086 [−0.141, −0.034]. C4 no cambia.
5. **k = 8.** Las condiciones clásicas apenas cambian. C4 empeora en calcificaciones: 0.561 en el test, con una diferencia de −0.07 [−0.14, 0.00] frente a k = 12. C5 se mantiene. Las cuánticas quedan entre 0.07 y 0.19 por debajo de C1 en el test.
   - Con k = 8 las métricas de kernel de C4 mejoraron (H-041) y su clasificación empeoró: otro caso de H-013. Un embedding más disperso no es necesariamente más informativo.

**Impacto.**
- La conclusión del M7 no depende del procedimiento de entrenamiento, de la profundidad del *ansatz* ni del número de qubits.
- Descarta la objeción del subentrenamiento.
- Matiza H-018: la dispersión del embedding no se traduce en clasificación, y con el θ del diseño reps = 2 ni siquiera dispersa más a C4.

**Datos.** `Code/7_Classification.ipynb` (4° a 7°); `Code/results/7_cv_por_fold.csv` y `7_test_diferencias.csv`; figura `Docs/Figures/M7_sensitivity.png`.

---

### H-044 · Un QSVM sobre el kernel de C4 iguala al SVM clásico y supera al MLP sobre los ⟨Zᵢ⟩: la información se pierde en la lectura, no en la codificación
**Fecha:** 2026-10-07 · **→ Reporte:** §6.x, §7 · *matiza H-039 y H-042*

| AUC en el test [IC 95 % por paciente] | Masas | Calcificaciones |
|---|---|---|
| SVM RBF (D-027) | 0.649 [0.57, 0.73] | 0.769 [0.70, 0.83] |
| QSVM C4, c = 1 | 0.628 [0.55, 0.70] | 0.759 [0.69, 0.83] |
| QSVM C5, c = 1 | 0.599 [0.52, 0.68] | 0.701 [0.62, 0.78] |
| MLP sobre los ⟨Zᵢ⟩ de C4 (M7) | 0.530 [0.47, 0.59] | 0.633 [0.56, 0.70] |

**Lecturas.**
1. **La codificación conserva casi toda la información de clase.**
   - QSVM C4 − SVM RBF: −0.02 [−0.05, 0.01] en masas y −0.01 [−0.04, 0.02] en calcificaciones; no se distinguen.
   - QSVM C4 − MLP sobre ⟨Zᵢ⟩: +0.10 [0.03, 0.17] y +0.13 [0.05, 0.20].

   La pérdida del M7 viene sobre todo de la lectura de la Arquitectura B: 12 valores ⟨Zᵢ⟩ tras un *ansatz* fijo, extraídos de un estado de 4,096 amplitudes. Es el caso más concreto de H-013.
2. **Las métricas globales del M6 no veían esa estructura.** El QSVM conserva prácticamente todas las lesiones de entrenamiento como vectores de soporte (fracción 1.00 y 0.998), como corresponde a un kernel casi identidad. Decide con los pocos pares que sí se solapan, una estructura local demasiado escasa para la KTA y el AUC de pares, que promedian sobre todos los pares. Ya estaba anotado como límite en H-036.
3. **No hay ventaja.** Eligiendo c por validación cruzada, C4 iguala al mejor kernel clásico en el test: −0.002 en masas (c = 0.05) y −0.005 en calcificaciones (c = 0.2). C5 queda significativamente por debajo a c = 1 (−0.05 y −0.07). C no cambia nada. Es lo que predice *g* ≈ 1.4 ≪ √N, porque el resultado de Huang et al. habla justamente de métodos de kernel.

**Impacto.**
- La conclusión del OE-3 se mantiene: no hay ventaja.
- Su explicación se precisa: la codificación ZZ equivale a un kernel clásico, y la Arquitectura B pierde información al leerla.
- Ante los sinodales, esto responde a «¿por qué no un QSVM?».
- La Arquitectura B se eligió por justicia y por coste (D-014), así que esta pérdida es un precio de esa elección que hay que declarar en §7.

**Datos.** `Code/experiments/X4_QSVM_and_67_Features.ipynb`; `Code/results/X4_*.csv`; figuras `Docs/Figures/X4_qsvm_vs_readout.png` y `X4_qsvm_scale.png`.

---

### H-045 · Con las 67 features tampoco hay ventaja: los kernels cuánticos simulables son clásicos o se concentran
**Fecha:** 2026-10-07 · **→ Reporte:** §7, OE-6

**Lecturas.**
1. **El techo clásico apenas sube.** Un SVM RBF sobre las 67 features rinde 0.649 en masas (−0.001 frente a las 12) y 0.787 en calcificaciones (+0.02 [−0.02, 0.06]). Coincide con X1.
2. **Codificación en amplitudes (7 qubits).**
   - Su kernel es exactamente el cuadrado de la similitud coseno, un kernel polinomial clásico de grado 2; se verificó con una diferencia de 2×10⁻¹⁶.
   - En calcificaciones da el AUC más alto del experimento, 0.795 [0.73, 0.85], pero no es cuántico en ningún sentido útil y no supera significativamente al RBF (+0.008).
   - En masas queda por debajo: −0.05 [−0.10, 0.00].
3. **Codificación angular producto (67 qubits).** A c = 1 se concentra por completo: la mediana fuera de la diagonal es 0.0000 y todas las lesiones quedan como vectores de soporte. Al reducir los ángulos, Π cos²(cΔᵢ) ≈ exp(−c²‖Δ‖²) se convierte en un kernel gaussiano y rinde lo mismo que el RBF.
4. **Lo que no se puede simular.** Un mapa ZZ sobre 67 qubits, que sí sería difícil de calcular clásicamente, necesitaría 2⁶⁷ ≈ 1.5×10²⁰ amplitudes.

**Impacto.** Más features no abren una ventaja. Los kernels cuánticos que admiten 67 features y se pueden simular son clásicos de hecho. Los que no lo son no se pueden evaluar en un simulador, y sus valores serían irresolubles en hardware por la concentración. Material directo del OE-6.

**Datos.** `Code/experiments/X4_QSVM_and_67_Features.ipynb` (4°); `Code/results/X4_67_features.csv`; figura `Docs/Figures/X4_67_features.png`.

---

### H-046 · La auditoría independiente del pipeline no encuentra errores
**Fecha:** 2026-10-07 · **→ Reporte:** §8.x, §7

**Qué se revisó, con implementaciones independientes de las de los módulos.** Pasan las 25 verificaciones.
- **Etiquetas y particiones:** reconstruidas desde los cuatro CSV originales sin pasar por M1. Coinciden en las 3,568 lesiones.
- **Fuga de información:** al reajustar M4 solo con el train, los ángulos del test salen idénticos (10⁻¹²), y ningún paciente queda repartido.
- **Kernel cuántico:** `FidelityQuantumKernel`, por circuitos *compute-uncompute*, coincide con el kernel de vectores de estado (6×10⁻¹¹).
- **QSVM:** la clase `QSVC` de `qiskit-machine-learning` da decisiones idénticas al SVM del X4.
- **Codificación:** cada ángulo actúa sobre su qubit, y reordenar las features deja invariante el kernel con entrelazamiento completo.
- **Referencias clásicas:** el MLP, el SVM y la regresión logística coinciden dentro del ruido de los folds.

**Impacto.** Descarta que un error de implementación esconda una ventaja. Lo que la auditoría no puede descartar son decisiones de diseño (la codificación, la lectura, la selección), y esas son las que varían el X4 y el X6.

**Además.** El notebook deja cuatro preguntas para leer los trabajos que reportan ventaja:
1. ¿El clasificador clásico recibió el mismo ajuste y las mismas features?
2. ¿La diferencia supera su incertidumbre?
3. ¿El test se usó una sola vez?
4. ¿El kernel cuántico es realmente difícil de calcular clásicamente?

Hay que aplicarlas a los artículos citados en §2 antes de redactar §2 y §7.

**Datos.** `Code/experiments/X5_Pipeline_Audit.ipynb`; `Code/results/X5_auditoria.csv`.

---

### H-047 · Con la misma búsqueda anidada en ambos lados, ningún kernel cuántico supera a los clásicos en las etiquetas reales
**Fecha:** 2026-10-07 · **→ Reporte:** §6.x, §7 · *protocolo de D-038*

**Qué se probó (X6).**
- **Lado cuántico:** mapas ZZ con entrelazamiento completo y lineal, con 1 y 2 repeticiones y en todo el barrido de c, y kernels proyectados (Huang et al., ec. 9) sobre ⟨X⟩, ⟨Y⟩ y ⟨Z⟩ de cada qubit.
- **Lado clásico:** gaussianos, lineal y polinomiales.
- **Selección:** validación cruzada anidada con los folds de M4 (3 folds internos por paciente) y SVM con C = 1.
- **Test:** uno por contendiente global.

| | Masas | Calcificaciones |
|---|---|---|
| CV anidada: clásico / cuántico | 0.677 / 0.651 | 0.745 / 0.753 |
| Diferencia en CV anidada | −0.027 [−0.043, −0.009] | +0.007 [−0.007, 0.023] |
| Test: clásico / cuántico | 0.652 / 0.656 | 0.760 / 0.755 |
| Diferencia en el test | +0.004 [−0.023, 0.033] | −0.005 [−0.032, 0.022] |

**Lecturas.**
1. **Lo mejor que logra lo cuántico es la equivalencia.** Elige el mapa ZZ completo con c pequeño (0.05 y 0.2), el régimen en que el término de producto ya no influye (H-031).
2. **Hipótesis refutada: el entrelazamiento lineal no reduce la concentración; la aumenta.** La mediana del kernel es 0.0001, frente a 0.002 con el completo. El razonamiento de la fase por qubit era incompleto: con menos acoplamientos el estado se acerca a uno producto, cuya fidelidad es un producto de solapamientos de un qubit, el término más concentrado de todos (5b, 6c).
3. **Los kernels proyectados hacen lo que dicen Huang et al. y no ayudan.**
   - Suben *g* de ~1.4 a 6–9, con una dimensión efectiva de ~10.
   - Son las peores familias cuánticas en las etiquetas reales: −0.11 en masas y −0.06 en calcificaciones frente a lo clásico.
   - Una *g* grande es necesaria, no suficiente.

**Datos.** `Code/experiments/X6_Searching_for_Advantage.ipynb` (2° a 4°); `Code/results/X6_rejilla_candidatos.csv`, `X6_anidada.csv`, `X6_diferencias.csv`, `X6_test.csv` y `X6_geometria.csv`; figura `Docs/Figures/X6_nested_auc.png`.

---

### H-048 · Etiquetas construidas según el Apéndice G dan una ventaja cuántica grande sobre las mismas lesiones: la ausencia de ventaja es una propiedad de la tarea
**Fecha:** 2026-10-07 · **→ Reporte:** §7, §2 (lectura de la literatura), OE-3, OE-6

**Método.** Con el kernel cuántico K_Q y el clásico más cercano K_C, ambos sobre todo el train, se construye y = √K_Q·v (Apéndice G, ecs. G3–G4). Luego se binariza por la mediana y se compara el QSVM con el **mejor** SVM clásico elegido por validación cruzada.

| CV AUC | Etiquetas construidas: QSVM / mejor clásico | Etiquetas reales: QSVM / mejor clásico |
|---|---|---|
| Masas, kernel proyectado | **0.998 / 0.800** | 0.566 / 0.682 |
| Calcificaciones, kernel proyectado | **0.994 / 0.824** | 0.667 / 0.759 |
| Masas, ZZ completo (C4) | 0.730 / 0.712 | 0.657 / 0.682 |
| Calcificaciones, ZZ completo (C4) | 0.829 / 0.807 | 0.752 / 0.759 |

**Lecturas.**
1. **Sobre estas mismas lesiones y features existen etiquetas para las que un kernel cuántico gana con mucha ventaja.** Es el tipo de resultado que la literatura reporta: tareas cuyas etiquetas siguen la geometría del kernel cuántico.
2. **Con el mapa ZZ completo, ni las etiquetas más favorables dan más que una ventaja pequeña**, porque su *g* es pequeña.
3. **Las etiquetas del diagnóstico no siguen esa geometría.** Para los mapas ZZ, el cociente s_C/s_Q de las etiquetas reales queda cerca de 1 (0.85 a 1.21). Para el kernel proyectado ese cociente no es interpretable, porque su matriz es casi singular; ahí la lectura válida es la de los AUC.

**Impacto.**
- **Responde la duda del autor.** La literatura tiene razón en que hay ventajas, pero en tareas cuyas etiquetas siguen la geometría cuántica. El benigno/maligno medido con features radiómicas no la sigue.
- **No es un error:** la auditoría (H-046) lo descarta.
- **Es la conclusión más fuerte para §7.** La ausencia de ventaja es una propiedad de la tarea, medida y no supuesta, y el mismo protocolo detecta una ventaja cuando existe.
- **Para leer la literatura:** cuando un trabajo reporta ventaja, la pregunta es si sus etiquetas tienen esa estructura o si la comparación es asimétrica (H-046).

**Datos.** `Code/experiments/X6_Searching_for_Advantage.ipynb` (5°); `Code/results/X6_etiquetas_construidas.csv`; figura `Docs/Figures/X6_built_labels.png`.

---

### H-049 · Los rankings de separabilidad y de clasificación coinciden en lo esencial: las tres condiciones clásicas van delante de las dos cuánticas en todos
**Fecha:** 2026-10-07 · **→ Reporte:** §6.x, OE-5, RF-21 · *protocolo de D-039*

| ρ_s primario (submuestra de 200 frente al AUC del test, k = 12) | Davies-Bouldin | Fisher J | KTA lineal |
|---|---|---|---|
| Masas | 0.72 (p = 0.17) | 0.82 (p = 0.13) | 0.72 (p = 0.17) |
| Calcificaciones | 0.97 (p = 0.033) | 0.67 (p = 0.27) | 0.97 (p = 0.033) |

**Lecturas.**
1. **Los 48 coeficientes son positivos, entre 0.67 y 0.97.** Cubren tres métricas, dos muestras, dos evaluaciones, dos subconjuntos y dos valores de k.
2. **En todos, ambos rankings ponen a C1–C3 por encima de C4 y C5.** El acuerdo está en esa partición.
3. **Dentro de cada bloque, el orden es ruido.** C1 y C2 solo difieren en AUC por el ruido del entrenamiento (D-016), y C4 frente a C5 nunca fue significativo (H-042).
4. **Cinco de los 48 valores bajan de p = 0.05.** Son justo el mejor orden alcanzable con el empate C1 = C2: ρ_s = 0.975, con p = 4/120. Se leen como acuerdo, no como prueba (D-039).
5. **En la familia de kernels** (tres objetos, sin prueba posible), el RBF va primero tanto en alineamiento como en el AUC del SVM del X4. C4 y C5 se intercambian, pero sus excesos de KTA difieren en menos de 0.003.

**Impacto.**
- **Responde el OE-5.** Separabilidad y clasificación ordenan igual a las condiciones.
- **La premisa de la hipótesis no se cumple.** La transformación cuántica no mejoró la separabilidad (H-039, H-040), y la menor separabilidad de C4 y C5 viene seguida de menor AUC. La correlación avala a las métricas del M6 como predictoras; no avala una ventaja.
- **Corrección para §3.4.** La ecuación `spearman` del reporte, 1 − 6Σd²/(n(n²−1)), solo vale sin empates. Con el empate C1 = C2 se usa la correlación de Pearson de los rangos promedio.

**Datos.** `Code/8_Comparison.ipynb` (3°); `Code/results/8_spearman.csv`, `8_spearman_nula.csv`, `8_rangos.csv` y `8_rangos_kernel.csv`; figuras `Docs/Figures/M8_spearman.png` y `M8_spearman_null.png`.

---

### H-050 · Con los descriptores del radiólogo las masas son el subconjunto más separable; con las features radiómicas, el menos: la inversión respecto al EDA está en las features
**Fecha:** 2026-10-07 · **→ Reporte:** §5 (hallazgos del EDA), §6.x, §7 · *referencia de D-040*

| AUC en validación cruzada, regresión logística | Masas | Calcificaciones |
|---|---|---|
| Descriptores del radiólogo (forma y márgenes; tipo y distribución) | **0.872** | 0.825 |
| Las 67 features radiómicas (X1) | 0.693 | **0.800** |
| Los 12 ángulos de M4 | 0.668 | 0.745 |

**Lecturas.**
1. **El EDA acertó sobre las clases.** En el vocabulario del radiólogo, las masas son más separables, como anticipaban la forma y los márgenes.
2. **Las features invierten el orden.**
   - En calcificaciones, las 67 features recuperan casi todo lo que llevan los descriptores: 0.800 contra 0.825.
   - En masas, mucho menos: 0.693 contra 0.872.
   - La debilidad de las masas es, por tanto, una propiedad de las features y no de las clases.
3. **Hipótesis, no hallazgo.** Los márgenes (espiculados, mal definidos) son detalles del borde, y las features del M3 resumen toda la región y el contorno de la máscara. Comprobarlo requeriría features específicas del margen, y este trabajo no lo hace.
4. **La penalización cuántica es la misma en ambos subconjuntos.** C4 − C1 vale −0.12 en masas y −0.14 en calcificaciones. La geometría del kernel también es igual:
   - mediana de 0.002–0.003 en C4 y de 0.00003 en C5;
   - *g* de 1.4 a 1.7.

   Lo que cambia entre subconjuntos es la señal clásica, no la codificación cuántica.

**Advertencia.** Los descriptores son una referencia, no un competidor: los escribió un radiólogo viendo la imagen, y ningún sistema automático los tiene al predecir. Se excluyeron `assessment` (BI-RADS) y `subtlety`.

**Datos.** `Code/8_Comparison.ipynb` (4°); `Code/results/8_descriptores_radiologo.csv` y `8_masas_vs_calcificaciones.csv`.

---

### H-051 · En esta máquina, el simulador admite unos 25 qubits para el embedding y 22 para el kernel; el techo que condicionó el diseño fue el gradiente, no el número de qubits
**Fecha:** 2026-10-07 · **→ Reporte:** §6.x, §8.x, OE-6, RF-22 · *completa H-011 y H-032*

**Método.** Se cronometró un estado del circuito de C4 con `AerSimulator` (statevector) para k par de 8 a 28, en una Apple M3 con 16 GiB. Con esos tiempos se proyectaron cuatro tareas como cotas inferiores (D-040).

| Tarea | Mayor k viable |
|---|---|
| Un estado en memoria (16 bytes × 2^k, hasta la mitad de la RAM) | 29 |
| Embedding de todas las lesiones en 24 h | 25 |
| Kernel de 200 × 200 por *compute-uncompute* en 24 h (la vía del hardware) | 22 |
| Kernel de 200 × 200 con el atajo del vector de estado, con todos los estados en memoria | 21 |
| Entrenar θ por *parameter-shift*, 50 épocas, un mapa, en 24 h (cota inferior) | 14 |

**Lecturas.**
1. **Tiempo por muestra a k = 12.** El mismo estado se calcula por tres vías:
   - 3 ms con `AerSimulator`;
   - 8 ms con el vector de estado directo del M5;
   - 93 ms a través de `EstimatorQNN` (B1).

   La diferencia entre las tres es sobrecarga de la primitiva, no física.
2. **El coste crece como 2^k.**
   - Por encima de 20 qubits, el tiempo crece unas 1.9 veces por qubit añadido.
   - A k = 28 la medición (75 s por estado, 5.4 veces la de 26) queda por encima de la tendencia, probablemente por presión de memoria; no se verificó.
   - Una primera ejecución del mismo barrido dio 152 s a k = 28 y límites de 26, 23 y 15. Los tiempos de los estados grandes dependen de la carga de la máquina, así que los límites tienen una incertidumbre de un qubit.
3. **El *parameter-shift* es lo caro.** Necesita 48 evaluaciones por lesión a k = 12 (4.7 s) y unas 191 h por *feature map* para 50 épocas (B1). La Arquitectura B, unas 1,900 veces más rápida, era la única factible (D-014, H-011).
4. **k = 12 está lejos de todos los límites.**

**Impacto.** Material directo del OE-6. Cumple la parte de RF-22 sobre el tiempo por muestra, el máximo de qubits y el coste del *parameter-shift*. RNF-07, que pide k ∈ [8, 16] con entrenamiento, solo es alcanzable sin entrenar θ.

**Datos.** `Code/8_Comparison.ipynb` (5° a–d); `Code/results/8_oe6_qubits.csv` y `8_oe6_resumen.csv`; figura `Docs/Figures/M8_oe6_qubits.png`.

---

### H-052 · Con 1,024 shots el MLP recupera casi todo el AUC exacto, pero el kernel cuántico no se puede medir: a c = 1, entre el 16 y el 74 % de sus valores leería 0
**Fecha:** 2026-10-07 · **→ Reporte:** §3.x (medición), §6.x, §7, OE-6, RF-22, RNF-05 · *completa H-019 y H-037*

**Embedding.**

| | C4 masas | C4 calcificaciones | C5 masas | C5 calcificaciones |
|---|---|---|---|---|
| Ruido / dispersión entre lesiones, 1,024 shots | 0.55 | 0.65 | 0.17 | 0.17 |
| Shots para que el ruido sea el 10 % de la dispersión | 31,000 | 44,000 | 2,900 | 3,000 |
| AUC de validación cruzada, 1,024 shots (exacto) | 0.548 (0.565) | 0.630 (0.640) | 0.565 (0.563) | 0.654 (0.667) |

**Kernel, c = 1.** En hardware, cada valor del kernel es la probabilidad de leer la cadena de ceros.

| | C4 masas | C4 calcificaciones | C5 masas | C5 calcificaciones |
|---|---|---|---|---|
| Entradas que leen exactamente 0, 1,024 shots por par | 21 % | 16 % | 74 % | 72 % |
| Lo mismo con 8,192 shots | 2.5 % | 1.5 % | 57 % | 56 % |
| Mediana de shots por par para un error relativo del 10 % | 46,000 | 35,000 | 3.1 millones | 3.2 millones |

**Lecturas.**
1. **El clasificador tolera el ruido mejor que las coordenadas.**
   - Con 1,024 shots, el mínimo de RNF-05, el AUC queda a menos de 0.02 del exacto en los cuatro casos.
   - Con 64 shots pierde hasta 0.08 (calcificaciones, C4).
2. **C5 es entre 10 y 15 veces más barato de medir que C4.**
   - La varianza de la estimación es (1 − ⟨Z⟩²)/n, así que los shots necesarios crecen como 1/dispersión².
   - C5 se dispersa tres veces más (H-037).
3. **El kernel es lo que fallaría en hardware.**
   - 58–60 % de los pares de C5 necesitan más de 10⁶ shots.
   - Achicar los ángulos (c = 0.05) baja el coste a 400–630 shots por par, pero ese es el régimen en el que el kernel se comporta como uno clásico (H-031).
4. **La concentración que dejó al kernel sin información (H-039) es la misma propiedad que lo hace imposible de medir.**

**Formalismo frente a implementación.** La ley (1 − ⟨Z⟩²)/n y el carácter binomial del valor del kernel son propiedades de la medición cuántica. El sorteo multinomial reproduce lo que haría un *sampler* ideal (H-019).

**Datos.** `Code/8_Comparison.ipynb` (5° e–h); `Code/results/8_oe6_shots_embedding.csv`, `8_oe6_shots_kernel.csv` y `8_oe6_resumen.csv`; figura `Docs/Figures/M8_oe6_shots.png`.

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

---

### Q-009 · ¿Min-max, logaritmo o cuantiles para las features de cola pesada?
**Bloquea:** M5, Fase 4 · **Límite:** antes de calcular los embeddings

H-028 muestra que el min-max deja casi constantes los ángulos de las features que crecen con el área: en calcificaciones, `Energy` y `PixelSurface` tienen un IQR de 0.05 rad. Eso puede penalizar a C3, C4 y C5 frente a C1 por el escalado y no por la codificación. Hay tres salidas, todas dentro de [0, π] (D-004):

- *(a)* conservar min-max y declararlo como limitación;
- *(b)* aplicar log a las features positivas de cola pesada antes del min-max;
- *(c)* aplicar una transformación por cuantiles a una distribución uniforme en [0, π], ajustada en train.

La *(c)* es la más homogénea, pero descarta la información de distancias dentro de cada feature. La *(b)* la conserva en escala logarítmica. Cambiar después de calcular los embeddings obligaría a repetir M5.

**Resuelta el 2026-09-23 → D-025:** transformación por cuantiles.

---

### Q-010 · ¿Semilla 42 para los folds, o una elegida por balance de clases?
**Bloquea:** M6, Fase 5 · **Límite:** antes de entrenar el MLP

H-027: con `StratifiedGroupKFold` y la semilla 42, el fold 2 de calcificaciones tiene un 52 % de malignas frente al 35 % global. Es la peor de 200 semillas. Hay dos salidas:

- *(a)* conservar la semilla 42 (RNF-01) y declarar el desbalance;
- *(b)* elegir la semilla de los folds por mínima desviación de la proporción de clases entre 200 candidatas, un criterio que solo mira las etiquetas.

La *(b)* no usa features ni rendimiento y es defendible, pero hay que declararla.

**Resuelta el 2026-09-23 → D-026:** semilla elegida por balance.

---

### Q-011 · ¿Qué se hace con el kernel cuántico concentrado?
**Bloquea:** M5 (5a en C4/C5 y 5b), Fase 4 · **Límite:** antes de despachar los workers

H-031: con el diseño actual (k=12, entrelazamiento completo, ángulos en [0, π]), el kernel de fidelidad es casi la identidad. Escalar los ángulos solo lo corrige cuando desaparecen los productos. Salidas:

- *(a)* mantener el diseño preregistrado (c = 1) como análisis principal y reportar un barrido de c como sensibilidad del OE-6;
- *(b)* adoptar un c pequeño, elegido sin mirar etiquetas, como diseño principal;
- *(c)* cambiar la codificación (entrelazamiento lineal, o productos xᵢxⱼ sin el desplazamiento de π), lo que redefine C4 y C5.

Afecta también a los embeddings ⟨Zᵢ⟩ de C4 y C5, porque usan el mismo feature map.

**Resuelta el 2026-09-24 → D-029:** opción *(a)*.

---

### Q-012 · ¿C5 se mantiene como mapa solo ZZ o se cambia?
**Bloquea:** M6 (6_Separability) · **Límite:** antes de calcular la separabilidad

H-034: con reps=1, `['X','ZZ']` equivale a un mapa solo ZZ. Hay dos salidas:

- *(a)* Mantener C5 tal como está y describirlo como una ablación del término de primer orden: C4 tiene Z más ZZ y C5 solo ZZ. No hay que recalcular nada.
- *(b)* Cambiar C5 a un conjunto cuyo primer orden actúe sobre |+⟩, por ejemplo `['Y','ZZ']` (fidelidad media 0.315 frente a ZZ en H-012). Eso recupera la comparación del eje de primer orden, pero obliga a recalcular C5 en 5a y 5b; son unos segundos de cómputo.

**Cerrada el 2026-10-05 → D-031:** opción *(b)*, con `['Y','ZZ']`.

### Q-013 · ¿Se compara contra k = 8 antes de concluir, como pide H-018?
**Bloquea:** la conclusión del OE-3 en §6 y §7 · **Límite:** 23 oct (congelamiento)

H-018 dejó una regla: si la separabilidad a k = 12 sale pobre, hay que comparar contra k = 8 antes de concluir que la codificación cuántica no aporta. El embedding está más concentrado a k = 12 (dispersión 0.042) que a k = 8 (0.084). El M6 dio separabilidad pobre (H-039, H-040). Hay dos salidas:

- *(a)* Hacer la comparación. Habría que repetir M4 con k = 8, con la misma regla de D-024 y D-025, recalcular en M5 los embeddings y los kernels de C1–C5 y repetir las métricas del M6. El cómputo tarda segundos; el trabajo, unas horas.
- *(b)* No hacerla y declararla como limitación, con el argumento de que D-013 fijó k = 12 antes de ver los datos.

**Decisión del autor.**

**Cerrada el 2026-10-06 → D-035:** opción *(a)*. Resultado en H-041.

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

