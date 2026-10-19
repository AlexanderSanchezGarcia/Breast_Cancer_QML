# G1 · Borrador del glosario

Lee primero `Docs/insumos/auditoria/reglas.md`. **Excepción a la regla 1**: en esta tarea sí escribes un `.tex`, y solo uno: `Docs/insumos/auditoria/glosario_borrador.tex` (el coordinador lo revisa y lo copia a `Docs/capitulos/G_Glosario/`). No edites `Docs/capitulos/G_Glosario/glosario.tex`.

El formato de la CATT exige una sección GLOSARIO después de Referencias.

1. Recorre los capítulos 1 a 8 y lista los términos técnicos que un sinodal de computación (no especialista en cuántica ni en radiología) necesitaría: computación cuántica (qubit, superposición, entrelazamiento, esfera de Bloch, compuerta, circuito parametrizado, *feature map*, *ansatz*, valor esperado, *shots*/disparos, simulador de vector de estado, kernel de fidelidad, concentración del kernel, *parameter-shift*, NISQ, transpilación…), aprendizaje automático (MLP, AUC-ROC, validación cruzada, *data leakage*, Kernel PCA, SVM, KTA, *geometric difference*, dimensión efectiva, Davies-Bouldin, Fisher, t-SNE, Spearman…), imagen médica (mamografía, masa, calcificación, ROI, DICOM, CBIS-DDSM, BI-RADS si aparece, radiómica, PyRadiomics, GLCM, GLRLM, IBSI, CLAHE…).
2. Para cada término: una definición de una o dos oraciones **coherente con la definición que ya da el reporte** (busca dónde se define y respeta su notación), y entre paréntesis la sección donde se define con `\ref` a una etiqueta que exista (compruébalo con `grep -rn '\\label{'`). Si el reporte no lo define, dilo en un comentario `% sin definición en el reporte`.
3. Formato: `\begin{description}` con `\item[Término.]`, en orden alfabético (ignorando mayúsculas y tildes), sin `\section` (la cabecera ya está en `glosario.tex`). Términos en inglés en `\textit{}` con su traducción si se usa en el texto.
4. Entre 40 y 70 entradas. Nada de definiciones de diccionario genéricas: cada una debe servir para leer este reporte.
5. Prueba: crea una copia temporal fuera del repo (`/tmp/aud_G1/`) de `Docs/capitulos/G_Glosario/glosario.tex` con tu borrador en lugar del `\begin{description}…\end{description}` y compila el reporte desde una copia de `Docs/` en `/tmp/aud_G1/Docs` (copia la carpeta `Docs` completa ahí; no compiles dentro del repo). Debe compilar sin referencias sin resolver.

Entrega: `glosario_borrador.tex` + `informe_G1.md` (lista de términos, los que quedaron sin definición en el reporte, salida de la compilación).
