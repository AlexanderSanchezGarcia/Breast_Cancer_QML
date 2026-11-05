# Datos verificados para las diapositivas nuevas de la ronda 6 del deck (separabilidad de las
# representaciones, curvas ROC y tabla resumen). Claude Design no lee el repositorio: este script
# escribe Other/defensa/datos_ronda6.json, que el autor adjunta junto con el brief.
#
# Uso (entorno qml_cancer):
#   /opt/anaconda3/envs/qml_cancer/bin/python Other/defensa/datos_ronda6.py
#
# Fuentes:
# - Curvas ROC: Data/processed/m7/predicciones.parquet (análisis main, split test), las mismas
#   predicciones de la Fig. 6.3.2; el AUC de cada curva se comprueba contra Code/results/7_test.csv.
# - Davies-Bouldin, Fisher y alineamiento lineal: Code/results/6_metricas_embedding.csv (submuestra
#   de 200, la de la Fig. 6.2.4), con la banda del 95 % de las 1,000 permutaciones de etiquetas.
# - t-SNE: recalculado con el mismo código y la misma semilla que la celda de la Fig. 6.2.5 en
#   Code/6_Separability.ipynb (perplejidad 30, init PCA, random_state 42).
# - Tabla resumen: los mismos CSV que Docs/tablas/resumen_resultados.tex (Tabla 23 del reporte).
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
from sklearn.metrics import roc_auc_score, roc_curve

ROOT = Path(__file__).resolve().parents[2]
RES = ROOT / 'Code/results'
M5 = ROOT / 'Data/processed/m5'
SALIDA = Path(__file__).resolve().parent / 'datos_ronda6.json'
FT = {'mass': 'masas', 'calcification': 'calcificaciones'}
COND = ['C1', 'C2', 'C3', 'C4', 'C5']
r3 = lambda v: None if v is None or pd.isna(v) else round(float(v), 3)

# --- Curvas ROC en prueba (Fig. 6.3.2) ---
pred = pd.read_parquet(ROOT / 'Data/processed/m7/predicciones.parquet')
test = pd.read_csv(RES / '7_test.csv').query("analysis == 'main'").set_index(['finding_type', 'condition'])
roc = {}
for ft, nombre in FT.items():
    roc[nombre] = {}
    for c in COND:
        p = pred.query("analysis == 'main' and split == 'test' and finding_type == @ft and condition == @c")
        auc = roc_auc_score(p['label'], p['prob'])
        assert abs(auc - test.loc[(ft, c), 'auc']) < 1e-9, (ft, c, auc)
        fpr, tpr, _ = roc_curve(p['label'], p['prob'], drop_intermediate=True)
        roc[nombre][c] = {
            'auc': r3(auc), 'ic95': [r3(test.loc[(ft, c), 'auc_ci_low']), r3(test.loc[(ft, c), 'auc_ci_high'])],
            'n_lesiones': int(len(p)), 'n_malignas': int(p['label'].sum()),
            'fpr': [round(float(v), 4) for v in fpr], 'tpr': [round(float(v), 4) for v in tpr],
        }

# --- Métricas sobre las representaciones vectoriales (Fig. 6.2.4) ---
emb = pd.read_csv(RES / '6_metricas_embedding.csv').query("sample == 'subsample'")
metricas = {}
for ft, nombre in FT.items():
    metricas[nombre] = {}
    for _, r in emb[emb['finding_type'] == ft].iterrows():
        metricas[nombre][r['condition']] = {
            'davies_bouldin': r3(r['davies_bouldin']), 'db_banda95_permutacion': [r3(r['db_null_p025']), r3(r['db_null_p975'])], 'p_db': r3(r['p_db']),
            'fisher_j': r3(r['fisher_j']), 'fisher_banda95_permutacion': [r3(r['fj_null_p025']), r3(r['fj_null_p975'])], 'p_fisher': r3(r['p_fisher']),
            'kta_lineal': r3(r['kta_linear']), 'kta_lineal_banda95_permutacion': [r3(r['la_null_p025']), r3(r['la_null_p975'])], 'p_kta_lineal': r3(r['p_kta_linear']),
        }

