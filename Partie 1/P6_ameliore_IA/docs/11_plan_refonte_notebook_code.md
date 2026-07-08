# Plan de refonte du notebook a partir des cellules de code

## Constat

La trame actuelle du notebook est difficile a lire car elle melange :

- des consignes historiques de formation ;
- des blocs de code exploratoires ;
- des syntheses intermediaires ;
- des workflows de verification ;
- des recapitulatifs longs ;
- des sorties et exports disperses.

Une simple renumerotation des titres ne suffit pas. La refonte doit repartir des cellules de code et reconstruire une narration data claire.

Inventaire source : `P6_ameliore_IA/data/notebook_code_inventory.csv`.

## Decision humaine recommandee

Retenir une refonte structurelle progressive : creer une version narrative plus propre du notebook, basee sur les cellules de code utiles, sans tenter de renumeroter toutes les anciennes syntheses.

Decision : **adapter et restructurer**, pas reecrire toute l'analyse depuis zero.

Justification :

- le code contient deja les controles, analyses, KPI et visualisations utiles ;
- le probleme principal est l'ordre et la narration ;
- supprimer ou reecrire trop vite ferait perdre des preuves ;
- une version cible par blocs est plus facile a valider.

## Architecture cible simplifiee

| Section cible | Role | Contenu issu des cellules de code |
|---|---|---|
| 0. Mission | Cadrer le livrable | Capture mission, consigne reformulee, public cible |
| 1. Objectif metier et methode | Expliquer la logique | Objectif Bottleneck, sources, methodologie courte |
| 2. Chargement et configuration | Rendre le notebook reproductible | Imports, chemins, chargement ERP/Web/Liaison |
| 3. Controle qualite des sources | Fiabiliser avant analyse | Volumetrie, colonnes, valeurs manquantes, doublons, cles |
| 4. Nettoyage et corrections | Documenter les corrections | Stock status, stocks negatifs, prix negatifs, colonnes inutiles |
| 5. Rapprochement ERP/Web/Liaison | Construire le dataset final | Jointures, non-matchs, `df_final`, disponibilite web |
| 6. EDA et analyses metier | Comprendre les variables | Prix, ventes, stocks, marges, categories, distributions |
| 7. KPI, anomalies et dataviz | Restituer les resultats | CA, Pareto, outliers, correlations, rotation, IDP/IPR |
| 8. Recommandations et limites | Conclure pour les metiers | Recommandations commerciales/logistiques, limites, prochaines actions |

## Mapping des cellules de code vers les sections cibles

| Groupe de cellules | Role actuel | Section cible | Action de refonte |
|---|---|---|---|
| 12 a 16 | Imports, options, chargement des donnees | 2. Chargement et configuration | Conserver et simplifier |
| 19 | `quality_report` transversal | 3. Controle qualite des sources | Conserver comme bloc central |
| 22 a 29 | Dimensions ERP, colonnes, doublons, stock status | 3. Controle qualite des sources | Regrouper et reduire les impressions redondantes |
| 31 a 33 | Identification et correction des incoherences stock | 4. Nettoyage et corrections | Conserver, documenter decision humaine |
| 36 a 44 | Analyses ERP : stock, prix, achat, marge | 6. EDA et analyses metier | Regrouper sous EDA univariee |
| 47 a 56 | Analyse Web, SKU, lignes sans code article | 3 puis 4 | Garder les controles utiles, reduire les explications longues |
| 58 a 70 | Analyse liaison et `id_web` manquants | 3 puis 5 | Regrouper dans controle qualite + rapprochement |
| 73 a 90 | Fusions ERP/Liaison/Web et `df_final` | 5. Rapprochement ERP/Web/Liaison | Conserver comme bloc essentiel |
| 94 a 106 | Outliers prix : boxplot, z-score, IQR | 7. KPI, anomalies et dataviz | Conserver, choisir une methode principale et documenter l'autre en controle |
| 109 a 126 | CA, Pareto, visualisations | 7. KPI, anomalies et dataviz | Conserver les graphes les plus utiles |
| 128 a 136 | Stocks, marges, taux de marge | 6 puis 7 | Regrouper avec EDA et KPI marge |
| 138 a 150 | Correlations, rotation, IDP/IPR, interpretation logistique | 7 puis 8 | Garder comme storytelling metier final |
| 152 a 156 | Rapport final et exports | 8. Recommandations et limites | A rationaliser vers `output/` |

## Ce qu'il faut supprimer ou deplacer hors notebook

| Element | Action | Raison |
|---|---|---|
| Consignes pedagogiques Jupyter | Supprimer | Ne sert plus dans un livrable portfolio |
| Longues syntheses redondantes | Deplacer vers synthese finale ou condenser | Surcharge la lecture |
| Workflows tres detailles | Transformer en annexes courtes ou tableaux | Trop lourd pour le notebook principal |
| Multiples impressions de colonnes | Regrouper dans un tableau de controle | Redondance visuelle |
| Exports disperses | Centraliser dans `output/` | Reproductibilite |
| Graphiques non retenus | Garder dans brouillon ou annexe | Evite un notebook trop long |

