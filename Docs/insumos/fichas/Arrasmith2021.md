# Arrasmith2021 · Effect of barren plateaus on gradient-free optimization

- Autores y año: Arrasmith et al. (2021)
- DOI comprobado en la página 1: Sí (10.22331/q-2021-10-05-558)
- Versión leída: Docs/fuentes/pdf/Arrasmith2021.pdf · publicada · 12 páginas
- Tipo: propuesta teórica / análisis numérico

## Respuestas a las preguntas
1. Conclusión central sobre barren plateaus y optimización sin gradientes — Demuestran analítica y numéricamente que los optimizadores sin gradientes no resuelven el problema de los barren plateaus: las diferencias en la función de coste que guían las decisiones se suprimen exponencialmente con el número de qubits, requiriendo precisión y recursos exponencialmente grandes para avanzar — «Here we show that, indeed, gradient-free optimizers do not solve the barren plateau problem.» (p. 1), «Our main result proves that cost function differences, which are the basis for making decisions in a gradient-free optimization, are exponentially suppressed in a barren plateau.» (p. 1), «Hence, without exponential precision, gradient-free optimizers will not make progress in the optimization.» (p. 1) y «This is consistent with our main result, and demonstrates that barren plateaus can lead to exponential scaling even for gradient-free optimizers.» (p. 8)

## Qué concluye la obra
- Ponen en duda que la elección del optimizador pueda constituir una estrategia efectiva para evitar los barren plateaus: «Our work casts doubt on the notion that the choice of optimizer could provide a strategy to avoid barren plateaus.» (p. 8)
- Concluyen que los optimizadores basados en búsqueda local o muestreo aleatorio requieren recursos exponencialmente crecientes para tomar decisiones sobre la dirección de avance en el paisaje de pérdidas: «This implies that such optimizers will need to expend exponentially large resources in order to make decisions about where to move in the landscape.» (p. 8)

## Qué deja como trabajo futuro o limitación declarada
- Señalan la necesidad de continuar desarrollando estrategias específicas para evitar los barren plateaus y plantean como trabajo futuro un tratamiento teórico unificado que abarque tanto optimizadores con gradiente como libres de gradiente: «Future work certainly should continue to develop strategies to avoid them. Additionally, in future work, we hope to develop a uniﬁed treatment that covers the impact of barren plateaus on various types of optimizers, gradient-based and gradient-free.» (p. 8)
