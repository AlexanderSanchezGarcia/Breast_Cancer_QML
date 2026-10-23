# X10 · Progreso y protocolo (archivo de relevo)

ESTADO: COMPLETO

Si eres un agente que retoma esta tarea (automatización de Orca «X10 relevo»):
1. Lee `CLAUDE.md` y este archivo completo. **No edites `Docs/Technical_Report.tex` ni los capítulos de `Docs/capitulos/`.**
2. Continúa desde la primera casilla sin marcar. Marca cada casilla al terminarla y actualiza la línea «Última actividad».
3. Al terminar todo, cambia la primera línea a `ESTADO: COMPLETO` y desactiva la automatización: `orca automations list --json`, y luego `orca automations edit <id> --disabled --json`.
4. No hagas commits. Sin menciones de IA en ningún archivo.

Última actividad: 2026-10-21 23:47 (sesión principal; tarea completa)

## Contexto

En la revisión del 2026-10-21, un sinodal pidió:
- (a) justificar por qué 5 folds; dijo que eran muchos;
- (b) probar árboles de decisión, *random forest* y XGBoost, documentando cómo se detiene el árbol (profundidad y pureza del nodo), y explicar por qué pasa lo que pasa si dan mejores resultados.

El autor decidió:
- mantener k = 5 y añadir una sensibilidad con 3 folds;
- dejar fuera el MLP profundo (trabajo futuro);
- correr los árboles sobre C1–C5.

La comprobación de balance con 3 a 10 folds ya está hecha; los números van abajo.

## Protocolo fijado ANTES de correr (D-043, provisional)

**Pregunta principal:** con el **mismo clasificador**, ¿alguna condición cuántica (C4, C5) supera a C1? Las comparaciones principales son, dentro de cada clasificador: C4−C1, C5−C1, C4−C3, C5−C3, C2−C1 y C5−C4.

**Datos.**
- Entradas: `Data/processed/m5/emb_<ft>.parquet`, columnas `C1_01…C5_12`, `fold`, `split`, `label`, `patient_id`, `case_id`.
- Folds congelados de M4.
- El test se usa una vez por modelo.

**Clasificadores**, con la misma malla para las cinco condiciones y semilla 42:
- **DT-depth:** `DecisionTreeClassifier(criterion='gini', class_weight='balanced')`, `max_depth` ∈ {1, …, 12}.
- **DT-purity:** el árbol completo, cuya predicción se detiene en el primer nodo de la ruta cuya fracción de la clase mayoritaria, con pesos balanceados, sea ≥ p; p ∈ {0.55, 0.60, …, 0.95, 1.00}. Es la regla literal de pre-poda por pureza (scikit-learn eliminó `min_impurity_split`).
- **DT-ccp:** post-poda por costo-complejidad, `ccp_alpha` ∈ {0, 1e-4, 3e-4, 1e-3, 2e-3, 5e-3, 1e-2, 2e-2}.
- **RF:** 500 árboles, `class_weight='balanced'`, `max_features` ∈ {sqrt, 0.5, 1.0}, `min_samples_leaf` ∈ {1, 5, 20}.
- **XGB:** `XGBClassifier(tree_method='hist', subsample=0.8, colsample_bytree=0.8)` con pesos de muestra balanceados, `max_depth` ∈ {2, 3, 4, 6}, `learning_rate` ∈ {0.03, 0.1}, `n_estimators` ∈ {100, 300}.
- **XGB-additive** (solo validación cruzada, para la explicación): la misma malla con `interaction_constraints` de una feature por grupo.

**Selección.**
- Validación cruzada anidada: externa con los 5 folds de M4; interna con `StratifiedGroupKFold(3, shuffle=True, random_state=42)` por paciente dentro del train externo. Se elige por el AUC interno medio, y los empates van a la opción más simple (orden de la malla).
- Para el test: la misma selección interna sobre todo el train, reajuste y una evaluación.

**Test.**
- AUC, más F1, *accuracy*, *precision* y *recall* con umbral 0.5.
- Bootstrap de 2,000 remuestreos por paciente, pareado y con semilla 42, con la misma función que el M7.
- Comparación secundaria: árbol contra el MLP del M7 en la misma condición, con `Data/processed/m7/predicciones.parquet`, análisis `main`.

**Explicación del «por qué».**
1. Curvas de AUC en entrenamiento y validación contra la profundidad, la pureza y `ccp_alpha`, sobre los folds externos.
2. XGB aditivo contra XGB completo, para separar los cortes no lineales de las interacciones.
3. Importancia por permutación (RF y XGB) en los folds externos.
4. Reglas del árbol de profundidad 3 sobre C1 (`export_text`).
5. Número de hojas y de probabilidades distintas de cada DT, porque el AUC se calcula con empates.

**Sensibilidad de folds.**
- El MLP base del M7 (D-036, semilla 42) con 3 folds `StratifiedGroupKFold` por paciente, semillas 68 (masas) y 119 (calcificaciones), elegidas con la regla de D-026. Solo validación cruzada.
- Verificación: la réplica con 5 folds reproduce el AUC de `7_cv_por_fold.csv` (análisis `main`).

**Salidas:** `Code/results/X10_*.csv`, `Docs/Figures/X10_*.png` y `Data/processed/x10/predicciones.parquet`.

