# Checklist de publication GitHub - P13 Partie 1

**Objectif** : Valider que le dépôt Bottleneck est prêt pour publication publique avec documentation P13 complète.  
**Date** : 2026-07-08  
**Statut** : À valider avant merge vers main / publication GitHub public

---

## 📋 Checklist technique - Notebook & Code

### Notebook principal : `bottleneck_analyse_ameliore_final.ipynb`
- [x] Renommé correctement (final, pas refactored)
- [x] **65 cellules** (28 code, 37 markdown) dans la version enrichie BC05
  - [x] Méthodologie & Traçabilité des choix - ✅ Exécuté
  - [x] BC05 : IF, SHAP, matrice stricte, K-Means, kNN et synchronisation dataviz - ✅ Exécuté
- [x] Exécution complète VALIDÉE (~1 min 30 version enrichie)
  - [x] Phase I : Chargement + Contrôles qualité (18 points) ✅
  - [x] Phase II : Rapprochement ERP/Web/Liaison (714 matches) ✅
  - [x] Phase III : EDA + KPI (CA 143.7k EUR, 689 produits vendus) ✅
  - [x] Phase IV : Audit final + Checkpoint ✅
- [x] Tous les chemins relatifs valides (`../../../P6_initial/data/`)
- [x] Pas de credentials/secrets embarqués
- [x] **Cell 2bis justifie** : Pandas vs GE vs Soda (comparaison P13)
- [x] **Cell 46bis satisfait** les 10 critères mission P13 (tableau final)

### Python Scripts (src/) - 5 modules
- [x] `quality_checks.py` : 18 contrôles documentés + tracés
- [x] `stock_cleaning.py` : Feature engineering (2 stocks corrigés)
- [x] `data_merging.py` : ERP/Web/Liaison rapprochement (714 matches validés)
- [x] `eda_analysis.py` : EDA compact (10 métriques)
- [x] `kpi_analysis.py` : KPI + anomalies (6 KPI + 3 anomalies types)
- [x] Tous les imports utiles (pas dead code)
- [x] Code commenté et traçable

---

## 📋 Checklist documentation - 8 fichiers requis pour P13

| 8 | `04_plan_projet_P13_partie_1.md` | Backlog (12 tasks), Kanban, planning J1-J4 [x], registre risques (8 risques) | [x] |
| 9 | `05_matrice_indicateurs_P13_partie_1.md` | 8 sections évaluation (veille, besoin, CDC, orga, doc/IA/repro) | [x] |
| 10 | `06_synthese_finale_P13_partie_1.md` | Avant/après (4 axes), 3-horizon roadmap, 15-point checklist, conclusions | [x] |
| 11 | `07_checklist_publication_github.md` | **Ce fichier** - validation publication + 10 critères mission | [x] |
| 12 | `13_great_expectations_strategy.md` | Stratégie GE pragmatique, 3 étapes, portfolio value | [x] |

---

## 📋 Checklist mission P13 - Les 10 critères

### Mission requiert que le livrable montre :

| # | Critère mission | Où documenté ? | Status |
|---|---|---|---|
| 1 | **Améliorer livrable existant** | 06_synthese (avant/après), notebook cell 46bis (metriques), execution validée | [x] |
| 2 | **IA critique & documentée** | 03_journal_ia (26 prompts), notebook cell 2bis (justifications), 06_synthese | [x] |
| 3 | **Tester plusieurs options** | 02_veille (5 solutions), notebook cell 2bis (alternatives Pandas/GE/Soda) | [x] |
| 4 | **Comparer selon critères EXPLICITES** | 02_veille (tableau 6 critères : qualité, robustesse, temps, repro, sécurité, conformité) | [x] |
| 5 | **Justifier les choix** | Cell 2bis (méthodologie), 03_journal_ia (decisions), 02_veille (rationale) | [x] |
| 6 | **Identifier besoins métier + contraintes** | 01_cahier_des_charges (5 contraintes listées), cell 2bis (4 appliquées) | [x] |
| 7 | **Formaliser cahier des charges** | 01_cahier_des_charges_P13_partie_1.md (complet, [x] status) | [x] |
| 8 | **Organiser projet data** | 04_plan_projet_P13_partie_1.md (backlog 12 tasks, kanban, planning) | [x] |
| 9 | **Outils de gestion de projet** | GitHub Projects (Kanban) + captures dans output/captures/ ✅ | [x] |
| 10 | **Intégrer différentes contraintes** | 01_cahier_des_charges (5 types), cell 2bis (4 appliquées : délai, RGPD, budget, sobriété) | [x] |

---

## 📁 Checklist fichiers & sorties

