# fuente: Code/6_Separability.ipynb · celda de código 3 · líneas 36-48
def center(k):
    # H K H with H = I - 11^T / n
    return k - k.mean(0) - k.mean(1)[:, None] + k.mean()


def alignment_with_null(k, y, perms):
    # uncentered and centered alignment for the observed labels y and for each permuted row of perms (labels +-1)
    n, kc = len(y), center(k)
    yc2 = np.sum((y - y.mean()) ** 2)        # ||H yy^T H||_F; the same for every permutation
    obs_u = y @ k @ y / (np.linalg.norm(k) * n)
    obs_c = y @ kc @ y / (np.linalg.norm(kc) * yc2)
    null_u = np.einsum('pi,ij,pj->p', perms, k, perms) / (np.linalg.norm(k) * n)
    null_c = np.einsum('pi,ij,pj->p', perms, kc, perms) / (np.linalg.norm(kc) * yc2)
