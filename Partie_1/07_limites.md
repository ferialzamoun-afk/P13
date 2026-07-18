# Limites - Partie 1

## Objectif

Documenter les points de vigilance qui bornent l'interpretation des resultats et evitent une surpromesse sur la qualite des analyses P6 ameliorees.

> **Note de synchronisation documentaire** : cette page est une synthese courte. La reference complete et a jour est `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`.

## Limites identifiees

- Jeu de donnees observe sur un perimetre temporel limite.
- Certaines jointures et corrections restent dependantes des sources metier disponibles.
- Les anomalies detectees demandent encore une validation metier avant action definitive.
- Les gains de structure et de temps ne remplacent pas une industrialisation complete.
- L'IA reste un support de travail, avec validation humaine obligatoire.

## Limites BC05 - Seuils de priorisation

- Les seuils `critical_score >= 0.65` et `surveillance_score >= 0.45` restent des seuils de pilotage, a recalibrer selon saisonnalite.
- Un cas classe critique ne signifie pas automatiquement une erreur de saisie : validation metier obligatoire.
- Le score Isolation Forest depend du contexte donnees et peut evoluer avec de nouveaux lots.
- kNN/K-Means ne sont pas supervises par une cible metier : ils signalent une rarete ou une distance statistique, pas une faute certaine.
- Les decisions automatiques du dashboard sont des recommandations, pas un arbitrage final.

## Preuves detaillees

- `P6_ameliore_IA/docs/06_synthese_finale_P13_partie_1.md`
- `P6_ameliore_IA/docs/00_dossier_projet_unique_P13_partie_1.md`
- `P6_ameliore_IA/docs/03_journal_ia_P13_partie_1.md`
- `P6_ameliore_IA/docs/01_cahier_des_charges_P13_partie_1.md`