## Balance de folds con 3 a 10 (solo etiquetas; regla de D-026; ya calculado)

La réplica con 5 folds reproduce exactamente los folds de M4 (semillas 125 y 168).

| k | Train por modelo | Desviación máx., mejor semilla (masas / calc.) | Mediana en 200 (masas / calc.) | Malignas en el fold más pobre (masas / calc.) | Paciente más grande / fold más chico (calc.) | Semillas (masas / calc.) |
|---|---|---|---|---|---|---|
| 3 | 0.667 | 0.003 / 0.003 | 0.033 / 0.037 | 200 / 167 | 0.050 | 68 / 119 |
| 4 | 0.750 | 0.006 / 0.009 | 0.055 / 0.051 | 150 / 131 | 0.063 | 199 / 7 |
| 5 | 0.800 | 0.011 / 0.019 | 0.060 / 0.065 | 122 / 96 | 0.089 | 125 / 168 |
| 6 | 0.833 | 0.020 / 0.030 | 0.071 / 0.080 | 96 / 79 | 0.103 | 7 / 106 |
| 8 | 0.875 | 0.035 / 0.038 | 0.094 / 0.098 | 65 / 60 | 0.152 | 183 / 194 |
| 10 | 0.900 | 0.044 / 0.045 | 0.109 / 0.121 | 57 / 49 | 0.171 | 81 / 9 |

El paciente más grande tiene 14 lesiones en masas y 24 en calcificaciones.

## Pasos

- [x] 1. Comprobación del balance de folds (tabla de arriba)
- [x] 2. Instalar `xgboost` con pip en `qml_cancer` (sin tocar numpy/scipy) y regenerar `Code/env/requirements-qml_cancer.txt`
- [x] 3. Abrir D-043 (provisional) en `Other/bitacora_decisiones.md` con este protocolo, más su fila en el índice
- [x] 4. Escribir `Code/experiments/X10_Tree_Classifiers.ipynb` (en inglés, con el estilo de M7 y X6, más una celda de verificaciones)
- [x] 5. Corrida reducida de prueba (malla mínima) para validar el código
- [x] 6. Corrida completa: `jupyter nbconvert --to notebook --execute --inplace` con el kernel de `qml_cancer`; log en `/tmp/x10_run.log`
- [x] 7. Revisar que pasen las verificaciones y anotar aquí las cifras principales
- [x] 8. Borrador de H-056 en la bitácora (marcado «pendiente de revisión del autor»); NO tocar capítulos
- [x] 9. `ESTADO: COMPLETO` y desactivar la automatización

## Notas de la corrida
- 2026-10-21 22:37: corrida reducida (`X10_QUICK=1`, salida en /tmp/x10_quick) completada en 2 min. Pasaron 25 de 26 verificaciones; la que falló fue el determinismo del RF (2e-16 por la predicción en paralelo). Se corrigió prediciendo con un solo hilo.
- 2026-10-21 22:37: lanzada la corrida completa con `jupyter nbconvert --execute --inplace` sobre `Code/experiments/X10_Tree_Classifiers.ipynb`; progreso en `/tmp/x10_run.log`. Si el proceso ya no existe (`pgrep -f X10_Tree`) y el log no termina en «Checks passed», hay que relanzarla.
- 22:59: primera corrida completa en 21 min, con 29 de 29 verificaciones. Bug encontrado: la celda del balance de folds sobrescribía la variable `sizes`, así que `X10_tamano_arboles.csv` salió mal (las pantallas del notebook eran correctas). Corregido, con una verificación nueva y las reglas del árbol con pesos.
- 2026-10-21 23:00: lanzada la segunda corrida completa. Si el proceso no existe y `/tmp/x10_run.log` no termina en «Checks passed», hay que relanzarla.
- 23:00: la segunda corrida se detuvo a propósito para subir la leyenda de `X10_auc.png`, que tapaba un intervalo. Tercera corrida lanzada a las 23:00.
- 2026-10-21 23:01: borrador de H-056 en `/tmp/x10_timing/h056.md`, con las cifras de la primera corrida (que es determinista). Al terminar la tercera: comprobar que `X10_test.csv` da las mismas cifras, insertar H-056 antes de `## Preguntas abiertas` en la bitácora y añadir su fila al índice de hallazgos.
- 23:24: la tercera corrida dio 30 de 30 verificaciones y cifras idénticas a la primera. H-056 quedó insertado en la bitácora como borrador, y D-043 apunta a `X10_balance_folds.csv`.
- 2026-10-21 23:25: cuarta corrida, solo para corregir dos figuras (el eje de `X10_additive.png` y las etiquetas de `X10_importance.png`). Las cifras deben salir idénticas.
- 2026-10-21 23:47: la cuarta corrida dio 30 de 30 verificaciones; `X10_test.csv` y `X10_cv_por_fold.csv` son idénticos byte a byte a los de la tercera. Figuras revisadas. Tarea completa y automatización desactivada.
- **Pendiente para el autor:** revisar y validar D-043 y H-056; redactar la celda «7° Consequence» del notebook; los párrafos de §5.6/§5.9 (por qué 5 folds), §5.11, §6.3 y §8 (MLP profundo).
