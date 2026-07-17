# Veille metier et technologique - Partie 1

## Objectif

Documenter les options techniques et les usages metier utiles pour transformer le livrable P6 en version plus fiable, reproductible et lisible pour un public projet ou recruteur.

## Points cles

- Comparaison de solutions de qualite data : Pandas, Great Expectations, Soda Core, Aikido.
- Criteres retenus : robustesse, temps d'implementation, reproductibilite, sobriete, documentation, securite.
- Choix court terme : Pandas pragmatique et controles explicites dans le notebook.
- Piste moyen terme : formaliser des Data Contracts et une migration vers Great Expectations v19+.
- Enjeu metier : fiabiliser les KPI Bottleneck et rendre les decisions plus auditables.

## Mise a jour BC05 - Seuils de priorisation metier

- Marge faible : seuil releve a < 25% pour mieux capter les cas de rentabilite fragile.
- Cas critique stock : rupture avec demande des 3 ventes et plus.
- Cas critique impact business : au moins 3 alertes statistiques et impact CA de 400 EUR et plus.
- Les cas Isolation Forest restent priorises en niveau eleve, avec audit metier recommande.

## Preuves detaillees

- `P6_ameliore_IA/docs/02_veille_technologique_P13_partie_1.md`
- `P6_ameliore_IA/docs/13_great_expectations_strategy.md`
- `P6_ameliore_IA/docs/05_matrice_indicateurs_P13_partie_1.md`