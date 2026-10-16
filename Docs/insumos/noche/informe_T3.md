# Informe de Trabajo · Tarea T3: Auditoría de §1 y §2 del Reporte Técnico

**Fecha:** 2026-10-14  
**Trabajador:** Dispatch `ctx_27222ac83f9a` / Task `task_0324284695a9` (Terminal `term_f1f13836-58ed-4d5a-b7ee-436b37e74a24`)  
**Coordinador Orca:** `orca_session_id:claude_b7dae366_a86f_4f0c_bf1a_4484c05dcb63`  
**Repositorio:** `/Users/alexander_san/TT`  

---

## 1. Resumen ejecutivo

Se completó íntegramente la auditoría diagnóstica de las secciones §1 (Panorama General) y §2 (Antecedentes) y del Abstract de `Docs/Technical_Report.tex` (líneas 421–978), en estricto modo de **solo lectura**, según lo especificado en `Docs/insumos/noche/T3_auditoria_s1_s2.md` y respetando las reglas comunes de `Docs/insumos/noche/reglas.md`.

El informe de diagnóstico resultante fue redactado y estructurado en el archivo único:
`Docs/insumos/auditoria_s1_s2.md`

### Principales resultados del diagnóstico:
1. **89 incidencias identificadas:**
   - `SIN_CITA`: 31 (afirmaciones factuales, cifras y menciones explícitas de autores sin comando `\cite`).
   - `PARAFRASIS?`: 8 (párrafos traducidos o adaptados directamente del inglés sin atribución).
   - `CONTRADICE_PROYECTO`: 16 (afirmaciones sobre el propio pipeline que contradicen decisiones cerradas D-xxx y mediciones empíricas).
   - `SOBREAFIRMA`: 11 (dogmas sobre supuesta ventaja cuántica o insuficiencia clásica no demostrada).
   - `CITA_DUDOSA`: 6 (citas a fuentes que no respaldan la afirmación del texto).
   - `FUERA_DE_TEMA`: 3 (digresiones sobre el algoritmo de Grover y la máquina ENIAC).
   - `CIFRA`: 14 (valores numéricos discrepantes o atribuidos a fuentes secundarias).
2. **Distribución por gravedad:**
   - **Alta:** 42 incidencias.
   - **Media:** 33 incidencias.
   - **Baja:** 14 incidencias.
3. **17 citas textuales verificadas:** Localización de fuentes primarias en `Docs/fuentes/txt/` para todas las paráfrasis y atribuciones críticas (Xiang et al. 2024, Mari et al. 2020, Shaydulin & Wild 2022, Azevedo et al. 2022, El Hafidi et al. 2025, Preskill 2018, McClean et al. 2018, Lee et al. 2017, Thanasilp et al. 2024, Huang et al. 2021, Schuld & Killoran 2022).
4. **Análisis crítico de la pregunta de investigación (l. 593–601):** Señalamiento de la presuposición de mejora («y qué impacto tiene dicha mejora») y respuesta sistemática y consolidada a las tres dimensiones (representación ↔ OE-3, clasificación ↔ OE-5, viabilidad ↔ OE-6) a partir de la evidencia experimental final del proyecto, respetando la estructura interrogativa del autor.

---

## 2. Archivos modificados y creados

| Archivo | Estado | Descripción |
|---|:---:|---|
| `Docs/insumos/auditoria_s1_s2.md` | **Creado** | Informe de auditoría integral con resumen, tablas por subsección (107 filas), paráfrasis con citas textuales verificadas, lista de `\cite` faltantes, análisis de la pregunta de investigación y catálogo de no comprobados. |
| `Docs/insumos/noche/informe_T3.md` | **Creado** | Presente informe de entrega de la tarea T3. |

*Nota de integridad:* No se editó `Docs/Technical_Report.tex`, `Docs/Technical_Report.bib`, `Other/bitacora_decisiones.md`, `CLAUDE.md`, ni ningún archivo en `Data/` o `Code/`. No se realizaron operaciones de control de versiones git.

---

## 3. Pruebas de aceptación

### 3.1 Verificación de citas textuales (`verificar_citas_fichas.py`)

Se ejecutó la herramienta de comprobación formal sobre el archivo de auditoría generado:

```bash
python3 Code/tools/verificar_citas_fichas.py Docs/insumos/auditoria_s1_s2.md
```

**Salida obtenida:**
```
auditoria_s1_s2.md: OK · 17/17 citas verificadas

1/1 fichas pasan.
```
*Código de salida:* `0`.  
Todas las citas literales con clave (`«...» (Clave, p. N)`) coinciden exactamente con el texto plano de los PDF extraídos en `Docs/fuentes/txt/`.

### 3.2 Verificación de correspondencia de líneas del `.tex`

Se auditó que cada una de las filas de las tablas del informe (`Docs/insumos/auditoria_s1_s2.md`, Sección 2) corresponda a números de línea reales y válidos dentro de `Docs/Technical_Report.tex`.
- Total de filas de tabla evaluadas: 107 filas.
- Filas fuera de rango o con desajuste de contexto: 0.

