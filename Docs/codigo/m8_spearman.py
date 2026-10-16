# fuente: Code/8_Comparison.ipynb · celda de código 6 · líneas 1-21
PERMS = np.array(list(itertools.permutations(range(5))))


def ranks(values, higher_is_better):
    # rank 1 = most separated or best classified; tied values share their average rank. Values are rounded to
    # 9 decimals first: the metrics of C1 and C2 differ only by floating-point noise (1e-14), and that is a tie (D-016)
    v = np.round(np.asarray(values, float), 9)
    return rankdata(-v if higher_is_better else v, method='average')


def rho(a, b):
    return float(np.corrcoef(a, b)[0, 1])


def exact_null(sep_ranks, cls_ranks):
    return np.array([rho(sep_ranks, cls_ranks[p]) for p in PERMS])


def spearman_exact(sep_ranks, cls_ranks):
    r = rho(sep_ranks, cls_ranks)
    return r, float(np.mean(np.abs(exact_null(sep_ranks, cls_ranks)) >= abs(r) - 1e-9))
