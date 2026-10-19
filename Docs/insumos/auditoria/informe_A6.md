# Informe de Auditoría A6 · Cumplimiento del Formato de la CATT

- **Tarea:** A6 · Auditoría de cumplimiento del formato de la CATT para el Trabajo Terminal 2026-B039.
- **Fecha y hora de ejecución:** 2026-10-18T23:22:00-06:00.
- **Auditor:** Antigravity (dispatched worker, terminal `term_bb382e39-f342-4bdf-8546-49a1e5b92308`).
- **Estado de edición:** Modo solo lectura respetado; únicamente se generó este archivo de informe dentro de `Docs/insumos/auditoria/`.

---

## 1. Alcance revisado

Se auditaron los siguientes documentos normativos y fuentes institucionales ubicados en `Other/ESCOM/`:
- `Disk Content Specifications 2026.docx` («Documentación a entregar posterior a las presentaciones»).
- `Formato Reporte Tecnico TT25.pdf` (documento escaneado de 9 páginas con las directrices de portada, márgenes, tipografía, resumen, cartas, advertencia, índices, secciones obligatorias y apéndices).
- `Carta Responsiva TT 2026.docx` (plantilla oficial actualizada de la carta responsiva para la entrega en DVD).
- `Protocolo.pdf` (versión registrada oficial del protocolo del TT 2026-B039).

Frente a la implementación y reporte en:
- `Docs/Technical_Report.tex` (546 líneas; archivo maestro del reporte técnico).
- `Docs/Technical_Report.pdf` (194 páginas; versión compilada oficial en el repositorio).
- Compilación limpia en `/tmp/aud_A6/Technical_Report.pdf` (194 páginas, generada en dos pasadas completas con `pdflatex` y analizada con su transcript `Technical_Report.log`).
- Todos los capítulos incluidos en `Docs/capitulos/**/*.tex` y tablas en `Docs/tablas/*.tex`.

---

## 2. Comandos ejecutados y salida final

### 2.1 Compilación aislada en dos pasadas
```bash
export PATH="/Library/TeX/texbin:$PATH"
mkdir -p /tmp/aud_A6
cd Docs
pdflatex -interaction=nonstopmode -output-directory /tmp/aud_A6 Technical_Report.tex
pdflatex -interaction=nonstopmode -output-directory /tmp/aud_A6 Technical_Report.tex
```
**Salida final:**
```
Output written on /tmp/aud_A6/Technical_Report.pdf (194 pages, 14857345 bytes).
Transcript written on /tmp/aud_A6/Technical_Report.log.
Exit code: 0
```

### 2.2 Extracción de texto y OCR de las especificaciones de CATT
```bash
textutil -convert txt -stdout "Other/ESCOM/Disk Content Specifications 2026.docx"
textutil -convert txt -stdout "Other/ESCOM/Carta Responsiva TT 2026.docx"
gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=png16m -r150 -sOutputFile="/tmp/formato_page_%02d.png" "Other/ESCOM/Formato Reporte Tecnico TT25.pdf"
# OCR de las 9 páginas mediante tesseract vía stdin
```
**Salida final:** Extracción completa de directrices de portada, hoja de resumen, carta responsiva, advertencia, carta de autorización de difusión e índice.

### 2.3 Inspección programática del PDF con PyMuPDF (`fitz`)
```bash
python3 -c "
import fitz
doc = fitz.open('/tmp/aud_A6/Technical_Report.pdf')
# Análisis de páginas, enlaces de índices, marcadores jerárquicos y dimensiones de cajas
"
```
**Salida final:**
- Total de páginas: 194.
- Enlaces activos: TOC (146), LOT (39), LOF (139), LOL (30).
- Total de marcadores en el catálogo PDF: 152.
- Advertencias de desbordamiento en log: 29 `Overfull \hbox`, 2 `Overfull \vbox`, 1 `Float too large for page by 145.11188pt`.

---

## 3. Lista de verificación punto por punto

