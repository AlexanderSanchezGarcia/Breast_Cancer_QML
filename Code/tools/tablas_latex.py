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


def bf(text):
    # negrita que también alcanza al signo menos en modo matemático
    return f'\\textbf{{\\boldmath {text}}}' if '$' in text else f'\\textbf{{{text}}}'


def best_mask(values, higher=True):
    # True donde el valor, redondeado a tres decimales como se imprime, es el mejor; los empates cuentan todos
    v = np.round(np.asarray(values, float), 3)
    ok = ~np.isnan(v)
    if not ok.any():
        return np.zeros(len(v), bool)
    target = v[ok].max() if higher else v[ok].min()
    return ok & (v == target)


def mark(text, flag):
    return bf(text) if flag else text


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
        rows = []
        for k, name in [('K_C', 'RBF (clásico)'), ('C4', 'C4, ZZ'), ('C5', 'C5, Y--ZZ')]:
            sel = (lambda df: df[(df.finding_type == ft) & (df.kernel == k) & (df.c.isna() if k == 'K_C' else df.c == 1.0)])
            ra, re_ = sel(a).iloc[0], sel(e).iloc[0]
            gg = '—' if k == 'K_C' else f3(g[(g.finding_type == ft) & (g['map'] == k) & (g.c == 1.0)].g_min.iloc[0])
            rows.append((name, ra, re_, gg))
        best = best_mask([r[1].excess_centered for r in rows])
        for (name, ra, re_, gg), b in zip(rows, best):
            body.append(f'\\quad {name} & {f3(ra.kta_centered)} & {mark(f3(ra.excess_centered), b)} & {p_fmt(ra.p_centered)} & {re_.effective_dimension:.1f} & {gg} \\\\')
    write('m6_separabilidad_kernels', '6_alineamiento_kernel.csv, 6_dimension_efectiva.csv y 6_diferencia_geometrica_resumen.csv',
          'Separabilidad en la familia de kernels (M6), $c = 1$, 200 lesiones de entrenamiento por subconjunto.',
          'tab:m6_kernels', 'l r r r r r',
          r'Kernel & KTA centrada & Exceso sobre permutación $\uparrow$ & $p$ & $d_{\mathrm{eff}}$ (de 200) & $g$ regularizada', body,
          r'El exceso es la KTA centrada menos la media de 1{,}000 permutaciones de etiquetas; $p$ es unilateral. '
          r'$g$ es el mínimo de la \textit{geometric difference} regularizada sobre la batería de kernels clásicos del Apéndice L.3 de Huang et al.\; $\sqrt{N} \approx 14$. '
          r'En negritas, el mayor exceso de cada subconjunto; la KTA cruda no es comparable entre kernels.')


def separabilidad_embeddings():
    d = pd.read_csv(RES / '6_metricas_embedding.csv')
    d = d[d['sample'] == 'subsample']
    body = []
    for ft, title in SUBSETS:
        body.append(f'\\multicolumn{{4}}{{l}}{{\\textit{{{title}}}}} \\\\')
        r = d[d.finding_type == ft].set_index('condition').loc[COND]
        b_db, b_fi, b_kt = best_mask(r.davies_bouldin, False), best_mask(r.fisher_j), best_mask(r.kta_linear)
        for i, c in enumerate(COND):
            x = r.loc[c]
            body.append(f'\\quad {c} & {mark(f3(x.davies_bouldin), b_db[i])} & {mark(f3(x.fisher_j), b_fi[i])} & {mark(f3(x.kta_linear), b_kt[i])} \\\\')
    write('m6_separabilidad_embeddings', '6_metricas_embedding.csv',
          'Separabilidad en la familia de embeddings (M6): 200 lesiones de entrenamiento por subconjunto.',
          'tab:m6_embeddings', 'l r r r', r'Condición & Davies--Bouldin $\downarrow$ & Fisher $J$ $\uparrow$ & KTA lineal $\uparrow$', body,
          r'Fisher $J = \Delta\mu^\top S_W^{-1} \Delta\mu$, con la covarianza intraclase combinada. C1 y C2 coinciden por construcción. '
          r'En negritas, el mejor valor de cada métrica en cada subconjunto.')


