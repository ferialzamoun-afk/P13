# Checklist d'amelioration notebook - P6 ameliore IA

## Objectif

Derouler l'amelioration du notebook P6 de maniere progressive, critique et documentee. Chaque etape doit produire une preuve ou une validation avant de passer a la suivante.

Notebook de travail final : `P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb`.

Etat actuel : notebook ameliore final en cours d'enrichissement documentaire et metier.

## Regle de travail

- Ne pas modifier le notebook initial conserve dans `P6_initial/`.
- Modifier uniquement la version de travail dans `P6_ameliore_IA/notebooks/`.
- Apres chaque changement important, verifier que le notebook reste lisible et executable.
- Documenter les decisions retenues, les limites et les preuves produites.

## Workflow obligatoire pour chaque etape R

Chaque etape `Rxx` doit suivre le meme cycle de travail afin de garder une trace claire de l'amelioration du notebook.

| Ordre | Action | Preuve attendue |
|---|---|---|
| 1 | Lire ou localiser la cellule/section concernee | Cellule, section ou fichier identifie |
| 2 | Formuler l'objectif de correction | Objectif court relie a la checklist |
| 3 | Appliquer une correction limitee | Modification ciblee dans le notebook ou les docs |
| 4 | Valider immediatement | Test local, execution de cellule, controle JSON ou controle documentaire |
| 5 | Formuler la decision humaine | Decision explicite : retenu, adapte, rejete ou reporte, avec justification |
| 6 | Documenter dans le journal IA | Prompt, resultat, decision humaine, limite |
| 7 | Mettre a jour le comptage des prompts | Total actualise dans le journal IA et la synthese finale |
| 8 | Cocher ou mettre a jour le statut de l'etape R | Statut `[x]`, `[~]` ou justification du blocage |
| 9 | Noter la prochaine action | Etape suivante ou point a verifier |

### Format de trace a utiliser dans le journal IA

Pour chaque etape terminee, ajouter une ligne dans le tableau des essais documentes et une ligne dans le comptage des prompts.

La decision humaine doit etre explicite et ne doit pas se limiter a "OK". Elle doit indiquer ce qui est retenu, adapte, rejete ou reporte, et pourquoi.

| Champ | Contenu attendu |
|---|---|
| Objectif | Nom de l'etape R et correction visee |
| Prompt utilise | Demande formulee a l'IA ou action accompagnee par l'IA |
| Resultat obtenu | Correction, analyse ou proposition produite |
| Decision humaine | Retenu, adapte, reporte ou rejete |
| Limites | Ce qui reste a verifier ou ce que l'IA ne prouve pas |

### Regle de validation

Une etape `Rxx` ne doit etre cochee `[x]` que si au moins une validation concrete existe : execution de cellule, test local, controle du fichier, capture, ou verification documentaire. Sinon, elle reste `[~]`.

## Checklist pas a pas