| Elemento / Requisito CATT | Estado | Evidencia técnica (`.tex` / PDF) |
|---|---|---|
| **Márgenes globales:** 2 cm superior, 2 cm inferior, 3 cm izquierdo, 2 cm derecho en todo el documento | CUMPLE | `Docs/Technical_Report.tex:25-30` (`\usepackage[top=2cm,bottom=2cm,left=3cm,right=2cm]{geometry}`). No hay `\newgeometry` secundario. |
| **Ausencia de invasión de márgenes por elementos flotantes y texto** | NO CUMPLE | En Anexo A.1 (`Technical_Report.tex:175`) la numeración de listados invade el margen izquierdo en 9-12 pt (p. 163-171); en Anexo C (`A.3.2_figuras_eda.tex:65`) `fig:sample_gallery` excede la altura por 145.1 pt y se desborda 49 pt fuera de la hoja física en p. 189; en Anexo E (`anexo_e_decisiones.tex:2`) la tabla invade 8.5 pt el margen derecho en pp. 192-194. |
| **Tipografía institucional:** Times New Roman, Calibri o Verdana | CUMPLE | `Docs/Technical_Report.tex:22` (`\usepackage{mathptmx}`, equivalente estándar de Times New Roman en pdfLaTeX). |
| **Tamaño de letra en cuerpo:** 12 pt | CUMPLE | `Docs/Technical_Report.tex:13` (`\documentclass[12pt, letterpaper]{article}`). |
| **Tamaño de letra en tablas, figuras, código y pies:** tamaños reducidos defendibles | CUMPLE | Se emplean `\small` y `\scriptsize` exclusivamente en tablas, diagramas TikZ y listados de código; no hay reducción en el cuerpo del texto regular. |
| **Portada: Encabezado institucional** («INSTITUTO POLITÉCNICO NACIONAL» en 20 pt, «ESCUELA SUPERIOR DE CÓMPUTO» en 16 pt, «ESCOM» en 20 pt) | CUMPLE | `Docs/Technical_Report.tex:227-229`, PDF p. 1. |
| **Portada: Título del Trabajo Terminal** en 16 pt negrita | CUMPLE | `Docs/Technical_Report.tex:236-238`, PDF p. 1. |
| **Portada: Número de TT** en 14 pt («2026-B039») | CUMPLE | `Docs/Technical_Report.tex:239`, PDF p. 1. |
| **Portada: Nombre del estudiante** («nombre seguido del apellido» en 12 pt) | CUMPLE | `Docs/Technical_Report.tex:242` («Miguel Alexander Sánchez García»), PDF p. 1. |
| **Portada: Directores** en orden alfabético por apellido con grado académico | PARCIAL | `Docs/Technical_Report.tex:246-248` ordena alfabéticamente (Dr. Jesús Yaljá Montiel Pérez antes de Dra. Ana María Winfield Reyes; M < W). La guía CATT estipula ubicar al director externo a la derecha (ambos son internos). |
| **Portada: Fecha de presentación** (mes y año de TT-II) | PARCIAL | `Docs/Technical_Report.tex:200` declara «Noviembre de 2026» (`\fechaTTII`), pendiente de día/fecha oficial exacta. |
| **Hoja de Resumen («Documento Técnico»):** Encabezado con logos IPN y ESCOM y Subdirección Académica | CUMPLE | `Docs/Technical_Report.tex:273-285`, PDF p. 2. |
| **Hoja de Resumen: No. de TT y Fecha de presentación** | PARCIAL | `Docs/Technical_Report.tex:288` («No. de TT 2026-B039 \hfill Noviembre de 2026»), PDF p. 2. |
| **Hoja de Resumen: Título entre comillas** y nombre del alumno | CUMPLE | `Docs/Technical_Report.tex:293-296`, PDF p. 2. |
| **Hoja de Resumen: Correo electrónico del participante al pie** | CUMPLE | `Docs/Technical_Report.tex:296` (`\footnote{msanchezg1904@alumno.ipn.mx}`), PDF p. 2. |
| **Hoja de Resumen: Directores en orden alfabético** | CUMPLE | `Docs/Technical_Report.tex:298-301`, PDF p. 2. |
| **Hoja de Resumen: Cuerpo del resumen y Palabras clave** | CUMPLE | `Docs/capitulos/0_Preliminares/resumen.tex:1-10`, PDF p. 2. |
| **Carta Responsiva escaneada** con firmas autógrafas de directores | NO APLICA TODAVÍA / PARCIAL | `Docs/Technical_Report.tex:319-332`, PDF p. 3. Actualmente cuenta con bloque condicional `\IfFileExists{preliminares/carta_responsiva.pdf}` con marco de sustitución. Se integrará escaneada al dictamen final. |
| **Advertencia:** Texto institucional fijo sin modificaciones | CUMPLE | `Docs/Technical_Report.tex:340-354`, PDF p. 4. Coincide exactamente con el texto de `Formato Reporte Tecnico TT25.pdf`, p. 4. |
| **Agradecimientos (opcional):** | CUMPLE / NO APLICA | `Docs/Technical_Report.tex:359-365` preparado y comentado para redacción por el autor. |
| **Carta de Autorización de Difusión en Repositorio Institucional** ubicada antes del índice | PARCIAL | `Docs/Technical_Report.tex:370-383`, PDF p. 5. Ubicada reglamentariamente antes de los índices con bloque condicional `\IfFileExists{preliminares/carta_difusion.pdf}`. Pendiente de firmas en tinta azul y escaneo. |
| **Índice de contenido general con enlaces activos** | CUMPLE | `Docs/Technical_Report.tex:390`, PDF pp. 6-10 (146 enlaces navegables). |
| **Índice de tablas con enlaces activos** | CUMPLE | `Docs/Technical_Report.tex:394`, PDF pp. 11-12 (39 enlaces navegables). |
| **Índice de figuras con enlaces activos** | CUMPLE | `Docs/Technical_Report.tex:398`, PDF pp. 13-16 (139 enlaces navegables). |
| **Índice de listados con enlaces activos** | CUMPLE | `Docs/Technical_Report.tex:402`, PDF p. 17 (30 enlaces navegables). |
| **Marcadores de navegación del PDF (PDF bookmarks)** | NO CUMPLE | Existen los 152 marcadores (`Docs/Technical_Report.tex:162`, `\usepackage{bookmark}`), pero debido a `\pdfbookmark[0]{Índice}{indice}`, todos los capítulos y secciones quedaron anidados dentro de «Índice» como subniveles, y los capítulos 6, 7 y 8 tienen marcadores duplicados. |
| **Sección obligatoria: INTRODUCCIÓN** | NO CUMPLE | `Docs/capitulos/1_Panorama_General/1.0_introduccion.tex:6` titula el capítulo «Panorama General», figurando la introducción únicamente como subsección «1.1 Introducción» (PDF p. 19). |
| **Sección obligatoria: CONCLUSIONES** | CUMPLE | `Docs/capitulos/7_Conclusiones/7.0_introduccion.tex:8` («7 Conclusiones»), PDF p. 145. |
| **Sección obligatoria: TRABAJO A FUTURO** | CUMPLE | `Docs/capitulos/8_Trabajo_Futuro/8.0_introduccion.tex:9` («8 Trabajo a Futuro»), PDF p. 151. |
| **Sección obligatoria: REFERENCIAS** | CUMPLE | `Docs/Technical_Report.tex:528` (`\renewcommand{\refname}{Referencias}` e inclusión de `bibliografia.tex`), PDF p. 154. |
| **Sección obligatoria: GLOSARIO** | PARCIAL | `Docs/capitulos/G_Glosario/glosario.tex:3` incluye la sección en p. 162, pero actualmente contiene solo un texto borrador pendiente (`item[Pendiente.]`). |
| **Sección obligatoria: APÉNDICES / ANEXOS** | PARCIAL | `Docs/Technical_Report.tex:536` y `A.0_introduccion.tex:6` estructuran cinco anexos (A a E, pp. 163-194) bajo la denominación «Anexos» en lugar de «Apéndices». |

