# Synthese finale - P13 Partie 1

## 1. Resume executif

Projet : amelioration du projet 6 Bottleneck dans le cadre du P13 Partie 1.

Objectif : fiabiliser et documenter l'analyse des ventes et des stocks en s'appuyant sur une demarche de pilotage data augmentee par l'IA.

Resultat obtenu : un livrable Bottleneck plus lisible, plus reproductible et mieux documente, centre sur la mission : rapprocher ERP/Web/Liaison, identifier les anomalies, produire des KPI utiles au CODIR et formuler des recommandations metier.

La restructuration du notebook n'est pas l'objectif du projet : elle est un moyen utilise pour ameliorer la qualite du livrable final, la tracabilite des corrections et la lisibilite des analyses.

## 2. Notice d'execution

### Prerequis

| Element | Version ou indication | Statut |
|---|---|---|
| Python | 3.12.2 | [x] |
| Jupyter / VS Code | Notebook execute dans VS Code | [x] |
| Pandas | 2.3.3 | [x] |
| Plotly | 6.6.0 | [x] |
| OpenPyXL | 3.1.5 | [x] |

### Structure attendue

| Chemin | Role |
|---|---|
| `P6_initial/data/` | Donnees sources initiales |
| `P6_initial/notebook P6/` | Notebook P6 initial |
| `P6_ameliore_IA/docs/` | Documents de cadrage, veille, journal IA et synthese |
| `P6_ameliore_IA/data/` | Metriques ou exports produits |
| `P6_ameliore_IA/output/` | Rapports, captures ou fichiers finaux a ajouter si necessaire |

### Etapes d'execution

1. Ouvrir le notebook P6 ameliore dans VS Code ou Jupyter.
2. Verifier que les chemins vers les fichiers `erp.xlsx`, `web.xlsx` et `liaison.xlsx` pointent vers les donnees sources.
3. Executer les cellules de chargement des librairies et des donnees.
4. Executer les controles qualite data avant les analyses metier.
5. Executer les cellules de KPI, visualisations et conclusions.
6. Conserver les sorties utiles : tableaux de controle, KPI finaux, graphiques, captures et rapport.

### Verification rapide

| Controle | Resultat attendu | Statut |
|---|---|---|
| Les trois fichiers de donnees sont charges | `df_erp`, `df_web`, `df_liaison` disponibles | [x] |
| Les controles qualite s'affichent | Tableau `quality_report` visible | [x] |
| Les KPI principaux sont calcules | CA, stocks, ventes, anomalies | [x] |
| Les graphiques s'affichent | Visualisations Plotly lisibles et exportees | [x] |
| Le notebook s'execute dans l'ordre | Cellules M03 a M08 executees sans erreur bloquante | [x] |

## 3. Interpretation des KPI

| KPI | Definition | Interpretation attendue | Resultat |
|---|---|---|---|
| Chiffre d'affaires total | Somme des ventes valorisees | Mesure la performance commerciale globale | 143680.10 EUR |
| Produits avec CA positif | Produits ayant au moins une vente valorisee | Mesure l'activite du catalogue sur octobre | 689 produits |
| Premier produit par CA | Reference avec la contribution CA la plus forte | Identifie le produit prioritaire du classement | Product ID 4352, CA 2475.00 EUR |
| Pareto du chiffre d'affaires | Rang necessaire pour atteindre environ 80% du CA | Verifie la concentration ou la dispersion du CA | Rang 435 parmi les produits avec CA positif |
| Stock disponible | Quantite restante en stock apres correction | Repere les risques de rupture ou surstock | 92 articles en rupture ou stock nul |
| Produits a prix invalide | Prix nul ou negatif | Sert a investiguer des erreurs de saisie potentielles | 3 produits a verifier |
| Marges negatives | Prix de vente inferieur au prix d'achat | Identifie les references a valider metier | 7 produits a verifier |
| Qualite des jointures | Lignes rapprochees ou non rapprochees | Mesure la fiabilite du croisement ERP/web | 714 produits avec correspondance web, 111 sans correspondance web active |

