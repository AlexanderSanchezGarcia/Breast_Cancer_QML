# Capítulos de reemplazo del reporte técnico

Cada carpeta es un capítulo completo de `Docs/Technical_Report.tex`, en el orden del reporte, con **un archivo por subsección** (§4) o **por subsubsección** (§3). La cabecera de cada archivo dice qué líneas del `.tex` reemplaza (numeración al 2026-10-13) y qué decisiones de la bitácora lo respaldan. `Technical_Report.tex` no se tocó.

| Carpeta | Estado |
|---|---|
| `3_Marco_Teorico/` | Completo. Las subsubsecciones sin cambios son copia literal del `.tex`; las demás se reescribieron con el paquete del miércoles, ya corregido. |
| `5_Metodologia/` | (Antes `4_Metodologia/`; capítulo 5 desde el 2026-10-14.) Completo, con la numeración M1–M8 de D-030 y los paquetes del lunes y del martes. |
| `4_EDA/` | (Antes `5_EDA/`; capítulo 4 desde el 2026-10-14, puente hacia la Metodología.) El texto de TT1 sin cambios, salvo cuatro correcciones: las 84 series recuperadas por la API REST y el 97.6 % inicial; sin recortes de 224×224; `Manufacturer`, `PixelSpacing` e `ImagerPixelSpacing` ausentes en las 3,103 mamografías, en lugar de «UNKNOWN», y sin la figura `D2_manufacturers.png`, que graficaba ese valor de relleno; sin «normalización de intensidades». |
| `2_Antecedentes/` | Reescrito el 2026-10-16. Orden: §2.1.1–§2.1.5 (corregidas con la auditoría y las fichas de T10), §2.1.6 límites de la ventaja, §2.1.7 imágenes cuánticas, §2.1.8 revisión crítica y §2.1.9 tabla comparativa (al final, con columnas P1–P4). Cada atribución lleva su `% respaldo:` verificable con `verificar_citas_fichas.py`; ya no hay copia literal de TT1, así que la prueba de literalidad se retiró. Queda un `% VERIFICAR` en §2.1.1: Zebari et al. es de acceso abierto, pero hay que descargarlo a mano (Taylor & Francis bloquea la descarga automática). |
| `A_Anexos/` | Nuevo (2026-10-14): anexos A–E; necesita `Docs/insumos/preambulo_extra.tex` (listings). |
| `6_Resultados/` | Capítulo nuevo, escrito a partir de las entradas H-020 a H-054 de la bitácora y de las tablas de `Docs/tablas/`. Cada párrafo con cifras lleva un `% fuente:` con las entradas y los CSV de donde salen. |

## Cómo usarlo

- **Para comprobar las cifras de §6:** `python Code/tools/verificar_cifras_capitulos.py Docs/capitulos/6_Resultados` busca cada número en las fuentes que declara su párrafo. Las cifras marcadas `EN_CSV(revisar)` coinciden con algún valor del CSV citado, pero la coincidencia podría ser casual; se revisaron a mano el 2026-10-13.

- **Para copiar una tabla o un párrafo:** abre el archivo de esa subsección y cópialo al `.tex`.
- **Para sustituir un capítulo entero:** borra en el `.tex` el rango de líneas que indican las cabeceras y pon `\input{capitulos/5_Metodologia/5.0_introduccion}` y los demás, en orden.
- **Para comprobar que compila** con el preámbulo y la bibliografía reales: `bash Docs/capitulos/compilar_prueba.sh`, o solo una carpeta, con `bash Docs/capitulos/compilar_prueba.sh 5_Metodologia`. El script no toca nada del repositorio: compila en un directorio temporal e informa de referencias sin resolver y de cajas desbordadas.

## Al integrarlo en el `.tex`

1. **Faltan dos `\bibitem` en el reporte:** `Cortes2012` y `Thanasilp2024`. Están verificados en `Docs/insumos/bibitems_nuevos.tex`. El script los añade solo para la prueba.
2. **Falta la cita de IBSI** en §4.4: queda un `% FALTA CITA IBSI` (Zwanenburg et al., 2020, *Radiology* 295(2), sin verificar todavía).
3. `\label{sec:metricas}` ya está en §3.4, así que desaparece el «sección ??» de la p. 56 del PDF de TT1.
4. Algunas etiquetas de §3 cambiaron: `eq:kta` pasa a `eq:kta_centered`, `eq:fisher_distance` a `eq:fisher_multivariate`, y el vector de §3.1.4 pasa a `eq:expZ_vector`. Comprobé que ninguna otra sección del `.tex` cita las etiquetas viejas.

## Decisiones de redacción que tomé y puedes cambiar

- **RNF-02:** opción (a), reformulado sin `config.yaml`.
- **RNF-03:** sin «estratificada por BI-RADS», que no está verificado, y con la partición real de 2,864 / 704.
- **RNF-08:** sin «PEP 8 con docstrings».
- **§3.2.3:** se conserva la ecuación con $-i$, que es la que implementa Qiskit, y una nota al pie explica la convención $+i$ de Havlíček et al.
- **§4.9:** dice «más de un orden de magnitud» de diferencia de escala entre representaciones: 0.90 frente a 0.056 de desviación típica media, unas 16 veces. D-036 dice «dos órdenes», que solo vale si se compara el rango $[0,\pi]$ con 0.05.

## Errores del material de partida que se corrigieron aquí

