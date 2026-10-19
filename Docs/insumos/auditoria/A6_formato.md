# A6 · Cumplimiento del formato de la CATT

Lee primero `Docs/insumos/auditoria/reglas.md`.

Fuentes del formato (léelas tú; están en `Other/ESCOM/`):
- `Disk Content Specifications 2026.docx` («Documentación a entregar posterior a las presentaciones»): `textutil -convert txt -stdout "<archivo>"`.
- `Formato Reporte Tecnico TT25.pdf` (escaneado, sin texto): su contenido ya lo transcribió el coordinador así: portada con márgenes 2 cm arriba, 2 cm abajo, 3 cm izquierda, 2 cm derecha **en todo el documento**; fuentes Times New Roman, Calibri o Verdana; 12 pt en el cuerpo; tamaños de la portada 20/16/16/14/16/12; nombres en la portada «nombre seguido del apellido», directores en orden alfabético por apellido, director externo a la derecha; hoja de resumen («Documento Técnico») con No. de TT, fecha de presentación de TT-II, correo del participante al pie; carta responsiva escaneada; advertencia (texto fijo); agradecimientos opcionales; carta de autorización de difusión antes del índice; índice con enlaces y marcadores; secciones obligatorias INTRODUCCIÓN, CONCLUSIONES, TRABAJO A FUTURO, REFERENCIAS y GLOSARIO; apéndices.
- `Carta Responsiva TT 2026.docx`: texto de la carta.

Comprueba contra `Docs/Technical_Report.tex` y el PDF `Docs/Technical_Report.pdf`:
1. Lista de verificación punto por punto (CUMPLE / NO CUMPLE / PARCIAL / NO APLICA TODAVÍA), con la línea del `.tex` o la página del PDF como evidencia.
2. Márgenes: busca cualquier `\newgeometry`, `\geometry`, `adjustbox`, `\hspace{-…}` o figura/tabla que invada el margen; lista las cajas desbordadas (compila en `/tmp/aud_A6`).
3. Tamaño de letra: cualquier `\small`, `\footnotesize`, `\scriptsize` en el cuerpo del texto (no en tablas, pies o código). Indica si es defendible.
4. Marcadores del PDF: compila y comprueba en el `.out` que hay marcadores para portada, resumen, cartas, advertencia, índices, cada sección, referencias, glosario y cada anexo.
5. Que el índice de contenidos tenga enlaces (hyperref) y que existan índice de figuras, de tablas y de listados.
6. Qué secciones obligatorias faltan o están con otro nombre (por ejemplo, ¿hay una «Introducción» reconocible como tal en el índice, o solo «Panorama General»?).
7. Datos para la **carta de autorización de difusión**: cuenta las páginas del PDF desde la hoja de Resumen (incluida) y desde la carta de difusión, como lo pide el instructivo (Sección II, puntos 2 y 4). Indica las dos cifras con la página de inicio de cada una.
8. Discrepancias entre los propios documentos de la CATT (por ejemplo, el orden de los nombres o el nombre de la Secretaria Ejecutiva en el PDF del formato frente a la carta 2026).

Entrega: `informe_A6.md` con la lista de verificación y los hallazgos.
