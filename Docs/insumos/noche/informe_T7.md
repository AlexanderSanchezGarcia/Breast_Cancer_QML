# Informe de Trabajo · Tarea T7: Subsecciones nuevas del Estado del arte (§2)

**Fecha:** 2026-10-14  
**Trabajador:** Dispatch `ctx_410a4fbd1933` / Task `task_3b69ce4e25d0` (Terminal `term_2136aa2c-e7d8-49ac-9adc-b0380a3d1719`)  
**Coordinador Orca:** `orca_session_id:claude_b7dae366_a86f_4f0c_bf1a_4484c05dcb63`  
**Repositorio:** `/Users/alexander_san/TT`  

---

## 1. Resumen ejecutivo

Se completó íntegramente la redacción de las tres subsecciones nuevas y la tabla comparativa ampliada del Estado del arte (§2), ubicadas en la carpeta nueva `Docs/capitulos/2_Antecedentes/`:

1. **`2.1.7_limites_ventaja.tex`** (`\label{sec:limites_ventaja}`):
   - Expone formalmente dónde se ha demostrado una ventaja cuántica analítica o experimental en aprendizaje: por estructura algebraica en la etiqueta (`Liu2021Speedup`, `Glick2024Covariant`) y con datos que son originariamente estados cuánticos transferidos a memoria cuántica (`Huang2022Experiments`).
   - Contrasta este escenario con las limitaciones intrínsecas de los datos clásicos genéricos codificados angularmente: *geometric difference* pequeña que favorece a los modelos clásicos (`huang2021power`), concentración exponencial de kernels inducida por expresividad, medición global, entrelazamiento y ruido (`Thanasilp2024`), colapso del sesgo inductivo y necesidad de espacios restringidos (`Kubler2021Inductive`), control y transición del ancho de banda (*bandwidth*) para evitar subajuste/sobreajuste (`Shaydulin2022Bandwidth`, `Canatar2023Bandwidth`), benchmarks sistemáticos donde los clasificadores clásicos superan a los cuánticos y despojar el entrelazamiento no degrada el rendimiento (`Bowles2024Benchmarking`), y perspectiva crítica sobre la reformulación de objetivos más allá de la ventaja comercial (`SchuldKilloran2022Advantage`).
   - Cierra conectando conceptualmente con el presente trabajo sin anticipar resultados numéricos: justifica por qué se evalúa la separabilidad con la diferencia geométrica y por qué se calibra el ancho de banda.
2. **`2.1.8_imagenes_cuanticas.tex`** (`\label{sec:imagenes_cuanticas}`):
   - Detalla las representaciones cuánticas de imágenes FRQI (`Le2011FRQI`) y NEQR (`Zhang2013NEQR`), indicando exactamente sus requerimientos de qubits ($2n+1$ vs. $q+2n$) y la complejidad formal de preparación ($O(2^{4n})$ vs. $O(q n 2^{2n})$), distinguiendo la escala polinomial en píxeles de la exponencial en qubits.
   - Analiza la evaluación comparativa de Parigi et al. (`Parigi2026QImR`) sobre cuatro representaciones (TNR, FRQI, NEQR, QPIE), su grado de compresión, su concentración en matrices de Gram y el hallazgo fundamental de que los kernels cuánticos de imagen directa empatan con el kernel lineal clásico, viéndose anulada cualquier ventaja por el costo $O(2^n)$ de preparación del estado.
   - Fundamenta rigurosamente por qué el presente trabajo desacopla el procesamiento espacial y codifica características radiómicas compactas (IBSI) en lugar de la imagen mamográfica completa.
