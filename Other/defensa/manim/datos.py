# Acceso a los datos reales de las escenas. Las escenas toman TODAS sus cifras de aquí:
# ninguna escena escribe un número del trabajo a mano.
# Los archivos de datos/ los genera preparar_datos.py a partir de Data/ y Code/results/.
import json
from pathlib import Path

import numpy as np
import pandas as pd

_DIR = Path(__file__).resolve().parent / 'datos'
_RES = json.load(open(_DIR / 'resumen.json', encoding='utf-8'))


def kernel(nombre):
    """Matriz 40x40 de 40 lesiones de masas: 20 benignas (índices 0-19) y 20 malignas (20-39).
    nombre: 'RBF', 'C5' o 'C4_c<c>' con c en c_valores(), p. ej. 'C4_c1.0' o 'C4_c0.02'."""
    return np.load(_DIR / 'kernels_40_masas.npz')[nombre]


def c_valores():
    """Escalas angulares del barrido, de mayor a menor: [1.0, 0.5, 0.2, 0.1, 0.05, 0.02]."""
    return list(_RES['c_valores'])


def mediana_kernel(nombre):
    """Mediana fuera de la diagonal sobre las 200 lesiones de masas del M6 (la cifra que se reporta)."""
    return _RES['medianas_kernel_200'][nombre]


def lesion():
    """Una lesión real de masas: 'x' (sus 12 ángulos en [0, pi]), 'z_c4' (sus 12 <Z_i> en C4)
    y 'kernel_c4_con_otra' (su valor de kernel C4 con otra lesión real)."""
    return dict(_RES['lesion'])


def estado_lesion():
    """Estado real tras el feature map de C4 (sin ansatz) de la lesión de lesion() ('_a') y de la otra ('_b').
    'prob_*': las 4,096 probabilidades, que valen TODAS exactamente 1/4096 (no distinguen lesiones).
    'fase_*': las 4,096 fases en (-pi, pi], relativas a la componente |0...0>: ahí está la información.
    La fidelidad es |media(exp(i(fase_a - fase_b)))|^2 = lesion()['kernel_c4_con_otra']."""
    d = np.load(_DIR / 'estado_lesion.npz')
    return {k: d[k] for k in ('prob_a', 'prob_b', 'fase_a', 'fase_b')}


def x11():
    """Curva de X11, kernel proyectado en masas: columnas alpha, quantum_auc, classical_auc,
    difference, ci_low, ci_high, quantum_wins (IC 95 % de la diferencia por encima de 0)."""
    return pd.read_csv(_DIR / 'x11_masas_proyectado.csv')


def x11_umbral():
    """alpha* por subconjunto y kernel: claves 'mass|ZZ full (C4)', 'calcification|Projected (ZZ full)', etc."""
    return dict(_RES['x11_umbral'])


def disparos():
    """Kernel con 1,024 disparos a c = 1. Claves 'mass_C4', 'calcification_C5', etc.:
    'mediana' (valor típico del kernel) y 'lee_cero_1024' (fracción de pares que se leen exactamente 0)."""
    return dict(_RES['disparos'])


def pipeline():
    """Conteos del trabajo (lesiones, pacientes, masas, calcificaciones, entrenamiento, prueba,
    caracteristicas, seleccionadas) y los nombres de las 12 características de cada subconjunto."""
    return dict(_RES['pipeline'])


def roc_prueba(condicion):
    """Predicciones reales del MLP en el conjunto de prueba de masas (Fig. 6.3.2), condicion 'C1' o 'C4'.
    'label' (0 benigna, 1 maligna) y 'prob' (probabilidad de maligno que da el MLP), una por lesión;
    'fpr', 'tpr' y 'umbral': la curva ROC completa de sklearn (fpr = 1 - especificidad, tpr = sensibilidad);
    'auc', 'ic95', 'n_lesiones', 'n_malignas', 'n_benignas'. El AUC está comprobado contra 7_test.csv."""
    d = np.load(_DIR / 'roc_prueba_masas.npz')
    r = json.load(open(_DIR / 'roc_prueba_masas.json', encoding='utf-8'))[condicion]
    r.update({k: d[f'{condicion}_{k}'] for k in ('label', 'prob', 'fpr', 'tpr', 'umbral')})
    return r
