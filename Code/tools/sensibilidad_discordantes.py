"""Cota del efecto de los 7 casos discordantes de M2 sobre el AUC del test (H-020).

Recalcula el AUC del test de masas del análisis principal del M7 con y sin los casos marcados
`crop_check == "discordant"` en Code/results/2_preprocesamiento_qa.csv. Usa las predicciones ya
guardadas (Data/processed/m7/predicciones.parquet) y no reentrena: mide solo el efecto de quitarlos
de la evaluación, no el de los discordantes de train sobre la selección, el escalado y el
entrenamiento. Comprueba además que ninguno esté en la submuestra de 200 del M6 (D-028).

Uso (entorno qml_cancer): python Code/tools/sensibilidad_discordantes.py
Salida: Code/results/2_discordantes_sensibilidad.csv
"""
from pathlib import Path

import pandas as pd
from sklearn.metrics import roc_auc_score

ROOT = Path(__file__).resolve().parents[2]
RES = ROOT / 'Code/results'

qa = pd.read_csv(RES / '2_preprocesamiento_qa.csv')
disc = qa.loc[qa['crop_check'] == 'discordant']
assert len(disc) == 7 and set(disc['finding_type']) == {'mass'}
disc_ids = set(disc['case_id'])

sub = pd.read_csv(RES / '5b_submuestra.csv')
assert not disc_ids & set(sub['case_id']), 'un discordante está en la submuestra del M6'

pred = pd.read_parquet(ROOT / 'Data/processed/m7/predicciones.parquet')
test = pred[(pred['analysis'] == 'main') & (pred['split'] == 'test') & (pred['finding_type'] == 'mass')]
ref = pd.read_csv(RES / '7_test.csv').query("finding_type == 'mass' and analysis == 'main'").set_index('condition')['auc']

rows = []
for cond, g in test.groupby('condition'):
    keep = g[~g['case_id'].isin(disc_ids)]
    auc_all = roc_auc_score(g['label'], g['prob'])
    assert abs(auc_all - ref[cond]) < 1e-12, f'{cond}: no reproduce 7_test.csv'
    auc_keep = roc_auc_score(keep['label'], keep['prob'])
    rows.append({'condition': cond, 'n_test': len(g), 'n_sin_discordantes': len(keep),
                 'auc_test': auc_all, 'auc_sin_discordantes': auc_keep, 'cambio': auc_keep - auc_all})

out = pd.DataFrame(rows)
c1 = out.set_index('condition').loc['C1']
out['brecha_c1'] = c1['auc_test'] - out['auc_test']
out['brecha_c1_sin_discordantes'] = c1['auc_sin_discordantes'] - out['auc_sin_discordantes']
out.to_csv(RES / '2_discordantes_sensibilidad.csv', index=False)
print(f'{len(disc_ids)} discordantes: {sorted(disc["split"].value_counts().items())}; ninguno en la submuestra del M6')
print(out.round(4).to_string(index=False))