def clasificacion():
    t = pd.read_csv(RES / '7_test.csv')
    t = t[t.analysis == 'main']
    cv = pd.read_csv(RES / '7_cv_resumen.csv')
    cv = cv[(cv.analysis == 'main') & (cv.config == 'base') & (cv.seed == 42) & (cv.k == 12)]
    body = []
    for ft, title in SUBSETS:
        body.append(f'\\multicolumn{{7}}{{l}}{{\\textit{{{title}}}}} \\\\')
        r = t[t.finding_type == ft].set_index('condition').loc[COND]
        v = cv[cv.finding_type == ft].set_index('condition').loc[COND]
        b_cv, b_te = best_mask(v.auc_mean), best_mask(r.auc)
        for i, c in enumerate(COND):
            x, y = r.loc[c], v.loc[c]
            body.append(f'\\quad {c} & {mark(f3(y.auc_mean), b_cv[i])} $\\pm$ {y.auc_std:.3f} & {mark(f3(x.auc), b_te[i])} {ci(x.auc_ci_low, x.auc_ci_high)} & '
                        f'{f3(x.f1)} & {f3(x.accuracy)} & {f3(x.precision)} & {f3(x.recall)} \\\\')
    write('m7_clasificacion', '7_test.csv y 7_cv_resumen.csv',
          'Clasificación con el mismo MLP sobre las cinco representaciones (M7, $k = 12$).',
          'tab:m7_clasificacion', 'l c c r r r r',
          r'Condición & AUC en VC & AUC en prueba [IC 95\,\%] & F1 & Exactitud & Precisión & Sensibilidad', body,
          r'VC: media $\pm$ desviación estándar sobre los 5 folds de M4. Prueba: el conjunto oficial, usado una sola vez por modelo; '
          r'el intervalo es un \textit{bootstrap} por paciente con 2{,}000 réplicas. Umbral de 0.5 para F1, exactitud, precisión y sensibilidad. '
          r'En negritas, el mayor AUC de cada subconjunto, la métrica principal.')


def diferencias():
    d = pd.read_csv(RES / '7_test_diferencias.csv')
    d = d[d.group == 'main']
    body = []
    for ft, title in SUBSETS:
        body.append(f'\\multicolumn{{4}}{{l}}{{\\textit{{{title}}}}} \\\\')
        for r in d[d.finding_type == ft].itertuples():
            comp = r.comparison.replace(' (main)', '').replace(' - ', ' $-$ ')
            p = 2 * min(r.share_above_0, 1 - r.share_above_0)
            sig = r.ci_low > 0 or r.ci_high < 0
            body.append(f'\\quad {comp} & {mark(f3(r.mean_difference), sig)} & {mark(ci(r.ci_low, r.ci_high), sig)} & {p_fmt(p)} \\\\')
    write('m7_diferencias', '7_test_diferencias.csv',
          'Diferencias pareadas de AUC en el conjunto de prueba (M7).',
          'tab:m7_diferencias', 'l r c r', r'Comparación & Diferencia & IC 95\,\% & $p$ bilateral', body,
          r'Las diferencias usan las mismas réplicas del \textit{bootstrap} por paciente para ambas condiciones. '
          r'$p \approx 2\min(q, 1 - q)$, con $q$ la fracción de réplicas con diferencia positiva; no está corregido por comparaciones múltiples. '
          r'En negritas, las diferencias cuyo intervalo no contiene el cero.')