3. **`2.1.9_revision_critica.tex`** (`\label{sec:revision_critica}`):
   - Enuncia formalmente las cuatro preguntas metodológicas de H-046: 1) paridad de ajuste y variables, 2) significación estadística de la diferencia frente a la incertidumbre, 3) uso único y ciego de la partición de prueba, y 4) intratabilidad de la simulación clásica del circuito.
   - Aplica exhaustivamente las cuatro preguntas a:
     - `Xiang2024QuantumCNN` (QCCNN sobre datos tabulares de Kaggle, sin mamografías, sin incertidumbre reportada, con parada temprana sobre validación y simulador clásico).
     - `ElHafidi2025` (QSVM sobre cáncer de pulmón tabular con 15 variables, paridad de datos en 6 subconjuntos, diferencia de 0.01 frente a SVM clásico RBF de 0.95 sin significación estadística, y simulación clásica con vulnerabilidad al ruido en PauliFeatureMap).
     - `Azevedo2022QuantumTransfer` (quantum transfer learning sobre mamografías de BCDR, paridad en extractor ResNet18, empate en exactitud de prueba en 84% con el modelo clásico C+TL, aumento de AUC sin intervalos en simulación que cae a 81% en QPU `ibm_lagos`, reuso de test y circuito de 4 qubits simulable).
   - Registra comentarios `% PENDIENTE: sin PDF` para `Radhi2025QuantumDeepLearning` y BreastMNIST (Rifat et al., 2024), omitiendo cualquier afirmación en el texto visible tal como estipula la especificación.
4. **`2.1.6_tabla_ampliada.tex`** (`\label{tab:estado_arte_v2}`):
   - Integra la versión ampliada de la tabla del estado del arte en orientación horizontal (`landscape`), incorporando la nueva columna **«Comp. justa»** con la calificación fundamentada bajo las cuatro preguntas de H-046.
   - Añade filas verificadas para El Hafidi et al. (2025) y Parigi et al. (2026).
   - Corrige la fila del presente trabajo (Sánchez García, 2026) con los feature maps C4 (`ZZFeatureMap`) y C5 (`PauliFeatureMap(['Y','ZZ'])`), calificación «Sí» en comparación justa, y las cifras de AUC del test de `Code/results/7_test.csv` (Masas: 0.530 en C4 / 0.581 en C5; Calcificaciones: 0.633 en C4 / 0.652 en C5), con respaldo `% fuente: H-042; 7_test.csv`.

---

## 2. Archivos creados

| Archivo | Estado | Descripción |
|---|:---:|---|
| `Docs/capitulos/2_Antecedentes/2.1.6_tabla_ampliada.tex` | **Creado** | Versión ampliada de `tab:estado_arte` (`tab:estado_arte_v2`) con columna «Comp. justa», filas de ElHafidi2025 y Parigi2026QImR, y resultados de test de C4 y C5. |
| `Docs/capitulos/2_Antecedentes/2.1.7_limites_ventaja.tex` | **Creado** | Subsección sobre límites de la ventaja cuántica con datos clásicos (Liu, Glick, Huang 2022, Huang 2021, Thanasilp, Kübler, Shaydulin, Canatar, Bowles, Schuld y Killoran). |
| `Docs/capitulos/2_Antecedentes/2.1.8_imagenes_cuanticas.tex` | **Creado** | Subsección sobre representaciones cuánticas de imagen (FRQI, NEQR, análisis de Parigi et al., justificación de features radiómicas). |
| `Docs/capitulos/2_Antecedentes/2.1.9_revision_critica.tex` | **Creado** | Subsección de revisión crítica aplicando las cuatro preguntas de H-046 a Xiang2024QuantumCNN, ElHafidi2025 y Azevedo2022QuantumTransfer. |
| `Docs/insumos/noche/informe_T7.md` | **Creado** | Presente informe durable de cierre de la tarea T7. |

*Nota:* No se modificó ningún archivo preexistente del repositorio (`Docs/Technical_Report.tex`, `Other/bitacora_decisiones.md`, etc., se mantuvieron estrictamente intactos según la regla 1 de `reglas.md`).

---

## 3. Pruebas de aceptación

### 3.1 Verificación de citas literales (`verificar_citas_fichas.py`)

Comando ejecutado:
```bash
python3 Code/tools/verificar_citas_fichas.py Docs/capitulos/2_Antecedentes
```

