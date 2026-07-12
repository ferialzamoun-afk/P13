# Matrice des exigences Portfolio - P13 Partie 2

**Objectif** : Transformer les livrables techniques (Partie 1) en preuves portfolio claires et actionnables pour recruteur/client/évaluateur.

**Date** : 2026-07-13  
**Scope** : Portfolio P13 - Sélection des projets phares + preuves minimum + liens publics

---

## 1. Critères de validation avant soutenance

| # | Critère | Description | Preuve requise | Status |
|---|---|---|---|---|
| 1 | **Lisibilité** | Portfolio lisible en <5 min | README synthétique + captures | [ ] |
| 2 | **Résultat chiffré** | Chaque projet phare affiche ≥1 KPI | Tableau avant/après ou nombre | [ ] |
| 3 | **Liens publics** | Tous les dépôts/dashboards fonctionnels | URLs testées, pas de 404 | [ ] |
| 4 | **Sécurité data** | Pas de données sensibles exposées | Scan chemins, pas de secrets | [ ] |
| 5 | **Cohérence P1↔P2** | Liaison explicite Partie 1 → Partie 2 | Cross-links dans README | [ ] |
| 6 | **Pitch projet** | 3-5 lignes par projet : contexte+action+résultat | Gabarit unifié appliqué | [ ] |
| 7 | **Harmonie visuelle** | README et captures au même style | Template appliqué uniformément | [ ] |

---

## 2. Projets phares candidats (P2-P14)

### 2.1 Projets pour portfolio FINAL (À sélectionner)

| Projet | Type | Défi clé | Résultat chiffré | Compétence | Priorize |
|---|---|---|---|---|---|
| **P6 Bottleneck** | Data Analysis | Réconciliation 3 sources (ERP/Web/Liaison) | CA 143.7k€, 689 produits, 92 anomalies | Python, Data Contracts, Reproductibilité | 🔴 PHARE |
| **P12 Faux billets** | Classification ML | Prédire billets contrefaits via 6 features | Accuracy 95%+, AUC 0.98+ (si mesuré) | Scikit-learn, ACP, CAH | 🟠 PHARE |
| **P11 Étude marché** | Data Exploration | Analyser demande marché via API + Web scraping | 19k+ observations consolidées, segmentation | SQL, API, NLP preprocessing | 🟠 PHARE |
| **P10 Eau potable** | Dashboard BI | Dashboard DWFA pour gestion eau | 50+ indicateurs temps réel (si applicables) | Power BI, SQL, Business logic | 🟡 IMPORTANT |
| **P14 Stage** | Data Pipeline | Pipeline retail ERP→Streamlit→Power BI | 1M+ lignes traitées, temps réel | ETL, Streamlit, Power BI | 🟡 IMPORTANT |
| **P9 Librairie ventes** | EDA + Analyses | Analyses ventes par genre/auteur | CA par segment, top 10 produits | Pandas, Matplotlib, Business insight | 🟢 OPTIONNEL |
| **P8 DBT Project** | Modélisation | Transformation ERP avec DBT + staging | 200+ mart fields, lineage visible | DBT, SQL, Data engineering | 🟢 OPTIONNEL |
| **P7 Santé dashboard** | BI Portfolio | Dashboard SANITORAL 3 personas | 15 alertes, taux d'occupation | Power BI, Personas, UX | 🟢 OPTIONNEL |

### 2.2 Sélection recommandée (MVP Portfolio)

**Phares** (obligatoires pour soutenance) :
- [ ] **P6 Bottleneck** → Preuve : P13 Partie 1 complète
- [ ] **P12 Faux billets** → Preuve : Notebook ML + résultats
- [ ] **P11 Étude marché** → Preuve : Notebook EDA + segmentation

**Compléments** (si temps) :
- [ ] P10 Eau potable → Dashboard screenshot + link
- [ ] P14 Stage → Pipeline overview + captures

---

## 3. Structure preuves par projet

