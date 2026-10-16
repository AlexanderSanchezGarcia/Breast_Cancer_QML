# Informe de Tarea T4 · Anexos A–E del Reporte Técnico

**Fecha:** 2026-10-14  
**Repositorio:** `/Users/alexander_san/TT`  
**Autor:** Antigravity (Trabajador nocturno T4)  
**ID de Tarea:** `task_ed012c867857` · **ID de Despacho:** `ctx_3992949ef96f`

---

## 1. Resumen Ejecutivo

Se implementaron de manera íntegra y reproducible los Anexos A a E del Reporte Técnico en `Docs/capitulos/A_Anexos/` conforme a la especificación de `Docs/insumos/noche/T4_anexos.md` y respetando todas las reglas metodológicas de `reglas.md`. 

1. **Anexo A (Código de los módulos):** Se extrajeron mediante `extraer_codigo.py` 15 fragmentos literales de los cuadernos de trabajo (M2 a M8), de entre 10 y 25 líneas cada uno, acompañados de párrafos introductorios con sus respectivas decisiones de bitácora respaldadas (`% fuente:`).
2. **Anexo B (Salidas complementarias):** Se creó el script generador `Code/tools/tablas_anexos.py` para construir de forma determinista 9 tablas en `Docs/tablas/anexo_b_*.tex` a partir de los archivos CSV de resultados, cubriendo preprocesamiento (M2), selección y redundancia (M4), validación cruzada estratificada (M4), tiempos y costes cuánticos (M5, M8, X8), la suite de verificaciones automáticas (M5 a M8) y la auditoría metodológica (X5).
3. **Anexo C (Figuras complementarias):** Se compilaron las 12 figuras de `Docs/Figures/` no incluidas en los capítulos principales (complejidad, coste, concentración, QSVM, alineamiento, etc.), redactando pies de figura rigurosamente apoyados en la bitácora e incorporando la salvedad de H-019/B3 para E3.
4. **Anexo D (Entorno de ejecución y reproducibilidad):** Se documentaron las dependencias congeladas de los entornos Conda `radiomics` y `qml_cancer` (exportadas a `conda_list_*.txt`), el procedimiento de compilación nativa de PyRadiomics en el commit fijado `8ed579383b44806651c463d5e691f3b2b57522ab`, las especificaciones de hardware (Apple M3, 16\,GB unificada, macOS 26.6.2) y las semillas pseudoaleatorias deterministas (42, 125, 168).
5. **Anexo E (Índice de decisiones):** Se generó automáticamente la tabla en formato `longtable` con las 40 decisiones metodológicas formales (D-001 a D-040), marcando las determinaciones revertidas (D-002, D-015) y enlazando las secciones del reporte correspondientes.

Todas las pruebas de aceptación pasaron sin advertencias ni discrepancias: `verificar_listados.py` constató 15 de 15 listados idénticos; `compilar_prueba.sh A_Anexos` compiló sin errores, sin citas/referencias pendientes y con cero cajas desbordadas; y `verificar_cifras_capitulos.py` ratificó que el 100\,\% de las cifras numéricas del texto redactado coinciden con la bitácora sin reportar ningún `SIN_FUENTE` ni `NO_ENCONTRADO`.

---

## 2. Inventario de Archivos Creados y Modificados

### Archivos de Capítulos LaTeX (`Docs/capitulos/A_Anexos/`)
- `A.0_introduccion.tex`: Apertura del entorno `\appendix` y compatibilidad para compilación aislada.
- `A.1_codigo.tex`: Anexo A con 15 listados de código y comentarios de fuente para M2 a M8.
- `A.2_salidas.tex`: Anexo B con inclusión de tablas complementarias y líneas de contexto.
- `A.3.1_figuras.tex`: Anexo C con las 12 figuras metodológicas complementarias y pies calibrados.
- `A.4_entorno.tex`: Anexo D con detalles de software, hardware, compilación C y semillas.
- `A.5_decisiones.tex`: Anexo E con el índice consolidado de 40 decisiones metodológicas.
*(Nota: No se modificó `A.3.2_figuras_eda.tex`, reservado para otro trabajador).*

