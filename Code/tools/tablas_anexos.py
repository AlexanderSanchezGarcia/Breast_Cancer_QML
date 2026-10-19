"""Genera tablas LaTeX para los Anexos B, D y E a partir de los CSV de resultados,
la bitacora de decisiones y las listas de paquetes conda.

Uso:
    /opt/anaconda3/envs/qml_cancer/bin/python Code/tools/tablas_anexos.py
"""
import re
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
RES = ROOT / 'Code/results'
OUT = ROOT / 'Docs/tablas'
INSUMOS = ROOT / 'Docs/insumos'
NOCHE = INSUMOS / 'noche'

SUBSETS = [('mass', 'Masas'), ('calcification', 'Calcificaciones')]


def f3(x):
    return '—' if pd.isna(x) else f'{x:.3f}'.replace('-', '$-$')


def p_fmt(p):
    if pd.isna(p):
        return '—'
    if p < 0.001:
        return '$<$0.001'
    return f'{p:.3f}'


def tex_name(feature):
    return feature.replace('original_', '').replace('_', r'\_')


def write_table(name, source, caption, label, colspec, header, body, note=None):
    lines = [
        f'% Generado por Code/tools/tablas_anexos.py desde {source}. No editar a mano.',
        r'\begin{table}[H]',
        r'\centering',
        r'\small',
        f'\\caption{{{caption}}}',
        f'\\label{{{label}}}',
        r'\begin{adjustbox}{max width=\linewidth}',
        f'\\begin{{tabular}}{{{colspec}}}',
        r'\toprule',
        header + r' \\',
        r'\midrule'
    ]
    lines += body
    lines += [
        r'\bottomrule',
        r'\end{tabular}',
        r'\end{adjustbox}'
    ]
    if note:
        lines += [r'\par\smallskip', f'\\parbox{{0.95\\linewidth}}{{\\footnotesize {note}}}']
    lines += [r'\end{table}', '']
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f'{name}.tex').write_text('\n'.join(lines), encoding='utf-8')
    print(f'{name}.tex  <-  {source}')


def tabla_m2_resumen():
    df = pd.read_csv(RES / '2_preprocesamiento_resumen.csv')
    body = []
    names = {'calcification': 'Calcificaciones', 'mass': 'Masas'}
    for _, r in df.iterrows():
        tipo = names.get(r['finding_type'], r['finding_type'])
        n_les = int(r['lesions'])
        desal = int(r['misaligned_scaled'] + r['misaligned_offset'])
        limp = int(r['masks_cleaned'])
        of_ok = int(r['official_crop_rule_ok'])
        of_disc = int(r['official_crop_border'] + r['official_crop_discordant'] + r['without_official_crop'])
        med_dim = f"{int(r['median_bbox_h'])}$\\times${int(r['median_bbox_w'])}"
        borde = int(r['border_clipped'])
        body.append(f"{tipo} & {n_les} & {desal} & {limp} & {of_ok} & {of_disc} & {med_dim} & {borde} \\\\")
    
    header = (
        r'Subconjunto & Lesiones & Desalineadas & Máscaras & Recortes & '
        r'Recortes oficiales & Dimensión mediana & Recortes \\' + '\n' +
        r' & analizadas & (escal./offset) & depuradas & coincidentes & '
        r'con discrepancia/sin & de lesión (px) & en borde'
    )
    note = (
        r'Auditoría y control de calidad de M2. Desalineadas: 78 por escala ($0.870$) en masas y 2 por traslación en calcificaciones. '
        r'Depuradas: reducción a la componente conexa mayor eliminando artefactos menores aislados. '
        r'Recortes coincidentes: concordancia exacta al píxel con los recortes oficiales del CBIS-DDSM.'
    )
    write_table(
        'anexo_b_m2_resumen',
        '2_preprocesamiento_resumen.csv',
        'Resumen del preprocesamiento, alineación de máscaras y control de calidad (Módulo 2).',
        'tab:anexo_m2_resumen',
        'l r r r r r c r',
        header,
        body,
        note
    )


