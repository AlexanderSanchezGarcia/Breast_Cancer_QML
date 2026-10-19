# Informe de Auditoría A2 · Consistencia numérica entre secciones

## 1. Alcance revisado

- **Documento maestro y capítulos (`.tex`):** `Docs/Technical_Report.tex` y todos los archivos en `Docs/capitulos/0_Preliminares/*.tex`, `Docs/capitulos/1_Panorama_General/*.tex`, `Docs/capitulos/2_Antecedentes/*.tex`, `Docs/capitulos/3_Marco_Teorico/*.tex`, `Docs/capitulos/4_EDA/*.tex`, `Docs/capitulos/5_Metodologia/*.tex`, `Docs/capitulos/6_Resultados/*.tex`, `Docs/capitulos/7_Conclusiones/*.tex`, `Docs/capitulos/8_Trabajo_Futuro/*.tex`, `Docs/capitulos/A_Anexos/*.tex` y `Docs/capitulos/G_Glosario/*.tex`.
- **Tablas generadas (`.tex`):** Los 19 archivos en `Docs/tablas/*.tex` y sus generadores `Code/tools/tablas_latex.py` y `Code/tools/tablas_anexos.py`.
- **Fuentes numéricas y registro canónico:** `Other/bitacora_decisiones.md`, `CLAUDE.md`, `Data/cbis_ddsm_unified.csv`, `Code/1_EDA.ipynb` y los archivos de resultados en `Code/results/*.csv`.

---

## 2. Comandos ejecutados y salida final (`verificar_cifras_capitulos.py`)

Comando ejecutado:

```sh
/opt/anaconda3/envs/qml_cancer/bin/python Code/tools/verificar_cifras_capitulos.py \
  Docs/capitulos/5_Metodologia \
  Docs/capitulos/6_Resultados \
  Docs/capitulos/7_Conclusiones \
  Docs/capitulos/8_Trabajo_Futuro \
  Docs/capitulos/0_Preliminares
```

Además se ejecutó sobre `Docs/capitulos/4_EDA`:

```sh
/opt/anaconda3/envs/qml_cancer/bin/python Code/tools/verificar_cifras_capitulos.py Docs/capitulos/4_EDA
```

### Salida resumida por carpeta

```text
=== Docs/capitulos/5_Metodologia ===
77 cifras: EN_BITACORA 5, EN_CSV 4, NO_ENCONTRADO 0, SIN_FUENTE 68

=== Docs/capitulos/6_Resultados ===
695 cifras: EN_BITACORA 563, EN_CSV 131, NO_ENCONTRADO 1, SIN_FUENTE 0

=== Docs/capitulos/7_Conclusiones ===
42 cifras: EN_BITACORA 40, EN_CSV 2, NO_ENCONTRADO 0, SIN_FUENTE 0

=== Docs/capitulos/8_Trabajo_Futuro ===
0 cifras: EN_BITACORA 0, EN_CSV 0, NO_ENCONTRADO 0, SIN_FUENTE 0

=== Docs/capitulos/0_Preliminares ===
12 cifras: EN_BITACORA 0, EN_CSV 0, NO_ENCONTRADO 0, SIN_FUENTE 12

=== Docs/capitulos/4_EDA ===
21 cifras: EN_BITACORA 2, EN_CSV 2, NO_ENCONTRADO 17, SIN_FUENTE 0
```

### Revisión manual de cada cifra marcada como `NO_ENCONTRADO` y `SIN_FUENTE`

1. **`Docs/capitulos/6_Resultados` (1 `NO_ENCONTRADO`):**
   - `6.7_lecciones_implementacion.tex:88` — cifra `2.1` en «A partir de Qiskit~2.1, la clase `\texttt{PauliFeatureMap}` está marcada como obsoleta» con comentario `% fuente: D-031`. En `Other/bitacora_decisiones.md` la entrada `D-031` dice «Qiskit 2.x deprecó la clase `PauliFeatureMap`» sin el decimal `2.1`, mientras que `CLAUDE.md:28` sí consigna «`PauliFeatureMap` (clase) está deprecada en Qiskit 2.1+». No es un error factual, sino de trazabilidad del comentario `% fuente:` (documentado en **A2-8**).
2. **`Docs/capitulos/0_Preliminares` (12 `SIN_FUENTE`):**
   - `resumen.tex:6` (`0.003`, `0.61`, `1.40`, `1.70`, `0.07`, `0.14`) y `abstract.tex:4` (`0.003`, `0.61`, `1.40`, `1.70`, `0.07`, `0.14`). Las 6 cifras coinciden exactamente con `6_alineamiento_kernel.csv`, `6_diferencia_geometrica_resumen.csv`, `7_test_diferencias.csv` y la bitácora (`H-031`, `H-039`, `H-040`, `H-042`). Aparecen como `SIN_FUENTE` porque `resumen.tex` solo tiene `% fuente:` antes del primer párrafo (líneas 2–3) y `abstract.tex` no incluye comentario `% fuente:` (documentado en **A2-8**).
3. **`Docs/capitulos/5_Metodologia` (68 `SIN_FUENTE`):**
   - 38 apariciones corresponden a coordenadas TikZ y anchos de tabla (`\arraystretch`, `cm`, `pt`) en `5.1_descripcion_general.tex`, `5.2_requerimientos.tex` y `5.7_M5_transformacion.tex`.
   - 30 apariciones son cifras del dominio en `5.2_requerimientos.tex` (`0.95`, `80.3`, `19.7`), `5.3_M1_lectura.tex` (`97.6`), `5.4_M2_preprocesamiento.tex` (`0.870`, `99.8`, `0.004`, `86.3`, `99.55`, `1.00`, `5.31`, `0.40`, `0.45`), `5.6_M4_seleccion.tex` (`0.95`, `0.05`), `5.8_M6_separabilidad.tex` (`0.87`, `1.19`, `0.045`, `0.25`, `0.5`, `0.025`, `0.05`, `0.1`, `0.2`, `0.02`) y `5.9_M7_clasificacion.tex` (`0.90`, `0.056`, `0.006`), cuyos párrafos carecen de comentario `% fuente:` individual. Todas coinciden con la bitácora y los CSV, salvo `0.056` en `5.9_M7_clasificacion.tex:16`, que arrastra la confusión entre conjunto total y conjunto de entrenamiento documentada en **A2-2**.
