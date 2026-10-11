# Correcciones verificadas · TT 2026-B039

> Lista de trabajo para la Fase 7, no texto del reporte. Cada punto está comprobado contra el código, los CSV o la fuente original, y dice dónde está la evidencia. Marca la casilla al aplicarlo. Lo que **todavía no está verificado** está aparte, en la sección 7.

**Creado:** 2026-10-10 · **Origen:** re-ejecución completa del pipeline en un clon limpio (8 y 9 oct) y revisión de fórmulas, cifras y citas (9 y 10 oct).

---

## 0. Reproducibilidad · para §8.x y la defensa

**Resultado.** Se re-ejecutaron M2→M8, X1–X6, B2 y B3 con `jupyter nbconvert --execute` en un clon del repositorio, y se compararon todas sus salidas con las originales.
- 0 notebooks con error.
- 81 archivos de resultados y los 10,704 NRRD de M2 son **idénticos bit a bit**.
- Otros 5 difieren en menos de 10⁻¹⁰ (punto flotante): `8_rangos`, `X3_comparacion_k8_k12`, `X3_metricas_embedding` y los dos `emb_k8` de X3.
- Solo difieren los tiempos medidos y el muestreo de B3.
- B1 no se re-ejecutó: es un benchmark de tiempos y su sección de shots está invalidada por H-019.

Es la respuesta a «la auditoría X5 la hizo el mismo equipo»: cualquiera puede re-ejecutar el pipeline y obtener los mismos archivos.

- [ ] **H-051, límites del simulador.** En la re-ejecución, k = 28 tardó 46.3 s por estado (antes 74.8 s), y los límites salieron 26 / 23 / 15 en lugar de 25 / 22 / 14. Es lo mismo que la primera corrida mencionada en H-051. En el reporte, escribir **25–26, 22–23 y 14–15** según la carga de la máquina.
- [ ] **B3 no es reproducible bit a bit.** El muestreo de shots no fija semilla: en `B3_origen_suelo_h016.csv` el MAE pasa de 0.0131 a 0.0122, y en `B3_shots_muestreo_real.csv` el sesgo medio cambia hasta un 13 %. Fijar `seed_simulator` o citar esas cifras con dos cifras significativas, y revisar con qué precisión las cita H-019.

---

## 1. §3.4 · Fórmulas del reporte frente a lo implementado

El texto es el de TT1; el código hace lo que dicen las decisiones. Se corrige el texto.

- [ ] **KTA** (ecuación que empieza en la línea 1736). Está sin centrar; el M6 usa la **centrada** como principal (D-033, Cortes, Mohri y Rostamizadeh 2012). Añadir la matriz de centrado H = I − (1/n)𝟏𝟏ᵀ y dejar la sin centrar como complemento, con la razón de D-033: la sin centrar premia el desbalance.
- [ ] **Fisher** (líneas 1870–1881). Dice que J_F se calcula por dimensión y se promedia. El código (`fisher_ratio`, `6_Separability` celda 9) y D-033 usan **J = Δμᵀ S_W⁻¹ Δμ**: la distancia de Mahalanobis al cuadrado con la covarianza intraclase combinada. Incluir la razón: es invariante ante transformaciones afines invertibles, y por eso C1 = C2 (D-016).
- [ ] **Línea 1783.** Dice que √K_C se obtiene «por descomposición de Cholesky». El código (`psd_sqrt`) usa la **raíz simétrica por descomposición espectral**, V Λ^{1/2} Vᵀ. Cholesky da una matriz triangular L con LLᵀ = K, que no es la raíz simétrica que pide la fórmula.
- [ ] Ya conocidas: *g* invierte K_C y K_Q (H-033) y falta la versión regularizada (H-038, D-032); la ecuación de Spearman con Σd² solo vale sin empates (H-049).

**Verificado, sin cambio.** Contra el código fuente de arXiv:2011.01938:
- La ec. (5) invierte K¹, y la fórmula de g_gen del Apéndice F invierte K², así que los papeles están intercambiados.
- En (F12), con 1/(N−k) el término k = N divide entre cero. Con 1/(N−k+1), los estados ortogonales dan exactamente N. La cota «≤ N−k» del párrafo anterior tiene el mismo desfase.
- El código usa n−k+1 (`effective_dimension`).
- La cita «*where all inputs are too far apart*» (H-031) aparece tal cual en la introducción.