### Herramientas y Scripts (`Code/tools/`)
- `Code/tools/tablas_anexos.py`: Script generador de tablas LaTeX (`booktabs` y `longtable`) a partir de CSVs y bitácora.

### Listados de Código Extraídos (`Docs/codigo/`)
- `m2_alineacion.py`: Alineación espacial de máscaras (`Code/2_Preprocessing.ipynb`, celda 5, ll. 1–10).
- `m2_componente.py`: Depuración de componente conexa mayor (`Code/2_Preprocessing.ipynb`, celda 11, ll. 1–13).
- `m2_recorte.py`: Recorte con margen de 20 px y exportación NRRD (`Code/2_Preprocessing.ipynb`, celda 13, ll. 7–26).
- `m3_configuracion.py`: Extractor PyRadiomics y 4 familias (`Code/3_Feature_Extraction.ipynb`, celda 3, ll. 1–13).
- `m4_seleccion.py`: Selección voraz ANOVA con $|r| \le 0.95$ (`Code/4_Selection_and_Scaling.ipynb`, celda 5, ll. 1–14).
- `m4_escalado.py`: Transformación angular por cuantiles a $[0, \pi]$ (`Code/4_Selection_and_Scaling.ipynb`, celda 8, ll. 4–13).
- `m4_folds.py`: Folds estratificados por paciente (`Code/4_Selection_and_Scaling.ipynb`, celda 9, ll. 1–12).
- `m5_embeddings.py`: Mapas C4/C5, ansatz con $\theta$ fijo y $\langle Z_i \rangle$ (`Code/5a_Embeddings.ipynb`, celda 2, ll. 10–20).
- `m5_kernels.py`: FidelityStatevectorKernel y RBF (`Code/5b_Quantum_Kernels.ipynb`, celda 4, ll. 11–26).
- `m6_geometric_difference.py`: Diferencia geométrica de Huang et al. (`Code/6_Separability.ipynb`, celda 3, ll. 20–33).
- `m6_kta_permutaciones.py`: KTA centrado y prueba de permutaciones (`Code/6_Separability.ipynb`, celda 3, ll. 36–48).
- `m7_mlp.py`: Definición de red MLP $k \to 32 \to 16 \to 1$ (`Code/7_Classification.ipynb`, celda 3, ll. 1–12).
- `m7_parada_temprana.py`: Bucle de optimización con parada temprana (`Code/7_Classification.ipynb`, celda 3, ll. 44–68).
- `m8_spearman.py`: Spearman con empates y nula exacta (`Code/8_Comparison.ipynb`, celda 6, ll. 1–21).
- `m8_muestreo.py`: Muestreo multinomial de disparos finitos (`Code/8_Comparison.ipynb`, celda 17, ll. 1–21).

### Tablas Generadas Automáticamente (`Docs/tablas/`)
- `anexo_b_m2_resumen.tex`: Auditoría de máscaras y preprocesamiento de imágenes (`2_preprocesamiento_resumen.csv`).
- `anexo_b_m4_seleccion.tex`: 12 características seleccionadas con $F$, $p$ y $|d|$ (`4_seleccion.csv`, `3_tamano_efecto.csv`).
- `anexo_b_m4_redundancia.tex`: Características descartadas por correlación $|r| > 0.95$ (`4_descartadas_redundancia.csv`).
- `anexo_b_m4_folds.tex`: Balance de lesiones, pacientes y malignidad por pliegue (`4_folds.csv`).
- `anexo_b_m5_tiempos.tex`: Costes temporales de kernels por vector de estado vs circuito (`5b_tiempos.csv`).
- `anexo_b_m8_oe6_qubits.tex`: Escalamiento exponencial con número de cúbits $k$ (`8_oe6_qubits.csv`).
- `anexo_b_x8_gradiente.tex`: Coste de cómputo de gradientes variacionales (`X8_costo_gradiente.csv`).
- `anexo_b_verificaciones.tex`: Consolidado de verificaciones automáticas de M5 a M8 (`5a_`, `5b_`, `6_`, `7_`, `8_verificaciones.csv`).
- `anexo_b_x5_auditoria.tex`: Auditoría metodológica independiente de 25 pruebas (`X5_auditoria.csv`).
- `anexo_d_paquetes.tex`: Versiones de software en `radiomics` y `qml_cancer` (`conda_list_*.txt`).
- `anexo_e_decisiones.tex`: Tabla `longtable` con las 40 decisiones D-001 a D-040 (`bitacora_decisiones.md`).

