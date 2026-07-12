# 📖 **Guide Utilisateur GitHub Pages – Portfolio Data Analyst**
*Documentation complète pour valoriser votre portfolio via GitHub Pages*

---

## **📋 Table des Matières**

1. [Qu'est-ce que GitHub Pages ?](#1-quest-ce-que-github-pages)
2. [Activation sur votre Compte](#2-activation-sur-votre-compte)
3. [Architecture du Portfolio](#3-architecture-du-portfolio)
4. [Déploiement des 4 Projets Phares](#4-déploiement-des-4-projets-phares)
5. [Personnalisation & Design](#5-personnalisation--design)
6. [Maintenance & Mise à Jour](#6-maintenance--mise-à-jour)
7. [Optimisation & Partage](#7-optimisation--partage)
8. [Troubleshooting](#8-troubleshooting)
9. [Checklist Déploiement](#9-checklist-déploiement)

---

## **1. Qu'est-ce que GitHub Pages ?**

### **Définition Simplifiée**
GitHub Pages est un **service d'hébergement web gratuit** fourni par GitHub qui transforme un dépôt Git en **site web statique** accessible publiquement.

### **Caractéristiques Clés**

| **Aspect** | **Description** | **Bénéfice pour vous** |
|-----------|-----------------|----------------------|
| **Gratuit** | Hébergement illimité | Pas de coût supplémentaire |
| **Automatisé** | Push sur GitHub = site mis à jour | Déploiement continu sans effort |
| **Domaine personnalisé** | `yourname.github.io` par défaut | Adresse professionnelle facile à retenir |
| **HTTPS sécurisé** | Certificat SSL gratuit | Confiance recruteur/visiteur |
| **Domaine custom possible** | Votre propre domaine | Brand professionnel |
| **Pas de base de données** | Contenu statique (HTML/CSS/JS) | Performance maximale |

### **Cas d'Usage Idéal pour Data Analysts**

✅ **Portfolio personnel** (projets, blogs, documentation)
✅ **Documentation technique** (README, guides, wikis)
✅ **Dashboards interactifs** (Plotly, D3.js)
✅ **Vitrine projet** (présentation professionnelle)

❌ **Applications avec backend** (ne pas utiliser si base de données nécessaire)
❌ **Contenu très dynamique** (non statique)

---

## **2. Activation sur votre Compte**

### **Étape 1 : Prérequis**

- ✅ Compte GitHub actif ([https://github.com/](https://github.com/))
- ✅ Dépôt public (nécessaire pour Pages gratuit)
- ✅ Aucun secret/données sensibles dans le repo

### **Étape 2 : Créer le Dépôt Portfolio**

**Option A : Si vous n'avez pas encore de repo portfolio**

```bash
# 1. Créer un dépôt nommé "MON-PORTFOLIO-DATA" (ou nom équivalent)
# Via GitHub UI : New Repository → Public → Initialize with README

# 2. Cloner localement
git clone https://github.com/YOUR-USERNAME/MON-PORTFOLIO-DATA.git
cd MON-PORTFOLIO-DATA

# 3. Ajouter votre contenu
# (fichiers, README, projets)

# 4. Push
git add .
git commit -m "Initial portfolio setup"
git push origin main
```

**Option B : Si le repo existe déjà** ✅ C'est votre cas

→ Continuez à l'**Étape 3**

### **Étape 3 : Activer GitHub Pages**

#### **Via Interface Web (Recommandé)**

1. Allez dans votre repo : `https://github.com/YOUR-USERNAME/MON-PORTFOLIO-DATA`
2. **Settings** (icône ⚙️ en haut à droite)
3. **Pages** (colonne gauche)
4. **Source** → Sélectionnez :
   - 📂 Branch: `main`
   - 📁 Folder: `/ (root)`
5. **Save**

![GitHub Pages Settings](../images/github_pages_settings.png)

#### **Résultat Attendu**

```
Your site is live at https://YOUR-USERNAME.github.io/MON-PORTFOLIO-DATA/
```

ou si vous configurez `ferialzamoun-afk.github.io` comme repo principal :

```
Your site is live at https://ferialzamoun-afk.github.io/
```

---

## **3. Architecture du Portfolio**

### **Structure Recommandée**

```
MON-PORTFOLIO-DATA/
├── README.md                          ← Landing page (auto-convertie en index.html)
├── index.md                           ← Optionnel : page d'accueil personnalisée
├── LICENSE                            ← MIT ou CC-BY-4.0
├── .gitignore
├── docs/                              ← Documentation (consultable depuis le site)
│   ├── 01_guide_github_pages.md       ← Ce guide
│   ├── 02_architecture.md
│   └── ...
├── projets/                           ← Fiches projets (liens vers repos)
│   ├── P13_portfolio_gouvernance_ia.md
│   ├── P12_detection_faux_billets.md
│   ├── P11_etude_marche_export.md
│   └── P9_lapage_librairie.md
├── images/                            ← Captures, bannières, icônes
│   ├── banniere.png
│   ├── projet_p13.png
│   └── ...
├── _config.yml                        ← Configuration Jekyll (optionnel)
└── streamlit_app/                     ← Données pour appli portable
    └── projets_data.md
```

### **Points Clés**

| **Dossier** | **Contenu** | **Visible ?** |
|------------|-----------|--------------|
| `README.md` | Page d'accueil du portfolio | ✅ Oui (auto-converti) |
| `docs/` | Documentation détaillée | ✅ Oui (/docs/) |
| `projets/` | Fiches par projet | ✅ Oui (/projets/) |
| `images/` | Bannières, captures | ✅ Oui (avec chemins relatifs) |
| `data/` | Fichiers Excel/CSV | ⚠️ Téléchargeables via GitHub |
| `.git/` | Historique Git | ❌ Non visible |

---

## **4. Déploiement des 4 Projets Phares**

### **Stratégie : Hub + Spokes**

```
ferialzamoun-afk.github.io/  ← HUB (Portfolio central)
├── P13/                     ← Lien vers P13 repo
├── P12/                     ← Lien vers P12 repo
├── P11/                     ← Lien vers P11 repo
└── P9/                      ← Lien vers P9 repo
```

### **Architecture Recommandée**

**OPTION A : Portfolio Central + Liens (Recommandée)**

```markdown
## 🌟 Projets Phares

### 1. P13 – Portfolio & Gouvernance IA
[📊 Voir le projet](https://github.com/ferialzamoun-afk/P13)
[🔗 Dépôt P13](https://github.com/ferialzamoun-afk/P13)

### 2. P12 – Détection de Faux Billets
[📊 Voir le projet](https://github.com/ferialzamoun-afk/P12)
[🔗 Dashboard Streamlit](https://streamlit-app-url.streamlit.app/)

### 3. P11 – Étude Marché
[📊 Voir le projet](https://github.com/ferialzamoun-afk/P11)
[📓 Notebooks](https://nbviewer.org/github/ferialzamoun-afk/P11)

### 4. P9 – Lapage Librairie
[📊 Voir le projet](https://github.com/ferialzamoun-afk/P9)
[🌐 Dashboard Streamlit](https://lapage-dashboard.streamlit.app/)
```

**OPTION B : Organisation via Dossiers** (avancé)

Créer des dossiers `projets/P13/`, `projets/P12/`, etc. avec contenu statique (HTML/Markdown).

---

### **Implémentation pour Vos 4 Projets**

#### **P13 – Portfolio & Gouvernance IA**

```markdown
# 📊 P13 – Portfolio & Gouvernance IA

**Contexte** : Certification RNCP 37837 – Démonstration du processus complet de fiabilisation données avec traçabilité IA.

**Résultats** :
- ✅ -68% de cellules notebook (148 → 50)
- ✅ 18 contrôles qualité validés
- ✅ 26 prompts IA tracés
- ✅ 16 documents de documentation

**Liens** :
- [📁 Dépôt Complet](https://github.com/ferialzamoun-afk/P13)
- [📓 Notebook Production](https://github.com/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/bottleneck_analyse_ameliore_final.ipynb)
- [🔗 Synthèse Finale](https://github.com/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/docs/06_synthese_finale_P13_partie_1.md)

**Compétences RNCP** : BC01, BC02, BC03, BC04, BC05 + Gouvernance IA
```

#### **P12 – Détection de Faux Billets**

```markdown
# 🎯 P12 – Détection de Faux Billets

**Contexte** : Modèle ML pour l'ONFM – Classification binaire avec recall 100%.

**Résultats** :
- ✅ Accuracy : 88%
- ✅ Recall (Faux Billets) : 100%
- ✅ F1-Score : 0.91
- ✅ API FastAPI déployée

**Liens** :
- [📁 Dépôt GitHub](https://github.com/ferialzamoun-afk/P12)
- [🌐 Documentation](https://github.com/ferialzamoun-afk/P12/blob/main/README.md)

**Compétences RNCP** : BC05 (Modélisation ML)
```

#### **P11 – Étude Marché**

```markdown
# 📈 P11 – Étude Marché – Priorisation Pays Export

**Contexte** : Analyse ACP + Clustering pour "La Poule Qui Chante" – Sélectionner 5 pays à l'export.

**Résultats** :
- ✅ 139 pays × 16 variables analysées
- ✅ ACP : 89.90% variance conservée (3 composantes)
- ✅ Silhouette Score : 0.60 (qualité bonne)
- ✅ Top 3 pays : Suisse, Dominique, Émirats Arabes Unis

**Liens** :
- [📁 Dépôt GitHub](https://github.com/ferialzamoun-afk/P11)
- [📓 Notebook 1 : Préparation](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb)
- [📓 Notebook 2 : Clustering](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations%20_112025.ipynb)

**Compétences RNCP** : BC01, BC02, BC03, BC04, BC05 (Data Science avancée)
```

#### **P9 – Lapage Librairie**

```markdown
# 📚 P9 – Lapage – Analyse Ventes Librairie

**Contexte** : Analyse data-driven pour optimiser performance commerciale et stratégie client.

**Résultats** :
- ✅ 480 000 € CA annuel
- ✅ 8 600 clients segmentés
- ✅ 3 pics saisonniers identifiés
- ✅ Dashboard Streamlit multi-pages

**Liens** :
- [📁 Dépôt GitHub](https://github.com/ferialzamoun-afk/P9)
- [🌐 Dashboard Streamlit](https://sznbna247tbtpj2hkhexqe.streamlit.app/)
- [📓 Notebooks](https://nbviewer.org/github/ferialzamoun-afk/P9/blob/main/notebooks/)

**Compétences RNCP** : BC01, BC02, BC03, BC04, BC05 (BI & Analytics)
```

---

## **5. Personnalisation & Design**

### **Option 1 : Utiliser le README.md (Minimal)**

**Avantage** : Aucune configuration, rapide
**Inconvénient** : Design basique

**Implémentation** :
1. Créer un `README.md` attrayant (voir template)
2. Ajouter des images/captures
3. Push → Pages actifs automatiquement

### **Option 2 : Utiliser Jekyll Theme (Recommandé)**

Jekyll est le générateur de sites statiques par défaut de GitHub Pages.

#### **Activer un Thème**

1. **Settings** → **Pages** → **Theme Chooser**
2. Sélectionnez un thème (ex: `Minimal`, `Cayman`, `Slate`)
3. Créez `_config.yml` :

```yaml
# GitHub Pages Jekyll Configuration
title: "Ferial Zamoun – Data Analyst Portfolio"
description: "Portfolio data science – P13, P12, P11, P9"
theme: jekyll-theme-cayman

# Metadata
author: Ferial Zamoun
email: ferial.zamoun@gmail.com
github_username: ferialzamoun-afk
linkedin_username: ferial-zamoun

# Build settings
markdown: kramdown
```

4. Créez `index.md` (page d'accueil personnalisée) :

```markdown
---
layout: default
title: Ferial Zamoun – Data Analyst Portfolio
---

# 📊 Portfolio Data Analyst

Bienvenue ! Vous trouverez ici mes 4 projets phares...

[Voir les projets](#projets)
```

#### **Ajouter une Navigation Personnalisée**

Créez `_layouts/default.html` (optionnel) :

```html
<!DOCTYPE html>
<html>
<head>
  <title>{{ site.title }}</title>
</head>
<body>
  <nav>
    <a href="/">Accueil</a>
    <a href="/projets/">Projets</a>
    <a href="/docs/">Docs</a>
    <a href="{{ site.github_url }}">GitHub</a>
  </nav>
  
  {{ content }}
</body>
</html>
```

### **Option 3 : Intégration Streamlit**

Pour un **portfolio interactif** :

```bash
# Créer une app Streamlit
streamlit run app.py

# Déployer via Streamlit Cloud
streamlit deploy
```

**App Structure** :
```python
import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

st.title("📊 Portfolio Ferial Zamoun")

tab1, tab2, tab3, tab4 = st.tabs(["P13", "P12", "P11", "P9"])

with tab1:
    st.header("P13 – Gouvernance IA")
    st.write("...")
    st.link_button("Voir le projet", "https://github.com/ferialzamoun-afk/P13")

# ... répéter pour P12, P11, P9
```

---

## **6. Maintenance & Mise à Jour**

### **Workflow Recommandé**

```bash
# 1. Ajouter nouveau contenu localement
echo "# Mon nouveau projet" >> projets/nouveau_projet.md

# 2. Commit avec message clair
git add projets/nouveau_projet.md
git commit -m "Add: Nouveau projet – Projet X"

# 3. Push (GitHub Pages se met à jour automatiquement)
git push origin main

# ✅ Changements visibles en ~5 secondes
```

### **Vérifier le Status de Déploiement**

1. Allez dans **Settings** → **Pages**
2. Cherchez **"Your site is live at..."**
3. Cliquez pour vérifier en direct

### **Actions Automatisées (CI/CD)**

Créer `.github/workflows/deploy.yml` :

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build site
        run: echo "Building portfolio..."
      - name: Deploy
        run: echo "Deploying to GitHub Pages..."
```

---

## **7. Optimisation & Partage**

### **SEO – Rendre votre Portfolio Trouvable**

#### **Ajouter Métadonnées**

```markdown
---
layout: default
title: "Ferial Zamoun – Data Analyst Portfolio"
description: "Portfolio data science avec P13 gouvernance IA, P12 ML, P11 clustering, P9 BI"
keywords: "data analyst, python, machine learning, data visualization, portfolio"
author: "Ferial Zamoun"
---
```

#### **Créer un `sitemap.xml`**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://ferialzamoun-afk.github.io</loc>
    <lastmod>2026-07-13</lastmod>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://ferialzamoun-afk.github.io/projets/P13/</loc>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://ferialzamoun-afk.github.io/projets/P12/</loc>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://ferialzamoun-afk.github.io/projets/P11/</loc>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://ferialzamoun-afk.github.io/projets/P9/</loc>
    <priority>0.9</priority>
  </url>
</urlset>
```

### **Partage & Distribution**

| **Plateforme** | **Lien à Partager** | **Exemple** |
|---------------|-------------------|-----------|
| **LinkedIn** | Portfolio URL | https://ferialzamoun-afk.github.io |
| **GitHub Profil** | Bio + pinned repos | Ajouter MON-PORTFOLIO-DATA aux repos épinglés |
| **Email/CV** | URL + QR code | "Mon portfolio : [lien]" |
| **Entretien Recruiter** | Écran partagé | Montrer en direct les 4 projets |

### **Créer un QR Code**

```bash
# Avec Python
pip install qrcode[pil]

python -c "
import qrcode
qr = qrcode.QRCode()
qr.add_data('https://ferialzamoun-afk.github.io')
qr.make()
qr.make_image().save('portfolio_qr.png')
"
```

---

## **8. Troubleshooting**

### **❌ "Your site is not published"**

**Causes** :
- ❌ Repo est privé
- ❌ Branch n'est pas `main` (ou `master`)
- ❌ Pas d'accès en Settings

**Solutions** :
```bash
# 1. Vérifier branche
git branch -a

# 2. Rendre repo public
# Settings → Danger Zone → Make Public

# 3. Forcer Settings dans Settings → Pages
```

### **❌ "404 File Not Found"**

**Causes** :
- ❌ Chemins relatifs incorrects
- ❌ Fichier non committé

**Solutions** :
```bash
# Vérifier fichier existe
ls projets/P13.md

# Vérifier commit
git status
git log --oneline

# Re-push si nécessaire
git add .
git commit -m "Fix: Add missing files"
git push origin main
```

### **❌ "Images ne s'affichent pas"**

**Causes** :
- ❌ Chemin absolu au lieu de relatif
- ❌ Fichier n'existe pas dans `/images/`

**Solutions** :

```markdown
# ❌ MAUVAIS
![alt](https://github.com/.../image.png)
![alt](/images/image.png)

# ✅ BON
![alt](images/image.png)
![alt](../images/image.png)  # Si dans sous-dossier
```

### **❌ "Theme ne s'applique pas"**

```yaml
# Vérifier _config.yml
theme: jekyll-theme-cayman
```

---

## **9. Checklist Déploiement**

### **Pré-Lancement**

- [ ] Repo **MON-PORTFOLIO-DATA** est public
- [ ] README.md est complet et attractif
- [ ] Images sont présentes dans `/images/`
- [ ] Tous les liens externes (GitHub, Streamlit) sont fonctionnels
- [ ] Pas de données sensibles/secrets dans le repo
- [ ] LICENSE file exists (MIT ou CC-BY-4.0)

### **Activation GitHub Pages**

- [ ] Settings → Pages → Source défini sur `main` (root)
- [ ] "Your site is live at..." message visible
- [ ] URL accessible : `https://YOUR-USERNAME.github.io/MON-PORTFOLIO-DATA/`

### **Contenu des 4 Projets**

- [ ] **P13** : Synthèse, liens, captures
- [ ] **P12** : ML metrics, API link, résultats
- [ ] **P11** : ACP results, clustering, recommendations
- [ ] **P9** : Streamlit dashboard, CA, clients

### **Navigation & UX**

- [ ] Accueil (README) accueillant et clair
- [ ] Liens internes fonctionnent (`/projets/`, `/docs/`)
- [ ] Tous les liens externes ouvrent dans nouvel onglet
- [ ] Mobile-responsive (tester sur téléphone)

### **Partage & Promotion**

- [ ] URL dans profil LinkedIn
- [ ] URL dans signature email
- [ ] QR code généré et sauvegardé
- [ ] GitHub repos P13, P12, P11, P9 épinglés

### **Post-Lancement**

- [ ] 1ère semaine : Vérifier stats (GitHub Pages analytics)
- [ ] Hebdomadaire : Mettre à jour avec nouveaux projets
- [ ] Monthly : Vérifier liens externes (ne deviennent pas 404)

---

## **Ressources Additionnelles**

| **Ressource** | **URL** | **Utilité** |
|-------------|--------|-----------|
| **GitHub Pages Doc** | https://pages.github.com/ | Officiel GitHub |
| **Jekyll Doc** | https://jekyllrb.com/ | Générateur sites statiques |
| **Markdown Guide** | https://www.markdownguide.org/ | Syntaxe Markdown |
| **HTML/CSS Basics** | https://www.w3schools.com/ | Références web |
| **Fonts Google** | https://fonts.google.com/ | Typos gratuites |
| **Icons Font Awesome** | https://fontawesome.com/ | Icônes |

---

## **Conclusion**

**GitHub Pages = Solution gratuite, automatisée, et professionnel pour valoriser votre portfolio.**

**Résumé du workflow** :

```bash
# 1 : Local (écrire contenu)
git add README.md projets/ images/
git commit -m "Update portfolio"

# 2 : Push (GitHub)
git push origin main

# 3 : Déploiement automatique ✅
# Visible en ~5 secondes à https://ferialzamoun-afk.github.io/
```

**Prochaines étapes** :

1. ✅ Activer GitHub Pages (Settings → Pages)
2. ✅ Ajouter les 4 fiches projets (`/projets/`)
3. ✅ Personnaliser thème Jekyll (optionnel)
4. ✅ Tester tous les liens
5. ✅ Partager sur LinkedIn & email

---

**Questions ?** Consultez la section [Troubleshooting](#8-troubleshooting) ou relisez la section correspondante.

**Bonne chance pour votre portfolio ! 🚀**
