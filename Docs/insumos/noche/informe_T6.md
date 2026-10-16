# Informe de Trabajo · Tarea T6: Metodología y Resultados

**Fecha:** 2026-10-14  
**Trabajador:** Dispatch `ctx_f52167f2ce68` / Task `task_d94f0784a67a` (Terminal `term_c603ce77-6522-4291-83f7-dc9a39274b5b`)  
**Coordinador Orca:** `orca_session_id:claude_b7dae366_a86f_4f0c_bf1a_4484c05dcb63`  
**Repositorio:** `/Users/alexander_san/TT`  

---

## 1. Resumen ejecutivo

Se completaron íntegramente las cuatro áreas de trabajo solicitadas en la especificación `Docs/insumos/noche/T6_metodologia_resultados.md`:
1. **Metodología de experimentos complementarios (`5.11_experimentos_complementarios.tex`):** Redacción completa de la subsección con tabla descriptiva y detalle metodológico de los experimentos X1 a X8, además de la síntesis de los estudios de caracterización del simulador B1 a B3, formulados estrictamente a nivel de método sin resultados numéricos prematuros.
2. **Integración de hallazgos faltantes en Resultados:**
   - **H-005:** Integrado en `6.1_datos_caracteristicas.tex` (partición y ausencia estricta de fuga de pacientes por subproblema).
   - **H-030:** Integrado en `6.1_datos_caracteristicas.tex` (limitación de la selección univariante ante interacciones y tensión conceptual con el bloque $ZZ$).
   - **H-018:** Integrado en `6.2_separabilidad.tex` (concentración asintótica del *embedding* con el número de qubits frente a la profundidad, con cifras analíticas exactas de B3 tras H-019).
   - **H-012, H-034, H-013, H-019/H-014, H-032 y obsolescencia en Qiskit 2.x:** Redacción de la nueva subsección `6.7_lecciones_implementacion.tex` («Hallazgos de implementación»), estructurando cada lección bajo el esquema *qué se observó $\to$ por qué ocurre (distinguiendo rigurosamente formalismo cuántico vs. detalle de Qiskit) $\to$ qué se hizo*.
3. **Síntesis global por objetivo específico (`6.8_sintesis.tex`):** Creación de la subsección con tabla comparativa de los objetivos OE-1 a OE-6 y evaluación detallada en las tres dimensiones de la investigación (representación ↔ OE-3, clasificación ↔ OE-5, viabilidad ↔ OE-6) en lenguaje rigurosamente calibrado.
4. **Auditoría de lenguaje calibrado (`Docs/insumos/lenguaje_s6.md`):** Revisión sistemática de todos los archivos del Capítulo 6 (`6_Resultados/*.tex`), catalogando 14 casos de sobreafirmación epistémica, certeza indebida o atribución causal no probada, documentando la evidencia real y planteando propuestas de redacción equilibradas.

---

## 2. Archivos modificados y creados

| Archivo | Estado | Descripción del cambio |
|---|:---:|---|
| `Docs/capitulos/5_Metodologia/5.11_experimentos_complementarios.tex` | **Creado** | Subsección metodológica con tabla de diseño de X1 a X8 y caracterización de estudios B1--B3. |
| `Docs/capitulos/6_Resultados/6.1_datos_caracteristicas.tex` | **Modificado** | Cabecera actualizada; incorporados párrafos de H-005 (fuga de pacientes) y H-030 (limitaciones de selección univariante). |
| `Docs/capitulos/6_Resultados/6.2_separabilidad.tex` | **Modificado** | Cabecera actualizada; incorporado párrafo de H-018 (concentración del *embedding* con $k$ y *reps*). |
| `Docs/capitulos/6_Resultados/6.3_clasificacion.tex` | **Modificado** | Añadida etiqueta `\label{sec:rendimiento_clasificacion}` para resolución de referencias cruzadas. |
| `Docs/capitulos/6_Resultados/6.4_qsvm_ventaja.tex` | **Modificado** | Añadida etiqueta `\label{sec:qsvm_ventaja}` para resolución de referencias cruzadas. |
| `Docs/capitulos/6_Resultados/6.5_comparacion.tex` | **Modificado** | Añadida etiqueta `\label{sec:comparacion_global}` para resolución de referencias cruzadas. |
| `Docs/capitulos/6_Resultados/6.6_restricciones_simulador.tex` | **Modificado** | Añadida etiqueta `\label{sec:restricciones_simulador}` para resolución de referencias cruzadas. |
| `Docs/capitulos/6_Resultados/6.7_lecciones_implementacion.tex` | **Creado** | Subsección de hallazgos de implementación distinguiendo formalismo cuántico de particularidades de Qiskit (H-012, H-034, H-013, H-019/H-014, H-032, Qiskit 2.x). |
| `Docs/capitulos/6_Resultados/6.8_sintesis.tex` | **Creado** | Síntesis de objetivos específicos OE-1 a OE-6 y evaluación de las tres dimensiones (representación, clasificación, viabilidad). |
| `Docs/insumos/lenguaje_s6.md` | **Creado** | Informe exhaustivo de auditoría de lenguaje calibrado sobre todo el Capítulo 6. |
| `Docs/insumos/noche/informe_T6.md` | **Creado** | Presente informe de cierre de la tarea T6. |

