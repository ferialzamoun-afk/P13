# Soutenance orale - P13 Partie 1

## Objectif de la soutenance

Présenter comment le livrable P6 Bottleneck a été amélioré dans une démarche de pilotage data augmentée par l'IA, avec une preuve claire de veille, de cadrage, de documentation, de gestion de projet et de comparaison méthodologique.

Fil directeur : **détecter, expliquer, prioriser, décider**.

---

## 1. Ouverture - 45 secondes

Bonjour, je vais présenter la Partie 1 de mon P13, centrée sur l'amélioration du projet P6 Bottleneck.

Le projet initial consistait à analyser les ventes et les stocks d'une boutique de vins à partir de trois sources : ERP, Web et table de liaison. Mon objectif n'a pas été de refaire le projet, mais de transformer un livrable exploratoire en livrable plus fiable, reproductible, documenté et exploitable par un public métier.

J'ai structuré mon travail autour de quatre étapes : **détecter les anomalies, les expliquer, prioriser les actions, puis fournir une aide à la décision via le notebook et le dashboard**.

Preuves à afficher :
- `README.md`
- `docs/00_dossier_projet_unique_P13_partie_1.md`
- GitHub Project : vue portfolio du projet 2

---

## 2. Gestion de projet et GitHub Project - 1 minute

Avant de modifier le livrable, j'ai cadré le projet comme un vrai lot d'amélioration.

J'ai utilisé GitHub Project pour suivre les tâches : cadrage, veille, audit du notebook, contrôles qualité, expérimentation IA, validation, documentation et publication. Cela m'a permis de distinguer ce qui était terminé, ce qui restait en cours et ce qui devait être reporté.

Le board sert aussi de preuve de pilotage : il montre que l'amélioration n'est pas une succession de corrections isolées, mais un projet structuré avec des jalons.

À dire clairement :
- Les tâches T13 à T21 concernent le cycle BC05 : veille IA, SHAP, K-Means, kNN, matrice décisionnelle, dashboard, documentation.
- T18 correspond à la synchronisation GitHub Project.
- T12 reste lié au nettoyage/publication/security scanning, donc il peut rester en cours si la publication complète n'est pas finalisée.

Preuves à afficher :
- `docs/04_plan_projet_P13_partie_1.md`
- GitHub Project : `https://github.com/users/ferialzamoun-afk/projects/2`

Checklist GitHub Project avant soutenance :

| Carte | Statut conseillé | Commentaire oral |
|---|---|---|
| T13 - Veille IF/SHAP/K-Means/kNN | Terminé | Veille technique et choix comparés |
| T14 - Focus prompts BC05 | Terminé | Traçabilité IA ciblée |
| T15 - Arbitrage méthodes dashboard | Terminé | Séparation critique / surveillance |
| T16 - Matrice indicateurs alignée | Terminé | Preuve RNCP et indicateurs |
| T17 - Documentation projet alignée | Terminé | Dossier unique + synthèses miroir |
| T18 - Synchronisation GitHub Projects | Terminé ou En cours | Selon mise à jour effective du board |
| T19 - Seuils métier BC05 | Terminé | `critical_score` / `surveillance_score` |
| T20 - Synthèse BC05 dashboard | Terminé | Dashboard public mis à jour |
| T21 - Traçabilité IA finale | En cours ou Terminé | Selon dernier contrôle du journal IA |

---

## 3. Veille métier et technologique - 1 minute 30

La veille m'a permis de comparer plusieurs familles d'outils et de méthodes.

Pour la qualité des données, j'ai retenu une approche pragmatique : **Pandas et Pandera**. Pandas permet des contrôles rapides et lisibles dans le notebook ; Pandera apporte une validation de schéma plus formelle.

J'ai aussi étudié Great Expectations. Je ne l'ai pas retenu comme outil principal à court terme, car le coût de mise en place était trop élevé pour le délai du projet. En revanche, je l'ai positionné comme trajectoire moyen terme pour contractualiser les contrôles avant publication ou industrialisation.

Pour l'analyse avancée, j'ai comparé :
- Z-score/IQR pour les alertes simples ;
- Isolation Forest pour détecter les cas atypiques multivariés ;
- SHAP pour expliquer les alertes ;
- K-Means et kNN pour organiser le backlog d'investigation.

