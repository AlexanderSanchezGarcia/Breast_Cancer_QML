"""Tiempo de las transformaciones clásicas C2 (PCA) y C3 (Kernel PCA RBF) del Módulo 5.

El notebook 5a_Embeddings solo cronometra C4 y C5 y registra 0 s para C1-C3 sin medirlos.
Este script repite exactamente las mismas llamadas de la celda 15 (ajuste en train, transformación
de todas las lesiones), toma la mediana de cinco repeticiones y comprueba que el resultado coincide
con Data/processed/m5/emb_<finding_type>.parquet. C1 es la identidad y no tiene costo.

Salida: Code/results/5a_tiempos_clasicos.csv
"""
import time
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.decomposition import KernelPCA, PCA
from sklearn.metrics import pairwise_distances

SEED, REPS = 42, 5
ROOT = Path(__file__).resolve().parents[2]
X_COLUMNS = [f'x_{i:02d}' for i in range(1, 13)]


def median_gamma(x_train):
    sq = pairwise_distances(x_train, metric='sqeuclidean')
    return 1.0 / (2.0 * np.median(sq[np.triu_indices_from(sq, k=1)]))


def c2(x, train):
    return PCA(n_components=12, random_state=SEED).fit(x[train]).transform(x)


def c3(x, train):
    return KernelPCA(n_components=12, kernel='rbf', gamma=median_gamma(x[train])).fit(x[train]).transform(x)


rows = []
for ft in ['mass', 'calcification']:
    frame = pd.read_parquet(ROOT / f'Data/processed/m4/x_{ft}.parquet')
    stored = pd.read_parquet(ROOT / f'Data/processed/m5/emb_{ft}.parquet')
    x = frame[X_COLUMNS].to_numpy(float)
    train = frame.split.eq('train').to_numpy()
    for name, fn in (('C2', c2), ('C3', c3)):
        times = []
        for _ in range(REPS):
            start = time.perf_counter()
            out = fn(x, train)
            times.append(time.perf_counter() - start)
        ref = stored[[f'{name}_{i:02d}' for i in range(1, 13)]].to_numpy(float)
        rows.append({'finding_type': ft, 'condition': name, 'n_lesions': len(frame), 'repetitions': REPS,
                     'seconds_median': float(np.median(times)), 'seconds_min': float(np.min(times)),
                     'max_abs_diff_vs_stored': float(np.abs(out - ref).max())})

result = pd.DataFrame(rows)
result.to_csv(ROOT / 'Code/results/5a_tiempos_clasicos.csv', index=False)
print(result.to_string(index=False))
