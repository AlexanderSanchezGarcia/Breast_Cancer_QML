# fuente: Code/5b_Quantum_Kernels.ipynb · celda de código 4 · líneas 11-26
feature_maps = {
    'C4': zz_feature_map(12, reps=1),
    'C5': pauli_feature_map(12, reps=1, paulis=['Y', 'ZZ']),
}
kernels, gammas, timing_rows = {}, {}, []
for finding in FINDINGS:
    feature_cols = [c for c in data[finding].columns if c.startswith('x_')]
    X_train = data[finding].loc[data[finding].split.eq('train'), feature_cols].to_numpy(dtype=float)
    train_d2 = pairwise_sqdist(X_train)
    gamma = 1.0 / (2.0 * np.median(train_d2[np.triu_indices_from(train_d2, k=1)]))
    gammas[finding] = gamma
    X = Xs[finding]
    results = {'K_C': rbf_kernel(X, gamma)}
    for name, feature_map in feature_maps.items():
        t0 = time.perf_counter()
        results[f'K_Q_{name}'] = FidelityStatevectorKernel(feature_map=feature_map).evaluate(X)
