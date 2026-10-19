# A2 · Consistencia numérica entre secciones

Lee primero `Docs/insumos/auditoria/reglas.md`.

Objetivo: que cada cifra que se repite en el reporte diga lo mismo en todas partes y coincida con su fuente.

1. Corre `/opt/anaconda3/envs/qml_cancer/bin/python Code/tools/verificar_cifras_capitulos.py Docs/capitulos/<carpeta>` para 5_Metodologia, 6_Resultados, 7_Conclusiones, 8_Trabajo_Futuro y 0_Preliminares. Copia la salida resumida. Revisa a mano cada cifra marcada como no encontrada.
2. Construye una tabla de las cifras «titulares» y busca cada una en TODO el reporte (`grep -rn`). Como mínimo:
   - conteos del dataset: 3,568 registros, 1,566 pacientes, 2,864/704, 1,318/378, 1,546/326, 912/784, 1,199/673, 80 máscaras desalineadas (78 + 2);
   - 67 features, k = 12, k = 8, 200 lesiones por subconjunto, semillas 42, 125 y 168;
   - AUC del test por condición (masas y calcificaciones), diferencias C4/C5 − C1;
   - KTA (exceso sobre la permutación), *g* (1.40–1.70; 306–388 sin regularizar), dimensión efectiva (168–188), mediana del kernel (0.003, 0.61, 0.00003), Spearman (0.67–0.97, p = 4/120);
   - OE-6: k ≈ 25 y ≈ 22 en 24 h, parameter-shift a partir de 15, 1,024 disparos, 16–74 % de lecturas nulas, 205 h.
   Para cada una: todas las apariciones con archivo:línea, si son iguales entre sí y si coinciden con la bitácora y con el CSV que la respalda (`Code/results/*.csv`).
3. Atención especial al **resumen y abstract** (`Docs/capitulos/0_Preliminares/`), a §1 (objetivos y alcance) y a §7 (conclusiones): son los que más se leen y los últimos que se escribieron.
4. Detecta cifras que se contradicen aunque no sean idénticas: por ejemplo «de 0.07 a 0.14» en un lugar y «0.08 a 0.13» en otro; o una cifra de TT1 que quedó sin actualizar (97.6 % de cobertura, 224×224, «100–300 features», TorchConnector, MinMaxScaler, `['X','ZZ']`, `PauliFeatureMap` como clase).

Entrega: `informe_A2.md` con la tabla de cifras (cifra · apariciones · fuente · estado) y los hallazgos.