### Data & Structure
- [x] `P6_initial/data/` : erp.xlsx, web.xlsx, liaison.xlsx présents
- [x] `output/dataviz/` : **13 graphiques Phase II + 12 visuels BC05** générés (CA, Pareto, anomalies, stocks, corrélations, IF, SHAP, K-Means, kNN)
- [x] `output/captures/` : **9 screenshots portfolio créés et validés** ✅
  - [x] `01_mission_p6_bottleneck.png` (context slide)
  - [x] `02_notebook_structure_49cells.png` (capture historique ; notebook courant : 65 cellules)
  - [x] `03_quality_report_18controls.png` (Phase I validation)
  - [x] `04_before_after_metrics.png` (68% cells, 76% time improvement)
  - [x] `05_kpi_dashboard_phase2.png` (CA 143k€, Pareto, anomalies)
  - [x] `06_kanban_github_projects.png` (Kanban 12 tasks final)
  - [x] `07_dataviz_sample_correlations.png` (2 graphiques Plotly examples)
  - [x] `08_ia_journal_26prompts.png` (IA traceability documentation)
  - [x] `github_project_kanban_en_cours.png` (Project management proof)
  - [ ] `08_ia_journal_26prompts.png` (journal IA coverage snapshot)

### Documentation référencées OK
- [x] Tous les liens `docs/` dans notebook pointent ✅
- [x] Tous les chemins `../../../P6_initial/data/` résolvent ✅
- [x] Filenames mises à jour (bottleneck_analyse_ameliore_final) ✅

---

## 🔒 Checklist sécurité & RGPD

- [x] **Pas de données utilisateur nominatives** dans chemins/configs
- [x] **Pas de credentials** (API keys, tokens, mots de passe)
- [x] **Pas de données métier sensibles** (contacts, emails, infos personnelles)
- [x] **Chemins relatifs** validés (pas d'absolus avec noms d'utilisateurs Windows)
- [ ] **Fichiers temporaires** supprimés (`*.tmp`, `__pycache__`, `.ipynb_checkpoints`, backups/)
- [x] **Git config** : `.gitignore` incluant `backups/`, `.venv/`, `__pycache__`, checkpoints et exports temporaires
- [x] **Workflow GitHub Aikido** ajouté : `.github/workflows/aikido.yml`
- [ ] **Secret GitHub** `AIKIDO_CLIENT_API_KEY` ajouté dans le repo pour activer le scan
- [ ] **Premier scan Aikido** exécuté et preuve/capture archivée

### Statut Aikido / security scanning

- **Workflow prêt** : oui, au niveau racine du repo P13.
- **Déclencheurs** : `push` sur `main`, `pull_request` sur `main`, lancement manuel, scan planifié hebdomadaire.
- **Couverture prévue** : SAST, IaC, secrets scanning, dependency scanning.
- **Blocage restant** : ajout manuel du secret GitHub `AIKIDO_CLIENT_API_KEY` dans les settings du dépôt.

---

## 🧹 Checklist nettoyage dépôt

### À garder (MVP publication)
- [x] `README.md` (racine)
- [x] `requirements.txt`
- [x] `Partie 1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb` (SEUL)
- [x] `Partie 1/P6_ameliore_IA/src/` (5 scripts .py)
- [x] `Partie 1/P6_ameliore_IA/docs/` (8 docs .md)
- [x] `Partie 1/P6_ameliore_IA/output/dataviz/` (13 HTML)
- [x] `Partie 1/P6_ameliore_IA/output/captures/` (6-8 PNG) **À créer**
- [x] `Partie 1/P6_initial/data/` (3 xlsx sources)

### À supprimer / archiver
- [ ] `Partie 1/P6_ameliore_IA/backups/` (archiver hors repo ou supprimer)
- [ ] `Partie 1/P6_ameliore_IA/notebooks/bottleneck_analyse_refactoree.ipynb` (ancien, supprimer)
- [ ] `Partie 1/P6_ameliore_IA/output/*.csv` (temporaires, supprimer)
- [ ] Tous `.ipynb_checkpoints/` et `__pycache__/`
- [ ] `Partie 2/` (hors scope P13 Partie 1 - archiver séparément)

### À créer avant publication
- [x] `.gitignore` (backups/, .venv/, __pycache__, *.pyc, checkpoints, exports temporaires)
- [ ] `LICENSE` (MIT ou CC-BY-4.0)
- [ ] `README.md` version publique (réécriture complète)
- [ ] OPTIONAL : `CONTRIBUTING.md`

---

## 📝 Checklist README.md - Version publique

