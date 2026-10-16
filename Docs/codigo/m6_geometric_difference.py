# fuente: Code/6_Separability.ipynb · celda de código 3 · líneas 20-33
def geometric_difference(kq, kc, lambdas):
    # g(K_C || K_Q): eq. (F19) for g_gen and eq. (F20) for g_tra; lambda = 0 gives the unregularized eq. (5)
    sq = psd_sqrt(kq)
    t, v = eigh(sym(kc))
    t = np.clip(t, 0, None)
    out = {}
    for lam in lambdas:
        if lam == 0:
            out[lam] = (np.sqrt(top_eigenvalue(sq @ ((v / t) @ v.T) @ sq)), 0.0) if t.min() > 0 else (np.inf, 0.0)
        else:
            gen = (v * (t / (t + lam) ** 2)) @ v.T          # sqrt(K_C) (K_C + lam I)^-2 sqrt(K_C)
            tra = (v * (1 / (t + lam) ** 2)) @ v.T          # (K_C + lam I)^-2
            out[lam] = (np.sqrt(top_eigenvalue(sq @ gen @ sq)), lam * np.sqrt(top_eigenvalue(sq @ tra @ sq)))
    return out
