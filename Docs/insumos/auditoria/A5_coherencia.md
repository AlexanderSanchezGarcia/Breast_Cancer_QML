# A5 · Coherencia lógica del argumento

Lee primero `Docs/insumos/auditoria/reglas.md`. Lee el reporte completo en orden (los `\input` de `Docs/Technical_Report.tex`).

Comprueba la cadena **pregunta → objetivos → metodología → resultados → conclusiones**:
1. La pregunta de investigación de §1 (y las subpreguntas que se formulen en §1 o §5, si las hay; el reporte no usa etiquetas PI-n): ¿§7 la responde exactamente, con la misma formulación? ¿Hay alguna que se responda sin evidencia en §6 o alguna evidencia de §6 que §7 ignore?
2. Cada objetivo específico (OE-1…OE-6) de §1: ¿qué módulo de §5 lo implementa, qué resultado de §6 lo evalúa y dónde dice §7 si se cumplió? Construye la tabla OE · §5 · §6 · §7 · estado. Señala objetivos sin cierre o cierres sin objetivo.
3. Alcance y limitaciones (§1.5, §7.6): ¿coinciden? ¿Se promete en §1 algo que no se hizo (hardware real, CNN, Estrategia B, otro dataset)?
4. Antecedentes (§2) → justificación: ¿la brecha que §2 identifica es la que el trabajo aborda? ¿§2 atribuye a una fuente algo que luego §7 contradice sin comentarlo?
5. Metodología (§5) frente a resultados (§6): ¿todo método descrito tiene resultado, y todo resultado tiene método? (incluye X1–X9 de §5.11).
6. **Calibración**: frases de §6, §7 o el resumen que digan más de lo que la evidencia sostiene, o que contradigan la regla 1 de `CLAUDE.md` (viabilidad, no benchmark). También lo contrario: afirmaciones demasiado tímidas donde hay una prueba significativa.
7. Contradicciones internas entre dos lugares del reporte (aunque cada uno por separado parezca bien).
8. El título: el del protocolo registrado es «Modelo de transformación cuántica variacional de características de cáncer de mama para un sistema híbrido de prediagnóstico». Busca cualquier otra variante del título en el reporte.

Este análisis es de prosa y razonamiento: cada hallazgo debe apoyarse en citas literales de las dos (o más) ubicaciones que entran en conflicto. Nada de impresiones generales sin ubicación.

Entrega: `informe_A5.md` con la tabla de objetivos y los hallazgos.
