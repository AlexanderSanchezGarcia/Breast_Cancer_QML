# T1 · Fichas de lectura (grupos A, B, C y D)

Lee primero `Docs/insumos/noche/reglas.md`. Tu especificación de Orca te dice qué **grupo** te toca; haz solo las claves de ese grupo.

## Objetivo

Una ficha por obra, en `Docs/insumos/fichas/<Clave>.md` (el nombre del archivo **es** la clave; el verificador lo usa para encontrar el texto). La ficha sirve para que el autor cite con precisión: debe separar lo que la obra **concluye** de lo que deja como **trabajo futuro o limitación** (regla 2 de `CLAUDE.md`), y toda afirmación sobre la obra lleva su cita literal con página.

## Formato de cada ficha

```markdown
# <Clave> · <título exacto>

- Autores y año: (de bibitems_nuevos.tex / bibitems_noche.tex / Technical_Report.tex)
- Versión leída: Docs/fuentes/pdf/<Clave>.pdf · preprint de arXiv | versión publicada · N páginas
- Tipo: teórico | experimental | revisión | conjunto de datos | manual

## Qué concluye
- <afirmación en español> — «cita literal» (p. N)
  (de 3 a 8 viñetas; las conclusiones centrales, no detalles)

## Qué deja como trabajo futuro o limitación declarada
- <afirmación> — «cita literal» (p. N)
  (si la obra no declara ninguna, escribe «No declara trabajo futuro explícito» y di dónde buscaste)

## Diseño experimental (solo obras experimentales)
- Datos, tamaño, partición, métricas, simulador o hardware, comparación clásica — cada dato con cita.

## Las cuatro preguntas de H-046 (solo obras que reportan una ventaja o un resultado cuántico frente a clásico)
1. ¿El modelo clásico recibió el mismo ajuste y las mismas features?
2. ¿La diferencia supera su incertidumbre (hay intervalos, desviaciones, pruebas)?
3. ¿El test se usó una sola vez?
4. ¿El kernel o el circuito cuántico es realmente difícil de simular clásicamente?
Para cada una: Sí / No / No lo dice, con la cita que lo sustenta o la indicación de dónde se buscó.

## Preguntas específicas
(responde las de la tabla de abajo para esta clave, cada respuesta con cita)

## Relevancia para el TT
- A qué hallazgo, decisión o sección del proyecto se conecta (H-0xx, D-0xx, §x), en una o dos líneas cada uno.
- **Qué NO se puede afirmar con esta fuente** (al menos una viñeta): lo que alguien podría atribuirle y la obra no dice.

## Contraste con lo que el proyecto ya le atribuye
- Busca la clave (y el apellido del primer autor) en `Docs/Technical_Report.tex`, `Other/verificacion/referencias_por_revisar.md`, `Other/verificacion/correcciones_verificadas.md` y `Other/bitacora_decisiones.md` con `grep -n`. Para cada atribución existente: línea, qué dice, y si la obra lo sostiene (Sí / No / Parcial), con cita.
```

## Grupos y preguntas específicas

### Grupo A · ventaja cuántica: teoría y datos cuánticos
| Clave | Preguntas específicas |
|---|---|
| `huang2021power` | Definición exacta de la *geometric difference* y de los kernels proyectados; la frase sobre «all inputs are too far apart» o equivalente (cítala literal si existe y da su página); qué dicen de la dimensión efectiva y del error de generalización. |
| `Liu2021Speedup` | En qué sentido exacto el kernel es difícil (supuesto de complejidad); si requiere computador tolerante a fallos; tamaño de los conjuntos; que la estructura está en la etiqueta (logaritmo discreto). |
| `Glick2024Covariant` | El problema de clases laterales; cuántos qubits y qué hardware; qué es el *kernel alignment* que usan; si afirman ventaja en datos reales. |
| `Huang2022Experiments` | Qué tareas muestran ventaja exponencial y si esa ventaja requiere memoria cuántica (datos que ya son estados cuánticos); tamaño del experimento (qubits, compuertas). |

### Grupo B · concentración, ancho de banda y evaluación de modelos cuánticos
| Clave | Preguntas específicas |
|---|---|
| `Thanasilp2024` | Las fuentes de concentración exponencial que identifican (expresividad, entrelazamiento global, medición global, ruido); qué implica para el número de *shots*; si la concentración afecta al kernel de fidelidad y al proyectado. |
| `Kubler2021Inductive` | Qué dicen del sesgo inductivo de los kernels cuánticos y de por qué hace falta restringirlo; papel de la «pureza»/escala; relación con kernels clásicos. |
| `Shaydulin2022Bandwidth` | Cómo definen el ancho de banda (factor que multiplica los datos antes del *feature map*); qué pasa con el kernel cuando el ancho es grande o pequeño; resultados de clasificación. |
| `Canatar2023Bandwidth` | Por qué el ancho de banda permite generalizar; relación con el espectro del kernel; si el kernel con ancho pequeño se vuelve aproximable clásicamente. |
| `SchuldKilloran2022Advantage` | Su argumento central sobre por qué la ventaja cuántica no debería ser el único objetivo; qué proponen en su lugar. |
| `Bowles2024Benchmarking` | Diseño del *benchmark* (cuántos modelos y conjuntos); si los modelos clásicos superan a los cuánticos; qué pasa al quitar el entrelazamiento; recomendaciones metodológicas. |

