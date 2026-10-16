ESTADO: TERMINADO

# Orquestación nocturna · 2026-10-14

Archivo de estado para retomar el trabajo si se corta la sesión coordinadora. **Quien retome: lee este archivo completo antes de hacer nada.** La última línea de «Bitácora» es el punto exacto donde quedó.

## Qué se acordó con el autor (sesión del 2026-10-14, 00:00–01:00)

1. **El EDA pasa antes de la Metodología.** Orden: 1 Panorama, 2 Antecedentes, 3 Marco teórico, **4 EDA**, **5 Metodología**, 6 Resultados, 7 Conclusiones. Carpetas `Docs/capitulos/4_EDA` y `Docs/capitulos/5_Metodologia`.
2. **No hay hipótesis.** Se conserva la pregunta de investigación (sugerencia de los directores). Se propondrá descomponerla en PI-1 (separabilidad), PI-2 (traslado a la clasificación) y PI-3 (viabilidad); los criterios operativos van en la Metodología, no en §1. La redacción de §1 la hace el coordinador con el autor en sesión, **no Gemini**.
3. **Anexos con `listings`**, con el código extraído literalmente de los notebooks a `Docs/codigo/*.py` y verificado por script.
4. **PDF:** 7 en `Docs/fuentes/` (ignorado en git). Rifat 2024 (BreastMNIST) no se consiguió: queda fuera de §2 salvo decisión del autor.
5. **Nadie edita `Docs/Technical_Report.tex`.** Ningún commit lleva atribución a IA (sin Co-Authored-By). Gemini no hace commits.

## Tareas

| Id | Tarea | Trabajador | Estado | Aceptación |
|---|---|---|---|---|
| F0 | Preparación: carpetas, `.gitignore`, PDF, texto por página, scripts, especificaciones | coordinador | **hecha** | — |
| T1 | Fichas de lectura (grupo A) | gemini | pendiente | `verificar_citas_fichas.py` |
| T2 | Fichas de lectura (grupo B) | gemini | pendiente | `verificar_citas_fichas.py` |
| T3 | Auditoría de §1–§2 | gemini | pendiente | revisión por muestreo |
| T4 | Anexos A–D | gemini | pendiente | `verificar_listados.py` + `compilar_prueba.sh` |
| T5 | §4 EDA como puente | gemini | pendiente | `compilar_prueba.sh` |
| T6 | §5.11 X1–X8 y añadidos de §6 | gemini | pendiente | `verificar_cifras_capitulos.py` + `compilar_prueba.sh` |
| T7 | §2 nuevas subsecciones y tabla (depende de T1, T2) | gemini | pendiente | citas respaldadas por fichas verificadas |
| F3 | Verificación de la mañana e informe al autor | coordinador | pendiente | — |

## Identificadores de Orca

- Run: `run_d9ce22a9f63c` (vincularse con `orca orchestration run-use --run run_d9ce22a9f63c`).
- Agente: `antigravity`, modelo `gemini-3.8-flash-high`, `--worktree current` (carpeta /Users/alexander_san/TT).
- Especificaciones: `Docs/insumos/noche/` (reglas.md + T1_fichas.md, T3…, T4…, T5…, T6…, T7…). Informes de los trabajadores: `Docs/insumos/noche/informe_T*.md`.

| Tarea | task id | dispatch | ola |
|---|---|---|---|
| T1A fichas A | task_f4eac562df5e | ctx_ca548ef73d64 | 1 |
| T1B fichas B | task_1b4c32a1f202 | ctx_2852ed7e61a7 | 1 |
| T1C fichas C | task_5fa40680a242 | ctx_d8b6673870a1 | 1 |
| T1D fichas D | task_f06837108dfe | ctx_1411714dcf61 | 1 |
| T6 metodología y resultados | task_d94f0784a67a | ctx_f52167f2ce68 | 1 |
| T3 auditoría §1–§2 | task_0324284695a9 | ctx_27222ac83f9a | 2 |
| T4 anexos | task_ed012c867857 | ctx_3992949ef96f | 2 |
| T5 EDA puente | task_ce04b6313725 | ctx_a190f90b0e2a | 2 |
| T7 antecedentes (deps: T1A–T1D) | task_3b69ce4e25d0 | ctx_410a4fbd1933 | 3 |
| (descartada, spec de prueba) | task_df5c329cb94b | — | — |

Lanzar un trabajador: `orca orchestration worker-start --run run_d9ce22a9f63c --task <task id> --worktree current --agent antigravity --model gemini-3.8-flash-high --json`.

## Aceptación (cómo verificar cada entrega)

- Fichas: `python3 Code/tools/verificar_citas_fichas.py` (todas) · auditoría: `python3 Code/tools/verificar_citas_fichas.py Docs/insumos/auditoria_s1_s2.md`.
- Anexos: `python3 Code/tools/verificar_listados.py Docs/capitulos/A_Anexos` y `bash Docs/capitulos/compilar_prueba.sh A_Anexos`.
- Capítulos: `/opt/anaconda3/envs/qml_cancer/bin/python Code/tools/verificar_cifras_capitulos.py Docs/capitulos/<carpeta>` y `bash Docs/capitulos/compilar_prueba.sh <carpetas>`.
- §2 nuevo: `python3 Code/tools/verificar_citas_fichas.py Docs/capitulos/2_Antecedentes` y `bash Docs/capitulos/compilar_prueba.sh 2_Antecedentes`.
- Después de las pruebas automáticas, revisión a mano por muestreo (Gemini ya inventó evidencia antes).

## Reanudación