**Salida completa:**
```
2.1.6_tabla_ampliada.tex: OK · 4/4 citas verificadas
2.1.7_limites_ventaja.tex: OK · 36/36 citas verificadas
2.1.8_imagenes_cuanticas.tex: OK · 18/18 citas verificadas
2.1.9_revision_critica.tex: OK · 21/21 citas verificadas

4/4 fichas pasan.
```
- **Total de citas verificadas:** 79/79 (100 % verificadas contra el texto de los PDF en `Docs/fuentes/txt/`).
- **Fallos:** 0.

### 3.2 Compilación LaTeX con preámbulo real (`compilar_prueba.sh`)

Comando ejecutado:
```bash
bash Docs/capitulos/compilar_prueba.sh 2_Antecedentes
```

**Salida completa:**
```
Compila sin errores. PDF: /var/folders/0p/s82cs_hd6y38lrx5wgk261kr0000gn/T/tmp.SG19Ob0rib/prueba.pdf
Referencias o citas sin resolver:
  ninguna
Cajas desbordadas (Overfull > 10pt):
  ninguna
```
- **Estado de compilación:** Compila sin errores en ambas pasadas de `pdflatex`.
- **Referencias o citas sin resolver:** ninguna.
- **Cajas desbordadas (Overfull > 10pt):** ninguna.

---

## 4. Auditoría de marcas `[VERIFICAR]` y afirmaciones no respaldadas

Durante la ejecución **no fue necesario introducir marcas `[VERIFICAR]`** en los textos visibles, gracias a la exhaustividad de las fichas de lectura verificadas (`Docs/insumos/fichas/`) y los textos originales de los PDF.

### Lista de precisiones críticas y afirmaciones no respaldadas en la literatura:
1. **Radhi et al. (2025) y BreastMNIST (Rifat et al., 2024):** No se evaluaron en el texto visible debido a la ausencia de PDF en el repositorio y falta de clave `\bibitem` verificada; se dejaron exclusivamente comentarios `% PENDIENTE: sin PDF`.
2. **Afirmación de «hasta 5 %» atribuida a Xiang et al. (2024):** Dicha frase textual no aparece en la obra de Xiang et al.; corresponde a un cálculo del autor de la tesis al restar la exactitud en el dataset WDBC. Se reportaron las exactitudes exactas por conjunto (GBSG, SEER y WDBC) y se puntualizó la ausencia de intervalos de confianza.
3. **Exactitud diagnóstica en Azevedo et al. (2022):** El 84 % de exactitud alcanzado por las redes híbridas clásico-cuánticas fue empatado idénticamente por la ResNet clásica con transfer learning (`C+TL`), de modo que no existe ventaja cuántica en exactitud diagnóstica. La ganancia sugerida residió en el AUC (0.77 vs. 0.58 en simulación), la cual no cuenta con intervalos de confianza y descendió al 81 % en el procesador físico `ibm_lagos`. Además, se corrigió el nombre del dataset a *Breast Cancer Data Repository* (BCDR).
4. **Ventaja reportada en El Hafidi et al. (2025):** El artículo trabaja con 15 variables clínicas tabulares (no mamografías). Su mejor modelo cuántico (PauliFeatureMap, 0.96) supera por un único punto porcentual al SVM clásico con RBF (0.95), diferencia que representa menos de un paciente en subconjuntos de prueba de 16 muestras y carece de significación estadística probada.
5. **Complejidad de preparación en FRQI y NEQR:** Se evitó calificar la preparación de FRQI o NEQR como «eficiente» a secas: se explicitó que, aunque cuadrática o lineal en el número de píxeles ($N = 2^{2n}$), la complejidad es estrictamente exponencial en el número de qubits espaciales ($O(2^{4n})$ y $O(q n 2^{2n})$), lo cual imposibilita la codificación directa de mamografías DICOM de alta resolución ($2048 \times 2048$).
