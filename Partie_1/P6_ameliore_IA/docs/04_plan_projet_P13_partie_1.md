# Plan projet - P13 Partie 1

## Lots de travail

| Lot | Contenu | Livrable | Definition de Done |
|---|---|---|---|
| 1. Cadrage | Besoin metier, objectifs, contraintes | Cahier des charges | Besoin reformule et criteres de reussite presents |
| 2. Veille | Comparaison outils et sources | Veille technologique | Au moins 2 solutions comparees et choix justifie |
| 3. Audit notebook | Lecture structure, donnees, sorties | Notes d'audit | Points forts, limites et risques identifies |
| 4. Amelioration du notebook | Clarification du notebook, chemins, fonctions, cellules redondantes | Journal d'amelioration | Changements avant/apres justifies et limites documentees |
| 5. Amelioration data | Controles qualite, jointures, KPI | Notebook ameliore | Controles visibles et resultats coherents |
| 6. IA critique | Prompts, variantes, decisions | Journal IA | Au moins 2 essais documentes |
| 7. Validation | Execution, relecture, coherence | Synthese de validation | Livrables relus, chemins et resultats verifies |
| 8. Publication GitHub | Nettoyage du depot, README public, preuves finales | Checklist publication GitHub | Depot presentable ou decision de garder prive justifiee |
| 9. Restitution | Synthese client/recruteur, portfolio | README/synthese | Resultats et recommandations reutilisables |

## Fil conducteur operationnel (dashboard)

1. Qualite des donnees (Pandera et controles amont).
2. Detection des risques business (Isolation Forest).
3. Explication des alertes (SHAP).
4. Priorisation de second niveau (K-Means/kNN).
5. Decision CODIR (top produits, exports actionnables).

## Backlog priorise

| ID | Tache | Priorite | Estimation | Dependances | Statut |
|---|---|---|---|---|---|
| T01 | Rediger le besoin metier reformule | Haute | 1 h | Aucune | [x] |
| T02 | Creer le cahier des charges initial | Haute | 1 h 30 | T01 | [x] |
| T03 | Construire le tableau de veille | Haute | 1 h | Aucune | [x] |
| T04 | Documenter 2 essais IA minimum | Haute | 45 min | T01, T02 | [x] |
| T05 | Auditer le notebook P6 existant | Haute | 2 h | T02 | [x] |
| T06 | Ajouter ou formaliser les controles qualite data | Haute | 2 h | T05 | [x] |
| T06b | Implementer Data Contracts (7 expectations GE formels) | Haute | 1 h | T06 | [x] |
| T07 | Verifier les chemins et la reproductibilite | Moyenne | 1 h | T05, T06 | [x] |
| T08 | Produire une synthese finale recruteur/client | Moyenne | 1 h | T06 | [x] |
| T09 | Preparer les preuves pour le portfolio | Moyenne | 1 h | T08 | [x] |
| T10 | Documenter les ameliorations du notebook | Moyenne | 1 h 30 | T05 | [x] |
| T11 | Renommer notebook et mettre a jour tous les fichiers de ref | Haute | 30 min | T10 | [x] |
| T12 | Nettoyer le depot GitHub avant publication + setup Aikido/security scanning | Haute | 2 h | T11 | [~] |
| T13 | Mettre a jour la veille avec IF/SHAP/K-Means/kNN | Haute | 45 min | T03, T06 | [x] |
| T14 | Centrer le journal IA sur le comptage de prompts BC05 | Haute | 30 min | T04 | [x] |
| T15 | Formaliser la priorisation dashboard (IF+SHAP socle, K-Means/kNN complement) | Haute | 45 min | T13, T14 | [x] |
| T16 | Mettre a jour la matrice d'indicateurs selon objectif anomalies dashboard | Haute | 45 min | T15 | [x] |
| T17 | Aligner la documentation plan/projet avec jalons sans duree fixe | Moyenne | 30 min | T16 | [x] |
| T18 | Synchroniser les taches dans GitHub Projects | Moyenne | 20 min | T13-T17 | [~] |

