# fuente: Code/4_Selection_and_Scaling.ipynb · celda de código 8 · líneas 4-14
    d = data[ft]
    cols = selection[ft]
    is_tr = (d.split == "train").values
    tr = d[is_tr]
    # subsample far above the size of train: the quantiles are computed from every training lesion
    qt = QuantileTransformer(n_quantiles=min(1000, len(tr)), output_distribution="uniform",
                             subsample=10**9, random_state=SEED).fit(tr[cols].values)
    mm = MinMaxScaler(feature_range=(0, np.pi), clip=True).fit(tr[cols].values)   # comparison only
    X, Xmm = np.pi * qt.transform(d[cols].values), mm.transform(d[cols].values)
    transformers[ft], scaled[ft] = qt, X
    te_raw = d.loc[~is_tr, cols].values
