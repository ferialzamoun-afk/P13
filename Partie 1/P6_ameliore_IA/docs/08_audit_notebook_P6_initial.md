# Audit du notebook P6 initial - Bottleneck

## Objectif de l'audit

Evaluer l'etat du notebook P6 Bottleneck avant amelioration et publication portfolio, afin d'identifier les points forts, les risques, les corrections prioritaires et les preuves a produire dans la version `P6_ameliore_IA`.

Notebook audite : `P6_initial/notebook P6/Template-Notebook-Bottleneck.ipynb`.

Date de l'audit : 2026-07-07.

## Synthese rapide

Le notebook contient une analyse riche et deja avancee du projet Bottleneck, avec chargement des donnees ERP, Web et Liaison, controles ponctuels, visualisations Plotly, exports et syntheses. Pour une exposition portfolio, il doit cependant etre clarifie, separe de la version initiale, allege de ses sorties intermediaires et rendu plus reproductible.

Point actualise : le notebook ameliore a ete cree dans `P6_ameliore_IA/notebooks/bottleneck_analyse_amelioree.ipynb`, mais il n'a pas encore ete corrige ni refactore. Les metriques montrent qu'il s'agit a ce stade d'une copie de travail identique au notebook initial. La checklist de correction doit donc etre deroulee avant de parler d'amelioration effective.

## Metriques observees

| Metrique | Valeur observee | Interpretation |
|---|---:|---|
| Nombre total de cellules | 148 | Notebook volumineux, a structurer pour la lecture |
| Cellules de code | 105 | Beaucoup de logique dans le notebook |
| Cellules Markdown | 43 | Narration presente, mais a harmoniser |
| Cellules avec sorties conservees | 99 | Fichier potentiellement lourd et bruyant pour GitHub |
| Cellules avec erreur ou sortie stderr | 1 | Execution complete a verifier |
| Cellules avec sorties Plotly | 14 | Visualisations nombreuses, a selectionner pour le portfolio |
| Mentions `read_excel` | 11 | Plusieurs chargements ou lectures a rationaliser |
| Mentions `to_excel` | 3 | Exports a documenter et orienter vers `output/` |
| Mentions `quality_report` | 3 | Controle qualite transversal deja present dans la version auditee |

## Comparaison avant/apres - etat initialise

| Metrique | P6 initial | P6 ameliore initialise | Ecart | Interpretation |
|---|---:|---:|---:|---|
| Nombre total de cellules | 148 | 148 | 0 | Le notebook ameliore est une copie de depart, non encore refactoree |
| Cellules de code | 105 | 105 | 0 | Aucune reduction ou restructuration mesuree a ce stade |
| Cellules Markdown | 43 | 43 | 0 | Narration identique a ce stade |
| Cellules avec sorties conservees | 99 | 99 | 0 | Les sorties devront etre nettoyees ou selectionnees |
| Cellules avec erreur ou stderr | 1 | 1 | 0 | L'erreur stockee doit etre identifiee puis corrigee ou documentee |
| Sorties Plotly | 14 | 14 | 0 | Les graphiques utiles au portfolio restent a selectionner |
| Mentions de chemins locaux | 0 | 0 | 0 | Aucun chemin local personnel detecte par la recherche automatique |
| Mentions `read_excel` | 11 | 11 | 0 | Les lectures devront etre rationalisees si necessaire |
| Mentions `to_excel` | 3 | 3 | 0 | Les exports devront pointer vers un dossier `output/` documente |
| Mentions `quality_report` | 3 | 3 | 0 | Le bloc existe deja dans la base de travail, il reste a executer et documenter |
| Hash fichier | `FC21246AAEB9` | `FC21246AAEB9` | identique | Confirme l'absence de refactoring applique a ce stade |

## Points forts

| Point fort | Preuve ou observation | Impact portfolio |
|---|---|---|
| Analyse metier avancee | Nombreuses cellules de controle, KPI et visualisations | Montre une demarche analytique complete |
| Donnees sources identifiees | ERP, Web, Liaison | Perimetre du projet clair |
| Visualisations presentes | Sorties Plotly conservees | Permet de produire des captures utiles |
| Synthese P6 existante | `P6_initial/Extraits_P6/SYNTHESE_GLOBALE.md` | Base de restitution deja disponible |
| Controles qualite amorces | Bloc `quality_report` et controles ponctuels | Bon point d'appui pour la version amelioree |

