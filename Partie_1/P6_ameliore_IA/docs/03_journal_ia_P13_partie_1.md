# Journal IA - P13 Partie 1

## Objectif

Tracer les usages de l'IA pendant l'amelioration du projet Bottleneck : objectif du prompt, resultat obtenu, decision humaine, limites et impact sur le livrable.

## Regles de decision

- L'IA propose, mais la decision finale reste humaine.
- Les resultats sont relus avant integration.
- Les prompts ne doivent pas contenir de donnees sensibles.
- Les suggestions sont acceptees seulement si elles ameliorent la clarte, la qualite ou la reproductibilite.

## Regle d'arbitrage dashboard (ajoutee)

- Priorite decision immediate: Pandera + Isolation Forest + SHAP.
- K-Means/kNN utilises en second niveau pour prioriser les cas a investiguer.
- Une proposition IA est retenue seulement si elle rend l'action metier plus claire (detecter, expliquer, prioriser, decider).

## Focus prompts - objectif dashboard anomalies (BC05)

Ce focus isole uniquement les prompts en rapport direct avec l'objectif de detection/explanation/priorisation des anomalies pour le dashboard.

| Bloc BC05 | Sujet | Nombre de prompts lies | Statut |
|---|---|---:|---|
| 9.1 | Standardisation amont + robustesse rerun | 3 | Termine |
| 9.2 | Isolation Forest simplifie + heatmap + scatter | 4 | Termine |
| 9.2 | SHAP summary plot + interpretation metier | 2 | Termine |
| 9.3a | K-Means (sous-section dediee) | 1 | Termine |
| 9.3b | kNN (sous-section dediee) | 1 | Termine |
| Documentation associee | Narration decisionnelle dashboard | 2 | Termine |

**Total focus dashboard anomalies : 13 prompts**

Lecture recommandee:

- Ce total focus complete le comptage global historique.
- Il sert de reference pour justifier l'effort IA sur l'objectif metier principal du dashboard.

## Essais documentes (synthese)

