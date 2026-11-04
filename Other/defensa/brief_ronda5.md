# Ronda 5 · «Defensa TT 2026-B039»: estado del arte, pregunta completa y un cierre nuevo

Esta ronda tiene cinco cambios:
1. Una diapositiva nueva con el estado del arte.
2. La pregunta de investigación completa en la diapositiva de la pregunta.
3. Un cierre nuevo: los objetivos cumplidos en tabla y el trabajo futuro como diagrama.
4. Un ajuste menor en la diapositiva del proceso.
5. Los tiempos.

Las reglas de los briefs anteriores siguen vigentes.

**Importante sobre los videos:** no cambies el texto alternativo de las imágenes de los seis videos. Debe seguir empezando con «Video…». El autor vuelve a incrustar los videos en el HTML exportado con un script que localiza esas imágenes por su texto alternativo.

---

## Nuevo orden y tiempos

| # | Diapositiva | Cambio | Tiempo (acumulado) |
|---|---|---|---|
| 1 | Portada | — | 0:15 (0:15) |
| 2 | Contexto | — | 0:40 (0:55) |
| 3 | **NUEVA · Estado del arte** | nueva | 0:50 (1:45) |
| 4 | Pregunta (antes 3) | **pregunta completa** | 0:50 (2:35) |
| 5 | Proceso (antes 4) | quitar la frase de abajo | 1:15 (3:50) |
| 6 | Qubit | — | 1:15 (5:05) |
| 7 | Dos lecturas | — | 1:00 (6:05) |
| 8 | Cinco representaciones | — | 0:45 (6:50) |
| 9 | Concentración | — | 1:45 (8:35) |
| 10 | Separabilidad | — | 1:15 (9:50) |
| 11 | El mismo MLP | — | 1:00 (10:50) |
| 12 | Árboles | — | 1:15 (12:05) |
| 13 | La lectura | — | 1:15 (13:20) |
| 14 | La ventaja sí existe | — | 1:15 (14:35) |
| 15 | X11 | — | 1:20 (15:55) |
| 16 | Viabilidad | — | 1:15 (17:10) |
| 17 | **Objetivos cumplidos** (sustituye a «Respuesta») | nueva | 1:15 (18:25) |
| 18 | **Trabajo futuro** (sustituye a «Limitaciones y trabajo futuro») | nueva | 0:45 (19:10; quedan ~0:50) |

- La parte principal pasa a **18 diapositivas**: actualiza los contadores «n / 18».
- Actualiza el «Tiempo objetivo» y el «acumulado» de todas las notas según la tabla.
- La antigua diapositiva «Respuesta» pasa a respaldo como **C0 · «La respuesta en cinco puntos»**, sin cambios.
- La tabla completa del estado del arte va como respaldo nuevo **A0** (ver abajo).

---

## 3 · NUEVA · «Ningún trabajo previo había combinado codificación cuántica, CBIS-DDSM y análisis de separabilidad»
- Etiqueta de sección: «01 · Contexto».
- **Visual:** una matriz de palomitas, con filas agrupadas en tres bandas con un rótulo gris a la izquierda.
  - Columnas: «Datos» · «Circuito cuántico» · «CBIS-DDSM» · «Analiza separabilidad» · «Masas y calcs. por separado» · «Desempeño».
  - Usa ✓ en verde suave, ✗ en gris claro, «—» para «no aplica» y «Parcial» como texto pequeño.

| Trabajo | Datos | Cuántico | CBIS-DDSM | Separab. | Masas/calcs. | Desempeño |
|---|---|---|---|---|---|---|
| **Aprendizaje profundo en mamografía** | | | | | | |
| Shen et al. (2019) | CBIS-DDSM | ✗ | ✓ | ✗ | ✗ | AUC 0.91 |
| Wang et al. (2020) | DDSM, INbreast, MIAS, UKy | ✗ | Parcial | ✗ | ✗ | AUC 0.88–0.95; externos 0.44–0.65 |
| Baccouche et al. (2022) | CBIS-DDSM, INbreast | ✗ | ✓ | ✗ | ✗ | Exactitud 0.95 |
| **Aprendizaje cuántico fuera de la mamografía** | | | | | | |
| Xiang et al. (2024) | tabulares (GBSG, SEER, WDBC) | ✓ sim. | ✗ | ✗ | — | Exactitud 0.70–0.96 |
| Toufah et al. (2025) | cáncer de pulmón (tabular) | ✓ sim. | ✗ | ✗ | — | Exactitud 0.91–0.96 (RBF 0.95) |
| Parigi et al. (2026) | MNIST, F-MNIST | ✓ sim. | ✗ | ✓ | — | Exactitud 0.94–0.99 |
| **Aprendizaje cuántico en mamografía** | | | | | | |
| Azevedo et al. (2022) | BCDR | ✓ sim. y hardware | ✗ | ✗ | ✗ | AUC 0.77 (clásico 0.58) |
| **Este trabajo** (fila resaltada en azul claro) | CBIS-DDSM | ✓ sim. | ✓ | ✓ | ✓ | AUC masas 0.53/0.58 (C1 0.65); calcs. 0.63/0.65 (C1 0.77) |

