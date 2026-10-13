# Auditoría de Compilación Fuera de macOS: Reporte Técnico TT 2026-B039

**Documento evaluado:** `Docs/Technical_Report.tex` (solo lectura)  
**Fecha de evaluación:** 13 de octubre de 2026  
**Entorno de prueba:** Sistema de archivos APFS que distingue mayúsculas (*Case-sensitive APFS* montado en `/Volumes/TTcs`) vs. sistema de archivos insensible (*Case-insensitive* montado en `/tmp/tt_ci`), contrastando el comportamiento con motores de compilación estrictos (Linux, Overleaf, contenedores Docker con `texmf_casefold_search=0`).  
**Archivo de respaldo:** `Docs/insumos/compilacion_fuera_macos_extractos.log`

---

## 1. Resumen Ejecutivo

El reporte técnico del Trabajo Terminal 2026-B039 compila sin errores fatales en el entorno predeterminado de macOS gracias a que el sistema de archivos del sistema anfitrión no distingue mayúsculas y minúsculas y a que la biblioteca `kpathsea` de MacTeX tiene habilitada la búsqueda *casefold* (`texmf_casefold_search = 1`).

Sin embargo, al trasladar el proyecto a un sistema de archivos que **distingue mayúsculas y minúsculas** (como Linux nativo, servidores de Integración Continua, o la plataforma **Overleaf** cuando opera en modo estricto):
1. **Fallo crítico en inclusión de imágenes (2 errores):** La segunda portada institucional (página 2 del PDF) hace referencia a `Logos/ipn_logo.png` (línea 256) y `Logos/escom_logo.png` (línea 265). Los nombres reales en disco bajo `Docs/Logos/` son `IPN_logo.png` y `ESCOM_logo.png`. En un entorno estricto, el compilador genera sendos errores `Package pdftex.def Error: File ... not found`, degrada la salida a modo *draft* (cajas vacías con la ruta impresa en lugar del gráfico) y finaliza con código de salida `1` (fallo de compilación).
2. **Problemas transversales (presentes en cualquier plataforma):**
   - **Referencia indefinida y «??» en PDF (1 caso):** En la línea 2884 se cita `sección~\ref{sec:metricas}`, pero la etiqueta `\label{sec:metricas}` no existe en el documento. Esto provoca que en la página 56 del PDF se imprima literalmente: `sección ??`.
   - **Etiqueta duplicada (*multiply-defined*, 1 caso):** La etiqueta `\label{eq:embedding_vector}` está declarada dos veces: en la línea 1174 (Sección 4, Marco Teórico) y en la línea 1452 (Sección 5, Metodología).
   - **Float demasiado grande (*Float too large*, 1 caso):** La tabla comparativa de estado del arte en orientación apaisada (`landscape`) en la línea 973 excede la altura útil de la página por `33.23714pt`.
   - **Desbordamientos de caja (*Overfull \hbox*, 12 casos):** Elementos que rebasan el margen horizontal del texto por anchos entre 2.63 pt y 52.18 pt (destacando la tabla de estado del arte y el diagrama TikZ del pipeline).
   - **Espaciados insuficientes (*Underfull \hbox*, 25 casos):** 20 casos dentro de las columnas estrechas de la tabla comparativa de estado del arte (línea 964) y 5 casos en entradas bibliográficas con hipervínculos URL largos.

---

## 2. Metodología Experimental y Entorno de Reproducción

Para evaluar con fidelidad matemática el comportamiento en entornos fuera de macOS se ejecutaron las siguientes pruebas controladas:
1. **Volumen insensible a mayúsculas (`/tmp/tt_ci`):** Réplica de la carpeta `Docs/` en el sistema de archivos nativo de macOS.
2. **Volumen sensible a mayúsculas (`/Volumes/TTcs`):** Imagen de disco APFS de 2 GB creada con el comando `hdiutil create -size 2g -fs "Case-sensitive APFS" -volname TTcs -type SPARSE /tmp/tt_cs.sparseimage` y montada en `/Volumes/TTcs`.
3. **Compilación estándar vs. estricta:**
   - La ejecución de `latexmk -pdf -interaction=nonstopmode -file-line-error Technical_Report.tex` detectó que los binarios auxiliares ya existían en la copia del repositorio, deteniéndose de forma limpia. Siguiendo el protocolo, se realizaron dos pasadas de `pdflatex -interaction=nonstopmode -file-line-error Technical_Report.tex`.
   - Se evaluó el comportamiento bajo dos modalidades:
     - **Modo MacTeX estándar (`texmf_casefold_search=1`):** `kpathsea` intercepta los fallos de `ENOENT` del sistema de archivos y realiza un escaneo de directorios en espacio de usuario para resolver mayúsculas/minúsculas.
     - **Modo Fuera de macOS / Estricto (`texmf_casefold_search=0`):** Se desactiva la resolución en espacio de usuario, emulando con exactitud un contenedor Linux, Overleaf o un compilador TeX estricto donde el sistema operativo niega el acceso al archivo con discrepancia de capitalización.

