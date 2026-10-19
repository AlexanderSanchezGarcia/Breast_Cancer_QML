# Referencias por revisar · TT 2026-B039

> Lista de trabajo, no bibliografía final. Cada entrada separa lo que **ya se verificó** de lo que **falta comprobar en el PDF** antes de citarla en el reporte (regla 2 de `CLAUDE.md`). Al pasarla a `Technical_Report.bib`, marca la casilla y anota la sección donde se usa.

**Creado:** 2026-10-07 · **Origen:** conversación sobre qué problemas siguen la geometría de un kernel cuántico (H-048).

---

## 1. Ventaja cuántica con datos clásicos y estructura algebraica oculta

### Liu, Arunachalam y Temme (2021) · *A rigorous and robust quantum speed-up in supervised machine learning*
- [ ] Revisado en el PDF · [ ] Agregado al `.bib`
- **Verificado (resumen de arXiv):**
  - Autores, título, año y arXiv:2010.02174.
  - Construyen una familia de conjuntos de datos donde ningún clasificador clásico supera de forma apreciable al azar, suponiendo la dificultad del logaritmo discreto.
  - Un SVM con kernel cuántico, estimado en un computador cuántico tolerante a fallos, clasifica con alta precisión. Es robusto al error aditivo de muestreo y solo requiere acceso clásico a los datos.
- **Falta verificar:** revista y volumen de la versión publicada (*Nature Physics*, según la memoria; no confirmado); en qué sentido exacto el kernel es «difícil»; el tamaño de los conjuntos.
- **Uso previsto:** §2 y §7. Es el análogo riguroso de Shor en clasificación. La estructura está en la **etiqueta** (definida por el logaritmo discreto), no en la codificación.
- **Enlace:** https://arxiv.org/abs/2010.02174

### Glick, Gujarati et al. (IBM) · *Covariant quantum kernels for data with group structure*
- [ ] Revisado en el PDF · [ ] Agregado al `.bib`
- **Verificado (ficha de IBM y búsqueda):**
  - Título, autores principales y arXiv:2105.03406.
  - El problema es clasificar a qué clase lateral (*coset*) de un subgrupo pertenece un elemento perturbado.
  - Los kernels se construyen con representaciones unitarias del grupo y respetan sus simetrías.
  - Se demostró con 27 qubits de un procesador superconductor.
- **Falta verificar:** **año y revista de la versión publicada** (el preprint es de 2021; la búsqueda mostró fechas de 2022, y no se confirmó si salió en una revista en 2024); la lista completa de autores.
- **Uso previsto:** §7. Datos con estructura de grupo como segundo ejemplo de etiquetas alineadas con la geometría cuántica.
- **Enlaces:** https://www.arxiv.org/pdf/2105.03406 · https://research.ibm.com/publications/covariant-quantum-kernels-for-data-with-group-structure--1

---

## 2. Ventaja con datos que ya son cuánticos

### Huang, Broughton, Cotler et al. (2022) · *Quantum advantage in learning from experiments*
- [ ] Revisado en el PDF · [ ] Agregado al `.bib`
- **Verificado (búsqueda y ficha de Google Research):**
  - *Science* 376, 1182–1186 (2022); arXiv:2112.00778.
  - Demuestran que un aprendiz con memoria cuántica necesita **exponencialmente menos experimentos** para predecir propiedades de sistemas físicos, hacer PCA cuántico sobre estados ruidosos y aprender modelos de dinámica.
  - Experimento con hasta 40 qubits superconductores y 1,300 compuertas.
- **Falta verificar:** la lista completa de autores y en qué tareas la ventaja requiere memoria cuántica frente a mediciones convencionales.
- **Uso previsto:** §7. Tercera fila de la tabla «tipos de problema»: la ventaja aparece cuando el dato *es* un estado cuántico. Una mamografía no lo es, porque el detector mide los fotones y destruye la información cuántica.
- **Enlaces:** https://arxiv.org/pdf/2112.00778 · https://research.google/pubs/quantum-advantage-in-learning-from-experiments/

---

## 3. Representaciones cuánticas de imágenes

### *Analysis of Quantum Image Representations for Supervised Classification* (2025)
- [ ] Revisado en el PDF · [ ] Agregado al `.bib`
- **Verificado:** título y arXiv:2507.22039. Compara representaciones como FRQI y NEQR para clasificación supervisada.
- **Falta verificar:** autores, conclusiones y si discute el coste de preparación del estado.
- **Uso previsto:** §7. Codificar imágenes como estados no las convierte en datos cuánticos, y el coste de carga suele anular la ventaja de usar pocos qubits.
- **Dato a confirmar en la fuente original de FRQI:** la complejidad de preparación O(2⁴ⁿ) que reporta la búsqueda.
- **Enlace:** https://arxiv.org/html/2507.22039v2

### Fuentes originales de FRQI y NEQR
- [ ] Localizar y verificar · [ ] Agregado al `.bib`
- No se buscaron. De memoria: Le et al. (2011) para FRQI y Zhang et al. (2013) para NEQR. **No citar sin verificar.**

---

## 4. Otras referencias mencionadas en la bitácora y aún no verificadas

| Referencia | Dónde se menciona | Qué falta |
|---|---|---|
| Concentración exponencial de kernels cuánticos (por localizar) | H-031 | Encontrar la referencia correcta y verificarla |
| Guyon y Elisseeff (2003), *An introduction to variable and feature selection*, JMLR 3 | H-035 | Verificar contra la fuente |
| Modelos cuánticos como series de Fourier en los ángulos codificados (Schuld et al., 2021, de memoria) | Explicación del 2026-10-07 sobre el prior de Fourier | Localizar y verificar |
| Kernels proyectados y *feature maps* entrenables (Hubregtsen et al. y otros) | Ideas de trabajo futuro (H-044, X6) | Localizar y verificar, si se mencionan en §7 |

## 5. Ya verificadas en esta etapa (referencia rápida)

- Huang et al. (2021), *Power of data in quantum machine learning*, *Nat. Commun.* 12, 2631, CC BY 4.0, PMC8113501. Usada en M6 y X6 (H-033, H-038, D-034).
- Cristianini, Shawe-Taylor, Elisseeff y Kandola (2001), *On kernel-target alignment*, NIPS 14 (D-033).
- Cortes, Mohri y Rostamizadeh (2012), *Algorithms for learning kernels based on centered alignment*, JMLR 13:795–828 (D-033).

## 6. Trabajos citados en §2 que reportan ventaja: revisar con las cuatro preguntas de H-046

Las cuatro preguntas:
1. ¿El modelo clásico recibió el mismo ajuste y las mismas features?
2. ¿La diferencia supera su incertidumbre?
3. ¿El test se usó una sola vez?
4. ¿El kernel cuántico es realmente difícil de calcular clásicamente?

Trabajos:
- [ ] Xiang et al. (2024), QCCNN sobre GBSG, SEER y WDBC (+5 % de *accuracy*).
- [ ] El trabajo sobre BreastMNIST con ResNet50 y una QNN (69 % frente a 67 %).
- [ ] El estudio de cáncer de pulmón con QSVM (ZZ 0.91; Pauli 0.96).
- [ ] Radhi et al. (2025), revisión de 28 estudios.
- [ ] Azevedo et al. (2022), *quantum transfer learning* sobre BCDR (84 %).