## Version cible du notebook

### 0. Mission

- Capture mission.
- Consigne reformulee.
- Public cible : direction, commercial, logistique, evaluateur.

### 1. Objectif metier et methode

- Objectif metier Bottleneck.
- Sources : ERP, Web, Liaison.
- Methode en 4 lignes : controle, nettoyage, rapprochement, analyse.

### 2. Chargement et configuration

- Imports.
- Chemins robustes.
- Chargement des trois fichiers.
- Affichage des dimensions.

### 3. Controle qualite des sources

- `quality_report` transversal.
- Unicite des cles.
- Valeurs manquantes.
- Doublons.
- Premiers risques data.

### 4. Nettoyage et corrections

- Corrections `stock_status`.
- Stocks negatifs.
- Prix negatifs.
- Colonnes conservees/supprimees.
- Trace des decisions humaines.

### 5. Rapprochement ERP/Web/Liaison

- Fusion ERP/Liaison.
- Analyse des lignes non rapprochees.
- Fusion Web.
- Creation de `df_final`.
- Marquage `web_disponible`.

### 6. EDA et analyses metier

- Prix et prix d'achat.
- Stocks.
- Ventes.
- Marges.
- Categories ou types produit.

### 7. KPI, anomalies et dataviz

- CA total et CA par produit.
- Pareto du CA.
- Outliers prix.
- Correlations utiles.
- Rotation des stocks.
- IDP/IPR.
- 3 a 5 visualisations finales maximum.

### 8. Recommandations et limites

- Recommandations commerciales.
- Recommandations logistiques.
- Limites data.
- Limites IA.
- Prochaines actions.

## Strategie de migration progressive

| Etape | Action | Validation |
|---|---|---|
| M01 | Creer une copie de securite du notebook ameliore actuel | Fichier backup cree |
| M02 | Creer une nouvelle trame Markdown propre dans le notebook | JSON valide |
| M03 | Deplacer ou regrouper les cellules de chargement | Execution chargement OK |
| M04 | Regrouper les controles qualite | `quality_report` affiche |
| M05 | Regrouper les corrections data | Corrections documentees |
| M06 | Regrouper les fusions | `df_final` cree |
| M07 | Selectionner les analyses EDA utiles | Tableaux coherents |
| M08 | Selectionner les KPI et visualisations finales | Captures candidates |
| M09 | Supprimer ou archiver les syntheses redondantes | Notebook plus court |
| M10 | Executer le notebook dans l'ordre | Pas d'erreur bloquante |

## Recommandation de prudence

Ne pas appliquer cette refonte en une seule grosse modification. Le notebook est long et contient des sorties utiles. Il faut proceder par lots avec validation apres chaque lot.

Priorite immediate :

1. Identifier l'erreur stockee R03.
2. Corriger ou documenter l'erreur R04.
3. Creer la section Mission R05.
4. Ensuite seulement, envisager la migration structurelle M01-M10.

## Avancement de la migration

| Etape | Statut | Preuve |
|---|---|---|
| M01 - Copie de securite | [x] | Backup horodate dans `P6_ameliore_IA/backups/` |
| M02 - Trame refactoree | [x] | `P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb` cree et JSON valide |
| M03 - Migration chargement | [x] | Cellule chargement executee dans `bottleneck_analyse_ameliore_final.ipynb` : sortie RGPD-friendly `P6_initial/data`, ERP (825, 6), Web (1513, 29), Liaison (825, 2) |
| M04 - Migration controle qualite | [x] | `quality_report` execute : 11 OK, 4 a verifier, 2 a documenter, 1 a corriger ; logique factorisee dans `src/quality_checks.py` ; CSV metriques alimente |
| M05 - Nettoyage stock ERP | [x] | Cellule executee : 2 `stock_status` corriges, 2 stocks negatifs ramenes a 0, 0 ecart restant |
| M05b - Data Contracts (GE) | [x] | **NOUVEAU** - 7 expectations formels (E1-E4 ERP, W1-W2 Web, L1 Liaison) ; 4/7 passes ; portfolio + piste moyen terme pipeline |
| M06 - Rapprochement ERP/Web/Liaison | [x] | `df_final` cree : 825 lignes, 714 avec correspondance web, 111 sans correspondance web active ; CSV metriques alimente avec 11 lignes M06 |
| M07 - EDA et analyses metier | [x] | EDA executee : 825 produits, CA total 143680.1 EUR, 689 produits avec ventes, 92 ruptures/stock nul, 7 marges negatives ; CSV metriques alimente avec 10 lignes M07 |
| M08 - KPI et visualisations finales | [x] | Cellule M08 executee : KPI, top 10 CA, Pareto 80% au rang 435, anomalies, KPI categories, boxplot prix et correlations ; 5 fichiers HTML exportes dans `output/dataviz/` |
| M09 a M10 | [ ] | A faire apres validation dataviz |
