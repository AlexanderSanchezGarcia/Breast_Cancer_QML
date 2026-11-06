# Datos del clip roc_umbral (ronda 7): las predicciones reales del MLP en el conjunto de prueba de
# masas para C1 y C4, las mismas de la Fig. 6.3.2 y de la diapositiva de las curvas ROC.
# El AUC de cada condición se comprueba contra Code/results/7_test.csv.
# Se corre una vez con el entorno qml_cancer:
#   /opt/anaconda3/envs/qml_cancer/bin/python Other/defensa/manim/preparar_datos_roc.py
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score, roc_curve

RAIZ = Path(__file__).resolve().parents[3]
SALIDA = Path(__file__).resolve().parent / 'datos'

pred = pd.read_parquet(RAIZ / 'Data/processed/m7/predicciones.parquet')
test = pd.read_csv(RAIZ / 'Code/results/7_test.csv').query("analysis == 'main'").set_index(['finding_type', 'condition'])

arrays, resumen = {}, {}
for c in ['C1', 'C4']:
    p = pred.query("analysis == 'main' and split == 'test' and finding_type == 'mass' and condition == @c")
    p = p.sort_values('case_id' if 'case_id' in p.columns else p.columns[0]).reset_index(drop=True)
    y, s = p['label'].to_numpy(int), p['prob'].to_numpy(float)
    auc = roc_auc_score(y, s)
    fila = test.loc[('mass', c)]
    assert abs(auc - fila['auc']) < 1e-9, (c, auc, fila['auc'])
    fpr, tpr, umbral = roc_curve(y, s, drop_intermediate=False)
    arrays[f'{c}_label'], arrays[f'{c}_prob'] = y, s
    arrays[f'{c}_fpr'], arrays[f'{c}_tpr'], arrays[f'{c}_umbral'] = fpr, tpr, umbral
    resumen[c] = {'auc': float(auc), 'ic95': [float(fila['auc_ci_low']), float(fila['auc_ci_high'])],
                  'n_lesiones': int(len(y)), 'n_malignas': int(y.sum()), 'n_benignas': int((y == 0).sum())}

np.savez_compressed(SALIDA / 'roc_prueba_masas.npz', **arrays)
json.dump(resumen, open(SALIDA / 'roc_prueba_masas.json', 'w', encoding='utf-8'), indent=1)
print(json.dumps(resumen, indent=1))