## Risques et limites constates

| Risque | Constat | Impact | Priorite |
|---|---|---|---|
| Confusion initial/ameliore | Le notebook dans `P6_initial` contient deja `quality_report` | Comparaison avant/apres moins claire | Haute |
| Notebook ameliore non corrige | Le notebook existe dans `P6_ameliore_IA/notebooks/`, mais il est encore identique au notebook initial | L'amelioration reste a produire et a documenter | Haute |
| Reproductibilite a valider | Le dossier de donnees a ete renomme en `P6_initial/data/`, ce qui aligne mieux l'arborescence avec la logique `project_root / 'data'` du notebook | Execution complete encore a verifier | Moyenne |
| Sorties trop nombreuses | 99 cellules avec sorties conservees | Depot GitHub plus lourd et moins lisible | Moyenne |
| Erreur stockee | 1 cellule contient une sortie d'erreur ou stderr | Execution complete a revalider | Haute |
| Exports non formalises | Plusieurs `to_excel` detectes | Risque de fichiers disperses ou non documentes | Moyenne |
| Notebook tres long | 148 cellules dont 105 de code | Lecture difficile pour recruteur/evaluateur | Moyenne |

## Decisions d'audit

| Decision | Justification | Action associee |
|---|---|---|
| Creer une version amelioree separee | Eviter de modifier la preuve initiale | Fait : notebook cree dans `P6_ameliore_IA/notebooks/` |
| Conserver `P6_initial` comme reference | Necessaire pour l'avant/apres | Ne plus enrichir le notebook initial |
| Documenter les ameliorations | Montrer la transformation professionnelle du livrable | Completer T10 et la section 5.1 de la synthese |
| Standardiser les chemins | Rendre le projet executable hors machine locale | Centraliser les chemins et utiliser `Path` |
| Nettoyer les sorties | Ameliorer la lisibilite GitHub | Garder les sorties finales ou produire des captures |

## Actions recommandees

| ID | Action | Livrable | Statut |
|---|---|---|---|
| A01 | Creer `P6_ameliore_IA/notebooks/` | Dossier notebook final | [x] |
| A02 | Copier le notebook de travail vers `P6_ameliore_IA/notebooks/bottleneck_analyse_amelioree.ipynb` | Notebook ameliore separe | [x] |
| A03 | Verifier que les chemins pointent vers `P6_initial/data/` ou vers une copie documentee des donnees | Cellule de configuration | [~] |
| A04 | Conserver le bloc `quality_report` dans la version amelioree, pas comme preuve du P6 initial | Controle qualite transversal | [~] |
| A05 | Identifier la cellule avec erreur/stderr et la corriger ou documenter | Execution notebook validee | [ ] |
| A06 | Selectionner les graphiques vraiment utiles pour le portfolio | Captures finales | [ ] |
| A07 | Documenter les exports Excel et leur emplacement cible | Dossier `output/` | [ ] |
| A08 | Nettoyer les sorties non necessaires avant publication GitHub | Depot plus leger | [ ] |
| A09 | Derouler la checklist de refactoring avec validation apres chaque changement | `09_checklist_refactoring_notebook.md` | [ ] |

## Preuves a produire pour le portfolio

| Preuve | Description | Emplacement conseille |
|---|---|---|
| Capture audit initial | Structure ou extrait du notebook avant amelioration | `P6_ameliore_IA/output/` |
| Capture controle qualite | Tableau `quality_report` execute | `P6_ameliore_IA/output/` |
| Capture avant/apres amelioration | Exemple d'une cellule ou section simplifiee | `P6_ameliore_IA/output/` |
| Notebook final | Version propre et executable | `P6_ameliore_IA/notebooks/` |
| Synthese finale | Resultats, limites, recommandations | `P6_ameliore_IA/docs/06_synthese_finale_P13_partie_1.md` |

## Conclusion de l'audit

Le notebook P6 constitue une base riche mais encore trop proche d'un notebook de travail. La version amelioree separee existe maintenant, mais elle correspond encore a un etat initialise non corrige. La prochaine etape prioritaire est de derouler la checklist de refactoring avec validations progressives : chemins reproductibles, controles qualite executes, erreur stockee traitee, sorties selectionnees et documentation claire.