La décision importante est que **kNN et K-Means ne déclenchent pas seuls une urgence critique**. Ils servent à repérer des produits rares ou éloignés de leur profil de cluster, donc à alimenter la catégorie `A surveiller`.

Preuves à afficher :
- `docs/02_veille_technologique_P13_partie_1.md`
- `Partie_1/01_veille_metier_technologique.md`
- Page publique : `01_veille_metier_technologique.html`

Phrase clé :
> J'ai utilisé la veille non pas pour ajouter des outils, mais pour choisir le bon niveau de complexité : simple pour fiabiliser, explicable pour décider, avancé seulement pour prioriser.

---

## 4. Cahier des charges fonctionnel - 1 minute

Le cahier des charges reformule le besoin métier : Bottleneck dispose de données dispersées entre ERP, Web et table de liaison. Le risque principal est de prendre des décisions commerciales sur des données mal rapprochées ou incohérentes.

Le périmètre porte donc sur :
- la fiabilisation des données ;
- le rapprochement ERP/Web/Liaison ;
- la production de KPI ;
- la détection des anomalies ;
- la restitution sous forme de notebook et de dashboard.

Les contraintes sont : délai court, sobriété technique, reproductibilité, traçabilité IA, sécurité de publication et lisibilité pour un public non technique.

Les critères de réussite sont concrets : notebook exécutable, contrôles qualité visibles, KPI cohérents, résultats documentés, limites explicites, dashboard exploitable.

Preuves à afficher :
- `docs/01_cahier_des_charges_P13_partie_1.md`
- `Partie_1/02_cahier_des_charges_fonctionnel.md`
- Page publique : `02_cahier_des_charges_fonctionnel.html`

---

## 5. Documentation : hypothèses, tests, résultats, limites, décisions - 2 minutes

J'ai structuré la documentation pour éviter une simple documentation technique dispersée.

La source complète est le dossier projet unique : `docs/00_dossier_projet_unique_P13_partie_1.md`. Les fichiers `Partie_1/01` à `08` sont des synthèses courtes miroir pour la lecture rapide.

### Hypothèses

J'ai posé plusieurs hypothèses :
- le notebook initial pouvait être amélioré sans être reconstruit entièrement ;
- les incohérences majeures venaient surtout du rapprochement des sources ;
- une alerte sans explication était peu actionnable ;
- kNN/K-Means étaient utiles pour prioriser, mais pas pour décider seuls.

### Tests réalisés

Les tests couvrent :
- contrôles qualité ;
- reproductibilité des chemins ;
- cohérence des jointures ;
- exécution du notebook ;
- validation de la matrice décisionnelle ;
- synchronisation des exports vers le dashboard.

### Résultats

Les résultats principaux sont :
- CA total : **143 680,10 EUR** ;
- produits avec CA positif : **689** ;
- Pareto 80% au rang **435** ;
- ruptures ou stock nul : **92** ;
- prix invalides : **3** ;
- marges négatives : **7** ;
- 36 alertes statistiques immédiates ;
- 25 alertes Isolation Forest ;
- 42 alertes kNN de surveillance ;
- matrice stricte : **1 critique, 172 à surveiller, 652 normaux**.

### Limites

Les limites sont assumées : données sur un périmètre limité, pas de généralisation temporelle, validation métier obligatoire sur les anomalies, et pas d'automatisation complète en production.

### Décisions gardées / écartées

J'ai gardé Pandas/Pandera à court terme, Isolation Forest + SHAP pour la décision critique, et K-Means/kNN pour la surveillance. J'ai écarté une bascule complète vers Great Expectations à court terme, car elle était trop lourde pour ce lot, mais je l'ai gardée comme trajectoire moyen terme.

Preuves à afficher :
- `Partie_1/04_hypotheses.md`
- `Partie_1/05_tests.md`
- `Partie_1/06_resultats.md`
- `Partie_1/07_limites.md`
- `Partie_1/08_decisions.md`
- `docs/00_dossier_projet_unique_P13_partie_1.md`

---

## 6. Livrable P6 amélioré : notebook et démarche IA - 2 minutes

Le livrable central reste le notebook amélioré : `bottleneck_analyse_ameliore_final.ipynb`.

La version initiale était plus exploratoire. La version améliorée est structurée autour de phases : prérequis, chargement, qualité, nettoyage, rapprochement, KPI, dataviz, puis BC05.

