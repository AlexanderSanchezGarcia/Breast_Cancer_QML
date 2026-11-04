# Extrae de Data/ y Code/results/ los datos reales que usan las escenas de Manim de la defensa
# y los guarda en Other/defensa/manim/datos/, que es pequeño y sí se versiona.
# Se corre una vez con el entorno qml_cancer:
#   /opt/anaconda3/envs/qml_cancer/bin/python Other/defensa/manim/preparar_datos.py
import json
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[3]
SALIDA = Path(__file__).resolve().parent / 'datos'
SALIDA.mkdir(exist_ok=True)
C_VALORES = [1.0, 0.5, 0.2, 0.1, 0.05, 0.02]

# 1. Kernels de 40 lesiones de masas: las mismas que kernel_40x40_masas.json (20 benignas, 20 malignas, semilla 42)
z = np.load(RAIZ / 'Data/processed/m5/kernels_mass.npz', allow_pickle=True)
y = z['label']
rng = np.random.default_rng(42)
ben = rng.choice(np.where(y == 0)[0], 20, replace=False)
mal = rng.choice(np.where(y == 1)[0], 20, replace=False)
idx = np.r_[np.sort(ben), np.sort(mal)]
fuera = ~np.eye(200, dtype=bool)
kern = {'RBF': z['K_C'][np.ix_(idx, idx)], 'C5': z['K_Q_C5'][np.ix_(idx, idx)]}
medianas = {'RBF': float(np.median(z['K_C'][fuera])), 'C5': float(np.median(z['K_Q_C5'][fuera]))}
for c in C_VALORES:
    k = z[f'K_Q_C4_c{c}']
    kern[f'C4_c{c}'] = k[np.ix_(idx, idx)]
    medianas[f'C4_c{c}'] = float(np.median(k[fuera]))
np.savez_compressed(SALIDA / 'kernels_40_masas.npz', **kern)

# 2. Una lesión de masas real para la diapositiva de las dos lecturas: sus 12 ángulos (C1) y sus 12 <Z_i> (C4)
emb = pd.read_parquet(RAIZ / 'Data/processed/m5/emb_mass.parquet')
caso = z['case_id'][idx[0]]
fila = emb[emb.case_id == caso].iloc[0]
otro = z['case_id'][idx[20]]
lesion = {
    'case_id': str(caso),
    'x': [float(fila[f'C1_{i:02d}']) for i in range(1, 13)],
    'z_c4': [float(fila[f'C4_{i:02d}']) for i in range(1, 13)],
    'kernel_c4_con_otra': float(z['K_Q_C4'][idx[0], idx[20]]),
    'otra_case_id': str(otro),
}

# 2b. Su vector de estado real tras el feature map de C4 (sin ansatz): las 4,096 probabilidades de la lesión
# y de la otra lesión, y su fidelidad, que debe coincidir con el valor del kernel del M5
from qiskit.circuit.library import zz_feature_map
from qiskit.quantum_info import Statevector
fmap = zz_feature_map(12, reps=1)
x4 = pd.read_parquet(RAIZ / 'Data/processed/m4/x_mass.parquet')
cols = [f'x_{i:02d}' for i in range(1, 13)]
def estado(case_id):
    v = x4.set_index('case_id').loc[case_id, cols].to_numpy(float)
    return Statevector(fmap.assign_parameters(dict(zip(fmap.parameters, v))))
sa, sb = estado(caso), estado(otro)
fid = float(abs(np.vdot(sa.data, sb.data)) ** 2)
assert abs(fid - lesion['kernel_c4_con_otra']) < 1e-9, (fid, lesion['kernel_c4_con_otra'])
# Tras H y las fases diagonales del mapa ZZ, las 4,096 probabilidades valen exactamente 1/4096:
# toda la información de la lesión está en las fases. Se guardan relativas a la componente |0...0>
# (la fase global no es observable) y envueltas en (-pi, pi].
fase = lambda s: np.angle(s.data * np.conj(s.data[0]))
fa, fb = fase(sa), fase(sb)
assert np.allclose(np.abs(sa.data) ** 2, 1 / 4096) and np.allclose(np.abs(sb.data) ** 2, 1 / 4096)
assert abs(abs(np.mean(np.exp(1j * (fa - fb)))) ** 2 - fid) < 1e-9
np.savez_compressed(SALIDA / 'estado_lesion.npz', prob_a=np.abs(sa.data) ** 2, prob_b=np.abs(sb.data) ** 2,
                    fase_a=fa, fase_b=fb)

# 3. X11: transición, kernel proyectado en masas, y umbrales alpha*
t = pd.read_csv(RAIZ / 'Code/results/X11_transicion.csv')
x11 = t[(t.finding_type == 'mass') & t.quantum_kernel.str.startswith('Projected')].sort_values('alpha')
x11[['alpha', 'quantum_auc', 'classical_auc', 'difference', 'ci_low', 'ci_high', 'quantum_wins']].to_csv(
    SALIDA / 'x11_masas_proyectado.csv', index=False)
umbral = pd.read_csv(RAIZ / 'Code/results/X11_umbral.csv')

# 4. Disparos: fracción de pares del kernel que se leen exactamente 0 con 1,024 disparos (c = 1)
sk = pd.read_csv(RAIZ / 'Code/results/8_oe6_shots_kernel.csv')
sk = sk[sk.c == 1.0]
disparos = {
    f'{r.finding_type}_{r.map}': {'mediana': float(r.median_value), 'lee_cero_1024': float(r.reads_zero_at_1024)}
    for r in sk.itertuples()
}

# 5. Conteos y nombres del pipeline
m4 = json.load(open(RAIZ / 'Data/processed/m4/x_mass.json'))
m4c = json.load(open(RAIZ / 'Data/processed/m4/x_calcification.json'))
resumen = {
    'medianas_kernel_200': medianas,
    'c_valores': C_VALORES,
    'lesion': lesion,
    'x11_umbral': {f'{r.finding_type}|{r.quantum_kernel}': float(r.alpha_star) for r in umbral.itertuples()},
    'disparos': disparos,
    'pipeline': {
        'lesiones': 3568, 'pacientes': 1566, 'masas': 1696, 'calcificaciones': 1872,
        'entrenamiento': 2864, 'prueba': 704, 'caracteristicas': 67, 'seleccionadas': 12,
        'features_masas': [f.replace('original_', '') for f in m4['features']],
        'features_calcificaciones': [f.replace('original_', '') for f in m4c['features']],
    },
    'fuentes': {
        'kernels': 'Data/processed/m5/kernels_mass.npz',
        'lesion': 'Data/processed/m5/emb_mass.parquet',
        'x11': 'Code/results/X11_transicion.csv, X11_umbral.csv',
        'disparos': 'Code/results/8_oe6_shots_kernel.csv',
        'pipeline': 'CLAUDE.md (dataset) y Data/processed/m4/x_*.json',
    },
}
json.dump(resumen, open(SALIDA / 'resumen.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in resumen.items() if k != 'pipeline'}, ensure_ascii=False, indent=1)[:1500])