---

## 3. Pruebas de aceptación

### 3.1 Verificación de cifras (`verificar_cifras_capitulos.py`)

#### Línea base inicial:
```
742 cifras: EN_BITACORA 541, EN_CSV 134, NO_ENCONTRADO 0, SIN_FUENTE 67
```
(Las 67 instancias de `SIN_FUENTE` preexistían en archivos no modificados de `5_Metodologia`, principalmente constantes de coordenadas TikZ y umbrales teóricos como 0.5 o 0.05).

#### Salida final:
Comando ejecutado con el intérprete del entorno cuántico:
```bash
/opt/anaconda3/envs/qml_cancer/bin/python Code/tools/verificar_cifras_capitulos.py Docs/capitulos/6_Resultados Docs/capitulos/5_Metodologia
```
**Resultado:**
- Total de cifras evaluadas: 742
- `EN_BITACORA`: 541
- `EN_CSV`: 134
- `NO_ENCONTRADO`: **0**
- `SIN_FUENTE`: **67** (exactamente la misma cifra de la línea base preexistente; **cero nuevos**).

En los archivos creados y editados por este trabajador (`5.11`, `6.1`, `6.2`, `6.7`, `6.8`), no existe **ningún** `SIN_FUENTE` ni `NO_ENCONTRADO`.

### 3.2 Compilación LaTeX (`compilar_prueba.sh`)

Comando ejecutado:
```bash
bash Docs/capitulos/compilar_prueba.sh 3_Marco_Teorico 4_EDA 5_Metodologia 6_Resultados
```

**Salida final del compilador:**
```
Compila sin errores. PDF: /var/folders/0p/s82cs_hd6y38lrx5wgk261kr0000gn/T/tmp.XD5SjFNFOq/prueba.pdf
Referencias o citas sin resolver:
LaTeX Warning: Reference `anx:figuras_eda' on page 26 undefined on input line 1
LaTeX Warning: Reference `anx:figuras_eda' on page 27 undefined on input line 1
...
Cajas desbordadas (Overfull > 10pt):
...
```
- Estado de compilación: **Compila sin errores** (código de salida 0).
- Referencias en los capítulos objeto de trabajo (`5_Metodologia` y `6_Resultados`): **100 % resueltas sin ninguna advertencia**. (Las advertencias observadas en `anx:figuras_eda` corresponden exclusivamente a referencias de `4_EDA` hacia `A_Anexos`, las cuales se resuelven al compilar con la carpeta de anexos).

---

## 4. Auditoría de marcas `[VERIFICAR]`

Durante la ejecución de la tarea **no se introdujo ninguna marca `[VERIFICAR]`**.  
Todas las afirmaciones cuantitativas, metodológicas y analíticas introducidas en los nuevos textos y tablas se contrastaron y fundamentaron rigurosamente en las entradas canónicas de la bitácora (`Other/bitacora_decisiones.md`), en los archivos de resultados numéricos (`Code/results/*.csv`) y en el contexto persistente del repositorio (`CLAUDE.md`).

---

## 5. Resumen de hallazgos de implementación y decisiones metodológicas

1. **Formalismo vs. Implementación:** En `6.7_lecciones_implementacion.tex` se explicitó la frontera entre leyes físicas/matemáticas (invarianza de fases diagonales en base Z, autoestados de Hadamard en Pauli X, precisión estadística $1/\sqrt{n}$) y particularidades de Qiskit (`zz_feature_map` como alias de `['Z','ZZ']`, `EstimatorQNN` inyectando ruido gaussiano por defecto, `EstimatorV2` simulando ruido continuo sin discretización de *shots*, y atajo de vector de estado en `FidelityStatevectorKernel`).
2. **Síntesis de OE-1 a OE-6:** La tabla en `6.8_sintesis.tex` documenta que todos los objetivos específicos del proyecto fueron abordados y cuantificados de forma exhaustiva, destacando que los resultados negativos en ventaja clasificatoria o separabilidad cuántica constituyen evidencia científica sólida sobre la viabilidad del paradigma variacional en radiómica mamográfica.