---

## 3. Tabla Exhaustiva de Problemas Detectados

Cada fila contiene el texto exacto citado literalmente del archivo de registro (`.log`), su causa técnica y el arreglo propuesto sin alterar el repositorio. Cada aviso cuenta con su correspondiente respaldo íntegro en `Docs/insumos/compilacion_fuera_macos_extractos.log`.

| ID | Tipo de Problema | Línea(s) en `Technical_Report.tex` | Texto Exacto del Aviso en el Log (Literal) | Causa Técnica | Arreglo Propuesto (Sin Aplicar) |
|---|---|---|---|---|---|
| P01 | Archivo no encontrado (sensibilidad a mayúsculas) | 256 | `LaTeX Warning: File \`Logos/ipn_logo.png' not found on input line 256.` | En la línea 256 se pide `Logos/ipn_logo.png` con minúsculas `ipn`, pero el archivo en `Docs/Logos/` se llama `IPN_logo.png`. En sistemas sensibles a mayúsculas el archivo no se localiza. | Cambiar en la línea 256: `\includegraphics[height=2.5cm]{Logos/ipn_logo.png}` por `\includegraphics[height=2.5cm]{Logos/IPN_logo.png}`. |
| P02 | Error de paquete (`pdftex.def`) | 256 | `./Technical_Report.tex:256: Package pdftex.def Error: File \`Logos/ipn_logo.png' not found: using draft setting.` | Al no encontrarse el archivo gráfico, el controlador `pdftex.def` dispara un error y activa el modo *draft*, reemplazando la imagen con un marco vacío con el texto de la ruta. | Se resuelve al corregir la capitalización a `Logos/IPN_logo.png`. |
| P03 | Archivo no encontrado (sensibilidad a mayúsculas) | 265 | `LaTeX Warning: File \`Logos/escom_logo.png' not found on input line 265.` | En la línea 265 se pide `Logos/escom_logo.png` con minúsculas `escom`, pero el archivo en `Docs/Logos/` se llama `ESCOM_logo.png`. | Cambiar en la línea 265: `\includegraphics[height=2.2cm]{Logos/escom_logo.png}` por `\includegraphics[height=2.2cm]{Logos/ESCOM_logo.png}`. |
| P04 | Error de paquete (`pdftex.def`) | 265 | `./Technical_Report.tex:265: Package pdftex.def Error: File \`Logos/escom_logo.pn g' not found: using draft setting.` | Controlador `pdftex.def` entra en modo *draft* para el logo de la ESCOM, rompiendo la composición de la segunda portada. | Se resuelve al corregir la capitalización a `Logos/ESCOM_logo.png`. |
| P05 | Referencia indefinida («??» en PDF) | 2884 | `LaTeX Warning: Reference \`sec:metricas' on page 56 undefined on input line 2884 .` | En el texto de la pág. 56 se incluye `sección~\ref{sec:metricas}`, pero ninguna sección del documento declara `\label{sec:metricas}`. En el PDF se imprime `sección ??`. | Agregar `\label{sec:metricas}` inmediatamente después de la línea 1710 (`\subsection{Métricas de separabilidad y evaluación}`). |
| P06 | Resumen global: referencias indefinidas | Final del log | `LaTeX Warning: There were undefined references.` | Aviso global de cierre emitido por LaTeX al detectar una o más referencias cruzadas sin resolver en la pasada actual. | Se resuelve al definir `\label{sec:metricas}`. |
| P07 | Etiqueta duplicada (*multiply defined*) | 1174 y 1452 | `LaTeX Warning: Label \`eq:embedding_vector' multiply defined.` | La etiqueta `\label{eq:embedding_vector}` está asignada tanto a la ecuación del embedding en la Sección 4 (l. 1174) como en la Sección 5 (l. 1452). | Renombrar la segunda ocurrencia en la línea 1452 a `\label{eq:embedding_vector_metodologia}` o similar. |
| P08 | Resumen global: etiquetas duplicadas | Final del log | `LaTeX Warning: There were multiply-defined labels.` | Aviso global de cierre emitido por LaTeX al existir colisiones de claves en el archivo auxiliar `.aux`. | Se resuelve al desambiguar la etiqueta duplicada `eq:embedding_vector`. |
| P09 | Float demasiado grande (*Float too large*) | 973 | `LaTeX Warning: Float too large for page by 33.23714pt on input line 973.` | La tabla apaisada `tab:estado_arte_comparativo` excede la altura útil de la página por `33.23714pt` (~1.17 cm) debido al espaciado de filas y notas al pie. | Reducir el interlineado o espaciado vertical de la tabla (ajustar `\renewcommand{\arraystretch}{...}` a un valor menor, p.ej. 0.95, o reducir el tamaño de letra del cuerpo a `\footnotesize`). |
| P10 | Overfull \hbox (10.68 pt) | 255--267 | `Overfull \hbox (10.67986pt too wide) in paragraph at lines 255--267` | La tabla con encabezado de la segunda portada excede el ancho de línea por 10.68 pt al sumar el ancho de las tres columnas (logos y minipage central de 11 cm). | Reducir el ancho de la `minipage` central de 11 cm a 10.4 cm o reducir el ancho asignado a las columnas laterales. |
| P11 | Overfull \hbox (3.99 pt) | 779--780 | `Overfull \hbox (3.99277pt too wide) in paragraph at lines 779--780` | La línea que describe `PauliFeatureMap` y su expresión matemática en línea excede el margen derecho en 3.99 pt por falta de punto de partición silábica. | Reformular ligeramente la frase o introducir un corte opcional de guion (`\-`) en las palabras compuestas. |
| P12 | Overfull \hbox (4.23 pt) | 964 | `Overfull \hbox (4.23474pt too wide) in paragraph at lines 964--964` | La palabra `ZZFeatureMap` en una celda de la tabla de estado del arte excede el ancho de la columna por 4.23 pt. | Permitir partición silábica o reducir tamaño de fuente de la celda a `\scriptsize`. |
| P13 | Overfull \hbox (13.86 pt) | 964 | `Overfull \hbox (13.85966pt too wide) in paragraph at lines 964--964` | La palabra `PauliFeatureMap` en una celda de la tabla de estado del arte excede el ancho de columna por 13.86 pt. | Permitir partición de la cadena `PauliFeatureMap` o ajustar los anchos de columna en el entorno `tabularx`. |
| P14 | Overfull \hbox (52.18 pt) | 964 | `Overfull \hbox (52.18251pt too wide) in alignment at lines 964--964` | La estructura tabular completa de la tabla de estado del arte desborda el margen derecho horizontal por 52.18 pt (~1.83 cm). | Revisar el ancho total asignado a las especificaciones de columnas de `tabularx` para asegurar que sumen exactamente `\linewidth`. |
| P15 | Overfull \hbox (18.68 pt) | 1106--1110 | `Overfull \hbox (18.68253pt too wide) in paragraph at lines 1106--1110` | Fórmulas y notación bra-ket en texto plano que desbordan el margen por falta de quiebre. | Mover la notación de base computacional extendida a una ecuación desplegada (`equation` o `align*`). |
| P16 | Overfull \hbox (17.15 pt) | 1622--1631 | `Overfull \hbox (17.14537pt too wide) in paragraph at lines 1622--1631` | El identificador monoespaciado `\texttt{TorchConnector}` no puede dividirse y empuja el final de línea 17.15 pt más allá del margen. | Permitir quiebre silábico con `\texttt{Torch\-Connector}` o reformular el párrafo para adelantar la palabra. |
| P17 | Overfull \hbox (33.43 pt) | 2216--2217 | `Overfull \hbox (33.4336pt too wide) in paragraph at lines 2216--2217` | El lienzo del diagrama de arquitectura `tikzpicture` del pipeline excede el ancho de texto por 33.43 pt (~1.18 cm). | Envolver el entorno `tikzpicture` en `\resizebox{\textwidth}{!}{...}` o reducir la escala (`[scale=0.9, every node/.style={transform shape}]`). |
| P18 | Overfull \hbox (2.63 pt) | 2601--2614 | `Overfull \hbox (2.62917pt too wide) in paragraph at lines 2601--2614` | Nombres de archivos CSV con formato `\texttt{mass_case_description_train_set}` provocan un leve desbordamiento de 2.63 pt. | Reestructurar la frase o permitir quiebre tras los guiones bajos. |
| P19 | Overfull \hbox (5.59 pt) | 2971--2981 | `Overfull \hbox (5.58589pt too wide) in paragraph at lines 2971--2981` | Línea con múltiples palabras en monoespaciado (`pathology`, `BENIGN`, `MALIGNANT`) y conteos numéricos desborda 5.59 pt. | Ajustar la redacción o permitir guionado manual. |
| P20 | Overfull \hbox (13.83 pt) | 3282--3292 | `Overfull \hbox (13.8299pt too wide) in paragraph at lines 3282--3292` | Identificador DICOM `\texttt{SOPClassUID}` al final de línea desborda 13.83 pt. | Reordenar la frase para que el identificador quede en una posición intermedia o permitir salto. |
| P21 | Overfull \hbox (2.94 pt) | 3433--3441 | `Overfull \hbox (2.93655pt too wide) in paragraph at lines 3433--3441` | Título en negrita y expresión matemática en línea desbordan el margen por 2.94 pt. | Ajustar el espaciado o la redacción del encabezado del punto. |
| P22 | Underfull \hbox (badness 10000, x20) | 964 | `Underfull \hbox (badness 10000) in paragraph at lines 964--964` | Columnas extremadamente angostas en la tabla apaisada fuerzan a TeX a estirar los espacios interpalabra al máximo permitido. | Justificar a la izquierda con `\raggedright` o `\RaggedRight` en las celdas de texto de la tabla. |
| P23 | Underfull \hbox (badness 1609) | 3617--3619 | `Underfull \hbox (badness 1609) in paragraph at lines 3617--3619` | Entrada bibliográfica con URL larga (`https://www.stopbreastcancer.org/`) genera salto de línea prematuro. | Cargar el paquete `xurl` o definir reglas de quiebre de URLs en `hyperref`. |
| P24 | Underfull \hbox (badness 10000, x2) | 3647--3649 | `Underfull \hbox (badness 10000) in paragraph at lines 3647--3649` | Entrada bibliográfica con URL larga (`https://windsongwny.com/breast-health/`) fuerza dos líneas con mala densidad tipográfica. | Permitir quiebre en cualquier carácter de la URL mediante `xurl`. |
| P25 | Underfull \hbox (badness 5217) | 3797--3799 | `Underfull \hbox (badness 5217) in paragraph at lines 3797--3799` | Entrada bibliográfica de Goodfellow et al. (2016) con hipervínculo que parte la línea de forma antiestética. | Ajustar el comando de la URL o configurar `\sloppy` localmente en la bibliografía. |
| P26 | Underfull \hbox (badness 1127) | 3862--3865 | `Underfull \hbox (badness 1127) in paragraph at lines 3862--3865` | Entrada bibliográfica de IBM Quantum (2024) con URL larga que deja espacios excesivos. | Ajustar configuración de `url` / `hyperref`. |