- **Debajo de la tabla, una franja** que conecta con Azevedo et al.: «Azevedo et al. (2022) dejaron como trabajo futuro…» y cuatro fichas pequeñas con palomita, «→ este trabajo lo hace»:
  - «separar masas y calcificaciones»;
  - «probar otros conjuntos de datos»;
  - «ver cómo quedan las clases en el espacio de Hilbert»;
  - «probar otras codificaciones».

  Pie: «Azevedo et al. (2022), pp. 12–13».
- **Pasos:** las tres bandas entran una por clic; la fila «Este trabajo» entra después, con un recuadro que abarca sus cuatro palomitas centrales: «la combinación que faltaba». La franja de Azevedo entra al final.
- **Notas:** *Tiempo objetivo: 0:50 (acumulado 1:45).*
  - El aprendizaje profundo ya clasifica mamografías con AUC alrededor de 0.9, pero no usa circuitos cuánticos.
  - Los trabajos cuánticos usan datos tabulares o imágenes sencillas, no mamografías.
  - El único que aplica aprendizaje cuántico a la mamografía, Azevedo et al., no analiza la separabilidad ni separa masas y calcificaciones. En su sección de trabajo futuro proponen cuatro cosas: separar masas y calcificaciones, probar otros conjuntos de datos, ver cómo quedan los datos en el espacio de Hilbert, idealmente como grupos separados, y probar otras codificaciones. Este trabajo parte exactamente de ahí.
  - Ninguno combina las cuatro cosas: un circuito de codificación, el CBIS-DDSM, un análisis explícito de la separabilidad y masas y calcificaciones por separado.
  - Ojo: los desempeños no son comparables entre sí, porque usan datos y métricas distintos. La tabla ubica el trabajo; no lo compite.

## 4 · Pregunta (antes 3): la pregunta completa
- Título: «La pregunta de investigación».
- **La pregunta completa, en grande y en serif**, a todo el ancho y con interlineado amplio:

  > ¿En qué medida las transformaciones cuánticas variacionales implementadas mediante **ZZFeatureMap y PauliFeatureMap** en Qiskit **modifican la separabilidad** de clases benigno/maligno de características radiómicas extraídas de mamografías del CBIS-DDSM, y **hasta qué punto esa diferencia se refleja en la capacidad de clasificación** de una misma red neuronal clásica, en comparación con representaciones clásicas construidas a partir del **mismo vector de características**?

- Las cuatro frases en negritas van además en color: las dos primeras en `C4` (naranja) y las dos últimas en `CLASICO` (azul).
- **Pasos:**
  1. Entra la pregunta completa.
  2. *(paso)* Bajo «modifican la separabilidad» aparece un pequeño «1» en un círculo, y bajo «se refleja en la capacidad de clasificación» un «2»: las dos partes de la pregunta.
- Abajo, igual que hoy: «Objetivo: viabilidad, no superar a una CNN · Simulación ideal (Qiskit Aer)».
- Los dos íconos actuales («¿Cambia la separabilidad?», «¿Se nota al clasificar?») salen: los sustituyen los números 1 y 2.
- El respaldo B0 («La pregunta de investigación completa») se queda como está.
- **Notas:** *Tiempo objetivo: 0:50 (acumulado 2:35).* Esta es la pregunta de investigación. Tiene dos partes. La primera: si la transformación cuántica cambia qué tan separables son las lesiones benignas y malignas. La segunda: si ese cambio se nota cuando la misma red neuronal clasifica sobre cada representación. Todo parte del mismo vector de características, para que la única diferencia sea la transformación. El objetivo es evaluar viabilidad, no superar a una red convolucional, y todo se hizo en simulación ideal.

## 5 · Proceso (antes 4)
- Quita la frase de abajo, «Masas y calcificaciones recorren el camino por separado»: el video ya la trae dentro.

## 17 · NUEVA · «Los seis objetivos se cumplieron»
- Sustituye a «Respuesta». Etiqueta de sección: «05 · Conclusiones».
- **Arriba**, una franja con la respuesta: «**La codificación cuántica no aumentó la separabilidad; la redujo, y la diferencia se nota al clasificar.**»
- **Tabla**, con tres columnas: «Objetivo», «Estado» (una insignia verde «✓ Cumplido» en cada fila) y «Evidencia». Cada fila en un renglón y entra una por clic:

