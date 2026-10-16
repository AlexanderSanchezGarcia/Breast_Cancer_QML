# Informe de Tarea T8 · Infraestructura de compilación por capítulo y borrador completo

- **Fecha:** 2026-10-15
- **Tarea:** T8 · Un borrador compilable por capítulo, más el completo
- **ID de tarea:** `task_3fbd1263aca1`
- **ID de despacho:** `ctx_9dbc26011df1`
- **Terminal:** `term_31526b69-3055-4fc2-b668-5b0d5950be4d`
- **Estado final:** Succeeded (Éxito completo, todos los criterios de aceptación verificados).

---

## 1. Resumen ejecutivo

Se construyó la infraestructura completa de compilación desacoplada para los capítulos del Trabajo Terminal (`Docs/capitulos/`), habilitando tanto la compilación individual por capítulo (`borrador_<carpeta>.pdf`) como el documento integral consolidado (`borrador_completo.pdf`). Se incorporaron como copia literal de TT1 las secciones faltantes de §2 en `2_Antecedentes/` (§2.0 a §2.1.5 y §2.1.6 previo a la tabla), verificadas al 100% línea por línea. Se logró cero referencias sin resolver, cero citas sin resolver y cero etiquetas duplicadas en todos los documentos generados, sincronizando de forma exacta la numeración canónica de secciones y apéndices.

---

## 2. Archivos creados y modificados

Bajo las restricciones de ownership y la desviación autorizada por el coordinador:

### Archivos creados
1. `Docs/capitulos/comun/preambulo.tex`: Preámbulo compartido extraído de `Technical_Report.tex`, con `xr-hyper` antes de `hyperref`, `\graphicspath{{../../}{../}{./}}` y `preambulo_extra.tex`.
2. `Docs/capitulos/comun/bibliografia_completa.tex`: Bibliografía unificada con deduplicación idéntica a `compilar_prueba.sh` (73 referencias).
3. `Docs/capitulos/comun/bibliografia_<carpeta>.tex`: 6 archivos bibliográficos independientes que contienen **únicamente** las claves citadas por cada capítulo.
4. `Docs/capitulos/comun/generar_piezas.py`: Script generador de preámbulo, bibliografías, borradores y wrappers `.latexmkrc`.
5. `Docs/capitulos/comun/generar_aux_externo.py`: Script extractor y filtrador de etiquetas externas para `xr-hyper`.
6. `Docs/capitulos/comun/verificar_literal_s2.py`: Validador de copia literal de §2 frente a `Technical_Report.tex`.
7. `Docs/capitulos/comun/analizar_logs.py`: Analizador de logs y PDFs que audita páginas, secciones, advertencias y cajas desbordadas.
8. `Docs/capitulos/compilar_borradores.sh`: Script maestro ejecutable de compilación.
9. `Docs/capitulos/.latexmkrc`: Configuración centralizada de `latexmk` (emulación de directorio auxiliar, redirección a `_build/`, `TEXINPUTS`).
10. `Docs/capitulos/<carpeta>/.latexmkrc`: Wrapper de una línea (`do '../.latexmkrc';`) por capítulo (desviación autorizada).
11. `Docs/capitulos/2_Antecedentes/`:
    - `2.0_introduccion.tex` (líneas 692–700 de `Technical_Report.tex`, con `\label{sec:antecedentes}`).
    - `2.1.1_ml_clasico.tex` (líneas 701–725).
    - `2.1.2_deep_learning.tex` (líneas 726–750).
    - `2.1.3_fundamentos_qml.tex` (líneas 751–798).
    - `2.1.4_hibridos_salud.tex` (líneas 799–814).
    - `2.1.5_cbis_ddsm.tex` (líneas 815–830).
12. `Docs/capitulos/borrador_completo.tex` y `borrador_completo.pdf`.
13. `Docs/capitulos/<carpeta>/borrador_<carpeta>.tex` y `borrador_<carpeta>.pdf` (en carpetas 2, 3, 4, 5, 6 y A).

### Archivos modificados
1. `Docs/capitulos/2_Antecedentes/2.1.6_tabla_ampliada.tex`: Se insertaron las líneas 831–838 previas a `\begin{landscape}` y se vinculó `\label{tab:estado_arte}` junto a `\label{tab:estado_arte_v2}`.
2. `Docs/capitulos/compilar_prueba.sh`: Se excluyó el patrón `borrador_*.tex` en el bucle de inclusión de archivos.
3. `Docs/capitulos/README.md`: Se agregó la sección «Borradores por capítulo» documentando uso, arquitectura y características técnicas sin alterar el contenido previo.

