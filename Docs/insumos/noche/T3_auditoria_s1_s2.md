# T3 · Auditoría de §1 (Panorama general) y §2 (Antecedentes)

Lee primero `Docs/insumos/noche/reglas.md`.

## Objetivo

Un informe de **diagnóstico**, no una reescritura. El autor redactará §1 y §2 con el coordinador; necesita saber, párrafo por párrafo, qué está mal sustentado, qué contradice los resultados del proyecto y qué parece paráfrasis sin fuente.

**Alcance:** `Docs/Technical_Report.tex`, líneas 470–978 (§1 y §2, hasta antes de `\section{Marco Teórico}`), y el Abstract (líneas 421–468). **Solo lectura.**

**Salida única:** `Docs/insumos/auditoria_s1_s2.md`.

## Qué revisar en cada párrafo

Para cada párrafo con afirmaciones de hecho, una fila en una tabla por subsección:

| Línea | Afirmación (resumida) | ¿Tiene `\cite`? | Problema | Fuente candidata o corrección | Gravedad |

Tipos de problema (usa estas etiquetas):
- **SIN_CITA**: afirmación factual o cifra sin `\cite`, incluidos autores nombrados en el texto sin `\cite` (p. ej. «Wang et al. (2020)»).
- **PARAFRASIS?**: párrafo con estilo de traducción de una fuente concreta y sin cita. Busca la fuente: haz `grep -ril` de frases clave (en inglés) en `Docs/fuentes/txt/`. Si la encuentras, da la cita literal con el formato `«…» (Clave, p. N)`. Si no, di qué buscaste.
- **CONTRADICE_PROYECTO**: lo que el texto dice del propio proyecto y ya no es cierto según `CLAUDE.md` y la bitácora. Ejemplos a comprobar como mínimo: uso de `TorchConnector` (D-014 lo eliminó); «hasta 16 qubits» (H-051 midió unos 25 para el *embedding* y 22 para el kernel); «partición train/test por categoría BI-RADS» (no verificado); «normalización» en el preprocesamiento (D-009, D-010); «100–300 features» (son 67, D-023); BCDR como «Barcelona Digital…» (es *Breast Cancer Digital Repository*); `PauliFeatureMap` con rotaciones X/Y/Z en lugar de `['Y','ZZ']` (D-031); que el MLP recibe vectores de dimensión k en todas las condiciones; el *parameter-shift* para entrenar θ (Arquitectura B: θ fijo, D-014).
- **SOBREAFIRMA**: se presenta como hecho lo que es hipótesis o lo que los resultados refutan (p. ej. «la geometría euclidiana es insuficiente», «φ introduce correlaciones que los métodos clásicos no capturan»). Indica qué hallazgo lo matiza (H-0xx).
- **CITA_DUDOSA**: la cita existe pero la fuente probablemente no respalda la frase (p. ej. una nota de prensa de estadísticas citada para variabilidad entre radiólogos). Ya hay casos documentados en `Docs/insumos/bibliografia_revision.md` §2–§4: incorpóralos, no los repitas con otras palabras.
- **FUERA_DE_TEMA**: párrafo que no sostiene el argumento del capítulo (p. ej. Grover y la búsqueda no estructurada).
- **CIFRA**: número que hay que comprobar contra su fuente (estadísticas de cáncer, AUC de otros trabajos).

Gravedad: **alta** (un sinodal lo señalaría o es falso), **media**, **baja** (redacción).

## Secciones del informe

1. Resumen: conteo por tipo de problema y por gravedad; las 10 correcciones más importantes en orden.
2. Tablas por subsección (§1.1.1 … §2.1.6, Abstract).
3. **Paráfrasis localizadas**: cada una con la cita literal verificada de la fuente.
4. **Lista de `\cite` faltantes** con la clave existente que corresponde (de `Technical_Report.tex`, `bibitems_nuevos.tex` o `bibitems_noche.tex`), o «falta referencia».
5. **La pregunta de investigación** (líneas 593–601): cita su texto literal y señala, sin reescribirla, qué partes presuponen un resultado (p. ej. «dicha mejora») y qué partes ya se pueden responder con las tres dimensiones que el propio texto enumera (representación, clasificación, viabilidad ↔ OE-3, OE-5, OE-6). **No propongas hipótesis**: el autor decidió conservar la forma de pregunta.
6. Lo que no pudiste comprobar.

## Aceptación

- `python3 Code/tools/verificar_citas_fichas.py Docs/insumos/auditoria_s1_s2.md` pasa (todas las citas literales con clave verificadas).
- Cada fila lleva número de línea real del `.tex` (compruébalo con `sed -n 'Np'`).
- Informe breve en `Docs/insumos/noche/informe_T3.md` con la salida del verificador.
