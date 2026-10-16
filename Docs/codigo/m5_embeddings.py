# fuente: Code/5a_Embeddings.ipynb · celda de código 2 · líneas 10-20
ansatz = real_amplitudes(N_QUBITS, reps=1)
theta = np.random.default_rng(SEED).uniform(0, 2*np.pi, ansatz.num_parameters)
feature_maps = {'C4': zz_feature_map(N_QUBITS, reps=1), 'C5': pauli_feature_map(N_QUBITS, reps=1, paulis=['Y', 'ZZ'])}
basis = np.arange(2**N_QUBITS)[:, None]
signs = 1.0 - 2.0 * ((basis >> np.arange(N_QUBITS)) & 1)

def exact_embedding(feature_map, x):
    values = {p: float(v) for p, v in zip(feature_map.parameters, x)}
    values.update({p: float(v) for p, v in zip(ansatz.parameters, theta)})
    circuit = feature_map.compose(ansatz).assign_parameters(values, inplace=False)
    return Statevector.from_instruction(circuit).probabilities() @ signs
