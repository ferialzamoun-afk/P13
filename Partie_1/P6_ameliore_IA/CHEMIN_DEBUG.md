# 🔧 Vérification des chemins - Notebook

**Date** : 2026-07-08  
**Status** : Chemins corrigés pour nouvelle structure

---

## ✅ Changements appliqués

### Cellules mises à jour

| Cellule | Change | Avant | Après |
|---|---|---|---|
| Cell 1 (M00 - Prérequis) | Chemins données | Cherche `P6_initial/data/` | Cherche `P6_ameliore_IA/data/` + fallback `../data/` |
| Cell 3 (M03 - Chargement) | Chemins données | Cherche `P6_initial/data/` | Cherche `P6_ameliore_IA/data/` + fallback `../data/` |

**Logique de recherche** (dans cet ordre) :
1. `Partie 1/P6_ameliore_IA/data/` (depuis racine projet)
2. `P6_ameliore_IA/data/` (chemin alternatif)
3. `../data/` (chemin relatif depuis notebook)

---

## 🔍 Vérification requise

### 1. Données présentes localement ?

```bash
# Vérifier les fichiers Excel
ls -la "Partie 1/P6_ameliore_IA/data/"
```

**Attendu** :
- ✅ `erp.xlsx` (présent)
- ✅ `web.xlsx` (présent)
- ✅ `liaison.xlsx` (présent)

### 2. .gitignore correct ?

```bash
cat .gitignore | grep -E "data|scripts|src"
```

**Attendu** :
```
Partie\ 1/P6_ameliore_IA/data/
Partie\ 1/P6_ameliore_IA/scripts/
Partie\ 1/P6_ameliore_IA/src/
```

### 3. Notebook exécutable ?

Pour tester :
```bash
cd "Partie 1/P6_ameliore_IA/notebooks"
python -m jupyter nbconvert bottleneck_analyse_ameliore_final.ipynb --to notebook --execute --allow-errors
```

Ou simplement exécuter Cell 1 (M00) dans VSCode pour vérifier que les fichiers sont trouvés.

---

## ⚙️ Si fichiers manquent

### Option 1 : Restaurer depuis git (commit précédent)

Les fichiers étaient dans commit `7d80de5` et `f0da909` (avant deletion).

```bash
# Voir ce qui a été supprimé
git show HEAD:Partie\ 1/P6_initial/data/ 

# Restaurer (si possible)
git checkout HEAD~2 -- "Partie 1/P6_initial/data/"
```

### Option 2 : Recréer manuellement

Importer depuis source originale ou depuis backups.

---

## 📊 Statut des chemins

| Ressource | Chemin | Git? | Accès |
|---|---|---|---|
| Notebook | `notebooks/bottleneck_analyse_ameliore_final.ipynb` | ✅ Trackée | ✅ Accès direct |
| Données ERP | `data/erp.xlsx` | ❌ Ignorée | ⚠️ Local only |
| Données Web | `data/web.xlsx` | ❌ Ignorée | ⚠️ Local only |
| Données Liaison | `data/liaison.xlsx` | ❌ Ignorée | ⚠️ Local only |
| Scripts | `src/*.py` | ❌ Ignorée | ⚠️ Local only |
| Sorties | `output/` | ✅ Trackée | ✅ Accès direct |
| Captures | `output/captures/` | ✅ Trackée | ✅ Accès direct |
| Dataviz | `output/dataviz/` | ✅ Trackée | ✅ Accès direct |

---

## 🎯 Prochaines étapes

- [ ] Vérifier que `data/` contient les 3 fichiers Excel
- [ ] Tester Cell 1 du notebook (M00 - Prérequis)
- [ ] Vérifier que Cell 3 (M03 - Chargement) trouve les données
- [ ] Exécuter le notebook complet si Cell 3 OK

---

## 📝 Notes

- Chemins relatifs utilisés quand possible
- Détection automatique du répertoire projet (robustesse)
- Pas de chemins nominatifs (RGPD)
- Fallback à `../data/` si exécution depuis `notebooks/`