### Grupo C · imágenes cuánticas y trabajos aplicados a cáncer
| Clave | Preguntas específicas |
|---|---|
| `Parigi2026QImR` | Las cuatro representaciones y su compresión; **si discuten el coste de preparar el estado** (cítalo literal si lo hacen; si no, dilo); qué kernels comparan y con qué conclusión. El proyecto pensaba usarla para decir que «el coste de carga anula la ventaja»: di si la obra lo sostiene. |
| `Le2011FRQI` | Complejidad de preparación del estado FRQI tal como la enuncian (¿polinomial? ¿O(2^{4n})? cita la expresión exacta); cuántos qubits para una imagen de 2^n × 2^n. |
| `Zhang2013NEQR` | Complejidad de preparación de NEQR y comparación con FRQI tal como la enuncian; qubits necesarios. |
| `Azevedo2022QuantumTransfer` | **Crítico.** El trabajo futuro que declaran, literal (el proyecto afirma que señalan analizar por tipo de hallazgo y evaluar la distribución de los datos en el espacio de Hilbert: verifica ambas cosas palabra por palabra); qué significa BCDR en el artículo; el 84 %; las variantes CQ1–CQ4 frente a C+TL; *embedding* usado. Aplica las cuatro preguntas. |
| `Xiang2024QuantumCNN` | Conjuntos de datos (GBSG, SEER, WDBC); el «hasta 5 %» de mejora; frente a qué modelos; si hay incertidumbre reportada; simulador o hardware. Aplica las cuatro preguntas. |
| `ElHafidi2025` | Las cifras de ZZ (0.91) y Pauli (0.96) y en qué métrica; el SVM clásico con RBF; tamaño y partición; qué *PauliFeatureMap* usan (qué Paulis). Aplica las cuatro preguntas. |

### Grupo D · fundamentos citados en el reporte
| Clave | Preguntas específicas |
|---|---|
| `Mari2020Transfer` | Qué es un *dressed quantum circuit*; si contiene una frase equivalente a «la red cuántica completa … mapea un espacio vectorial clásico a otro … funcionalmente análoga a una red clásica profunda» (el §1.1.3 del reporte la usa sin cita: compara con `sed -n 561,564p Docs/Technical_Report.tex`). |
| `Lee2017CBISDDSM` | Número de casos/estudios/pacientes que reporta; cómo se construyeron las ROI y la partición train/test (¿estratificada por BI-RADS? cítalo si lo dice; si no, dilo: el reporte lo afirma sin verificar); licencia. |
| `Preskill2018NISQ` | Definición de NISQ y el rango de qubits; lo que dice sobre ventaja a corto plazo. |
| `McClean2018Barren` | El enunciado del *barren plateau* (gradientes que se anulan exponencialmente con el número de qubits) y sus condiciones (circuitos aleatorios, 2-diseños). |
| `Schuld2021Encoding` | Que los modelos variacionales son series de Fourier en los datos codificados; qué determina el espectro de frecuencias. |
| `Hubregtsen2022` | Qué son los *quantum embedding kernels* entrenables y cómo entrenan con *kernel-target alignment*. |
| `Guyon2003` | Lo que dicen de la selección univariante y de variables inútiles por sí solas pero útiles juntas (relacionado con H-030); cítalo literal con página. |
| `Zwanenburg2020IBSI` | El PDF es el **manual de referencia de IBSI** (178 pp.), no el artículo de *Radiology*. Busca solo: qué recomienda sobre discretización con número fijo de *bins* frente a ancho fijo cuando las intensidades no están calibradas (relacionado con D-008: `binCount=32`). En la ficha aclara que las citas son del manual. |

## Aceptación

- `python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/<Clave>.md` pasa para **cada** ficha de tu grupo.
- Cada ficha tiene las secciones del formato (las que no aplican, con «No aplica: …»).
- Informe en `Docs/insumos/noche/informe_T1_<grupo>.md` con la salida del verificador y una tabla de **discrepancias** entre lo que el proyecto atribuye a cada obra y lo que la obra dice. Esa tabla es lo más valioso para el autor.