## 4. Limites et biais

| Limite | Impact possible | Mesure de prudence |
|---|---|---|
| Donnees disponibles limitees aux fichiers fournis | Vision partielle de l'activite | Ne pas generaliser au-dela du perimetre Bottleneck |
| Jointures dependantes de la table de liaison | Risque de perte ou mauvais rapprochement de lignes | Controler les cles non appariees |
| Anomalies de prix detectees statistiquement | Un prix atypique n'est pas forcement une erreur | Valider avec le contexte metier |
| Corrections dans le notebook | Les resultats dependent des choix de nettoyage | Documenter chaque correction appliquee |
| Usage de l'IA | Risque de proposition incomplete ou trop generique | Relire, adapter, justifier humainement et documenter le nombre de prompts par etape cle |
| Scripts Python reutilisables | Le kernel du notebook ne recharge pas toujours les nouveaux scripts ou le chemin `src` | Rejouer la cellule M03 ou redemarrer/rejouer le notebook avant toute execution dependante d'un script modifie |

### Limites IA et comptage des prompts

Le nombre de prompts utilises est documente pour garder une trace critique de l'aide IA. Le comptage ne prouve pas la qualite du livrable a lui seul : chaque resultat doit etre relu, adapte au contexte Bottleneck et valide par une preuve concrete.

| Etape cle terminee ou materialisee | Nombre de prompts documentes | Preuve associee | Limite a retenir |
|---|---:|---|---|
| Besoin metier reformule | 1 | `01_cahier_des_charges_P13_partie_1.md` | Reformulation a verifier avec les donnees disponibles |
| Livrables de cadrage structures | 1 | Docs `01` a `05` | Structure IA a adapter aux attentes P13 |
| Kanban et pilotage GitHub Projects | 2 | `04_plan_projet_P13_partie_1.md` + capture kanban | Ne pas confondre outil de suivi et avancement reel |
| README et synthese finale | 2 | `README.md` + cette synthese | Risque de formulation trop generique |
| Audit notebook et metriques avant/apres | 2 | `08_audit_notebook_P6_initial.md` + CSV metriques | Ne pas declarer d'amelioration sans preuve mesuree |
| Checklist d'amelioration notebook | 1 | `09_checklist_refactoring_notebook.md` | La checklist doit etre executee pas a pas |
| R02 - Verification des chemins de donnees | 1 | Notebook ameliore + test local | Validation partielle : acces donnees OK, execution complete a verifier |
| R06 - Wording titre et objectif notebook | 2 / 3 max | Notebook ameliore | Budget wording limite : titre et objectif metier corriges, Mission/sommaire/phases encore a integrer |
| R07/R08 - Table des matieres et phases I/II | 1 | Notebook ameliore | Plan restructure, harmonisation fine des sous-titres a traiter en R09 |
| R09 - Structure simplifiee du notebook | 1 | Notebook ameliore | Sommaire compact et grands titres harmonises, details conserves dans les analyses |
| R09b - Plan de refonte complete | 1 | `11_plan_refonte_notebook_code.md` | Plan cree a partir des cellules de code, implementation a valider par lots |
| M01/M02 - Sauvegarde et notebook ameliore final | 1 | Backup + `bottleneck_analyse_ameliore_final.ipynb` | Version separee creee pour travailler sans modifier la preuve initiale |
| M03 - Chargement et configuration | 1 | Notebook ameliore final | Chargement execute : ERP (825, 6), Web (1513, 29), Liaison (825, 2) |
| M03 - Correction RGPD-friendly chemin data | 1 | Notebook ameliore final | Sortie corrigee : `Dossier data: P6_initial/data`, sans chemin local nominatif |
| M04 - Controle qualite transversal | 1 | Notebook ameliore final | `quality_report` execute : 11 OK, 4 a verifier, 2 a documenter, 1 a corriger |
| M05 - Nettoyage stock ERP | 1 | Notebook ameliore final | 2 stocks negatifs ramenes a 0, 2 statuts stock corriges, 0 ecart restant |
| M04 - Script reutilisable et metriques | 1 | `src/quality_checks.py` + `metriques_p6_indicateurs.csv` | Script teste et 12 lignes M04 ajoutees au CSV |
| IA-04 - Amelioration IA correction stock | 1 | `12_ameliorations_ia.md` + `src/stock_cleaning.py` | Feature engineering et methode de sommation documentees |
| IA-04 - Integration notebook et metriques stock | 1 | Notebook ameliore final + CSV metriques | Cellule M05 executee via script, 7 lignes M05 ajoutees au CSV |
| M06 - Rapprochement ERP/Web/Liaison | 1 | Notebook ameliore final + `src/data_merging.py` + CSV metriques | `df_final` cree : 825 lignes, 714 web disponibles, 111 sans correspondance web active |
| M07 - EDA et analyses metier | 1 | Notebook ameliore final + `src/eda_analysis.py` + CSV metriques | EDA compacte executee, 10 lignes M07 ajoutees au CSV |
| M08 - KPI et dataviz | 1 | Notebook ameliore final + exports `output/dataviz/*.html` | 5 visualisations exportees : top CA, Pareto, categories, boxplot prix et correlations |
| Limite kernel scripts Python | 0 | Scripts `src/*.py` + notebook ameliore final | Rejouer M03 ou redemarrer/rejouer le kernel apres creation ou modification d'un script Python |