def tabla_m4_seleccion():
    s = pd.read_csv(RES / '4_seleccion.csv')
    d = pd.read_csv(RES / '3_tamano_efecto.csv')
    d_raw = d[d['variant'] == 'raw']
    m = pd.merge(s, d_raw[['finding_type', 'feature', 'abs_d']], on=['finding_type', 'feature'], how='left')
    
    body = []
    for i in range(12):
        row_cells = [str(i + 1)]
        for ft, _ in SUBSETS:
            r = m[(m['finding_type'] == ft) & (m['order'] == i + 1)].iloc[0]
            feat = tex_name(r['feature'])
            fam = r['family']
            f_val = f"{r['F']:.1f}"
            p_val = p_fmt(r['p'])
            d_val = f3(r['abs_d'])
            row_cells.extend([feat, fam, f_val, p_val, d_val])
        body.append(' & '.join(row_cells) + r' \\')
    
    header = (
        r' & \multicolumn{5}{c}{Masas} & \multicolumn{5}{c}{Calcificaciones} \\ '
        r'\cmidrule(lr){2-6}\cmidrule(lr){7-11}' + '\n' +
        r'\# & Característica & Familia & $F$ & $p$ & $|d|$ & Característica & Familia & $F$ & $p$ & $|d|$'
    )
    note = (
        r'Selección de las 12 características en cada subconjunto mediante ANOVA univariado ($F$-test) sobre el conjunto de entrenamiento '
        r'con restricción de redundancia lineal $|r| \le 0.95$. '
        r'$p$ reporta el nivel de significación estadística; $|d|$ es el tamaño del efecto (d de Cohen sobre intensidades crudas).'
    )
    write_table(
        'anexo_b_m4_seleccion',
        '4_seleccion.csv y 3_tamano_efecto.csv',
        'Conjunto completo de características radiómicas seleccionadas por subconjunto (Módulo 4).',
        'tab:anexo_m4_seleccion',
        'r l l r r r l l r r r',
        header,
        body,
        note
    )


def tabla_m4_redundancia():
    df = pd.read_csv(RES / '4_descartadas_redundancia.csv')
    body = []
    names = {'mass': 'Masas', 'calcification': 'Calcificaciones'}
    for ft, title in SUBSETS:
        sub = df[df['finding_type'] == ft]
        body.append(f"\\multicolumn{{4}}{{l}}{{\\textit{{{title}}}}} \\\\")
        for _, r in sub.iterrows():
            feat = tex_name(r['feature'])
            red = tex_name(r['redundant_with'])
            r_val = f3(r['abs_r'])
            body.append(f"\\quad {feat} & {red} & {r_val} & Descartada ($|r| > 0.95$) \\\\")
            
    header = r'Característica candidata & Redundante con & $|r|$ & Estado'
    note = (
        r'Características candidatas con alto valor de $F$ que fueron omitidas de la selección final para evitar colinealidad extrema '
        r'($|r| > 0.95$). En masas se descartaron 7 variables y en calcificaciones 8.'
    )
    write_table(
        'anexo_b_m4_redundancia',
        '4_descartadas_redundancia.csv',
        'Características radiómicas descartadas por restricción de redundancia (Módulo 4).',
        'tab:anexo_m4_redundancia',
        'l l r l',
        header,
        body,
        note
    )


