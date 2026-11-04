# Estado · ronda 4 de la presentación (Manim + recorte de texto + respaldos)

Archivo de coordinación. Lo actualiza el coordinador (Claude) después de cada paso. Si una sesión nueva retoma el trabajo, empieza aquí.

ESTADO: COMPLETO

## Contexto
- Petición del autor (2026-11-03):
  - presentación más dinámica y con menos texto;
  - el proceso general del trabajo;
  - clips de Manim hechos por Gemini mediante orquestación;
  - unos 30 respaldos, con fórmulas del marco teórico, para preguntas básicas y pesadas;
  - la diapositiva 13 tiene demasiado texto.
- Claude Design acepta MP4 (H.264) o WebM de hasta 20 MB. El video arranca con un clic **sobre el video**, no con la flecha; como imagen fija usa un fotograma (pedir el último). En el PDF solo se ve esa imagen.
- Pregunta de un sinodal que debe tener respaldo: «¿qué habría pasado si θ se entrenaba?». Respuesta del autor, coherente con X8 (H-054) y con la desigualdad de procesamiento de datos (D-043): en el mejor caso empataría con el mejor clásico, sin superarlo; en X8 ganó a lo sumo 0.05 y no alcanzó a C1.

## Piezas
- Datos reales: `preparar_datos.py` (entorno qml_cancer) → `datos/`. API en `datos.py`. Paleta y fuentes en `estilo.py`.
- Especificación de los clips: `ESPEC.md`.
- Entorno de render: conda `manim` (conda-forge, Manim CE).
- Orca Run: `run_9f9d3a6f4caf`. Automatización de respaldo: `871590d7-6912-49bd-a6f8-67b61648f6b3` (cada hora; precheck.sh: solo corre si ESTADO.md lleva más de 75 min sin cambios y sigue EN CURSO). Al terminar todo, desactívala con `orca automations edit --id 871590d7-6912-49bd-a6f8-67b61648f6b3 --disabled`. Workers Antigravity con gemini-4-argon-high:
  - W1 `ctx_83990b64985f`: mapa_trabajo y dos_lecturas.
  - W2 `ctx_4eb95c54a36b`: qubit_bloch y disparos.
  - W3 `ctx_6e865c6dfb4d`: concentracion y x11_curva.

## Pasos
- [x] 1. Entorno manim, datos reales y verificación (fidelidad del estado = kernel del M5, < 1e-9).
- [x] 2. ESPEC.md y lanzamiento de los 3 workers.
- [x] 3. Brief de la ronda 4 para Claude Design (`../brief_ronda4.md`): recorte de texto, diapositiva del proceso general, ubicación de los clips y respaldos con fórmulas. Cada cifra y fórmula se verifica contra la bitácora y §3 del reporte.
- [x] 4. Revisión de cada clip: código (ninguna cifra a mano, todas de datos.py), fotogramas en `revision/` y MP4 (H.264, < 20 MB). Correcciones a los workers con `orca orchestration send`.
- [x] 5. Entregar al autor: los clips aprobados en `clips/`, el brief y qué adjuntar en Claude Design.
- [x] 6. Commit (sin coautoría; `media/` va en .gitignore).

## Cómo retomar (para una sesión nueva)
1. Lee este archivo y `ESPEC.md`.
2. Mensajes de los workers: `orca orchestration run-use --id run_9f9d3a6f4caf`, luego `orca orchestration inbox --terminal run:run_9f9d3a6f4caf --limit 50` y `orca orchestration worker-list --json`, filtrando los tres dispatchId de arriba.
3. Sigue con el primer paso sin marcar. Al terminar cada paso, márcalo aquí y añade una línea en «Bitácora».
4. No hagas push. No toques `Technical_Report.tex`. Commits sin línea de coautoría.

