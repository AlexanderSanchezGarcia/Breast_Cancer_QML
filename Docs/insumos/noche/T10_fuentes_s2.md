# T10 · Fuentes y fichas para §2.1.1–§2.1.5

Lee primero `Docs/insumos/noche/reglas.md`. Todas sus reglas valen aquí, en especial la 4: **no inventes nada**.

## Objetivo

El coordinador va a reescribir §2.1.1–§2.1.5 (`Docs/capitulos/2_Antecedentes/2.1.1_ml_clasico.tex` a `2.1.5_cbis_ddsm.tex`). Esos archivos citan obras de las que hoy no hay texto en el repositorio, así que sus afirmaciones no se pueden comprobar. Tu tarea es **mecánica**: conseguir el texto de cada obra de acceso abierto y escribir una ficha que responda, con citas literales, las preguntas de la tabla. **No edites ningún `.tex`.** Tú no decides qué dice el capítulo; solo informas qué dice cada fuente.

## Pasos por cada clave

1. **Descarga** el PDF desde una fuente legítima de acceso abierto: la página del editor (Nature/Scientific Reports, BMC, MDPI, Taylor & Francis OA, Quantum), PubMed Central o arXiv. Guárdalo como `Docs/fuentes/pdf/<Clave>.pdf`. **Prohibido** usar Sci-Hub, LibGen o cualquier copia no autorizada. Si la obra no es de acceso abierto, no la descargues: marca la clave como `NO_ACCESIBLE` en el informe y sigue con la siguiente.
2. **Extrae** el texto con `python3 Code/tools/extraer_texto_pdf.py <Clave>`. El script imprime las primeras líneas de la página 1: **comprueba que el título y el DOI coinciden** con los de la tabla. Si no coinciden, borra el PDF y su carpeta de `txt/` y anótalo en el informe.
3. **Escribe la ficha** `Docs/insumos/fichas/<Clave>.md` con el formato de abajo. Cada respuesta lleva su cita literal con página, o la etiqueta `NO_ENCONTRADO` y dónde buscaste (secciones o páginas). Una respuesta `NO_ENCONTRADO` es un resultado útil: varias de estas afirmaciones vienen de TT1 y podrían no estar en la fuente.
4. **Verifica**: `python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/<Clave>.md` debe pasar sin fallos.

## Formato de cada ficha

```markdown
# <Clave> · <título exacto, copiado de la página 1>

- Autores y año: (de la tabla)
- DOI comprobado en la página 1: Sí / No
- Versión leída: Docs/fuentes/pdf/<Clave>.pdf · publicada | preprint de arXiv · N páginas
- Tipo: revisión | experimental | teórico | conjunto de datos

## Respuestas a las preguntas
1. <pregunta resumida> — <respuesta en español en una línea> — «cita literal» (p. N)
   (o: NO_ENCONTRADO — busqué en pp. X–Y, secciones …)
2. …

## Qué concluye la obra
- 2 a 5 viñetas, cada una con cita literal.

## Qué deja como trabajo futuro o limitación declarada
- Con cita literal, o «No declara trabajo futuro explícito» y dónde buscaste.
```

Las citas: copia exacta del `.txt`, en el idioma original, máximo dos oraciones, sin traducir dentro de las comillas.

## Claves y preguntas