- **§3.2.7:** el paquete del miércoles daba «2,455 casos en masas y 1,113 en calcificaciones» y «117,000 ejecuciones». Son cifras inventadas. El texto usa las 2,864 lesiones de entrenamiento y los 5.16 s por lesión de `X8_costo_gradiente.csv`.
- **§3.4.8:** con el empate C1 = C2, *p* = 4/120, no 2/120.
- **§3.3.4:** la precisión de 0.015625 la pone `EstimatorQNN`. La de `StatevectorEstimator` por defecto es 0, comprobado en Qiskit 2.3.0.
- **§3.2.5:** la ecuación de `real_amplitudes` estaba en el orden equivocado.
- **§4.4 y D-009:** la caja más pequeña de masas mide **116×55**. «86×55» junta el alto mínimo de una lesión con el ancho mínimo de otra; es el mismo error que «3,801×2,873» en calcificaciones. D-009 ya está corregida.

## Correcciones a lo que entregó Gemini en §5 y §6 (2026-10-13)

- **§6.6:** puso los porcentajes de lectura nula del kernel con un decimal inventado («21.0 %»). Se sustituyeron por los del CSV: 21.5, 15.7, 74.5 y 71.6 %; 2.5, 1.5, 57.0 y 55.9 % con 8,192 disparos. El costo del *parameter-shift* se dejó en 205 h, la misma cifra que en §3.2.7.
- **§6.2:** las medianas a c = 0.02 venían de una prueba rápida con 60 masas. Ahora usan las 200 lesiones: 0.55 y 0.54 en masas, 0.59 y 0.58 en calcificaciones. La dimensión efectiva de C4 con k = 8 en masas es 139.6, no 140.0.
- **§6.4:** decía «auditoría independiente» a la vez que «la formuló el propio equipo»; se quitó «independiente».
- **§5:** se restauraron los anchos originales de tres figuras, entre ellas la galería D4, que con `\textwidth` desbordaba la página.
- **Tablas:** los pies de `Docs/tablas/*.tex` ya no muestran identificadores D-xxx ni H-xxx (`tablas_latex.py`).

## Pendiente cosmético

Hay cajas desbordadas en:
- §4.3, por los nombres de los CSV en `\texttt`; ya estaban en el PDF de TT1;
- §3.3.4, por las llamadas de Qiskit en `\texttt`;
- §3.2.3, en la ecuación con la nota al pie.

No afectan al contenido.

## Borradores por capítulo

Se dispone de una infraestructura de compilación independiente por capítulo y de un borrador completo con todos los capítulos existentes (`borrador_completo.pdf`), diseñada para permitir la revisión y edición aislada desde VSCode (con LaTeX Workshop) o terminal.

### Estructura de archivos generada

- `Docs/capitulos/borrador_completo.tex` y `borrador_completo.pdf`: documento maestro con índice de contenidos (`\tableofcontents`), numeración canónica de secciones y la bibliografía completa.
- `Docs/capitulos/<carpeta>/borrador_<carpeta>.tex` y `borrador_<carpeta>.pdf`: documento autónomo para cada capítulo con numeración de secciones idéntica a la del completo, su bibliografía específica (únicamente con las fuentes citadas) y resolución de referencias cruzadas a otros capítulos.
- `Docs/capitulos/comun/`: piezas compartidas regeneradas dinámicamente (`preambulo.tex`, `bibliografia_completa.tex` y `bibliografia_<carpeta>.tex`).
- `Docs/capitulos/_build/`: directorio donde se aíslan todos los archivos auxiliares de compilación (`.aux`, `.log`, `.fls`, `.fdb_latexmk`, `.toc`), manteniendo limpios los directorios de los capítulos.
- `Docs/capitulos/.latexmkrc` y `.latexmkrc` en cada capítulo: configuración de `latexmk` para direccionar auxiliares a `_build/`, resolver rutas de `Figures/`, `tablas/`, `codigo/` y `Logos/` vía `TEXINPUTS`, y depositar el PDF resultante directamente en la carpeta del capítulo.

### Instrucciones de uso

1. **Compilar todos los borradores (completo y capítulos):**
   ```bash
   bash Docs/capitulos/compilar_borradores.sh
   ```
2. **Compilar solo capítulos específicos:**
   ```bash
   bash Docs/capitulos/compilar_borradores.sh 5_Metodologia 6_Resultados
   ```
   *(El script compila previamente `borrador_completo.tex` para actualizar las referencias cruzadas y numeración).*
3. **Compilar un capítulo individual desde su carpeta (o VSCode con LaTeX Workshop):**
   ```bash
   cd Docs/capitulos/5_Metodologia && latexmk -pdf borrador_5_Metodologia.tex
   ```
   Los archivos auxiliares se almacenan automáticamente en `_build/5_Metodologia/` sin ensuciar la carpeta de trabajo.

### Características técnicas

- **Referencias cruzadas externas (`xr-hyper`):** Las referencias entre capítulos se resuelven mediante `_build/externo_<carpeta>.aux`, el cual filtra las etiquetas propias del capítulo para evitar avisos de etiquetas duplicadas (`multiply defined`).
- **Numeración sincronizada:** Cada borrador de capítulo ajusta el contador de `section` (`\setcounter{section}{N-1}`) de forma que la primera sección coincide con la numeración canónica del reporte completo.
- **Extensibilidad automática:** Cuando se incorporen nuevos capítulos (p. ej. `1_Panorama_General` o `7_Conclusiones`), `compilar_borradores.sh` los detecta en orden numérico natural, genera su `.latexmkrc` y borrador, y los inserta en la posición adecuada del borrador completo sin requerir modificaciones manuales.

