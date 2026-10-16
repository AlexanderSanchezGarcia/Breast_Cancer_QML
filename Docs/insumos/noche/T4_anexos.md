# T4 · Anexos A–D

Lee primero `Docs/insumos/noche/reglas.md`.

## Objetivo

Crear los anexos del reporte en `Docs/capitulos/A_Anexos/`, para que el capítulo de Metodología pueda remitir al código, a las salidas y a las figuras que no caben en el cuerpo. **Tú escribes solo en:** `Docs/capitulos/A_Anexos/A.0_*.tex`, `A.1_*.tex`, `A.2_*.tex`, `A.3.1_*.tex`, `A.4_*.tex`, `A.5_*.tex`; `Docs/codigo/` (solo mediante `extraer_codigo.py`); `Code/tools/tablas_anexos.py`; `Docs/tablas/anexo_*.tex`. El archivo `A_Anexos/A.3.2_figuras_eda.tex` es de otro trabajador: no lo toques.

Estructura LaTeX: `A.0_introduccion.tex` abre con `\appendix` y `\section{Anexos}` no numerado como capítulo… — usa simplemente:
```latex
\appendix
\section{Código de los módulos}\label{anx:codigo}
```
y una `\section` por anexo (A, B, C, D, E). `\appendix` hace que se numeren con letras.

## A · Código de los módulos (`A.1_codigo.tex`)

Fragmentos **literales** de los notebooks, extraídos con la herramienta (nunca copiados a mano):
```
python3 Code/tools/extraer_codigo.py --listar Code/4_Selection_and_Scaling.ipynb
python3 Code/tools/extraer_codigo.py Code/4_Selection_and_Scaling.ipynb <k> m4_seleccion --lineas a-b
```
Cada fragmento de 10 a 45 líneas; elige el rango que muestra la idea, no la impresión de resultados. Un `\subsection` por módulo con 1–3 listados y, antes de cada listado, un párrafo de 2–4 líneas que diga qué hace el fragmento y por qué (la decisión que implementa, con `% fuente: D-0xx` en comentario). Contenido mínimo:

| Módulo | Notebook | Qué mostrar |
|---|---|---|
| M2 | `Code/2_Preprocessing.ipynb` | la regla de alineación de máscaras (escala 0.870 vs. anclaje) y la reducción a la componente conexa mayor; el recorte de caja + 20 px |
| M3 | `Code/3_Feature_Extraction.ipynb` | la configuración de PyRadiomics (`binCount=32`, clases de features activas) |
| M4 | `Code/4_Selection_and_Scaling.ipynb` | selección por F con restricción \|r\| ≤ 0.95; `QuantileTransformer` × π ajustado solo en train; `StratifiedGroupKFold` por paciente |
| M5 | `Code/5a_Embeddings.ipynb`, `Code/5b_Quantum_Kernels.ipynb` | construcción de C4 (`zz_feature_map`) y C5 (`pauli_feature_map(paulis=['Y','ZZ'])`) con el *ansatz* y θ fijo (semilla 42); cálculo de ⟨Zᵢ⟩ con `Statevector`; kernel con `FidelityStatevectorKernel` |
| M6 | `Code/6_Separability.ipynb` | KTA centrada con permutaciones; *geometric difference* regularizada |
| M7 | `Code/7_Classification.ipynb` | definición del MLP k→32→16→1 y el bucle con parada temprana |
| M8 | `Code/8_Comparison.ipynb` | Spearman con empates y su nula exacta; muestreo de ⟨Zᵢ⟩ con `SamplerV2` (OE-6) |

Leyenda de cada listado: qué es + `(notebook, celda de código k)`. Etiquetas `lst:m2_alineacion`, etc. Si el código importa funciones de `Code/tools/` o de otro módulo, no las extraigas: menciónalas.

## B · Salidas (`A.2_salidas.tex`)

Tablas generadas **por script** desde `Code/results/*.csv`, nunca tecleadas. Escribe `Code/tools/tablas_anexos.py` (con pandas; ejecútalo con `/opt/anaconda3/envs/qml_cancer/bin/python`) que genere `Docs/tablas/anexo_*.tex` (`booktabs`, como `Docs/tablas/m4_seleccion.tex`; mira `Code/tools/tablas_latex.py` y reutiliza su estilo). Mínimo:
1. Resumen de M2: `2_preprocesamiento_resumen.csv` (y `2_preprocesamiento_qa.csv` si aporta).
2. Las 12 features seleccionadas por subconjunto con su F, p y |d|: `4_seleccion.csv` (+ `3_tamano_efecto.csv`), y las descartadas por redundancia: `4_descartadas_redundancia.csv`.
3. Balance de clases por fold: `4_folds.csv`.
4. Costes del simulador: `5b_tiempos.csv`, `8_oe6_qubits.csv`, `X8_costo_gradiente.csv`.
5. Verificaciones automáticas de cada módulo: `5a_verificaciones.csv`, `5b_verificaciones.csv`, `6_verificaciones.csv`, `7_verificaciones.csv`, `8_verificaciones.csv` (qué comprueba cada una y si pasó).
6. Auditoría X5: `X5_auditoria.csv`.