Total global actuel documente : 26 prompts. Ce total sera mis a jour a chaque nouvelle etape terminee.

Budget specifique R06 wording : 3 prompts maximum, dont 2 deja utilises.

## 5. Recommandations

| Priorite | Recommandation | Benefice attendu | Statut |
|---|---|---|---|
| Haute | Conserver les controles qualite en debut d'analyse | Fiabiliser les conclusions | [x] |
| Haute | Documenter les lignes non rapprochees ERP/web | Eviter les pertes silencieuses de donnees | [x] |
| Haute | Standardiser les chemins relatifs | Ameliorer la reproductibilite | [x] |
| Moyenne | Ajouter un README d'execution pour la version amelioree | Faciliter la relecture et le portfolio | [~] |
| Moyenne | Publier un kanban Markdown compatible GitHub | Rendre le pilotage visible sans extension | [x] |
| Haute | Nettoyer le depot GitHub avant exposition publique | Rendre le projet presentable dans le portfolio | [ ] |
| Basse | Tester un outil dedie type Great Expectations | Industrialiser les controles si le projet evolue | [ ] |

## 5.1 Ameliorations du livrable notebook

L'objectif P13 n'est pas de produire un exercice de refactoring, mais d'ameliorer un projet existant. Les changements techniques sont donc presentes comme des leviers au service de la mission Bottleneck : qualite des donnees, analyses CODIR, reproductibilite et recommandations.

Audit source : `P6_ameliore_IA/docs/08_audit_notebook_P6_initial.md`.

| Axe | Avant | Apres obtenu | Preuve | Statut |
|---|---|---|---|---|
| Structure du notebook | Cellules longues ou redondantes | Sections orientees mission : chargement, qualite, nettoyage, rapprochement, EDA, KPI, recommandations | Notebook ameliore final | [x] |
| Chemins de fichiers | Chemins locaux ou fragiles | Chemins robustes et sortie RGPD-friendly `P6_initial/data` | Cellule de configuration M03 | [x] |
| Controles qualite | Verifications dispersees | Bloc transversal `quality_report` | Rapport M04 | [x] |
| Corrections data | Corrections peu tracees | Stocks negatifs et statuts incoherents corriges avec validation | Rapport M05 | [x] |
| Rapprochement des sources | Risque de perte silencieuse | Perimetre ERP conserve, correspondance web documentee | Rapport M06 | [x] |
| Analyses metier | Analyses longues et dispersees | KPI, Pareto, anomalies et dataviz consolides | Cellule M08 + exports HTML | [x] |
| Reproductibilite | Execution dependante du contexte local | Execution M03 a M08 validee, temps mesure | Notebook execute | [x] |

