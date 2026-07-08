# Ameliorations IA - P13 Partie 1

## Objectif

Documenter les ameliorations apportees au livrable P6 avec l'aide de l'IA, en distinguant clairement ce qui est propose par l'IA, ce qui est retenu humainement, ce qui est valide techniquement et ce qui reste a finaliser pour le livrable Bottleneck.

## Regle de documentation

Chaque amelioration IA doit préciser :

| Champ | Contenu attendu |
|---|---|
| Besoin | Probleme ou opportunite identifiee |
| Apport IA | Proposition, structuration, code ou reformulation aidee par IA |
| Decision humaine | Retenu, adapte, reporte ou rejete, avec justification |
| Validation | Test, execution, controle documentaire ou limite |
| Statut | En cours, realise, reporte |

## Limite transversale - Kernel et scripts Python

La creation ou la modification d'un script Python dans `src/` n'est pas toujours prise en compte automatiquement par le kernel du notebook.

Decision de travail : apres creation ou modification d'un script reutilisable, rejouer la cellule M03 du notebook ameliore, ou redemarrer puis rejouer le notebook dans l'ordre.

Cette limite est importante car une cellule peut echouer avec `ModuleNotFoundError` ou continuer a utiliser une ancienne version du script si le kernel n'a pas ete rejoue.

## Ameliorations documentees

| ID | Amelioration IA | Besoin | Apport IA | Decision humaine | Validation | Statut |
|---|---|---|---|---|---|---|
| IA-01 | Structuration des livrables P13 Partie 1 | Rendre la demarche de pilotage lisible | Proposition de documents courts : cahier des charges, veille, journal IA, plan projet, matrice | Retenu et adapte a la matrice P13 | Documents crees dans `docs/` | Realise |
| IA-02 | Amelioration progressive du notebook | Eviter un notebook illisible, construit par accumulation | Proposition d'une version separee et d'une migration par lots | Retenu : ameliorer par lots valides | `bottleneck_analyse_ameliore_final.ipynb` cree et valide JSON | En cours |
| IA-03 | Controle qualite reutilisable | Eviter un controle qualite enferme dans le notebook | Factorisation dans `src/quality_checks.py` | Retenu : rend le controle reutilisable hors notebook | Script teste, `quality_report` reproduit : 18 controles | Realise |
| IA-04 | Script Python de correction stock | Corriger les incoherences `stock_status` et les stocks negatifs de maniere tracee | Creation de `src/stock_cleaning.py` avec feature engineering et methode de sommation booleenne | Retenu et adapte : les stocks negatifs sont ramenes a 0 car ils representent des ruptures ou corrections de stock a investiguer, pas des quantites vendables | Script appele dans le notebook ameliore, cellule executee, 7 lignes M05 ajoutees au CSV metriques | En cours de finalisation |

## Detail IA-04 - Script Python de correction stock

### Besoin

Le controle qualite M04 a identifie :

- 2 stocks negatifs dans l'ERP ;
- 2 incoherences entre `stock_quantity` et `stock_status` ;
- un besoin de tracer la correction avant les rapprochements ERP/Web/Liaison.

### Feature engineering ajoute

Le script `src/stock_cleaning.py` ajoute des variables de controle :

| Feature | Role |
|---|---|
| `stock_status_expected` | Statut attendu selon `stock_quantity` |
| `is_negative_stock` | Identifie les stocks inferieurs a 0 |
| `has_stock_status_gap` | Identifie les ecarts entre statut reel et attendu |
| `needs_stock_correction` | Regroupe les lignes necessitant une correction |
| `stock_quantity_was_corrected` | Trace les quantites modifiees |
| `stock_status_was_corrected` | Trace les statuts modifies |
| `stock_was_corrected` | Trace toutes les lignes corrigees |

### Methode de sommation

Les controles utilisent la sommation booleenne :

```python
nombre_anomalies = int(condition_booleenne.sum())
```

Cette methode est retenue car elle est simple, lisible, reproductible et facilement explicable en soutenance.

### Decision humaine

Decision : retenir la correction automatique des stocks negatifs vers 0, mais la documenter comme une correction metier prudente.

Justification : un stock negatif ne represente pas une quantite vendable. Il indique plutot une rupture, une erreur de saisie ou un ajustement de stock a investiguer. Le passage a 0 permet de poursuivre l'analyse sans interpreter une quantite negative comme un stock reel.

### Validation actuelle

Test du script sur `P6_initial/data/erp.xlsx` :

| Controle | Resultat |
|---|---:|
| Incoherences stock_status | 2 |
| Stocks negatifs | 2 |
| Lignes a corriger | 4 |
| Stock_status modifies | 2 |
| Stock_quantity modifies | 2 |
| Stocks negatifs restants | 0 |
| Ecarts stock_status restants | 0 |

### Limite

Cette amelioration est implementee dans le notebook ameliore, et elle reste a valoriser avec une capture ou une sortie finale dans le dossier des preuves.

## A finaliser pour le livrable Bottleneck

| Action | Preuve attendue | Statut |
|---|---|---|
| Remplacer la cellule M05 par l'appel explicite au script `stock_cleaning.py` | Notebook ameliore execute | [x] |
| Reporter les metriques stock dans `metriques_p6_indicateurs.csv` | Lignes M05 stock ajoutees | [x] |
| Ajouter une capture ou sortie du rapport de correction stock | Capture ou sortie notebook | A faire |
| Mettre a jour la synthese finale | Section limites/recommandations completee | A faire |
