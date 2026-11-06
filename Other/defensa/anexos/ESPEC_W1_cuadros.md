# W1 · Recortar los 36 cuadros (tablas) del reporte técnico como imágenes

Contexto: presentación de defensa de una tesis. Los anexos del final llevarán cada tabla del reporte técnico como imagen, recortada del PDF, para que las cifras sean exactamente las del reporte (nadie las reescribe a mano).

## Entrada
- `Docs/Technical_Report.pdf` (215 páginas). Las tablas se llaman **«Cuadro N:»** (no «Tabla»): el pie va **arriba** de la tabla, p. ej. «Cuadro 12: Separabilidad en la familia de kernels (M6), …». Debajo de muchas tablas hay una nota en letra más pequeña («El exceso es…»), que **sí** forma parte del recorte. Después viene texto normal del cuerpo, que **no** debe entrar.
- `Docs/Technical_Report.lot`: la lista de los 36 cuadros con su título y la página impresa (`\contentsline {table}{\numberline {N}…}{página}`). La página impresa coincide con el número de página física del PDF (1-based), pero no lo supongas: localiza cada pie buscando el texto «Cuadro N:» en el PDF.
- Python con PyMuPDF: `/opt/anaconda3/bin/python` (`import fitz`). No instales nada.

## Qué hacer
1. Escribe `Other/defensa/extraer_tablas.py` que, para cada N de 1 a 36:
   - localice el pie «Cuadro N:» (si un cuadro ocupa varias páginas, tendrá continuación; detéctalo);
   - recorte la región: desde el borde superior del pie hasta el final de la tabla **incluida su nota**, con un margen de ~10 pt, a todo el ancho de la caja de texto. Pistas: `page.get_text('dict')` da bloques con tamaño de letra (la nota y el contenido de la tabla suelen ir en letra menor que el cuerpo); `page.get_drawings()` da las reglas horizontales de la tabla (booktabs). El recorte termina antes del primer bloque de texto del cuerpo (tamaño normal, ancho completo) que sigue a la tabla, o antes del pie de página / número de página;
   - guarde PNG a 200 dpi, fondo blanco: `Other/defensa/tablas_anexos/Cuadro_N.png`; si ocupa varias páginas, `Cuadro_N_a.png`, `Cuadro_N_b.png`, …
2. Escribe `Other/defensa/tablas_anexos/manifiesto.json`, una entrada por cuadro: `numero`, `titulo` (del .lot, limpio de LaTeX: sin `\ignorespaces`, `\textit{}`, `$…$` convertido a texto legible), `pagina_reporte` (la del .lot), `paginas_pdf` (índices 1-based donde lo recortaste), `archivos` (lista), `multipagina` (bool), `orden_deck`.
   - `orden_deck`: primero 1–5 y 9–34 en orden; al final las administrativas 6, 7, 8, 35 y 36. Es decir, orden_deck 1..31 para [1,2,3,4,5,9,…,34] y 32..36 para [6,7,8,35,36].
3. Verificación automática (imprímela en tu reporte final), para cada cuadro:
   - el texto dentro del rectángulo recortado (`page.get_text(clip=rect)`) empieza con «Cuadro N:» (en la primera parte);
   - las primeras y las últimas ~70 letras del texto recortado;
   - tamaño en px de cada PNG.
4. Hojas de contacto para revisión humana: `Other/defensa/tablas_anexos/revision/hoja_1.png`, `hoja_2.png`, … con 6 recortes por hoja, cada uno con su número encima. Revísalas tú mismo al 100 % y corrige recortes que corten la tabla o que incluyan texto del cuerpo.

## Reglas
- Solo puedes crear o modificar `Other/defensa/extraer_tablas.py` y archivos dentro de `Other/defensa/tablas_anexos/`. Nada de git. No toques el PDF ni ningún otro archivo.
- No inventes títulos ni páginas: salen del .lot y del PDF.
- Hecho = 36 cuadros con sus PNG, el manifiesto, las hojas de contacto y la verificación del punto 3 sin fallos. Si algún cuadro no se puede recortar bien, entrégalo marcado como dudoso en el reporte, no lo des por bueno.
