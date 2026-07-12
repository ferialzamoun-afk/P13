# 📦 **Guide Assets Portfolio – Stratégies de Preuves & Partage**
*Comment valoriser des projets sans repo GitHub, avec des fichiers Power BI, ou sans interactivité web*

---

## **📋 Table des Matières**

1. [Inventaire des Preuves Disponibles](#1-inventaire-des-preuves-disponibles)
2. [Projets Sans Repo GitHub](#2-projets-sans-repo-github)
3. [Fichiers Power BI (.pbit / .pbix)](#3-fichiers-power-bi-pbit--pbix)
4. [Alternatives à Power BI Service (interactivité gratuite)](#4-alternatives-à-power-bi-service-interactivité-gratuite)
5. [Stratégie par Type de Preuve](#5-stratégie-par-type-de-preuve)
6. [Workflow Recommandé par Projet](#6-workflow-recommandé-par-projet)
7. [Checklist Assets Portfolio](#7-checklist-assets-portfolio)

---

## **1. Inventaire des Preuves Disponibles**

### **Situation dans MON-PORTFOLIO-DATA**

Votre portfolio dispose déjà de preuves pour chaque projet dans `/projets/PX/assets/` :

| Projet | Type de Preuve | Format | Accessibilité |
|--------|---------------|--------|---------------|
| **P3** | Requêtes SQL + PDF présentation | `.sql`, `.pdf` | ✅ Direct sur GitHub |
| **P4** | PDF présentation | `.pdf` | ✅ Direct sur GitHub |
| **P5** | PDF présentation | `.pdf` | ✅ Direct sur GitHub |
| **P7** | PDF présentation (Power BI) | `.pdf` | ✅ Direct sur GitHub |
| **P8** | PDF présentation | `.pdf` | ✅ Direct sur GitHub |
| **P10** | Notebook Python + PDF | `.ipynb`, `.pdf` | ✅ Via nbviewer |
| **P14** | PNG + PDF + Notebook | `.png`, `.pdf`, `.ipynb` | ✅ Direct sur GitHub |
| **P11** | Repo GitHub complet | Repo public | ✅ Repo dédié |
| **P12** | Repo GitHub complet | Repo public | ✅ Repo dédié |
| **P13** | Repo GitHub complet | Repo public | ✅ Repo dédié |
| **P9** | Repo GitHub + Streamlit | Repo + App | ✅ Live app |

### **Ce qui compte comme "preuve" pour un évaluateur**

```
Niveau 1 (Minimum) : Captures d'écran annotées = ✅ Suffisant
Niveau 2 (Standard) : PDF export + captures = ✅ Bon
Niveau 3 (Recommandé) : README + captures + code source = ✅ Très bien
Niveau 4 (Phare) : Repo dédié + app live + documentation = 🌟 Excellent
```

---

## **2. Projets Sans Repo GitHub**

### **Principe : MON-PORTFOLIO-DATA est votre repo-hub de preuves**

Vous n'avez PAS besoin d'un repo séparé pour chaque projet. Le dépôt `MON-PORTFOLIO-DATA` devient le **hub centralisé** qui contient :
- Les README de chaque projet (contexte, résultats, compétences)
- Les preuves visuelles (captures PNG, exports PDF)
- Les artefacts de code (SQL, notebooks, scripts)

### **Stratégie pour chaque cas**

#### **CAS A : Projet ancien sans code récupérable**

> "J'ai fait ce projet mais je n'ai plus le code source / il était sur un outil en ligne"

**Solution** : Preuve par la documentation

```
projets/P3_requetes_sql/
├── README.md                    ← Contexte + résultats + compétences
├── assets/
│   ├── captures/
│   │   ├── 01_schema_bdd.png   ← Schema de la base de données
│   │   ├── 02_requete_ex1.png  ← Capture d'une requête complexe
│   │   └── 03_resultats.png    ← Résultats dans l'outil
│   ├── Zamoun_P3_requetes.sql  ← Fichier SQL (si récupérable)
│   └── presentation.pdf        ← PDF de présentation
```

**README template** :

```markdown
# P3 – Requêtes SQL – [Contexte Client]

## Contexte
[Description de la mission]

## Démarche Technique
- Base de données : [MySQL / PostgreSQL / etc.]
- Nombre de tables : X
- Requêtes : JOIN, GROUP BY, sous-requêtes, vues

## Résultats
- [Résultat 1]
- [Résultat 2]

## Preuves
| Type | Fichier | Description |
|------|---------|-------------|
| Capture | [schema_bdd.png](assets/captures/01_schema_bdd.png) | Schéma BDD |
| SQL | [requetes.sql](assets/requetes.sql) | Requêtes principales |
| Présentation | [presentation.pdf](assets/presentation.pdf) | Slides de restitution |

## Compétences RNCP
BC01 – Structurer une base de données
BC02 – Extraire et agréger les données
```

#### **CAS B : Projet avec outil cloud (Tableau, Power BI, Metabase)**

> "J'ai créé un dashboard dans un outil qui n'exporte pas de code"

**Solution** : Exporter en PDF + captures détaillées

```bash
# Dans Power BI Desktop
Fichier → Exporter → PDF (toutes les pages)

# Captures détaillées
Chaque page du dashboard → Print Screen → PNG (annoté)
```

#### **CAS C : Projet de stage (données confidentielles)**

> "J'ai travaillé sur des données internes que je ne peux pas publier"

**Solution** : Documentation sanitisée (sans données réelles)

```markdown
## ⚠️ Note de Confidentialité
*Les données utilisées dans ce projet sont confidentielles (accord NDA).*
*Les captures sont anonymisées et les données d'exemple sont fictives.*

## Ce que j'ai réalisé
- [Description des tâches sans données réelles]
- [Résultats en termes de % d'amélioration sans les valeurs brutes]

## Preuves Disponibles
- [Capture anonymisée] du dashboard final
- [PDF] de la présentation au client (données remplacées)
- [README] avec description technique détaillée
```

---

## **3. Fichiers Power BI (.pbit / .pbix)**

### **Comprendre les formats**

| Format | Contenu | Taille | Partage |
|--------|---------|--------|---------|
| `.pbix` | Rapport + données + requêtes | **Lourd** (10Mo-1Go+) | ⚠️ Risqué (données incluses) |
| `.pbit` | Template = rapport SANS données | **Léger** (1-5Mo) | ✅ Safe + technique |
| `.pdf` | Export statique toutes pages | **Moyen** (1-5Mo) | ✅ Universel |
| `.png` | Captures d'écran | **Léger** (<1Mo) | ✅ Universel |

### **Utiliser .pbit sur GitHub**

```
projets/P7_dashboard_powerbi/
├── README.md
├── assets/
│   ├── sanitoral_dashboard.pbit  ← Template Power BI (sans données)
│   ├── presentation.pdf          ← Export PDF toutes les pages
│   ├── captures/
│   │   ├── 01_vue_globale.png
│   │   ├── 02_page_ventes.png
│   │   ├── 03_page_clients.png
│   │   └── 04_alerte_seuil.png
```

**Ce que voit le recruteur sur GitHub** :
- `presentation.pdf` → Preview intégré dans le navigateur ✅
- `captures/` → Images directement visibles ✅
- `sanitoral_dashboard.pbit` → Téléchargeable (necessite Power BI Desktop) ⬇️

### **Pour télécharger et ouvrir .pbit**

Ajoutez dans votre README :

```markdown
## 📥 Tester le Dashboard Localement

**Prérequis** : [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (gratuit)

1. Télécharger [`sanitoral_dashboard.pbit`](assets/sanitoral_dashboard.pbit)
2. Ouvrir dans Power BI Desktop
3. Connecter vos propres données (template sans données)

*Note : Les données originales sont confidentielles et non incluses.*
```

### **Peut-on rendre un .pbix interactif sur le web ?**

| Option | Coût | Interactivité web |
|--------|------|-------------------|
| **Power BI Service** (Microsoft 365) | 💰 Pro (10€/mois) | ✅ Oui, iframe embed |
| **Power BI Embedded** | 💰 Azure (très cher) | ✅ Oui, API |
| **Publish to web** | 🆓 Gratuit MAIS risque sécurité | ✅ Oui, mais données publiques |
| **Export PDF** | 🆓 Gratuit | ❌ Statique seulement |
| **Recréer en Streamlit** | 🆓 Gratuit | ✅ Oui, full interactif |

**Recommandation** : Pour un **portfolio public**, n'utilisez PAS "Publish to web" (données visibles par tous). Préférez PDF + captures + éventuelle recréation Streamlit.

---

## **4. Alternatives à Power BI Service (interactivité gratuite)**

### **Option A : Looker Studio (ex-Google Data Studio)**

**Avantage** : Gratuit, web-based, partage par lien public

```
1. Importer vos données dans Google Sheets
2. Créer dashboard dans Looker Studio (studio.google.com)
3. Partager via lien public "Viewer only"
4. Intégrer le lien dans votre README
```

**Limites** : Données dans Google Sheets (RGPD à vérifier), moins riche que Power BI

### **Option B : Streamlit (recommandé pour Python)**

**Avantage** : Gratuit, déjà utilisé (P9), puissant, pythonique

```python
# streamlit_app/dashboard_p7.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Recréer les visuels Power BI en Plotly
df = pd.read_csv("data/sanitoral_processed.csv")

st.title("Dashboard Sanitoral")

col1, col2, col3 = st.columns(3)
col1.metric("CA Total", "1.2M€", "+15%")
col2.metric("Taux Alerte", "23%", delta="-5%", delta_color="inverse")
col3.metric("Clients Actifs", "847")

fig = px.bar(df, x="region", y="ca", color="segment")
st.plotly_chart(fig)
```

**Déploiement** :
```bash
# Gratuit sur Streamlit Cloud
streamlit deploy
# URL : https://your-app.streamlit.app/
```

### **Option C : Plotly HTML (dashboards statiques interactifs)**

**Avantage** : Gratuit, 100% Python, interactif dans le navigateur, hébergeable sur GitHub Pages

```python
import plotly.express as px
import plotly.io as pio

fig = px.bar(df, x="categorie", y="ca")
pio.write_html(fig, "dashboard_p7.html")
```

**Héberger sur GitHub Pages** :
```
MON-PORTFOLIO-DATA/
├── dashboards/
│   ├── P7_sanitoral.html   ← Interactif dans le navigateur !
│   ├── P9_lapage.html
│   └── ...
```

**URL d'accès** : `https://ferialzamoun-afk.github.io/MON-PORTFOLIO-DATA/dashboards/P7_sanitoral.html`

> ✅ **100% interactif** (zoom, hover, filtre) sans licence Power BI

### **Option D : nbviewer (pour notebooks Jupyter)**

**Avantage** : Gratuit, affiche notebooks `.ipynb` avec output (graphiques, tables)

```markdown
# Dans votre README
[📓 Notebook avec visualisations](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P10_eau_potable/assets/notebook.ipynb)
```

> Le visiteur voit le notebook **avec tous les outputs** (graphiques Plotly/Matplotlib inclus) sans rien installer.

---

## **5. Stratégie par Type de Preuve**

### **Tableau de Décision**

| Situation | Preuve Prioritaire | Preuve Complémentaire |
|-----------|------------------|----------------------|
| Projet Python complet | Repo GitHub + README | Notebook nbviewer |
| Projet Power BI | PDF export + captures PNG | `.pbit` dans repo |
| Projet SQL | Fichier `.sql` dans repo | Captures des résultats |
| Projet sans code | Captures annotées + README | PDF présentation |
| Données confidentielles | README sanitisé + captures anonymisées | Description technique |
| Dashboard interactif voulu | Streamlit (Python) ou Looker Studio | Plotly HTML |

### **Hiérarchie de Preuves**

```
🌟 NIVEAU 4 (Phare) :
   Repo GitHub dédié + App live + Documentation complète
   → P9, P11, P12, P13

✅ NIVEAU 3 (Standard) :
   README détaillé + captures PNG + code source (SQL, notebooks)
   → P3, P10, P14

📄 NIVEAU 2 (Acceptable) :
   README + PDF présentation + captures
   → P4, P5, P7, P8

📋 NIVEAU 1 (Minimum) :
   README + captures annotées
   → P1, P2, P6 (ou tout projet sans autres assets)
```

---

## **6. Workflow Recommandé par Projet**

### **P7 – Dashboard Power BI (Sanitoral)**

**Problème** : Dashboard Power BI sans Power BI Service  
**Solution** :

```bash
# Étape 1 : Exporter en PDF (Power BI Desktop)
# Fichier → Exporter → PDF

# Étape 2 : Captures annotées
# Chaque page → Screenshot → Annoter avec flèches/légendes

# Étape 3 : Sauvegarder le .pbit (template sans données)
# Fichier → Exporter → Modèle Power BI (.pbit)

# Étape 4 : Organiser dans le repo
projets/P7_dashboard_powerbi/
├── README.md
├── assets/
│   ├── SANITORAL_dashboard.pbit  ← Uploadé sur GitHub
│   ├── SANITORAL_presentation.pdf
│   └── captures/
│       ├── 01_page_accueil.png
│       ├── 02_ventes_par_region.png
│       └── 03_alerte_seuil_15pct.png

# Étape 5 : Option Interactivité (facultatif)
# Recréer dashboard principal en Plotly HTML ou Streamlit
```

### **P3 – Requêtes SQL**

```bash
# Étape 1 : Récupérer fichier SQL
cp chemin/requetes.sql projets/P3_requetes_sql/assets/

# Étape 2 : Sur GitHub, SQL est présenté avec coloration syntaxique ✅

# Étape 3 : Captures des résultats dans l'outil SQL
# (pgAdmin, MySQL Workbench, DBeaver, etc.)

# Étape 4 : README avec contexte et résultats
```

### **P10 – Eau Potable (Notebook + PDF)**

```bash
# Assets déjà présents :
# - Notebook (.ipynb) → via nbviewer
# - PDF présentation

# Étape 1 : Uploader sur GitHub
git add projets/P10_eau_potable/assets/
git commit -m "Add: P10 assets - notebook + PDF"
git push

# Étape 2 : Lien nbviewer dans README
# https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P10_eau_potable/assets/notebook.ipynb

# Étape 3 : README avec contexte
```

### **P8 – Égalité Femmes/Hommes**

```bash
# Assets existants :
# - PDF présentation

# Étape 1 : Uploader PDF
git add projets/P8_egalite_femmes_hommes/assets/

# Étape 2 : README contexte + résultats + compétences BC04

# Étape 3 : (Optionnel) Captures des visuels Power BI/Tableau si disponibles
```

---

## **7. Checklist Assets Portfolio**

### **Par projet (minimum requis)**

**Projets Phares (P9, P11, P12, P13)** :
- [ ] Repo GitHub dédié et public
- [ ] README complet avec métriques précises
- [ ] Captures PNG de qualité (3-5 minimum)
- [ ] Liens fonctionnels (repos, notebooks, dashboards)
- [ ] Compétences RNCP documentées

**Projets Standard (P3, P7, P10, P14)** :
- [ ] README dans MON-PORTFOLIO-DATA avec contexte
- [ ] Au moins 2-3 captures PNG
- [ ] PDF présentation uploadé
- [ ] Code source si récupérable (SQL, notebooks)
- [ ] Note de confidentialité si applicable

**Projets Minimaux (P1, P2, P4, P5, P6, P8)** :
- [ ] README dans MON-PORTFOLIO-DATA avec contexte court
- [ ] Au moins 1 capture de preuve
- [ ] Mention des compétences RNCP

### **Assets à ne PAS publier**

- ❌ `.pbix` avec données réelles (confidentialité)
- ❌ Fichiers Excel/CSV avec données personnelles
- ❌ Clés API, tokens, mots de passe
- ❌ Données clients/employés nominatives
- ❌ Fichiers > 100Mo (GitHub limite)

### **Assets recommandés (à publier)**

- ✅ `.pbit` (template Power BI sans données)
- ✅ `.pdf` (exports présentations)
- ✅ `.png` (captures annotées)
- ✅ `.sql` (requêtes SQL)
- ✅ `.ipynb` (notebooks Jupyter sans données sensibles)
- ✅ `.py` (scripts Python)
- ✅ `.html` (exports Plotly interactifs)

---

## **Résumé Stratégique**

### **Architecture Recommandée pour MON-PORTFOLIO-DATA**

```
MON-PORTFOLIO-DATA/
├── README.md                        ← Landing page portfolio public
│
├── projets/
│   ├── P1_presentation/
│   │   ├── README.md                ← Contexte + captures + compétences
│   │   └── assets/captures/         ← Screenshots annotés
│   │
│   ├── P3_requetes_sql/
│   │   ├── README.md
│   │   └── assets/
│   │       ├── requetes_sql.sql     ← Visible + coloré sur GitHub ✅
│   │       ├── presentation.pdf     ← Preview GitHub navigateur ✅
│   │       └── captures/            ← PNG résultats requêtes
│   │
│   ├── P7_dashboard_powerbi/
│   │   ├── README.md
│   │   └── assets/
│   │       ├── dashboard.pbit       ← Template téléchargeable ⬇️
│   │       ├── dashboard.pdf        ← Preview toutes pages ✅
│   │       └── captures/            ← PNG par page du dashboard
│   │
│   ├── P9_librairie/                ← Lien vers repo + Streamlit
│   ├── P11_etude_marche/            ← Lien vers repo dédié
│   ├── P12_faux_billets/            ← Lien vers repo dédié
│   └── P13_portfolio/               ← Lien vers repo dédié (P13)
│
├── dashboards/                      ← Plotly HTML interactifs (optionnel)
│   ├── P7_sanitoral.html
│   └── P9_lapage.html
│
└── images/
    └── banniere.png
```

### **Pour les recruteurs non-techniques**

> "Pas de lien GitHub → pas de preuve" est **faux**. Ce qui compte :
>
> ✅ "Je comprends la démarche et les résultats"
> ✅ "Je vois les preuves (captures, PDF)"
> ✅ "Je comprends les compétences mobilisées"
>
> Un README bien rédigé + 3 captures de qualité = **preuve valide** pour RNCP et recruteurs.

### **Pour les évaluateurs techniques (RNCP)**

> Privilégier : Code source > notebooks > PDF > captures

---

## **Récapitulatif des Solutions**

| Besoin | Solution | Coût | Effort |
|--------|---------|------|--------|
| Publier dashboard Power BI | PDF + captures + .pbit | 0€ | 30 min |
| Dashboard interactif sur web | Plotly HTML ou Streamlit | 0€ | 1-3h |
| Prouver SQL sans repo | .sql dans MON-PORTFOLIO-DATA | 0€ | 10 min |
| Prouver projet sans code | README + captures + PDF | 0€ | 45 min |
| Données confidentielles | README sanitisé + captures anonymisées | 0€ | 1h |
| Power BI interactif en ligne | Recréer en Streamlit | 0€ | 2-4h |
| Power BI interactif (officiel) | Power BI Service Pro | 10€/mois | 1h |
