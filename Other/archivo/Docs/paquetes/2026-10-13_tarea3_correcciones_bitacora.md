# Tarea 3 · Propuesta de correcciones a la bitácora

> Para aprobar de una lectura. **Nada de esto está aplicado.** Responde «apruebo todo» o indica los números
> que cambias o descartas. Al aprobarlo, lo aplico tal cual, vuelvo a correr
> `Code/tools/trazabilidad_cifras.py` y `Code/tools/tablas_latex.py` y hago un solo commit.
> Cada cifra nueva se comprobó contra su CSV la noche del 12 al 13 de octubre.

---

## A · Las que pediste

### 1. H-039 · 0.152 → 0.151 (dos lugares)

`6_alineamiento_kernel.csv`, fila `calcification, K_C`: `excess_centered = 0.15145057910610307`.

- **Línea 1794 (tabla).** `| Exceso de KTA centrada sobre la permutación, RBF (D-027) | 0.049 | 0.152 |`
  → `… | 0.049 | 0.151 |`
- **Línea 1810 (lectura 4).** «(contra 0.049 y 0.152 del RBF)» → «(contra 0.049 y 0.151 del RBF)»

CLAUDE.md ya lo advierte («H-039 dice 0.152 por un redondeo»). Al corregirlo, esa nota se quita de CLAUDE.md.

### 2. H-027 · línea «Datos.» (línea 1464)

Las cifras de balance (0.038, 0.060, 0.011, 0.168, 0.065, 0.019) están en `4_semilla_folds.csv` (columnas
`max_dev_seed_42`, `max_dev_median`, `max_dev_chosen`), no en `4_folds.csv`.

- **Hoy:** ``**Datos.** `Code/4_Selection_and_Scaling.ipynb` §5; `Code/results/4_folds.csv`.``
- **Propuesta:** ``**Datos.** `Code/4_Selection_and_Scaling.ipynb` §5; `Code/results/4_semilla_folds.csv` (balance de los folds por semilla) y `4_folds.csv` (asignación de cada lesión).``

### 3. H-045 · línea «Datos.» (línea 1978)

Las cifras del test (0.649, 0.787, 0.795 [0.73, 0.85], −0.05 [−0.10, 0.00], +0.008, +0.02 [−0.02, 0.06]) están
en `X4_test.csv` y `X4_test_diferencias.csv`.

- **Propuesta:** añadir `` `X4_test.csv` y `X4_test_diferencias.csv` `` después de `X4_67_features.csv`.

### 4. H-043 · redacción de k = 8 (línea 1923)

`7_test_diferencias.csv`, fila `calcification, C4 (k8) - C4 (main)`: −0.069899 [−0.140711, **+0.000499**],
`share_above_0 = 0.0255`. El intervalo toca el cero.

- **Hoy:** «C4 empeora en calcificaciones: 0.561 en el test, con una diferencia de −0.07 [−0.14, 0.00] frente a k = 12.»
- **Propuesta:** «C4 tiende a empeorar en calcificaciones: 0.561 en el test, con una diferencia de −0.070 [−0.141, +0.0005] frente a k = 12; el intervalo llega al cero.»

### 5. H-048 · alcance de «propiedad de la tarea»

**Ojo: la redacción que sugiere `correcciones_verificadas.md` (§5) está mal.** Dice «ZZ, Y-ZZ y proyectados»,
pero `X6_rejilla_candidatos.csv` no tiene ningún kernel Y-ZZ. Las familias cuánticas de X6 son ZZ con
entrelazamiento completo y lineal, con 1 y 2 repeticiones, y los kernels proyectados de ambos. Las etiquetas
construidas (`X6_etiquetas_construidas.csv`) se probaron con ZZ completo, ZZ lineal y proyectado (ZZ completo).

- **Título (índice, línea 118, y encabezado, línea 2035).** «…: la ausencia de ventaja es una propiedad de la tarea»
  → «…: la ausencia de ventaja es una propiedad de estas etiquetas, no del protocolo»
