# Veille technologique - P13 Partie 1

## Objectif de veille

Identifier des outils et methodes utiles pour ameliorer le notebook Bottleneck, renforcer la qualite des donnees, securiser la publication du projet et rendre le livrable plus reproductible.

Date de lancement : 2026-07-07.
Derniere mise a jour : 2026-07-17.

## Storytelling cible (dashboard)

- Detecter: controles qualite + anomalies critiques.
- Expliquer: SHAP pour rendre l'alerte actionnable.
- Prioriser: K-Means/kNN pour organiser le backlog d'investigation.
- Decider: exports produits pour arbitrage CODIR.

## Criteres de comparaison

| Critere | Question associee |
|---|---|
| Pertinence metier | L'outil aide-t-il a fiabiliser l'analyse Bottleneck ? |
| Simplicite | Peut-il etre mis en place rapidement ? |
| Reproductibilite | Facilite-t-il une execution stable du projet ? |
| Securite | Reduit-il les risques avant publication GitHub ? |
| Sobriete numerique | Ajoute-t-il peu de dependances et de temps d'execution ? |
| Accessibilite | Aide-t-il a produire un livrable comprehensible ? |

## Tableau comparatif

| Solution | Usage possible | Points forts | Limites | Sobriete | Decision |
|---|---|---|---|---|---|
| Controles Pandas | Verifier valeurs manquantes, doublons, types, cles de jointure, bornes de prix | Deja disponible dans le notebook, rapide, transparent | Demande de coder les controles manuellement | Bonne : pas de dependance supplementaire | Retenu en priorite |
| Isolation Forest (scikit-learn) | Detection multivariee des anomalies produits (prix, marge, stock, CA/article) | Efficace sans labels, parametrable (contamination), interpretable avec pipeline clair | Sensible au choix des variables et a la standardisation | Bonne : deja dans stack sklearn | Retenu comme moteur principal de detection |
| SHAP | Explicabilite locale/globale des alertes Isolation Forest | Rend les alertes actionnables pour le CODIR, visualisation claire des contributions | Cout de calcul selon volume, besoin de mise en forme pedagogique | Moyenne : dependance supplementaire | Retenu en priorite avec IF |
| K-Means + kNN | Segmentation et score de rarete locale pour prioriser les investigations | Complete IF/SHAP pour ordonner le backlog | Ne remplace pas une detection primaire de risque | Bonne : sklearn natif | Retenu en second niveau |
| Great Expectations | Formaliser des tests de qualite data reutilisables | Cadre robuste, documentation claire, tests declaratifs | Mise en place plus lourde pour un notebook court | Moyenne : dependance et configuration ajoutees | A garder comme piste moyen terme |
| Ruff + nbQA | Controler style Python et qualite du code notebook | Ameliore lisibilite et maintenance | Peut necessiter adaptation du notebook existant | Bonne : execution ponctuelle | Retenu si temps disponible |
| ydata-profiling | Generer un rapport exploratoire automatique | Utile pour repérer rapidement distributions et valeurs atypiques | Rapport parfois lourd, moins cible metier | Moyenne a faible selon volume | Non prioritaire |
| Aikido Security | Scanner le depot avant publication GitHub | Controle securite complementaire, utile portfolio | Depend d'un depot publie ou connecte | Bonne si scan ponctuel | Retenu comme controle complementaire |

## Matrice de maturité Bottleneck par stade

### Stade 1 : Court terme (J+30) - Stabilisation & fiabilisation
**Objectif** : Consolider les données ERP/Web/Liaison, valider l'analyse, publier sur GitHub

| Outil | Besoin immédiat | Mise en œuvre | Technologie |
|---|---|---|---|
| Pandas | ✅ Oui | Phase I + II | Contrôles 18 points (doublons, manquants, clés) |
| Isolation Forest | ✅ Oui | Phase II | Detection anomalies multivariees |
| SHAP | ✅ Oui | Phase II | Explicabilite des alertes IF |
| K-Means/kNN | ✅ Oui | Phase II (complement) | Segmentation + rarete locale |
| Ruff/nbQA | ⚠️ Si temps | Phase III | Qualité code avant publication |
| Aikido Security | ✅ Workflow prêt, activation via secret GitHub | Phase IV | Scan sécurité GitHub |
| Great Expectations | ❌ Non prioritaire | Futur | Trop lourd pour 1 notebook |

**Livrables attendus** : Notebook exécutable, GUIDE_EXECUTION.md, 18 contrôles qualité documentés, 13 dataviz

---

### Stade 2 : Moyen terme (Q1-Q2 2026) - Automatisation & monitoring
**Objectif** : Pipeline quotidien ERP→Web, alertes anomalies, dashboards métier

| Outil | Besoin | Architecture | Technologie |
|---|---|---|---|
| Great Expectations | ✅ Oui | Suite tests GE après Phase I | Expectations sur colonnes critiques |
| Airflow/Prefect | ✅ Oui | Orchestration ETL Bottleneck | DAG quotidien ERP → Web → Analyse |
| Plotly/Dash | ✅ Oui | Dashboard temps réel | KPI quotidiens + anomalies |
| PostgreSQL | ✅ Oui | Datawarehouse Bottleneck | Historique 12 mois |