---

## 4. Análisis temático detallado

### 4.1 Márgenes y cajas desbordadas
- **Configuración de geometría:** `\geometry{top=2cm, bottom=2cm, left=3cm, right=2cm}` es uniforme y no se vulnera mediante `\newgeometry` en ninguna parte del documento.
- **Análisis de `adjustbox`:** Todas las apariciones de `\begin{adjustbox}{max width=\linewidth}` (en tablas de M4, M6, M7, M8 y Anexos B y D) cumplen la función de encoger tablas anchas para no invadir márgenes.
- **Cajas desbordadas detectadas en `/tmp/aud_A6/Technical_Report.log`:**
  1. *Desbordamiento crítico de figura:* En `Docs/capitulos/A_Anexos/A.3.2_figuras_eda.tex:65-68`, la figura `fig:sample_gallery` (`D4_sample_gallery.png`, resolución 1189×2833 px) arroja `LaTeX Warning: Float too large for page by 145.11188pt`. En el PDF (p. 189), el bloque de imagen desciende hasta `y = 841.0 pt` (el papel mide 792 pt), saliéndose 49 pt fuera de la hoja física y perdiendo por completo la leyenda (`\caption`).
  2. *Invasión de margen en listados:* En `Docs/Technical_Report.tex:175`, `\lstdefinestyle{tt}` no define sangría izquierda (`xleftmargin`). Los números de línea (`numbers=left`) se imprimen en `x = 73.1 pt` a `76.1 pt`, invadiendo el margen izquierdo de 3 cm (85.0 pt) a lo largo de 9 páginas (pp. 163-171).
  3. *Invasión de margen en tabla de bitácora:* En `Docs/tablas/anexo_e_decisiones.tex:2`, `\begin{longtable}{@{}llp{9.4cm}p{2.3cm}@{}}` totaliza un ancho de ~16.8 cm frente a un ancho útil de 16.59 cm, invadiendo el margen derecho en 8.5 pt (pp. 192-194).
  4. *Títulos de listados desbordados:* Siete subtítulos de listados en `A.1_codigo.tex` exceden el ancho de línea entre 35.3 pt y 134.6 pt debido a nombres de archivo largos en `\texttt{...}` sin puntos de quiebre.