def spearman():
    d = pd.read_csv(RES / '8_spearman.csv')
    d = d[d.primary.astype(str) == 'True']
    names = {'Davies-Bouldin': 'Davies--Bouldin', 'Fisher J': 'Fisher $J$', 'linear KTA': 'KTA lineal'}
    body = []
    for ft, title in SUBSETS:
        part = d[d.finding_type == ft]
        best = best_mask(part.rho)
        for r, b in zip(part.itertuples(), best):
            body.append(f'{title} & {names[r.metric]} & {mark(f"{r.rho:.3f}", b)} & {r.p_exact_two_sided:.3f} \\\\')
    write('m8_spearman', '8_spearman.csv',
          'Correlación de Spearman entre el orden de separabilidad y el de clasificación de las cinco condiciones (M8).',
          'tab:m8_spearman', 'l l r r', r'Subconjunto & Métrica de separabilidad & $\rho_s$ & $p$ exacto bilateral', body,
          r'Submuestra de 200 lesiones frente al AUC de prueba, $k = 12$. Con $n = 5$ hay 120 órdenes; $\rho_s$ es la correlación de Pearson '
          r'de los rangos promedio, porque C1 y C2 empatan. Es descriptivo: con el empate, el mejor orden alcanzable da $p = 4/120$. '
          r'En negritas, la métrica con mayor $\rho_s$ en cada subconjunto.')


def sorteos_theta():
    d = pd.read_csv(RES / 'X7_resumen.csv')
    body = []
    for ft, title in SUBSETS:
        for r in d[d.finding_type == ft].itertuples():
            bt, bm = best_mask([r.range_over_theta, r.range_over_mlp_seeds])
            body.append(f'{title} & {r.condition} & {f3(r.auc_design_draw)} ({r.rank_design_draw}.\\textsuperscript{{o}}) & '
                        f'{f3(r.auc_min)}--{f3(r.auc_max)} & {mark(f3(r.range_over_theta), bt)} & {mark(f3(r.range_over_mlp_seeds), bm)} & {f3(r.C1_minus_best_draw)} \\\\')
    write('x7_sorteos_theta', 'X7_resumen.csv',
          'Dependencia del AUC de C4 y C5 respecto al sorteo de $\\theta$: 10 sorteos, mismo MLP y mismos folds que el M7.',
          'tab:x7_theta', 'l l c c r r r',
          r'Subconjunto & Mapa & Semilla 42 (lugar) & Mín.--máx. & Rango ($\theta$) & Rango (MLP) & C1 $-$ mejor', body,
          r'AUC medio en validación cruzada; el conjunto de prueba no se usó. Rango (MLP): variación entre las 5 semillas del MLP con el $\theta$ del diseño. '
          r'En negritas, la mayor de las dos fuentes de variación en cada fila. C1 $-$ mejor es positivo en las cuatro filas: ningún sorteo alcanza a C1.')


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
            b_cv, b_te = best_mask([cv_fx, cv_tr]), best_mask([fixed.auc, trained.auc])
            sig = dd.ci_low > 0 or dd.ci_high < 0
            body.append(f'\\quad {q} & {mark(f3(cv_fx), b_cv[0])} $\\to$ {mark(f3(cv_tr), b_cv[1])} & '
                        f'{mark(f3(fixed.auc), b_te[0])} $\\to$ {mark(f3(trained.auc), b_te[1])} & '
                        f'{ci(trained.auc_ci_low, trained.auc_ci_high)} & {mark(f3(dd.mean_difference) + " " + ci(dd.ci_low, dd.ci_high), sig)} \\\\')
    write('x8_theta_entrenado', 'X8_test.csv, X8_test_diferencias.csv, X8_cv_por_fold.csv y 7_cv_resumen.csv',
          'Efecto de entrenar $\\theta$ junto con el MLP: de $\\theta$ fijo (M7) a $\\theta$ entrenado.',
          'tab:x8_theta', 'l c c c c',
          r'Mapa & AUC en VC & AUC en prueba & IC 95\,\% (entrenado) & Entrenado $-$ C1 en prueba', body,
          r'Mismo protocolo que el M7; solo cambia que $\theta$ se entrena desde el sorteo del diseño, con gradientes exactos del simulador. '
          r'En negritas, el mayor AUC de cada par y las diferencias frente a C1 cuyo intervalo no contiene el cero.')


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
        sel_k = lambda df, k: df[(df.finding_type == ft) & (df.kernel == k) & (df.c.isna() if k == 'K_C' else df.c == 1.0)]
        exc_all = [sel_k(a, kern[c]).iloc[0].excess_centered if c in kern else np.nan for c in COND]
        mm = m[m.finding_type == ft].set_index('condition').loc[COND]
        cvv = cv[cv.finding_type == ft].set_index('condition').loc[COND]
        x4f = x4[x4.finding_type == ft].set_index('model')
        svm_models = ['SVM RBF (D-027)', 'QSVM C4, c = 1', 'QSVM C5, c = 1']
        te_all = list(t[t.finding_type == ft].set_index('condition').loc[COND].auc) + [x4f.loc[mo].auc for mo in svm_models]
        b_exc, b_db, b_fi = best_mask(exc_all), best_mask(mm.davies_bouldin, False), best_mask(mm.fisher_j)
        b_cv, b_te = best_mask(cvv.auc_mean), best_mask(te_all)
        for i, c in enumerate(COND):
            if c in kern:
                k = kern[c]
                sel = (lambda df: df[(df.finding_type == ft) & (df.kernel == k) & (df.c.isna() if k == 'K_C' else df.c == 1.0)])
                exc, deff = mark(f3(sel(a).iloc[0].excess_centered), b_exc[i]), f'{sel(e).iloc[0].effective_dimension:.1f}'
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
            body.append(f'\\quad {c} & {exc} & {deff} & {gg} & {mark(f3(r.davies_bouldin), b_db[i])} & {mark(f3(r.fisher_j), b_fi[i])} & '
                        f'{mark(f3(v.auc_mean), b_cv[i])} & {mark(f3(te.auc), b_te[i])} {ci(te.auc_ci_low, te.auc_ci_high)} & {t_fmt(secs)} \\\\')
        for j, (model, name) in enumerate([('SVM RBF (D-027)', 'SVM sobre el kernel RBF'), ('QSVM C4, c = 1', 'QSVM sobre el kernel de C4'),
                                           ('QSVM C5, c = 1', 'QSVM sobre el kernel de C5')]):
            r = x4[(x4.finding_type == ft) & (x4.model == model)].iloc[0]
            body.append(f'\\quad {name} & \\multicolumn{{6}}{{c}}{{}} & {mark(f3(r.auc), b_te[len(COND) + j])} {ci(r.auc_ci_low, r.auc_ci_high)} & — \\\\')
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
          r'calcificaciones, frente a 0.800 y 0.824 del mejor clasificador clásico. '
          r'En negritas, el mejor valor de cada columna con dirección en cada subconjunto; en el AUC de prueba se comparan también las filas de X4.')