| ID | Etape | Objectif | Preuve attendue | Statut |
|---|---|---|---|---|
| R01 | Figer l'etat de depart | Confirmer que le notebook ameliore est une copie initialisee | Audit + metriques avant/apres | [x] |
| R02 | Verifier les chemins de donnees | Garantir l'acces a `P6_initial/data/` ou a une copie documentee | Cellule de configuration validee : `erp.xlsx`, `web.xlsx`, `liaison.xlsx` charges | [x] |
| R03 | Identifier l'erreur stockee | Comprendre la cellule avec stderr ou erreur | Note d'erreur ou capture | [ ] |
| R04 | Corriger ou documenter l'erreur | Eviter une execution finale ambigue | Cellule corrigee ou limite justifiee | [ ] |
| R05 | Ajouter une section Mission | Introduire la mission avant le contexte pour coller a la presentation orale | Capture mission + consigne courte | [ ] |
| R06 | Corriger le wording et l'objectif metier | Reformuler le notebook pour un public metier et evaluateur | Titre et objectif metier corriges ; section Mission, sommaire et phases I/II a integrer | [~] |
| R07 | Inserer une table des matieres orientee competences | Relier le notebook aux competences : collecter, stocker, agreger, analyser, restituer | Sommaire compact integre avec EDA, analyses univariees, bivariees, KPI et storytelling | [x] |
| R08 | Ventiler les phases I et II | Aligner le notebook avec la presentation orale | Phases I/II visibles dans le sommaire et les grands separateurs | [x] |
| R09 | Structurer les sections du notebook | Separer chargement, controles, nettoyage, analyse, restitution | Sommaire simplifie et grands titres harmonises sans toucher aux analyses detaillees | [x] |
| R09b | Cadrer la refonte complete a partir des cellules de code | Repartir du code pour proposer une trame vraiment lisible | Plan de refonte `11_plan_refonte_notebook_code.md` | [x] |
| M01 | Sauvegarder le notebook ameliore actuel | Eviter toute perte avant refonte structurelle | Backup horodate cree dans `P6_ameliore_IA/backups/` | [x] |
| M02 | Creer une version amelioree separee | Disposer d'une cible propre avant migration du code | `bottleneck_analyse_ameliore_final.ipynb` cree et JSON valide | [x] |
| M03 | Migrer le chargement et la configuration | Charger les sources dans la version amelioree | Cellule executee avec affichage RGPD-friendly : `P6_initial/data`, ERP (825, 6), Web (1513, 29), Liaison (825, 2) | [x] |
| R10 | Centraliser les controles qualite | Rendre le bloc `quality_report` clair et exploitable | `quality_report` execute ; `src/quality_checks.py` cree ; `metriques_p6_indicateurs.csv` alimente avec 12 lignes M04 | [x] |
| M05 | Migrer le nettoyage stock ERP | Corriger les incoherences critiques avant rapprochement | 2 `stock_status` corriges, 2 stocks negatifs ramenes a 0, 0 ecart restant | [x] |
| IA-04 | Documenter le script Python de correction stock | Valoriser l'amelioration IA apres enrichissement du notebook | Script appele dans le notebook ameliore, 7 lignes M05 ajoutees au CSV, documentation IA mise a jour | [x] |
| R11 | Verifier les jointures ERP/Web/Liaison | Documenter les lignes rapprochees et non rapprochees | `df_final` cree : 825 lignes, 714 avec correspondance web, 111 sans correspondance web active | [x] |
| M07 | Migrer EDA et analyses metier | Ajouter les features metier et produire une EDA compacte | 10 lignes M07 ajoutees au CSV ; CA total 143680.1 EUR ; 7 marges negatives | [x] |
| R12 | Rationaliser les exports | Orienter les fichiers produits vers `output/` | Chemins d'export documentes | [ ] |
| R13 | Selectionner les graphiques portfolio | Garder les visualisations utiles et lisibles | Liste des captures finales | [ ] |
| R14 | Nettoyer les sorties inutiles | Alleger le notebook avant publication | Notebook plus leger ou captures separees | [ ] |
| R15 | Executer le notebook dans l'ordre | Valider la reproductibilite | Execution sans erreur bloquante | [ ] |
| R16 | Mettre a jour la synthese finale | Reporter uniquement KPI, limites, recommandations et preuves utiles | `06_synthese_finale_P13_partie_1.md` complete sans redondance | [ ] |

## Wording et table des matieres cible

L'objectif est d'ameliorer la lisibilite sans transformer le notebook en dossier de soutenance complet. Le notebook doit rester centre sur l'analyse data ; les details de pilotage, IA, GitHub et portfolio restent dans les documents Markdown.

### Section Mission a placer avant le contexte

La premiere section du notebook peut commencer par la mission, avant le contexte, pour reprendre la logique de la soutenance orale.

Capture cible : `P6_ameliore_IA/output/captures/mission_p6_bottleneck.png`.

Contenu recommande :

| Element | Contenu dans le notebook | Niveau de detail |
|---|---|---|
| Titre | Mission - Analyse des ventes et des stocks Bottleneck | Court |
| Capture mission | Capture de l'enonce ou de la slide mission | Visuel unique |
| Consigne reformulee | Ce qui est attendu : fiabiliser les donnees, analyser les ventes/stocks, restituer les anomalies | Court |
| Livrable attendu | Notebook d'analyse + synthese metier | Court |
| Public cible | Direction, equipes commerciales, equipes logistiques, evaluateur | Court |

Regle : une seule capture mission suffit. Le detail de la mission reste dans le cahier des charges et la synthese finale.

### Objectif metier reformule

Proposition a integrer en debut de notebook :

