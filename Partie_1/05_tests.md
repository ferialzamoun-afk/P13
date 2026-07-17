# Tests et validations - Partie 1

## Objectif

Montrer comment les hypotheses ont ete verifiees par execution, relecture, controles qualite et validations successives du notebook ameliore.

## Tests menes

- Audit du notebook initial : structure, variables, chemins, redondances.
- Controles qualite data : doublons, cles, nulls, coherence des jointures, valeurs critiques.
- Tests de reproductibilite : chemins relatifs, execution de bout en bout, verification des sorties.
- Relecture des prompts IA et des integrations retenues ou ecartees.
- Verification finale pour publication GitHub et soutenance.

## Validation BC05 - Seuils de decision

- Test du seuil marge faible (< 25%) sur les alertes actionnables.
- Test de criticite rupture avec demande (stock nul et 3 ventes ou plus).
- Test de criticite combinee (3 alertes et impact CA de 400 EUR et plus).
- Verification de la table decisionnelle en dashboard : priorite, motif, action, responsable, delai.

## Preuves detaillees

- `P6_ameliore_IA/docs/07_checklist_publication_github.md`
- `P6_ameliore_IA/docs/04_plan_projet_P13_partie_1.md`
- `P6_ameliore_IA/docs/05_matrice_indicateurs_P13_partie_1.md`