| Objetivo | Estado | Evidencia |
|---|---|---|
| **General:** efecto de la codificación cuántica en la separabilidad y la clasificación | ✓ Cumplido | Sin mayor separabilidad; −0.07 a −0.14 de AUC con el mismo MLP |
| **OE-1** · Pipeline de datos sobre CBIS-DDSM | ✓ Cumplido | 3,568 lesiones, 100 % DICOM; 67 → 12 características; sin fuga entre pacientes |
| **OE-2** · Cinco representaciones del mismo vector | ✓ Cumplido | C1–C5 con k = 12; θ fijo con semilla 42 |
| **OE-3** · Separabilidad con cuatro métricas | ✓ Cumplido | Exceso de KTA 0.003–0.007 frente a 0.049/0.151 del RBF; g = 1.40–1.70 ≪ √N ≈ 14.1 |
| **OE-4** · El mismo MLP en las cinco condiciones | ✓ Cumplido | 12 → 32 → 16 → 1; validación cruzada de 5 folds por paciente |
| **OE-5** · ¿La separabilidad se refleja al clasificar? | ✓ Cumplido | Mismo orden en ambos (ρ = 0.67–0.97): C1–C3 delante de C4–C5 |
| **OE-6** · Viabilidad práctica | ✓ Cumplido | Simulación viable hasta ~25 qubits; en hardware, del 16 al 74 % de los valores del kernel se leerían 0 |

- **Abajo**, la frase de cierre actual: «Un resultado negativo, medido con rigor, es evidencia de viabilidad».
- **Notas:** *Tiempo objetivo: 1:15 (acumulado 18:25).* Respondo la pregunta de investigación: la codificación cuántica no aumentó la separabilidad; la redujo, y la diferencia se nota al clasificar. Los seis objetivos se cumplieron, y conviene subrayarlo: el objetivo era medir, no ganar. (Luego un renglón por objetivo, leyendo solo la evidencia.) Además, el método sí detecta una ventaja cuando existe, como vimos con las etiquetas diseñadas. Un resultado negativo, medido con rigor, es evidencia de viabilidad.

## 18 · NUEVA · «Lo que sigue: de cada limitación, una línea de trabajo»
- Sustituye a «Limitaciones y trabajo futuro». Etiqueta de sección: «06 · Cierre».
- **Visual:** cuatro carriles horizontales. Cada uno tiene un ícono a la izquierda, la limitación observada en gris, una flecha y la línea futura en `TINTA`, en negritas:

| Carril | Lo que se observó | → | Línea de trabajo futuro |
|---|---|---|---|
| 🧭 Codificación | El kernel se concentra a c = 1 | → | **Codificaciones sin concentración**: ancho de banda por característica y conocimiento del problema |
| 🔍 Lectura | 12 valores esperados pierden información | → | **Lecturas intermedias**: correlaciones ⟨ZᵢZⱼ⟩ (66 valores) y lectores más profundos |
| ⚛️ Hardware | Todo fue simulación sin ruido | → | **Procesadores reales**: primero simular con el ruido de un dispositivo, luego medir en uno |
| 🩻 Datos | Un solo conjunto, sin escala física | → | **Mamografía digital con escala conocida** y validación externa |

- Usa íconos de línea propios del deck, no emojis; los de la tabla solo indican el tema.
- **Pasos:** cada carril entra con un clic.
- **Abajo**, como hoy: «Gracias · ¿Preguntas?» y el nombre del autor.
- **Notas:** *Tiempo objetivo: 0:45 (acumulado 19:10; quedan ~0:50 de margen).* Cada limitación del trabajo abre una línea concreta. En la codificación, buscar mapas que no se concentren sin perder la interacción. En la lectura, medir más que 12 valores. En hardware, primero simular con el ruido de un dispositivo real y luego medir en uno: con 200 lesiones, una matriz de kernel exige 19,900 circuitos. Y en datos, repetir el estudio con mamografía digital con escala física y validación externa. Muchas gracias; quedo atento a sus preguntas.

---

## Respaldos nuevos

**A0 · «Estado del arte: la tabla completa»** (al inicio de la familia A)
- La tabla de la diapositiva 3 con cuatro columnas más, P1 a P4: paridad, incertidumbre, partición de prueba y simulabilidad. Solo aplican a los trabajos cuánticos.

| Trabajo | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| Xiang et al. (2024) | Parcial | No | No | No |
| Toufah et al. (2025) | Sí | No | ND | No |
| Parigi et al. (2026) | Sí | Sí | Sí | No |
| Azevedo et al. (2022) | Parcial | No | No | No |
| Este trabajo | Sí | Sí | Sí | No |

- Pie: «P1 paridad: el clásico recibe los mismos datos y ajuste · P2 incertidumbre reportada · P3 conjunto de prueba usado una vez · P4 circuito difícil de simular · ND: el trabajo no lo dice».
- **Notas:** ningún trabajo cuántico, incluido este, usa un circuito difícil de simular clásicamente (P4). Este trabajo cumple paridad, incertidumbre y partición de prueba.

**C0 · «La respuesta en cinco puntos»**: la antigua diapositiva 16, sin cambios.

Actualiza el índice R0 con A0 y C0.

---

## Comprobación final antes de exportar
- [ ] 18 diapositivas principales con contadores «n / 18»; respaldos A0 y C0 añadidos y en el índice.
- [ ] Las imágenes de los seis videos conservan su texto alternativo, que empieza con «Video…».
- [ ] La diapositiva 4 muestra la pregunta completa y legible, sin cortar.
- [ ] La tabla de objetivos cabe completa y cada fila ocupa un renglón.
- [ ] Las cifras son exactamente las de este documento.
- [ ] Tiempos de todas las notas según la tabla.
