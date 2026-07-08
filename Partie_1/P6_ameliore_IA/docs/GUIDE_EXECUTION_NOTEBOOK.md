# Guide d'exécution du notebook Bottleneck

## 🎯 Objectif

Ce notebook analyse les données commerciales de Bottleneck en rapprochant trois sources (ERP, Web, Liaison) pour produire :
- **Chiffre d'affaires** : montant total et par produit
- **Tops références** : meilleurs contributeurs au CA
- **Analyse 20/80** : concentration des ventes
- **Anomalies** : prix invalides, marges négatives, ruptures de stock
- **Stocks & rotation** : indicateurs logistiques
- **Corrélations** : relations entre prix, stock, ventes

**Résultat attendu** : Un rapport analytique exploitable pour le CODIR de Bottleneck.

---

## 📋 Prérequis (avant de lancer)

### Vérifications à faire
- [ ] Python 3.12 ou supérieur installé
- [ ] Les fichiers `erp.xlsx`, `web.xlsx`, `liaison.xlsx` sont présents dans `P6_initial/data/`
- [ ] Les packages requis sont installés (pandas, plotly, openpyxl, numpy)
- [ ] VS Code ou Jupyter ouvert avec le notebook

### Comment vérifier les prérequis ?
1. Le notebook affichera automatiquement les versions requises au démarrage
2. Un tableau vert (✅) confirme que tout est OK
3. Un tableau jaune (⚠️) indique une action corrective

---

## 📁 Structure des dossiers (à respecter)

```
P13/
├── Partie 1/
│   ├── P6_initial/                          # Données source
│   │   ├── data/
│   │   │   ├── erp.xlsx                     # ✅ Obligatoire
│   │   │   ├── web.xlsx                     # ✅ Obligatoire
│   │   │   ├── liaison.xlsx                 # ✅ Obligatoire
│   │   └── notebook P6/
│   │       └── Template-Notebook-Bottleneck.ipynb
│   │
│   └── P6_ameliore_IA/                      # Notebook amélioré
│       ├── notebooks/
│       │   └── bottleneck_analyse_ameliore_final.ipynb    # ✅ Celui-ci !
│       ├── src/                             # Modules Python
│       │   ├── data_merging.py
│       │   ├── eda_analysis.py
│       │   ├── kpi_analysis.py
│       │   ├── quality_checks.py
│       │   └── stock_cleaning.py
│       ├── data/                            # Données intermédiaires
│       ├── output/                          # Graphiques générés
│       └── docs/                            # Documentation
│           └── GUIDE_EXECUTION_NOTEBOOK.md  # ← Vous êtes ici
```

**⚠️ Important** : Le notebook se localize automatiquement. Pas besoin de modifier les chemins !

---

## ⚙️ Étapes d'exécution (simple)

### 1️⃣ Ouvrir le notebook
- Fichier : `Partie 1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb`
- Logiciel : VS Code ou Jupyter

### 2️⃣ Lancer les vérifications initiales (Cells 1-4)
- Le notebook affiche les prérequis
- Affiche la structure attendue
- ✅ Si tout est vert, continuer
- ⚠️ Si jaune, corriger selon les indications

### 3️⃣ Phase I - Préparation (Cells 5-13)
- Charge les données ERP, Web, Liaison
- Applique des contrôles qualité automatiques
- Corrige les stocks négatifs si besoin
- Rapproche les données entre les 3 sources
- **Checkpoint** : Un résumé vert confirme Phase I OK

### 4️⃣ Phase II - Analyses (Cells 14-38)
- Calcule le chiffre d'affaires
- Analyse les tops références (20/80)
- Détecte les prix aberrants
- Analyse les stocks et marges
- Calcule les corrélations
- **Checkpoint** : Un résumé vert confirme Phase II OK

### 5️⃣ Validation finale (Cell 39-40)
- Affiche le temps d'exécution total
- Compte les fichiers générés
- **✅ SUCCÈS** = notebook exécuté sans erreur

---

## ✅ Vérifications rapides pendant l'exécution

