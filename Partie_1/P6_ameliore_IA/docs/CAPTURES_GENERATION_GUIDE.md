# Guide : Générer les captures portfolio - P13 Partie 1

**Objectif** : Créer 6-8 screenshots pour prouver le livrable et enrichir le portfolio.

---

## 📸 Captures à générer

| # | Capture | Source | Dimensions | Destination |
|---|---|---|---|---|
| 1 | **Mission & Contexte** | Cell 1 (Mission) | 1024×600 | `captures/01_mission_p6_bottleneck.png` |
| 2 | **Structure notebook** | VS Code outline (65 cellules courantes ; capture historique nommee 49cells) | 1024×800 | `captures/02_notebook_structure_49cells.png` |
| 3 | **Checkpoint Phase I** | Cell M00 output | 1024×600 | `captures/03_quality_report_18controls.png` |
| 4 | **Avant/Après metrics** | 06_synthese tableau avant/après | 1024×600 | `captures/04_before_after_metrics.png` |
| 5 | **KPI Dashboard Phase II** | Cells Phase II output (CA, Pareto) | 1024×600 | `captures/05_kpi_dashboard_phase2.png` |
| 6 | **Kanban GitHub Projects** | Browser screenshot | 1024×600 | `captures/06_kanban_github_projects.png` |
| 7 | **Dataviz Sample** | output/dataviz/correlations_quantitatives.html (screenshot) | 1024×600 | `captures/07_dataviz_sample_correlations.png` |
| 8 | **IA Journal Coverage** | 03_journal_ia "Comptage des prompts" table | 1024×600 | `captures/08_ia_journal_26prompts.png` |

---

## 🎬 Procédure pour chaque capture

### Capture 1 : Mission & Contexte
```
1. VS Code : Ouvrir notebook
2. Cell 1 (Mission) → Sélectionner le markdown
3. Screenshot : Cmd+Shift+P → "Screenshot" (VS Code) 
4. Sauver dans captures/01_mission_p6_bottleneck.png
```

### Capture 2 : Structure notebook (Outline)
```
1. VS Code : Ouvrir notebook
2. Vue → Explorer → Outline (panneau gauche)
3. Voir les 65 cellules listées dans la version enrichie BC05
4. Screenshot du panneau outline
5. Sauver dans captures/02_notebook_structure_49cells.png
```

### Capture 3 : Quality Report Phase I
```
1. VS Code : Exécuter Cell M00 (Prérequis)
2. Voir output ✅ STRUCTURE OK
3. Screenshot de l'output
4. Sauver dans captures/03_quality_report_18controls.png
```

### Capture 4 : Avant/Après Metrics
```
1. Ouvrir docs/06_synthese_finale_P13_partie_1.md
2. Section "Comparaison avant/après" → Tableau
3. Screenshot du tableau
4. Sauver dans captures/04_before_after_metrics.png
```

### Capture 5 : KPI Dashboard
```
1. Ouvrir docs/06_synthese_finale_P13_partie_1.md
2. Section "Phase II - Résultats" (CA, Pareto, anomalies)
3. Screenshot des KPI résumés
4. Sauver dans captures/05_kpi_dashboard_phase2.png
```

### Capture 6 : Kanban GitHub
```
1. Ouvrir https://github.com/<repo>/projects
2. Voir le Kanban avec colonnes (Backlog, In Progress, Done)
3. Screenshot
4. Sauver dans captures/06_kanban_github_projects.png
```

### Capture 7 : Dataviz Sample
```
1. Fichier local : output/dataviz/correlations_quantitatives.html
2. Ouvrir dans navigateur
3. Screenshot de la heatmap corrélations
4. Sauver dans captures/07_dataviz_sample_correlations.png
```

### Capture 8 : IA Journal Coverage
```
1. Ouvrir docs/03_journal_ia_P13_partie_1.md
2. Section "Comptage des prompts par étape clé" (tableau)
3. Voir 15 lignes consolidées = 26 prompts
4. Screenshot
5. Sauver dans captures/08_ia_journal_26prompts.png
```

---

## 📁 Structure destination

Créer dossier `output/captures/` s'il n'existe pas :
```bash
mkdir -p "Partie 1/P6_ameliore_IA/output/captures"
```

---

## ✅ Checklist après captures

- [ ] Tous les 8 fichiers PNG générés ✅
- [ ] Noms de fichiers cohérents (01_*, 02_*, etc.)
- [ ] Dimensions ~1024×600 pour cohérence
- [ ] Qualité visible (pas flou)
- [ ] Fichiers ajoutés à git

---

## 🚀 Utilisation dans README & Portfolio

Après génération, ajouter section "Screenshots" dans README.md :

```markdown
## 📷 Screenshots

| Capture | Contexte |
|---|---|
| ![01](output/captures/01_mission_p6_bottleneck.png) | Context Bottleneck |
| ![02](output/captures/02_notebook_structure_49cells.png) | Notebook overview |
| ![03](output/captures/03_quality_report_18controls.png) | Quality validation |
| ... |
```

---

## 💡 Alternative : Génération semi-automatique

Si captures manuelles compliquées, utiliser `selenium` ou `playwright` :

```python
# capture_generation.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Capture 7 : Dataviz
    page.goto("file:///" + os.path.abspath("output/dataviz/correlations_quantitatives.html"))
    page.screenshot(path="output/captures/07_dataviz_sample_correlations.png")
    
    browser.close()
```

Mais pour P13, captures manuelles suffisent (portfolio evaluation).

---

## 📋 Timeline recommandée

1. **Instant T0** : Générer captures 1-5 (VS Code + docs) → 10 min
2. **T0+15 min** : Capture 6 (GitHub Projects) → 5 min
3. **T0+20 min** : Capture 7 (dataviz HTML) → 5 min
4. **T0+25 min** : Capture 8 (Journal IA) → 5 min
5. **T0+30 min** : Vérifier qualité + git add + commit

**Total** : ~30 minutes pour 8 captures professionnelles

---

## ✅ Validation

Après génération :
```bash
ls -la output/captures/
# Devrait montrer : 01_*.png 02_*.png ... 08_*.png

# Vérifier tailles (MB)
du -h output/captures/
```

Attendu : ~2-5 MB au total (images légères)

---

**Prochaine étape** : Exécuter ce guide et ajouter captures à git avant publication.
