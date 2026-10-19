# A4 · Fidelidad de las citas y formato de la bibliografía

Lee primero `Docs/insumos/auditoria/reglas.md`.

1. Corre `python3 Code/tools/verificar_citas_fichas.py Docs/capitulos` y `... Docs/insumos/fichas`; copia el resumen.
2. Para **cada** `\cite{}` de los capítulos 1, 2, 3, 6 y 7 (son los que atribuyen afirmaciones a terceros), comprueba que la afirmación del texto está respaldada por la fuente:
   - si la fuente está en `Docs/fuentes/txt/<Clave>/`, busca el pasaje y copia la cita literal con página;
   - si hay ficha en `Docs/insumos/fichas/<Clave>.md`, úsala;
   - si no hay ni texto ni ficha, marca `[NO VERIFICADO: sin fuente local]`, no supongas.
   Distingue lo que la fuente **concluye** de lo que deja como **trabajo futuro** o simplemente **menciona**. La regla 2 de `CLAUDE.md` es explícita: este trabajo se apoya en el trabajo futuro de Azevedo et al. (2022), no en Incudini et al.
   Atención especial a Huang et al. (2021): el reporte cita el material suplementario publicado (secciones 1–13, ecuaciones S1–S133), no los apéndices de arXiv; comprueba que la numeración visible es la publicada (`Docs/capitulos/README.md` tiene la tabla de equivalencias).
3. Bibliografía (`Docs/bibliografia.tex`):
   - **estilo**: el artículo técnico exige IEEE y el reporte debe ser uniforme. Indica qué estilo sigue cada entrada (APA, IEEE, mixto) y cuántas no siguen el mayoritario;
   - campos que faltan (año, volumen, páginas, DOI), DOI mal formados, URL rotas a simple vista, entradas «Retrieved from» sin fecha de consulta;
   - autores, años o títulos que no coinciden con la ficha o con la primera página del PDF en `Docs/fuentes/txt/<Clave>/p001.txt`.
   No consultes internet para «corregir» metadatos; solo compara con lo que hay en el repositorio y marca lo dudoso.

Entrega: `informe_A4.md` con una tabla por cita (clave · ubicación · afirmación · respaldo literal o NO VERIFICADO · veredicto: RESPALDADA / PARCIAL / NO RESPALDADA) y la lista de problemas de la bibliografía.