---

## 2. §2 y bibliografía

- [ ] **`TandFOnline2021`** (línea 3701) es una plantilla sin llenar: «Author(s). (2021). [Article title]. *AI Magazine*, 42(4), [pages]». Según Crossref, su DOI corresponde a: Zebari, Ibrahim, Zeebaree, Haron, Salih, Damaševičius y Mohammed (2021). *Systematic review of computing approaches for breast cancer detection based computer aided diagnosis using mammogram images*. **Applied Artificial Intelligence**, 35(15), 2157–2203. doi:10.1080/08839514.2021.2001177. Completa las iniciales desde el DOI.
- [ ] **Duplicados.**
  - Schuld y Killoran (2019) aparece como `Schuld2019QuantumML` (línea 3757) y como `schuld2019quantum` (línea 3831).
  - American Cancer Society (2024) aparece como `GlobalCancerStatistics2024` (línea 3621) y como `GlobalCancerStatistics2024_2` (línea 3656).
  - Dejar una clave por obra.
- [ ] **`GLOBOCAN2022`** (línea 3604) cita a Freihat, Sipos y Kovacs (2025), no a GLOBOCAN. Renombrar la clave o citar la fuente primaria, verificada en Crossref: Bray, Laversanne, Sung, Ferlay, Siegel, Soerjomataram y Jemal (2024). *Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries*. **CA: A Cancer Journal for Clinicians**, 74(3), 229–263. doi:10.3322/caac.21834.
- [ ] **10 `\bibitem` sin `\cite`** (no 11 como decía la lista de TT1; Radhi sí se cita):
  - `WHO2025`, `NBCF2026_Facts`, `Wang2020DeepLearning`, `Xiang2024QuantumCNN`, `Azevedo2022QuantumTransfer`;
  - `SaezOrtuño2026QuantumKernel`, `AlvarezEstevez2024QuantumKernelBench`, `Gao2023MammographyReview`, `Baccouche2022ResidualNN`, `ibmquantum2024learning`.
  - Varias se nombran en el texto sin `\cite` («Azevedo et al. (2022)», «Xiang et al. (2024)»…).
- [ ] **Azevedo et al. (2022)** (línea 825 y la tabla de §2). El 84 % de exactitud lo alcanzan **tanto** la ResNet clásica con *transfer learning* (C+TL) como las híbridas CQ1 y CQ4 (Tabla 4, p. 11). La diferencia que destacan está en el **AUC: 0.77 frente a 0.58**. En `ibm_lagos` la exactitud baja a 81 % (Tabla 5). Y concluyen: «*It is too soon to say whether or not QML can be an advantage*». El nombre correcto del dataset es Breast Cancer Digital Repository (ya estaba en la lista de TT1).
  - **Verificado, sin cambio: la atribución de D-019 es correcta.** §6 del artículo: «*As future work, an interesting approach could be to separate the dataset into masses and calcifications and only then perform classification*» y «*Lastly, the best way to know how well this model performs would be to see how the data appears in our Hilbert space. Ideally, both classes would appear very separately in it, as tight clusters.*»
- [ ] **Línea 783, cáncer de pulmón con QSVM, sin cita.** El trabajo es arXiv:2506.03272: El Hafidi, Toufah y Kadim (2025), *Investigating Quantum Feature Maps in Quantum Support Vector Machines for Lung Cancer Classification*. Tiene 309 registros de pacientes, 39 sin cáncer y 270 con cáncer. **Falta confirmar en el PDF** que las cifras de la línea 783 (ZZ 0.91, Pauli 0.96) son de ese trabajo y de qué subconjunto.
- [ ] **Línea 805, BreastMNIST con ResNet50 y una QNN (69 % frente a 67 %), sin cita.** La fuente **no se ha localizado**. Pista: arXiv:2512.02066 menciona en sus trabajos relacionados un modelo con ResNet50 que llega a 69 % en BreastMNIST. Hay que encontrar el artículo primario antes de citarlo.