| Clave | Obra (DOI) | Preguntas |
|---|---|---|
| `TandFOnline2021` | Zebari et al. (2021), *Applied Artificial Intelligence* 35(15) — 10.1080/08839514.2021.2001177 | (1) ¿Dice que GLCM es la técnica de extracción de características más usada en los trabajos revisados? Cifra si la da. (2) ¿Menciona descriptores de forma y margen para masas y de distribución para calcificaciones? (3) ¿Describe los sistemas CAD en dos etapas (extracción y clasificación) y su origen en los años noventa? (4) ¿Dice algo sobre interpretabilidad o generalización como retos futuros? |
| `Mashekova2025AIBreastCancer` | Mashekova et al. (2025), *Bioengineering* 12(10) 1110 — 10.3390/bioengineering12101110 | (1) ¿Qué porcentaje de los estudios usa SVM y en qué periodo? (2) ¿Dice que SVM es el más frecuente con mamografía? (3) ¿Qué razones da para el uso de SVM? |
| `Avci2023MammographyEnhancement` | Avcı y Karakaya (2023), *Diagnostics* 13(3) 348 — 10.3390/diagnostics13030348 | (1) ¿Qué clasificadores comparan y con qué características (GLCM, GLRLM)? (2) ¿Cuáles rinden mejor y en qué métricas? (3) ¿Qué dicen de la sensibilidad al preprocesamiento? (4) Conjunto de datos usado. |
| `Anez2025AIPipeline` | Añez et al. (2025), *Medicina* 61(12) 2237 — 10.3390/medicina61122237 | (1) AUC-ROC y sensibilidad de la CNN (¿ResNet-50?), de XGBoost y de SVM sobre CBIS-DDSM: cifras exactas. (2) ¿Qué entrada recibieron SVM y XGBoost (características manuales, de una CNN, otra)? (3) Partición o protocolo de evaluación. |
| `Abdelhafiz2019DeepCNN` | Abdelhafiz et al. (2019), *BMC Bioinformatics* 20(Suppl 11) 281 — 10.1186/s12859-019-2823-4 | (1) ¿Dice que las CNN poco profundas se usaron en cáncer de mama desde 1995? (2) ¿Atribuye el auge desde 2012 a AlexNet, capacidad de cómputo, hardware barato, código abierto y *big data*? (3) ¿Qué arquitecturas menciona como base de los CAD modernos? |
| `Shen2019DeepLearning` | Shen et al. (2019), *Scientific Reports* 9 12495 — 10.1038/s41598-019-48995-4 | (1) AUC por imagen del mejor modelo individual sobre el test del CBIS-DDSM. (2) AUC del promedio de cuatro modelos, y sensibilidad y especificidad que reportan. (3) ¿Lo comparan con radiólogos? Cita literal. (4) ¿Qué arquitecturas usan (ResNet, VGG)? |
| `Shia2025MicrocalcClassification` | Shia (2025), *Scientific Reports* 15 42768 — 10.1038/s41598-025-27149-9 | (1) Modelos comparados (ResNet-50, ResNet-101, EfficientNet B0–B4) y validación (¿5 pliegues?). (2) ¿EfficientNet supera significativamente a ResNet en F1? ¿Con qué prueba estadística? (3) Resultado de la validación externa con CBIS-DDSM (EfficientNet-B3, *recall*). (4) Origen de los datos de entrenamiento (¿etiquetas BI-RADS?). |
| `Wang2020DeepLearning` | Wang et al. (2020), *JACR* 17(6) 796–803 — 10.1016/j.jacr.2020.01.006 | **Ya hay texto** en `Docs/fuentes/txt/Wang2020DeepLearning/` (resumen HTML); no descargues nada salvo que encuentres el texto completo de acceso abierto. (1) Número de modelos y de conjuntos de datos. (2) AUC en validación (0.88–0.95) y en los conjuntos externos (0.44–0.65), con sus intervalos. (3) ¿Dice algo de la variabilidad entre lectores, del cambio de dominio o de la necesidad de conjuntos diversos? |
| `Baccouche2022ResidualNN` | Baccouche et al. (2022), *Scientific Reports* 12 12259 — 10.1038/s41598-022-15632-6 | (1) *Accuracy* en patología (¿95.13 %?) y en forma (¿90.02 %?) y sobre qué conjuntos. (2) ¿Reportan AUC? Cifra exacta. (3) ¿Trabajan solo con masas o también con calcificaciones? (4) Modelos del *ensemble* (ResNet50V2, ResNet101V2, ResNet152V2). |
| `havlicek2019supervised` | Havlíček et al. (2019), *Nature* 567 209–212 — 10.1038/s41586-019-0980-2. Si el editor no es abierto, usa el preprint arXiv:1804.11326 y dilo en «Versión leída». | (1) ¿Qué dos métodos proponen? (2) ¿En qué procesador y con cuántos qubits los ejecutan? (3) ¿Qué dicen exactamente sobre la ventaja cuántica: la afirman, la conjeturan o la ponen como condición (kernel difícil de estimar clásicamente)? Cita literal. (4) Forma del circuito de codificación que proponen (funciones φ de los datos). |
| `Schuld2019QuantumML` | Schuld y Killoran (2019), *Phys. Rev. Lett.* 122 040504 — 10.1103/PhysRevLett.122.040504. Si no es abierto, usa arXiv:1803.07128 y dilo. | (1) La frase que compara la computación cuántica con los métodos kernel (cómputo eficiente en un espacio de Hilbert grande). (2) ¿Interpretan la codificación como un *feature map* no lineal hacia el espacio de Hilbert? (3) ¿Dicen que el kernel puede ser clásicamente intratable? ¿Con qué matiz? |
| `Long2025HybridQCQ` | Long et al. (2025), *Scientific Reports* 15 31780 — 10.1038/s41598-025-13417-1 | (1) Su definición de circuito cuántico variacional y de PQC, literal. |
| `Radhi2025QuantumDeepLearning` | Radhi et al. (2025), *Iraqi J. Comput. Sci. Math.* 6(2) — 10.52866/2788-7421.1252 | (1) Número de estudios y periodo de la revisión (¿28, 2018–2024?). (2) Aplicaciones (¿tumores cerebrales, piel, COVID-19?) y modelos (QSVM, QCNN, híbridos). (3) Retos que identifican (codificación de imágenes, escalabilidad del hardware, interpretabilidad). |
| `Arrasmith2021` | Arrasmith et al. (2021), *Quantum* 5 558 — 10.22331/q-2021-10-05-558 | (1) Su conclusión central sobre *barren plateaus* y optimización sin gradientes, literal. |
| `Yang2023MedMNIST` | Yang et al. (2023), «MedMNIST v2», *Scientific Data* 10, 41 — 10.1038/s41597-022-01721-8 | (1) ¿De qué modalidad de imagen sale BreastMNIST (mamografía o ultrasonido) y de qué conjunto original? (2) Número de imágenes y resolución (¿28×28?). **No hay `\bibitem` de esta obra**; no lo crees, el coordinador lo genera desde Crossref. |
| `Rifat2024` | Rifat et al. (2024), ICCIT, IEEE, pp. 1464–1469 — metadatos en `Docs/insumos/fuentes_bib/Rifat2024.json` | Es de pago: **no descargues el PDF**. Consulta solo el resumen público de la página de IEEE Xplore o de Crossref y guárdalo como `Docs/fuentes/txt/Rifat2024/p001.txt` (texto visible del resumen, sin nada más). (1) ¿Qué conjunto de datos y qué *accuracy* reporta el resumen? (2) ¿Con qué lo compara? Si el resumen no es accesible, marca `NO_ACCESIBLE`. |

## Prohibido además

- Editar cualquier `.tex`, `bibitems_*.tex`, `Technical_Report.tex` o la bitácora.
- Crear `\bibitem`.
- Hacer commits o `git add` (regla 2).
- Escribir fuera de `Docs/fuentes/pdf/`, `Docs/fuentes/txt/`, `Docs/insumos/fichas/` y tu informe.

## Aceptación

1. `python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas` termina sin fallos en las fichas nuevas (copia la salida).
2. En el informe `Docs/insumos/noche/informe_T10.md`, una tabla con una fila por clave: estado (`HECHA` / `NO_ACCESIBLE` / `PDF_INCORRECTO`), URL de descarga, título de la página 1 tal como lo imprimió el script y número de preguntas con `NO_ENCONTRADO`.
3. Una lista de cada `NO_ENCONTRADO`, con la clave y la pregunta.
