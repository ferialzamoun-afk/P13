# 📊 SYNTHÈSE GLOBALE - Projet Bottleneck Data Optimization

## 🎯 Vue d'ensemble

**Projet** : Optimisation des données de stock et ventes - Bottleneck  
**Date** : 11/02/2026  
**Status** : Phase 1 complétée ✅  
**Environnement** : Python 3.10 | Pandas | Plotly  

---

## 📈 Tableau de synthèse général

### Architecture des données

```
┌─────────────────────────────────────────────────────────┐
│                    BOTTLENECK DATA                       │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ ERP.xlsx     │  │ WEB.xlsx     │  │ LIAISON.xlsx │  │
│  │ 825 produits │  │ N produits   │  │ Mapping      │  │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤  │
│  │ product_id ✓ │  │ sku          │  │ product_id   │  │
│  │ price        │  │ total_sales  │  │ id_web       │  │
│  │ stock_qty    │  │ ratings      │  └──────────────┘  │
│  │ status       │  │ 28 colonnes  │        │            │
│  │ purchase_pr  │  └──────────────┘        │            │
│  │ onsale_web   │         │                │            │
│  └──────────────┘         │                │            │
│         │                 │                │            │
│         └─────────────────┼────────────────┘            │
│                           ▼                              │
│                    MERGED (Fusion)                      │
│                     ~825 lignes                         │
│                   35+ colonnes                          │
└─────────────────────────────────────────────────────────┘
```

### Fichiers source - Statistiques

| Fichier | Lignes | Colonnes | Clé primaire | Doublons | Complétude |
|---------|--------|----------|--------------|----------|-----------|
| **ERP** | 825 | 6 | product_id | ❌ 0 | ✅ 100% |
| **Web** | ? | 28 | (index) | À vérifier | À vérifier |
| **Liaison** | ? | 2 | product_id | À vérifier | À vérifier |
| **MERGED** | ~825 | 35+ | product_id | ✅ 0 | À déterminer |

---

## 🔍 Analyse CODIR - Résultats Phase 1

### Qualité des données ERP

| Métrique | Résultat | Status |
|----------|----------|--------|
| **Doublons product_id** | 0 | ✅ Excellent |
| **Valeurs manquantes** | 0 | ✅ Excellent |
| **Complétude** | 100% | ✅ Excellent |
| **Prix négatifs/nuls** | À déterminer | ⏳ À auditer |
| **Stocks négatifs** | À déterminer | ⏳ À auditer |
| **Marges positives** | À déterminer | ⏳ À auditer |

### Qualité des jointures

| Type de jointure | Produits matchés | Non-matchés | Taux |
|------------------|------------------|------------|------|
| **ERP → Liaison** | À déterminer | À déterminer | À déterminer |
| **Liaison → Web** | À déterminer | À déterminer | À déterminer |
| **Produits Web orphelins** | À déterminer | À déterminer | À déterminer |

### Erreurs détectées

#### Erreurs de saisie
- [ ] Prix de vente négatifs
- [ ] Prix de vente nuls
- [ ] Stocks négatifs
- [ ] Prix d'achat > Prix de vente

#### Erreurs de cohérence
- [ ] Incohérence `stock_status` vs `stock_quantity`
- [ ] Ratings invalides (< 0 ou > 5)
- [ ] Produits orphelins (Web sans ERP)
- [ ] Articles sans correspondance

#### Erreurs de calcul
- [ ] Marges négatives détectées
- [ ] Rotation de stock aberrante
- [ ] Valorisation stock extrême

---

## 📊 Indicateurs clés - Phase 1

### Prix

```
Minimum     : À déterminer
Maximum     : À déterminer
Moyenne     : À déterminer
Médiane     : À déterminer
Std-Dev     : À déterminer
Outliers    : À identifier
```

### Stock

```
Minimum     : À déterminer
Maximum     : À déterminer
Moyenne     : À déterminer
Rotation    : À calculer (mois)
Sur-stockés : À identifier
Rupture     : À identifier
```

### Ventes (si disponible)

```
Total CA    : À calculer
Ventes moy  : À déterminer
Top 20      : À obtenir
Pareto 80%  : À calculer
```

---

## 🎯 Plan d'action - 4 Phases

### Phase 1 ✅ COMPLÈTE
- [x] Agrégation 3 fichiers
- [x] Fusion données ERP + Liaison + Web
- [x] Détection doublons ERP
- [x] Création colonne `stock_status_computed`
- [ ] Audit complet (À exécuter)

