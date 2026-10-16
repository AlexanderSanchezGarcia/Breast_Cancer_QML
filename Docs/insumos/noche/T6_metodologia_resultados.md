# T6 · Experimentos complementarios en la Metodología y hallazgos que faltan en Resultados

Lee primero `Docs/insumos/noche/reglas.md`. Lee `CLAUDE.md` completo y, de `Other/bitacora_decisiones.md`, cada entrada que cites (búscala con `grep -n '### H-0xx'`).

## Contexto

Los capítulos 5 (Metodología, `Docs/capitulos/5_Metodologia/`) y 6 (Resultados, `Docs/capitulos/6_Resultados/`) ya existen. El autor pidió que Resultados sea **más específico en sus hallazgos**. Tres carencias concretas:
1. La Metodología no describe los experimentos complementarios X1–X8, aunque Resultados los reporta.
2. Faltan hallazgos de la bitácora: H-005, H-018, H-030 y los de implementación (H-012, H-013, H-014, H-019, H-032, H-034).
3. No hay una síntesis que diga, objetivo por objetivo, qué evidencia hay y qué respuesta da.

## Tú escribes solo en

- `Docs/capitulos/5_Metodologia/5.11_experimentos_complementarios.tex` (nuevo).
- `Docs/capitulos/6_Resultados/*.tex` (existentes y nuevos con prefijo `6.`).
- `Docs/insumos/lenguaje_s6.md` (nuevo).

## Cambios

### 1. `5.11_experimentos_complementarios.tex`
`\subsection{Experimentos complementarios}` con `\label{sec:experimentos_complementarios}`. Un párrafo introductorio: los experimentos X1–X8 no cambian el diseño; ponen a prueba la robustez de la conclusión ante alternativas que un lector razonable plantearía. Después, una tabla (`booktabs`, columnas con `p{}`) y un párrafo corto por experimento, cada uno con: **pregunta** que responde, **diseño** (qué se varía y qué se mantiene fijo), **control** (contra qué se compara), **uso del test** (si lo toca o no), y la entrada de la bitácora en `% fuente:`. Experimentos y entradas:
- X1 `Code/experiments/X1_Selection_Information_Loss.ipynb` · H-035
- X2 `X2_Kernel_Class_Structure` · H-036
- X3 `X3_Fewer_Qubits_k8` · H-041, D-035
- X4 `X4_QSVM_and_67_Features` · H-044, H-045, D-038
- X5 `X5_Pipeline_Audit` · H-046
- X6 `X6_Searching_for_Advantage` · H-047, H-048
- X7 `X7_Theta_Draws` · H-053
- X8 `X8_Trained_Theta` · H-054
Incluye también los estudios del simulador B1–B3 (`Code/benchmark/`), en un párrafo: qué midieron y que la sección de *shots* de B1 quedó invalidada por H-019 y la sustituye B3.
**Sin resultados numéricos en esta sección**: es método. Los resultados están en el capítulo 6; remite con `\ref`.

### 2. Hallazgos que faltan en el capítulo 6
Intégralos en el archivo que corresponda, cada uno como uno o dos párrafos con `% fuente:` y cifras de la bitácora o los CSV:
- **H-005** (sin fuga de pacientes dentro de cada subproblema) → `6.1_datos_caracteristicas.tex`.
- **H-030** (la selección univariante no ve interacciones, justo lo que codifica el bloque ZZ) → `6.1`, como limitación del diseño que matiza la comparación. Relaciónalo con X1 (H-035) si la bitácora lo hace.
- **H-018** (el *embedding* se concentra con el número de qubits, no con la profundidad; cifras exactas tras H-019) → `6.2_separabilidad.tex` o `6.6_restricciones_simulador.tex`, donde encaje.
- **Nueva subsección `6.7_lecciones_implementacion.tex`** («Hallazgos de implementación», `\label{sec:lecciones_implementacion}`), parte de la respuesta al OE-6: cada lección en un párrafo con la forma *qué se observó → por qué ocurre (propiedad del formalismo cuántico o detalle de Qiskit; distínguelo explícitamente) → qué se hizo*. Lecciones: H-012 (`['Z','ZZ']` es el mismo circuito que ZZ), H-034 (con reps=1 el término X actúa sobre |+⟩ y no codifica nada), H-013 (sin *ansatz*, ⟨Zᵢ⟩ es idénticamente cero), H-019 y H-014 (`EstimatorQNN` trae precisión 0.015625 y suma ruido gaussiano; el `EstimatorV2` de Aer no muestrea), H-032 (`FidelityStatevectorKernel` da el mismo kernel ~1000× más rápido), y la deprecación de `PauliFeatureMap` en Qiskit 2.1+ (`CLAUDE.md`). Verifica cada afirmación en la entrada de la bitácora; no añadas explicaciones físicas que la entrada no dé.

### 3. Síntesis por objetivo: `6.8_sintesis.tex`
`\subsection{Síntesis por objetivo específico}` con `\label{sec:sintesis_objetivos}`. Una tabla (`booktabs`, `p{}`) con filas OE-1 a OE-6 (el texto de los objetivos está en `Docs/Technical_Report.tex`, líneas 647–657) y columnas: *Objetivo (resumido)* | *Evidencia principal* (cifras clave, con su `% fuente:` encima de la tabla) | *Sección* (`\ref`) | *Resultado*. Luego un párrafo por cada una de las tres dimensiones que el planteamiento enuncia (representación ↔ OE-3; clasificación ↔ OE-5; viabilidad ↔ OE-6) diciendo qué responde la evidencia, en lenguaje calibrado: no hubo mayor separabilidad cuántica en ninguna familia de métricas a c = 1; el mismo MLP clasifica peor sobre C4/C5; la concentración del kernel lo hace inmedible con *shots* razonables. **No escribas conclusiones generales ni trabajo futuro**: eso es el capítulo 7, que redactará el autor.

### 4. Lenguaje: `Docs/insumos/lenguaje_s6.md`
Revisa **todos** los archivos de `6_Resultados/` (incluidos los que no tocaste) y lista cada frase que afirma más de lo que su evidencia permite: verbos como «demuestra», «confirma», «evidencia», «sin excepción», «estrictamente», «de manera coherente», y conclusiones causales sin prueba. Formato: archivo, línea, frase literal, por qué sobreafirma (qué dice realmente el dato: p. ej. «ρ_s = 0.718 con p = 0.167 no es significativo»), propuesta de redacción. **No reescribas esas frases en los .tex** salvo en los párrafos nuevos que tú escribes.

## Aceptación

- `/opt/anaconda3/envs/qml_cancer/bin/python Code/tools/verificar_cifras_capitulos.py Docs/capitulos/6_Resultados Docs/capitulos/5_Metodologia` — córrelo **antes** de empezar (línea base, guárdala en tu informe) y al final: ningún `SIN_FUENTE` ni `NO_ENCONTRADO` nuevo en lo que escribiste.
- `bash Docs/capitulos/compilar_prueba.sh 3_Marco_Teorico 4_EDA 5_Metodologia 6_Resultados` compila sin errores ni referencias sin resolver.
- Informe en `Docs/insumos/noche/informe_T6.md`.
