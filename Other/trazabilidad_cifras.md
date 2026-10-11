# Trazabilidad de cifras · TT 2026-B039

> Resultado de `Code/tools/trazabilidad_cifras.py` (2026-10-11) sobre la bitácora (D-020 en adelante, H-020 en adelante) y `Docs/borrador_secciones_4.md`, más la revisión a mano de las cifras que el script no pudo confirmar. La tabla completa, cifra por cifra y con su contexto, está en `Other/trazabilidad_cifras.csv`. Para repetirlo después de editar la bitácora: `python Code/tools/trazabilidad_cifras.py`.

## Resultado

**Un solo error de cifra en toda la bitácora.**
- **H-039** dice 0.152 para el exceso de KTA del RBF en calcificaciones, en la tabla (línea 1782) y en la lectura 4 (línea 1798).
- `6_alineamiento_kernel.csv` da 0.151451, es decir **0.151**, que es lo que dice H-041.
- Está anotado en `correcciones_verificadas.md`.

**Errores de referencia, no de cifra.** Dos entradas citan en su línea **Datos.** un archivo que no contiene sus cifras:
- **H-027:** las cifras de balance de los folds (0.038, 0.060, 0.011, 0.168, 0.065 y 0.019) están en `4_semilla_folds.csv`, no en `4_folds.csv`.
- **H-045:** las cifras del test (0.649, 0.787, 0.795 [0.73, 0.85], −0.05 [−0.10, 0.00], +0.008 y +0.02 [−0.02, 0.06]) están en `X4_test.csv` y `X4_test_diferencias.csv`, no solo en `X4_67_features.csv`.

## Cómo funciona y qué tanto prueba

El script extrae los 846 números con decimales de 48 entradas (hasta H-054) y los busca **solo en los CSV que cita la propia entrada**.

Buscar en todos los CSV no sirve. Con más de 100,000 valores, un número cualquiera de 2 o 3 decimales coincide con alguno por azar; se midió con números aleatorios y coinciden el 99–100 % de las veces. Por la misma razón, una coincidencia solo con un archivo citado muy grande (más de 2,000 valores) tampoco prueba nada.

| Estado | Cifras | Qué significa |
|---|---|---|
| OK | 172 | Coincide con un archivo citado pequeño y difícilmente por azar: los vecinos de la cifra no coinciden |
| DEBIL | 375 | Coincide con un archivo citado, pero una cifra vecina también coincidiría (o tiene un solo decimal). Probablemente bien, sin prueba fuerte |
| SOLO_ARCHIVO_GRANDE | 24 | Solo coincide con un archivo citado de más de 2,000 valores. **Revisadas a mano: 23 están bien y 1 es el error de H-039** |
| REDONDEO | 17 | Difiere en una unidad del último decimal de un valor del archivo citado. Revisadas por grupos: son umbrales (0.95, 0.99) o cifras que sí cuadran con otra columna |
| NO_ENCONTRADO | 64 | La entrada cita CSV y la cifra no está en ellos. Ver la tabla siguiente |
| SIN_CSV_CITADO | 194 | La entrada no cita ningún CSV (casi todas las D y el borrador): no verificable automáticamente |

## Revisión a mano de NO_ENCONTRADO y REDONDEO

| Entrada | Cifras | Resultado |
|---|---|---|
| H-020 | rangos 0.8700–0.8704, 0.997–1.014, 1.003–1.011; 99.8 % | **Correctas**: se recalcularon de las columnas de `2_preprocesamiento_qa.csv` (3,206 / 3,213 = 99.8 %). La tabla de control (0.950, 0.993, 4.3 px…) sale de la salida del notebook y no está en un CSV; **sin verificar**. 0.870 = 43.5/50 es la hipótesis del texto, no una cifra medida |
| H-021 | 86.3 %, ≥ 99.55 %, 0.45 %, 3.6, 9.2 y 14 px | **Correctas**, recalculadas de `2_preprocesamiento_qa.csv` |
| H-023 | 1.42 | Es la cifra antigua de H-003 que la entrada corrige; no es un resultado actual |
| H-024 | 0.95, 0.99 | Umbrales de correlación, no resultados |
| H-025 | 0.879, 0.860, 0.881, −0.054, −0.035, −0.002 | **Correctas**: medianas por familia de `3_efecto_clahe.csv` |
| H-027 | seis cifras de balance de folds | **Correctas**, pero están en `4_semilla_folds.csv` (ver arriba) |
| H-035 | R² (0.44, 0.45, 0.56), diferencias −0.007 a −0.002, 0.006 | Salen de la salida del notebook X1; **sin verificar** |
| H-036 | 0.505, 0.088, 0.515, 0.042 | Son del C5 original `['X','ZZ']`, anterior a D-031; los CSV actuales ya no los contienen. Conviene marcarlas en el texto como cifras de la versión anterior. Las medianas por par (0.583, 0.652, 0.663) y los márgenes quedan **sin verificar** |
| H-037 | 0.046 | Del C5 original; mismo caso que H-036 |
| H-041 | 0.47 → 0.45, 0.29 → 0.38 | Cocientes C5/C1 derivados; sin verificar |
| H-043 | 0.533, 0.557, 0.596, 0.631, 0.680; 0.581 → 0.603, 0.652 → 0.682; 0.561 | **Correctas**: `7_cv_resumen.csv` (`config fixed`) y `7_test.csv` (`reps2`, `k8`). Las dispersiones 0.058 / 0.180 coinciden con X7 |
| H-045 | 0.649, 0.787, 0.795 [0.73, 0.85], −0.05 [−0.10, 0.00], +0.008, +0.02 | **Correctas**, en `X4_test.csv` y `X4_test_diferencias.csv` (ver arriba) |
| H-050 | 0.002–0.003, 0.00003 | Medianas del kernel; ya verificadas en H-031 y H-037 |
| H-051 | 1.9, 5.4 | Cocientes de tiempos, derivados |
| H-053, H-054 | 0.612, 0.759, 0.701, 1.4 ms, 3.4 min | **Correctas**: una media de folds, dos valores de `X4_test.csv` y conversiones de unidades de `X8_costo_gradiente.csv` |
| D-022 | 5.31, 2.17 GB | 5.306 en `2_preprocesamiento_qa.csv`; el tamaño en disco no está en un CSV |

## Lo que queda

- **194 cifras SIN_CSV_CITADO**, casi todas en las D y en el borrador. En su mayoría repiten cifras de las H, que sí se revisaron, pero no se cruzaron una por una.
- **332 DEBIL.** Coinciden con su archivo citado, pero sin prueba fuerte.
- **Antes del 19 de octubre**, tras editar la bitácora o el reporte, volver a correr el script y revisar las cifras que salgan nuevas en REDONDEO, NO_ENCONTRADO o SOLO_ARCHIVO_GRANDE.
