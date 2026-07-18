# Decisions - Partie 1

## Objectif

Tracer les arbitrages principaux pris pendant l'amelioration du projet P6, en separant ce qui a ete retenu, ecarte ou reporte.

> **Note de synchronisation documentaire** : cette page est une synthese courte. La reference complete et a jour est `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`.

## Decisions prises

- Conserver l'existant et l'ameliorer progressivement plutot que refaire le notebook depuis zero.
- Utiliser Pandas et des controles explicites pour le court terme.
- Reporter l'industrialisation lourde vers une trajectoire Great Expectations / Data Contracts.
- Formaliser la traçabilite IA dans un journal dedie.
- Prioriser lisibilite, preuves et publication publique avant extension technique supplementaire.

## Decisions BC05 - Regle retenue

- Separer `critical_score` et `surveillance_score` pour eviter que la rarete statistique declenche seule une urgence metier.
- Definir `Critique` avec IF + SHAP + impact business (`critical_score >= 0.65`).
- Definir `A surveiller` avec IF + kNN + K-Means + SHAP + impact business (`surveillance_score >= 0.45`).
- Conserver kNN/K-Means comme signaux de second niveau pour ordonner les investigations.
- Exiger une restitution decisionnelle explicite en dashboard : motif, scores, action, responsable, export CSV.

## Preuves detaillees

- `P6_ameliore_IA/docs/03_journal_ia_P13_partie_1.md`
- `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`
- `P6_ameliore_IA/docs/02_veille_technologique_P13_partie_1.md`
- `P6_ameliore_IA/docs/06_synthese_finale_P13_partie_1.md`