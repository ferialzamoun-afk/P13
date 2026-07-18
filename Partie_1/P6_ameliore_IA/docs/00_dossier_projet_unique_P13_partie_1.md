# Dossier projet unique - P13 Partie 1

## 1) Fiche projet

- Projet: Amelioration du livrable P6 Bottleneck (stocks, ventes, anomalies)
- Perimetre: Partie 1 du P13 (pilotage data augmente par IA)
- Objectif principal: rendre le livrable plus fiable, reproductible, explicable et exploitable metier
- Date de consolidation: 2026-07-18

## 2) Resume executif

> **Source documentaire unique** : ce document est la reference complete de P13 Partie 1. Les fichiers `Partie_1/01_*.md` a `08_*.md` sont des syntheses courtes miroir ; en cas d'ecart, ce dossier unique et les fichiers detailles de `P6_ameliore_IA/docs/` font foi.

Le projet consolide l analyse ERP/Web/Liaison pour produire des KPI utiles au CODIR et une priorisation actionnable des anomalies.

Chaine metier retenue:

1. Detecter
2. Expliquer
3. Prioriser
4. Decider

Socle de decision:

- Isolation Forest + SHAP + controles qualite

Renfort de priorisation:

- K-Means/kNN (en complement, pas en remplacement)

Regle BC05 retenue:

- `Critique` = score strict IF + SHAP + impact business (`critical_score >= 0.65`).
- `A surveiller` = score large IF + kNN + K-Means + SHAP + impact business (`surveillance_score >= 0.45`).
- kNN et K-Means ordonnent les investigations mais ne suffisent plus a declencher une urgence critique.

## 3) Contexte et besoin metier

Contexte: 3 sources (ERP, web, liaison) avec risques de valeurs incoherentes, jointures incompletes et alertes prix/stock.

Besoin reformule:

- Fiabiliser les donnees avant analyse
- Produire des KPI lisibles
- Detecter et expliquer les anomalies critiques
- Prioriser les actions de correction

Reference detaillee:

- docs/01_cahier_des_charges_P13_partie_1.md

## 4) Methode retenue

Qualite des donnees:

- Controles de qualite transversaux
- Pandera pour controles amont

Detection et explicabilite:

- Isolation Forest pour detection multivariee
- SHAP pour expliquer les alertes

Priorisation:

- K-Means/kNN pour ordonner le backlog de surveillance, sans passage critique automatique

Gouvernance qualite:

- Pandera en amont du scoring
- Great Expectations en aval de publication

Regle de blocage:

- Echec Pandera: arret analyse
- Echec GE: publication bloquee

Reference detaillee:

- docs/02_veille_technologique_P13_partie_1.md

## 5) Resultats metier consolides

KPI principaux:

- Chiffre d affaires total: 143680.10 EUR
- Produits avec CA positif: 689
- Pareto 80 pourcent du CA: rang 435
- Ruptures/stock nul: 92
- Prix invalides: 3
- Marges negatives: 7
- Correspondances web actives: 714
- Sans correspondance web active: 111

References detaillees:

- docs/06_synthese_finale_P13_partie_1.md
- docs/05_matrice_indicateurs_P13_partie_1.md

Resultats BC05 decisionnels:

- Matrice complete: 825 produits = 1 critique, 172 a surveiller, 652 normaux.
- Tableau dashboard filtre courant: 713 lignes alignees = 1 critique, 152 a surveiller, 560 normaux.
- 36 alertes statistiques immediates, 25 alertes Isolation Forest, 4 clusters K-Means, 42 alertes kNN.

## 6) Etat reel notebook (verification locale)

Notebook cible:

- notebooks/bottleneck_analyse_ameliore_final.ipynb

Metriques verifiees localement (2026-07-18):

- Cellules totales: 65
- Cellules code: 28
- Cellules markdown: 37
- Sorties erreur/stderr: 0

Point important:

- Certaines anciennes traces documentaires mentionnent 49 ou 50 cellules. Pour la livraison, la valeur de reference est la verification locale ci-dessus.

## 7) Livrables disponibles

Livrables de pilotage:

- docs/01_cahier_des_charges_P13_partie_1.md
- docs/02_veille_technologique_P13_partie_1.md
- docs/03_journal_ia_P13_partie_1.md
- docs/04_plan_projet_P13_partie_1.md
- docs/05_matrice_indicateurs_P13_partie_1.md
- docs/06_synthese_finale_P13_partie_1.md

Livrables operationnels:

- notebooks/bottleneck_analyse_ameliore_final.ipynb
- output/dataviz/ (13 graphiques Phase II + 12 visuels BC05)
- output/captures/

Exports notebook synchronises:

- `notebooks/output/bc05_matrice_decisionnelle.csv`
- `notebooks/output/bc05_matrice_critique_surveillance.csv`
- `notebooks/output/bc05_alertes_actionnables.csv`
- `notebooks/output/bc05_anomalies_summary.csv`
- `notebooks/output/bc05_iforest_alerts.csv`
- Copies operationnelles dans `P6-Dashboard/data/` via `P6-Dashboard/sync_bc05_exports.py`.
- Exports qualite sources brutes synchronisables vers `P6-Dashboard/data/quality_reporting/`.

Livrables dashboard:

- P6-Dashboard/streamlit_app.py
- P6-Dashboard/docs/GUIDE_UTILISATEUR_DASHBOARD.md

Livrables publics portfolio:

- Voir le dossier MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Amelioration_P6_IA (README + mode d emploi dashboard)

## 8) Mode d exploitation

### 8.1 Exploiter le notebook

1. Ouvrir le notebook ameliore.
2. Verifier les chemins de donnees.
3. Executer dans l ordre.
4. Verifier le rapport qualite et les KPI.
5. Exporter les sorties utiles.

Reference:

- docs/GUIDE_EXECUTION_NOTEBOOK.md

### 8.2 Exploiter le dashboard

Parcours recommande:

1. Reporting qualite
2. Tableau decisionnel
3. Filtres metier
4. Traitement Critique puis A surveiller
5. Export matrice d action

Reference:

- P6-Dashboard/docs/GUIDE_UTILISATEUR_DASHBOARD.md

## 9) IA critique et tracabilite

- Journal IA maintenu avec decisions humaines explicites
- 26 prompts documentes au global
- 13 prompts directement lies au flux BC05 detecter/expliquer/prioriser/decider

Reference:

- docs/03_journal_ia_P13_partie_1.md

## 10) Risques, limites, points de vigilance

- Donnees limitees au perimetre fourni
- Resultats statistiquement pertinents mais validation metier necessaire
- Jointures ERP/Web a surveiller
- Publication publique a securiser (secrets, hygiene repo)

References:

- docs/06_synthese_finale_P13_partie_1.md
- docs/07_checklist_publication_github.md

## 11) Checklist finale de livraison

- Notebook executable sans erreur bloquante
- KPI et exports presents
- Documentation de pilotage complete
- Guide utilisateur dashboard disponible
- Liens publics valides
- Aucun secret dans les fichiers publics

## 12) Version courte pour partage

Ce dossier unique est la reference de livraison pour P13 Partie 1.
Il permet, en un seul document, de comprendre le besoin metier, la methode, les resultats, les preuves, les limites et la procedure d exploitation notebook/dashboard.