4. **`Docs/capitulos/4_EDA` (17 `NO_ENCONTRADO`):**
   - `4.1_validacion.tex:40` (`1.3` de `\arraystretch`), `4.1_validacion.tex:62-63` (`59.2`, `40.8`), `4.2_variable_objetivo.tex:31-35` (`1.45`, `1.16`, `1.78`), `4.3_variables_clinicas.tex:20,24,38,118,131` (`-0.03`, `0.09`, `-0.31`, `1.04`, `0.51`, `0.43`, `0.12`): verificadas contra `Data/cbis_ddsm_unified.csv` y `Code/1_EDA.ipynb` (el verificador no lee `.ipynb` ni `Data/cbis_ddsm_unified.csv`). Todas son exactas ($2111/3568 = 59.16\% \approx 59.2\%$, $1457/3568 = 40.84\% \approx 40.8\%$, ratios $2111/1457 = 1.4489 \approx 1.45$, $912/784 = 1.163 \approx 1.16$, $1199/673 = 1.7816 \approx 1.78$, $1819/1749 = 1.040$, y correlaciones $r = -0.0329$, $+0.0886$, $-0.3125$, $+0.5130$, $+0.4307$, $|r| \le 0.1065 < 0.12$).
   - En cambio, las cuatro cifras de `4.2_variable_objetivo.tex:68-70` (`3.1`, `2.8`, `3.4`, `3.2` para la media de `subtlety`) **no coinciden** ni con `Data/cbis_ddsm_unified.csv` ni con `Code/1_EDA.ipynb` (documentado en **A2-1**).

---

## 3. Tabla de cifras titulares

