# Hypotheses de travail - Partie 1

## Objectif

Rendre explicites les hypotheses de refonte du notebook P6 avant d'ajouter controles, refactoring et documentation.

## Hypotheses retenues

- Le notebook initial peut etre ameliore sans etre reconstruit entierement.
- Les incoherences majeures viennent du rapprochement entre ERP, Web et table de liaison.
- Des controles de qualite explicites ameliorent la confiance dans les KPI finaux.
- Une documentation plus courte mais mieux structuree augmente la lisibilite pour la soutenance.
- L'IA peut accelerer le cadrage et la reformulation, mais pas remplacer la validation humaine.

## Hypotheses BC05 - Priorisation metier

- Un seuil marge < 25% capte mieux les cas economiquement risqués qu'un seuil plus strict.
- Une rupture avec au moins 3 ventes est un signal de perte business a traiter en priorite.
- La combinaison multi-alertes + impact CA (>= 400 EUR) constitue un niveau de criticite defendable.
- Les alertes Isolation Forest doivent declencher un audit fiche produit meme sans erreur evidente.

## Preuves detaillees

- `P6_ameliore_IA/docs/03_journal_ia_P13_partie_1.md`
- `P6_ameliore_IA/docs/04_plan_projet_P13_partie_1.md`
- `P6_ameliore_IA/docs/08_audit_notebook_P6_initial.md`