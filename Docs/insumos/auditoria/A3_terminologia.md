# A3 · Terminología, notación y estilo

Lee primero `Docs/insumos/auditoria/reglas.md`.

Alcance: todos los `.tex` incluidos por `Docs/Technical_Report.tex` (lista los `\input` en orden).

Revisa, con `grep` y lectura:
1. **Nombres de módulos y condiciones**: M1–M8 con el significado de D-030 (M6 = separabilidad, M7 = clasificación, M8 = comparación); cualquier «M6 · Clasificación» o «M7 · Evaluación» es un resto del esquema antiguo. C1–C5 con su significado (C5 = `pauli_feature_map` con `['Y','ZZ']`). OE-1…OE-6 usados igual que en §1.
2. **Nombres de API**: `zz_feature_map` y `pauli_feature_map` (funciones de Qiskit 2.x); `ZZFeatureMap`/`PauliFeatureMap` solo si el texto habla explícitamente de la clase deprecada. `TorchConnector` y `EstimatorQNN` solo como opciones descartadas.
3. **Notación matemática**: el mismo símbolo para lo mismo en todos los capítulos ($k$ número de features/qubits, $N$ o $n$ número de muestras, $\theta$, $\gamma$, $\lambda$, $c$ ancho de banda, $K_Q$, $K_C$, $g$, $\langle Z_i\rangle$). Lista cada conflicto con sus ubicaciones.
4. **Identificadores internos visibles**: D-xxx, H-xxx, Q-xxx, X1–X9 o B1–B3 en el texto visible (fuera de comentarios `%`). Los nombres de notebooks en `\texttt{}` sí se permiten en Metodología y Anexos; decide caso por caso y explica.
5. **Comillas y rayas**: el texto visible usa ``…'' (no «», ni comillas rectas "…"). No hay incisos con `---` ni `--` (se usan comas o paréntesis); los rangos numéricos sí pueden usar `--`.
6. **Lenguaje sobredimensionado**: «demuestra», «confirma», «prueba», «ventaja cuántica» (como algo observado), «sin excepción», «estrictamente», «de manera contundente», «revolucionario». Indica si la evidencia lo sostiene.
7. **Restos de TT1 o del diseño anterior**: tiempo verbal futuro para trabajo ya hecho («se implementará», «se evaluará»), «en la siguiente etapa», referencias a TT2 como futuro, «Breast Cancer Wisconsin», 224×224, CLAHE en la ruta radiómica, `binWidth`.
8. **Ortografía y concordancia** en español: lista solo errores reales (tildes, concordancia, palabras repetidas), no preferencias.
9. Términos en inglés: en `\textit{}` la primera vez; consistencia (no alternar «kernel»/«núcleo», «feature»/«característica» sin criterio).

Entrega: `informe_A3.md`. Agrupa por categoría; los de estilo puro (punto 8) pueden ir en una tabla compacta.