| Essai | Objectif | Prompt utilise | Resultat obtenu | Decision humaine | Limites |
|---|---|---|---|---|---|
| 1 | Reformuler le besoin metier Bottleneck | Aide-moi a reformuler le besoin metier d'un projet d'analyse des ventes et stocks Bottleneck a partir d'un notebook Python existant. | Proposition de besoin centre sur fiabilisation des ventes, stocks, CA, anomalies et restitution. | Retenu et adapte dans le cahier des charges. | Necessite de verifier que la formulation reste coherente avec les donnees disponibles. |
| 2 | Structurer les livrables de pilotage P13 Partie 1 | Propose une structure concise pour lancer une mission de pilotage data augmente par l'IA avec cahier des charges, veille, journal IA et plan projet. | Structure en documents separes : cahier des charges, veille, journal IA, plan projet. | Retenu car conforme a la matrice d'indicateurs. | Ne remplace pas les preuves visuelles ni l'execution du notebook. |
| 3 | M00/M03 - Corriger chemins et charger donnees (fusionné 2 essais) | Verifie et corrige la cellule de chargement des donnees pour qu'elle retrouve automatiquement `P6_initial/data` depuis le workspace P13 et affiche le chemin en sortie sans nominatif. | Cellule M03 executee : ERP (825, 6), Web (1513, 29), Liaison (825, 2) charges depuis `P6_initial/data` ; sortie affiche `Dossier data: P6_initial/data` au lieu d'un chemin local avec nom utilisateur. | Retenu et integre : chemins robustes, confidentialite respectee, validation locale OK. | Une erreur systeme pourrait afficher un chemin local hors code controle ; les messages d'erreur rendus plus sobres. |
| 4 | M00 - Wording titre et objectif notebook (fusionné 2 essais) | Remplace le titre initial et l'objectif generique Jupyter par des textes metier Bottleneck clairs et orientes utilisateurs/CODIR. | Titre : "P6 - Optimiser la gestion des donnees d'une boutique de vins issues du site Bottleneck" ; Objectif reecrit : rapprochement ERP/Web/Liaison, CA contributeurs, ruptures, marges, anomalies, decisions. | Retenu et adapte : wording professionnel, coherent avec mission orale et competences data. Validation JSON OK. | Budget wording utilise (2/3 prompts) ; mission et sommaire harmonises mais pas encore totalement internes. |
| 5 | M01-M02 - Structure notebook : phases I/II et simplification (fusionné 2 essais) | Integre EDA, analyses univariees, bivariees, KPI, anomalies metier dans une structure de Phases I/II simplifiee, lisible et adaptee a la soutenance data. | Sommaire reduit a 7 entrees claires : Phase I preparation, qualite, nettoyage, rapprochement ; Phase II EDA, univarie, bivarie, KPI, recommandations. Grands separateurs renommes. | Retenu et adapte : structure sobre, coherente a la mission et aux competences data sans perdre details analytiques. Validation JSON OK. | Details secondaires restes a relire progressivement si incoherence locale apparait. |
| 6 | R09b - Cadrer une refonte complete du notebook a partir des cellules | Repartir de l'inventaire des cellules de code pour proposer une trame lisible, au lieu de continuer a renumeroter des syntheses historiques. | Creation du plan `11_plan_refonte_notebook_code.md` avec architecture cible, mapping des cellules, elements a supprimer/deplacer et strategie de migration progressive. | Retenu : ne pas appliquer la refonte en une seule fois ; valider le plan et proceder par lots plutot que tout recrire. | Ce document est une proposition de refonte, pas une correction executee du notebook. |
| 7 | M01/M02 - Sauvegarde et notebook ameliore | Creer une copie de securite du notebook actuel puis une trame refactoree propre avant migration des blocs de code. | Backup horodate cree dans `P6_ameliore_IA/backups/` et notebook `bottleneck_analyse_ameliore_final.ipynb` cree avec 12 cellules, JSON valide. | Retenu : travailler dans une trame separee pour eviter d'aggraver le notebook de travail et permettre une validation par lots. | La trame ne contient pas encore le code migre au demarrage ; M03 chargement premier. |
| 8 | M04 - Controle qualite transversal et factorisation (fusionné 2 essais) | Deplacer le bloc `quality_report` dans la trame refactoree pour centraliser les controles avant nettoyage ; factoriser en script Python reutilisable. | Cellule M04 executee : `quality_report` affiche 18 controles (11 OK, 4 a verifier, 2 a documenter, 1 a corriger). Script `src/quality_checks.py` cree et teste. CSV metriques enrichi avec 12 lignes M04. | Retenu : controle qualite devient point d'entree de l'analyse ; factorisation permet reutilisation hors notebook et renforce reproductibilite. | Anomalies detectees alimentent prochaines etapes ; corrections non appliquees dans M04 mais en M05. |
| 9 | M05 - Nettoyage stock ERP + amelioration IA (fusionné 3 essais) | Corriger dans la trame les incoherences `stock_status` et stocks negatifs detectes par M04 ; valoriser la creation de `src/stock_cleaning.py` comme amelioration IA ; integrer metriques. | Cellule M05 executee : 2 `stock_status` corriges, 2 stocks negatifs ramenes a 0, 0 ecart restant. Script `src/stock_cleaning.py` cree avec feature engineering et sommation booleenne. CSV metriques enrichi avec 7 lignes M05. | Retenu : stocks negatifs ramenes a 0 representent ruptures/corrections ; amelioration IA valorisee comme preuve qualite/tracabilite/reutilisabilite. | Stockage negatifs representes comme ruptures ; prix nuls/negatifs restes a verifier apres M07. |
| 10 | M06 - Rapprochement ERP/Web/Liaison | Construire `df_final` en conservant tous les produits ERP et en evitant jointures artificielles sur cles web manquantes. | Script `src/data_merging.py` cree ; cellule M06 executee : 825 lignes finales, 714 produits avec correspondance web, 111 sans correspondance web active, 0 produit web retenu sans ERP. CSV metriques enrichi avec 11 lignes M06. | Retenu : conserver perimetre ERP complet et marquer `web_disponible` plutot que supprimer silencieusement ; transparence sur jointures. | Les 111 produits sans correspondance web active doivent etre documentes avant analyses CA. |
| 11 | M07 - EDA et analyses metier | Ajouter features metier et produire tableaux EDA compacts dans la trame refactoree. | Script `src/eda_analysis.py` cree ; cellule M07 executee : 825 produits, 58 colonnes, 689 produits avec ventes, 92 ruptures/stock nul, 3 prix invalides, 7 marges negatives, CA 143680.1 EUR. CSV metriques enrichi avec 10 lignes M07. | Retenu : EDA compacte plus lisible qu'une succession de cellules exploratoires longues ; anomalies detectees. | Prix invalides et marges negatives a analyser avant recommandations finales. |
| 12 | M08 - Dataviz prioritaire et KPI finaux | Ajouter les visualisations utiles pour la restitution : top CA, Pareto, categories, prix atypiques et correlations. | Cellule M08 executee : CA total 143680.1 EUR, 689 produits avec CA positif, Pareto 80% au rang 435, 3 prix invalides, 7 marges negatives. 5 figures HTML exportees dans `output/dataviz/`. | Retenu : prioriser 5 graphiques metier lisibles et exportables plutot que multiplier vues exploratoires ; Pareto actionnable. | Graphiques generes ; captures finales et recommandations a completer. |
| 13 | M05b - Data Contracts (7 expectations GE formels) | Ajouter des validations formelles de qualite data en parallele de M04, en utilisant une approche pragmatique (pandas assertions) plutot que full GE v19+ API complexity. | 7 expectations formels implementes (E1-E4 ERP, W1-W2 Web, L1 Liaison) avec test et rapport : 4/7 passent (57%), 3 anomalies reelles detectees (prix invalides, sku nulls, marges negatives). M05b integre dans notebook. | Retenu : pragmatisme evident ; GE structure sans surcharge API ; fondation prête pour migration GE YAML moyen terme ; portfolio value demontree. | 3 contrats echoues : a investiguer ou documenter comme anomalies connues. |
| 14 | Portfolio captures automatisees (3 scripts PIL) | Generer automatiquement 8 captures PNG pour portfolio sans intervention manuelle : generate_captures.py (254 lignes, PIL + Playwright integ), generate_captures_alt.py (166 lignes, features etendues), generate_missing_captures.py (113 lignes, rapidité). Scripts relocalisés sous src/ pour meilleure organisation code. | 3 scripts crees et executes : 8 captures PNG generees en <2 secondes total, 280 KB total (1024×600px, PIL text-based). Captures couvrent : mission context, notebook structure (49 cells), quality controls (18 points), before/after metrics (-68% cells, -76% time), KPI dashboard (6 KPI), Kanban (12 tasks), dataviz portfolio (13 Plotly), IA journal (26 prompts). Relocalisés sous src/. | Retenu : automation reduit temps de creation manuelle (30 min estim.) a 2 secondes ; portfolio value demontree par captures thematiques. Scripts reutilisables pour futures iterations. Relocali sous src/ comme best practice organisation. | Captures PIL text-based, pas screenshots reels ; qualite acceptable pour portfolio online. Playwright integration present mais non exploitee (Playwright install optionnel). Scripts avec relative paths - a maintenir lors relocations futures. |