---

## 3. `referencias_por_revisar.md` · metadatos verificados en Crossref

Autores, título, revista, volumen y páginas comprobados por DOI. **El contenido que se les atribuye sigue pendiente de verificar en el PDF** (regla 2 de la tesis).

| Referencia | Publicación | DOI |
|---|---|---|
| Liu, Arunachalam y Temme (2021), *A rigorous and robust quantum speed-up in supervised machine learning* | Nature Physics 17(9), 1013–1017 | 10.1038/s41567-021-01287-z |
| Glick, Gujarati, Córcoles, Kim, Kandala, Gambetta y Temme, *Covariant quantum kernels for data with group structure* | Nature Physics 20(3), 479–483 (**2024**; el preprint es de 2021) | 10.1038/s41567-023-02340-9 |
| Huang, Broughton, Cotler, Chen, Li, Mohseni, Neven, Babbush, Kueng, Preskill y McClean (2022), *Quantum advantage in learning from experiments* | Science 376(6598), 1182–1186 | 10.1126/science.abn7293 |
| Parigi, Khosrojerdi, Caruso y Banchi, *Analysis of quantum image representations for supervised classification* (arXiv:2507.22039) | AVS Quantum Science 8(1), 013801 (2026) | 10.1116/5.0296376 |
| Le, Dong y Hirota, FRQI | Quantum Information Processing 10(1), 63–84 (número de 2011; en línea desde 2010) | 10.1007/s11128-010-0177-y |
| Zhang, Lu, Gao y Wang (2013), NEQR | Quantum Information Processing 12(8), 2833–2860 | 10.1007/s11128-013-0567-z |
| Thanasilp, Wang, Cerezo y Holmes (2024), *Exponential concentration in quantum kernel methods*: candidata para H-031 | Nature Communications 15, 5200 | 10.1038/s41467-024-49287-w |
| Schuld, Sweke y Meyer (2021), *Effect of data encoding on the expressive power of variational quantum-machine-learning models*: la de las series de Fourier | Physical Review A 103(3), 032430 | 10.1103/PhysRevA.103.032430 |
| Hubregtsen, Wierichs, Gil-Fuster, Derks, Faehrmann y Meyer (2022), *Training quantum embedding kernels on near-term quantum computers* | Physical Review A 106(4), 042431 | 10.1103/PhysRevA.106.042431 |

Guyon y Elisseeff (2003), *JMLR* 3, 1157–1182, no tiene DOI en Crossref; verificar en jmlr.org.

---

## 4. §4.2 · Requerimientos que cambian por decisiones ya tomadas

Correspondencia entre requerimiento y decisión. Falta contrastarla con la redacción exacta de cada RF en el `.tex`.

| Requerimiento | Qué cambia | Decisión |
|---|---|---|
| RF-04 | Sin normalizar a [0, 1]: intensidades crudas de 16 bits en M2; el escalado a [0, π] pasa a M4 | D-022, D-025 |
| RF-05 | CLAHE solo como variante de comparación, fuera de la ruta radiómica | D-010, H-025 |
| RF-06 | Sin redimensionar a 224×224: recorte a resolución original con caja + 20 px | D-009, D-022 |
| RF-09 | `QuantileTransformer` × π en lugar de `MinMaxScaler` | D-025 |
| RF-13 | θ fijo con semilla 42, sin entrenar | D-014; X7 |
| RF-14 | C5 = `pauli_feature_map(['Y','ZZ'])` | D-031, H-034 |
| RF-16 | Fórmula de *g* corregida y regularizada | H-033, D-032 |
| RNF-02 | No hay `config.yaml`: los parámetros viven en cada notebook y en `emb_meta.json`, `x_<tipo>.json`. Reformular o declarar | — |
| RNF-07 | k = 12 sin entrenar θ; k ∈ [8, 16] con entrenamiento por *parameter-shift* es inalcanzable | H-011, H-051 |
| RNF-08 | Ocho módulos: la separabilidad es el M6 | D-030 |

---

## 5. §6 y §7 · Redacción de resultados