def x10_arboles():
    """§6.3: AUC en el conjunto de prueba de cada clasificador sobre cada representación (X10)."""
    t = pd.read_csv(RES / 'X10_test.csv')
    names = [('DT-depth', 'Árbol, poda por profundidad'), ('DT-purity', 'Árbol, poda por pureza'),
             ('DT-ccp', 'Árbol, poda por costo-complejidad'), ('RF', '\\textit{Random forest}'), ('XGB', 'XGBoost'),
             ('MLP (M7)', 'Perceptrón multicapa (M7)')]
    body = []
    for ft, title in SUBSETS:
        body.append(f'\\multicolumn{{6}}{{l}}{{\\textit{{{title}}}}} \\\\')
        for fam, name in names:
            r = t[(t.finding_type == ft) & (t.family == fam)].set_index('condition').loc[COND]
            best = best_mask(r.auc)
            body.append(f'\\quad {name} & ' + ' & '.join(mark(f3(r.loc[c, 'auc']), b) for c, b in zip(COND, best)) + ' \\\\')
    write('x10_arboles', 'X10_test.csv',
          'AUC-ROC en el conjunto de prueba de los clasificadores de árboles y del perceptrón multicapa sobre las cinco representaciones (experimento X10).',
          'tab:x10_arboles', 'l r r r r r', 'Clasificador & C1 & C2 & C3 & C4 & C5', body,
          r'Hiperparámetros elegidos por validación cruzada anidada con los \textit{folds} de M4; un ajuste por clasificador y '
          r'representación, evaluado una sola vez. Con el mismo clasificador, ninguna representación cuántica supera a C1 '
          r'con un intervalo pareado por encima de cero (sección~\ref{sec:rendimiento_clasificacion}). '
          r'En negritas, la mejor representación para cada clasificador.')