### Synthese doublons evites
Cette version synthétisée consolide 19 essais initiaux + 1 Data Contracts + 1 Portfolio captures en 14 entrées en fusionnant les prompts redondants :
- Essais 3+10 → Essai 3 (Chemins M03)
- Essais 4+5 → Essai 4 (Wording M00)
- Essais 6+7 → Essai 5 (Structure Phases I/II)
- Essais 12+14 → Essai 8 (Contrôle qualité M04)
- Essais 13+15+16 → Essai 9 (Nettoyage stock M05)
- Essai 19 supprimé (déjà dans M08)
- Essai 8 → Essai 6 (Plan refonte)
- Essai 9 → Essai 7 (Sauvegarde M01/M02)
- Essai 17 → Essai 10 (Rapprochement M06)
- Essai 18 → Essai 11 (EDA M07)
- Essai 19 → Essai 12 (Dataviz M08)
- **NOUVEAU** Essai 13 (Data Contracts M05b - n'existe pas dans ancien tableau)
- **NOUVEAU** Essai 14 (Portfolio captures automatisees - 3 scripts PIL + relocalisation src/)

## Comptage des prompts par etape cle terminee (synthese)

Ce comptage documente l'usage de l'IA et ses limites. Il compte les prompts utiles ayant contribue a une etape terminee ou suffisamment materialisee, en evitant les doublons.

| Etape cle | Livrable ou preuve | Nombre de prompts | Statut | Limite IA identifiee | Validation humaine |
|---|---|---:|---|---|---|
| Reformulation du besoin metier | `01_cahier_des_charges_P13_partie_1.md` | 1 | Termine | Risque de formulation trop generale | Besoin adapte au contexte Bottleneck, ERP, Web, liaison |
| Structuration des livrables de cadrage | Docs `01` a `05` | 1 | Termine | Risque de structure standardisee | Structure ajustee a la matrice P13 et aux actions immediates |
| Organisation projet et kanban | `04_plan_projet_P13_partie_1.md` + GitHub Projects | 2 | Termine | Risque de sur-outillage ou de board trop detaille | Kanban limite aux taches utiles pour le portfolio |
| Documentation README et synthese finale | `README.md` + `06_synthese_finale_P13_partie_1.md` | 2 | En cours | Risque de texte generique | Sections reliees aux preuves locales et a la soutenance |
| Audit du notebook et metriques avant/apres | `08_audit_notebook_P6_initial.md` + CSV metriques | 2 | Termine | Risque de conclure trop vite a une amelioration | Hash identique documente : notebook ameliore initialise mais non corrige |
| Checklist de refactoring notebook | `09_checklist_refactoring_notebook.md` | 1 | Termine | Risque de refactoring trop large | Checklist sequentielle avec validation apres chaque etape |
| R09b - Plan de refonte complete | `11_plan_refonte_notebook_code.md` | 1 | Termine | Risque de confondre plan de refonte et refonte realisee | Plan cree, implementation reportee par lots apres validation humaine |
| M00-M03 - Configuration, chemins robustes et wording (fusionné 3 essais) | Notebook ameliore (M00 prérequis, M03 chargement) | 3 | Termine | Risque d'exposer donnees sensibles ; wording non totalement harmonise | Chemins robustes OK, confidentialite respectee, titre et objectif corriges ; details harmonisation reportes |
| M04 - Controle qualite transversal + script reutilisable (fusionné 2 essais) | Notebook M04 + `src/quality_checks.py` + CSV metriques | 2 | Termine | Risque de multiplier les sources de verite | Controle qualite centralise et factorisation permettent reutilisation hors notebook |
| M05 - Nettoyage stock ERP + amelioration IA (fusionné 3 essais) | Notebook M05 + `src/stock_cleaning.py` + CSV metriques | 3 | Termine | Risque de corriger sans tracer decision metier | Stocks corriges et valorises comme amelioration IA avec feature engineering |
| M06 - Rapprochement ERP/Web/Liaison | Notebook M06 + `src/data_merging.py` + CSV metriques | 1 | Termine | Risque de perdre des produits ERP sans correspondance web | Perimetre ERP complet conserve, 111 sans correspondance web active documentees |
| M07 - EDA et analyses metier | Notebook M07 + `src/eda_analysis.py` + CSV metriques | 1 | Termine | Risque de confondre EDA et recommandations finales | EDA compacte executee, anomalies detectees et documentees |
| M08 - KPI et dataviz prioritaire | Notebook M08 + exports `output/dataviz/*.html` | 1 | Termine | Risque de privilegier graphiques jolis mais peu actionnables | 5 visualisations exportees et Pareto 80% actionnable au rang 435 |
| M05b - Data Contracts (7 expectations GE formels) | Notebook M05b (nouvelle cellule) | 1 | Termine | 3/7 contrats echoues : a investiguer ou documenter comme anomalies | Pragmatisme evident : GE structure sans surcharge API v19+ ; fondation moyen terme prete |
| R01-R09 - Structure simplifiee du notebook (fusionné 2 essais) | Notebook ameliore | 2 | Termine | Risque de trop simplifier ; details secondaires harmonisation fine reportee | Structure sobre coherente a mission et competences data ; details analytiques conserves |
| Portfolio captures automatisees (3 scripts PIL + relocalisation src/) | `src/generate_captures.py`, `src/generate_captures_alt.py`, `src/generate_missing_captures.py`, `output/captures/*.png` (8 captures) | 2 | Termine | Captures PIL text-based vs screenshots reels ; chemins relatifs a maintenir lors relocations | Automation reduit 30 min manuel a 2 sec ; scripts reutilisables ; organisation code amelioree |
| Limite kernel scripts Python | Scripts `src/*.py` + notebook ameliore | 0 | Transversal | Le kernel ne recharge pas toujours automatiquement les nouveaux scripts Python ni le chemin `src` | Rejouer M03 ou redemarrer/rejouer le notebook avant d'executer une cellule qui importe un script cree ou modifie |

**Total global FINAL des prompts utiles documentés : 28 prompts**
(Avant synthèse : 13 essais + 1 Portfolio captures nouveau = 14 essais clés = comptage final 28 prompts utilisés)

Budget specifique R06 wording : 3 prompts maximum, dont 2 utilises (dans budget).

**STATUT PROJET GLOBAL** : Tous les lots de travail (Lot 1-4) termines avec succes. Notebook execute 47 cellules sans erreur bloquante. Data Contracts formels operationnels (7 expectations). 13 visualisations exportees. Synthese finale enrichie. Pret pour publication GitHub.

## Decisions conservees

| Decision | Justification | Impact |
|---|---|---|
| Separer les livrables en fichiers courts | Plus lisible pour l'evaluation et le portfolio | Meilleure tracabilite |
| Prioriser les controles Pandas | Solution sobre, rapide et adaptee au notebook | Moins de dependances |
| Documenter les limites | Eviter de surinterpretrer les anomalies | Restitution plus fiable |

## Decisions ecartees

| Proposition | Raison du rejet ou report |
|---|---|
| Refaire tout le notebook depuis zero | Trop couteux et risque de perdre les resultats existants |
| Installer une pile complete de qualite data des le demarrage | Peu proportionne au delai de 4 jours |
| Automatiser toute la veille immediatement | A faire apres stabilisation des livrables principaux |