| Cifra titular | Apariciones (`archivo:línea`) | Fuente (`bitácora` / `CSV`) | Estado |
| :--- | :--- | :--- | :--- |
| **3,568 registros** (1,696 masas + 1,872 calcificaciones) | `Docs/capitulos/0_Preliminares/resumen.tex:4`, `abstract.tex:2`; `1_Panorama_General/1.3_justificacion.tex:60`; `4_EDA/4.0_introduccion.tex:15`, `4.1_validacion.tex:11,28,29,46,61`; `5_Metodologia/5.3_M1_lectura.tex:62,67`, `5.4_M2_preprocesamiento.tex:14`, `5.5_M3_extraccion.tex:35`; `6_Resultados/6.1_datos_caracteristicas.tex:10,23,24`, `6.4_qsvm_ventaja.tex:33`, `6.8_sintesis.tex:27`; `7_Conclusiones/7.2_objetivos.tex:15`; `A_Anexos/A.2_salidas.tex:17`; `Docs/tablas/anexo_b_m2_resumen.tex:13,14` | `H-001`, `D-005`; `Data/cbis_ddsm_unified.csv` (3,568 filas: 1,696 `mass`, 1,872 `calcification`), `2_preprocesamiento_resumen.csv` (`n_rows = 1696, 1872, 3568`) | **Consistente** |
| **1,566 pacientes únicos** (1,248 train / 349 test global, 31 solapados entre tipos; 691/201 masas, 602/151 calc., 0 solapes por subproblema) | `Docs/capitulos/1_Panorama_General/1.3_justificacion.tex:60`; `4_EDA/4.1_validacion.tex:48,79,80,82`; `5_Metodologia/5.3_M1_lectura.tex:11,68,69`; `6_Resultados/6.1_datos_caracteristicas.tex:118-121`; `Docs/tablas/anexo_b_x5_auditoria.tex:23,27` | `H-001`, `H-005`; `Data/cbis_ddsm_unified.csv` (`patient_id.nunique() == 1566`), `X5_auditoria.csv` (filas 8, 12) | **Consistente** |
| **Partición train/test: 2,864 / 704** (80.3 % / 19.7 %); **masas 1,318 / 378**; **calc. 1,546 / 326** | `Docs/capitulos/3_Marco_Teorico/3.2.7_parameter_shift.tex:30`; `4_EDA/4.1_validacion.tex:28-32,49,50`; `5_Metodologia/5.2_requerimientos.tex:295`; `6_Resultados/6.2_separabilidad.tex:20,148`, `6.4_qsvm_ventaja.tex:33`, `6.6_restricciones_simulador.tex:13`; `Docs/tablas/anexo_b_m4_seleccion.tex:16`, `anexo_b_m4_folds.tex:19` | `H-001`, `D-005`; `Data/cbis_ddsm_unified.csv`, `4_folds.csv` | **Consistente** |
| **Balance benigno/maligno: masas 912 / 784** (53.8 % / 46.2 %; train 681 / 637, test 231 / 147); **calc. 1,199 / 673** (64.0 % / 36.0 %; train 1,002 / 544, test 197 / 129); **total 2,111 / 1,457** | `Docs/capitulos/4_EDA/4.1_validacion.tex:51,52,62,63`, `4.2_variable_objetivo.tex:33-36`; `6_Resultados/6.1_datos_caracteristicas.tex:33`; `Docs/tablas/anexo_b_x5_auditoria.tex:19,20` | `H-001`, `D-005`; `Data/cbis_ddsm_unified.csv`, `X5_auditoria.csv` (filas 4–5) | **Consistente** |
| **80 máscaras desalineadas (78 masas a escala ~0.870 + 2 calc. con offset)**; 3,206/3,213 (99.8 %) recortes verificados; 7 discordantes (4 train, 3 test; $\Delta\text{AUC} \le 0.004$) | `Docs/capitulos/4_EDA/4.5_hallazgos.tex:86`; `5_Metodologia/5.4_M2_preprocesamiento.tex:13-23`; `6_Resultados/6.1_datos_caracteristicas.tex:11-20`, `6.3_clasificacion.tex:10`, `6.4_qsvm_ventaja.tex:10`; `7_Conclusiones/7.2_objetivos.tex:16`; `Docs/tablas/anexo_b_m2_resumen.tex:13,14,19` | `H-020`, `D-020`; `2_preprocesamiento_resumen.csv`, `2_discordantes_sensibilidad.csv` | **Consistente** |
| **67 características radiómicas**, **$k = 12$ seleccionadas** y comparación con **$k = 8$** | `Docs/capitulos/0_Preliminares/resumen.tex:4`, `abstract.tex:2`; `1_Panorama_General/1.3_justificacion.tex:66`, `1.5_alcance.tex:48,50`; `3_Marco_Teorico/3.2.4_paulifeaturemap.tex:30,65`, `3.5.1_radiomica.tex:11`; `5_Metodologia/5.1_descripcion_general.tex:37,43,133`, `5.2_requerimientos.tex:113,123,320,321`, `5.5_M3_extraccion.tex:10`, `5.6_M4_seleccion.tex:11,15,17,21,28`, `5.11_experimentos_complementarios.tex:16,35-38,52-56,73-77,84-90`; `6_Resultados/6.1_datos_caracteristicas.tex:84,136,165`, `6.2_separabilidad.tex:34,36,197-242`, `6.3_clasificacion.tex:43,48,72`, `6.4_qsvm_ventaja.tex:23,28,57`, `6.5_comparacion.tex:13,16,36`, `6.8_sintesis.tex:27,29,35,37,58,71,85`; `7_Conclusiones/7.1_respuesta.tex:13,28`, `7.2_objetivos.tex:17`, `7.3_causas.tex:14,23,51`, `7.5_aportaciones.tex:24`, `7.6_limitaciones.tex:18`; `8_Trabajo_Futuro/8.1_lineas.tex:50,79`; `Docs/tablas/m4_seleccion.tex:5`, `m7_clasificacion.tex:5` | `D-013`, `D-023`, `D-024`, `D-035`, `H-023`, `H-026`, `H-041`; `3_resumen_extraccion.csv`, `4_seleccion.csv`, `X3_comparacion_k8_k12.csv` | **Consistente** |
| **200 lesiones por subconjunto** (100 benignas + 100 malignas en M6; 19,900 pares fuera de la diagonal) | `Docs/capitulos/3_Marco_Teorico/3.4.1_kta.tex:55`, `3.4.2_geometric_difference.tex:76`; `5_Metodologia/5.2_requerimientos.tex:179,313`, `5.8_M6_separabilidad.tex:12,16`, `5.11_experimentos_complementarios.tex:43,142,143`; `6_Resultados/6.0_introduccion.tex:17`, `6.2_separabilidad.tex:11,65,110,140,161,213`, `6.5_comparacion.tex:13`, `6.6_restricciones_simulador.tex:10,13`, `6.7_lecciones_implementacion.tex:77`; `7_Conclusiones/7.1_respuesta.tex:21`, `7.4_viabilidad.tex:12,20,24`, `7.6_limitaciones.tex:31`; `8_Trabajo_Futuro/8.1_lineas.tex:61`; `Docs/tablas/m6_separabilidad_embeddings.tex:5`, `m6_separabilidad_kernels.tex:5` | `D-028`, `H-039`, `H-055`; `5b_concentracion.csv` (`n_off_diagonal_pairs = 19900`), `X9_submuestras_separabilidad.csv` | **Consistente** |
| **Semillas 42 (global / $\boldsymbol{\theta}$), 125 (folds masas) y 168 (folds calcificaciones)** | `Docs/capitulos/1_Panorama_General/1.5_alcance.tex:52`; `3_Marco_Teorico/3.2.6_quantum_embedding.tex:24`, `3.4.2_geometric_difference.tex:77`; `5_Metodologia/5.1_descripcion_general.tex:136`, `5.2_requerimientos.tex:162,206,281-283`, `5.6_M4_seleccion.tex:55`, `5.7_M5_transformacion.tex:101`, `5.8_M6_separabilidad.tex:13,61`, `5.9_M7_clasificacion.tex:21`, `5.11_experimentos_complementarios.tex:17,41,122-125`; `6_Resultados/6.1_datos_caracteristicas.tex:110-112`, `6.3_clasificacion.tex:40,48,56`, `6.7_lecciones_implementacion.tex:55`, `6.8_sintesis.tex:29,33,70`; `7_Conclusiones/7.2_objetivos.tex:31`; `A_Anexos/A.1_codigo.tex:79,91`, `A.4_entorno.tex:10,55,60`; `Docs/tablas/anexo_b_m4_folds.tex:10,24`, `x7_sorteos_theta.tex:20` | `D-014`, `D-026`, `H-027`, `H-053`; `4_semilla_folds.csv`, `X7_sorteos_theta.csv` | **Consistente** |
| **AUC-ROC en test del MLP por condición y diferencias C4/C5 − C1** (Masas: C1 `0.651`, C2 `0.651`, C3 `0.646`, C4 `0.530` [$\Delta = -0.120$, $p=0.003$], C5 `0.581` [$\Delta = -0.070$, $p=0.044$]; Calc.: C1 `0.769`, C2 `0.769`, C3 `0.758`, C4 `0.633` [$\Delta = -0.136$, $p=0.001$], C5 `0.652` [$\Delta = -0.117$, $p<0.001$]; pérdida de `0.07` a `0.14`) | `Docs/capitulos/0_Preliminares/resumen.tex:6`, `abstract.tex:4`; `6_Resultados/6.3_clasificacion.tex:10,16,19,22,69`, `6.4_qsvm_ventaja.tex:16,36`, `6.5_comparacion.tex:36`, `6.8_sintesis.tex:35,64`; `7_Conclusiones/7.1_respuesta.tex:25,26`, `7.2_objetivos.tex:26,33`; `Docs/tablas/m7_clasificacion.tex:12-23`, `m7_diferencias.tex:12-30` | `H-042`; `7_test.csv`, `7_test_diferencias.csv` (`delta_auc_B_minus_A = -0.1204, -0.0697, -0.1363, -0.1173`) | **Consistente** |
| **AUC-ROC en test del QSVM vs SVM clásico (X4)** (Masas: C1 lin `0.630`, C1 RBF `0.649`, C4 $c=1$ `0.594`, C4 $c^*$ `0.630`, C5 $c=1$ `0.599`, C5 $c^*$ `0.625`; Calc.: C1 lin `0.766`, C1 RBF `0.769`, C4 $c=1$ `0.733`, C4 $c^*$ `0.779` [$\Delta = +0.010$ vs RBF, $+0.013$ vs lin], C5 $c=1$ `0.648`, C5 $c^*$ `0.788` [$\Delta = +0.019$ vs RBF, $+0.022$ vs lin]) | `Docs/capitulos/0_Preliminares/resumen.tex:6`, `abstract.tex:4`; `6_Resultados/6.4_qsvm_ventaja.tex:10,13,16,23`, `6.8_sintesis.tex:67`; `7_Conclusiones/7.1_respuesta.tex:27`, `7.3_causas.tex:35-38`, `7.5_aportaciones.tex:41`; `Docs/tablas/x4_qsvm.tex:12-27` | `H-044`, `H-045`; `X4_test.csv`, `X4_test_diferencias.csv` | **Consistente** |
| **KTA (exceso sobre permutación)** (Kernels a $c=1$: C4/C5 `0.003` y `0.005` en masas, `0.006` y `0.007` en calc., frente a RBF `0.049` y `0.151`; Lineal sobre $\langle Z_i\rangle$: C4/C5 `-0.0005` y `+0.0033` en masas, `-0.0009` y `+0.0007` en calc., frente a C1–C3 `0.029–0.036` y `0.119–0.132`) | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:60,115,116,133,222,223`, `6.8_sintesis.tex:31,51`; `7_Conclusiones/7.1_respuesta.tex:16,19`, `7.2_objetivos.tex:22`; `Docs/tablas/m6_separabilidad_kernels.tex:13-28`, `m6_separabilidad_embeddings.tex:14-26` | `H-039`, `H-040`, `H-055`; `6_alineamiento_kernel.csv`, `6_separabilidad_embeddings.csv`, `X9_submuestras_separabilidad.csv` | **Consistente** |
| **Diferencia geométrica $g$** (`1.40` a `1.70` mínima regularizada a $c=1$: masas `1.43` y `1.51`, calc. `1.40` y `1.70`, con $\sqrt{N}\approx 14.1$; con entrenabilidad $\le 0.045$: `1.62`, `1.63`, `1.41`, `1.70`; sin regularizar $\lambda=0$: `379`, `388`, `306`, `331`) | `Docs/capitulos/0_Preliminares/resumen.tex:6`, `abstract.tex:4`; `6_Resultados/6.2_separabilidad.tex:77,78,82,83,224`, `6.8_sintesis.tex:31,55`; `7_Conclusiones/7.1_respuesta.tex:17`, `7.2_objetivos.tex:22`, `7.5_aportaciones.tex:36`; `Docs/tablas/m6_separabilidad_kernels.tex:14,15,18,19,22,23,26,27` | `H-039`; `6_diferencia_geometrica_resumen.csv` (`g_min_over_grid = 1.430, 1.509, 1.396, 1.700`; `g_unregularized_median_gamma = 378.79, 387.84, 305.51, 331.33`) | **Consistente** |
| **Dimensión efectiva $d_{\text{eff}}$** (`167.6` a `187.7` en un decimal, o `168` a `188` redondeado a enteros: C4 `184.0` y `187.7`, C5 `171.3` y `167.6`, frente a RBF `13.4` y `13.2` con $N=200$) | `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:61,134,221`, `6.8_sintesis.tex:31,54`; `7_Conclusiones/7.1_respuesta.tex:16`, `7.3_causas.tex:17`; `Docs/tablas/m6_separabilidad_kernels.tex:14,15,18,19,22,23,26,27` | `H-039`, `H-055`; `6_dimension_efectiva.csv` (`d_eff_lambda_0p01 = 184.02, 171.29, 187.66, 167.64`, `K_C = 13.43, 13.19`) | **Consistente** |
| **Mediana fuera de la diagonal del kernel** (C4 `0.0024` / `0.0033` $\approx 0.002\text{--}0.003$, C5 `0.00003` [$3.2\times 10^{-5}$ y $2.9\times 10^{-5}$], frente a RBF `0.610` y `0.613` $\approx 0.61$) | `Docs/capitulos/0_Preliminares/resumen.tex:6`, `abstract.tex:4`; `6_Resultados/6.2_separabilidad.tex:13,15,59-61,220`, `6.8_sintesis.tex:31,51`; `7_Conclusiones/7.1_respuesta.tex:16`, `7.3_causas.tex:15,16`; `Docs/tablas/m6_separabilidad_kernels.tex:14,15,18,19,22,23,26,27` | `H-037`, `H-039`; `5b_concentracion.csv`, `6_dimension_efectiva.csv` (`off_diag_median`) | **Consistente** |
| **Correlación de Spearman $\rho_s$ (`0.67` a `0.97`; `0.667` a `0.975`) y $p$ exacta con $n=5$ (`p = 4/120 = 0.033` con un empate; `1/120 = 0.0083` sin empates)** | `Docs/capitulos/3_Marco_Teorico/3.4.8_spearman.tex:37`; `6_Resultados/6.5_comparacion.tex:10,13,16`, `6.8_sintesis.tex:35,71`; `7_Conclusiones/7.1_respuesta.tex:28`, `7.2_objetivos.tex:34`; `Docs/tablas/m8_spearman.tex:13-22` | `D-039`, `H-049`; `8_spearman.csv` (`spearman_rho` entre `0.666886` y `0.974679`, `p_exact_permutation = 0.033333`) | **Consistente** |
| **Dispersión por dimensión de $\langle Z_i \rangle$ en C4 y C5** (`0.056` vs. `0.058` en C4 masas; `0.048` en C4 calc.; `0.180` y `0.178` en C5) | `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:16` (`0.056`); `6_Resultados/6.2_separabilidad.tex:21` (`0.056` atribuido a 1,318 masas de train), `6.2_separabilidad.tex:225` (`0.058` en train), `6.3_clasificacion.tex:43` (`0.058`), `6.4_qsvm_ventaja.tex:105` (`0.058`); `Docs/tablas/x8_theta_entrenado.tex:17` (`0.058`) | `H-037`, `H-041`, `H-054`; `5a_resumen.csv` (`0.0565` en train+test, $n=1696$) vs. `X3_comparacion_k8_k12.csv` y `X8_theta_entrenado.csv` (`0.0579` en train, $n=1318$) | **Inconsistente (ver A2-2)** |
| **OE-6: qubits en 24 h (`k ≈ 25` embeddings, `k ≈ 22` kernel $200\times 200$, `k = 14` vs `14–15` / `15` en *parameter-shift*), `1,024` disparos, `15.7 %–74.5 %` (`16 %–74 %`) de lecturas nulas, y costo de *parameter-shift* (`5.16 s/lesión`, `205 h` en X8 vs `381.7 h` [2 mapas, B1] vs `5.7 h` [Aer crudo en Tabla B.8])** | `Docs/capitulos/0_Preliminares/resumen.tex:6`, `abstract.tex:4`; `3_Marco_Teorico/3.2.7_parameter_shift.tex:30`; `5_Metodologia/5.9_M7_clasificacion.tex:36`; `6_Resultados/6.3_clasificacion.tex:72`, `6.6_restricciones_simulador.tex:10,13,23,26`, `6.8_sintesis.tex:29,37,80-85`; `7_Conclusiones/7.4_viabilidad.tex:11-26`; `8_Trabajo_Futuro/8.1_lineas.tex:62`; `Docs/tablas/anexo_b_m8_oe6_qubits.tex:14-16`, `anexo_b_x8_gradiente.tex:12` | `H-051`, `H-052`, `H-054`, `D-040`; `8_oe6_qubits.csv`, `8_oe6_resumen.csv`, `8_oe6_shots_kernel.csv`, `X8_costo_gradiente.csv`, `B1_benchmark_arquitectura.csv` | **Inconsistencia parcial en costo de entrenamiento por mapa (ver A2-4)** |
| **Cifras residuales de TT1** (`97.6 %` de cobertura, `224×224`, «100–300 features», `TorchConnector`, `MinMaxScaler`, `['X','ZZ']`, `PauliFeatureMap` como clase) | `Docs/capitulos/1_Panorama_General/1.2_planteamiento.tex:84,94`, `1.3_justificacion.tex:30`, `1.4_objetivos.tex:22,46`, `1.5_alcance.tex:47`; `2_Antecedentes/2.1.3_fundamentos_qml.tex:46,51`; `3_Marco_Teorico/3.2.4_paulifeaturemap.tex:6,9`, `3.3.3_integracion.tex:12`, `3.3.4_implementacion_qiskit.tex:17,19`; `4_EDA/4.1_validacion.tex:64`; `5_Metodologia/5.3_M1_lectura.tex:59`, `5.4_M2_preprocesamiento.tex:40`, `5.7_M5_transformacion.tex:87`; `6_Resultados/6.1_datos_caracteristicas.tex:97`, `6.7_lecciones_implementacion.tex:88,89`, `6.8_sintesis.tex:29`; `7_Conclusiones/7.1_respuesta.tex:11`, `7.5_aportaciones.tex:46`; `Docs/tablas/anexo_e_decisiones.tex:19,26,32` | `D-001` a `D-031`, `H-018` | **Consistente** (todas aparecen únicamente como contexto histórico/descartado o nombre conceptual; ninguna figura como decisión activa del pipeline) |

---

## 4. Hallazgos

### A2-1 · ALTA · Discrepancia con datos fuente (`Data/cbis_ddsm_unified.csv` y `Code/1_EDA.ipynb`)
- Ubicación: `Docs/capitulos/4_EDA/4.2_variable_objetivo.tex:67-70`
- Texto: «La media de \textit{subtlety} en casos malignos (3.1 para masas, 2.8 para calcificaciones) es ligeramente inferior a la de casos benignos (3.4 y 3.2 respectivamente), aunque la diferencia es pequeña.»
- Problema: Las cuatro medias reportadas para `subtlety` (`3.1`, `2.8`, `3.4` y `3.2`) no coinciden con el conjunto de datos unificado ni con la salida del cuaderno `Code/1_EDA.ipynb`. Además, en el subconjunto de masas el sentido de la diferencia está invertido: las masas malignas presentan una media de `subtlety` ligeramente mayor que las benignas, no menor.
- Evidencia: En `Data/cbis_ddsm_unified.csv` y en la salida impresa de la celda 32 de `Code/1_EDA.ipynb` (`=== SUBTLETY POR PATOLOGIA ===`), la columna `subtlety` registra para `finding_type == 'mass'`: `BENIGN` media `3.88` (`3.881579`, mediana `4.0`, $n=912$) y `MALIGNANT` media `3.98` (`3.977041`, mediana `4.0`, $n=784$, correlación con `label` de $r = +0.042504$); para `finding_type == 'calcification'`: `BENIGN` media `3.49` (`3.489575`, mediana `3.0`, $n=1199$) y `MALIGNANT` media `3.23` (`3.227340`, mediana `3.0`, $n=673$, correlación con `label` de $r = -0.106539$). Asimismo, `Code/tools/verificar_cifras_capitulos.py Docs/capitulos/4_EDA` marca las cuatro cifras (`3.1`, `2.8`, `3.4`, `3.2`) como `NO_ENCONTRADO`.
- Propuesta: Reemplazar las cifras por las medias reales de `1_EDA.ipynb` (`3.98` frente a `3.88` en masas, y `3.23` frente a `3.49` en calcificaciones, con medianas de `4.0` en masas y `3.0` en calcificaciones), precisando que solo en calcificaciones la media en casos malignos es ligeramente inferior a la de benignos.

### A2-2 · ALTA · Contradicción entre secciones por confusión de muestra (entrenamiento vs. total del dataset)
- Ubicación: `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:20-23` (y `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:16`)
- Texto: «Sobre todas las lesiones del conjunto de entrenamiento (1\,318 masas y 1\,546 calcificaciones), la desviación estándar media por dimensión de los valores esperados $\langle Z_i \rangle$ fue de 0.056 en masas y 0.048 en calcificaciones para C4, mientras que en C5 ascendió a 0.180 en masas y 0.178 en calcificaciones.»
- Problema: El párrafo declara explícitamente que el cálculo se realiza sobre el conjunto de entrenamiento (`1,318` masas), pero reporta `0.056` para C4 en masas, lo que contradice la Tabla 6.3 de la misma sección y los capítulos posteriores, donde el valor sobre el conjunto de entrenamiento de masas es `0.058`. La cifra `0.056` corresponde al conjunto completo de `1,696` masas (entrenamiento + prueba).
- Evidencia:
  1. En la misma sección, `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:225` (Tabla `tab:comparacion_k8_k12`) consigna: `Dispersión \langle Z_i \rangle en todo el train (C4 / C5) & 0.058 / 0.180`; igualmente, `Docs/capitulos/6_Resultados/6.3_clasificacion.tex:43` dice «disminuye en C4 (de 0.058 a 0.047 en masas)», `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:105` dice «la dispersión por dimensión de $\langle Z_i \rangle$ aumentó de 0.058 a 0.067 en masas» y `Docs/tablas/x8_theta_entrenado.tex:17` reporta `0.058 (0.067)`.
  2. En `Code/results/5a_resumen.csv` (fila `subset=mass, condition=C4`, columna `std_mean_by_dimension = 0.05649745020593691`), la desviación estándar media se calculó sobre las **1,696 lesiones totales (entrenamiento + prueba)** (como indica `Other/bitacora_decisiones.md` en `H-037`: «Sobre todas las lesiones»), mientras que sobre las **1,318 lesiones de entrenamiento** (`Code/results/X3_comparacion_k8_k12.csv`, fila `finding_type=mass, family="B, embeddings (full train)", metric="mean per-dimension std", object=C4, k=12`, columna `value = 0.05792197848394025`, y `Code/results/X8_theta_entrenado.csv`, fila `subset=mass, condition=C4`, columna `dispersion_theta_fixed = 0.05794417118678791`) el valor es `0.058`.
- Propuesta: En `Docs/capitulos/6_Resultados/6.2_separabilidad.tex:21` (y en `Docs/capitulos/5_Metodologia/5.9_M7_clasificacion.tex:16`), sustituir `0.056` por `0.058` para que corresponda efectivamente a las 1,318 lesiones de entrenamiento y coincida con la Tabla 6.3, §6.3 y §6.4 (o bien aclarar en `6.2_separabilidad.tex:20` que `0.056` se midió sobre las 1,696 lesiones totales de `5a_resumen.csv`).

### A2-3 · MEDIA · Contradicción aparente entre tablas y secciones en el costo de entrenamiento por *parameter-shift* a $k = 12$ (`5.7 h` vs. `205 h` vs. `381.7 h`) y el techo de `14–15` qubits en 24 h
- Ubicación: `Docs/capitulos/7_Conclusiones/7.4_viabilidad.tex:12-15`, `Docs/capitulos/6_Resultados/6.8_sintesis.tex:29,37` y `Docs/tablas/anexo_b_m8_oe6_qubits.tex:14-15`
- Texto: «El límite lo impuso el gradiente: entrenar los parámetros variacionales por \textit{parameter-shift}, la regla que funciona en \textit{hardware}, cuesta 5.16\,s por lesión a $k = 12$, unas 205\,h para 50 épocas, y deja de caber en un día a partir de unos 15 qubits.» (`7.4_viabilidad.tex:12-15`); «extracción analítica en 0.20\,h frente a 381.7\,h de Arquitectura~A» (`6.8_sintesis.tex:29`); `12 & Medido & 0.06 MiB & 0.0029 & 0.006 & 5.7 \\` (`Docs/tablas/anexo_b_m8_oe6_qubits.tex:14`).
- Problema: Se mezclan sin aclaración tres mediciones distintas del tiempo de entrenamiento de 50 épocas por *parameter-shift* a $k = 12$: (1) `205 h` por mapa (`5.16 s/lesión` con `EstimatorQNN` en `X8_costo_gradiente.csv`), (2) `381.7 h` para ambos mapas (`190.9 h` por mapa, `4.70 s/lesión` con `EstimatorQNN` en `B1_benchmark_arquitectura.csv`), y (3) `5.7 h` por mapa a $k = 12$ y `14.8 h` a $k = 14$ en `8_oe6_qubits.csv` / Tabla `tab:anexo_m8_oe6_qubits` (que proyecta 49 evaluaciones multiplicando el tiempo crudo de `AerSimulator` de `2.9 ms/estado` sin la sobrecarga de `EstimatorQNN`). En consecuencia, `7.4_viabilidad.tex:14-15` afirma en la misma oración que a $k = 12$ toma `205 h` (8.5 días) y que «deja de caber en un día [24 h] a partir de unos 15 qubits», y la Tabla B.8 (`5.7 h` a $k=12$) parece contradecir la Tabla B.11 (`205.21 h` a $k=12$).
- Evidencia:
  1. `Code/results/X8_costo_gradiente.csv` (fila `method="parameter shift (EstimatorQNN, exact)"`): `seconds_per_lesion = 5.158895`, `hours_50_epochs_train = 205.209377` (reproducido en `Docs/tablas/anexo_b_x8_gradiente.tex:12`).
  2. `Code/results/B1_benchmark_arquitectura.csv` (fila `architecture="A: end-to-end (TorchConnector, 50 ep)"`) y `Code/results/8_oe6_resumen.csv` (filas 3–4): `bwd_per_sample_s = 4.704788`, `190.863614 h` por mapa y `total_hours = 381.727227` para los dos mapas (`6.8_sintesis.tex:29`).
  3. `Code/results/8_oe6_qubits.csv` (filas `k=12, 14, 15`, columna `training_A_hours_per_map`): `5.704805` h ($k=12$), `14.825054` h ($k=14$) y `36.676908` h ($k=15$), calculados como $50 \times 2864 \times 49 \times \text{seconds\_per\_state} / 3600$ con `AerSimulator` directo (`0.002927 s` a $k=12$), de donde proviene `largest viable k: training theta by parameter-shift in 24 h (one map) = 14` en `8_oe6_resumen.csv` (fila 12).
- Propuesta: Aclarar explícitamente en `6.6_restricciones_simulador.tex:10-13`, `7.4_viabilidad.tex:13-15` y el pie de `Docs/tablas/anexo_b_m8_oe6_qubits.tex` que el techo de `14–15` qubits en 24 h (`5.7 h` a $k=12$, `14.8 h` a $k=14$) corresponde al tiempo puro de simulación en `AerSimulator` (`2.9 ms/circuito` a $k=12$), mientras que con la primitiva `EstimatorQNN` (`93–107 ms/circuito`) el costo a $k = 12$ asciende a `191–205 h` por mapa (`381.7 h` para ambos mapas en el benchmark B1).

### A2-4 · MEDIA · Conteo e índice de decisiones desactualizados en Anexo E (`40` decisiones `D-001` a `D-040` en vez de `42` decisiones `D-001` a `D-042`) y numeración de secciones obsoleta
- Ubicación: `Docs/capitulos/A_Anexos/A.5_decisiones.tex:3,10-12` y `Docs/tablas/anexo_e_decisiones.tex:18-57`
- Texto: «La Tabla~\ref{tab:anexo_decisiones} recopila el índice cronológico de las 40 decisiones metodológicas registradas (D-001 a D-040), identificando su estado de vigencia y las secciones correspondientes del cuerpo del reporte que fundamentan.»
- Problema: El Anexo E reporta 40 decisiones (`D-001` a `D-040`), omitiendo `D-041` y `D-042`, que forman parte de la bitácora canónica y se citan en el cuerpo del reporte. Asimismo, la columna `Sección en reporte` de `Docs/tablas/anexo_e_decisiones.tex` mantiene la numeración de capítulos anterior al 2026-10-14 (`\S\,4.1` a `\S\,4.10` para Metodología y `\S\,8.x` para Anexos), cuando en el reporte final el Capítulo 4 es el EDA (`§4.1`–`§4.5`), Metodología es el Capítulo 5 (`§5.1`–`§5.11`) y el Capítulo 8 es Trabajo Futuro (`§8.1`).
- Evidencia: En `Other/bitacora_decisiones.md:26-67` existen **42** decisiones (`D-001` a `D-042`), y `D-042` aparece referenciada en `Docs/capitulos/5_Metodologia/5.8_M6_separabilidad.tex:4`, `5.11_experimentos_complementarios.tex:4`, `6_Resultados/6.2_separabilidad.tex:3`, `7_Conclusiones/7.4_viabilidad.tex:3`, `7.6_limitaciones.tex:3` y `8_Trabajo_Futuro/8.1_lineas.tex:3,58,88`.
- Propuesta: Actualizar `Docs/capitulos/A_Anexos/A.5_decisiones.tex:3,11` a `42 decisiones metodológicas registradas (D-001 a D-042)`, agregar las filas `D-041` y `D-042` en `Docs/tablas/anexo_e_decisiones.tex` y corregir en esa tabla las referencias `\S\,4.x` por `\S\,5.x` y `\S\,8.x` por los anexos correspondientes.

### A2-5 · BAJA · Discrepancia por truncamiento entero en la dimensión mediana de las lesiones de masas (`302×304` en Tabla B.1 vs. `302×304.5` / `302×305` en CSV y bitácora)
- Ubicación: `Docs/tablas/anexo_b_m2_resumen.tex:14`
- Texto: «`Masas & 1696 & 78 & 1464 & 1543 & 75 & 302$\times$304 & 67 \\`»
- Problema: La Tabla B.1 (`tab:anexo_m2_resumen`) reporta `302×304` píxeles como dimensión mediana de lesión en masas porque el script generador trunca con `int()` el valor `304.5` del CSV, discrepando de la bitácora (`302 × 304.5 px` en `D-022` y `302 × 305 px` en `H-022`).
- Evidencia: En `Code/results/2_preprocesamiento_resumen.csv` (fila `finding_type=mass`), las columnas son `median_bbox_h = 302.0` y `median_bbox_w = 304.5`. En `Code/tools/tablas_anexos.py:76`, la instrucción `f"{int(r['median_bbox_h'])}$\\times${int(r['median_bbox_w'])}"` trunca `304.5` a `304`, mientras que `Other/bitacora_decisiones.md` consigna `302 × 304.5 px` (`D-022`, línea 526) y `302 × 305 px` (`H-022`, línea 1052).
- Propuesta: Formatear `median_bbox_w` en `Docs/tablas/anexo_b_m2_resumen.tex:14` (y en `Code/tools/tablas_anexos.py:76`) como `302$\times$304.5` o redondeado a `302$\times$305` para coincidir con `2_preprocesamiento_resumen.csv` y la bitácora.

### A2-6 · BAJA · Truncamiento a `0.0` de discrepancias numéricas no nulas en la Tabla B.10 (`tab:anexo_x5_auditoria`)
- Ubicación: `Docs/tablas/anexo_b_x5_auditoria.tex:29-32,37-39`
- Texto: «`\quad mass: C4 compute-uncompute kernel equals statevector kernel (12 x 12) & 0.0 & Superada \\`» (y líneas 30–32, 37–39 con valor `0.0`).
- Problema: La Tabla B.10 muestra `0.0` exacto en la columna `Discrepancia máx.` para las pruebas de equivalencia de kernels cuánticos y de codificación, mientras que el texto de la sección 6.4 informa que dichas discrepancias son del orden de $10^{-11}$ (inferiores a $6 \times 10^{-11}$).
- Evidencia: En `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex:19` se afirma que «ambas construcciones coincidieron con una diferencia máxima inferior a $6 \times 10^{-11}$», lo que respalda `Code/results/X5_auditoria.csv` en la columna `max_discrepancy`: filas 14–17 (`4.229421e-11`, `9.404812e-13`, `5.744050e-11`, `3.224998e-11`) y filas 20–22 (`6.106227e-15`, `1.110223e-16`, `4.718448e-16`). Sin embargo, `Code/tools/tablas_anexos.py:376` convierte a `'0.0'` cualquier valor menor o igual a `1e-6`.
- Propuesta: Mostrar notación científica (`4.23e-11`, `9.40e-13`, `5.74e-11`, `3.22e-11`, etc.) en `Docs/tablas/anexo_b_x5_auditoria.tex:29-32,37-39` cuando `max_discrepancy > 0`, reservando `0.0` para ceros exactos.

### A2-7 · BAJA · Enumeración incompleta de experimentos complementarios en Anexo D (`X1 al X6` en lugar de `X1 al X9`)
- Ubicación: `Docs/capitulos/A_Anexos/A.4_entorno.tex:65-68`
- Texto: «La totalidad del pipeline experimental (Módulos 2 al 8 y experimentos complementarios X1 al X6) fue objeto de un protocolo de re-ejecución completa y verificación independiente entre el 8 y el 10 de octubre de 2026 sobre un clon limpio del repositorio, constatándose la reproducción exacta e invariable de todas las predicciones, métricas y tablas numéricas obtenidas.»
- Problema: El texto identifica «La totalidad del pipeline experimental» con «Módulos 2 al 8 y experimentos complementarios X1 al X6», omitiendo que el reporte técnico integra nueve experimentos complementarios (`X1` a `X9`), cuyos resultados y tablas forman parte de los capítulos 5, 6 y Anexo B.
- Evidencia: `Docs/capitulos/5_Metodologia/5.11_experimentos_complementarios.tex:6-172` define y tabula los nueve experimentos complementarios `X1` a `X9` (Tabla `tab:experimentos_complementarios`), y `Docs/capitulos/A_Anexos/A.2_salidas.tex:120-165` e `Other/bitacora_decisiones.md` (`D-042`, `H-053`, `H-054`, `H-055`) documentan `X7`, `X8` y `X9` ejecutados entre el 12 y el 18 de octubre de 2026.
- Propuesta: Precisar en `Docs/capitulos/A_Anexos/A.4_entorno.tex:65-66` que la re-ejecución del 8–10 de octubre cubrió los Módulos 2 al 8 y `X1` al `X6`, y que los experimentos `X7` al `X9` se ejecutaron y verificaron bajo el mismo entorno y semillas entre el 12 y el 18 de octubre de 2026.

### A2-8 · BAJA · Comentarios de trazabilidad `% fuente:` ausentes o incompletos detectados por `verificar_cifras_capitulos.py`
- Ubicación: `Docs/capitulos/0_Preliminares/resumen.tex:6`, `Docs/capitulos/0_Preliminares/abstract.tex:2-4`, `Docs/capitulos/6_Resultados/6.7_lecciones_implementacion.tex:87-88` y `Docs/capitulos/5_Metodologia/5.2_requerimientos.tex`, `5.3_M1_lectura.tex`, `5.4_M2_preprocesamiento.tex`, `5.6_M4_seleccion.tex`, `5.8_M6_separabilidad.tex`, `5.9_M7_clasificacion.tex`
- Texto: «`% fuente: D-031` / `\textbf{Obsolescencia de \texttt{PauliFeatureMap} en Qiskit~2.x.} A partir de Qiskit~2.1...`» (`6.7_lecciones_implementacion.tex:87-88`); segundo párrafo de `resumen.tex:6` y todo `abstract.tex:2-4` sin línea `% fuente:` inmediata.
- Problema: El script `Code/tools/verificar_cifras_capitulos.py` asocia cada comentario `% fuente:` únicamente al bloque de texto inmediatamente siguiente (separado por líneas en blanco). Debido a ello, marca 12 cifras como `SIN_FUENTE` en `0_Preliminares`, 30 cifras de dominio como `SIN_FUENTE` en `5_Metodologia`, y 1 cifra (`2.1`) como `NO_ENCONTRADO` en `6.7_lecciones_implementacion.tex:88` (porque `D-031` en `Other/bitacora_decisiones.md` dice `Qiskit 2.x` y no `2.1`).
- Evidencia: Salida de `Code/tools/verificar_cifras_capitulos.py` reproducida en la Sección 2 de este informe (`0_Preliminares`: `SIN_FUENTE 12`; `5_Metodologia`: `SIN_FUENTE 68`; `6_Resultados`: `NO_ENCONTRADO 1` en `6.7_lecciones_implementacion.tex` para `2.1 [D-031]`).
- Propuesta: Añadir el comentario `% fuente:` antes del segundo párrafo de `resumen.tex` y de los dos párrafos de `abstract.tex` (incluyendo `6_alineamiento_kernel.csv, 6_diferencia_geometrica_resumen.csv, 7_test_diferencias.csv`), agregar `% fuente:` en los párrafos con cifras de `5_Metodologia/*.tex` y precisar `Qiskit 2.1` en `D-031` (o cambiar a `Qiskit~2.x` en `6.7_lecciones_implementacion.tex:88`).

---

## 5. Conteo de hallazgos por severidad

- **ALTA:** 2 (`A2-1`, `A2-2`)
- **MEDIA:** 2 (`A2-3`, `A2-4`)
- **BAJA:** 4 (`A2-5`, `A2-6`, `A2-7`, `A2-8`)
- **Total:** 8 hallazgos

---

## 6. Verificación de estado del repositorio (`git status --short`)

Comando ejecutado al finalizar:

```sh
git -C /Users/alexander_san/TT status --short
```

Salida obtenida:

```text
?? Docs/articulo/
?? Docs/insumos/auditoria/glosario_borrador.tex
?? Docs/insumos/auditoria/informe_A2.md
?? Docs/insumos/auditoria/informe_A3.md
?? Docs/insumos/auditoria/informe_A4.md
?? Docs/insumos/auditoria/informe_A5.md
?? Docs/insumos/auditoria/informe_G1.md
?? Docs/insumos/auditoria/informe_W1.md
```

Se confirma que esta tarea únicamente creó el archivo `Docs/insumos/auditoria/informe_A2.md` dentro de `Docs/insumos/auditoria/` y no modificó ningún archivo versionado del repositorio.
