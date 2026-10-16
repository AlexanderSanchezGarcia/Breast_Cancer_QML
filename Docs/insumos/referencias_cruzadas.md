# Informe de Referencias Cruzadas y Numeración de Capítulos

**Fecha:** 2026-10-14  
**Contexto:** Reorganización estructural del reporte técnico en el marco de los trabajos nocturnos. El Análisis Exploratorio de Datos (EDA) se reubica como **Capítulo 4** (previamente §5), funcionando como puente justificativo hacia la **Metodología (Capítulo 5)** (previamente §4). El orden global canónico del reporte queda establecido como:
1. Panorama general
2. Antecedentes
3. Marco teórico
4. **Análisis Exploratorio de Datos (EDA)**
5. **Metodología**
6. Resultados
7. Conclusiones
8. Anexos (A--E)

---

## 1. Correcciones ejecutadas en `Docs/capitulos/4_EDA/`

Todas las referencias en los archivos correspondientes al Capítulo 4 fueron corregidas y resueltas:

| Archivo | Línea original | Texto original | Corrección aplicada | Justificación |
|---|---|---|---|---|
| `4.0_introduccion.tex` | 20 | «descritos en esta sección fueron obtenidos» | «descritos en este capítulo fueron obtenidos mediante el cuaderno \texttt{1\_EDA.ipynb}» | El EDA es ahora un capítulo completo (Capítulo 4). Se añadió además enlace explícito a `capítulo~\ref{sec:metodologia}`. |
| `4.4_imagenes_dicom.tex` | 29 | «características radiómicas (sección de Metodología)» | «características radiómicas (capítulo~\ref{sec:metodologia}, sección~\ref{sec:modulo3})» | Se reemplazó el texto libre por referencias LaTeX directas a la Metodología y a su Módulo 3. |
| `4.4_imagenes_dicom.tex` | 47 | «faltan en los archivos DICOM.» | «faltan en los archivos DICOM (véase la Figura~\ref{fig:manufacturers} del Anexo~\ref{anx:figuras_eda}).» | Se vinculó formalmente con la figura de fabricantes reubicada en el Anexo A.3.2. |
| `4.5_hallazgos.tex` | 6--63 | «\subsection{Hallazgos principales}» | «\subsection{Implicaciones para el diseño}\label{sec:implicaciones_diseno}» | Se incorporó la Tabla~\ref{tab:eda_implicaciones_diseno} con 8 filas que referencian `\ref{sec:descripcion_general}`, `\ref{sec:modulo2}`, `\ref{sec:modulo3}`, `\ref{sec:modulo4}` y `\ref{sec:modulo7}`. |
| `4.0` a `4.5` (todos) | 4 | N/A | `% Capítulo 4 desde el 2026-10-14 (antes §5).` | Cabecera normalizada en todos los archivos del EDA. |

---

## 2. Referencias escritas a mano en otros capítulos (`Docs/capitulos/` y `Docs/Technical_Report.tex`)

A continuación se auditan las referencias detectadas fuera del Capítulo 4 que no deben ser modificadas directamente por este trabajador para respetar la partición de tareas paralela:

