# Mini formation pour les metiers - Partie 1

## Objectif

Fournir un support court pour aider un public non technique a lire les KPI, comprendre les graphiques et interpreter les anomalies sans surinterpreter les resultats.

> **Note de synchronisation documentaire** : cette page est une synthese courte. La reference complete et a jour est `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`.

## Modules proposes

1. Lire les KPI Bottleneck : chiffre d'affaires, marges, ruptures, concentration Pareto.
2. Comprendre les graphiques : courbes, histogrammes, repartitions, corrélations.
3. Interpréter les anomalies : prix incoherents, marges negatives, stock manquant.
4. Connaitre les limites : donnees d'un seul mois, jointures incertaines, correlation non causale.
5. Utiliser la restitution : que surveiller, quand recontroler, quelles decisions prendre ou reporter.

## Accessibilite

- Vocabulaire simple et limite au strict necessaire.
- Resultats visibles dans des tableaux et graphiques commentes.
- Supports consultables en Markdown et notebook.

## Mise a jour BC05 - Lecture metier des seuils

- `Critique` : short-list stricte basee sur `critical_score` (IF + SHAP + impact business), action sous 24-48h.
- `A surveiller` : file d'investigation basee sur `surveillance_score`, incluant kNN/K-Means pour reperer rarete locale et distance au cluster.
- `Normal` : suivi standard, sans action immediate.
- Restitution attendue en dashboard : motif, action recommandee, score critique, score de surveillance et export CSV.

## Preuves detaillees

- `P6_ameliore_IA/docs/01_cahier_des_charges_P13_partie_1.md`
- `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`
- `P6_ameliore_IA/docs/05_matrice_indicateurs_P13_partie_1.md`
- `P6_ameliore_IA/docs/GUIDE_EXECUTION_NOTEBOOK.md`