---

## 4. Hallazgos prioritarios para el autor y el coordinador

1. **Desacoples críticos con el diseño implementado:**
   - **`TorchConnector`:** Mencionado en el Abstract (l. 443) y en §2.1.3 (l. 793). En D-014 se eliminó: los embeddings $\langle Z_i \rangle$ están precalculados y el MLP de PyTorch se entrena sobre la matriz en caché.
   - **Entrenamiento de $\theta$ por *parameter-shift*:** Afirmado en §2.1.3 (l. 766–768) como optimización conjunta del circuito y la red downstream. En la Arquitectura B, $\theta$ está fijo con semilla 42 y no se entrena (H-011, H-051, H-054 demuestran que entrenar $\theta$ a $k=12$ por parameter-shift superaba el tiempo admisible por factor $\approx 3,600$).
   - **`PauliFeatureMap` en C5:** Descrito en l. 435–436 y 779 como rotaciones multi-eje en $X, Y, Z$. En D-031 se fijó exclusivamente como `pauli_feature_map(paulis=['Y', 'ZZ'])` con `reps=1`.
   - **Límites de simulación:** La l. 623 afirma «circuitos de hasta 16 qubits», mientras que H-051 demostró que en Apple Silicon M3 (16 GiB) el límite es $\approx 25$ qubits para embedding y $\approx 22$ para kernel compute-uncompute.
2. **Citas espurias:**
   - Línea 557: Se cita la página de una clínica mamográfica privada local (*Windsong Radiology*, `Windsong2026_EarlyDetection`) para respaldar una «revisión sistemática de aplicaciones oncológicas de QML». Debe cambiarse por una revisión formal como Radhi et al. (2025).
   - Línea 527: Se cita una nota de prensa de estadísticas globales de cáncer (`GlobalCancerStatistics2024_2`) para fundamentar la «variabilidad inter-observador entre radiólogos».
   - Línea 484: `GLOBOCAN2022` apunta a Freihat et al. (2025), un análisis secundario de proyecciones, mientras el texto atribuye el dato directamente a la IARC. Debe usarse `Bray2024GLOBOCAN`.
3. **Paráfrasis y omisiones de `\cite`:**
   - Línea 559: Traducción literal del abstract de Xiang et al. (2024) sin comillas ni `\cite`.
   - Línea 563: Traducción literal de Mari et al. (2020), pp. 2–3 sin `\cite`.
   - Línea 783: Traducción literal de El Hafidi et al. (2025), pp. 6 y 9 sin `\cite`.
   - Línea 825: Azevedo et al. (2022) sin `\cite`, con el nombre de BCDR falseado como «Barcelona Digital Breast Cancer Dataset» (es *Breast Cancer Digital Repository*) y omitiendo que el 84 % fue un empate con la línea base clásica ResNet C+TL.
4. **Obras huérfanas en bibliografía ya comentadas en el texto:**
   - `Wang2020DeepLearning` (mencionada en l. 529, 740, 873).
   - `Xiang2024QuantumCNN` (mencionada en l. 559, 805, 927).
   - `Azevedo2022QuantumTransfer` (mencionada en l. 613, 825, 939).
   - `Baccouche2022ResidualNN` (mencionada en l. 821, 883).

---

## 5. Elementos marcados como `[VERIFICAR]` y no comprobados

En apego a la regla de no inventar datos:
- **Rifat et al. (2024)** (BreastMNIST 69 % frente a 67 %, l. 805): Marcado como `[VERIFICAR: falta referencia]`. El artículo está tras muro de pago en IEEE Xplore. La cifra de 69 % se confirmó vía fuente secundaria (Yurtseven, 2025), pero el «frente a 67 %» y el reconocimiento explícito de restricciones de hardware no pudieron verificarse en el texto primario.
- **Referencias huérfanas en la Tabla 2.1:** `Bilal et al. (2025)` (l. 895), `Singh et al. (2025)` (l. 905) y `Ajlouni et al. (2023)` (l. 917) se marcaron como `[VERIFICAR: falta referencia]` porque no tienen `\bibitem` en `Technical_Report.tex` ni en los archivos de insumos.
- **Artículos clínicos sin PDF en el repositorio:** `Anez2025AIPipeline`, `Mashekova2025AIBreastCancer`, `Avci2023MammographyEnhancement`, `Abdelhafiz2019DeepCNN`, `Shia2025MicrocalcClassification` y `Kim2025GlobalBreastCancer`. Sus afirmaciones y porcentajes se mantuvieron como están en el `.tex`, señalando en la Sección 6 de la auditoría que su texto completo no fue abierto.
- **Digresión de la ENIAC (l. 676–680):** No se localizó fuente documental en el repositorio para la anécdota del «cerebro gigante» de 1945/1946; se recomienda eliminar o abreviar como ilustración retórica.