La version actuelle contient :
- **65 cellules** ;
- **28 cellules de code** ;
- **37 cellules markdown** ;
- aucun stderr bloquant ;
- 13 graphiques Phase II ;
- 12 visuels BC05.

La démarche IA est comparative et documentée :
- j'ai utilisé l'IA pour proposer, structurer, comparer ;
- j'ai gardé les décisions humaines dans le journal IA ;
- j'ai écarté les solutions trop lourdes ou peu lisibles ;
- j'ai corrigé une dérive possible : le kNN non supervisé ne doit pas rendre un produit critique seul.

Point clé à expliquer :
> J'ai séparé `critical_score` et `surveillance_score` pour éviter qu'une rareté statistique devienne automatiquement une urgence métier. C'est un exemple concret d'usage critique de l'IA : je ne prends pas le modèle comme verdict, je l'encadre par une règle métier.

Preuves à afficher :
- Notebook amélioré
- `docs/03_journal_ia_P13_partie_1.md`
- `docs/GUIDE_EXECUTION_NOTEBOOK.md`
- Dashboard public

---

## 7. Démonstration conseillée - 2 minutes

### Démo 1 : GitHub Project

Montrer rapidement le board :
- colonnes ;
- tâches BC05 ;
- distinction terminé / en cours ;
- preuve de pilotage.

### Démo 2 : Notebook

Montrer :
- structure du notebook ;
- cellule de checkpoint final ;
- résultats BC05 ;
- matrice stricte.

### Démo 3 : Dashboard

Montrer :
- page `Reporting qualite` ;
- page `Tableau de bord decisionnel` ;
- compteurs : 1 critique, 152 à surveiller, 560 normaux avec les filtres courants ;
- lecture des scores `critical_score` et `surveillance_score`.

---

## 8. Conclusion - 45 secondes

Pour conclure, cette Partie 1 montre que j'ai su reprendre un livrable existant, l'auditer, le fiabiliser, documenter les choix, comparer plusieurs méthodes, et intégrer l'IA de manière critique.

La valeur ajoutée n'est pas seulement technique : elle est aussi méthodologique. Le projet passe d'un notebook d'analyse à un système de preuves : cahier des charges, veille, journal IA, tests, résultats, limites, dashboard et gestion de projet.

La suite logique serait d'industrialiser les contrôles qualité avec Great Expectations et de suivre ces indicateurs dans le temps, mais le livrable actuel répond déjà à l'objectif court terme : produire une analyse fiable, explicable et actionnable.

---

## Questions probables du jury et réponses courtes

### Pourquoi ne pas avoir utilisé Great Expectations directement ?

Parce que le projet avait un délai court et un périmètre notebook/dashboard. J'ai retenu Pandas/Pandera à court terme pour fiabiliser vite, et j'ai positionné Great Expectations en trajectoire moyen terme pour contractualiser la publication.

### Pourquoi kNN n'est-il pas utilisé pour décider les critiques ?

Parce que le kNN est non supervisé. Il détecte une rareté locale, pas une gravité métier. Je l'utilise donc pour prioriser la surveillance, mais la criticité repose sur IF + SHAP + impact business.

### Quelle est la preuve que l'IA a été utilisée de façon critique ?

Le journal IA documente les prompts, les décisions gardées ou écartées, et les limites. L'exemple le plus clair est l'arbitrage `critical_score` / `surveillance_score`, qui montre que je n'ai pas accepté automatiquement le score modèle.

### Comment le projet est-il piloté ?

Par un backlog documenté et un GitHub Project. Les lots couvrent le cadrage, la veille, l'audit, le notebook, l'IA, la validation, la documentation et la publication.

### Que reste-t-il à faire ?

Finaliser le nettoyage public complet, sécuriser la publication, activer les scans si besoin, et envisager une industrialisation future avec Great Expectations ou un pipeline automatisé.

---

## Version ultra-courte à mémoriser

J'ai amélioré le P6 Bottleneck en passant d'une analyse exploratoire à un livrable piloté, documenté et actionnable. J'ai cadré le besoin, mené une veille, comparé les outils, fiabilisé les données, enrichi le notebook, documenté l'usage de l'IA, puis relié les exports au dashboard. La règle clé est la séparation entre `critical_score`, pour les urgences métier, et `surveillance_score`, pour les signaux statistiques comme kNN et K-Means. Le projet est suivi dans GitHub Project et toutes les preuves sont reliées dans le dossier projet unique.