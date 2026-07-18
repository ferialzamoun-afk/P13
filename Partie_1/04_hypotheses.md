# Hypotheses de travail - Partie 1

## Objectif

Rendre explicites les hypotheses de refonte du notebook P6 avant d'ajouter controles, refactoring et documentation.

> **Note de synchronisation documentaire** : cette page est une synthese courte. La reference complete et a jour est `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`.

## Hypotheses retenues

- Le notebook initial peut etre ameliore sans etre reconstruit entierement.
- Les incoherences majeures viennent du rapprochement entre ERP, Web et table de liaison.
- Des controles de qualite explicites ameliorent la confiance dans les KPI finaux.
- Une documentation plus courte mais mieux structuree augmente la lisibilite pour la soutenance.
- L'IA peut accelerer le cadrage et la reformulation, mais pas remplacer la validation humaine.

## Hypotheses BC05 - Priorisation metier

- Un produit rare selon kNN ou eloigne de son cluster K-Means doit etre investigue, mais pas automatiquement classe critique.
- La criticite immediate doit rester fondee sur IF + SHAP + impact business pour eviter la surpriorisation statistique.
- Les alertes `A surveiller` constituent un backlog hebdomadaire d'investigation metier.
- Les alertes `Critique` doivent rester une short-list actionnable et defendable en CODIR.

## Preuves detaillees

- `P6_ameliore_IA/docs/03_journal_ia_P13_partie_1.md`
- `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`
- `P6_ameliore_IA/docs/04_plan_projet_P13_partie_1.md`
- `P6_ameliore_IA/docs/08_audit_notebook_P6_initial.md`