- Recordatorios internos de la sesión: 05:07 y 06:13.
- Automatización de Orca de respaldo: 06:40, solo si este archivo dice `EN_CURSO` y lleva más de 60 min sin cambios.
- Al terminar todo: cambiar la primera línea a `ESTADO: TERMINADO`, borrar la automatización (`orca automations remove`) y los recordatorios.

## Bitácora

- 00:55 · Creado el archivo de estado. caffeinate activo (10 h).
- 01:04 · F0 hecha: carpetas 4_EDA/5_Metodologia renombradas (git mv, sin commit), etiquetas sec:metodologia y sec:moduloN añadidas, `Docs/fuentes/` ignorada con 24 PDF y su texto por página, `bibitems_noche.tex` (14 entradas desde Crossref/DataCite/arXiv), `preambulo_extra.tex` (listings), `compilar_prueba.sh` con PATH de TeX, preámbulo extra y bibitems_noche; scripts `verificar_citas_fichas.py`, `extraer_codigo.py`, `verificar_listados.py` probados.
- 01:06 · Ola 1 lanzada: T1A, T1B, T1C, T1D, T6. Siguiente: al terminar trabajadores de la ola 1, verificar y lanzar T3, T4, T5; cuando T1A–T1D estén aceptadas, lanzar T7.
- 01:16 · Ola 1 trabajando bien (Lee2017 y Mari2020 pasan el verificador, 32/32 citas). Ola 2 lanzada: T3, T4, T5. Nota para el informe: Lee2017 (p. 5) sí dice que la partición train/test se hizo por categoría BI-RADS → RNF-03 y §1.3 pueden recuperarlo con cita.
- 01:21 · T1A aceptada: 4 fichas, 134/134 citas verificadas; trabajador liberado.
- 01:21 · T1A aceptada: 4 fichas, 134/134 citas verificadas; trabajador liberado.
- 01:22 · T1B aceptada: 6 fichas, 118/118 citas; revisada a mano la de Bowles (fiel). Liberado.
- 01:23 · T1C aceptada: 6 fichas, 86/86 citas. Azevedo p. 12 confirma literalmente las dos líneas de trabajo futuro (masas/calcificaciones y distribución en el espacio de Hilbert). Comprobado: el artículo usa «Breast Cancer Data Repository» (p. 4) y «Breast cancer digital repository» (bibliografía); la ficha queda con ambas formas. Liberado.
- 01:24 · T1D aceptada: 8 fichas, 108/108 citas. Confirmado: §1.1.3 (línea 561) parafrasea a Mari et al. p. 3 sin cita. Ficha IBSI suavizada por el coordinador («exige» → recomienda; el manual no menciona mamografía ni fija 32). Liberado. Fichas T1A–T1D completas → se lanza T7.
- 01:25 · T7 lanzada (ctx_410a4fbd1933). Activos: T3, T4, T5, T6, T7.
- 01:27 · T6 aceptada tras correcciones del coordinador: quitados los D-xxx/H-xxx visibles en 6.7, 6.2 y 5.11; reescrito el párrafo de deprecación de PauliFeatureMap (decía «módulo de algoritmos antiguos»); en 6.8 «millones de mediciones por par» solo vale para C5 (C4: decenas de miles, bitácora l. 2171). Verificados: enteros de B1 contra CSV, IC de 7_test_diferencias (los 4 excluyen 0). Pruebas: compila sin refs sin resolver; cifras: 1 NO_ENCONTRADO aceptable («Qiskit 2.1», de CLAUDE.md). Liberado.
- 01:29 · T3 aceptada (17/17 citas; muestreo de líneas 443, 527, 557, 591, 783 correcto). Corregida por el coordinador: la paráfrasis de l. 591 es de Álvarez-Estévez 2024 (no Shaydulin), y hay otra de la misma fuente en l. 587; añadido al final de auditoria_s1_s2.md.
- 01:30 · T5 aceptada: EDA como cap. 4, tabla de 8 implicaciones, 8 figuras a A.3.2; cifras del cuerpo sin cambios (comprobado con diff); compilación 3–6 + A_Anexos. Pendiente para la mañana: Docs/insumos/referencias_cruzadas.md. Liberado.
- 01:32 · T4 aceptada: 15/15 listados idénticos a sus celdas; 11 tablas reproducibles con tablas_anexos.py (regeneradas byte a byte); versiones del anexo D = conda list crudo; M8 describe bien el muestreo multinomial (no SamplerV2). Corregido: «sin binarios en conda-forge para la arquitectura de prueba» → no existe paquete en conda-forge (H-006). Nota: en radiomics la versión de pyradiomics figura como 0.1.dev1 (mismo commit; etiqueta de setuptools_scm, H-029). Liberado.
- 01:39 · T7 aceptada tras correcciones del coordinador: 2.1.7 calibrado (Huang 2021 «observaron… siempre», quitado «destruye la coherencia», cierre sin «la teoría establece que solo»); 2.1.9 sin H-046 visible, Xiang P3 reformulada con su cita (máximo sobre validación), El Hafidi: eliminadas las «16 instancias» (inventadas: el artículo no describe partición de prueba); 2.1.8: tamaño real de las mamografías (5,037×2,960 → n=13, 42 qubits, ~1.4e10 operaciones; Gemini usó 2,048×2,048). 79/79 citas; compila. Liberado. TODAS LAS TAREAS TERMINADAS.
- 01:40 · Informe final en Docs/insumos/informe_noche_2026-10-14.md; borrador completo en Docs/insumos/noche/borrador_completo_2026-10-14.pdf. Automatización y recordatorios cancelados; caffeinate detenido.
