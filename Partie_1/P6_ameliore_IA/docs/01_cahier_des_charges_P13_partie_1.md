# Cahier des charges - P13 Partie 1

## 1. Contexte

Le projet P13 Partie 1 consiste a piloter un projet data augmente par l'IA a partir du livrable du projet 6 Bottleneck : un notebook Python d'analyse du stock et des ventes.

Le contexte metier porte sur le rapprochement de plusieurs sources de donnees : donnees ERP, donnees web et table de liaison. Ces sources permettent d'analyser les ventes, les stocks, le chiffre d'affaires et les anomalies possibles, mais elles peuvent contenir des valeurs manquantes, des doublons, des incoherences de jointure ou des prix atypiques.

## 2. Besoin metier reformule

Bottleneck a besoin de fiabiliser son analyse des ventes et des stocks afin d'obtenir une vision exploitable de la performance commerciale, d'identifier les produits a forte valeur, de detecter les anomalies de prix ou de stock, et de produire une restitution claire pour aider la decision.

Le projet doit donc transformer le notebook existant en livrable plus robuste, documente et reproductible, en integrant des controles qualite data, des justifications techniques et une trace critique de l'utilisation de l'IA.

## 2.b Storytelling dashboard (fil directeur)

La restitution metier suit une chaine unique:

1. Detecter les cas a risque (qualite + anomalies multivariees).
2. Expliquer pourquoi ils sont signales (SHAP).
3. Prioriser les actions (risque immediate puis rarete locale).
4. Decider en CODIR (liste de produits a corriger et plan de suivi).

Arbitrage methodes pour la decision:

- Socle court terme: Pandera + Isolation Forest + SHAP.
- Renfort moyen terme: K-Means/kNN pour la priorisation avancee.

## 3. Objectifs

| Objectif | Resultat attendu | Indicateur de validation |
|---|---|---|
| Fiabiliser les donnees | Sources controlees avant analyse | Valeurs manquantes, doublons et cles de jointure controles |
| Produire les KPI metier | Chiffre d'affaires, stock, rotation, prix atypiques | KPI calcules et interpretes |
| Ameliorer le notebook | Notebook plus lisible, structure et reproductible | Sections claires, chemins relatifs, versions documentees |
| Tracer l'usage de l'IA | Prompts, variantes, resultats et decisions humaines | Journal IA complete avec au moins 2 essais |
| Preparer la restitution | Synthese recruteur/client et preuves portfolio | Documentation exploitable dans le portfolio |

## 4. Perimetre

### Inclus

- Audit du notebook P6 Bottleneck existant.
- Formalisation du besoin metier et des criteres de reussite.
- Ajout ou formalisation de controles qualite data.
- Veille courte sur des outils utiles au projet.
- Journalisation des essais IA et des arbitrages humains.
- Planning, backlog et registre des risques.

### Hors perimetre

- Reconstruction complete du projet P6 depuis zero.
- Mise en production d'un pipeline automatise complet.
- Creation d'un dashboard interactif avance si le temps disponible ne le permet pas.
- Analyse de donnees non presentes dans les fichiers du projet initial.

## 5. Contraintes

| Type | Contrainte | Impact |
|---|---|---|
| Delai | Mission ciblee sur 4 jours | Prioriser les livrables les plus demonstratifs |
| Budget | Budget nul ou limite | Privilegier outils gratuits, open source ou deja disponibles |
| Technique | Notebook existant volumineux | Eviter les refontes lourdes, travailler par ameliorations ciblees |
| Donnees | Qualite variable et rapprochements sensibles | Ajouter des controles avant les conclusions |
| Restitution | Livrables evaluables et reutilisables portfolio | Produire des preuves claires, sourcables et lisibles |

## 6. Parties prenantes

| Public | Besoin | Adaptation prevue |
|---|---|---|
| Client metier | Comprendre les ventes, stocks et anomalies | Synthese courte, KPI explicites, recommandations |
| Evaluateur | Verifier la demarche de pilotage data | Documents structures, indicateurs, preuves |
| Recruteur | Identifier les competences data analyst | README, captures, resultats, limites |
| Public non technique | Lire les resultats sans jargon excessif | Glossaire court, graphiques lisibles, interpretation simple |

## 7. Livrables attendus

| Livrable | Format | Critere d'acceptation | Statut final |
|---|---|---|---|
| Cahier des charges | Markdown puis PDF possible | Besoin, objectifs, perimetre, contraintes et livrables presents | [x] |
| Veille technologique | Markdown | Au moins 2 solutions comparees avec decision argumentee ; Great Expectations integre | [x] |
| Notebook P6 ameliore (bottleneck_analyse_ameliore_final) | Notebook (47 cellules) | Controles qualite formels, 7 Data Contracts, conclusions maintenus, 13 dataviz | [x] |
| Journal IA | Markdown | 26 prompts traces avec decisions humaines et limites | [x] |
| Plan projet | Markdown | Backlog, planning 4 jours, risques et kanban GitHub | [x] |
| Synthese finale | Markdown | Resultats KPI, impact avant/apres, limites, prochaines etapes 3 horizons | [x] |

## 8. Criteres de reussite

- Le besoin metier est reformule clairement et relie aux contraintes du projet.
- Les donnees critiques sont controlees avant interpretation.
- Les choix techniques sont justifies et proportionnes.
- Les essais IA sont utiles, traces et relus humainement.
- Les limites de l'analyse sont explicites.
- Les livrables peuvent etre repris dans le portfolio P13.

## 9. Suivi des taches (passe pre-commit/push)

Etat synchronise avec la documentation projet et le board GitHub Projects (controle du 2026-07-18):

| Tache | Description | Statut |
|---|---|---|
| T09 | Preparer les preuves pour le portfolio | [x] |
| T12 | Nettoyer le depot GitHub + setup security scanning | [~] |
| T18 | Synchroniser les taches dans GitHub Projects | [~] |

Reste a finaliser avant publication:

- Cloturer les cartes legacy encore en "A faire" dans le board GitHub.
- Finaliser le lot securite (secret AIKIDO_CLIENT_API_KEY et premier scan).
- Refaire une verification finale docs + liens publics juste avant commit/push.