| Point de contrôle | À vérifier | Bon signe |
|---|---|---|
| **Après prérequis** | Tableau vert avec versions | ✅ Versions OK |
| **Après Phase I** | Rapport de qualité affiché | ✅ Données chargées |
| **Après Phase I.2** | Stocks corrigés affichés | ✅ 0 stock négatif restant |
| **Après Phase I.3** | 714 produits rapprochés | ✅ Jointure réussie |
| **Après Phase II.1** | CA = 143 680 EUR | ✅ KPI principaux OK |
| **Après Phase II.2** | 435 produits pour 80% CA | ✅ Pareto calculé |
| **Après Phase II.3** | 3 prix invalides, 7 marges negatives | ✅ Anomalies détectées |
| **Après Phase II.6** | Corrélations affichées | ✅ Relations confirmées |
| **Après Phase II final** | Fichiers HTML générés | ✅ Dataviz créées |
| **À la fin** | Temps exécution < 5 min | ✅ Performance OK |

---

## 📊 Interprétation des résultats principaux

### Chiffre d'affaires (Phase II.1)
- **CA total** : 143 680,10 EUR = Ventes totales octobre
- **Produits actifs** : 689 = Références ayant au moins une vente
- **CA moyen par produit** : ~210 EUR = Indicateur de concentration

### Concentration des ventes (Phase II.2)
- **Rang Pareto** : 435 produits = Nombre de références pour atteindre 80% du CA
- **Interprétation** : 435/689 = 63% du catalogue = Moins concentré qu'un 20/80 classique
- **Implication** : Bottleneck vend un peu de beaucoup de produits (stratégie diversifiée)

### Anomalies détectées (Phase II.3-4)
- **Prix invalides (3)** : Nuls ou négatifs = Erreurs de saisie à corriger
- **Marges négatives (7)** : Prix de vente < prix d'achat = À valider métier
- **Ruptures (92)** : Stock nul = Risque de perte de ventes

### Stocks & rotation (Phase II.5)
- **Mois de stock moyen** : Indicateur de longueur des cycles
- **Rotation mensuelle** : Nombre de fois où le stock se renouvelle par mois
- **Produits sans vente** : Surstock potentiel

### Corrélations (Phase II.6)
- **Prix ↔ Prix d'achat** : Relation forte confirmée (politique de prix cohérente)
- **Stock ↔ Ventes** : Relation pour optimiser approvisionnement
- **CA ↔ Marge** : Relation pour rentabilité

---

## ❓ FAQ & Dépannage

### Q1 : Le notebook prend trop de temps ?
**R** : Normal ! Plotly génère des graphiques interactifs.
- Temps attendu : 3-5 minutes
- Si > 10 min : peut y avoir un problème de chargement des données

### Q2 : J'obtiens une erreur "Fichier non trouvé" ?
**R** : Vérifier que les 3 fichiers sont dans `P6_initial/data/` :
- `erp.xlsx`
- `web.xlsx`
- `liaison.xlsx`

### Q3 : Le notebook affiche "⚠️ À vérifier" partout ?
**R** : Vérifier les conditions du système :
- Python 3.12+
- Packages à jour (pandas 2.3.3+, plotly 5.0+)
- Relancer le notebook en entier (Kernel → Restart)

### Q4 : Les graphiques n'apparaissent pas ?
**R** : Problème d'affichage Plotly dans VS Code.
- Solution 1 : Relancer le notebook
- Solution 2 : Ouvrir dans Jupyter Browser au lieu de VS Code
- Solution 3 : Les fichiers HTML sont sauvegardés dans `output/dataviz/`

### Q5 : Que faire des fichiers HTML générés ?
**R** : Les graphiques sont exportés dans `P6_ameliore_IA/output/dataviz/` :
- Ouvrir directement dans un navigateur
- Inclure dans une présentation client
- Joindre au rapport CODIR

---

## 📞 Support & Questions

Si le notebook s'exécute jusqu'au bout (✅ final), vous avez :
- ✅ Données fiabilisées
- ✅ KPI validés
- ✅ Anomalies détectées
- ✅ Graphiques exportés
- ✅ Rapport exploitable

**Prêt à partager avec le CODIR !**

---

## 📌 Notes importantes

- Ce guide est conçu pour des **utilisateurs métier** (pas de code à modifier)
- Le notebook est **reproductible** : mêmes données = mêmes résultats
- Les **chemins relatifs** s'adaptent automatiquement
- Les **graphiques** sont interactifs (zoom, survol, etc.)
- Les **listes détaillées** (M08.3b, M08.4b) affichent tous les produits anormaux
