# fuente: Code/8_Comparison.ipynb · celda de código 17 · líneas 1-21
rng = np.random.default_rng(SEED)
shot_rows, law = [], []
t0 = time.perf_counter()
for ft in FINDINGS:
    frame = frames[ft]
    for q in QUANTUM:
        p, z = probs[(ft, q)], frame[cols(q)].to_numpy()
        spread = float(z.std(axis=0).mean())                         # between-lesion spread, as in 5a
        mean_var = float((1 - z ** 2).mean())                        # mean of 1 - <Z_i>^2 over lesions and qubits
        exact = main_cv[(main_cv.finding_type == ft) & (main_cv.condition == q)].auc.mean()
        shot_rows.append({'finding_type': ft, 'map': q, 'shots': np.inf, 'repeat': 0, 'noise_sd': 0.0, 'theory_sd': 0.0,
                          'spread': spread, 'noise_over_spread': 0.0, 'cv_auc': exact})
        for n in SHOTS:
            for rep in range(SHOT_REPEATS):
                z_hat = rng.multinomial(n, p) @ signs / n
                e = z_hat - z
                theory = np.sqrt(mean_var / n)
                law.append({'finding_type': ft, 'map': q, 'shots': n, 'ratio_sd': e.std() / theory,
                            'mean_error_in_se': abs(e.mean()) / (theory / np.sqrt(e.size))})
                shot_rows.append({'finding_type': ft, 'map': q, 'shots': n, 'repeat': rep, 'noise_sd': float(e.std()), 'theory_sd': theory,
                                  'spread': spread, 'noise_over_spread': float(e.std()) / spread, 'cv_auc': cv_auc(z_hat, frame).mean()})