## Kanban de suivi

| A faire | En cours | Termine |
|---|---|---|
|  | T12 - Nettoyer le depot GitHub avant publication + setup Aikido/security scanning | T01 - Rediger le besoin metier reformule |
|  | T18 - Synchroniser les taches dans GitHub Projects | T02 - Creer le cahier des charges initial |
|  |  | T03 - Construire le tableau de veille |
|  |  | T04 - Documenter 2 essais IA minimum |
|  |  | T05 - Auditer le notebook P6 existant |
|  |  | T06 - Ajouter ou formaliser les controles qualite data |
|  |  | T06b - Implementer Data Contracts (7 expectations GE formels) |
|  |  | T07 - Verifier les chemins et la reproductibilite |
|  |  | T08 - Produire une synthese finale recruteur/client |
|  |  | T09 - Preparer les preuves pour le portfolio |
|  |  | T10 - Documenter les ameliorations du notebook |
|  |  | T11 - Renommer notebook et mettre a jour tous les fichiers de ref |
|  |  | T13 - Mettre a jour la veille avec IF/SHAP/K-Means/kNN |
|  |  | T14 - Centrer le journal IA sur le comptage de prompts BC05 |
|  |  | T15 - Formaliser la priorisation dashboard |
|  |  | T16 - Mettre a jour la matrice d'indicateurs |
|  |  | T17 - Aligner le plan avec jalons sans duree fixe |

### Variante compatible GitHub

Ce kanban est volontairement en Markdown pour etre lisible directement dans GitHub. Une extension VS Code peut aider au suivi local, mais le tableau Markdown reste la version exportable et partageable dans le depot.

Une vue GitHub Projects complete ce suivi pour la preuve visuelle portfolio : https://github.com/users/ferialzamoun-afk/projects/2/views/3?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Linked+pull+requests%22%2C%22Sub-issues+progress%22%2C366231487%2C366231820%5D

Capture locale associee : `P6_ameliore_IA/output/github_project_kanban_en_cours.png`.

### Lien direct GitHub Project et taches ajoutees

- Lien board principal: https://github.com/users/ferialzamoun-afk/projects/2/views/1
- Lien vue suivi portfolio: https://github.com/users/ferialzamoun-afk/projects/2/views/3

Point de synchro board (controle pre-commit, 2026-07-18):

- T09 visible en "Termine" dans le board.
- T12 visible en "A faire/En cours" selon la carte legacy et le lot en cours.
- T18 toujours en cours de synchronisation (mise a jour fine des statuts necessite une session GitHub authentifiee).

Taches ajoutees dans ce cycle:

- T13 - Mise a jour veille IF/SHAP/K-Means/kNN
- T14 - Focus comptage prompts BC05 dans le journal IA
- T15 - Arbitrage methodes dashboard formalise
- T16 - Matrice d'indicateurs alignee objectif anomalies
- T17 - Planning converti en jalons sans duree fixe
- T18 - Synchronisation GitHub Projects (en cours)

## Documentation a conserver

