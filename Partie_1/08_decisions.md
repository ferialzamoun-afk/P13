# Decisions - Partie 1

## Objectif

Tracer les arbitrages principaux pris pendant l'amelioration du projet P6, en separant ce qui a ete retenu, ecarte ou reporte.

## Decisions prises

- Conserver l'existant et l'ameliorer progressivement plutot que refaire le notebook depuis zero.
- Utiliser Pandas et des controles explicites pour le court terme.
- Reporter l'industrialisation lourde vers une trajectoire Great Expectations / Data Contracts.
- Formaliser la traçabilite IA dans un journal dedie.
- Prioriser lisibilite, preuves et publication publique avant extension technique supplementaire.

## Decisions BC05 - Seuils retenus a ce stade

- Relever le seuil de marge faible a < 25% pour mieux couvrir le risque business.
- Definir une criticite rupture sur stock nul avec demande >= 3 ventes.
- Definir une criticite impact via la combinaison 3 alertes statistiques + CA >= 400 EUR.
- Conserver Isolation Forest en priorite elevee avec audit metier systematique.
- Exiger une restitution decisionnelle explicite en dashboard : motif, action, responsable, delai.

## Preuves detaillees

- `P6_ameliore_IA/docs/03_journal_ia_P13_partie_1.md`
- `P6_ameliore_IA/docs/02_veille_technologique_P13_partie_1.md`
- `P6_ameliore_IA/docs/06_synthese_finale_P13_partie_1.md`