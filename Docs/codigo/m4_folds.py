# fuente: Code/4_Selection_and_Scaling.ipynb · celda de código 9 · líneas 1-12
def group_folds(tr, seed):
    y, g = tr.label.values, tr.patient_id.values
    fold = np.empty(len(tr), int)
    for k, (_, va) in enumerate(StratifiedGroupKFold(N_FOLDS, shuffle=True, random_state=seed).split(tr, y, g)):
        fold[va] = k
    return fold


def max_dev(tr, fold):
    y = tr.label.values
    return float(np.abs(pd.Series(y).groupby(fold).mean() - y.mean()).max())