# --- t-SNE (Fig. 6.2.5), mismo código que la celda 29 del notebook 6 ---
tsne = {}
for ft, nombre in FT.items():
    z = np.load(M5 / f'kernels_{ft}.npz', allow_pickle=True)
    case_id, y01 = z['case_id'].astype(str), z['label'].astype(int)
    sub = pd.read_parquet(M5 / f'emb_{ft}.parquet').set_index('case_id').loc[case_id]
    assert np.array_equal(sub['label'].to_numpy(), y01)
    tsne[nombre] = {'clase': [int(v) for v in y01], 'clase_leyenda': {'0': 'benigna', '1': 'maligna'},
                    'n_benignas': int((y01 == 0).sum()), 'n_malignas': int((y01 == 1).sum())}
    for c in COND:
        x = sub[[f'{c}_{i:02d}' for i in range(1, 13)]].to_numpy(float)
        proj = TSNE(n_components=2, perplexity=30, init='pca', learning_rate='auto', random_state=42).fit_transform(x)
        proj = (proj - proj.min(0)) / (proj.max(0) - proj.min(0))   # normalizado a [0, 1] para dibujar
        tsne[nombre][c] = [[round(float(a), 3), round(float(b), 3)] for a, b in proj]

# --- Tabla resumen (Tabla 23 del reporte) ---
kta = pd.read_csv(RES / '6_alineamiento_kernel.csv')
deff = pd.read_csv(RES / '6_dimension_efectiva.csv')
gdf = pd.read_csv(RES / '6_diferencia_geometrica_resumen.csv')
cv = pd.read_csv(RES / '7_cv_resumen.csv').query("analysis == 'main'").set_index(['finding_type', 'condition'])
x4 = pd.read_csv(RES / 'X4_test.csv').set_index(['finding_type', 'model'])
tabla = {}
for ft, nombre in FT.items():
    filas = []
    for c in COND:
        kernel = {'C3': ('K_C', None), 'C4': ('C4', 1.0), 'C5': ('C5', 1.0)}.get(c)
        f = {'condicion': c, 'exceso_kta': None, 'd_eff': None, 'g': None}
        if kernel:
            k, cc = kernel
            sel = lambda d: d[(d['finding_type'] == ft) & (d['kernel'] == k) & (d['c'].isna() if cc is None else d['c'] == cc)]
            f['exceso_kta'] = r3(sel(kta)['excess_centered'].iloc[0])
            f['d_eff'] = round(float(sel(deff)['effective_dimension'].iloc[0]), 1)
            if cc:
                f['g'] = r3(gdf[(gdf['finding_type'] == ft) & (gdf['map'] == k) & (gdf['c'] == 1.0)]['g_min'].iloc[0])
        m = metricas[nombre][c]
        f.update({'davies_bouldin': m['davies_bouldin'], 'fisher_j': m['fisher_j'],
                  'auc_vc': r3(cv.loc[(ft, c), 'auc_mean']), 'auc_prueba': roc[nombre][c]['auc'], 'auc_prueba_ic95': roc[nombre][c]['ic95']})
        filas.append(f)
    for modelo, etiqueta in [('SVM RBF (D-027)', 'SVM sobre el kernel RBF'), ('QSVM C4, c = 1', 'QSVM sobre el kernel de C4'), ('QSVM C5, c = 1', 'QSVM sobre el kernel de C5')]:
        r = x4.loc[(ft, modelo)]
        filas.append({'condicion': etiqueta, 'auc_prueba': r3(r['auc']), 'auc_prueba_ic95': [r3(r['auc_ci_low']), r3(r['auc_ci_high'])]})
    tabla[nombre] = filas

json.dump({
    'nota': 'Generado por Other/defensa/datos_ronda6.py. No editar a mano.',
    'roc_prueba_fig_6_3_2': roc,
    'metricas_representacion_fig_6_2_4': metricas,
    'tsne_fig_6_2_5': tsne,
    'tabla_resumen_tabla_23': tabla,
}, open(SALIDA, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('Escrito', SALIDA.relative_to(ROOT), f'({SALIDA.stat().st_size / 1024:.0f} KiB)')
for nombre, filas in tabla.items():
    print(nombre)
    for f in filas:
        print('  ', {k: v for k, v in f.items() if v is not None})