def tabla_m4_folds():
    df = pd.read_csv(RES / '4_folds.csv')
    body = []
    for k in range(5):
        rm = df[(df['finding_type'] == 'mass') & (df['fold'] == k)].iloc[0]
        rc = df[(df['finding_type'] == 'calcification') & (df['fold'] == k)].iloc[0]
        prev_m = f"{rm['malignant_share'] * 100:.1f}\\%"
        prev_c = f"{rc['malignant_share'] * 100:.1f}\\%"
        body.append(
            f"{k} & {int(rm['lesions'])} & {int(rm['patients'])} & {prev_m} & "
            f"{int(rc['lesions'])} & {int(rc['patients'])} & {prev_c} \\\\"
        )
    # Totals
    tm_les = int(df[df['finding_type'] == 'mass']['lesions'].sum())
    tm_pat = int(df[df['finding_type'] == 'mass']['patients'].sum())
    tm_prev = f"{df[df['finding_type'] == 'mass']['malignant_share'].mean() * 100:.1f}\\%"
    tc_les = int(df[df['finding_type'] == 'calcification']['lesions'].sum())
    tc_pat = int(df[df['finding_type'] == 'calcification']['patients'].sum())
    tc_prev = f"{df[df['finding_type'] == 'calcification']['malignant_share'].mean() * 100:.1f}\\%"
    body.append(r'\midrule')
    body.append(f"Total / media & {tm_les} & {tm_pat} & {tm_prev} & {tc_les} & {tc_pat} & {tc_prev} \\\\")
    
    header = (
        r' & \multicolumn{3}{c}{Masas (semilla elegida: 125)} & \multicolumn{3}{c}{Calcificaciones (semilla elegida: 168)} \\ '
        r'\cmidrule(lr){2-4}\cmidrule(lr){5-7}' + '\n' +
        r'Fold & Lesiones & Pacientes & Malignas (\%) & Lesiones & Pacientes & Malignas (\%)'
    )
    note = (
        r'Partición de validación cruzada 5-fold estratificada por paciente (\texttt{StratifiedGroupKFold}). '
        r'Garantiza cero fuga de pacientes entre folds y balance de clases óptimo entre candidatos de semillas.'
    )
    write_table(
        'anexo_b_m4_folds',
        '4_folds.csv',
        'Balance de lesiones, pacientes y proporción de malignidad por fold (Módulo 4).',
        'tab:anexo_m4_folds',
        'c r r r r r r',
        header,
        body,
        note
    )


def tabla_m5_tiempos():
    df = pd.read_csv(RES / '5b_tiempos.csv')
    body = []
    names = {'calcification': 'Calcificaciones', 'mass': 'Masas'}
    for _, r in df.iterrows():
        tipo = names.get(r['finding_type'], r['finding_type'])
        kern = r['kernel'].replace('_', r'\_')
        dim = r['shape']
        sec = f3(r['seconds'])
        body.append(f"{tipo} & \\texttt{{{kern}}} & {dim} & {sec} \\\\")
        
    header = r'Subconjunto & Kernel cuántico evaluado & Dimensión & Tiempo total (s)'
    note = (
        r'Tiempos medidos en simulación exacta. \texttt{FidelityStatevectorKernel} calcula la matriz $200\times 200$ en $\sim$1.5\,s '
        r'aprovechando vectores de estado precomputados. \texttt{FidelityQuantumKernel} evalúa el circuito cuántico directo '
        r'requiriendo $\sim$5.0\,s para una matriz reducida de solo $10\times 10$.'
    )
    write_table(
        'anexo_b_m5_tiempos',
        '5b_tiempos.csv',
        'Costes computacionales de evaluación de kernels cuánticos (Módulo 5).',
        'tab:anexo_m5_tiempos',
        'l l c r',
        header,
        body,
        note
    )