### 4.2 Tamaño de letra
- El documento principal se compila en 12 pt (`\documentclass[12pt, letterpaper]{article}`).
- Se rastreó toda ocurrencia de `\small`, `\footnotesize`, `\scriptsize` y `\tiny` en `Docs/capitulos/`:
  - En `Docs/capitulos/5_Metodologia/5.1_descripcion_general.tex`: Se usan dentro del diagrama TikZ para etiquetas de cajas de proceso.
  - En `Docs/capitulos/5_Metodologia/5.2_requerimientos.tex`: Se usan en cabeceras y notas de las tablas de requerimientos funcionales.
  - En tablas de resultados (`5.11_experimentos_complementarios.tex:27`, `2.1.9_tabla_comparativa.tex:24`, `6.2_separabilidad.tex:212`, `6.8_sintesis.tex:19`): Se usan para asegurar legibilidad en tablas densas.
  - En listados de código (`Docs/Technical_Report.tex:171`): `basicstyle=\ttfamily\scriptsize`.
- **Dictamen:** No existe ninguna reducción de tamaño de letra en el cuerpo de la prosa textual. El uso de tamaños menores en tablas, figuras, notas y código es plenamente defendible conforme a las prácticas editoriales y al formato de la CATT.

### 4.3 Marcadores de navegación del PDF
- Se constató la presencia de marcadores mediante `fitz.open().get_toc()`, encontrando 152 entradas.
- **Anomalía crítica estructural:** En `Docs/Technical_Report.tex:389`, la instrucción `\pdfbookmark[0]{Índice}{indice}` define el marcador del índice en nivel raíz (nivel 0). En la clase `article`, todas las divisiones `\section` se compilan como nivel 1 de marcadores. Como consecuencia, el paquete `bookmark` anida los capítulos 1 al 8, Referencias, Glosario y Anexos como hijos subordinados a «Índice». Un lector que colapse el árbol de marcadores sólo ve Portada, Resumen, Carta responsiva, Advertencia, Carta de difusión e Índice.
- **Marcadores y entradas de índice duplicadas:**
  - `Docs/capitulos/6_Resultados/6.0_introduccion.tex:7-8` ejecuta `\section{Resultados}` y seguidamente `\addcontentsline{toc}{section}{Resultados}`.
  - `Docs/capitulos/7_Conclusiones/7.0_introduccion.tex:8-9` ejecuta `\section{Conclusiones}` y `\addcontentsline{toc}{section}{Conclusiones}`.
  - `Docs/capitulos/8_Trabajo_Futuro/8.0_introduccion.tex:9-10` ejecuta `\section{Trabajo a Futuro}` y `\addcontentsline{toc}{section}{Trabajo a Futuro}`.
  Esto produce dos entradas idénticas en la Tabla de Contenidos impresa (PDF pp. 8 y 9) y dos nodos idénticos en los marcadores del PDF para cada uno de estos tres capítulos.

### 4.4 Enlaces e hipervínculos en índices
- Índice de contenido (TOC): 146 hipervínculos funcionales en pp. 6-10.
- Índice de tablas (LOT): 39 hipervínculos funcionales en pp. 11-12.
- Índice de figuras (LOF): 139 hipervínculos funcionales en pp. 13-16.
- Índice de listados (LOL): 30 hipervínculos funcionales en p. 17.
- **Dictamen:** Cumple a cabalidad con la exigencia de la CATT de vincular los índices con las páginas y temas correspondientes.