## Bitácora
- 2026-11-03 ~21:55 · Pasos 1 y 2 hechos. Los workers trabajan; Claude empieza el brief de la ronda 4.
- 2026-11-03 ~22:05 · Paso 3 hecho: `../brief_ronda4.md` (recorte de texto, diapositiva 4 nueva con el mapa, seis clips, R0 + respaldos A1–E6 con fórmulas de §3). Cifras verificadas contra 8_tabla_clasificacion.csv, H-011, H-044, H-053, H-054, H-035 y CLAUDE.md. Falta revisar los clips (paso 4).
- 2026-11-03 ~22:15 · Primera pasada de los 6 clips revisada: código sin cifras a mano; H.264, 1080p, < 2 MB.
  - Hallazgo: las probabilidades del estado del mapa ZZ son todas 1/4096, así que la información está en las fases. `preparar_datos.py` y `datos.py` exponen ahora `fase_a` y `fase_b`, con aserciones, y el clip 2 de ESPEC.md se rehízo con la caminata de fasores.
  - Correcciones enviadas: W1 `msg_96ca043f2189` (mapa encimado, miniaturas de 1600×220, dos_lecturas con fases), W2 `msg_a4bed807342a` (títulos, recuadro de C4, menos texto, esfera más grande) y W3 `msg_69bc6755ce3a` (rótulo de X11).
  - Pendiente: revisar la segunda versión.
- 2026-11-03 22:24 · W2 reportó worker_done con la versión ANTERIOR a las correcciones (archivos de las 22:22). Reenviadas como seguimiento: `msg_37a4b7ff092b`. Si W2 no se reabre, lanzar un worker nuevo para qubit_bloch y disparos con ese mismo texto.
- 2026-11-03 22:26 · W3 reportó también la versión anterior a las correcciones; el rótulo de X11 sigue cruzado. Reenviado como seguimiento. concentracion: los rótulos se deforman al cambiar c (glifos rotos); corrección enviada en un segundo mensaje.
- 2026-11-03 22:30 · disparos verificado: los conteos [3,1,3,3,1,6,3,0,1,1] coinciden con una simulación independiente (rng.random(1024) < p, semillas 0–9). Solo falta quitarle el título (seguimiento de W2).
- 2026-11-03 22:40 · x11_curva APROBADO (el rótulo en dos renglones ya no toca las curvas). Seguimientos en marcha: `ctx_23f366f6e6ce` (task_e52c8b0f7d45) y `ctx_661ae56ce8b6` (task_63b1dc1a098f): correcciones de W2 (qubit_bloch y disparos) y rótulos de concentracion (W3). W1 `ctx_83990b64985f` sigue con mapa_trabajo y dos_lecturas.
- 2026-11-03 22:45 · W1 reportó: miniaturas APROBADAS (1600×220, sin encimados). mapa_trabajo sigue con título, cajas desbordadas y la bifurcación cruzando su rótulo; dos_lecturas hecho con la especificación vieja (probabilidades). Seguimiento enviado.
- 2026-11-03 22:55 · qubit_bloch y disparos APROBADOS (sin títulos, recuadros correctos, física revisada: C4 gira alrededor de Z en el ecuador; C5 con RY desde |+⟩ pasa por |1⟩ y termina cerca de |0⟩). Faltan concentracion (rótulos, W3) y mapa_trabajo y dos_lecturas (W1).
- 2026-11-03 23:00 · concentracion APROBADO: fundido limpio verificado con fotogramas cada 0.4 s; las medianas mostradas (0.55, 0.20, 0.069, 0.032, 0.0060, 0.0022) coinciden con datos. Solo falta W1 (mapa_trabajo y dos_lecturas).
- 2026-11-04 01:45 · La automatización corrió 2 veces (00:00 y 01:00) sin modificar archivos. W1 entregó mapa_trabajo y dos_lecturas: dos_lecturas APROBADO (fases reales, caminata, kernel 0.0035, escala ±0.25). Claude corrige él mismo la geometría de mapa_trabajo (la bifurcación cruza los rótulos de la estación 5 y de Comparación).
- 2026-11-04 01:55 · mapa_trabajo APROBADO tras revisar el MP4 real (el compuesto anterior usaba PNG viejos): tramo recto antes de bifurcar, «Comparación» a la derecha y sin choques, también en los fotogramas intermedios. **Los 6 clips y las 7 miniaturas están aprobados.** Las miniaturas se copiaron a `clips/`. `media/` y `revision/` van en .gitignore. Commit hecho y automatización desactivada.

## Resumen para el autor
- Entregables en `Other/defensa/manim/clips/`: mapa_trabajo, qubit_bloch, dos_lecturas, concentracion, x11_curva y disparos (MP4 H.264 1080p, < 2 MB cada uno) y mapa_mini_1…7.png (1600×220, transparentes).
- Qué adjuntar en Claude Design: `Other/defensa/brief_ronda4.md`, los 6 MP4 y mapa_mini_5, 6 y 7.