def tres_lecturas():
    """§6.4: las tres lecturas del estado del mapa ZZ completo, con sus resultados (M7, X4/X6 y X6)."""
    geo = pd.read_csv(RES / 'X6_geometria.csv')
    eng = pd.read_csv(RES / 'X6_etiquetas_construidas.csv')
    cv = pd.read_csv(RES / '7_cv_resumen.csv')
    cv = cv[(cv.analysis == 'main') & (cv.config == 'base') & (cv.seed == 42) & (cv.k == 12) & (cv.condition == 'C4')]
    def pair(fn):
        return ' & '.join(fn(ft) for ft, _ in SUBSETS)
    g = lambda enc, col: (lambda ft: f3(geo[(geo.finding_type == ft) & (geo.encoding == enc)].iloc[0][col]))
    e = lambda q, col: (lambda ft: f3(eng[(eng.finding_type == ft) & (eng.quantum_kernel == q)].iloc[0][col]))
    dash = lambda ft: '—'
    def best_row(vals):
        # vals: [mlp_m, mlp_c, fid_m, fid_c, proj_m, proj_c] como texto; mejor por subconjunto (columnas pares e impares)
        out = list(vals)
        for start in (0, 1):
            idx = [i for i in range(start, 6, 2) if vals[i] != '—']
            nums = [float(vals[i]) for i in idx]
            for i, b in zip(idx, best_mask(nums)):
                out[i] = mark(vals[i], b)
        return ' & '.join(out)
    cvv = {ft: f3(cv[cv.finding_type == ft].auc_mean.iloc[0]) for ft, _ in SUBSETS}
    ev = lambda q, col: [e(q, col)(ft) for ft, _ in SUBSETS]
    real = [cvv['mass'], cvv['calcification']] + ev('ZZ full (C4)', 'real_qsvm_auc') + ev('Projected (ZZ full)', 'real_qsvm_auc')
    built_q = ev('ZZ full (C4)', 'built_qsvm_auc') + ev('Projected (ZZ full)', 'built_qsvm_auc')
    built_c = ev('ZZ full (C4)', 'built_best_classical_auc') + ev('Projected (ZZ full)', 'built_best_classical_auc')
    bq = [mark(q, float(q) >= float(c)) for q, c in zip(built_q, built_c)]
    bc = [mark(c, float(c) > float(q)) for q, c in zip(built_q, built_c)]
    body = [
        'Mediana del kernel fuera de la diagonal & ' + pair(dash) + ' & ' + pair(g('ZZ full', 'median_off_diagonal')) + ' & '
        + pair(g('Projected (ZZ full), median bandwidth', 'median_off_diagonal')) + ' \\\\',
        '$g$ frente al modelo clásico más cercano & ' + pair(dash) + ' & ' + pair(g('ZZ full', 'g_min')) + ' & '
        + pair(g('Projected (ZZ full), median bandwidth', 'g_min')) + ' \\\\',
        'AUC, etiquetas diagnósticas & ' + best_row(real) + ' \\\\',
        'AUC, etiquetado diseñado & ' + pair(dash) + ' & ' + ' & '.join(bq) + ' \\\\',
        '\\quad mejor SVM clásico con ese etiquetado & ' + pair(dash) + ' & ' + ' & '.join(bc) + ' \\\\',
    ]
    write('tres_lecturas', 'X6_geometria.csv, X6_etiquetas_construidas.csv y 7_cv_resumen.csv',
          'Tres lecturas del estado del mapa ZZ completo: valores esperados $\\langle Z_i\\rangle$ con perceptrón (C4), kernel de fidelidad y kernel proyectado.',
          'tab:tres_lecturas', 'l c c c c c c',
          r' & \multicolumn{2}{c}{$\langle Z_i\rangle$ y MLP (C4)} & \multicolumn{2}{c}{Fidelidad (QSVM)} & \multicolumn{2}{c}{Proyectado}'
          r' \\ \cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}' '\n'
          r' & Masas & Calcif. & Masas & Calcif. & Masas & Calcif.', body,
          r'AUC en validación cruzada sobre el entrenamiento con los \textit{folds} de M4. Mediana y $g$ sobre las 200 lesiones del M6; '
          r'en el kernel proyectado, la mediana de 0.607 ($e^{-1/2}$) es consecuencia de fijar el ancho de banda por la heurística de la mediana, '
          r'no una propiedad del circuito. El etiquetado diseñado se construye para cada kernel, así que sus columnas no son comparables entre sí. '
          r'En negritas: con las etiquetas diagnósticas, la mejor lectura de cada subconjunto; con el etiquetado diseñado, el mejor entre el kernel cuántico y el clásico.')