### 4.5 Secciones obligatorias de la CATT
- `Formato Reporte Tecnico TT25.pdf` (p. 9) prescribe: INTRODUCCIÓN, CAPÍTULOS, CONCLUSIONES, TRABAJO A FUTURO, REFERENCIAS, GLOSARIO y APÉNDICES.
- El reporte técnico omite la sección «INTRODUCCIÓN» como encabezado de primer nivel, denominando al capítulo 1 «1 Panorama General» y relegando la introducción a «1.1 Introducción».
- Las secciones de Conclusiones, Trabajo a Futuro y Referencias cumplen con el estándar.
- Glosario está formalmente creado pero su contenido es un borrador provisional.
- Los Apéndices están titulados como «Anexos» (A a E).

### 4.6 Conteo de páginas para la Carta de Autorización de Difusión
Con base en el instructivo institucional de la CATT (`Disk Content Specifications 2026.docx`, Sección II, puntos 2 y 4) y la versión compilada actual de 194 páginas:
1. **Punto 2 (Versión pública de la investigación):**
   - Instructivo 2026: «A partir de la 'Hoja de Resumen' (se incluye la Hoja de Resumen)».
     - Página de inicio: Página 2 del PDF.
     - Total de páginas: **193 páginas** (194 - 2 + 1).
   - *Nota de discrepancia histórica:* Si la ventanilla de CATT exigiera el criterio del PDF escaneado («a partir de la Advertencia, incluida»), la página de inicio sería la página 4, con **191 páginas** (194 - 4 + 1).
2. **Punto 4 (Documentos de soporte):**
   - Instructivo: «A partir de la 'Carta De Autorización De Difusión En El Repositorio Institucional De Tesis'».
     - Página de inicio: Página 5 del PDF.
     - Total de páginas: **190 páginas** (194 - 5 + 1).

*(Nota: Al integrar los escaneos definitivos con firmas autógrafas en PDF, si las cartas físicas ocupan más de una página por documento, el conteo total aumentará en la misma proporción).*

### 4.7 Discrepancias internas en los documentos de la CATT
Se identificaron 4 contradicciones entre las directrices provistas por la propia CATT:
1. **Titular de la Secretaría Ejecutiva:** En `Formato Reporte Tecnico TT25.pdf` (p. 3) figura `M. EN AN. MARÍA MAGDALENA SALDÍVAR ALMOREJO`, mientras que en la plantilla oficial vigente `Carta Responsiva TT 2026.docx` se nombra a `LIC. MILDRED SANDOVAL GARCÍA`.
2. **Ortografía del Presidente de la CATT:** En el formato escaneado aparece como `M. EN C. IVÁN GIOVANNI MOSSO GARCÍA` (con «I»), mientras que en la plantilla de 2026 figura `M. EN C. IVÁN GIOVANNY MOSSO GARCÍA` (con «Y»).
3. **Punto de partida del conteo de páginas en la Carta de Difusión:** `Disk Content Specifications 2026.docx` indica contar a partir de la «Hoja de Resumen», mientras que `Formato Reporte Tecnico TT25.pdf` indica contar a partir de la «Advertencia».
4. **Formato de nombres de los participantes:** La Portada y la Hoja de Resumen exigen «nombre seguido del apellido», mientras que la Carta Responsiva y la Autorización de Difusión instruyen llenar «iniciando por Apellido Paterno, Materno y Nombre(s)».

---

## 5. Lista de hallazgos

### A6-01 · MEDIA · Estructura y secciones obligatorias CATT
- Ubicación: `Docs/capitulos/1_Panorama_General/1.0_introduccion.tex:6`
- Texto: «\section{Panorama General}»
- Problema: La CATT establece en su guía oficial de formato (`Formato Reporte Tecnico TT25.pdf`, pág. 9) que la primera división principal del trabajo debe denominarse «INTRODUCCIÓN», mientras que el reporte técnico titula el capítulo 1 como «Panorama General» y restringe la introducción a la subsección 1.1.
- Evidencia: `Other/ESCOM/Formato Reporte Tecnico TT25.pdf`, pág. 9 (esquema del índice: «INTRODUCCIÓN (número de página) CAPÍTULO 1...»); `Technical_Report.pdf`, pág. 6.
- Propuesta: Renombrar el capítulo 1 a `\section{Introducción: Panorama General}` o `\section{Introducción}` para que el sinodal y la CATT identifiquen inequívocamente la sección obligatoria en el índice.