### Insumos y Registros Crudos (`Docs/insumos/noche/`)
- `conda_list_radiomics.txt`: Listado exportado de paquetes del entorno `radiomics`.
- `conda_list_qml_cancer.txt`: Listado exportado de paquetes del entorno `qml_cancer`.
- `informe_T4.md`: Este informe de actividades.

---

## 3. Detalle de Listados de Código Extraídos

| Etiqueta | Archivo destino | Cuaderno fuente | Celda código | Líneas | Decisión |
|---|---|---|---|---|---|
| `lst:m2_alineacion` | `Docs/codigo/m2_alineacion.py` | `Code/2_Preprocessing.ipynb` | 5 | 1–10 | D-020 |
| `lst:m2_componente` | `Docs/codigo/m2_componente.py` | `Code/2_Preprocessing.ipynb` | 11 | 1–13 | D-021 |
| `lst:m2_recorte` | `Docs/codigo/m2_recorte.py` | `Code/2_Preprocessing.ipynb` | 13 | 7–26 | D-022 |
| `lst:m3_extractor` | `Docs/codigo/m3_configuracion.py` | `Code/3_Feature_Extraction.ipynb` | 3 | 1–13 | D-008, D-023 |
| `lst:m4_seleccion` | `Docs/codigo/m4_seleccion.py` | `Code/4_Selection_and_Scaling.ipynb` | 5 | 1–14 | D-024 |
| `lst:m4_escalado` | `Docs/codigo/m4_escalado.py` | `Code/4_Selection_and_Scaling.ipynb` | 8 | 4–13 | D-025 |
| `lst:m4_folds` | `Docs/codigo/m4_folds.py` | `Code/4_Selection_and_Scaling.ipynb` | 9 | 1–12 | D-018, D-026 |
| `lst:m5_embeddings` | `Docs/codigo/m5_embeddings.py` | `Code/5a_Embeddings.ipynb` | 2 | 10–20 | D-014, D-031 |
| `lst:m5_kernels` | `Docs/codigo/m5_kernels.py` | `Code/5b_Quantum_Kernels.ipynb` | 4 | 11–26 | D-017, D-027 |
| `lst:m6_kta` | `Docs/codigo/m6_kta_permutaciones.py` | `Code/6_Separability.ipynb` | 3 | 36–48 | D-033 |
| `lst:m6_geometric_difference` | `Docs/codigo/m6_geometric_difference.py` | `Code/6_Separability.ipynb` | 3 | 20–33 | D-017, D-032 |
| `lst:m7_mlp` | `Docs/codigo/m7_mlp.py` | `Code/7_Classification.ipynb` | 3 | 1–12 | D-036 |
| `lst:m7_parada_temprana` | `Docs/codigo/m7_parada_temprana.py` | `Code/7_Classification.ipynb` | 3 | 44–68 | D-036 |
| `lst:m8_spearman` | `Docs/codigo/m8_spearman.py` | `Code/8_Comparison.ipynb` | 6 | 1–21 | D-039 |
| `lst:m8_muestreo` | `Docs/codigo/m8_muestreo.py` | `Code/8_Comparison.ipynb` | 17 | 1–21 | D-040 |

---

## 4. Detalle de Figuras Complementarias Incluidas

