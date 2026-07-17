# Limites - Partie 1

## Objectif

Documenter les points de vigilance qui bornent l'interpretation des resultats et evitent une surpromesse sur la qualite des analyses P6 ameliorees.

## Limites identifiees

- Jeu de donnees observe sur un perimetre temporel limite.
- Certaines jointures et corrections restent dependantes des sources metier disponibles.
- Les anomalies detectees demandent encore une validation metier avant action definitive.
- Les gains de structure et de temps ne remplacent pas une industrialisation complete.
- L'IA reste un support de travail, avec validation humaine obligatoire.

## Limites BC05 - Seuils de priorisation

- Les seuils (25%, 3 ventes, 400 EUR) sont des seuils de pilotage initial, a recalibrer selon saisonnalite.
- Un cas classe critique ne signifie pas automatiquement une erreur de saisie : validation metier obligatoire.
- Le score Isolation Forest depend du contexte donnees et peut evoluer avec de nouveaux lots.
- Les decisions automatiques du dashboard sont des recommandations, pas un arbitrage final.

## Preuves detaillees

- `P6_ameliore_IA/docs/06_synthese_finale_P13_partie_1.md`
- `P6_ameliore_IA/docs/03_journal_ia_P13_partie_1.md`
- `P6_ameliore_IA/docs/01_cahier_des_charges_P13_partie_1.md`