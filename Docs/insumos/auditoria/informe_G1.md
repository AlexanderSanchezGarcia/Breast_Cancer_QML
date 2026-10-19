# Informe G1 · Borrador del glosario técnico y verificación de referencias

## 1. Alcance revisado

Conforme a la especificación de la tarea G1 (`Docs/insumos/auditoria/G1_glosario.md`) y a las reglas comunes de auditoría (`Docs/insumos/auditoria/reglas.md`), se recorrieron exhaustivamente los capítulos 1 a 8, preliminares y anexos del reporte técnico integrado (`Docs/Technical_Report.tex`), con el objetivo de elaborar un borrador integral de glosario técnico orientado a un sinodal de ciencias de la computación (no especialista en computación cuántica ni en radiología diagnóstica).

El alcance comprendió:
- **Marco Teórico y Fundamentos:** `Docs/capitulos/3_Marco_Teorico/` (subsecciones 3.1.1 a 3.1.4 de fundamentos cuánticos, 3.2.1 a 3.2.7 de circuitos variacionales y mapas cuánticos, 3.3.1 a 3.3.4 de MLP e integración PyTorch--Qiskit, 3.4.0 a 3.4.8 de métricas de separabilidad y evaluación, 3.5.0 a 3.5.6 de representaciones clásicas y modelos de kernel).
- **Metodología experimental:** `Docs/capitulos/5_Metodologia/` (módulos M1 a M8 y experimentos complementarios).
- **Análisis Exploratorio y Adquisición:** `Docs/capitulos/4_EDA/` (validación de datos, variables clínicas, imágenes DICOM).
- **Resultados y Restricciones:** `Docs/capitulos/6_Resultados/` (separabilidad, clasificación, QSVM, restricciones del simulador, lecciones de implementación).
- **Antecedentes, Panorama y Conclusiones:** Capítulos 1, 2, 7 y 8, y `Docs/capitulos/G_Glosario/glosario.tex`.

### Resumen del borrador generado
Se generó el archivo `Docs/insumos/auditoria/glosario_borrador.tex` conteniendo **68 entradas** estructuradas bajo el entorno `\begin{description}`, cumpliendo la cota requerida (entre 40 y 70 entradas). Todas las entradas están ordenadas alfabéticamente (ignorando mayúsculas, minúsculas y tildes), presentan términos en inglés en `\textit{}` con su correspondiente traducción cuando se emplea en el texto, respetan estrictamente la notación y definiciones formuladas a lo largo del reporte técnico, y enlazan la sección donde se definen mediante referencias cruzadas a etiquetas verificadas existentes (`\ref{...}`).

#### Distribución temática de los términos (68 entradas):
1. **Computación cuántica (26 términos):** Ansatz; Base computacional; Circuito cuántico parametrizado (PQC); Compuerta cuántica; Concentración del kernel; Decoherencia cuántica; Entrelazamiento cuántico; Esfera de Bloch; Feature map; Incrustación cuántica (quantum embedding); Kernel cuántico de fidelidad; Kernel cuántico proyectado; Meseta estéril (barren plateau); NISQ; Operadores de Pauli; Parameter-shift; PauliFeatureMap; QSVM; Qubit; Qubit lógico; Shots / disparos; Simulador de vector de estado; Superposición cuántica; Teorema de no clonación; Transpilación; ZZFeatureMap.
2. **Aprendizaje automático y estadística (25 términos):** AUC-ROC; Coeficiente de correlación de Spearman ($\rho_s$); Diferencia geométrica ($g$); Dimensión efectiva ($d_{\mathrm{eff}}$); Escalado por cuantiles (QuantileTransformer); Exactitud (accuracy); Exceso de KTA; Fuga de datos (data leakage); Heurística de la mediana; Índice Davies-Bouldin; Kernel PCA (KPCA); KTA (Kernel-Target Alignment); MLP; Parada temprana (early stopping); PCA lineal; Ponderación de clases; Precisión; Razón multivariante de Fisher; SelectKBest; Sensibilidad / exhaustividad (recall); SVM; t-SNE; Validación cruzada estratificada por grupos (StratifiedGroupKFold); Valor esperado; Valor F1.
3. **Imagen médica y radiómica (17 términos):** BI-RADS; Calcificación mamaria; Características de primer orden; Características morfológicas; CBIS-DDSM; CLAHE; Componente conexa mayor; DICOM; GLCM; GLRLM; IBSI; Mamografía; Masa mamaria; PyRadiomics; Radiómica; Región de interés (ROI); Ventaja cuántica (contextualizada al problema de salud).

### Términos que quedaron sin definición en el reporte
De conformidad con el punto 2 de la especificación G1, los siguientes 3 términos relevantes para la comprensión de un sinodal informático no cuentan con una definición formal o ecuación explícita dentro del texto del reporte y fueron marcados explícitamente con `% sin definición en el reporte`:
1. **Decoherencia cuántica (\textit{quantum decoherence}):** Pérdida de las propiedades cuánticas de superposición y entrelazamiento debida a la interacción disipativa no controlada entre los qubits y el entorno térmico o electromagnético circundante.
2. **Qubit lógico (\textit{logical qubit}):** Qubit protegido contra fallos y decoherencia mediante la codificación redundante y distribuida de la información cuántica en múltiples qubits físicos a través de un código de corrección cuántica de errores.
3. **Teorema de no clonación (\textit{no-cloning theorem}):** Principio fundamental derivado de la linealidad de la mecánica cuántica que establece la imposibilidad física de crear una copia idéntica y exacta de un estado cuántico arbitrario y desconocido.

---

## 2. Comandos ejecutados y su salida final