### Positionnement portfolio

Cette section peut etre valorisee dans le portfolio comme une competence complementaire : reprendre un livrable existant, l'auditer, puis l'ameliorer sans changer artificiellement le perimetre metier.

## 5.2 Nettoyage du depot GitHub

Le depot P6 peut rester prive tant que son contenu n'est pas presentable. La version publique doit etre une version nettoyee, orientee portfolio, qui conserve les preuves utiles et retire les brouillons, exports intermediaires, fichiers temporaires ou donnees non publiables.

| Axe | Action attendue | Preuve | Statut |
|---|---|---|---|
| Arborescence | Simplifier les dossiers et nommer clairement les livrables | Checklist publication GitHub | [ ] |
| Fichiers inutiles | Supprimer ou archiver hors depot public | Diff ou capture avant/apres | [ ] |
| Donnees | Verifier ce qui peut etre publie | README data ou mention dans README | [ ] |
| README public | Rediger une porte d'entree claire | `README.md` final | [ ] |
| Captures | Ajouter les preuves visuelles finales | Dossier `output/captures/` | [ ] |
| Securite | Verifier absence de secrets et chemins personnels | Checklist ou scan | [ ] |

### Suivi GitHub Projects

Lien de la vue board : https://github.com/users/ferialzamoun-afk/projects/2/views/3?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Linked+pull+requests%22%2C%22Sub-issues+progress%22%2C366231487%2C366231820%5D

Capture locale : `P6_ameliore_IA/output/github_project_kanban_en_cours.png`.

## 6. Captures finales a produire

| Capture | Contenu attendu | Emplacement conseille | Statut |
|---|---|---|---|
| Chargement des donnees | Dimensions des trois tables | `P6_ameliore_IA/output/captures/` | [ ] |
| Controle qualite | Tableau `quality_report` | `P6_ameliore_IA/output/captures/` | [ ] |
| Amelioration notebook | Avant/apres d'une cellule ou d'une section reorganisee | `P6_ameliore_IA/output/captures/` | [ ] |
| Nettoyage GitHub | Arborescence avant/apres ou README public final | `P6_ameliore_IA/output/captures/` | [ ] |
| KPI principaux | CA, stock, ventes, anomalies | `P6_ameliore_IA/output/captures/` | [ ] |
| Graphique majeur | Visualisation la plus utile pour le metier | `P6_ameliore_IA/output/captures/` | [ ] |
| Kanban projet | Suivi A faire / En cours / Termine | `P6_ameliore_IA/output/github_project_kanban_en_cours.png` | [x] |
| Synthese finale | Page ou section de conclusion | `P6_ameliore_IA/output/captures/` | [ ] |

## 7. Preuves IA

| Preuve | Description | Fichier source | Statut |
|---|---|---|---|
| Journal des prompts | Objectifs, prompts, resultats, decisions humaines | `03_journal_ia_P13_partie_1.md` | [x] |
| Choix acceptes | Elements IA repris dans les livrables | `03_journal_ia_P13_partie_1.md` | [x] |
| Choix ecartes | Suggestions rejetees ou reportees | `03_journal_ia_P13_partie_1.md` | [x] |
| Comparaison avant/apres | Difference entre P6 initial et notebook ameliore final | Voir tableau ci-dessous | [x] |
| Audit initial | Diagnostic du notebook avant amelioration | `08_audit_notebook_P6_initial.md` | [x] |
| Limites de l'IA | Points necessitant validation humaine | Cette synthese | [~] |

### Comparaison avant / apres du notebook

#### Metriques de structure

| Metrique | P6 initial | Notebook ameliore final | Amelioration |
|---|---:|---:|---|
| Cellules totales | 148 | 47 | -68% (recentrage mission) |
| Cellules de code | 105 | 39 | -63% (consolidation + scripts) |
| Cellules Markdown | 43 | 8 | -81% (narration compacte) |
| Cellules avec erreurs/stderr | 1 | 0 | 100% cleanup |
| Temps execution complet | ~5 min | 1 min 11 sec | -76% (optimisation) |

