"""Genera tablas LaTeX para el reporte a partir de los CSV de Code/results.

Cada tabla se escribe en Docs/tablas/<nombre>.tex y se incluye en el reporte con \\input{tablas/<nombre>}.
Las cifras salen directamente de los CSV, así que no hay que transcribirlas a mano; si un resultado cambia,
basta con volver a correr el script. Usa booktabs, float y adjustbox, que ya carga el preámbulo del reporte; adjustbox solo reduce una tabla si no cabe en el ancho del texto.

Uso: python Code/tools/tablas_latex.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RES = ROOT / 'Code/results'
OUT = ROOT / 'Docs/tablas'
SUBSETS = [('mass', 'Masas'), ('calcification', 'Calcificaciones')]
COND = ['C1', 'C2', 'C3', 'C4', 'C5']


def f3(x):
    return '—' if pd.isna(x) else f'{x:.3f}'.replace('-', '$-$')


def ci(lo, hi):
    return f'[{f3(lo)}, {f3(hi)}]'


def p_fmt(p):
    return '$<$0.001' if p < 0.001 else f'{p:.3f}'


def tex_name(feature):
    return feature.replace('original_', '').replace('_', r'\_')


def write(name, source, caption, label, colspec, header, body, note=None):
    lines = [f'% Generado por Code/tools/tablas_latex.py desde {source}. No editar a mano: volver a correr el script.',
             r'\begin{table}[H]', r'\centering', r'\small', f'\\caption{{{caption}}}', f'\\label{{{label}}}',
             r'\begin{adjustbox}{max width=\linewidth}', f'\\begin{{tabular}}{{{colspec}}}', r'\toprule', header + r' \\', r'\midrule']
    lines += body
    lines += [r'\bottomrule', r'\end{tabular}', r'\end{adjustbox}']
    if note:
        lines += [r'\par\smallskip', f'\\parbox{{0.95\\linewidth}}{{\\footnotesize {note}}}']
    lines += [r'\end{table}', '']
    (OUT / f'{name}.tex').write_text('\n'.join(lines), encoding='utf-8')
    print(f'{name}.tex  <-  {source}')


def seleccion():
    d = pd.read_csv(RES / '4_seleccion.csv')
    body = []
    for i in range(12):
        cells = []
        for ft, _ in SUBSETS:
            r = d[(d.finding_type == ft) & (d.order == d[d.finding_type == ft].order.min() + i)].iloc[0]
            cells += [tex_name(r.feature), r.family, f'{r.F:.1f}']
        body.append(f'{i + 1} & ' + ' & '.join(cells) + r' \\')
    write('m4_seleccion', '4_seleccion.csv',
          'Las 12 características seleccionadas en cada subconjunto (M4): F-test ANOVA sobre el entrenamiento con restricción de redundancia $|r| \\le$ 0.95.',
          'tab:m4_seleccion', 'r l l r l l r',
          r' & \multicolumn{3}{c}{Masas} & \multicolumn{3}{c}{Calcificaciones} \\ \cmidrule(lr){2-4}\cmidrule(lr){5-7}' '\n'
          r'\# & Característica & Familia & $F$ & Característica & Familia & $F$', body)


def separabilidad_kernels():
    a = pd.read_csv(RES / '6_alineamiento_kernel.csv')
    e = pd.read_csv(RES / '6_dimension_efectiva.csv')
    g = pd.read_csv(RES / '6_diferencia_geometrica_resumen.csv')
    body = []
    for ft, title in SUBSETS:
        body.append(f'\\multicolumn{{6}}{{l}}{{\\textit{{{title}}}}} \\\\')
        for k, name in [('K_C', 'RBF (clásico)'), ('C4', 'C4, ZZ'), ('C5', 'C5, Y--ZZ')]:
            sel = (lambda df: df[(df.finding_type == ft) & (df.kernel == k) & (df.c.isna() if k == 'K_C' else df.c == 1.0)])
            ra, re_ = sel(a).iloc[0], sel(e).iloc[0]
            gg = '—' if k == 'K_C' else f3(g[(g.finding_type == ft) & (g['map'] == k) & (g.c == 1.0)].g_min.iloc[0])
            body.append(f'\\quad {name} & {f3(ra.kta_centered)} & {f3(ra.excess_centered)} & {p_fmt(ra.p_centered)} & {re_.effective_dimension:.1f} & {gg} \\\\')
    write('m6_separabilidad_kernels', '6_alineamiento_kernel.csv, 6_dimension_efectiva.csv y 6_diferencia_geometrica_resumen.csv',
          'Separabilidad en la familia de kernels (M6), $c = 1$, 200 lesiones de entrenamiento por subconjunto.',
          'tab:m6_kernels', 'l r r r r r',
          r'Kernel & KTA centrada & Exceso sobre permutación & $p$ & $d_{\mathrm{eff}}$ (de 200) & $g$ regularizada', body,
          r'El exceso es la KTA centrada menos la media de 1{,}000 permutaciones de etiquetas; $p$ es unilateral. '
          r'$g$ es el mínimo de la \textit{geometric difference} regularizada sobre la batería de kernels clásicos del Apéndice L.3 de Huang et al.\; $\sqrt{N} \approx 14$.')


def separabilidad_embeddings():
    d = pd.read_csv(RES / '6_metricas_embedding.csv')
    d = d[d['sample'] == 'subsample']
    body = []
    for ft, title in SUBSETS:
        body.append(f'\\multicolumn{{4}}{{l}}{{\\textit{{{title}}}}} \\\\')
        for c in COND:
            r = d[(d.finding_type == ft) & (d.condition == c)].iloc[0]
            body.append(f'\\quad {c} & {f3(r.davies_bouldin)} & {f3(r.fisher_j)} & {f3(r.kta_linear)} \\\\')
    write('m6_separabilidad_embeddings', '6_metricas_embedding.csv',
          'Separabilidad en la familia de embeddings (M6): 200 lesiones de entrenamiento por subconjunto.',
          'tab:m6_embeddings', 'l r r r', r'Condición & Davies--Bouldin $\downarrow$ & Fisher $J$ $\uparrow$ & KTA lineal $\uparrow$', body,
          r'Fisher $J = \Delta\mu^\top S_W^{-1} \Delta\mu$, con la covarianza intraclase combinada. C1 y C2 coinciden por construcción.')


def clasificacion():
    t = pd.read_csv(RES / '7_test.csv')
    t = t[t.analysis == 'main']
    cv = pd.read_csv(RES / '7_cv_resumen.csv')
    cv = cv[(cv.analysis == 'main') & (cv.config == 'base') & (cv.seed == 42) & (cv.k == 12)]
    body = []
    for ft, title in SUBSETS:
        body.append(f'\\multicolumn{{7}}{{l}}{{\\textit{{{title}}}}} \\\\')
        for c in COND:
            r = t[(t.finding_type == ft) & (t.condition == c)].iloc[0]
            v = cv[(cv.finding_type == ft) & (cv.condition == c)].iloc[0]
            body.append(f'\\quad {c} & {f3(v.auc_mean)} $\\pm$ {v.auc_std:.3f} & {f3(r.auc)} {ci(r.auc_ci_low, r.auc_ci_high)} & '
                        f'{f3(r.f1)} & {f3(r.accuracy)} & {f3(r.precision)} & {f3(r.recall)} \\\\')
    write('m7_clasificacion', '7_test.csv y 7_cv_resumen.csv',
          'Clasificación con el mismo MLP sobre las cinco representaciones (M7, $k = 12$).',
          'tab:m7_clasificacion', 'l c c r r r r',
          r'Condición & AUC en VC & AUC en prueba [IC 95\,\%] & F1 & Exactitud & Precisión & Sensibilidad', body,
          r'VC: media $\pm$ desviación estándar sobre los 5 folds de M4. Prueba: el conjunto oficial, usado una sola vez por modelo; '
          r'el intervalo es un \textit{bootstrap} por paciente con 2{,}000 réplicas. Umbral de 0.5 para F1, exactitud, precisión y sensibilidad.')


def diferencias():
    d = pd.read_csv(RES / '7_test_diferencias.csv')
    d = d[d.group == 'main']
    body = []
    for ft, title in SUBSETS:
        body.append(f'\\multicolumn{{4}}{{l}}{{\\textit{{{title}}}}} \\\\')
        for r in d[d.finding_type == ft].itertuples():
            comp = r.comparison.replace(' (main)', '').replace(' - ', ' $-$ ')
            p = 2 * min(r.share_above_0, 1 - r.share_above_0)
            body.append(f'\\quad {comp} & {f3(r.mean_difference)} & {ci(r.ci_low, r.ci_high)} & {p_fmt(p)} \\\\')
    write('m7_diferencias', '7_test_diferencias.csv',
          'Diferencias pareadas de AUC en el conjunto de prueba (M7).',
          'tab:m7_diferencias', 'l r c r', r'Comparación & Diferencia & IC 95\,\% & $p$ bilateral', body,
          r'Las diferencias usan las mismas réplicas del \textit{bootstrap} por paciente para ambas condiciones. '
          r'$p \approx 2\min(q, 1 - q)$, con $q$ la fracción de réplicas con diferencia positiva; no está corregido por comparaciones múltiples.')


def spearman():
    d = pd.read_csv(RES / '8_spearman.csv')
    d = d[d.primary.astype(str) == 'True']
    names = {'Davies-Bouldin': 'Davies--Bouldin', 'Fisher J': 'Fisher $J$', 'linear KTA': 'KTA lineal'}
    body = []
    for ft, title in SUBSETS:
        for r in d[d.finding_type == ft].itertuples():
            body.append(f'{title} & {names[r.metric]} & {r.rho:.3f} & {r.p_exact_two_sided:.3f} \\\\')
    write('m8_spearman', '8_spearman.csv',
          'Correlación de Spearman entre el orden de separabilidad y el de clasificación de las cinco condiciones (M8).',
          'tab:m8_spearman', 'l l r r', r'Subconjunto & Métrica de separabilidad & $\rho_s$ & $p$ exacto bilateral', body,
          r'Submuestra de 200 lesiones frente al AUC de prueba, $k = 12$. Con $n = 5$ hay 120 órdenes; $\rho_s$ es la correlación de Pearson '
          r'de los rangos promedio, porque C1 y C2 empatan. Es descriptivo: con el empate, el mejor orden alcanzable da $p = 4/120$.')


def sorteos_theta():
    d = pd.read_csv(RES / 'X7_resumen.csv')
    body = []
    for ft, title in SUBSETS:
        for r in d[d.finding_type == ft].itertuples():
            body.append(f'{title} & {r.condition} & {f3(r.auc_design_draw)} ({r.rank_design_draw}.\\textsuperscript{{o}}) & '
                        f'{f3(r.auc_min)}--{f3(r.auc_max)} & {f3(r.range_over_theta)} & {f3(r.range_over_mlp_seeds)} & {f3(r.C1_minus_best_draw)} \\\\')
    write('x7_sorteos_theta', 'X7_resumen.csv',
          'Dependencia del AUC de C4 y C5 respecto al sorteo de $\\theta$: 10 sorteos, mismo MLP y mismos folds que el M7.',
          'tab:x7_theta', 'l l c c r r r',
          r'Subconjunto & Mapa & Semilla 42 (lugar) & Mín.--máx. & Rango ($\theta$) & Rango (MLP) & C1 $-$ mejor', body,
          r'AUC medio en validación cruzada; el conjunto de prueba no se usó. Rango (MLP): variación entre las 5 semillas del MLP con el $\theta$ del diseño.')


def theta_entrenado():
    path = RES / 'X8_test.csv'
    if not path.exists():
        print('X8_test.csv no existe todavía: se omite la tabla del X8')
        return
    t = pd.read_csv(path)
    d = pd.read_csv(RES / 'X8_test_diferencias.csv')
    cv = pd.read_csv(RES / 'X8_cv_por_fold.csv')
    m7 = pd.read_csv(RES / '7_cv_resumen.csv')
    m7 = m7[(m7.analysis == 'main') & (m7.config == 'base') & (m7.seed == 42) & (m7.k == 12)]
    body = []
    for ft, title in SUBSETS:
        body.append(f'\\multicolumn{{5}}{{l}}{{\\textit{{{title}}}}} \\\\')
        for q in ['C4', 'C5']:
            fixed = t[(t.finding_type == ft) & (t.model == f'{q} theta fixed')].iloc[0]
            trained = t[(t.finding_type == ft) & (t.model == f'{q} theta trained')].iloc[0]
            cv_tr = cv[(cv.finding_type == ft) & (cv.condition == q) & (cv.config == 'main')].auc.mean()
            cv_fx = m7[(m7.finding_type == ft) & (m7.condition == q)].auc_mean.iloc[0]
            dd = d[(d.finding_type == ft) & (d.comparison == f'{q} theta trained - C1')].iloc[0]
            body.append(f'\\quad {q} & {f3(cv_fx)} $\\to$ {f3(cv_tr)} & {f3(fixed.auc)} $\\to$ {f3(trained.auc)} & '
                        f'{ci(trained.auc_ci_low, trained.auc_ci_high)} & {f3(dd.mean_difference)} {ci(dd.ci_low, dd.ci_high)} \\\\')
    write('x8_theta_entrenado', 'X8_test.csv, X8_test_diferencias.csv, X8_cv_por_fold.csv y 7_cv_resumen.csv',
          'Efecto de entrenar $\\theta$ junto con el MLP: de $\\theta$ fijo (M7) a $\\theta$ entrenado.',
          'tab:x8_theta', 'l c c c c',
          r'Mapa & AUC en VC & AUC en prueba & IC 95\,\% (entrenado) & Entrenado $-$ C1 en prueba', body,
          r'Mismo protocolo que el M7; solo cambia que $\theta$ se entrena desde el sorteo del diseño, con gradientes exactos del simulador.')



def t_fmt(x):
    return '—' if pd.isna(x) else (f'{x:.4f}' if x < 0.01 else f'{x:.2f}' if x < 1 else f'{x:.1f}')


def resumen_resultados():
    """Tabla general de §6.8: separabilidad (M6), clasificación (M7 y X4) y tiempo de transformación (M5)."""
    a = pd.read_csv(RES / '6_alineamiento_kernel.csv')
    e = pd.read_csv(RES / '6_dimension_efectiva.csv')
    g = pd.read_csv(RES / '6_diferencia_geometrica_resumen.csv')
    m = pd.read_csv(RES / '6_metricas_embedding.csv')
    m = m[m['sample'] == 'subsample']
    t = pd.read_csv(RES / '7_test.csv')
    t = t[t.analysis == 'main']
    cv = pd.read_csv(RES / '7_cv_resumen.csv')
    cv = cv[(cv.analysis == 'main') & (cv.config == 'base') & (cv.seed == 42) & (cv.k == 12)]
    x4 = pd.read_csv(RES / 'X4_test.csv')
    tq = pd.read_csv(RES / '5a_resumen.csv')
    tc = pd.read_csv(RES / '5a_tiempos_clasicos.csv')
    kern = {'C3': 'K_C', 'C4': 'C4', 'C5': 'C5'}   # el kernel RBF de M6 usa el mismo gamma que C3 (D-027)
    body = []
    for ft, title in SUBSETS:
        body.append(f'\\multicolumn{{9}}{{l}}{{\\textit{{{title}}}}} \\\\')
        for c in COND:
            if c in kern:
                k = kern[c]
                sel = (lambda df: df[(df.finding_type == ft) & (df.kernel == k) & (df.c.isna() if k == 'K_C' else df.c == 1.0)])
                exc, deff = f3(sel(a).iloc[0].excess_centered), f'{sel(e).iloc[0].effective_dimension:.1f}'
            else:
                exc = deff = '—'
            gg = f3(g[(g.finding_type == ft) & (g['map'] == c) & (g.c == 1.0)].g_min.iloc[0]) if c in ('C4', 'C5') else '—'
            r = m[(m.finding_type == ft) & (m.condition == c)].iloc[0]
            v = cv[(cv.finding_type == ft) & (cv.condition == c)].iloc[0]
            te = t[(t.finding_type == ft) & (t.condition == c)].iloc[0]
            if c == 'C1':
                secs = np.nan
            elif c in ('C2', 'C3'):
                secs = tc[(tc.finding_type == ft) & (tc.condition == c)].seconds_median.iloc[0]
            else:
                secs = tq[(tq.finding_type == ft) & (tq.condition == c)].total_time_seconds.iloc[0]
            body.append(f'\\quad {c} & {exc} & {deff} & {gg} & {f3(r.davies_bouldin)} & {f3(r.fisher_j)} & '
                        f'{f3(v.auc_mean)} & {f3(te.auc)} {ci(te.auc_ci_low, te.auc_ci_high)} & {t_fmt(secs)} \\\\')
        for model, name in [('SVM RBF (D-027)', 'SVM sobre el kernel RBF'), ('QSVM C4, c = 1', 'QSVM sobre el kernel de C4'),
                            ('QSVM C5, c = 1', 'QSVM sobre el kernel de C5')]:
            r = x4[(x4.finding_type == ft) & (x4.model == model)].iloc[0]
            body.append(f'\\quad {name} & \\multicolumn{{6}}{{c}}{{}} & {f3(r.auc)} {ci(r.auc_ci_low, r.auc_ci_high)} & — \\\\')
    write('resumen_resultados',
          '6_alineamiento_kernel.csv, 6_dimension_efectiva.csv, 6_diferencia_geometrica_resumen.csv, 6_metricas_embedding.csv, '
          '7_cv_resumen.csv, 7_test.csv, X4_test.csv, 5a_resumen.csv y 5a_tiempos_clasicos.csv',
          'Resumen de resultados por condición: separabilidad (M6), clasificación (M7 y X4) y tiempo de transformación (M5).',
          'tab:resumen_resultados', 'l r r r r r r c r',
          r' & \multicolumn{3}{c}{Kernel} & \multicolumn{2}{c}{Representación} & \multicolumn{2}{c}{AUC-ROC} & \\'
          r' \cmidrule(lr){2-4}\cmidrule(lr){5-6}\cmidrule(lr){7-8}' '\n'
          r'Condición & Exceso KTA $\uparrow$ & $d_{\mathrm{eff}}$ & $g$ & DB $\downarrow$ & Fisher $\uparrow$ & VC & Prueba [IC 95\,\%] & Tiempo (s)', body,
          r'Separabilidad sobre 200 lesiones de entrenamiento por subconjunto y $c = 1$. Las columnas de kernel de C3 corresponden al kernel RBF, '
          r'con el mismo $\gamma$ que C3; C1 y C2 no definen un kernel propio. $g$: mínimo de la \textit{geometric difference} regularizada '
          r'($\sqrt{N} \approx 14$). AUC: el mismo MLP en C1--C5; las tres últimas filas de cada bloque son clasificadores de vectores de soporte '
          r'sobre el kernel (experimento X4). Tiempo: transformación de todas las lesiones del subconjunto en la máquina del proyecto; '
          r'en C2 y C3, mediana de cinco repeticiones; C1 es la identidad. Con el etiquetado diseñado según Huang et al., control positivo del '
          r'protocolo (sección~\ref{sec:qsvm_ventaja}), el kernel cuántico proyectado alcanza en validación cruzada 0.998 en masas y 0.994 en '
          r'calcificaciones, frente a 0.800 y 0.824 del mejor clasificador clásico.')

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    for f in [seleccion, separabilidad_kernels, separabilidad_embeddings, clasificacion, diferencias, spearman, sorteos_theta, theta_entrenado, resumen_resultados]:
        f()