---

## 4. Sección «Solo fuera de macOS»

### 4.1. Análisis del Comportamiento Diferencial

En sistemas operativos de la familia macOS, el sistema de archivos por defecto (APFS formateado como *Case-insensitive*) no distingue entre mayúsculas y minúsculas. Por lo tanto, una solicitud a nivel de sistema para abrir `Logos/ipn_logo.png` resuelve sin ninguna dificultad hacia el archivo físico `Docs/Logos/IPN_logo.png`. Adicionalmente, el paquete MacTeX distribuye su motor `kpathsea` con la directiva `texmf_casefold_search = 1` configurada de fábrica en `texmf.cnf`, lo que añade una capa de resolución tolerante en espacio de usuario.

Por el contrario, **fuera de macOS** (en entornos de producción académica como **Linux**, servidores de integración continua basados en Docker, o la plataforma **Overleaf** cuando opera en modo estricto):
1. **El sistema de archivos ext4, XFS o Btrfs es estrictamente sensible a mayúsculas y minúsculas (*case-sensitive*).**
2. **Las plataformas como Overleaf operan con restricciones de seguridad y entornos de compilación optimizados** donde no se permite el escaneo indiscriminado de directorios (*casefolding search*) debido al sobrecosto de Entrada/Salida en proyectos de gran envergadura.
3. Al solicitar un archivo con una grafía distinta de la física en disco, el kernel responde inmediatamente con el error `ENOENT` (*No such file or directory*).