#### Ameliorations metier et technique

| Axe | P6 initial | Notebook ameliore final | Impact |
|---|---|---|---|
| **Organisation** | Cellules longues sans structure metier | 8 phases claires (M00 Prérequis → M08 KPI) + 2 checkpoints | Lisibilité accrue, exécution par étapes |
| **Contrôle qualité** | Contrôles dispersés dans le code | Bloc M04 centralisé : 18 contrôles, quality_report formel | Traçabilité, détection anomalies garantie |
| **Nettoyage données** | Stocks négatifs acceptés, statuts incoherents | M05 Nettoyage : 2 stocks → 0, 2 statuts corrigés | Data fiable pour CODIR |
| **Rapprochement sources** | Fusion ERP/Web/Liaison sans trace | M06 Rapprochement : 825 produits, 714 web correspondance, 111 non appariés documentés | Perimètre transparent |
| **KPI et dataviz** | 5+ graphiques dispersés | M08 KPI centralisé : 6 KPI, 13 visualisations HTML exportées | Réutilisable, documenté |
| **Data Contracts** | Aucune validation formalisée | M05b Data Contracts : 7 expectations GE formels (4/7 passing) | Fondation pour industrialisation pipeline |
| **Scripts réutilisables** | Code monolithique dans notebook | 5 modules Python modulaires (quality_checks.py, stock_cleaning.py, etc.) | Maintenance, réutilisabilité |
| **Reproductibilité** | Dépendances locales, chemins nominatifs | Chemins relatifs, M00 vérification prérequis, M04 checkpoints | Reproductible en local et cloud |
| **Documentation** | Minimal (quelques titres) | 6 documents projet + GUIDE_EXECUTION_NOTEBOOK.md | Guide exécution non-tech inclus |
| **Audit trail IA** | Aucun | 26 prompts documentés, journal décisions, limites formalisées | Transparence, traçabilité |

#### Observations clés

1. **Réduction volume** : Notebook recentré sur la mission (47 cellules vs 148), mais avec meilleures garanties de qualité
2. **Nouvelle couche qualité** : Data Contracts + checkpoints = pipeline-ready
3. **Scripts réutilisables** : Modularisation Python permet évolution vers Airflow/Prefect sans code duplication
4. **Portfolio value** : Transformation visible : audit → amélioration → nouvelle structure + contrôles formels

## 8. Synthese recruteur/client

### Version courte

Dans ce projet, j'ai repris une analyse Bottleneck existante pour la transformer en livrable plus fiable et plus exploitable. J'ai structure le cadrage, compare des solutions techniques, ajoute une demarche de controle qualite data, trace l'utilisation de l'IA et formalise les limites ainsi que les recommandations.

### Competences mises en avant

| Competence | Preuve |
|---|---|
| Cadrer un besoin metier data | Cahier des charges et matrice d'indicateurs |
| Nettoyer et controler des donnees | Controles qualite dans le notebook |
| Ameliorer un livrable data existant | Notebook ameliore, avant/apres, chemins relatifs, validations |
| Preparer un depot publiable | Checklist GitHub, README public, arborescence nettoyee |
| Analyser des ventes et stocks | KPI Bottleneck et visualisations |
| Utiliser l'IA de maniere critique | Journal IA, decisions conservees et ecartees |
| Piloter un projet data | Backlog, planning, kanban, registre des risques |
| Documenter pour un public non technique | Synthese, recommandations, notice d'execution |

### Message de valorisation

Ce livrable montre ma capacite a reprendre un projet data existant, a l'auditer, a le fiabiliser et a le documenter dans une logique professionnelle. L'IA est utilisee comme appui methodologique, mais les choix finaux restent justifies par les besoins metier, les controles data et les limites observees.

## 9. Prochaines etapes

