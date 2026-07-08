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
| T09 | Preparer les preuves pour le portfolio | Moyenne | 1 h | T08 | [~] |
| T10 | Documenter les ameliorations du notebook | Moyenne | 1 h 30 | T05 | [x] |
| T11 | Renommer notebook et mettre a jour tous les fichiers de ref | Haute | 30 min | T10 | [x] |
| T12 | Nettoyer le depot GitHub avant publication | Haute | 2 h | T11 | [~] |

## Kanban de suivi

| A faire | En cours | Termine |
|---|---|---|
| T09 - Preparer les preuves pour le portfolio | T12 - Nettoyer le depot GitHub avant publication | T01 - Rediger le besoin metier reformule |
| T12 - Nettoyer le depot GitHub avant publication |  | T02 - Creer le cahier des charges initial |
|  |  | T03 - Construire le tableau de veille |
|  |  | T04 - Documenter 2 essais IA minimum |
|  |  | T05 - Auditer le notebook P6 existant |
|  |  | T06 - Ajouter ou formaliser les controles qualite data |
|  |  | T06b - Implementer Data Contracts (7 expectations GE formels) |
|  |  | T07 - Verifier les chemins et la reproductibilite |
|  |  | T08 - Produire une synthese finale recruteur/client |
|  |  | T10 - Documenter les ameliorations du notebook |
|  |  | T11 - Renommer notebook et mettre a jour tous les fichiers de ref |

### Variante compatible GitHub

Ce kanban est volontairement en Markdown pour etre lisible directement dans GitHub. Une extension VS Code peut aider au suivi local, mais le tableau Markdown reste la version exportable et partageable dans le depot.

Une vue GitHub Projects complete ce suivi pour la preuve visuelle portfolio : https://github.com/users/ferialzamoun-afk/projects/2/views/3?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Linked+pull+requests%22%2C%22Sub-issues+progress%22%2C366231487%2C366231820%5D

Capture locale associee : `P6_ameliore_IA/output/github_project_kanban_en_cours.png`.

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

## Planning 4 jours

| Jour | Objectif | Actions | Livrables | Status |
|---|---|---|---|---|
| J1 | Cadrer et lancer | Cahier des charges, veille, journal IA, plan projet | Docs de pilotage initiales | [x] |
| J2 | Auditer et ameliorer le notebook | Identifier controles manquants, clarifier le code, ajouter Data Contracts (7 expectations GE formels) | Notebook P6 ameliore (47 cellules) + M05b Data Contracts | [x] |
| J3 | Valider et documenter | Execution complete, verification resultats, KPI finaux, 13 dataviz, renommage bottleneck_analyse_ameliore_final.ipynb | Synthese enrichie avant/apres, preuves | [x] |
| J4 | Finaliser la restitution | Mettre a jour synthese et docs, preparer publication GitHub, portfolio | Dossier publiable, checklist publication | [~] |

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
| Fin J1 | Documents de cadrage crees | Fichiers docs et matrice mise a jour |
| Fin J2 | Notebook audite et controles ajoutes | Cellules controles qualite, resultats |
| Fin J3 | Resultats verifies | Notes de validation, execution notebook |
| Fin J4 | Restitution prete | README, captures, synthese finale |