---

## 3. Salida final de `compilar_borradores.sh`

```
============================================================
1. Regenerando comun/, borradores y borrador_completo.tex...
============================================================
OK: Piezas compartidas y borradores generados para 6 capítulos.
============================================================
2. Compilando borrador_completo.tex...
============================================================
Rc files read:
  .latexmkrc
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: Nothing to do for 'borrador_completo.tex'.
Latexmk: All targets (borrador_completo.pdf) are up-to-date

============================================================
3. Generando archivos .aux filtrados para referencias cruzadas...
============================================================
OK: Archivos aux externos generados para 6 capítulos.
============================================================
4. Compilando borradores por capítulo: 2_Antecedentes
3_Marco_Teorico
4_EDA
5_Metodologia
6_Resultados
A_Anexos
============================================================
--- Compilando 2_Antecedentes/borrador_2_Antecedentes.tex ---
Rc files read:
  .latexmkrc
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: Nothing to do for 'borrador_2_Antecedentes.tex'.
Latexmk: All targets (borrador_2_Antecedentes.pdf) are up-to-date

--- Compilando 3_Marco_Teorico/borrador_3_Marco_Teorico.tex ---
Rc files read:
  .latexmkrc
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: Nothing to do for 'borrador_3_Marco_Teorico.tex'.
Latexmk: All targets (borrador_3_Marco_Teorico.pdf) are up-to-date

--- Compilando 4_EDA/borrador_4_EDA.tex ---
Rc files read:
  .latexmkrc
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: Nothing to do for 'borrador_4_EDA.tex'.
Latexmk: All targets (borrador_4_EDA.pdf) are up-to-date

--- Compilando 5_Metodologia/borrador_5_Metodologia.tex ---
Rc files read:
  .latexmkrc
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: Nothing to do for 'borrador_5_Metodologia.tex'.
Latexmk: All targets (borrador_5_Metodologia.pdf) are up-to-date

--- Compilando 6_Resultados/borrador_6_Resultados.tex ---
Rc files read:
  .latexmkrc
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: Nothing to do for 'borrador_6_Resultados.tex'.
Latexmk: All targets (borrador_6_Resultados.pdf) are up-to-date

--- Compilando A_Anexos/borrador_A_Anexos.tex ---
Rc files read:
  .latexmkrc
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: Nothing to do for 'borrador_A_Anexos.tex'.
Latexmk: All targets (borrador_A_Anexos.pdf) are up-to-date

============================================================
5. Verificación de literalidad de §2...
============================================================
=================================================================
Verificación de literalidad de §2 (Technical_Report.tex vs 2_Antecedentes)
=================================================================
OK   2.0_introduccion.tex       (líneas 692–700,  9 líneas coincidentes)
OK   2.1.1_ml_clasico.tex       (líneas 701–725, 25 líneas coincidentes)
OK   2.1.2_deep_learning.tex    (líneas 726–750, 25 líneas coincidentes)
OK   2.1.3_fundamentos_qml.tex  (líneas 751–798, 48 líneas coincidentes)
OK   2.1.4_hibridos_salud.tex   (líneas 799–814, 16 líneas coincidentes)
OK   2.1.5_cbis_ddsm.tex        (líneas 815–830, 16 líneas coincidentes)
OK   2.1.6_tabla_ampliada.tex   (líneas 831–838 previas a landscape: coincidencia exacta)
-----------------------------------------------------------------
Resultado: ÉXITO COMPLETO — Todas las líneas coinciden literalmente.
============================================================
6. Resumen de compilación y aceptación de documentos...
============================================================
==================================================================================================================
RESUMEN DE COMPILACIÓN DE BORRADORES (Docs/capitulos/)
==================================================================================================================
| Documento                  |  Págs | 1ª Sección             | Refs sin resolver | Citas sin resolver | Etiquetas dup. | Overfull > 10pt |
|----------------------------|-------|------------------------|-------------------|--------------------|----------------|-----------------|
| borrador_completo          |   155 | 2. Antecedentes        |                 0 |                  0 |              0 |              15 |
| borrador_2_Antecedentes    |    23 | 2. Antecedentes        |                 0 |                  0 |              0 |               0 |
| borrador_3_Marco_Teorico   |    25 | 3. Marco Teórico       |                 0 |                  0 |              0 |               5 |
| borrador_4_EDA             |    10 | 4. Análisis Exploratori |                 0 |                  0 |              0 |               2 |
| borrador_5_Metodologia     |    22 | 5. Metodología         |                 0 |                  0 |              0 |               7 |
| borrador_6_Resultados      |    36 | 6. Resultados          |                 0 |                  0 |              0 |               1 |
| borrador_A_Anexos          |    32 | A. Código de los módulo |                 0 |                  0 |              0 |               0 |
|----------------------------|-------|------------------------|-------------------|--------------------|----------------|-----------------|

ESTADO: ACEPTACIÓN SATISFECHA (Cero referencias sin resolver, cero citas sin resolver, cero etiquetas duplicadas).
Compilación de borradores finalizada exitosamente.
```