### 4.2. Problemas que Ocurren Únicamente Fuera de macOS

Al reproducir la compilación en el volumen APFS sensible a mayúsculas (`/Volumes/TTcs`) bajo condiciones de búsqueda estricta (`texmf_casefold_search=0`), se manifiestan de inmediato los siguientes **problemas exclusivos**:

1. **Inclusión fallida de `ipn_logo.png` (Línea 256):**
   - **Solicitud en `.tex` (línea 256):** `\includegraphics[height=2.5cm]{Logos/ipn_logo.png}`
   - **Nombre real en disco (`Docs/Logos/`):** `IPN_logo.png`
   - **Discrepancia:** El prefijo institucional fue escrito en minúsculas (`ipn`) en lugar de mayúsculas (`IPN`). Curiosamente, en la primera portada del mismo reporte (línea 183), sí fue escrito correctamente como `Logos/IPN_logo.png`.
   - **Mensaje exacto del log:**
     ```
     LaTeX Warning: File `Logos/ipn_logo.png' not found on input line 256.

     ./Technical_Report.tex:256: Package pdftex.def Error: File `Logos/ipn_logo.png'
      not found: using draft setting.
     ```

2. **Inclusión fallida de `escom_logo.png` (Línea 265):**
   - **Solicitud en `.tex` (línea 265):** `\includegraphics[height=2.2cm]{Logos/escom_logo.png}`
   - **Nombre real en disco (`Docs/Logos/`):** `ESCOM_logo.png`
   - **Discrepancia:** El acrónimo de la escuela fue escrito en minúsculas (`escom`) en lugar de mayúsculas (`ESCOM`). En la primera portada (línea 229), el archivo se incluyó con su grafía correcta `Logos/ESCOM_logo.png`.
   - **Mensaje exacto del log:**
     ```
     LaTeX Warning: File `Logos/escom_logo.png' not found on input line 265.

     ./Technical_Report.tex:265: Package pdftex.def Error: File `Logos/escom_logo.pn
     g' not found: using draft setting.
     ```

