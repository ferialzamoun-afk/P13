# Veille metier et technologique - Partie 1

## Objectif

Documenter les options techniques et les usages metier utiles pour transformer le livrable P6 en version plus fiable, reproductible et lisible pour un public projet ou recruteur.

> **Note de synchronisation documentaire** : cette page est une synthese courte. La reference complete et a jour est `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`.

## Points cles

- Comparaison de solutions de qualite data : Pandas, Great Expectations, Soda Core, Aikido.
- Criteres retenus : robustesse, temps d'implementation, reproductibilite, sobriete, documentation, securite.
- Choix court terme : Pandas pragmatique et controles explicites dans le notebook.
- Piste moyen terme : formaliser des Data Contracts et une migration vers Great Expectations v19+.
- Enjeu metier : fiabiliser les KPI Bottleneck et rendre les decisions plus auditables.

## Mise a jour BC05 - Regle de priorisation metier retenue

- `Critique` repose sur un score strict : Isolation Forest + SHAP + impact business (`critical_score >= 0.65`).
- `A surveiller` repose sur un score large : IF + kNN + K-Means + SHAP + impact business (`surveillance_score >= 0.45`).
- kNN est non supervise : il mesure une rarete locale et sert a ordonner les investigations, pas a declencher seul une urgence metier.
- K-Means segmente les profils et repere les distances au centroide ; il complete la priorisation mais ne remplace pas la validation metier.

## Preuves detaillees

- `P6_ameliore_IA/docs/02_veille_technologique_P13_partie_1.md`
- `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`
- `P6_ameliore_IA/docs/13_great_expectations_strategy.md`
- `P6_ameliore_IA/docs/05_matrice_indicateurs_P13_partie_1.md`