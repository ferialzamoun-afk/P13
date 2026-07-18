# Tests et validations - Partie 1

## Objectif

Montrer comment les hypotheses ont ete verifiees par execution, relecture, controles qualite et validations successives du notebook ameliore.

> **Note de synchronisation documentaire** : cette page est une synthese courte. La reference complete et a jour est `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`.

## Tests menes

- Audit du notebook initial : structure, variables, chemins, redondances.
- Controles qualite data : doublons, cles, nulls, coherence des jointures, valeurs critiques.
- Tests de reproductibilite : chemins relatifs, execution de bout en bout, verification des sorties.
- Relecture des prompts IA et des integrations retenues ou ecartees.
- Verification finale pour publication GitHub et soutenance.

## Validation BC05 - Seuils de decision

- Test de separation des scores : `critical_score` (IF + SHAP + impact) vs `surveillance_score` (IF + kNN + K-Means + SHAP + impact).
- Verification que kNN/K-Means alimentent `A surveiller` sans declencher seuls `Critique`.
- Verification des compteurs apres regeneration stricte : 825 produits = 1 critique, 172 a surveiller, 652 normaux.
- Verification dashboard avec filtres courants : 713 lignes alignees = 1 critique, 152 a surveiller, 560 normaux.
- Verification de synchronisation des exports notebook vers `P6-Dashboard/data` : matrice decisionnelle, matrice critique/surveillance, alertes actionnables, summary, Isolation Forest.
- Verification de synchronisation dataviz BC05 vers `P6_ameliore_IA/output/dataviz`.

## Preuves detaillees

- `P6_ameliore_IA/docs/07_checklist_publication_github.md`
- `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`
- `P6_ameliore_IA/docs/04_plan_projet_P13_partie_1.md`
- `P6_ameliore_IA/docs/05_matrice_indicateurs_P13_partie_1.md`