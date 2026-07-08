# 🍷 Optimisation de la gestion des données - Bottleneck Wine Shop

*Amélioration du livrable P6 avec IA, documentation critique et traçabilité complète*

---

## 📊 En 30 secondes

Ce projet transforme un notebook d'analyse exploratoire (148 cells) en livrable professionnel **reproductible, tracé et documenté** (49 cells, **-68% cells**, **-76% temps d'exécution**).

**Résultats clés :**
- 💰 **Chiffre d'affaires** : 143,680 EUR / mois (octobre 2026)
- 📦 **Catalogue** : 689 produits avec CA, ~80% du CA porté par 435 produits (#Pareto)
- 🚨 **Anomalies détectées** : 3 prix invalides, 7 marges négatives, 92 ruptures stock
- 📈 **Dataviz** : 13 graphiques interactifs générés pour présentation CODIR
- ✅ **Reproductibilité** : 100% - chemins relatifs, prérequis vérifiés, RGPD compliant

**Approche P13** : Pandans pragmatique (courts terme, J+30) avec **Data Contracts formalisés** en vue migration Future GE v19+ (moyen terme).

---

## 🎯 Contexte métier

**Qui** : Bottleneck, boutique de vins en ligne + ERP physique  
**Problème** : 3 sources de données (ERP, Web, Liaison) avec incohérences = manque de visibilité commerciale  
**Mission** : Réconcilier les données, identifier anomalies, fournir KPI au CODIR pour la décision  

---

## 📂 Structure du dépôt

```
Partie 1/P6_ameliore_IA/
├── README.md (ce fichier)
├── requirements.txt
├── notebooks/
│   └── bottleneck_analyse_ameliore_final.ipynb  [49 cells, ~1:11 min execution]
├── src/                                         [5 modules Python]
│   ├── quality_checks.py
│   ├── stock_cleaning.py
│   ├── data_merging.py
│   ├── eda_analysis.py
│   └── kpi_analysis.py
├── docs/                                        [8 fichiers documenting P13]
│   ├── 01_cahier_des_charges_P13_partie_1.md
│   ├── 02_veille_technologique_P13_partie_1.md
│   ├── 03_journal_ia_P13_partie_1.md
│   ├── 04_plan_projet_P13_partie_1.md
│   ├── 05_matrice_indicateurs_P13_partie_1.md
│   ├── 06_synthese_finale_P13_partie_1.md
│   ├── 07_checklist_publication_github.md
│   └── 13_great_expectations_strategy.md
└── output/
    ├── dataviz/        [13 fichiers HTML Plotly]
    └── captures/       [6-8 screenshots portfolio]
```

---

## 🚀 Quickstart

### 1️⃣ Prérequis
- **Python 3.12.2+** (vérification automatique dans le notebook)
- **Virtual Environment** (recommandé)

### 2️⃣ Installation
```bash
# Clone repo
git clone <repo-url> && cd <repo>

# Activate venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Exécuter le notebook
```bash
# Ouvrir Jupyter
jupyter notebook notebooks/bottleneck_analyse_ameliore_final.ipynb

# OU exécuter directement (VS Code / Jupyter Lab)
# Cell par cell en appuyant sur Shift+Enter
```

### 4️⃣ Résultats générés
- ✅ **Checkpoints** à chaque phase (M00, Phase I, Phase II, Final)
- ✅ **13 graphiques Plotly** dans `output/dataviz/` (CA, Pareto, anomalies, stocks, corrélations)
- ✅ **Rapport de qualité** : 18 contrôles + 7 Data Contracts validés
- ✅ **Temps total** : ~1 minute 11 secondes

---

## 📋 Méthodologie & Choix technologiques

### Contrôle qualité : Pourquoi Pandas vs alternatives ?

| Critère | Pandas | Great Expectations | Soda Core |
|---|---|---|---|
| **Temps d'implémentation** | ⚡ Rapide (J+30 OK) | 🐢 Courbe apprentissage steep | 🐢 Dépendance externe |
| **Reproductibilité** | ✅ Native | ✅ OK | ⚠️ Config YAML complexe |
| **Sobriété / Dépendances** | ✅ Minimal | ⚠️ Lourd | ⚠️ Lourd |
| **Audit trail** | ✅ Logs pandas | ✅ Full | ⚠️ Limité |
| **RGPD / Chemins** | ✅ OK | ✅ OK | ⚠️ À vérifier |

**Décision** : **Pandas pragmatique** (court terme) + **Data Contracts formalisés** (fondation pour GE v19+ moyen terme)

→ Voir [`docs/02_veille_technologique_P13_partie_1.md`](docs/02_veille_technologique_P13_partie_1.md) pour détails comparaison + roadmap 3-horizon

### Reproductibilité & RGPD
- ✅ **Chemins relatifs** robustes (`../../../P6_initial/data/`)
- ✅ **Zéro données nominatives** embarquées
- ✅ **Vérification prérequis** automatique (Cell 1)
- ✅ **Timekeeper** pour traçabilité performance

### Traçabilité IA
- 📌 **26 prompts Claude** documentés (essais 1-13)
- 📌 **Journal IA complet** : objectif → prompt → résultat → décision humaine → limitations
- 📌 **Chaque décision majeure** justifiée : contraintes appliquées, alternatives testées

→ Voir [`docs/03_journal_ia_P13_partie_1.md`](docs/03_journal_ia_P13_partie_1.md) pour traçabilité complète

---

## 📊 Résultats clés

### Phase I - Préparation & Qualité
| Étape | Résultat |
|---|---|
| Données chargées | 825 ERP + 1,513 Web + 825 Liaison |
| Contrôles qualité | **18 points** validés (11 OK, 4 à vérifier, 2 à documenter, 1 corrigé) |
| Stocks corrigés | 2 exceptions (< 0) identifiées et tracées |
| Rapprochement ERP/Web | 714 / 1,513 matches (47.2% web → anomalies à investiguer) |

### Phase II - Business KPI
| KPI | Valeur | Interprétation |
|---|---|---|
| **CA total** | 143,680 EUR | ✅ Revenue consolidée |
| **Produits avec CA** | 689 | ✅ Diversité catalogue |
| **Pareto 80%** | Rang 435 | ⚠️ Catalogue large, pas fortement concentré |
| **Marge moyenne** | 47.32% | ✅ Saine |
| **Stock / Rotation** | 2.98 mois avg | ⚠️ À optimiser (stockouts: 92 refs) |
| **Anomalies** | 10 détectées | 🚨 À investiguer (3 prix, 7 marges) |

### Dataviz générées (13 fichiers)
```
• chiffre_affaires_par_categorie.html
• courbe_pareto_80_20.html
• anomalies_prix_et_marges.html
• distribution_stocks.html
• rotation_mensuelle.html
• correlations_quantitatives.html
... (7 autres)
```

---

## 🔍 Limites & Prudences

| Limite | Impact | Recommandation |
|---|---|---|
| **1 mois données** (oct 2026) | Snapshot, pas trend | Confirmer sur multi-mois |
| **Corrélations ≠ causalité** | Risque faux signal | Utiliser comme aide décision, pas preuve |
| **Outliers statistiques** | Modèle IQR | Valider avec équipe métier (prix premium légitimes ?) |
| **Stock/Liaison manuels** | Risque sync | Investiguer 799 web sans match ERP |
| **Pas historique** | Données point-in-time | Intégrer historique pour tendances |

→ Voir [`docs/06_synthese_finale_P13_partie_1.md`](docs/06_synthese_finale_P13_partie_1.md) pour analyse complète

---

## 📈 Améliorations apportées au P6 initial

### Avant vs Après

| Dimension | P6 initial | P6 amélioré | Gain |
|---|---|---|---|
| **Cellules notebook** | 148 | 49 | **-68%** |
| **Temps exécution** | ~5 min | 1:11 min | **-76%** |
| **Code cells** | 105 | 39 | -63% |
| **Markdown cells** | 43 | 8 | -81% |
| **Erreurs/warnings** | 1 major | 0 | ✅ |
| **Contrôles qualité** | Implicites | **18 explicites** | ✅ |
| **Data Contracts** | 0 | **7 formalisés** | ✅ |
| **Checkpoints** | 0 | **4 internes** | ✅ |
| **Documentation IA** | 0 | **26 prompts tracés** | ✅ |
| **Reproductibilité** | Chemins locaux | Chemins relatifs | ✅ |

---

## 📚 Documentation

Tous les **10 critères mission P13 Partie 1** sont documentés et tracés :

1. ✅ **Améliorer livrable** → Voir synthèse avant/après ci-dessus
2. ✅ **IA critique & documentée** → [`docs/03_journal_ia_P13_partie_1.md`](docs/03_journal_ia_P13_partie_1.md) (26 prompts)
3. ✅ **Tester plusieurs options** → [`docs/02_veille_technologique_P13_partie_1.md`](docs/02_veille_technologique_P13_partie_1.md) (5 solutions)
4. ✅ **Critères explicites** → Tableau comparaison veille + notebook cell 2 (méthodologie)
5. ✅ **Justifier choix** → Chaque cellule commencée par "Pourquoi ?"
6. ✅ **Identifier besoins métier** → [`docs/01_cahier_des_charges_P13_partie_1.md`](docs/01_cahier_des_charges_P13_partie_1.md)
7. ✅ **Cahier des charges** → Document complet (CDC)
8. ✅ **Organiser projet** → [`docs/04_plan_projet_P13_partie_1.md`](docs/04_plan_projet_P13_partie_1.md) (backlog, kanban, planning)
9. ✅ **Outils gestion** → GitHub Projects Kanban (capture dans output/captures/)
10. ✅ **Intégrer contraintes** → 5 types documentés (délai, RGPD, budget, sobriété, conformité)

---

## 🛠️ Pour les développeurs / contributeurs

### Environnement local
```bash
# Setup
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Modifier / Tester
jupyter notebook
# ... edit & execute cells

# Lint & Format (optionnel)
ruff check src/
```

### Modules Python
- `quality_checks.py` : 18 contrôles de données (structure, valeurs, doublons)
- `stock_cleaning.py` : Corrections tracées des stocks anomalies
- `data_merging.py` : Rapprochement ERP/Web avec logging
- `eda_analysis.py` : Analyses exploratoires
- `kpi_analysis.py` : Calcul KPI métier

---

## 📞 Questions fréquentes

**Q : Puis-je relancer le notebook sur mes données ?**  
✅ Oui, remplacez `data/erp.xlsx`, `data/web.xlsx`, `data/liaison.xlsx` avec vos fichiers (format identique attendu).

**Q : Pourquoi Pandas et pas Great Expectations d'emblée ?**  
🔧 Délai court terme (J+30) + pragmatisme. GE v19+ planifiée pour Q1 2027 (voir roadmap [`docs/13_great_expectations_strategy.md`](docs/13_great_expectations_strategy.md)).

**Q : Les résultats sont-ils fiables ?**  
⚠️ Snapshot 1 mois (oct 2026). Validez anomalies avec équipes métier. Limites documentées dans cell 7 (Audit).

**Q : Comment contribuer ?**  
Voir [`CONTRIBUTING.md`](CONTRIBUTING.md) (si applicable).

---

## 📜 License

CC-BY-4.0 / MIT (À définir selon contexte)

---

## 👤 Contexte

**Projet** : OpenClassrooms - P13 Partie 1 (Data Analyst)  
**Date** : Juillet 2026  
**Mentee** : Portfolio P13 - Livrables finaux pour soutenance

---

## 🎓 Portfolio / Compétences démontrées

Ce projet valide les compétences :
- ✅ **Data cleaning & preparation** (18 contrôles, stock correction)
- ✅ **Data quality architecture** (Data Contracts, pragmatic GE)
- ✅ **Business analysis & KPI** (6 KPI, anomaly detection)
- ✅ **Reproducibility & governance** (relative paths, RGPD, audit trail)
- ✅ **IA governance & critical thinking** (26 prompts tracés, decisions humaines)
- ✅ **Project management** (backlog, kanban, planning)
- ✅ **Technical documentation** (8 docs, 13 captures, traçabilité complète)