---

## 4. Tabla de documentos generados

| Documento | Páginas | Primera sección en el PDF | Referencias sin resolver | Citas sin resolver | Etiquetas duplicadas | Cajas desbordadas (>10 pt) |
|---|:---:|:---|:---:|:---:|:---:|:---:|
| `borrador_completo` | 155 | `2. Antecedentes` | 0 | 0 | 0 | 15 |
| `borrador_2_Antecedentes` | 23 | `2. Antecedentes` | 0 | 0 | 0 | 0 |
| `borrador_3_Marco_Teorico` | 25 | `3. Marco Teórico` | 0 | 0 | 0 | 5 |
| `borrador_4_EDA` | 10 | `4. Análisis Exploratorio` | 0 | 0 | 0 | 2 |
| `borrador_5_Metodologia` | 22 | `5. Metodología` | 0 | 0 | 0 | 7 |
| `borrador_6_Resultados` | 36 | `6. Resultados` | 0 | 0 | 0 | 1 |
| `borrador_A_Anexos` | 32 | `A. Código de los módulos` | 0 | 0 | 0 | 0 |

*(Nota: las cajas desbordadas son inherentes al texto original de TT1, listados de código y llamadas extensas de Qiskit en `\texttt`, tal como se documenta en el README de capítulos).*

---

## 5. Prueba de literalidad de §2

Ejecutada mediante `Docs/capitulos/comun/verificar_literal_s2.py` comparando contra `Docs/Technical_Report.tex`:

```
=================================================================
Verificación de literalidad de §2 (Technical_Report.tex vs 2_Antecedentes)
=================================================================
OK   2.0_introduccion.tex       (líneas 692–700,  9 líneas coincidentes)
OK   2.1.1_ml_clasico.tex       (líneas 701–725, 25 líneas coincidentes)
OK   2.1.2_deep_learning.tex    (líneas 726–750, 25 líneas coincidentes)
OK   2.1.3_fundamentos_qml.tex  (líneas 751–798, 48 líneas coincidentes)
OK   2.1.4_hibridos_salud.tex   (líneas 799–814, 16 líneas coincidentes)
OK   2.1.5_cbis_ddsm.tex        (líneas 815–830, 16 líneas coincidentes)
OK   2.1.6_tabla_ampliada.tex   (líneas 831–838 previas a landscape: coincidencia exacta)
-----------------------------------------------------------------
Resultado: ÉXITO COMPLETO — Todas las líneas coinciden literalmente.
```

---

## 6. Tres ejemplos concretos de resolución de referencias cruzadas entre capítulos

Verificados mediante extracción directa de texto con PyMuPDF (`fitz`) sobre los archivos PDF generados:

1. **Capítulo 2 (`2_Antecedentes`) refiriendo al Capítulo 4 (`4_EDA`):**
   - En el archivo fuente `2.1.8_imagenes_cuanticas.tex` se incluye: `(Capítulo~\ref{sec:eda})`.
   - En el PDF generado `Docs/capitulos/2_Antecedentes/borrador_2_Antecedentes.pdf` (página 17) el texto compilado dice textualmente:
     > *«bits por píxel (Capítulo 4). Para codificarlas con NEQR habría que completarlas a 213 × 213 posi-»*
   - Resuelve el número de capítulo **4** sin `??`.