Abre antes cada CSV y elige columnas legibles; redondea a 3 cifras significativas salvo enteros. Pie de cada tabla: qué es y de qué CSV sale (sin D-xxx/H-xxx visibles). En `A.2_salidas.tex`, `\input{tablas/anexo_…}` y una línea de contexto por tabla.

## C · Figuras complementarias (`A.3.1_figuras.tex`)

Figuras de `Docs/Figures/` que **no** usa ningún capítulo de `Docs/capitulos/` (compruébalo con `grep -rn <nombre> Docs/capitulos`), excepto las del EDA (`B*`, `C*`, `D*`), que son de otro trabajador. Mínimo: `E1_circuit_complexity`, `E2_training_cost`, `E3_shots_sensitivity`, `E4_embedding_concentration`, `M2_mask_alignment`, `M2_preprocessing_examples`, `M5_circuit_12q` (muy alta: ancho `0.6\textwidth` o la altura de la página), `M5_embeddings`, `M8_spearman_null`, `X2_kernel_pairs_by_class`, `X3_embedding_metrics_k8_k12`, `X4_qsvm_scale`. El inventario `Docs/insumos/inventario_figuras.md` dice qué notebook y qué entrada de la bitácora genera cada una. **Atención:** E3 lo invalidó en parte H-019 (la sección de *shots* de B1); si la incluyes, dilo en el pie y apóyate en B3. El pie de cada figura se redacta a partir de la entrada de la bitácora correspondiente (comentario `% fuente:` delante); sin cifras que no estén en esa entrada.

## D · Entorno de ejecución (`A.4_entorno.tex`)

- Tabla de versiones de los paquetes clave de los dos entornos, obtenida con `/opt/anaconda3/bin/conda list -n radiomics` y `-n qml_cancer` (python, numpy, pandas, scikit-learn, scipy, matplotlib, opencv, pydicom, SimpleITK, pyradiomics, qiskit, qiskit-aer, qiskit-machine-learning, torch). Guarda la salida cruda en `Docs/insumos/noche/conda_list_<entorno>.txt` y genera la tabla desde ahí.
- PyRadiomics compilado desde el commit `8ed579383b44806651c463d5e691f3b2b57522ab` (procedimiento en `Code/env/README.md`; resúmelo en 3–5 líneas).
- Hardware: `sysctl -n machdep.cpu.brand_string`, `sysctl -n hw.memsize`, `sw_vers`.
- Semillas fijas (42 para θ y submuestras; 125 y 168 para los folds, D-026) y la reproducción bit a bit del 8–10 oct (`CLAUDE.md`, «Re-ejecución completa»).

## E · Índice de decisiones (`A.5_decisiones.tex`)

Tabla larga (`longtable`) con cada decisión `### D-0xx · título` de `Other/bitacora_decisiones.md`: identificador, título y sección del reporte que alimenta (si la entrada lo dice). Genérala **con un script** (añádelo a `Code/tools/tablas_anexos.py`) a partir de los encabezados; marca las revertidas (D-002, D-015). Aquí sí aparecen los identificadores D-xxx, porque es el índice. Una línea de introducción: la bitácora completa acompaña al reporte como material complementario.

## Aceptación

- `python3 Code/tools/verificar_listados.py Docs/capitulos/A_Anexos` sin problemas.
- `bash Docs/capitulos/compilar_prueba.sh A_Anexos` compila sin errores ni referencias sin resolver.
- `/opt/anaconda3/envs/qml_cancer/bin/python Code/tools/verificar_cifras_capitulos.py Docs/capitulos/A_Anexos`: sin `SIN_FUENTE` ni `NO_ENCONTRADO` en los párrafos que escribiste (las tablas generadas por script no cuentan).
- Informe en `Docs/insumos/noche/informe_T4.md`: listados (archivo, notebook, celda, líneas), tablas generadas, figuras incluidas y salida de las tres pruebas.