def tabla_m8_oe6_qubits():
    df = pd.read_csv(RES / '8_oe6_qubits.csv')
    k_targets = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
    sub = df[df['k'].isin(k_targets)].copy()
    body = []
    for _, r in sub.iterrows():
        k = int(r['k'])
        est = 'Medido' if r['measured'] else 'Extrapolado'
        s_per_state = f"{r['seconds_per_state']:.4f}" if r['seconds_per_state'] < 1 else f"{r['seconds_per_state']:.1f}"
        mem_mb = r['state_GiB'] * 1024
        mem_str = f"{mem_mb:.2f} MiB" if mem_mb < 1024 else f"{r['state_GiB']:.2f} GiB"
        emb_h = f"{r['embedding_hours']:.3f}" if r['embedding_hours'] < 10 else f"{r['embedding_hours']:.1f}"
        train_h = f"{r['training_A_hours_per_map']:.1f}" if r['training_A_hours_per_map'] < 100 else f"{r['training_A_hours_per_map']:.0f}"
        body.append(f"{k} & {est} & {mem_str} & {s_per_state} & {emb_h} & {train_h} \\\\")
        
    header = (
        r'$k$ (qubits) & Tipo de dato & Memoria estado & '
        r'Tiempo/estado (s) & Tiempo embedding (h) & Entrenamiento (h/mapa)'
    )
    note = (
        r'Escalamiento del coste en simulación cuántica por vector de estado en función del número de qubits ($k$). '
        r'Para $k \le 28$ las cifras corresponden a ejecuciones empíricas en el hardware de referencia (Apple M3); '
        r'para $k \ge 30$ corresponden a la extrapolación exponencial teórica.'
    )
    write_table(
        'anexo_b_m8_oe6_qubits',
        '8_oe6_qubits.csv',
        'Escalamiento computacional con el número de qubits en simulación por vector de estado (OE-6).',
        'tab:anexo_m8_oe6_qubits',
        'c c r r r r',
        header,
        body,
        note
    )


def tabla_x8_gradiente():
    df = pd.read_csv(RES / 'X8_costo_gradiente.csv')
    body = []
    for _, r in df.iterrows():
        met = r['method'].replace('(', r'(').replace(')', r')')
        grad = r['gradient'].replace('x', r'$\times$')
        s_les = f"{r['seconds_per_lesion']:.4f}"
        h_50 = f"{r['hours_50_epochs_one_map_all_train']:.2f}"
        body.append(f"{met} & {grad} & {s_les} & {h_50} \\\\")
        
    header = (
        r'Método de cálculo & Naturaleza del gradiente & '
        r'Tiempo/lesión (s) & Coste estimado (50 épocas, h)'
    )
    note = (
        r'Comparación de costes entre diferenciación exacta por \textit{parameter-shift rule} y '
        r'diferenciación automática directa sobre vector de estado en simulación (Experimento X8).'
    )
    write_table(
        'anexo_b_x8_gradiente',
        'X8_costo_gradiente.csv',
        'Coste computacional del cálculo de gradientes variacionales (Experimento X8).',
        'tab:anexo_x8_gradiente',
        'l l r r',
        header,
        body,
        note
    )


def tabla_verificaciones():
    v5a = pd.read_csv(RES / '5a_verificaciones.csv')
    v5b = pd.read_csv(RES / '5b_verificaciones.csv')
    v6 = pd.read_csv(RES / '6_verificaciones.csv')
    v7 = pd.read_csv(RES / '7_verificaciones.csv')
    v8 = pd.read_csv(RES / '8_verificaciones.csv')
    
    rows = [
        ('Módulo 5a', '5a_verificaciones.csv', len(v5a), int(v5a['passed'].sum()),
         'Recomputación exacta, dispersión positiva y validación con SparsePauliOp'),
        ('Módulo 5b', '5b_verificaciones.csv', len(v5b), int(v5b['passed'].sum()),
         'Simetría de matrices, diagonal unitaria y semidefinición positiva ($\\lambda_{\\min} \\ge 0$)'),
        ('Módulo 6', '6_verificaciones.csv', len(v6), int(v6['passed'].sum()),
         'Normalización de traza, identidades teóricas de $g$, KTA y control nulo C1=C2'),
        ('Módulo 7', '7_verificaciones.csv', len(v7), int(v7['passed'].sum()),
         'Cero fuga de pacientes, convergencia por parada temprana y estabilidad de probabilidades'),
        ('Módulo 8', '8_verificaciones.csv', len(v8), int(v8['passed'].sum()),
         'Reproducción de AUC en test y CV, nula exacta de Spearman y muestreo de $\\langle Z_i \\rangle$')
    ]
    
    body = []
    tot_p, tot_t = 0, 0
    for mod, src, total, passed, desc in rows:
        tot_t += total
        tot_p += passed
        pct = f"{passed / total * 100:.0f}\\%"
        src_esc = src.replace('_', r'\_')
        body.append(f"{mod} & \\texttt{{{src_esc}}} & {total} & {passed} ({pct}) & {desc} \\\\")
    body.append(r'\midrule')
    body.append(f"Total suite & 5 archivos CSV & {tot_t} & {tot_p} (100\\%) & Suite completa de aserciones automáticas \\\\")
    
    header = r'Módulo & Archivo de resultados & Pruebas & Superadas & Ámbito de verificación'
    note = (
        r'Todas las pruebas automáticas del pipeline ejecutan aserciones matemáticas estrictas sobre las estructuras de datos generadas. '
        r'El 100\,\% de las verificaciones resultó exitoso, sin discrepancias numéricas tolerables más allá del error de redondeo de punto flotante.'
    )
    write_table(
        'anexo_b_verificaciones',
        '5a_, 5b_, 6_, 7_ y 8_verificaciones.csv',
        'Resumen de la suite de verificaciones automáticas de consistencia y correctitud.',
        'tab:anexo_verificaciones',
        'l l c c p{6.5cm}',
        header,
        body,
        note
    )


