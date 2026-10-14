# Capítulos de reemplazo del reporte técnico

Cada carpeta es un capítulo completo de `Docs/Technical_Report.tex`, en el orden del reporte, con **un archivo por subsección** (§4) o **por subsubsección** (§3). La cabecera de cada archivo dice qué líneas del `.tex` reemplaza (numeración al 2026-10-13) y qué decisiones de la bitácora lo respaldan. `Technical_Report.tex` no se tocó.

| Carpeta | Estado |
|---|---|
| `3_Marco_Teorico/` | Completo. Las subsubsecciones sin cambios son copia literal del `.tex`; las demás se reescribieron con el paquete del miércoles, ya corregido. |
| `4_Metodologia/` | Completo, con la numeración M1–M8 de D-030 y los paquetes del lunes y del martes. |
| `5_EDA/` | El texto de TT1 sin cambios, salvo cuatro correcciones: las 84 series recuperadas por la API REST y el 97.6 % inicial; sin recortes de 224×224; `Manufacturer`, `PixelSpacing` e `ImagerPixelSpacing` ausentes en las 3,103 mamografías, en lugar de «UNKNOWN», y sin la figura `D2_manufacturers.png`, que graficaba ese valor de relleno; sin «normalización de intensidades». |
| `6_Resultados/` | Capítulo nuevo, escrito a partir de las entradas H-020 a H-054 de la bitácora y de las tablas de `Docs/tablas/`. Cada párrafo con cifras lleva un `% fuente:` con las entradas y los CSV de donde salen. |

## Cómo usarlo

- **Para comprobar las cifras de §6:** `python Code/tools/verificar_cifras_capitulos.py Docs/capitulos/6_Resultados` busca cada número en las fuentes que declara su párrafo. Las cifras marcadas `EN_CSV(revisar)` coinciden con algún valor del CSV citado, pero la coincidencia podría ser casual; se revisaron a mano el 2026-10-13.

- **Para copiar una tabla o un párrafo:** abre el archivo de esa subsección y cópialo al `.tex`.
- **Para sustituir un capítulo entero:** borra en el `.tex` el rango de líneas que indican las cabeceras y pon `\input{capitulos/4_Metodologia/4.0_introduccion}` y los demás, en orden.
- **Para comprobar que compila** con el preámbulo y la bibliografía reales: `bash Docs/capitulos/compilar_prueba.sh`, o solo una carpeta, con `bash Docs/capitulos/compilar_prueba.sh 4_Metodologia`. El script no toca nada del repositorio: compila en un directorio temporal e informa de referencias sin resolver y de cajas desbordadas.

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