- **Impacto (línea 2055).** «La ausencia de ventaja es una propiedad de la tarea, medida y no supuesta, y el mismo protocolo detecta una ventaja cuando existe.»
  → «La ausencia de ventaja es una propiedad de la tarea tal como se planteó: estas etiquetas, estas 12 features y las familias de kernels probadas (mapas ZZ con entrelazamiento completo o lineal, una o dos repeticiones, y sus kernels proyectados). Está medida, no supuesta, y el mismo protocolo detecta una ventaja cuando las etiquetas siguen la geometría del kernel cuántico.»
- **También en `correcciones_verificadas.md` §5:** corregir «(ZZ, Y-ZZ y proyectados)» por la lista de arriba.

C5 = (Y, ZZ) sí se evaluó con QSVM en X4 (H-044) y queda por debajo del RBF, pero no entró en la búsqueda de X6
ni en las etiquetas construidas.

### 6. «Preregistrado» → «fijado de antemano»

No hubo un registro público, así que «preregistrado» promete más de lo que hubo. Las 10 apariciones:

| Línea | Hoy | Propuesta |
|---|---|---|
| 54 (índice D-029) | «se mantiene el diseño preregistrado» | «se mantiene el diseño fijado de antemano» |
| 539 (título D-029) | «diseño preregistrado más barrido» | «diseño fijado de antemano más barrido» |
| 547 | «Mantener el diseño preregistrado (c = 1)» | «Mantener el diseño fijado de antemano (c = 1)» |
| 740 | «El diseño preregistrado no mostró ventaja» | «El diseño fijado de antemano no mostró ventaja» |
| 1715, 1722, 1813, 1879, 1907 | «con el diseño preregistrado» | «con el diseño fijado de antemano» |
| 2391 (Q-011) | «mantener el diseño preregistrado (c = 1)» | «mantener el diseño fijado de antemano (c = 1)» |

**Fuera de la bitácora** (dime si también los cambio):
- `Other/plan_trabajo.html`: 3 apariciones; mismo cambio.
- Notebooks: «preregistered» aparece en celdas **markdown** de 5b, 6, 7, 8, X2, X3, X4 y X6 (19 en total).
  Cambiarlas por «pre-specified» no altera ninguna salida. Además hay 6 en celdas de código y una en una
  salida de X4: **no las tocaría**, porque cambiar código obliga a re-ejecutar para que la salida coincida.

### 7. H-036 y H-037 · cifras del C5 anterior

**Ya están rotuladas** como del C5 original: H-036 dice «Con el C5 original, un mapa solo ZZ, eran 0.505
(p = 0.088)…», y H-037 tiene filas «C5 original (`['X','ZZ']`)». Lo que falta es decir que **ya no están en los
CSV**, porque la trazabilidad las marca como no encontradas.

- **H-036, al final de «Actualizado el 2026-10-05 (D-031)»** añadir: «Esas cifras son de la corrida anterior a D-031 y ya no están en `X2_auc_pares.csv`.»
- **H-037, línea «Datos.»** añadir: «Las filas del C5 original vienen de la corrida anterior a D-031; los CSV actuales solo tienen el C5 con `['Y','ZZ']`.»

### 8. H-054 → D-014 y H-015 · el costo vale para el hardware

Cifras de `X8_costo_gradiente.csv`: *parameter-shift* 5.159 s por lesión y 205.2 h por 50 épocas sobre todo el
train, con un mapa; retropropagación de una pérdida escalar 0.00142 s por lesión y 0.0565 h (3.4 min). El
cociente es ~3,600.

- **D-014, al final de «Por qué», punto 1 (Coste):**
  > **Matizado el 2026-10-11 (H-054).** La razón de costo vale para los gradientes que puede producir un
  > computador cuántico. En el simulador, la retropropagación a través del vector de estado da el mismo
  > Jacobiano (diferencia 1.8×10⁻¹⁵) y es unas 3,600 veces más barata: 50 épocas costarían ~3.4 min en lugar
  > de ~205 h. Ese atajo no existe en hardware. Las razones 2 y 3 no dependen del costo y se sostienen.
