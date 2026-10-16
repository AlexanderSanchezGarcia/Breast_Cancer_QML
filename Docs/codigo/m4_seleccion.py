# fuente: Code/4_Selection_and_Scaling.ipynb · celda de código 5 · líneas 1-14
def select(ft, r_max, k=K):
    tr = data[ft][data[ft].split == "train"]
    C = tr[FEATURES].corr().abs()
    chosen, skipped = [], []
    for f in scores[ft].feature:
        clash = [(s, C.loc[f, s]) for s in chosen if C.loc[f, s] > r_max]
        if clash:
            s, r = max(clash, key=lambda c: c[1])
            skipped.append(dict(feature=f, redundant_with=s, abs_r=r))
        else:
            chosen.append(f)
        if len(chosen) == k:
            break
    return chosen, pd.DataFrame(skipped), C