### A6-02 · ALTA · Marcadores de navegación y jerarquía PDF
- Ubicación: `Docs/Technical_Report.tex:389`
- Texto: «\pdfbookmark[0]{Índice}{indice}»
- Problema: Al asignar nivel 0 (`[0]`) al marcador del índice, todas las divisiones `\section` posteriores (que en la clase `article` se traducen en nivel 1 de bookmarks) quedan anidadas como hijas de «Índice» en la jerarquía del PDF, ocultando todos los capítulos y anexos del documento principal al contraer el árbol.
- Evidencia: Salida de inspección del árbol de marcadores con PyMuPDF (`fitz.open().get_toc()`), donde `Índice` tiene nivel 1 y los capítulos 1 al 8 y anexos tienen nivel 2 dependientes de él.
- Propuesta: Insertar `\bookmarksetup{startatroot}` en la línea 416 de `Docs/Technical_Report.tex` inmediatamente antes del capítulo 1, o cambiar los marcadores preliminares a nivel 1 (`\pdfbookmark[1]{...}`).

### A6-03 · ALTA · Duplicación en Tabla de Contenidos y Marcadores
- Ubicación: `Docs/capitulos/6_Resultados/6.0_introduccion.tex:7-8`
- Texto: «\section{Resultados}
\addcontentsline{toc}{section}{Resultados}»
- Problema: La instrucción `\section{Resultados}` ya ingresa de forma nativa la sección en la tabla de contenidos y genera su marcador; la línea consecutiva `\addcontentsline` produce una segunda entrada redundante en el índice impreso y en los marcadores del PDF.
- Evidencia: `Technical_Report.pdf`, pág. 8 (la tabla de contenidos impresa imprime consecutivamente «6. Resultados» y «Resultados» para la página 108); árbol de marcadores del PDF con doble nodo en pág. 108.
- Propuesta: Eliminar la línea 8 (`\addcontentsline{toc}{section}{Resultados}`) de `Docs/capitulos/6_Resultados/6.0_introduccion.tex`.

### A6-04 · ALTA · Duplicación en Tabla de Contenidos y Marcadores
- Ubicación: `Docs/capitulos/7_Conclusiones/7.0_introduccion.tex:8-9`
- Texto: «\section{Conclusiones}
\addcontentsline{toc}{section}{Conclusiones}»
- Problema: La orden `\addcontentsline{toc}{section}{Conclusiones}` genera una duplicación visual en el índice impreso y crea dos marcadores idénticos de navegación hacia la misma página.
- Evidencia: `Technical_Report.pdf`, pág. 9 (la tabla de contenidos lista consecutivamente «7. Conclusiones» y «Conclusiones» en la pág. 145); catálogo de marcadores del PDF con dos entradas en pág. 145.
- Propuesta: Eliminar la línea 9 (`\addcontentsline{toc}{section}{Conclusiones}`) de `Docs/capitulos/7_Conclusiones/7.0_introduccion.tex`.

### A6-05 · ALTA · Duplicación en Tabla de Contenidos y Marcadores
- Ubicación: `Docs/capitulos/8_Trabajo_Futuro/8.0_introduccion.tex:9-10`
- Texto: «\section{Trabajo a Futuro}
\addcontentsline{toc}{section}{Trabajo a Futuro}»
- Problema: La inclusión redundante de `\addcontentsline{toc}{section}{Trabajo a Futuro}` provoca una doble entrada consecutiva en el índice de contenidos y en el árbol de marcadores del PDF.
- Evidencia: `Technical_Report.pdf`, pág. 9 (la tabla de contenidos lista consecutivamente «8. Trabajo a Futuro» y «Trabajo a Futuro» en la pág. 151); catálogo de marcadores del PDF con dos entradas en pág. 151.
- Propuesta: Eliminar la línea 10 (`\addcontentsline{toc}{section}{Trabajo a Futuro}`) de `Docs/capitulos/8_Trabajo_Futuro/8.0_introduccion.tex`.

### A6-06 · ALTA · Formato y Márgenes
- Ubicación: `Docs/capitulos/A_Anexos/A.3.2_figuras_eda.tex:63-68`
- Texto: «\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.7\textwidth]{Figures/D4_sample_gallery.png}
  \caption{Galería de casos representativos: mamografía completa, máscara ROI e imagen recortada, para masas y calcificaciones benignas y malignas.}
  \label{fig:sample_gallery}
