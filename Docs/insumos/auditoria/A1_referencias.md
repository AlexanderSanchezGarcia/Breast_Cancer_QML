# A1 · Referencias cruzadas, etiquetas y bibliografía (mecánica)

Lee primero `Docs/insumos/auditoria/reglas.md`.

Alcance: `Docs/Technical_Report.tex`, todos los `.tex` de `Docs/capitulos/` que incluye (excepto `borrador_*.tex` y `comun/`), `Docs/bibliografia.tex`, `Docs/tablas/*.tex`.

Escribe un script propio en `Docs/insumos/auditoria/a1_refs.py` (con el Python de qml_cancer) que liste:
1. `\label` definidos y nunca referenciados (`\ref`, `\eqref`, `\autoref`, `\cref`, `\pageref`). Lista aparte de las etiquetas de figuras y tablas nunca referenciadas en el texto: toda figura y tabla debería citarse al menos una vez.
2. `\ref`/`\eqref` a etiquetas inexistentes, y etiquetas duplicadas.
3. `\cite{}` a claves sin `\bibitem`, y `\bibitem` que nadie cita.
4. `\bibitem` duplicados o casi duplicados (mismo DOI, mismo título con distinta clave).
5. Referencias del tipo «sección ??», «Tabla~\ref» con el prefijo incorrecto (por ejemplo, «Figura~\ref{tab:…}» o «Tabla~\ref{fig:…}»), «ecuación~\ref» sin `\eqref`.
6. Menciones en el texto visible a números de sección escritos a mano («§4.9», «sección 6.2», «Capítulo 5») en lugar de `\ref`: compara cada una con la numeración real del PDF (usa el `.toc` de una compilación en `/tmp/aud_A1`). La numeración de capítulos cambió en TT2 (EDA es el capítulo 4 y Metodología el 5), así que las menciones a mano son la sospecha principal.
7. Rutas de `\includegraphics`, `\input` y `\lstinputlisting` que no existan, o que difieran solo en mayúsculas (macOS no distingue mayúsculas; Linux sí).

Compila una vez en `/tmp/aud_A1` y extrae del `.log`: referencias sin resolver, `Overfull \hbox` mayores de 10 pt con su archivo y línea, `Float too large`.

Entrega: `informe_A1.md` + `a1_refs.py` (el script, para que el coordinador lo vuelva a correr).