| Document | Emplacement conseille | Pourquoi le conserver |
|---|---|---|
| Donnees sources P6 | `P6_initial/data/` | Preuve du perimetre initial et reproductibilite |
| Notebook P6 initial | `P6_initial/notebook P6/` | Base de comparaison avant amelioration IA |
| Presentation de validation P6 | `P6_initial/Extraits_P6/` | Preuve que le projet initial a ete valide |
| Documents de cadrage P13 | `P6_ameliore_IA/docs/` | Preuve de pilotage, veille, IA critique et organisation |
| Metriques et exports produits | `P6_ameliore_IA/data/` ou `P6_ameliore_IA/output/` | Preuve des resultats et indicateurs calcules |
| Documentation utilisateur finale | `P6_ameliore_IA/docs/` ou `P6_ameliore_IA/README.md` | Aide a l'execution, a la lecture des KPI et a la reutilisation portfolio |
| Checklist publication GitHub | `P6_ameliore_IA/docs/07_checklist_publication_github.md` | Preuve que le depot prive sera rendu publiable de maniere controlee |
| Checklist amelioration notebook | `P6_ameliore_IA/docs/09_checklist_refactoring_notebook.md` | Fil conducteur pour corriger et enrichir le notebook ameliore pas a pas |
| Idees pipelines data/ML | `P6_ameliore_IA/docs/10_idees_pipelines_ml_p13.md` | Piste optionnelle pour anticiper les derives projet a partir des metriques P13 |
| Audit du notebook P6 initial | `P6_ameliore_IA/docs/08_audit_notebook_P6_initial.md` | Preuve du diagnostic avant amelioration |

La documentation utilisateur doit etre ajoutee si elle aide a comprendre ou reutiliser le projet : notice d'execution, interpretation des KPI, limites, recommandations et captures finales. Les brouillons, exports intermediaires non commentes et documents redondants peuvent rester hors du dossier final ou etre places en annexe.

Mode d'emploi utilisateur du dashboard (lecture metier et usage operationnel): `P6-Dashboard/docs/GUIDE_UTILISATEUR_DASHBOARD.md`.

## Planning par jalons (sans duree fixe)

| Jalon | Objectif | Actions | Livrables | Status |
|---|---|---|---|---|
| J1 | Cadrer et lancer | Cahier des charges, veille, journal IA, plan projet | Docs de pilotage initiales | [x] |
| J2 | Fiabiliser et detecter | Controles qualite, Data Contracts, Isolation Forest | Notebook ameliore + alertes anomalies | [x] |
| J3 | Expliquer et prioriser | SHAP, segmentation K-Means/kNN, exports dashboard | Dataviz et listes actionnables | [x] |
| J4 | Restituer et publier | Mise a jour docs, synchronisation GitHub Project, preuves portfolio | Dossier publiable, checklist publication | [~] |

## Registre des risques

| Risque | Probabilite | Impact | Criticite | Mitigation | Statut |
|---|---|---|---|---|---|
| Donnees incompletes ou incoherentes | Moyenne | Fort | Elevee | Controler valeurs manquantes, doublons et cles de jointure | Ouvert |
| Jointures incorrectes entre ERP et web | Moyenne | Fort | Elevee | Verifier cardinalites et lignes non rapprochees | Ouvert |
| Surinterpretation des anomalies de prix | Moyenne | Moyen | Moyenne | Documenter les seuils et limites d'interpretation | Ouvert |
| Notebook difficile a executer | Moyenne | Moyen | Moyenne | Standardiser chemins, dependances et ordre des cellules | Ouvert |
| Temps insuffisant | Moyenne | Moyen | Moyenne | Prioriser controles data et documentation principale | Ouvert |
| Donnees sensibles publiees par erreur | Faible | Fort | Moyenne | Relire le depot avant publication, scan Aikido si possible | Ouvert |
| Depot GitHub trop charge pour le portfolio | Elevee | Moyen | Elevee | Nettoyer l'arborescence, exclure les brouillons, documenter la version publique | Ouvert |
| Usage IA non trace | Faible | Moyen | Moyenne | Tenir le journal IA a jour apres chaque usage | En cours |

## Points de controle

| Moment | Controle | Preuve |
|---|---|---|
| Jalon 1 | Documents de cadrage crees | Fichiers docs et matrice mise a jour |
| Jalon 2 | Detection anomalies operationnelle | Isolation Forest + controles qualite executes |
| Jalon 3 | Explicabilite et priorisation valides | SHAP + K-Means/kNN + exports |
| Jalon 4 | Restitution prete | README, captures, synthese finale, GitHub Project |