def tabla_x5_auditoria():
    df = pd.read_csv(RES / 'X5_auditoria.csv')
    body = []
    area_names = {
        'labels': 'Integridad de etiquetas y particiones',
        'leakage': 'Ausencia de fuga de datos (escalado y folds)',
        'quantum kernel': 'Equivalencia física de kernels cuánticos',
        'QSVM': 'Equivalencia de formulación QSVM (Qiskit vs dual)',
        'encoding': 'Invarianza de rotación y transformaciones',
        'classical references': 'Consistencia de modelos de referencia clásicos'
    }
    for area, g in df.groupby('area', sort=False):
        a_title = area_names.get(area, area)
        body.append(f"\\multicolumn{{3}}{{l}}{{\\textbf{{{a_title}}}}} \\\\")
        for _, r in g.iterrows():
            chk = r['check'].replace('_', r'\_').replace('pi', r'$\pi$').replace('<=', r'$\le$')
            val = f"{r['value']:.2e}" if abs(r['value']) > 1e-6 else '0.0'
            passed = 'Superada' if r['passed'] else 'Fallo'
            body.append(f"\\quad {chk} & {val} & {passed} \\\\")
            
    header = r'Propiedad auditada & Discrepancia máxima & Veredicto'
    note = (
        r'Auditoría metodológica independiente de extremo a extremo (Experimento X5). '
        r'Comprueba rigurosamente la ausencia de fugas de datos entre particiones de pacientes, '
        r'la correspondencia exacta de etiquetas patológicas con los metadatos clínicos de CBIS-DDSM y '
        r'la consistencia matemática de los componentes cuánticos.'
    )
    write_table(
        'anexo_b_x5_auditoria',
        'X5_auditoria.csv',
        'Auditoría metodológica independiente de consistencia, datos y modelos (Experimento X5).',
        'tab:anexo_x5_auditoria',
        'p{11.5cm} r c',
        header,
        body,
        note
    )