2. **Capítulo 5 (`5_Metodologia`) refiriendo a Sección 3.4 (`3_Marco_Teorico`) y Capítulo 6 (`6_Resultados`):**
   - En `5.8_M6_separabilidad.tex` se incluye: `sección~\ref{sec:metricas}`.
   - En `5.10_M8_evaluacion.tex` se incluye: `Capítulo~\ref{sec:resultados}`.
   - En el PDF generado `Docs/capitulos/5_Metodologia/borrador_5_Metodologia.pdf` (página 15 y página 18) el texto compilado dice textualmente:
     > (Pág. 15): *«La dimensión efectiva d del espacio que generan las lesiones [4] (ecuación (48), sección 3.4),»*
     > (Pág. 15): *«La geometric difference regularizada ggen [4] (ecuaciones (45) y (46), sección 3.4), sujeta a»*
     > (Pág. 18): *«reportan en el Capítulo 6.»*
   - Resuelve la subsección **3.4** y el capítulo **6** sin `??`.

3. **Capítulo 4 (`4_EDA`) refiriendo al Anexo C (`A_Anexos`):**
   - En `4.2_variable_objetivo.tex` se incluye: `Figura~\ref{fig:class_distribution} del Anexo~\ref{anx:figuras_eda}`.
   - En el PDF generado `Docs/capitulos/4_EDA/borrador_4_EDA.pdf` (página 2) el texto compilado dice textualmente:
     > (Pág. 2): *«namiento y prueba (train/test) se ilustra en la Figura C.5.1 del Anexo C.5.»*
   - Resuelve la figura y subsección de anexo **C.5** sin `??`.

---

## 7. Desviaciones autorizadas de la especificación

- **Creación de `.latexmkrc` en cada carpeta de capítulo:**
  - *Contexto:* Se comprobó empíricamente que `latexmk` (versión 4.86a en TeX Live) no busca archivos de configuración en directorios superiores de forma automática al invocarse en un subdirectorio como `cd Docs/capitulos/5_Metodologia && latexmk -pdf borrador_5_Metodologia.tex`.
  - *Consulta y resolución:* Se consultó al coordinador mediante `orca orchestration ask`. El coordinador respondió:
    > *"Sí: crea un .latexmkrc en cada carpeta de capítulo, pero que solo contenga una línea que cargue el común (p. ej. do '../.latexmkrc'; o el equivalente que funcione, con ruta relativa al propio archivo). Toda la configuración real (TEXINPUTS, aux_dir/out_dir a ../_build/<carpeta>, PDF en la carpeta) vive en Docs/capitulos/.latexmkrc. compilar_borradores.sh debe crear ese .latexmkrc por carpeta si falta, para que 1_Panorama_General y 7_Conclusiones lo reciban solas. Anótalo en el informe como desviación autorizada."*
  - *Implementación:* Se implementó exactamente esta estructura. Cada carpeta de capítulo contiene únicamente `do '../.latexmkrc';\n`. Toda la configuración real reside en `Docs/capitulos/.latexmkrc`. El script `compilar_borradores.sh` (a través de `generar_piezas.py`) genera dicho archivo si falta en cualquier carpeta descubierta.

---

## 8. Verificación de criterios de aceptación

1. **Ejecución completa de `compilar_borradores.sh`:** Termina con código 0 y genera `borrador_completo.pdf` y los 6 PDFs por capítulo. (**Verificado**)
2. **Cero referencias/citas sin resolver y cero duplicados:** 0 en todos los documentos. (**Verificado**)
3. **Coincidencia de numeración:** Primera sección de cada borrador coincide con la del completo (2, 3, 4, 5, 6 y A). (**Verificado**)
4. **Bibliografía específica por capítulo:** Verificado con script automatizado que cada capítulo contiene única y exclusivamente las claves que cita (27 en §2, 15 en §3, 0 en §4, 6 en §5, 4 en §6, 0 en Anexos). (**Verificado**)
5. **Compilación aislada con `latexmk`:** Comprobado con `5_Metodologia`, `6_Resultados` y `A_Anexos`; compilan sin error y no dejan ningún archivo auxiliar en la carpeta de trabajo (se aíslan en `_build/<carpeta>/`). (**Verificado**)
6. **Literalidad de §2:** 100% verificado línea a línea con `verificar_literal_s2.py`. (**Verificado**)
7. **Prueba de `compilar_prueba.sh 5_Metodologia`:** Ejecutado; reporta «Compila sin errores» y excluye `borrador_*.tex`. (**Verificado**)
8. **Prueba de extensibilidad con `7_Conclusiones`:** Se creó temporalmente `7_Conclusiones/7.0_prueba.tex`. El sistema generó automáticamente su `.latexmkrc`, su borrador independiente (`borrador_7_Conclusiones.pdf`), lo integró en `borrador_completo.tex` entre §6 y los anexos, y compiló sin errores. Posteriormente se eliminó por completo la carpeta y auxiliares temporales. (**Verificado**)