> Fiabiliser l'analyse des ventes et des stocks de Bottleneck en rapprochant les donnees ERP, Web et Liaison, afin d'identifier les incoherences de donnees, les indicateurs commerciaux prioritaires, les produits a forte valeur et les anomalies necessitant une validation metier.

### Table des matieres compacte proposee

| Section notebook | Competence associee | Contenu attendu | Niveau de detail |
|---|---|---|---|
| 0. Mission | Cadrer la demande | Capture mission, consigne reformulee, livrable attendu | Tres court |
| 1. Contexte et objectif metier | Comprendre le besoin | Probleme, utilisateurs metiers, decisions a eclairer | Court |
| 2. Phase I - Preparation des donnees | Collecter, stocker, nettoyer | Librairies, chemins, sources ERP/Web/Liaison, controles qualite | Detail utile |
| 3. Phase I - Agregation et rapprochement | Agreger | Jointures, lignes rapprochees/non rapprochees, dataset final | Detail utile |
| 4. Phase II - Analyse des indicateurs | Analyser | CA, ventes, stocks, prix, anomalies | Detail utile |
| 5. Phase II - Dataviz et storytelling metier | Restituer, dataviz | Graphiques selectionnes, interpretation pour utilisateurs metiers | Selection courte |
| 6. Limites et recommandations | Communiquer | Limites, prudence, prochaines actions | Court |

### Ventilation orale Phase I / Phase II

Cette ventilation sert a faire correspondre le notebook avec la presentation orale sans ajouter trop de texte.

| Phase orale | Etapes notebook | Message a faire passer | Preuve attendue |
|---|---|---|---|
| Phase I - Preparation des donnees | Collecte, chargement, controle qualite, nettoyage, rapprochement ERP/Web/Liaison | Les donnees sont fiabilisees avant l'analyse | Dimensions, valeurs manquantes, doublons, jointures |
| Phase II - Analyse des donnees | KPI, anomalies, dataviz, storytelling, recommandations | Les indicateurs sont interpretes pour des utilisateurs metiers | CA, stocks, prix atypiques, graphiques, recommandations |

### Exemple de wording court pour les phases

**Phase I - Preparation des donnees**  
Cette phase vise a collecter, controler et rapprocher les donnees ERP, Web et Liaison afin de construire une base fiable pour l'analyse.

**Phase II - Analyse des donnees**  
Cette phase transforme la base fiabilisee en indicateurs metiers, visualisations et recommandations exploitables par les equipes commerciales et logistiques.

### Regles pour ne pas surcharger

| Element | Dans le notebook | Dans la synthese globale |
|---|---|---|
| Objectif metier | Oui, version courte | Oui, version executive |
| Capture mission | Oui, une seule capture au debut | Oui, optionnel si utile pour la soutenance |
| Table des matieres | Oui, compacte | Non necessaire |
| Details IA et prompts | Non, renvoi vers journal IA | Synthese courte + limites IA |
| Kanban et GitHub Projects | Non, renvoi docs | Capture et lien seulement |
| Refactoring detaille | Quelques commentaires utiles | Section avant/apres et preuves |
| Graphiques | Selection des plus utiles | Captures et interpretation courte |
| Recommandations | Liste courte | Version client/recruteur complete |

## Metriques a suivre avant/apres

| Metrique | Pourquoi elle compte | Etat cible |
|---|---|---|
| Cellules avec erreur | Verifie la qualite d'execution | 0 ou erreur documentee |
| Cellules avec sorties conservees | Mesure le bruit dans le notebook | Sorties finales selectionnees |
| Mentions de chemins locaux | Verifie la portabilite | 0 |
| Lectures `read_excel` | Repere les chargements redondants | Lectures rationalisees |
| Exports `to_excel` | Verifie la destination des fichiers produits | Exports documentes vers `output/` |
| Captures finales | Preuves portfolio | Captures nommees et referencees |

## Ordre de demarrage recommande

1. R02 - Verifier les chemins de donnees.
2. R03 - Identifier l'erreur stockee.
3. R04 - Corriger ou documenter l'erreur.
4. R05 - Ajouter la section Mission et la capture mission.
5. R06 - Corriger le wording et l'objectif metier.
6. R07 - Inserer une table des matieres compacte.
7. R08 - Ventiler les phases I et II.
8. R09 - Harmoniser la structure du notebook.
9. R10 - Executer et documenter les controles qualite.