**Livrables attendus** : Pipeline ETL, GE suite complète (100+ expectations), dashboard temps réel, alertes Slack

---

### Stade 3 : Long terme (2027+) - Industrialisation & IA
**Objectif** : Prédictions demande, optimisation stocks, recommandations produits

| Outil | Besoin | Architecture | Technologie |
|---|---|---|---|
| Great Expectations | ✅✅ Oui | Data contracts avant ML | Expectations 200+, version control |
| DBT | ✅ Oui | Transformations ERP → datamart | dbt tests + freshness |
| MLflow | ✅ Oui | Tracking expériences ML | Prédictions rotation/marge |
| Evidently AI | ✅ Oui | Monitoring dérive modèles | Data drift + model performance |
| DuckDB | ⚠️ Opt | Analytics analytiques rapides | Requêtes <100ms sur 10M lignes |

**Livrables attendus** : Modèles ML production, monitoring dérive, recommandations produits, prédictions demande

---

## Choix retenus pour P13 Partie 1

### Phase immédiate (Semaine 1-2)
1. ✅ **Contrôles Pandas** : 18 points validation déjà implémentés
2. ✅ **Isolation Forest** : Détection principale des anomalies business
3. ✅ **SHAP** : Explication des alertes pour arbitrage CODIR
4. ✅ **K-Means/kNN** : Priorisation complémentaire des investigations
5. ✅ **Great Expectations** : Implémentation légère Phase I (5-6 expectations clés)
6. ✅ **Ruff/nbQA** : Script optionnel pour qualité code
7. ✅ **Aikido** : Workflow GitHub ajouté, activation finale via `AIKIDO_CLIENT_API_KEY`

### Arbitrage methodes pour la decision

- **Court terme (decision immediate)** : Isolation Forest + SHAP en priorite.
- **Moyen terme (priorisation fine)** : K-Means/kNN en complement, pas en remplacement.

### Justification implémentation Data Contracts
- **Court terme** : Pragmatique via pandas assertions (pas d'API complexity GE v19+)
- **Moyen terme** : Fondation prête pour migration GE YAML + Airflow (Q1-Q2 2027)
- **Portfolio** : Démontre compétence data quality engineering ET pragmatisme ingénierie
- **Effort réel** : 45 min pour 7 expectations formels avec anomaly detection (4/7 passent, 3 anomalies reelles detectees)

## Articulation Pandera et Great Expectations

Objectif: eviter le doublon et relier les controles de qualite a la decision metier.

| Niveau | Outil | Role principal | Moment d'execution | Effet metier |
|---|---|---|---|---|
| Controle amont | Pandera | Valider schema, types et regles critiques sur DataFrame | Avant scoring et analyses BC05 | Bloquer tot les erreurs de donnees |
| Controle aval | Great Expectations | Contractualiser et tracer les expectations de publication | Avant export/pipeline | Bloquer la diffusion d'un lot non conforme |

Regle de fonctionnement retenue:

- Si Pandera echoue: arret du flux analytique et correction data.
- Si Pandera passe mais GE echoue: analyse possible en interne, publication bloquee jusqu'a correction.
- Les regles critiques partagent un identifiant unique (ex. Q001 unicite product_id, Q002 price > 0, Q003 stock >= 0) pour garder une trace commune entre notebook et pipeline.

## Sources a verifier et conserver

| Source | Type | Utilite | Date de consultation |
|---|---|---|---|
| Documentation officielle Pandas | Documentation | Fonctions de controle et nettoyage | 2026-07-07 |
| Documentation Great Expectations | Documentation | Tests de qualite data | 2026-07-07 |
| Documentation Ruff | Documentation | Qualite de code Python | 2026-07-07 |
| Documentation nbQA | Documentation | Lint notebooks Jupyter | 2026-07-07 |
| Documentation Aikido Security | Documentation | Scan securite depot | 2026-07-07 |
| GitHub Docs | Documentation | Publication, README, alertes securite | 2026-07-07 |
| Documentation scikit-learn (Isolation Forest) | Documentation | Parametrage modele et bonnes pratiques | 2026-07-17 |
| Documentation SHAP | Documentation | Interpretablite et summary plot | 2026-07-17 |

## Mise en place retenue pour T12

- Workflow ajoute dans `.github/workflows/aikido.yml`
- Trigger sur `push` `main`, `pull_request` `main`, `workflow_dispatch` et scan planifie hebdomadaire
- Scan gate configure pour **SAST**, **IaC** et **secrets**
- Dependency scanning couvert via le cloud scan Aikido
- Activation finale conditionnee par le secret GitHub `AIKIDO_CLIENT_API_KEY`

## Pistes d'amelioration continue

| Piste | Priorite | Gain attendu |
|---|---|---|
| Ajouter une section controles qualite dans le notebook | Haute | Fiabiliser les conclusions |
| Standardiser les chemins relatifs | Haute | Ameliorer la reproductibilite |
| Ajouter un README d'execution | Haute | Faciliter la relecture |
| Activer une alerte GitHub/Dependabot | Moyenne | Automatiser une partie de la veille securite |
| Tester Great Expectations sur un extrait | Basse | Evaluer une industrialisation future |