def x11_transicion():
    """§6.4: diferencia cuántico − mejor clásico a lo largo de la mezcla de etiquetas (X11)."""
    p = pd.read_csv(RES / 'X11_transicion.csv')
    u = pd.read_csv(RES / 'X11_umbral.csv')
    geo = pd.read_csv(RES / 'X6_geometria.csv')
    alphas = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    kernels = [('ZZ full (C4)', 'ZZ full', 'ZZ completo (C4)'), ('ZZ linear', 'ZZ linear', 'ZZ lineal'),
               ('Projected (ZZ full)', 'Projected (ZZ full), median bandwidth', 'Proyectado (ZZ completo)')]
    body = []
    for ft, title in SUBSETS:
        body.append(f'\\multicolumn{{9}}{{l}}{{\\textit{{{title}}}}} \\\\')
        for q, enc, name in kernels:
            r = p[(p.finding_type == ft) & (p.quantum_kernel == q)].set_index('alpha')
            cells = []
            for a in alphas:
                x = r.loc[a]
                mark = '$^{*}$' if x.ci_low > 0 else ('$^{\\dagger}$' if x.ci_high < 0 else '')
                d = 0.0 if abs(x.difference) < 0.0005 else x.difference      # sin «−0.000»
                txt = ('0.000' if d == 0 else f'{d:+.3f}'.replace('-', '$-$')) + mark
                cells.append(bf(txt) if x.ci_low > 0 else txt)
            a_star = u[(u.finding_type == ft) & (u.quantum_kernel == q)].alpha_star.iloc[0]
            gg = geo[(geo.finding_type == ft) & (geo.encoding == enc)].g_min.iloc[0]
            body.append(f'\\quad {name} & {gg:.2f} & ' + ' & '.join(cells) + f' & {"—" if pd.isna(a_star) else bf(f"{a_star:.1f}")} \\\\')
    write('x11_transicion', 'X11_transicion.csv, X11_umbral.csv y X6_geometria.csv',
          'Diferencia de AUC entre el kernel cuántico y el mejor clasificador clásico al pasar de las etiquetas diagnósticas ($\\alpha = 0$) al etiquetado diseñado ($\\alpha = 1$) (experimento X11).',
          'tab:x11_transicion', 'l r r r r r r r r',
          r'Kernel cuántico & $g$ & $\alpha=0$ & 0.2 & 0.4 & 0.6 & 0.8 & 1 & $\alpha^{*}$', body,
          r'$\alpha$: fracción de lesiones con la etiqueta diseñada; media de cinco máscaras. Validación cruzada sobre el entrenamiento; '
          r'lado clásico con búsqueda anidada entre SVM lineal, polinomiales, gaussianos y XGBoost. $^{*}$ intervalo bootstrap por paciente '
          r'del 95\,\% por encima de cero; $^{\dagger}$ por debajo. $\alpha^{*}$: menor $\alpha$ con el intervalo por encima de cero. '
          r'$g$: \textit{geometric difference} regularizada sobre las 200 lesiones del M6. En negritas, las diferencias con ventaja cuántica significativa y el umbral.')

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    for f in [seleccion, separabilidad_kernels, separabilidad_embeddings, clasificacion, diferencias, spearman, sorteos_theta, theta_entrenado, resumen_resultados,
              x10_arboles, tres_lecturas, x11_transicion]:
        f()