### 2.1. Inspección y extracción de etiquetas `\label{...}`
Se analizaron todas las etiquetas presentes en el reporte para garantizar que cada entrada del glosario apunte a una etiqueta válida.

```sh
# Extracción y clasificación de etiquetas en Docs/
/opt/anaconda3/envs/qml_cancer/bin/python -c '
import glob, re
labels = {}
for path in sorted(glob.glob("Docs/**/*.tex", recursive=True)):
    with open(path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, 1):
            for m in re.finditer(r"\\label\{([^}]+)\}", line):
                labels[m.group(1)] = (path, idx)
print(f"Total labels found: {len(labels)}")
'
```
Salida final:
```text
Total labels found: 139
```

### 2.2. Verificación de etiquetas referenciadas en el glosario
Se confrontaron todas las etiquetas invocadas en `glosario_borrador.tex` contra el archivo auxiliar `Technical_Report.aux` del documento principal.

```sh
# Verificación de integridad de referencias
/opt/anaconda3/envs/qml_cancer/bin/python -c '
# [Script de verificación contra Technical_Report.aux]
'
```
Salida final:
```text
Total unique labels checked: 84
Missing labels: []
```

### 2.3. Prueba de compilación aislada en `/tmp/aud_G1/Docs`
Siguiendo el punto 5 de la instrucción G1 y la regla 32 de `reglas.md`, se copió el árbol `Docs/` a `/tmp/aud_G1/Docs`, se reemplazó el cuerpo de `glosario.tex` con `glosario_borrador.tex` y se ejecutó la compilación de dos pasadas con `pdflatex`:

```sh
mkdir -p /tmp/aud_G1 && cp -r Docs /tmp/aud_G1/
# [Actualización de /tmp/aud_G1/Docs/capitulos/G_Glosario/glosario.tex con el borrador]
cd /tmp/aud_G1/Docs && export PATH="/Library/TeX/texbin:$PATH"
pdflatex -interaction=nonstopmode Technical_Report.tex > /tmp/aud_G1/compile_test_pass1.log 2>&1
pdflatex -interaction=nonstopmode Technical_Report.tex > /tmp/aud_G1/compile_test_pass2.log 2>&1
```

Salida final de compilación (extracto de `compile_test_pass2.log`):
```text
Output written on Technical_Report.pdf (202 pages, 14885110 bytes).
Transcript written on Technical_Report.log.
```

Búsqueda de referencias sin resolver (`??` o `undefined`):
```sh
grep -i "LaTeX Warning: Reference" /tmp/aud_G1/compile_test_pass2.log
```
Salida final:
*(código de salida 1: cero referencias indefinidas detectadas)*

---

## 3. Hallazgos detectados

### G1-1 · MEDIA · Estructura y completitud
- Ubicación: `Docs/capitulos/G_Glosario/glosario.tex:7`
- Texto: «`\item[Pendiente.] El glosario se completa a partir de los términos definidos en los capítulos 3 y 5.`»
- Problema: El archivo de glosario obligatorio según el formato CATT carecía de contenido técnico real y mantenía una entrada provisional pendiente.
- Evidencia: Línea 7 de `Docs/capitulos/G_Glosario/glosario.tex` y requerimiento formal de la CATT para la entrega final de Trabajo Terminal.
- Propuesta: Sustituir el entorno `description` provisional por el contenido validado de `Docs/insumos/auditoria/glosario_borrador.tex` (68 términos con enlaces verificados).

### G1-2 · BAJA · Navegación y consistencia de hipervínculos
- Ubicación: `Docs/capitulos/3_Marco_Teorico/3.1.1_qubit.tex:6`
- Texto: «`\subsection{Fundamentos de computación cuántica}`»
- Problema: La subsección 3.1 no define una etiqueta `\label{sec:...}` para su encabezado principal, lo que obliga a referenciar la sección de fundamentos a través de sus ecuaciones (`\label{eq:qubit}`, `\label{eq:bloch}`) o figuras (`\label{fig:bloch}`).
- Evidencia: Inspección de etiquetas en `Docs/capitulos/3_Marco_Teorico/3.1.1_qubit.tex` donde solo figuran `eq:qubit`, `eq:basis`, `eq:bloch` y `fig:bloch`.
- Propuesta: Mantener las citas numéricas y de ecuaciones empleadas en el borrador (`sección~3.1, ec.~\ref{eq:qubit}`), y evaluar la incorporación de `\label{sec:fundamentos_cuantica}` en futuras revisiones de estilo.

---

## 4. Conteo de hallazgos por severidad

- **ALTA:** 0
- **MEDIA:** 1
- **BAJA:** 1
- **TOTAL:** 2

---

## 5. Verificación de integridad del repositorio

Se ejecutó `git -C /Users/alexander_san/TT status --short` para certificar que no se modificaron archivos versionados del reporte ni se alteraron rutas fuera de `Docs/insumos/auditoria/`:

```text
 M Other/orquestacion_noche_2026-10-19.md
?? Docs/articulo/
?? Docs/insumos/auditoria/W1_articulo.md
?? Docs/insumos/auditoria/a1_refs.py
?? Docs/insumos/auditoria/glosario_borrador.tex
?? Docs/insumos/auditoria/informe_A1.md
?? Docs/insumos/auditoria/informe_A5.md
?? Docs/insumos/auditoria/informe_A6.md
?? Docs/insumos/auditoria/informe_G1.md
```

Se confirma que únicamente se crearon dentro de esta tarea los archivos asignados:
- `Docs/insumos/auditoria/glosario_borrador.tex` (borrador con 68 términos y compilación verificada).
- `Docs/insumos/auditoria/informe_G1.md` (informe de auditoría).