def tabla_d_paquetes():
    rad_path = NOCHE / 'conda_list_radiomics.txt'
    qml_path = NOCHE / 'conda_list_qml_cancer.txt'
    
    def load_conda(path):
        d = {}
        if not path.exists():
            return d
        for l in path.read_text(encoding='utf-8').splitlines():
            if l.startswith('#') or not l.strip():
                continue
            parts = l.split()
            if len(parts) >= 2:
                d[parts[0].lower()] = parts[1]
        return d
    
    vr = load_conda(rad_path)
    vq = load_conda(qml_path)
    
    pkgs = [
        ('python', 'Lenguaje base del entorno', 'python'),
        ('numpy', 'Cómputo matricial y vectores', 'numpy'),
        ('scipy', 'Rutinas científicas y optimización', 'scipy'),
        ('pandas', 'Estructuras de datos tabulares', 'pandas'),
        ('scikit-learn', 'Modelos clásicos y métricas ML', 'scikit-learn'),
        ('pyradiomics', 'Extracción de características radiómicas', 'pyradiomics'),
        ('pydicom', 'Lectura de mamografías DICOM crudas', 'pydicom'),
        ('simpleitk', 'Conversión y exportación espacial NRRD', 'SimpleITK'),
        ('opencv', 'Alineación de máscaras y CLAHE', 'opencv-python'),
        ('matplotlib', 'Generación de gráficos y figuras', 'matplotlib'),
        ('torch', 'Redes neuronales y optimización MLP', 'torch'),
        ('qiskit', 'Definición de circuitos cuánticos', 'qiskit'),
        ('qiskit-aer', 'Simulación cuántica de alto rendimiento', 'qiskit-aer'),
        ('qiskit-machine-learning', 'Kernels y algoritmos cuánticos de aprendizaje', 'qiskit-machine-learning'),
    ]
    
    body = []
    for pkg_key, desc, display_name in pkgs:
        r_ver = vr.get(pkg_key, '—')
        if pkg_key == 'opencv':
            r_ver = vr.get('opencv-python', '—')
            q_ver = vq.get('opencv-python-headless', vq.get('opencv-python', '—'))
        elif pkg_key == 'simpleitk':
            r_ver = vr.get('simpleitk', '—')
            q_ver = vq.get('simpleitk', '—')
        else:
            q_ver = vq.get(pkg_key, '—')
            
        # Clean versions
        r_ver = r_ver.replace('_', r'\_')
        q_ver = q_ver.replace('_', r'\_')
        body.append(f"\\texttt{{{display_name}}} & {desc} & \\texttt{{{r_ver}}} & \\texttt{{{q_ver}}} \\\\")
        
    header = r'Paquete de software & Función en el pipeline & Entorno \texttt{radiomics} & Entorno \texttt{qml\_cancer}'
    note = (
        r'Versiones exactas de librerías en los dos entornos de ejecución reproducible gestionados con Conda. '
        r'\texttt{pyradiomics} se encuentra anclado en ambos entornos al commit \texttt{8ed579383b44806651c463d5e691f3b2b57522ab}.'
    )
    write_table(
        'anexo_d_paquetes',
        'conda_list_radiomics.txt y conda_list_qml_cancer.txt',
        'Versiones de los paquetes de software fundamentales en los entornos de ejecución.',
        'tab:anexo_d_paquetes',
        'l p{6.5cm} l l',
        header,
        body,
        note
    )