| Projet | Preuve Minimum | Format | Location | Priorité |
|---|---|---|---|---|
| **P6** | README P13, notebook 50 cells, 5 captures clés, dashboard Streamlit | `.md`, `.ipynb`, `.png`, `link` | `P13/Partie_1/` | 🔴 |
| **P12** | Notebook ML + confusion matrix/ROC, accuracy chiffre | `.ipynb`, `.csv` | `MON-PORTFOLIO-DATA/projets/P12/` | 🔴 |
| **P11** | Notebook EDA + segmentation résumé, n observations | `.ipynb`, `.md` | `MON-PORTFOLIO-DATA/projets/P11/` | 🔴 |
| **P10** | Dashboard screenshot, KPI synthèse | `.png`, `.pbix` template | `MON-PORTFOLIO-DATA/projets/P10/` | 🟠 |
| **P14** | Pipeline diagram, Streamlit link, Power BI screenshot | `.md`, `link`, `.png` | `MON-PORTFOLIO-DATA/projets/P14/` | 🟠 |
| **P9** | EDA top insights + top 10 produits | `.ipynb`, `.png` | `MON-PORTFOLIO-DATA/projets/P9/` | 🟢 |
| **P8** | DBT lineage diagram + marts count | `.png`, `.yml` | `MON-PORTFOLIO-DATA/projets/P8/` | 🟢 |
| **P7** | BI dashboard screenshot, 3 personas résumé | `.png`, `.md` | `MON-PORTFOLIO-DATA/projets/P7/` | 🟢 |

---

## 4. Template README unifié par projet

### 4.1 Gabarit standard (6 sections)

```markdown
# Projet X - [Titre métier]

## 📌 En 30 secondes
- Contexte (1 ligne)
- Défi (1 ligne)
- Résultat chiffré (1-2 chiffres clés)
- Compétence principale

## 🎯 Contexte métier
- Qui : [Stakeholder]
- Quoi : [Problème]
- Pourquoi : [Enjeu décisionnel]

## 📊 Démarche
- Étape 1 : [Action]
- Étape 2 : [Action]
- Étape 3 : [Action]

## 📈 Résultats mesurés
| KPI | Valeur | Unité |
| --- | --- | --- |
| Métrique 1 | X | unité |

## 🛠️ Compétences démontrées
- Compétence 1 : [Outil/Méthode]
- Compétence 2 : [Outil/Méthode]

## 🔗 Ressources
- Dépôt : [lien GitHub]
- Dashboard : [lien public]
- Notebook : [lien nbviewer]
```

### 4.2 Application par projet

| Projet | Template statut | Où revoir |
|---|---|---|
| P6 Bottleneck | À créer (README P13 actuel = docs interne) | P13/Partie_1/README.md |
| P12 Faux billets | À créer | MON-PORTFOLIO-DATA/projets/P12/README.md |
| P11 Étude marché | À créer | MON-PORTFOLIO-DATA/projets/P11/README.md |
| P10 Eau potable | À harmoniser | MON-PORTFOLIO-DATA/projets/P10/README.md |
| P14 Stage | À harmoniser | MON-PORTFOLIO-DATA/projets/P14/README.md |
| P9 Librairie | À harmoniser | MON-PORTFOLIO-DATA/projets/P9/README.md |
| P8 DBT | À harmoniser | MON-PORTFOLIO-DATA/projets/P8/README.md |
| P7 Santé | À harmoniser | MON-PORTFOLIO-DATA/projets/P7/README.md |

---

## 5. Compétences couvertes par projet

| Compétence | P6 | P12 | P11 | P10 | P14 | P9 | P8 | P7 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Python | ✅ | ✅ | ✅ | - | ✅ | ✅ | - | - |
| SQL | - | - | ✅ | ✅ | ✅ | - | ✅ | ✅ |
| ML/Stats | ✅ | ✅ | ✅ | - | - | ✅ | - | - |
| Data Contracts | ✅ | - | - | - | - | - | - | - |
| Power BI | - | - | - | ✅ | ✅ | - | - | ✅ |
| Streamlit | ✅ | - | - | - | ✅ | - | - | - |
| ETL/Pipeline | ✅ | - | - | - | ✅ | - | ✅ | - |
| Reproductibilité | ✅ | - | - | - | - | - | - | - |
| IA critique | ✅ | - | - | - | - | - | - | - |

