# T8 · Un borrador compilable por capítulo, más el completo

Lee primero `Docs/insumos/noche/reglas.md`. Todas sus prohibiciones siguen vigentes. Esta tarea es **de infraestructura**: no cambias ni una palabra del contenido de los capítulos, salvo lo que el punto 4 te pide copiar literalmente.

## Contexto

`Docs/capitulos/` tiene una carpeta por capítulo con un `.tex` por subsección: `2_Antecedentes`, `3_Marco_Teorico`, `4_EDA`, `5_Metodologia`, `6_Resultados` y `A_Anexos`. El coordinador creará luego `1_Panorama_General` y `7_Conclusiones`. Tu solución debe recogerlas solas cuando existan, sin tocar el script.

Hoy solo existe `compilar_prueba.sh`, que genera un único PDF temporal. El autor quiere revisar y editar **capítulo por capítulo**: en cada carpeta, un `.tex` principal que compile ese capítulo solo, con su PDF al lado. Además, un borrador completo con todos los capítulos.

## Tú escribes solo en

- `Docs/capitulos/comun/` (nueva): piezas compartidas generadas.
- `Docs/capitulos/<carpeta>/borrador_<carpeta>.tex` y `Docs/capitulos/<carpeta>/borrador_<carpeta>.pdf`, uno por carpeta de capítulo.
- `Docs/capitulos/borrador_completo.tex` y `Docs/capitulos/borrador_completo.pdf`.
- `Docs/capitulos/compilar_borradores.sh` (nuevo).
- `Docs/capitulos/_build/` (nueva): auxiliares de compilación.
- `Docs/capitulos/.latexmkrc` (nuevo), si lo necesitas para el punto 3.
- `Docs/capitulos/compilar_prueba.sh`, solo para que ignore los `borrador_*.tex` (punto 5).
- `Docs/capitulos/2_Antecedentes/`: los archivos nuevos del punto 4, y `2.1.6_tabla_ampliada.tex` solo como dice ese punto.
- `Docs/capitulos/README.md`: añade una sección «Borradores por capítulo». No borres nada de lo que ya tiene.
- Tu informe: `Docs/insumos/noche/informe_T8.md`.

**No toques** `.gitignore`, los demás `.tex` de los capítulos, `Docs/tablas/`, `Docs/codigo/` ni `Docs/insumos/*.tex`.

## Lo que hay que construir

### 1. Piezas compartidas (`comun/`), generadas por el script

- **`comun/preambulo.tex`:** el preámbulo de `Docs/Technical_Report.tex`, todo lo anterior a `\begin{document}`, seguido de `Docs/insumos/preambulo_extra.tex`. Se genera en cada ejecución; no se edita a mano. Debe cargar `xr-hyper` **antes** de `hyperref`, por el punto 2.
- **`comun/bibliografia_completa.tex`:** el `thebibliography` que hoy arma `compilar_prueba.sh`, con las mismas fuentes y el mismo filtrado de duplicados. Son el `.tex`, más `bibitems_nuevos.tex` sin `huang2021power` ni `TandFOnline2021`, más `bibitems_noche.tex`.
- Cada carpeta lleva su bibliografía **con solo las claves que cita ese capítulo**. El script la extrae de `\cite`, `\citep` y `\citet`, también de las llamadas con varias claves separadas por comas. Si una clave citada no tiene `\bibitem`, el script falla con un mensaje claro.

### 2. Referencias entre capítulos

Un capítulo compilado solo no conoce las etiquetas de los demás. Usa `xr-hyper` con `\externaldocument` sobre un `.aux` **filtrado**. El script compila primero el borrador completo y luego, por cada capítulo, genera `_build/externo_<carpeta>.aux` con las líneas `\newlabel` del `.aux` completo **cuyas etiquetas no estén definidas en ese capítulo**. Así no aparecen avisos de etiqueta duplicada.

La numeración debe coincidir con la del completo. Si en el completo Metodología es la sección 5, en su borrador también; ajusta el contador de `section` antes del primer `\input`. Los anexos usan `\appendix` (ya está en `A.0_introduccion.tex`) y deben salir con letras.

### 3. Los `.tex` principales

- **`<carpeta>/borrador_<carpeta>.tex`:** corto y legible. Lleva una cabecera de comentario con qué es, cómo compilarlo y que lo genera el script. Luego `\input{…/comun/preambulo}`, `\externaldocument`, `\begin{document}`, el contador, un `\input` por cada subsección **en el orden del reporte** y la bibliografía del capítulo. El script lo regenera, así que la lista de `\input` refleja siempre los archivos de la carpeta. El orden es el de `compilar_prueba.sh` (`sort -t_ -k1,1V`); comprueba que deja `5.10` y `5.11` después de `5.9`.
- **`borrador_completo.tex`:** índice (`\tableofcontents`) y todos los capítulos en el orden 1, 2, 3, 4, 5, 6, 7, A, con los que existan. Un `\input` por subsección, agrupados con un comentario por capítulo, y la bibliografía completa. Sin portada.
- Los capítulos usan rutas relativas a `Docs/`: `Figures/…`, `tablas/…`, `codigo/…`, `Logos/…`. Deben resolverse de las dos formas:
  - con el script;
  - con `cd Docs/capitulos/<carpeta> && latexmk -pdf borrador_<carpeta>.tex`, que es como compila el autor desde VSCode con LaTeX Workshop.

  Para la segunda forma usa `\graphicspath` y `TEXINPUTS` (en `Docs/capitulos/.latexmkrc`, que latexmk lee al subir por directorios, o en un `latexmkrc` por carpeta si no lo hace; compruébalo). Los auxiliares van a `_build/`; en cada carpeta solo quedan el `.tex` principal y el `.pdf`.