À créer : **README.md** clair pour recruteur/public

| Section | Contenu attendu | Status |
|---|---|---|
| **Titre** | "Optimisation de la gestion des données - Bottleneck Wine Shop" | [ ] |
| **Contexte** | Qui = PME Bottleneck, Quoi = ERP/Web data, Pourquoi = analyse CODIR | [ ] |
| **Résultats clés** | CA 143k€, Pareto 80% = 435 produits, 3 anomalies détectées, 13 dataviz Phase II + 12 visuels BC05 | [ ] |
| **Améliorations** | P6 initial: 148 cells → améliore: 65 cells (-56%) avec enrichissement BC05, temps ~1min30 | [ ] |
| **Structure dépôt** | Tree clair (notebooks/, docs/, src/, data/, output/) | [ ] |
| **Quickstart** | Python 3.12.2 → pip install -r requirements.txt → jupyter notebook | [ ] |
| **Méthodologie** | Pandas + 18 contrôles + Data Contracts (voir docs/02_veille) | [ ] |
| **Documentation** | Liens vers docs/ (CDC, journal IA, plan projet, synthèse) | [ ] |
| **IA critique** | 26 prompts tracés, décisions humaines (voir docs/03_journal_ia) | [ ] |
| **Reproductibilité** | Chemins relatifs, prérequis listés, données fournies | [ ] |
| **Limites** | 1 mois données, corrélations ≠ causalité, stocks anomalies (voir cell audit) | [ ] |
| **Portfolio** | Compétences démontrées : data prep, quality, reproducibility, IA governance | [ ] |
| **License** | MIT ou CC-BY-4.0 clairement indiquée | [ ] |

---

## ✅ Points de validation finale

### Exécution technique
- [ ] Notebook s'exécute de A à Z sans erreur
- [ ] Tous checkpoints (M00, Phase I, Phase II, Final) ✅
- [ ] Temps < 2 minutes
- [ ] 13 graphiques Phase II + 12 visuels BC05 générés dans output/dataviz/
- [ ] Pas de warnings importants

### Cohérence mission P13
- [ ] **Tous les 10 critères** mission documentés & traçables (tableau cell 46bis valide)
- [ ] **Traçabilité IA** complète (26 prompts → 13 essais → journal IA)
- [ ] **Choix justifiés** (Pandas vs GE vs Soda → cell 2bis + veille)
- [ ] **Limitations documentées** (cell audit + synthèse)
- [ ] **Contraintes intégrées** (4 dans cell 2bis, 5 dans CDC)

### Prêt GitHub
- [ ] Pas de chemins nominatifs
- [ ] Pas de credentials/secrets
- [ ] Pas de données sensibles
- [ ] README public rédigé et clair
- [ ] Captures portfolio 6-8 prêtes
- [ ] `.gitignore` créé
- [ ] Dépôt < 50 MB (sans backups)

---

## 🚀 Processus de publication

**Étape 1 (maintenant)** : Validation complète checklist
- [ ] Cocher toutes les cases [ ]
- [ ] Générer 6-8 captures

**Étape 2** : Nettoyage dépôt
- [ ] Supprimer notebooks ancien + backups
- [ ] Créer .gitignore
- [ ] Vérifier pas de secrets
- [ ] Ajouter `AIKIDO_CLIENT_API_KEY` dans GitHub Secrets

**Étape 3** : README & docs finales
- [ ] Rédiger README public
- [ ] Ajouter LICENSE
- [ ] Vérifier liens cohérents

**Étape 3bis** : Sécurité
- [x] Ajouter le workflow `.github/workflows/aikido.yml`
- [ ] Lancer un premier scan Aikido avec secret configuré
- [ ] Archiver une capture ou une note de validation sécurité

**Étape 4** : Tests finaux
- [ ] Clone repo frais
- [ ] Notebook s'exécute ✅
- [ ] Chemins OK ✅

**Étape 5** : Publication
- [ ] Push vers branche `publication-p13-partie-1`
- [ ] Merge vers main
- [ ] Basculer repo en public
- [ ] Lier dans portfolio

---

## 📊 Signature de validation

| Point | Responsable | Date | Statut |
|---|---|---|---|
| Validation technique (notebook, code, data) | [À remplir] | [ ] | [ ] |
| Validation mission (10 critères P13) | [À remplir] | [ ] | [ ] |
| Validation sécurité (RGPD, pas secrets) | [À remplir] | [ ] | [ ] |
| Validation README & captures | [À remplir] | [ ] | [ ] |
| **PRÊT POUR PUBLICATION PUBLIQUE** | [À remplir] | [ ] | **[ ] OUI** |