---

## 6. Liens publics à vérifier/créer

| Projet | Type lien | URL | Status | Action |
|---|---|---|---|---|
| P6 | Dépôt GitHub | https://github.com/ferialzamoun-afk/P13 | ✅ | Rendre public |
| P6 | Dashboard Streamlit | https://p6-dashboard-wdcn5o8grt39nqtim6mgym.streamlit.app/ | ✅ | Vérifier accès |
| P12 | Dépôt GitHub | À créer | [ ] | Créer/publier |
| P11 | Dépôt GitHub | À créer | [ ] | Créer/publier |
| P10 | Dashboard Power BI | À publier | [ ] | Partage public |
| P14 | Dashboard Streamlit | À créer/publier | [ ] | Déployer |
| P9 | Dépôt GitHub | À vérifier | [ ] | Vérifier accès |
| P8 | Dépôt GitHub | À vérifier | [ ] | Vérifier accès |
| P7 | Dashboard Power BI | À vérifier | [ ] | Partage public |

---

## 7. Checklist MVP Portfolio (Partie 2)

### Phase 1 - Préparation (Cette semaine)
- [ ] Finaliser P13 Partie 1 (README public, LICENSE)
- [ ] Créer README gabarit unifié
- [ ] Identifier 3 projets phares minimum
- [ ] Extraire KPI par projet (avant/après ou résultats chiffrés)

### Phase 2 - Exécution (Semaine suivante)
- [ ] Harmoniser README P6 (portfolio version)
- [ ] Harmoniser README P12 (ML results)
- [ ] Harmoniser README P11 (marché analysis)
- [ ] Ajouter captures/screenshots à chaque projet

### Phase 3 - Publication (Avant soutenance)
- [ ] Rendre dépôts P13 publics
- [ ] Vérifier tous les liens (pas de 404)
- [ ] Créer fichier INDEX avec liens vers projets
- [ ] Tester accessibilité en 5 min max

### Phase 4 - Validation (Jour J)
- [ ] Vérifier que portfolio est lisible en <5 min
- [ ] Confirmer que ≥1 KPI chiffré par projet phare
- [ ] Tester tous les liens publics
- [ ] Vérifier pas de données sensibles exposées

---

## 8. Synthèse : État des lieux

| Critère | Status | Note |
|---|---|---|
| **Projets phares sélectionnés** | 🟠 Partiel | 3 phares (P6, P12, P11) à confirmer |
| **READMEs harmonisés** | 🔴 Non | À faire - créer gabarit unifié |
| **Captures générées** | ✅ Partiel | P6 = 9/9 OK, autres à faire |
| **KPI chiffrés** | 🟠 Partiel | P6 OK (143k€, 689 produits), autres à extraire |
| **Liens publics vérifiés** | 🔴 Non | À vérifier/créer |
| **Sécurité data** | 🟠 Partiel | P13 OK, autres à valider |
| **Cohérence P1↔P2** | 🔴 Non | À créer cross-links |

---

## 9. Prochaines étapes

### 🔴 CRITIQUE (Cette semaine)
1. [ ] Finaliser LICENSE + README.md public pour P13 Partie 1
2. [ ] Créer gabarit README unifié (6 sections standard)
3. [ ] Harmoniser README P6 (portfolio version)

### 🟠 HAUTE (Semaine suivante)
4. [ ] Extraire et documenter KPI P12, P11, P10
5. [ ] Harmoniser README P12 + P11
6. [ ] Générer captures manquantes (P12, P11, P10)

### 🟡 MOYENNE (Avant soutenance)
7. [ ] Vérifier/créer tous les liens publics
8. [ ] Tester portfolio end-to-end (<5 min)
9. [ ] Créer fichier INDEX central

---

**Contact** : Pour questions sur le portfolio, voir docs/ de P13 Partie 2.