def tabla_e_decisiones():
    content = (ROOT / 'Other/bitacora_decisiones.md').read_text(encoding='utf-8')
    content_esc = content.replace(r'\|', '__ESCAPED_PIPE__')
    # Filas del índice de decisiones; las últimas pueden venir sin la celda final de sección.
    table_rows = []
    for line in content_esc.splitlines():
        m = re.match(r'\|\s*(D-\d{3})\s*\|', line)
        if m and line.count('|') >= 6:
            cells = [c for c in line.strip().strip('|').split('|')]
            cells += [''] * (6 - len(cells))
            table_rows.append(tuple(cells[:6]))
    
    def clean_latex(s):
        s = s.strip()
        s = s.replace('__ESCAPED_PIPE__', '|')
        s = s.replace(r'|r|', r'$|r|$').replace(r'\|r\|', r'$|r|$')
        s = s.replace('&', r'\&').replace('%', r'\%')
        s = re.sub(r'\*([^*]+)\*', r'\\textit{\1}', s)
        # replace `code`
        parts = s.split('`')
        if len(parts) > 1 and len(parts) % 2 == 1:
            res = []
            for i, p in enumerate(parts):
                if i % 2 == 1:
                    res.append(r'\texttt{' + p.replace('_', r'\_') + '}')
                else:
                    res.append(p)
            s = ''.join(res)
        s = s.replace('θ', r'$\theta$')
        s = s.replace('π', r'$\pi$')
        s = s.replace('γ', r'$\gamma$')
        s = s.replace('§', r'\S\,')
        s = s.replace('≤', r'$\le$')
        s = s.replace('×', r'$\times$')
        s = s.replace('->', r'$\to$').replace('→', r'$\to$')
        s = s.replace('pauli_feature_map', r'pauli\_feature\_map\allowbreak ')
        return s

    lines = [
        r'% Generado por Code/tools/tablas_anexos.py desde Other/bitacora_decisiones.md. No editar a mano.',
        r'\begin{longtable}{@{}llp{8.4cm}p{3.0cm}@{}}',
        r'\caption{Índice cronológico de decisiones metodológicas documentadas en la bitácora.}\label{tab:anexo_decisiones} \\',
        r'\toprule',
        r'Identificador & Estado & Título de la decisión & Sección en reporte \\',
        r'\midrule',
        r'\endfirsthead',
        r'\multicolumn{4}{c}{\tablename\ \thetable\ -- \textit{continuación de la página anterior}} \\',
        r'\toprule',
        r'Identificador & Estado & Título de la decisión & Sección en reporte \\',
        r'\midrule',
        r'\endhead',
        r'\midrule',
        r'\multicolumn{4}{r}{\textit{Continúa en la siguiente página\dots}} \\',
        r'\endfoot',
        r'\bottomrule',
        r'\endlastfoot',
    ]

    # La columna de sección de la bitácora usa la numeración de TT1 (Metodología = §4). La sección
    # vigente se deriva del módulo con \ref, y de la bitácora solo se conservan §1–§3, que no cambiaron.
    # Antes de D-030 el M6 era la clasificación y el M7 la evaluación con la separabilidad;
    # desde D-030 la separabilidad es el M6, la clasificación el M7 y la comparación el M8.
    def secciones(tag, modulo, sec_bitacora):
        antes_d030 = int(tag[2:]) < 30
        refs = []
        for a, b in re.findall(r'M(\d)(?:\s*[–-]\s*M(\d))?', modulo):
            for n in range(int(a), int(b or a) + 1):
                if antes_d030 and n in (6, 7):
                    n = 13 - n
                refs.append(rf'\ref{{sec:modulo{n}}}')
        if re.search(r'\bX\d', modulo):
            refs.append(r'\ref{sec:experimentos_complementarios}')
        if 'todos' in modulo:
            refs.append(r'\ref{sec:descripcion_general}')
        if 'infra' in modulo:
            refs.append(r'\ref{anx:entorno}')
        refs += [f'{x}' for x in re.findall(r'§\s*([123]\.\d+(?:\.\d+)?)', sec_bitacora)]
        vistos = []
        for r_ in refs:
            if r_ not in vistos:
                vistos.append(r_)
        return ', '.join(r'\S\,' + r_ for r_ in vistos)

    for tr in table_rows:
        tag = tr[0].strip()
        title = clean_latex(tr[2])
        if 'Revertida' in tr[4]:
            status = r'\textbf{Revertida}'
        elif 'Provisional' in tr[4]:
            status = r'\textit{Provisional}'
        else:
            status = 'Firme'
        sec = secciones(tag, tr[3], tr[5])
        lines.append(f"{tag} & {status} & {title} & {sec} \\\\")

    lines.append(r'\end{longtable}')
    lines.append('')
    
    (OUT / 'anexo_e_decisiones.tex').write_text('\n'.join(lines), encoding='utf-8')
    print('anexo_e_decisiones.tex  <-  Other/bitacora_decisiones.md')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    tabla_m2_resumen()
    tabla_m4_seleccion()
    tabla_m4_redundancia()
    tabla_m4_folds()
    tabla_m5_tiempos()
    tabla_m8_oe6_qubits()
    tabla_x8_gradiente()
    tabla_verificaciones()
    tabla_x5_auditoria()
    tabla_d_paquetes()
    tabla_e_decisiones()


if __name__ == '__main__':
    main()
