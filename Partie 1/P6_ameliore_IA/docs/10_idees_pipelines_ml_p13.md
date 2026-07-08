# Idees de pipelines data/ML - P13

## Objectif

Explorer une piste de POC data/ML a partir du fichier `P6_ameliore_IA/data/metriques_p6_indicateurs.csv` pour analyser l'avancement du projet et anticiper les derives potentielles en couts, delais, budget ou charge.

Cette piste n'est pas un livrable obligatoire du P13. Elle peut servir d'idee differenciante pour montrer une capacite a transformer une matrice de pilotage en base d'analyse predictive ou prescriptive.

## Question metier

Comment exploiter les indicateurs de suivi du P13 pour estimer le risque de derive d'un projet data et prioriser les actions correctives ?

Exemples de risques a anticiper :

- retard sur les jalons ;
- surcharge documentaire ;
- preuves manquantes ;
- budget ou charge sous-estimes ;
- dependances techniques non maitrisees ;
- avancement reel different de l'avancement declare.

## Source de donnees

| Source | Role | Statut |
|---|---|---|
| `P6_ameliore_IA/data/metriques_p6_indicateurs.csv` | Base d'indicateurs P13 | Disponible |
| `04_plan_projet_P13_partie_1.md` | Backlog, planning, risques, kanban | Disponible |
| `05_matrice_indicateurs_P13_partie_1.md` | Statuts et preuves attendues | Disponible |
| `09_checklist_refactoring_notebook.md` | Etapes de correction notebook | Disponible |
| GitHub Projects | Statuts A faire / En cours / Termine | Disponible via capture et lien |

## Hypothese generale

Les metriques de pilotage et de qualite documentaire peuvent etre transformees en variables explicatives pour estimer un score de risque projet.

Comme le volume de donnees est faible, l'approche doit rester un POC explicable : scoring, regles metier, regression simple ou classification interpretable. Un modele complexe serait peu justifie.

## Variables explicatives possibles

| Famille | Variables candidates | Exemple de transformation |
|---|---|---|
| Avancement | `statut_matrice`, nombre de `[x]`, `[~]`, `[ ]` | Encodage numerique : 0, 0.5, 1 |
| Preuves | `preuve_calculee`, presence de source, presence de fichier | Binaire oui/non |
| Charge | nombre de taches, lots, risques, documents | Comptage par axe |
| Complexite | nombre de dependances, cellules notebook, sorties, erreurs | Normalisation ou seuils |
| Qualite data | anomalies, valeurs manquantes, jointures non rapprochees | Score de risque data |
| Reproductibilite | chemins locaux, erreurs notebook, execution complete | Score de portabilite |
| Documentation | nombre de docs, prompts traces, limites documentees | Score de maturite documentaire |
| Pilotage | jalons, kanban, risques ouverts | Score de gouvernance |

## Variables cibles possibles

| Cible | Type | Commentaire |
|---|---|---|
| `risque_delai` | Classification faible/moyen/eleve | A construire a partir des statuts et jalons |
| `risque_budget` | Classification faible/moyen/eleve | Budget surtout interprete comme charge/temps sur ce projet |
| `risque_qualite` | Classification faible/moyen/eleve | Lie aux preuves manquantes, erreurs et limites |
| `score_avancement` | Regression ou score 0-100 | Plus simple et plus explicable |
| `priorite_action` | Classification | Aide a choisir la prochaine action corrective |

## Pipeline 1 - Scoring explicable sans ML lourd

### Objectif

Construire un score de risque projet a partir de regles metier simples.

### Etapes

1. Charger `metriques_p6_indicateurs.csv` avec Pandas.
2. Nettoyer les valeurs `a_completer` et convertir les nombres exploitables.
3. Encoder les statuts : `A faire = 0`, `En cours = 0.5`, `Realise = 1`.
4. Calculer des scores par axe : veille, besoin, cahier des charges, pilotage, documentation.
5. Ajouter des penalites : preuves manquantes, erreurs notebook, chemins non valides, risques ouverts.
6. Produire un score final : `risque_projet = faible / moyen / eleve`.

### Resultats attendus

- Tableau des axes les plus fragiles.
- Score global de risque.
- Recommandations prioritaires.

### Limites

- Regles definies humainement.
- Pas de generalisation statistique.
- Pertinent pour piloter ce projet, pas pour predire tous les projets data.

### Decision possible

Retenir ce pipeline comme premiere version car il est explicable, sobre et adapte a un faible volume de donnees.

## Pipeline 2 - Classification interpretable

### Objectif

Predire une classe de risque (`faible`, `moyen`, `eleve`) a partir des variables explicatives.

### Approche technique

| Etape | Methode possible |
|---|---|
| Preparation | Pandas, encodage des statuts et variables categorielles |
| Feature engineering | Scores par axe, nombre de preuves manquantes, nombre de risques ouverts |
| Modele | Logistic Regression, Decision Tree peu profond |
| Validation | Validation manuelle ou jeu simule faute d'historique |
| Interpretation | Coefficients ou arbre de decision |

### Tests a realiser

- Comparer modele avec regles metier.
- Tester la stabilite avec plusieurs scenarios simules.
- Verifier que les variables explicatives sont coherentes metier.

### Limites

- Le fichier ne contient pas assez d'historique pour entrainer un vrai modele robuste.
- Il faudra simuler ou annoter des exemples de risques.
- Risque de surinterpretation si le modele est presente comme predictif fort.