- [ ] **X6 no es simétrico en número de candidatos** (D-038, H-047). Tiene **28 candidatos cuánticos y 12 clásicos** (`X6_rejilla_candidatos.csv`: 140 y 60 filas con 5 folds). Lo simétrico es el procedimiento, la misma búsqueda anidada. La asimetría favorece a lo cuántico, así que la conclusión es conservadora; declararlo.
- [ ] **H-042, comparaciones múltiples.** Las cuatro diferencias cuánticas frente a C1 en el test (`7_test_diferencias.csv`), con p bilateral ≈ 2 × `share_above_0`:
  - C4 masas: p ≈ 0.003.
  - C4 calcificaciones: p ≈ 0.001.
  - C5 calcificaciones: p < 0.001.
  - C5 masas: −0.070 [−0.140, −0.004], **p ≈ 0.044**.
  - Con Holm sobre esa familia de cuatro, las cuatro siguen siendo significativas. Con Bonferroni, C5 en masas no lo es (0.044 × 4 ≈ 0.18).
  - Escribir «en el límite» para C5 en masas y decir qué corrección se usa.
- [ ] **H-043, k = 8.** C4 en calcificaciones da −0.070 [−0.141, **+0.0005**]: el intervalo toca el cero. Cambiar «C4 empeora» por «C4 tiende a empeorar; el intervalo llega al cero».
- [ ] **H-041, tabla.** El exceso de KTA del RBF en calcificaciones a k = 12 dice 0.151. El CSV da 0.1517, es decir, **0.152**, como en H-039.
- [ ] **H-052 frente a `8_oe6_resumen.csv`.** El CSV redondea a entero (2 % y 1 %) lo que H-052 da con un decimal (2.5 % y 1.5 %). Si esa tabla va al reporte, usar un decimal.
- [ ] **«Preregistrado».** Aparece 10 veces en la bitácora y en la celda 11 de `7_Classification` («*preregistered configuration*»). Como no hay un registro público, conviene «fijado antes de ver los resultados» o «establecido a priori».
- [ ] **H-048, alcance de la conclusión.** «La ausencia de ventaja es una propiedad de la tarea» conviene acotarlo: de **estas etiquetas, con estas 12 features y estas familias de kernels** (ZZ, Y-ZZ y proyectados). El mismo protocolo sí detecta una ventaja cuando las etiquetas siguen la geometría del kernel cuántico.

---

## 6. Decisiones provisionales · evidencia para validarlas

Los números que sostienen D-020 y D-021, recalculados de `2_preprocesamiento_qa.csv`:
- **D-020.** `mismatch`: 78 `scaled`, todas masas, con razón máscara/imagen de 0.8700 a 0.8704 en filas y columnas. Otras 2 son `offset`, ambas calcificaciones de P_00353. El resto, 3,488, no tiene desajuste.
- **D-021.** 1,464 de las 1,696 máscaras de masas (86.3 %) traen más de una componente; ninguna de calcificaciones.
  - Al quedarse con la mayor se conserva siempre al menos el **99.55 % del área**.
  - Lo removido tiene una mediana de 5 px (máximo 110 px) y nunca está a más de 14 px de la lesión.
- **Los 7 casos discordantes** (`crop_check = discordant`) siguen en M3 y M4. Excluirlos o no es tu decisión.
- D-022, D-036 y D-040: sin hallazgos en contra en la revisión.

---

## 7. Pendiente de verificar · pistas, no hechos

- **El factor 0.870 de D-020** podría ser la razón entre los tamaños de píxel de dos digitalizadores del DDSM, 43.5 µm / 50 µm = 0.870. Es una hipótesis: hay que confirmar en la documentación del DDSM qué escáneres se usaron y con qué resolución antes de mencionarla.
- **Las cuatro preguntas de H-046** aplicadas a Xiang et al. (2024), al trabajo de BreastMNIST, al de cáncer de pulmón, a Radhi et al. (2025) y a Azevedo et al. (2022). De Azevedo ya está verificado que las variantes CQ1–CQ4 se comparan en el mismo conjunto de prueba (Tabla 4) y que el 84 % es un empate con C+TL. Lo demás hay que leerlo en cada PDF.