\end{figure}»
- Problema: La imagen `D4_sample_gallery.png` tiene una proporción vertical extrema (1189×2833 px); al escalarse por ancho (`width=0.7\textwidth`), su altura excede la página en 145.1 pt, invadiendo el margen inferior, proyectándose 49 pt fuera de la hoja física y eliminando por completo la leyenda (`\caption`) del PDF compilado.
- Evidencia: `Technical_Report.log` línea 2744 (`LaTeX Warning: Float too large for page by 145.11188pt on input line 68`); inspección con PyMuPDF en pág. 189 del PDF donde la imagen llega a `y1 = 841.0 pt` (límite del papel 792 pt) y la leyenda no existe en el texto extraído.
- Propuesta: Acotar la escala por altura con `\includegraphics[width=0.7\textwidth, height=0.75\textheight, keepaspectratio]{Figures/D4_sample_gallery.png}`.

### A6-07 · MEDIA · Formato y Márgenes
- Ubicación: `Docs/Technical_Report.tex:175`
- Texto: «  numbers=left, numberstyle=\tiny\color{gray}, numbersep=6pt,»
- Problema: La configuración de los listados de código en el Anexo A omite la sangría izquierda (`xleftmargin`), provocando que los números de línea se sitúen entre `x = 73.1 pt` y `76.1 pt`, invadiendo en 9 a 12 pt el margen izquierdo reglamentario de 3 cm (85.04 pt).
- Evidencia: Inspección de bloques de texto con PyMuPDF en páginas 163 a 171 de `Technical_Report.pdf`, donde la numeración de líneas se posiciona a la izquierda del límite reglamentario de 3 cm.
- Propuesta: Incorporar `xleftmargin=1.5em` y `framexleftmargin=1.5em` en la definición de `tt` dentro de `Docs/Technical_Report.tex:169-193`.

### A6-08 · MEDIA · Formato y Márgenes
- Ubicación: `Docs/capitulos/A_Anexos/A.1_codigo.tex:113`
- Texto: «\subsection{Centrado matricial y alineamiento kernel-objetivo con prueba de permutación (\texttt{Code/6\_Separability.ipynb}, módulo 6)}»
- Problema: Los títulos de las subsecciones de listados contienen rutas de archivo extensas en `\texttt{...}` sin puntos de corte tipográfico, ocasionando cajas desbordadas masivas (Overfull `\hbox`) de hasta 134.6 pt que rebasan ampliamente el margen derecho.
- Evidencia: `Technical_Report.log` líneas 1349 a 1404 (avisos de `Overfull \hbox` de 35.3 pt, 54.1 pt, 69.7 pt, 82.9 pt, 83.9 pt, 95.1 pt, 105.2 pt, 112.4 pt y 134.6 pt en las líneas de listados).
- Propuesta: Utilizar el argumento opcional de título corto para `\subsection[título breve]{título largo}` y separar la ruta del notebook en una línea secundaria o emplear `\path{...}` / `\allowbreak`.

### A6-09 · MEDIA · Discrepancias institucionales en datos de la CATT
- Ubicación: `Other/ESCOM/Carta Responsiva TT 2026.docx` frente a `Other/ESCOM/Formato Reporte Tecnico TT25.pdf:3, 7` y `Other/ESCOM/Disk Content Specifications 2026.docx:5`
- Texto: «EN ATENCIÓN A: 
LIC. MILDRED SANDOVAL GARCÍA
SECRETARIA EJECUTIVA» frente a «EN ATENCION A:
M. EN AN. MARIA MAGDALENA SALDIVAR ALMOREJO
SECRETARIA EJECUTIVA»
- Problema: Existen inconsistencias entre los documentos oficiales emitidos por la CATT respecto al nombre de la Secretaria Ejecutiva, la grafía del Presidente de la CATT (Giovanny vs. Giovanni) y la página de inicio para el cómputo de hojas de la Carta de Autorización de Difusión (desde Hoja de Resumen vs. desde Advertencia).
- Evidencia: Texto extraído de `Other/ESCOM/Carta Responsiva TT 2026.docx` vs. OCR de `Other/ESCOM/Formato Reporte Tecnico TT25.pdf` (páginas 3 y 7).
- Propuesta: Utilizar la plantilla vigente 2026 para la Carta Responsiva (con Lic. Mildred Sandoval García) y asentar 193 páginas en la Sección II de la Carta de Difusión, declarando ambas cifras en caso de aclaración en ventanilla.