### Decision possible

Utiliser ce pipeline uniquement comme demonstration pedagogique, avec mention explicite des limites.

## Pipeline 3 - Regression du score d'avancement

### Objectif

Estimer un score d'avancement global entre 0 et 100.

### Variables possibles

| Variable | Role |
|---|---|
| Taux de statuts realises | Mesure directe d'avancement |
| Nombre de preuves calculees | Maturite des livrables |
| Nombre de champs `a_completer` | Reste a documenter |
| Nombre de risques ouverts | Penalite projet |
| Nombre de prompts documentes | Trace IA, avec prudence |
| Execution notebook validee | Maturite technique |

### Resultats attendus

- Score d'avancement global.
- Score par axe P13.
- Ecart entre avancement documentaire et avancement technique.

### Limites

- Le score depend des ponderations choisies.
- Les ponderations doivent etre justifiees dans le notebook.

### Decision possible

Retenir pour un dashboard de pilotage simple plutot qu'un modele ML complet.

## Pipeline 4 - Detection de derive projet

### Objectif

Identifier les signaux faibles de derive avant qu'ils deviennent bloquants.

### Signaux possibles

| Signal | Interpretation |
|---|---|
| Beaucoup de preuves non calculees | Documentation insuffisante |
| Nombre eleve de risques ouverts | Pilotage a renforcer |
| Notebook avec erreur stockee | Reproductibilite fragile |
| Sorties notebook nombreuses | Depot difficile a publier |
| Statuts declares realises mais preuves absentes | Avancement surestime |
| Prompts nombreux mais decisions peu documentees | Usage IA insuffisamment critique |

### Sorties attendues

- Liste des alertes.
- Niveau de criticite.
- Action corrective recommandee.

### Decision possible

Tres pertinent pour le P13, car le but est de piloter et documenter un projet data augmente par l'IA.

## Structure possible du notebook ML

| Section | Contenu |
|---|---|
| 1. Contexte | Objectif du POC et limites du jeu de donnees |
| 2. Chargement | Lecture du CSV et controle qualite |
| 3. Nettoyage | Conversion des valeurs, traitement `a_completer` |
| 4. Feature engineering | Statuts, preuves, risques, axes, scores |
| 5. Hypotheses | Hypotheses metier sur couts, delais, budget, qualite |
| 6. Tests | Comparaison scoring, classification, regression simple |
| 7. Resultats | Scores, alertes, variables importantes |
| 8. Limites | Faible volume, absence d'historique, labels construits |
| 9. Decisions | Pipeline retenu, raisons, actions suivantes |

## Hypotheses a documenter

| Hypothese | Test possible | Decision attendue |
|---|---|---|
| Les preuves manquantes augmentent le risque de derive | Comparer score avec/sans penalite preuve | Garder si impact lisible |
| Les erreurs notebook signalent un risque technique | Penaliser les cellules avec erreur | Garder si l'objectif inclut reproductibilite |
| Les risques ouverts impactent delai et charge | Pondérer par criticite | Garder si registre des risques maintenu |
| Le nombre de prompts ne suffit pas a mesurer la qualite IA | Comparer prompts vs decisions documentees | Garder la validation humaine comme variable |
| Les sorties nombreuses nuisent a la publication GitHub | Penaliser bruit notebook | Garder pour l'objectif portfolio |

## Resultats attendus d'un POC reussi

- Un score global de risque projet.
- Un score d'avancement par axe P13.
- Une liste des actions prioritaires.
- Une explication claire des variables qui influencent le score.
- Une conclusion prudente : outil d'aide au pilotage, pas prediction certaine.

## Limites majeures

| Limite | Consequence | Mitigation |
|---|---|---|
| Peu de donnees historiques | ML supervise fragile | Preferer scoring explicable ou simulation |
| Labels de risque construits | Risque de circularite | Documenter les regles de labellisation |
| Donnees issues d'un seul projet | Generalisation limitee | Presenter comme POC interne |
| Variables qualitatives nombreuses | Encodage discutable | Justifier chaque transformation |
| Avancement humain difficile a quantifier | Score imparfait | Conserver une validation humaine |

## Decision recommandee

Pour le P13, la piste la plus solide est de commencer par un pipeline de scoring explicable, puis d'ajouter une classification simple uniquement comme comparaison pedagogique.

Decision proposee :

1. Construire un notebook POC `pilotage_p13_scoring_ml.ipynb`.
2. Utiliser `metriques_p6_indicateurs.csv` comme source principale.
3. Produire un score d'avancement et un score de risque.
4. Documenter les hypotheses, tests, resultats, limites et decisions.
5. Ne pas presenter le modele comme une prediction certaine, mais comme un outil d'aide a l'anticipation des derives.

## Backlog POC potentiel

| ID | Action | Statut |
|---|---|---|
| ML01 | Definir les variables cibles : avancement, risque delai, risque qualite | [ ] |
| ML02 | Nettoyer et typer les colonnes du CSV | [ ] |
| ML03 | Construire les scores par axe | [ ] |
| ML04 | Tester un scoring regle metier | [ ] |
| ML05 | Tester une classification simple sur scenarios simules | [ ] |
| ML06 | Comparer les resultats et choisir l'approche retenue | [ ] |
| ML07 | Documenter limites et decisions | [ ] |