### 4. §2 completo

`2_Antecedentes/` solo tiene lo nuevo (§2.1.6–§2.1.9). Para que su borrador sea el capítulo entero, copia **literalmente** las líneas correspondientes de `Docs/Technical_Report.tex`:

| Archivo nuevo | Líneas del `.tex` |
|---|---|
| `2.0_introduccion.tex` | de `\section{Antecedentes}` (l. 692) hasta antes de la primera `\subsubsection` (l. 701), con `\subsection{Estado del arte}` |
| `2.1.1_ml_clasico.tex` | 701 hasta antes de 726 |
| `2.1.2_deep_learning.tex` | 726 hasta antes de 751 |
| `2.1.3_fundamentos_qml.tex` | 751 hasta antes de 799 |
| `2.1.4_hibridos_salud.tex` | 799 hasta antes de 815 |
| `2.1.5_cbis_ddsm.tex` | 815 hasta antes de 831 |

Las líneas 831–838 (la `\subsubsection{Tabla comparativa y brechas identificadas}` y su texto previo a la tabla) y lo que haya entre el `\end{table}` original y `\section{Marco Teórico}` van **dentro** de `2.1.6_tabla_ampliada.tex`: las primeras antes del `\begin{landscape}` y las segundas después del cierre. Las tablas original y ampliada no deben aparecer las dos. Antes de cortar, comprueba los números de línea con `grep -n`: si no coinciden con los de esta tabla, usa los reales y anótalo.

Cada archivo nuevo lleva su cabecera, con las líneas del `.tex` que reemplaza y la nota `% Copia literal de TT1; pendiente de corrección con Docs/insumos/auditoria_s1_s2.md.` Añade `\label{sec:antecedentes}` tras el `\section` si no existe ya en otra parte (`grep -rn 'sec:antecedentes' Docs/`).

**Prueba de literalidad (obligatoria):** un script de Python, dentro del propio `compilar_borradores.sh` o como `Docs/capitulos/comun/verificar_literal_s2.py`. Debe quitar las cabeceras de comentario y la etiqueta añadida, y comprobar que el resto de los archivos copiados es idéntico, línea a línea, a los rangos del `.tex`. Copia su salida en el informe.

### 5. `compilar_prueba.sh`

Cambia solo el bucle que lista `*.tex` para que excluya `borrador_*.tex`; si no, se incluiría a sí mismo. Nada más.

### 6. `compilar_borradores.sh`

- Uso: `bash Docs/capitulos/compilar_borradores.sh` (todo) o `bash Docs/capitulos/compilar_borradores.sh 5_Metodologia 6_Resultados`. Con argumentos, igual compila antes el completo, porque hace falta su `.aux`.
- Pasos: regenerar `comun/`, los `borrador_*.tex` y el completo; compilar el completo (las pasadas que hagan falta para el índice y las referencias); generar los `.aux` filtrados; compilar cada capítulo; dejar los PDF en su sitio.
- Al final, una tabla por documento con: páginas, referencias o citas sin resolver, etiquetas duplicadas y cajas desbordadas de más de 10 pt.
- Encuentra `pdflatex` y `latexmk` como `compilar_prueba.sh` (`/Library/TeX/texbin`). Que falle con `set -euo pipefail` y un mensaje claro ante un error de LaTeX, indicando qué documento falló.
- No toca nada fuera de lo que lista «Tú escribes solo en».

## Aceptación

1. `bash Docs/capitulos/compilar_borradores.sh` termina sin error. Genera `borrador_completo.pdf` y un `borrador_<carpeta>.pdf` en cada carpeta: 2, 3, 4, 5, 6 y A.
2. **Cero** referencias o citas sin resolver en todos los documentos. Cero etiquetas duplicadas. Las referencias cruzadas de un capítulo a otro muestran número, no `??`. Compruébalo con `pdftotext` si está disponible, o con `grep '??'` sobre el `.log`. Pon tres ejemplos concretos en el informe, como «5.4 cita la sección 4.2 y en el PDF dice 4.2».
3. La numeración coincide: la primera sección de cada PDF por capítulo tiene el mismo número que en el completo. Inclúyelo en la tabla del informe.
4. La bibliografía de cada capítulo contiene solo las claves que cita.
5. Funciona `cd Docs/capitulos/5_Metodologia && latexmk -pdf borrador_5_Metodologia.tex`, y en la carpeta no quedan auxiliares. Pruébalo también con `6_Resultados` y `A_Anexos`.
6. La prueba de literalidad de §2 pasa.
7. `bash Docs/capitulos/compilar_prueba.sh 5_Metodologia` sigue diciendo «Compila sin errores» y no incluye `borrador_*`.
8. Crea temporalmente `Docs/capitulos/7_Conclusiones/7.0_prueba.tex`, con `\section{Conclusiones}\label{sec:conclusiones_prueba}` y una frase. Comprueba que el script la recoge sola y que aparece en el completo después de §6 y antes de los anexos. **Después borra esa carpeta**, sus PDF y lo que haya generado.
9. El informe `Docs/insumos/noche/informe_T8.md` lleva:
   - la salida final del script;
   - la tabla de documentos;
   - la prueba de literalidad;
   - los tres ejemplos de referencias cruzadas;
   - cualquier desviación de esta especificación y su motivo.

   No declares nada «verificado» que no hayas ejecutado.