| Archivo | Línea | Texto actual | A qué apunta ahora | Propuesta de corrección (`\ref{…}` o número nuevo) |
|---|---|---|---|---|
| `Docs/Technical_Report.tex` | 468 | `% SECCIÓN 1 — PANORAMA GENERAL` | Encabezado estructural de Capítulo 1 | Mantener como comentario informativo o actualizar a `% CAPÍTULO 1`. |
| `Docs/Technical_Report.tex` | 617 | «Como se documentó en la sección 1.1.1,» | Subsección 1.1.1 (Antecedentes clínicos) | Cambiar por `\ref{sec:1.1.1}` o mantener «sección~1.1.1» si la numeración del Capítulo 1 permanece fija. |
| `Docs/Technical_Report.tex` | 740 | «Como se señaló en la sección 1.1.2,» | Subsección 1.1.2 (Falta de generalización) | Cambiar por `\ref{sec:1.1.2}` o mantener «sección~1.1.2». |
| `Docs/capitulos/6_Resultados/6.7_lecciones_implementacion.tex` | 3 | `% Sección 6.7 del reporte técnico.` | Comentario cabecera de subsección | Mantener o actualizar a `% Subsección 6.7 del reporte técnico.`. |
| `Docs/capitulos/6_Resultados/6.8_sintesis.tex` | 3 | `% Sección 6.8 del reporte técnico.` | Comentario cabecera de subsección | Mantener o actualizar a `% Subsección 6.8 del reporte técnico.`. |
| `Docs/capitulos/README.md` | 3 | «con un archivo por subsección (§4) o por subsubsección (§3)» | Estructura interna de carpetas | Actualizar a «(§5 Metodología, antes §4) o por subsubsección (§3 Marco Teórico)». |
| `Docs/capitulos/README.md` | 14 | «Para comprobar las cifras de §6:» | Capítulo 6 Resultados | Mantener «§6» (Resultados no cambió de número). |
| `Docs/capitulos/README.md` | 23 | «Falta la cita de IBSI en §4.4:» | Módulo 2 Preprocesamiento (antiguo §4.4) | Actualizar a «en §5.4 (Módulo 2)». |
| `Docs/capitulos/README.md` | 24 | «ya está en §3.4,» | Marco Teórico (Métricas) | Mantener «§3.4». |
| `Docs/capitulos/README.md` | 25 | «etiquetas de §3 cambiaron:» | Marco Teórico | Mantener «§3». |
| `Docs/capitulos/README.md` | 32 | «§3.2.3: se conserva la ecuación» | Subsección 3.2.3 | Mantener «§3.2.3». |
| `Docs/capitulos/README.md` | 33 | «§4.9: dice más de un orden de magnitud» | Módulo 7 Clasificación (antiguo §4.9) | Actualizar a «§5.9 (Módulo 7)». |
| `Docs/capitulos/README.md` | 37 | «§3.2.7: el paquete del miércoles» | Subsección 3.2.7 | Mantener «§3.2.7». |
| `Docs/capitulos/README.md` | 38 | «§3.4.8: con el empate C1 = C2» | Subsección 3.4.8 | Mantener «§3.4.8». |
| `Docs/capitulos/README.md` | 39 | «§3.3.4: la precisión de 0.015625» | Subsección 3.3.4 | Mantener «§3.3.4». |
| `Docs/capitulos/README.md` | 40 | «§3.2.5: la ecuación de real_amplitudes» | Subsección 3.2.5 | Mantener «§3.2.5». |
| `Docs/capitulos/README.md` | 41 | «§4.4 y D-009: la caja más pequeña» | Módulo 2 Preprocesamiento (antiguo §4.4) | Actualizar a «§5.4 (M2) y D-009». |
| `Docs/capitulos/README.md` | 43 | «Gemini en §5 y §6» | Antiguo §5 (EDA) y §6 (Resultados) | Actualizar a «EDA (ahora §4) y §6». |
| `Docs/capitulos/README.md` | 45 | «§6.6: puso los porcentajes» | Subsección 6.6 | Mantener «§6.6». |
| `Docs/capitulos/README.md` | 46 | «§6.2: las medianas a c = 0.02» | Subsección 6.2 | Mantener «§6.2». |
| `Docs/capitulos/README.md` | 47 | «§6.4: decía auditoría independiente» | Subsección 6.4 | Mantener «§6.4». |
| `Docs/capitulos/README.md` | 48 | «§5: se restauraron los anchos» | Antiguo §5 (EDA) | Actualizar a «§4 (EDA, antes §5)». |
| `Docs/capitulos/README.md` | 54 | «§4.3, por los nombres de los CSV» | Antiguo §4.3 (Módulo 1 Lectura) | Actualizar a «§5.3 (M1)». |
| `Docs/capitulos/README.md` | 55 | «§3.3.4, por las llamadas de Qiskit» | Subsección 3.3.4 | Mantener «§3.3.4». |
| `Docs/capitulos/README.md` | 56 | «§3.2.3, en la ecuación con la nota» | Subsección 3.2.3 | Mantener «§3.2.3». |

---

## 3. Nota de equivalencias para `Other/bitacora_decisiones.md`

En cumplimiento de las reglas comunes, **no se modificó la bitácora**. Para preservar el registro histórico de las 211 referencias existentes que mencionan secciones antiguas, se recomienda al coordinador incorporar la siguiente tabla de equivalencias al inicio de `Other/bitacora_decisiones.md`:

```markdown
> ### Nota de equivalencia de secciones (reorganización 2026-10-14)
> Con el movimiento del Análisis Exploratorio de Datos como Capítulo 4 (antes §5)
> y la Metodología como Capítulo 5 (antes §4), las referencias a secciones en las
> entradas históricas se interpretan según la siguiente correspondencia:
>
> | Referencia en bitácora | Sección original | Ubicación actual en el reporte |
> |---|---|---|
> | §4.1 | Descripción general del pipeline | §5.1 (`sec:descripcion_general`) |
> | §4.2 | Requerimientos funcionales y no funcionales | §5.2 (`sec:requerimientos`) |
> | §4.3 | M1 · Ingesta y validación de DICOM | §5.3 (`sec:modulo1`) |
> | §4.4 | M2 · Preprocesamiento y segmentación | §5.4 (`sec:modulo2`) |
> | §4.5 | M3 · Extracción de features radiómicas | §5.5 (`sec:modulo3`) |
> | §4.6 | M4 · Selección y escalado angular | §5.6 (`sec:modulo4`) |
> | §4.7 | M5 · Transformaciones cuánticas y embeddings | §5.7 (`sec:modulo5`) |
> | §4.8 | M6 · Métricas de separabilidad geométrica | §5.8 (`sec:modulo6`) |
> | §4.9 | M7 · Clasificación y entrenamiento MLP | §5.9 (`sec:modulo7`) |
> | §4.10 | M8 · Evaluación comparativa y correlación | §5.10 (`sec:modulo8`) |
> | §5.x / §5 | Análisis Exploratorio de Datos (EDA) | Capítulo 4 completo (§4.0 a §4.5) |
> | §6.x / §6 | Resultados experimentales | Capítulo 6 (§6.0 a §6.8, sin cambio numérico) |
> | §7.x / §7 | Discusión y Conclusiones | Capítulo 7 (sin cambio numérico) |
> | §8.x | Infraestructura y anexos | Anexos A--E (`Docs/capitulos/A_Anexos/`) |
```

---

## 4. Auditoría de etiquetas de sección clave entre capítulos

Para garantizar la interoperabilidad de enlaces cruzados en futuras compilaciones completas del reporte:

- `\label{sec:eda}`: Definida en `Docs/capitulos/4_EDA/4.0_introduccion.tex`.
- `\label{sec:implicaciones_diseno}`: Definida en `Docs/capitulos/4_EDA/4.5_hallazgos.tex`.
- `\label{anx:figuras_eda}`: Definida en `Docs/capitulos/A_Anexos/A.3.2_figuras_eda.tex`.
- `\label{sec:metodologia}`: Definida en `Docs/capitulos/5_Metodologia/5.0_introduccion.tex`.
- `\label{sec:descripcion_general}`: Definida en `Docs/capitulos/5_Metodologia/5.1_descripcion_general.tex`.
- `\label{sec:modulo1}` a `\label{sec:modulo8}`: Definidas en `Docs/capitulos/5_Metodologia/5.3` a `5.10`.
- `\label{sec:resultados}`: Definida en `Docs/capitulos/6_Resultados/6.0_introduccion.tex`.
- `\label{sec:datos_caracteristicas_seleccion}`: Definida en `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex`.
- `\label{sec:separabilidad_representaciones}`: Definida en `Docs/capitulos/6_Resultados/6.2_separabilidad.tex`.
- `\label{sec:rendimiento_clasificacion}`: Definida en `Docs/capitulos/6_Resultados/6.3_clasificacion.tex`.
- `\label{sec:qsvm_ventaja}`: Definida en `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex`.
- `\label{sec:comparacion_global}`: Definida en `Docs/capitulos/6_Resultados/6.5_comparacion.tex`.
- `\label{sec:restricciones_simulador}`: Definida en `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex`.
- `\label{sec:lecciones_implementacion}`: Definida en `Docs/capitulos/6_Resultados/6.7_lecciones_implementacion.tex`.
- `\label{sec:sintesis_objetivos}`: Definida en `Docs/capitulos/6_Resultados/6.8_sintesis.tex`.