- **H-015, al final de «Impacto»:**
  > **Matizado el 2026-10-11 (H-054).** «Ningún método rescata la Arquitectura A» vale para los métodos que
  > usan solo mediciones del circuito, es decir, *parameter-shift*, SPSA y PSO. La retropropagación sobre el
  > vector de estado sí la haría asequible en simulación (~3.4 min por 50 épocas), pero no existe en hardware.

> **Concepto, para defenderlo.** La retropropagación (modo inverso) obtiene el gradiente de una pérdida
> **escalar** respecto a todos los parámetros con un solo paso hacia atrás, sin importar cuántos parámetros haya.
> El *parameter-shift* necesita dos evaluaciones del circuito por parámetro: el gradiente sale de mediciones del
> circuito con el parámetro desplazado ±π/2. La retropropagación necesita las 4,096 amplitudes del estado, que un
> computador cuántico nunca entrega, porque medir colapsa el estado. Por eso una es una propiedad del
> **formalismo** que funciona en hardware, y la otra un privilegio del **simulador**.

---

## B · Encontradas esta noche (no estaban en la lista)

### 9. D-011 · el encabezado contradice al índice

El índice (línea 36) dice «Firme (2026-09-22)», pero el encabezado de la entrada (línea 229) dice
`**Estado:** Provisional`, y su texto «**Decisión provisional.**».

- **Propuesta:** encabezado → `**Estado:** Firme (2026-09-22)`; «**Decisión provisional.**» → «**Decisión.**».

### 10. H-002 · ampliar de 25 mamografías a todas

H-002 se midió sobre 25 mamografías. Esta noche lo comprobé sobre las **3,103 mamografías distintas** (los 3,568
registros comparten imágenes): ninguna trae `PixelSpacing`, `ImagerPixelSpacing` ni `Manufacturer`, y todas son
MG, 16 bits y MONOCHROME2. La etiqueta `Manufacturer` **no existe**; el «UNKNOWN» del EDA y de §5.4 del reporte
era un relleno.

- **Propuesta, al final de H-002:**
  > **Ampliado el 2026-10-13 a todo el dataset.** Sobre las 3,103 mamografías distintas, ninguna trae
  > `PixelSpacing`, `ImagerPixelSpacing` ni `Manufacturer`; las tres etiquetas faltan, no valen «UNKNOWN».
  > Todas son MG, de 16 bits y MONOCHROME2. §5.4 debe decir que la etiqueta falta.
  > **Datos.** `Code/tools/verificar_metadatos_dicom.py`; `Code/results/1_metadatos_dicom.csv`.

### 11. D-009 · el rango de tamaños mezcla dos lesiones

D-009 (cifras del 2026-09-23) dice «entre 33×33 y 3801×2873 px en calcificaciones». 3,801 es el alto máximo y
2,873 el ancho máximo, **de lesiones distintas**. La caja más grande mide 3,777×2,753 (`2_preprocesamiento_qa.csv`,
`bbox_h × bbox_w`). En masas no pasa: la mayor sí es 1,329×1,365.

- **Propuesta:** «… y entre 33×33 y 3,777×2,753 px en calcificaciones (mediana 273×289); el alto llega a 3,801 y el ancho a 2,873 en lesiones distintas».
- `Docs/borrador_secciones_4.md` §4.4 repite «3,801×2,873»; el paquete del lunes ya usa la cifra corregida.

### 12. `trazabilidad_cifras.md` · dos conteos de DEBIL

La tabla dice 375 cifras DEBIL y «Lo que queda» dice 332. Se resuelve solo al volver a correr el script y
rehacer el resumen.

### 13. H-037 · 0.057 para la dispersión de C4 en masas (menor)

`5a_resumen.csv` da 0.056497 sobre todas las lesiones (0.056 a tres decimales); sobre el train, 0.0579
(`X3_comparacion_k8_k12.csv`), y sobre la submuestra de 200, 0.0590. El 0.057 de H-037 (y de la tabla de H-041)
no coincide con ninguna a tres decimales. **Propuesta:** en H-037, «0.057» → «0.056», añadiendo «(todas las
lesiones)» al rótulo de la fila; en H-041, «0.057» → «0.058 (train)», si esa tabla usa el train. Si prefieres no
tocarlo, basta con citar en §6 la cifra del CSV con su población.
