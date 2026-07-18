# Cahier des charges fonctionnel - Partie 1

## Objectif

Poser le cadre du projet d'amelioration P6 : besoin metier, livrables attendus, criteres de reussite, parties prenantes et contraintes de publication.

> **Note de synchronisation documentaire** : cette page est une synthese courte. La reference complete et a jour est `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`.

## Points cles

- Besoin : reconcilier les donnees ERP, Web et Liaison pour produire des KPI exploitables.
- Publics : mentor evaluateur, recruteur, CODIR, public non technique.
- Livrables attendus : notebook ameliore, documentation, journal IA, synthese finale, checklist de publication.
- Criteres de reussite : fiabilite des calculs, chemins reproductibles, preuves lisibles, limites explicites.
- Contraintes : sobriete technique, traçabilite IA, publication GitHub exploitable.

## Exigences fonctionnelles BC05 - Aide a la decision

- Transformer les alertes statistiques en priorites metier actionnables.
- Afficher pour chaque cas : priorite, motif, action recommandee, responsable et delai.
- Seuils de reference : `Critique` via `critical_score >= 0.65` (IF + SHAP + impact), `A surveiller` via `surveillance_score >= 0.45` (IF + kNN + K-Means + SHAP + impact).
- kNN/K-Means servent a ordonner les investigations et ne declenchent pas seuls une urgence critique.
- Maintenir une traçabilite exportable (plan d'actions CSV) pour pilotage equipe.

## Preuves detaillees

- `P6_ameliore_IA/docs/01_cahier_des_charges_P13_partie_1.md`
- `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`
- `P6_ameliore_IA/docs/04_plan_projet_P13_partie_1.md`