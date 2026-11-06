# W2 · Navegación de los anexos: enlaces en los índices, botón de regreso y atajos de teclado

Contexto: `Other/defensa/insertar_videos.py` posprocesa el HTML que exporta Claude Design para la presentación de defensa (reinserta videos, figuras, fuentes, círculos ❶❷ y ajustes de composición). Hay que añadirle la navegación de los anexos. Léelo completo antes de empezar y conserva todo lo que ya hace.

## Cómo es el HTML exportado (comprobado)
- Cada diapositiva es `<section class="deck-slide" id="N" aria-label="Slide N of M" data-label="…" data-speaker-notes="…">`, con N de 1 a M. Dentro hay un lienzo `<div class="slide" … style="width: 1920px; height: 1080px; position: relative; …">`.
- El visor navega con la dirección: cambiar `location.hash` a `#N` lleva a la diapositiva N (hay un listener de `hashchange` en el script del deck). Por tanto un `<a href="#N">` salta a la diapositiva N.
- El visor avanza con clic en la diapositiva, pero ignora los clics sobre `a` (su handler hace `closest("a,[data-text-path],…")`). Teclas que ya usa el visor: espacio, flechas, Av/Re Pág, Inicio, Fin, f/F (pantalla completa). El script de videos (`tt-videos-js`) intercepta →, espacio y Av Pág en las diapositivas con video: no lo rompas.
- Los textos visibles están en `<div data-text-path="…" …>texto</div>`.
- Las diapositivas de anexo tienen en el pie un texto «Anexo N / M» (p. ej. «Anexo 16 / 86» o «Reporte técnico, p. 126 · Anexo 65 / 86»). Ese N es el número de anexo, distinto del número de diapositiva.

## Convenciones de la próxima exportación (ronda 8)
- Tres diapositivas índice, con `data-label` exactamente: «Índice de respuestas», «Índice de figuras», «Índice de tablas».
- Cada entrada de un índice es **un solo** bloque de texto que empieza con el número de anexo: «57 · ¿Por qué no una CNN?», «63 · Figura 6.2.3 · Diferencia geométrica», «90 · Cuadro 12 · Separabilidad de los kernels».
- Grupo de cada anexo según su `data-label`: empieza con «Figura » → figuras; empieza con «Cuadro » → tablas; cualquier otro → respuestas.
- **Para poder probar ya**, acepta también el formato de la exportación actual (ronda 7, `~/Downloads/Defensa TT 2026-B039.html`): el índice de respuestas tiene `data-label` «Anexos» y sus entradas son pares de bloques («1», «Estado del arte»): un bloque que solo tiene el número y el bloque siguiente con el nombre (enlaza los dos); el índice de figuras tiene `data-label` «Índice de figuras del reporte» y entradas en pares («Figura 3.4.1», «→ Anexo 51»): enlaza los dos. No hay índice de tablas: el script debe avisar y seguir.

## Qué añadir a insertar_videos.py
1. **Mapa** anexo N → id de su diapositiva (del pie «Anexo N / M») y grupo de cada anexo. Mapa grupo → id de su diapositiva índice.
2. **Enlaces en los índices:** cada entrada (formatos de arriba) queda envuelta en `<a class="tt-enlace" href="#ID">…</a>` hacia la diapositiva de su anexo, sin cambiar su aspecto (hereda color y tipografía; subrayado solo al pasar el ratón).
3. **Barra de índices** en cada diapositiva índice: tres fichas pequeñas «Respuestas · Figuras · Tablas» arriba a la derecha (`position:absolute; right:120px; top:44px` dentro del lienzo), enlazadas a los tres índices; la del índice actual resaltada. Omite la ficha de un índice que no exista.
4. **Botón de regreso** en cada anexo: `<a class="tt-volver" href="#ID_DEL_INDICE_DE_SU_GRUPO">↩ Índice</a>`, abajo al centro del lienzo (`position:absolute; left:50%; transform:translateX(-50%); bottom:40px`), ficha discreta con el estilo del deck (Inter 15 px, color `#505468`, fondo `#F3F4FB`, radio grande). Exactamente uno por anexo.
5. **Atajos de teclado** (un `<script id="tt-nav-js">` propio, listener en `window` con `capture: true`, ignorando teclas con Ctrl/Alt/Meta):
   - dígitos 0–9: acumulan un número de anexo y muestran un indicador pequeño abajo a la derecha («Anexo 57 ⏎»); Enter salta a ese anexo; Escape o 4 s sin teclear lo cancelan; Retroceso borra un dígito; si el anexo no existe, el indicador dice «No existe el anexo 57» y se borra;
   - «i» o «I»: va al Índice de respuestas; si ya estás en un índice, pasa al siguiente (respuestas → figuras → tablas → respuestas);
   - solo detén la propagación de las teclas que manejas, y Enter solo cuando hay un número en curso. No uses «f».
   - El indicador no sale al imprimir (`@media print`). Los enlaces y botones sí se imprimen.
6. Que todo sea idempotente con el control actual («El archivo ya tiene los videos insertados») y que imprima un resumen: entradas enlazadas por índice, anexos con botón, anexos sin índice de su grupo.

## Pruebas (obligatorias) en `Other/defensa/probar_navegacion.py`
Con la exportación actual (`~/Downloads/Defensa TT 2026-B039.html`) procesada a un archivo temporal (no sobrescribas `Other/defensa/Defensa TT 2026-B039.html`):
- todos los `href="#N"` añadidos apuntan a un `id` de sección existente;
- índice «Anexos»: 50 entradas enlazadas, cada una al anexo de su número; índice de figuras: 36;
- cada diapositiva con pie «Anexo N / M» tiene exactamente un `tt-volver`, que apunta al índice de su grupo;
- imprime a PDF con Chrome headless (`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=20000 --print-to-pdf=… file://…`) y comprueba con PyMuPDF (`/opt/anaconda3/bin/python`, `page.get_links()`) que en la página del índice hay enlaces internos (`kind == fitz.LINK_GOTO`) a las páginas correctas y que la página de un anexo tiene el enlace de regreso. Reporta los conteos.
- Renderiza a PNG la página del índice de respuestas, la del índice de figuras y dos anexos (uno de texto y uno de figura) y revisa que el botón y la barra no tapen contenido. Guárdalas en `Other/defensa/anexos/revision/`.

## Reglas
- Solo puedes modificar `Other/defensa/insertar_videos.py` y crear `Other/defensa/probar_navegacion.py` y archivos en `Other/defensa/anexos/revision/`. Nada de git. No sobrescribas el HTML ni el PDF del repo.
- Hecho = las pruebas pasan y reportas sus salidas y las rutas de las capturas. Los atajos de teclado no se pueden probar sin navegador: dilo en el reporte y describe cómo los probaste (por ejemplo, con un HTML mínimo y lectura del código), sin afirmar que funcionan si no los ejecutaste.