### 4.3. Impacto Observable en el Documento Compilado (PDF)

El impacto directo en el documento resultante fuera de macOS es severo:
- **Página 2 (Segunda portada institucional):** El encabezado institucional pierde por completo los dos escudos gráficos. En lugar de los logotipos oficiales del IPN y de la ESCOM, el compilador dibuja **dos rectángulos vacíos en modo draft** con el texto literal de la ruta impreso en su interior (`Logos/ipn_logo.png` y `Logos/escom_logo.png`).
- **Estado de salida del proceso:** El compilador finaliza con **código de salida 1 (`EXIT_CODE: 1`)**, lo que en un flujo de integración continua (CI/CD) o en un proceso automatizado de validación de tesis marcaría la tarea como fallida (*Build Failed*).

### 4.4. Problemas que NO son Exclusivos de Fuera de macOS

Todos los demás problemas detectados en la auditoría (la referencia rota `sec:metricas`, la etiqueta duplicada `eq:embedding_vector`, el float desbordado de la línea 973, y la totalidad de los 12 Overfull \hbox y 25 Underfull \hbox) **se replican de forma idéntica en macOS y fuera de macOS**. Su origen no reside en el sistema de archivos ni en el sistema operativo anfitrión, sino en la codificación tipográfica y lógica del archivo fuente `Technical_Report.tex`.

---

## 5. Conteos Totales Comparativos

