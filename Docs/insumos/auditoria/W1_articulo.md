# W1 · Borrador del artículo técnico (IEEE, máximo 6 cuartillas)

Lee primero `Docs/insumos/auditoria/reglas.md`. **Excepción a la regla 1**: en esta tarea escribes, y solo, dentro de `Docs/articulo/` (créala): `articulo.tex`, `referencias.tex` si la separas, y tu informe `Docs/insumos/auditoria/informe_W1.md`. Las figuras se toman de `../Figures/` con `\graphicspath`; no copies ni generes figuras nuevas.

## Formato (requisito de la CATT; ejemplo en `Other/ESCOM/Ejemplo Articulo Tecnico.pdf`)

- `\documentclass[conference,letterpaper]{IEEEtran}`, dos columnas, en **español** (`\usepackage[spanish]{babel}`, `inputenc utf8`, `fontenc T1`).
- **Máximo 6 páginas** incluyendo referencias. Compila y cuenta.
- Título: «Modelo de transformación cuántica variacional de características de cáncer de mama para un sistema híbrido de prediagnóstico».
- Autores en una línea: Miguel Alexander Sánchez García, Jesús Yaljá Montiel Pérez, Ana María Winfield Reyes (directores en orden alfabético por apellido, como en el reporte). Debajo: «Escuela Superior de Cómputo, Instituto Politécnico Nacional, Ciudad de México» y «Tel. 57-29-6000 ext. 52000 y 52021. E-mail: msanchezg1904@alumno.ipn.mx». No inventes correos de los directores: deja `[VERIFICAR: correo de los directores]` en un comentario.
- Secciones, en este orden: Resumen (`\begin{abstract}` con el rótulo «Resumen»), Palabras clave (`\begin{IEEEkeywords}` con rótulo «Palabras clave»), I. Introducción, II. Metodología, III. Resultados, IV. Conclusiones, Referencias.
- Referencias en **formato IEEE** (`\begin{thebibliography}`), numeradas por orden de aparición. Toma los metadatos **solo** de `Docs/bibliografia.tex` (reformateándolos a IEEE: iniciales y apellido, «título», *revista*, vol., no., pp., año, doi). Entre 10 y 18 referencias. Ninguna referencia que no esté en `Docs/bibliografia.tex`.

## Contenido

El artículo es una síntesis del reporte, no un texto nuevo. Fuentes, en este orden de prioridad:
1. `Docs/capitulos/0_Preliminares/resumen.tex` (estructura del argumento);
2. `Docs/capitulos/1_Panorama_General/` (motivación, pregunta, objetivos), `5_Metodologia/` (pipeline M1–M8 y las cinco condiciones), `6_Resultados/` (cifras), `7_Conclusiones/`.

Reglas:
- **Cada cifra** del artículo debe aparecer tal cual en un archivo de `Docs/capitulos/6_Resultados/` o `5_Metodologia/`. Encima de cada párrafo con cifras pon `% fuente: <archivo.tex>:<línea>`. Si una cifra no la encuentras literal, no la escribas.
- Regla 1 de `CLAUDE.md`: el objetivo es la viabilidad y la separabilidad, no superar a lo clásico. El resultado principal es negativo y se presenta como evidencia válida, con sus causas (concentración del kernel, lectura de ⟨Z_i⟩) y las restricciones del simulador (OE-6).
- Masas y calcificaciones se reportan por separado.
- Una figura como máximo dos: elige entre las que ya usa §6 (`grep includegraphics Docs/capitulos/6_Resultados/*.tex`). Una tabla compacta de AUC del test por condición y subconjunto, con los valores copiados de `Docs/tablas/m7_clasificacion.tex`.
- Estilo: el de `reglas.md` de la noche anterior aplica: comillas ``…'', sin incisos con `---`, sin D-xxx/H-xxx visibles, lenguaje calibrado (nunca «ventaja cuántica» como algo observado).

## Prueba

`cd Docs/articulo && export PATH="/Library/TeX/texbin:$PATH" && pdflatex -interaction=nonstopmode -output-directory /tmp/aud_W1 articulo.tex` (dos pasadas). Informa el número de páginas, las referencias sin resolver (deben ser cero) y las cajas desbordadas. No dejes el PDF ni auxiliares dentro del repositorio.

Entrega: `Docs/articulo/articulo.tex` + `informe_W1.md` con la tabla de cifras (cifra · fuente archivo:línea) y la lista de referencias usadas con su clave original de `bibliografia.tex`.
