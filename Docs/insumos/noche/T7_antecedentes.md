# T7 · Subsecciones nuevas del Estado del arte (§2)

Lee primero `Docs/insumos/noche/reglas.md`. **Esta tarea depende de las fichas** de `Docs/insumos/fichas/`: úsalas como fuente principal y vuelve al texto de los PDF (`Docs/fuentes/txt/`) cuando necesites más detalle. Lee también `Docs/insumos/auditoria_s1_s2.md` si ya existe.

## Contexto

El §2 actual está en `Docs/Technical_Report.tex`, líneas 692–978 (subsecciones 2.1.1 a 2.1.6 y la tabla `tab:estado_arte`). No lo edites. Escribes **subsecciones nuevas** que el autor insertará, en `Docs/capitulos/2_Antecedentes/`, y una versión ampliada de la tabla.

## Tú escribes solo en

`Docs/capitulos/2_Antecedentes/` (carpeta nueva) e `Docs/insumos/noche/informe_T7.md`.

## Archivos

1. **`2.1.7_limites_ventaja.tex`** · `\subsubsection{Límites de la ventaja cuántica con datos clásicos}` (`\label{sec:limites_ventaja}`). Hilo argumental: dónde se ha demostrado una ventaja (estructura algebraica en la **etiqueta**: Liu2021Speedup, Glick2024Covariant; datos que **ya son** estados cuánticos: Huang2022Experiments) frente a qué ocurre con datos clásicos genéricos codificados por ángulo (huang2021power: *geometric difference*; Thanasilp2024: concentración exponencial; Kubler2021Inductive: sesgo inductivo; Shaydulin2022Bandwidth y Canatar2023Bandwidth: el ancho de banda; Bowles2024Benchmarking: los modelos clásicos suelen ganar en *benchmarks* cuidadosos; SchuldKilloran2022Advantage: la ventaja no tiene por qué ser el objetivo). Cierra conectando con el presente trabajo **sin adelantar resultados numéricos**: estas obras describen las condiciones bajo las cuales se espera o no se espera ventaja, y por eso el trabajo mide separabilidad con la *geometric difference* y controla el ancho de banda.
2. **`2.1.8_imagenes_cuanticas.tex`** · `\subsubsection{Representaciones cuánticas de imágenes}` (`\label{sec:imagenes_cuanticas}`). FRQI (Le2011FRQI), NEQR (Zhang2013NEQR), el análisis comparativo de Parigi2026QImR; por qué el trabajo codifica features radiómicas y no la imagen. Usa **solo** lo que digan las fichas sobre complejidad de preparación; si la ficha dice que la obra no lo trata, no lo afirmes.
3. **`2.1.9_revision_critica.tex`** · `\subsubsection{Revisión crítica de los trabajos que reportan ventaja}` (`\label{sec:revision_critica}`). Las cuatro preguntas de H-046 (enúncialas) aplicadas a Xiang2024QuantumCNN, ElHafidi2025 y Azevedo2022QuantumTransfer, a partir de las fichas. Para Radhi2025QuantumDeepLearning (no hay PDF) y para el trabajo de BreastMNIST (Rifat 2024, sin PDF ni `\bibitem`): **no los evalúes**; añade un comentario `% PENDIENTE: sin PDF` y nada en el texto visible.
4. **`2.1.6_tabla_ampliada.tex`** · copia la tabla `tab:estado_arte` de `Technical_Report.tex` (líneas 839–974, desde `\begin{landscape}` hasta `\end{landscape}`), cambia la etiqueta a `tab:estado_arte_v2`, y: añade la columna **«Comparación justa»** (resumen de las cuatro preguntas: Sí / Parcial / No / ND) para las filas con QML; añade filas para ElHafidi2025 (QSVM, cáncer de pulmón) y Parigi2026QImR (representaciones de imagen), con datos tomados de las fichas; corrige la fila del presente trabajo según `CLAUDE.md` (*feature maps* C4 `zz_feature_map` y C5 `pauli_feature_map(['Y','ZZ'])`, sin AUC «Por det.»: pon las AUC del test de `Code/results/7_test.csv` para C4 y C5 por subconjunto, con `% fuente: H-042; 7_test.csv`). Si la tabla no cabe, reduce `\small` a `\footnotesize` o abrevia, no elimines columnas.

## Reglas de citación (estrictas)

- Cada oración que atribuya algo a una obra lleva `\cite{Clave}` **y**, en la línea anterior, un comentario `% respaldo: «cita literal» (Clave, p. N)` copiado de la ficha (o del `.txt`). Una oración sin respaldo verificable no se escribe.
- Distingue lo que la obra **concluye** de lo que **propone como trabajo futuro** o **supone** (p. ej., Liu et al. suponen un computador tolerante a fallos).
- Solo claves existentes (ver reglas). Las de las obras nuevas están en `Docs/insumos/bibitems_noche.tex`.

## Aceptación

- `python3 Code/tools/verificar_citas_fichas.py Docs/capitulos/2_Antecedentes` sin fallos.
- `bash Docs/capitulos/compilar_prueba.sh 2_Antecedentes` compila sin errores ni citas sin resolver.
- Informe en `Docs/insumos/noche/informe_T7.md` con la salida de ambas pruebas, y una lista de lo que quisiste afirmar y no pudiste respaldar.