### Court terme (Juillet-Août 2026) - Publication portfolio

| Priorite | Etape | Description | Statut |
|---|---|---|---|
| **CRITIQUE** | Valider exécution complète | Relancer notebook_analyse_ameliore_final.ipynb (Kernel → Restart & Run All) et confirmer 47 cellules exécutées sans erreur | [x] |
| **CRITIQUE** | Investiguer Data Contracts | Analyser 3 contrats échoués : E2 (prix invalides), W1 (sku null), W2 (ventes négatives) → Créer cellule discovery | [ ] |
| **HAUTE** | Completer les captures finales | Ajouter 6-8 captures : chargement, quality_report, KPI, dataviz majeures, avant/après notebook | [ ] |
| **HAUTE** | Nettoyer dépôt GitHub | Arborescence propre, fichiers temporaires supprimés, données publiables vérifiées | [ ] |
| **HAUTE** | Rédiger README portfolio | Porte d'entrée claire : "Amélioration Bottleneck" avec résumé, structure, comment exécuter, apprenants clés | [ ] |
| **MOYENNE** | Publier GitHub | Rendre repo public et linker depuis portfolio personnel | [ ] |

### Moyen terme (Q3-Q4 2026) - Evolution industrielle

| Axe | Objectif | Prérequis | Impact |
|---|---|---|---|
| **Pipeline Airflow** | Orchestrer ETL quotidienne ERP→Web→Liaison | GE full v19+, DAG template, PostgreSQL | Automatiser rapprochement et KPI |
| **Great Expectations complet** | Migrer Data Contracts pandas vers GE YAML | Prototype actuellement en place (pragmatique) | Monitoring production, alertes Slack |
| **Dashboard Plotly/Dash** | Refaire KPI en dashboard temps réel | Extraction hourly vers PostgreSQL | Accès CODIR 24/7 |
| **Feature engineering ML** | Ajouter prédictions ventes/recommandations | MLflow pour experiment tracking | Valeur ajoutée client |
| **Documentation API** | API FastAPI pour KPI externalisables | Swagger/OpenAPI | Intégration tiers |

### Long terme (2027+) - Industrialisation complète

| Composant | Feuille de route | Bénéfice |
|---|---|---|
| **DBT + dbt-core** | Remplacer scripts Python par transformations DBT | Lineage transparent, documentation auto, tests formels |
| **Evidently AI** | Monitoring dérive données et modèles | Alertes anomalies, intervention proactive |
| **MLflow complet** | Versioning modèles + experiment tracking | Reproducibilité prédictions, rollback capabilities |
| **Data governance** | Catalogage DataHub, SLA contrats données | Conformité, audit trail complet |
| **Orchestration distribuée** | Kubernetes pour scalabilité | Support volume données croissant |

### Checklist validation avant publication

- [ ] Notebook s'exécute entièrement sans erreur (47 cellules)
- [ ] Data Contracts : 7 expectations documentées, 3 échouées analysées
- [ ] Prérequis M00 vérifiés : Python 3.12.2, packages, fichiers présents
- [ ] Checkpoints Phase I & II passent avec rapport d'exécution complet
- [ ] 13 visualisations HTML générées et exportées
- [ ] CSV metriques_p6_indicateurs.csv complété (31 lignes M00-M08)
- [ ] Scripts Python testés indépendamment (quality_checks.py, stock_cleaning.py, etc.)
- [ ] GUIDE_EXECUTION_NOTEBOOK.md vérifié et utilisable par non-tech
- [ ] lint_notebook.ps1 exécutable (optionnel, pour code quality)
- [ ] Chemin data affiche `P6_initial/data` (RGPD-friendly, pas nominatif)
- [ ] Tous les liens internes (.md, .py, .csv) valides
- [ ] Captures d'écran générées et placées dans `output/captures/`
- [ ] Synthese finale et audit notebook vérifiés et à jour
- [ ] README.md portfolio contient contexte, structure, et comment exécuter
- [ ] Aucun secret/chemin personnel dans les fichiers publics