**Livrable** : `phase1_merged_data.xlsx`

### Phase 2 ⏳ À DÉMARRER
- [ ] Analyse exploratoire complète
- [ ] Identification outliers (Z-score, IQR)
- [ ] Analyse Pareto 80/20
- [ ] Corrélations multivariées
- [ ] Visualisations interactives

**Livrable** : Notebook Phase 2 + Rapport

### Phase 3 ⏳ À DÉMARRER
- [ ] Recommandations d'optimisation
- [ ] Classification ABC des produits
- [ ] Stratégie prix/stock optimale
- [ ] Plan d'action détaillé

**Livrable** : Rapport recommandations

### Phase 4 ⏳ À DÉMARRER
- [ ] Suivi KPIs
- [ ] Tableau de bord
- [ ] Rapports périodiques

**Livrable** : Dashboard Plotly

---

## 📁 Structure du projet

```
OC_P6_Optimisation/
├── 📄 README.md
├── 📄 main.py (orchestration)
├── 📄 audit_phase1.py (audit automatisé)
│
├── 📁 src/
│   ├── data_loader.py (chargement)
│   ├── exploratory_analysis.py (analyse)
│   ├── data_preparation.py (fusion)
│   ├── analysis.py (calculs)
│   └── __init__.py
│
├── 📁 data/
│   ├── erp.xlsx (825 produits)
│   ├── web.xlsx (N produits)
│   └── liaison.xlsx (mapping)
│
├── 📁 notebooks/
│   └── analysis_bottleneck.ipynb (exemple)
│
├── 📁 output/
│   ├── phase1_merged_data.xlsx
│   ├── phase1_audit_report.txt
│   ├── analysis_result.xlsx
│   └── ...
│
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 Phase_*.md (documents phases)
```

---

## ⚙️ Configuration technique

| Élément | Version |
|---------|---------|
| Python | 3.10.1 |
| Pandas | 2.3.3 |
| Plotly | 5.0.0+ |
| NumPy | 1.20.0+ |
| Jupyter | 1.0.0+ |
| Seaborn | 0.11.0+ |

---

## 🚀 Commandes clés

```bash
# Exécuter l'audit Phase 1 complet
python audit_phase1.py

# Exécuter le script principal
python main.py

# Lancer le notebook
jupyter notebook notebooks/analysis_bottleneck.ipynb

# Installer les deps
pip install -r requirements.txt
```

---

## 📊 Checklist complète

### Phase 1 - Agrégation & CODIR

#### Données sources ✅
- [x] ERP.xlsx chargé
- [x] Web.xlsx chargé
- [x] Liaison.xlsx chargé
- [x] Structures validées

#### Fusion données ✅
- [x] ERP + Liaison fusionnées
- [x] Résultat + Web fusionnés
- [x] Colonnes calculées (stock_status_computed)

#### CODIR ⏳
- [ ] Audit doublons Web
- [ ] Audit doublons Liaison
- [ ] Audit complétude Web
- [ ] Erreurs saisie identifiées
- [ ] Erreurs calcul identifiées
- [ ] Rapport généré

#### Livrables ✅
- [x] README complet
- [x] Modules réutilisables
- [x] Script audit
- [x] Documentation phases

### Phase 2 - Analyse exploratoire ⏳

#### À faire
- [ ] Analyse descriptive
- [ ] Détection outliers
- [ ] Corrélations
- [ ] Visualisations
- [ ] Rapport

---

## 💡 Prochaines étapes

1. **Immédiat** : Exécuter `python audit_phase1.py` pour audit complet
2. **Court terme** : Corriger les anomalies détectées
3. **Moyen terme** : Phase 2 - Analyse exploratoire
4. **Long terme** : Phases 3 & 4 - Optimisation et suivi

---

## 📞 Support & Documentation

| Document | Localisation |
|----------|--------------|
| README | `README.md` |
| Phase 1 | `Phase_1_Agregation_CODIR.md` |
| Phase 2 | `Phase_2_Analyse_exploratoire.md` |
| Phase 3 | `Phase_3_Optimisation.md` |
| Notebook | `notebooks/analysis_bottleneck.ipynb` |
| Audit | `audit_phase1.py` |

---

**Version** : 1.0  
**Dernière mise à jour** : 11/02/2026  
**Responsable** : Projet OpenClassrooms P6