### A6-10 · BAJA · Formato y Márgenes
- Ubicación: `Docs/tablas/anexo_e_decisiones.tex:2`
- Texto: «\begin{longtable}{@{}llp{9.4cm}p{2.3cm}@{}}»
- Problema: El ancho total configurado de las columnas excede en ~8.5 pt el ancho útil de la página (16.59 cm), produciendo cajas desbordadas hacia el margen derecho en las páginas 192, 193 y 194 del reporte.
- Evidencia: `Technical_Report.log` líneas 2813-2880 (`Overfull \hbox (8.5369pt too wide) in alignment`); páginas 192 a 194 de `Technical_Report.pdf` donde el texto alcanza `x1 = 563.8 pt` (margen derecho reglamentario fija `x = 555.3 pt`).
- Propuesta: Reducir la columna descriptiva a `p{8.6cm}` en `Docs/tablas/anexo_e_decisiones.tex:2`.

### A6-11 · BAJA · Formato y Márgenes
- Ubicación: `Docs/capitulos/3_Marco_Teorico/3.2.4_paulifeaturemap.tex:28-29`
- Texto: «En el presente trabajo, la condición experimental C5 se define formalmente como
\texttt{pauli\_feature\_map(paulis=['Y', 'ZZ'], reps=1)}, manteniendo el mismo número»
- Problema: Cadenas inline de código monospace sin guionado causan desbordamientos menores hacia el margen derecho de 14 pt a 48 pt en varias secciones del cuerpo del marco teórico y resultados.
- Evidencia: `Technical_Report.log` líneas 1513, 1530, 1554, 1561, 1656, 1673, 2168 (avisos de `Overfull \hbox` en párrafos que contienen `pauli_feature_map`, `real_amplitudes`, `SecondaryCapture` y `IRREGULAR/SPICULATED`).
- Propuesta: Añadir `\allowbreak` dentro de las llamadas de función monospace extensas o reordenar ligeramente la redacción del renglón para facilitar el salto de línea.

### A6-12 · BAJA · Nomenclatura CATT
- Ubicación: `Docs/Technical_Report.tex:536` y `Docs/capitulos/A_Anexos/A.0_introduccion.tex:2`
- Texto: «% ===== A_Anexos» y «% ANEXOS DEL REPORTE TÉCNICO»
- Problema: La CATT establece en su esquema de índice la etiqueta «APÉNDICES» (ej. «APÉNDICE A...»), mientras que el reporte utiliza la denominación «Anexos» (Anexo A a Anexo E).
- Evidencia: `Other/ESCOM/Formato Reporte Tecnico TT25.pdf`, pág. 9 («APÉNDICE A... (número de página)»); `Technical_Report.pdf`, pág. 10 y pág. 163.
- Propuesta: Consultar con los directores si se prefiere ajustar los encabezados a «Apéndice A», «Apéndice B», etc., para ceñirse a la literalidad de la plantilla de la CATT.

### A6-13 · BAJA · Contenido de Secciones
- Ubicación: `Docs/capitulos/G_Glosario/glosario.tex:6-8`
- Texto: «\begin{description}
  \item[Pendiente.] El glosario se completa a partir de los términos definidos en los capítulos 3 y 5.
\end{description}»
- Problema: La sección obligatoria «Glosario» se encuentra formalmente integrada en la estructura y en el índice, pero su contenido actual es un texto provisional en borrador.
- Evidencia: `Docs/capitulos/G_Glosario/glosario.tex:7`; `Technical_Report.pdf`, pág. 162.
- Propuesta: Redactar las definiciones completas de términos del glosario conforme a lo previsto en la tarea G1 de la auditoría.

---

## 6. Conteo de hallazgos por severidad

- **Severidad ALTA:** 5 hallazgos (A6-02, A6-03, A6-04, A6-05, A6-06).
- **Severidad MEDIA:** 4 hallazgos (A6-01, A6-07, A6-08, A6-09).
- **Severidad BAJA:** 4 hallazgos (A6-10, A6-11, A6-12, A6-13).
- **Total:** 13 hallazgos documentados.

---

## 7. Confirmación de estado de repositorio

Verificación mediante `git -C /Users/alexander_san/TT status --short`:
- No se realizaron modificaciones en archivos ajenos (`.tex`, `.py`, `.ipynb`, `.csv`).
- Único archivo generado por esta tarea: `Docs/insumos/auditoria/informe_A6.md`.
- No se ejecutaron comandos `git commit`, `git add` ni alteraciones en el árbol de trabajo.