Se incorporaron las 12 figuras requeridas en `A.3.1_figuras.tex` garantizando la correspondencia con las fuentes primarias:
1. `M2_mask_alignment.png`: Desajustes por factor de escala ($0.870$) y traslación de origen (fuente: H-020).
2. `M2_preprocessing_examples.png`: Etapas de preprocesamiento, recortes y ecualización CLAHE (fuente: D-022).
3. `M5_circuit_12q.png`: Circuito variacional completo a $k = 12$ qubits con ancho ajustado a $0.6\textwidth$ por su formato vertical (fuente: D-031).
4. `M5_embeddings.png`: Distribución de valores esperados $\langle Z_i \rangle$ por dimensión (fuente: D-014).
5. `E1_circuit_complexity.png`: Profundidad y número de compuertas CNOT en función de $k$ (fuente: D-013).
6. `E2_training_cost.png`: Coste temporal por época y muestra en simuladores (fuente: D-013).
7. `E3_shots_sensitivity.png`: Sensibilidad a disparos finitos; pie redactado indicando el artefacto numérico de la referencia inicial aclarado por H-019 y corregido en B3 (fuente: H-016, H-019).
8. `E4_embedding_concentration.png`: Decaimiento exponencial de la dispersión de estados al crecer $k$ (fuente: H-018).
9. `X2_kernel_pairs_by_class.png`: Similitudes intraclase e interclase entre kernel clásico RBF y cuánticos C4/C5 con barrido de escala $c$ (fuente: H-036).
10. `X3_embedding_metrics_k8_k12.png`: Comparativa de separabilidad geométrica entre $k = 8$ y $k = 12$ qubits (fuente: H-041).
11. `X4_qsvm_scale.png`: Desempeño clasificador de QSVM frente a SVM clásico al variar $c$ (fuente: H-044).
12. `M8_spearman_null.png`: Distribución nula exacta de Spearman sobre las 120 permutaciones de las 5 condiciones con empates (fuente: H-049).

---

## 5. Salida Literal de las Pruebas de Aceptación

### Prueba 1: Verificación de Listados (`verificar_listados.py`)

```text
$ python3 Code/tools/verificar_listados.py Docs/capitulos/A_Anexos
m2_alineacion.py: OK
m2_componente.py: OK
m2_recorte.py: OK
m3_configuracion.py: OK
m4_escalado.py: OK
m4_folds.py: OK
m4_seleccion.py: OK
m5_embeddings.py: OK
m5_kernels.py: OK
m6_geometric_difference.py: OK
m6_kta_permutaciones.py: OK
m7_mlp.py: OK
m7_parada_temprana.py: OK
m8_muestreo.py: OK
m8_spearman.py: OK

15 listados; 0 problemas.
```

### Prueba 2: Compilación de Prueba de los Anexos (`compilar_prueba.sh A_Anexos`)

```text
$ bash Docs/capitulos/compilar_prueba.sh A_Anexos
Compila sin errores. PDF: /var/folders/0p/s82cs_hd6y38lrx5wgk261kr0000gn/T/tmp.XvFFisN9Qr/prueba.pdf
Referencias o citas sin resolver:
  ninguna
Cajas desbordadas (Overfull > 10pt):
  ninguna
```

### Prueba 3: Trazabilidad y Verificación de Cifras (`verificar_cifras_capitulos.py`)

```text
$ /opt/anaconda3/envs/qml_cancer/bin/python Code/tools/verificar_cifras_capitulos.py Docs/capitulos/A_Anexos
3 cifras: EN_BITACORA 3, EN_CSV 0, NO_ENCONTRADO 0, SIN_FUENTE 0
```

---

## 6. Observaciones Finales

- No se dejó ninguna etiqueta `[VERIFICAR]`; todos los datos, citas y parámetros provienen directamente de fuentes canónicas ejecutadas y comprobadas.
- No se modificó ningún archivo fuera del alcance asignado (`Technical_Report.tex`, `.bib`, `bitacora_decisiones.md`, `CLAUDE.md`, cuadernos `.ipynb`, datos en `Data/` ni `A.3.2_figuras_eda.tex` permanecen estrictamente intactos).
- No se realizaron commits ni operaciones de versionado en git.