La siguiente tabla presenta el balance cuantitativo exhaustivo contrastando la compilación en un sistema sensible a mayúsculas fuera de macOS con la compilación en el entorno nativo de macOS:

| Métrica / Tipo de Evento | En Volumen Case-Sensitive Estricto (Linux / Overleaf / CI) | En Volumen Case-Insensitive (macOS Nativo) | Diferencia Exclusiva Fuera de macOS |
|---|:---:|:---:|:---:|
| **Código de salida del compilador (`pdflatex`)** | **`1` (Fallo)** | `0` (Éxito) | **`1`** |
| **Errores de paquete críticos (`Package Error`)** | **2** | 0 | **+2** |
| **Archivos no encontrados (`File ... not found`)** | **2** | 0 | **+2** |
| **Referencias indefinidas (`Reference ... undefined`)** | 1 (`sec:metricas`) | 1 (`sec:metricas`) | 0 |
| **Apariciones de «??» en el PDF generado** | 1 (Pág. 56) | 1 (Pág. 56) | 0 |
| **Etiquetas duplicadas (*multiply defined*)** | 1 (`eq:embedding_vector`) | 1 (`eq:embedding_vector`) | 0 |
| **Avisos globales de resumen (`Warnings` finales)** | 2 | 2 | 0 |
| **Avisos de Floats demasiado grandes (*Float too large*)** | 1 (Línea 973, +33.24 pt) | 1 (Línea 973, +33.24 pt) | 0 |
| **Avisos de Overfull \hbox** | 12 | 12 | 0 |
| **Avisos de Underfull \hbox** | 25 | 25 | 0 |
| **Avisos de Overfull \vbox** | 0 | 0 | 0 |
| **Avisos de Underfull \vbox** | 0 | 0 | 0 |
| **Total de páginas generadas en el PDF** | 77 | 77 | 0 |

### Desglose Detallado de Conteos
- **Archivos no encontrados (2):**
  1. `Logos/ipn_logo.png` (Línea 256) $\rightarrow$ Archivo real: `Docs/Logos/IPN_logo.png`
  2. `Logos/escom_logo.png` (Línea 265) $\rightarrow$ Archivo real: `Docs/Logos/ESCOM_logo.png`
- **Referencias indefinidas (1):**
  1. `sec:metricas` (Línea 2884, Pág. 56) $\rightarrow$ Genera «??» en el PDF en la frase: *"sección ??: KTA respecto al kernel..."*
- **Etiquetas duplicadas (1):**
  1. `eq:embedding_vector` $\rightarrow$ Definida simultáneamente en Línea 1174 y Línea 1452.
- **Floats desbordados (1):**
  1. Entorno de tabla apaisada en Línea 973 $\rightarrow$ Desborde de `33.23714pt`.
- **Overfull \hbox (12):**
  - Líneas 255--267: 10.68 pt (Tabla encabezado portada 2)
  - Líneas 779--780: 3.99 pt (Descripción PauliFeatureMap)
  - Línea 964: 4.23 pt (Celda ZZFeatureMap)
  - Línea 964: 13.86 pt (Celda PauliFeatureMap)
  - Línea 964: 52.18 pt (Estructura tabular de estado del arte)
  - Líneas 1106--1110: 18.68 pt (Fórmula de superposición de estados)
  - Líneas 1622--1631: 17.15 pt (Palabra monoespaciada TorchConnector)
  - Líneas 2216--2217: 33.43 pt (Lienzo TikZ del pipeline)
  - Líneas 2601--2614: 2.63 pt (Nombres de archivos CSV)
  - Líneas 2971--2981: 5.59 pt (Valores de etiquetas pathology)
  - Líneas 3282--3292: 13.83 pt (Identificador DICOM SOPClassUID)
  - Líneas 3433--3441: 2.94 pt (Dimensiones de mamografías)
- **Underfull \hbox (25):**
  - Línea 964: 20 avisos dentro de la tabla comparativa apaisada (columnas estrechas forzadas).
  - Líneas 3617--3619: 1 aviso en referencia Stop Breast Cancer (2025).
  - Líneas 3647--3649: 2 avisos en referencia Windsong Radiology (2026).
  - Líneas 3797--3799: 1 aviso en referencia Goodfellow et al. (2016).
  - Líneas 3862--3865: 1 aviso en referencia IBM Quantum (2024).
