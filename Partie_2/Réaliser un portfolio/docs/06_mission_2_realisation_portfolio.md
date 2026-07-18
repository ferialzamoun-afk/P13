# Mission 2 - Realisation du portfolio

## Objectif

Construire un portfolio GitHub Pages qui raconte les preuves de competences du parcours Data Analyst de facon lisible pour un jury, un recruteur ou un client.

La mission ne consiste pas seulement a publier des liens : elle consiste a transformer des livrables techniques en preuves comprehensibles, reliees aux blocs RNCP et aux besoins metier.

## Narration attendue des preuves

Chaque projet prioritaire doit suivre une narration stable :

| Etape | Question a laquelle repondre | Preuve attendue |
|---|---|---|
| Contexte | Dans quel environnement metier le projet s'inscrit-il ? | Situation, client fictif/reel, enjeu |
| Besoin metier | Quelle decision ou quel probleme data fallait-il traiter ? | Objectif explicite, utilisateur cible |
| Demarche | Comment les donnees ont-elles ete collectees, nettoyees, analysees et restituees ? | Notebook, scripts, dashboard, documentation |
| Resultats | Quels KPI, insights ou livrables ont ete produits ? | Chiffres, captures, exports, liens publics |
| Impact | Quelle valeur le projet apporte-t-il ? | Decision facilitee, gain de temps, qualite, priorisation |

## Integration des resultats de veille

La veille doit apparaitre dans le portfolio comme une justification des choix, pas comme une annexe isolee.

Exemples d'integration :

- Pour un projet qualite data : expliquer pourquoi Pandas/Pandera est retenu a court terme et Great Expectations en trajectoire moyen terme.
- Pour un projet IA/statistique : expliquer pourquoi Isolation Forest + SHAP est utilise pour la decision, et kNN/K-Means pour la surveillance.
- Pour un projet dashboard : expliquer pourquoi GitHub Pages, Streamlit, Power BI ou Plotly est adapte au public cible.

## Correction vs evolution

La documentation du portfolio distingue deux types d'interventions :

| Type | Definition | Exemple | Statut attendu |
|---|---|---|---|
| Correction | Action qui repare une incoherence, un lien casse, une erreur de rendu ou un chiffre obsolete | Corriger un lien GitHub Pages, remplacer une ancienne metrique, fixer un tableau Markdown mal rendu | Prioritaire avant publication |
| Evolution | Amelioration qui ajoute de la valeur sans corriger un defaut bloquant | Ajouter une nouvelle preuve, enrichir une fiche projet, ajouter une capture ou une page de synthese | Planifiee selon priorite |

Cette distinction aide a eviter de melanger les urgences de publication avec les ameliorations futures.

## TNR GitHub Pages

Avant chaque push important du portfolio, un test de non-regression doit verifier :

| Controle TNR | Attendu |
|---|---|
| Build Jekyll local | `bundle exec jekyll build --config _config.yml,_config.dev.yml` sans erreur |
| Liens internes | Les pages `.html` publiees restent accessibles |
| Liens externes | GitHub, nbviewer, Streamlit et dashboards publics ouvrent correctement |
| Rendu Markdown | Les tableaux importants ne restent pas en texte brut |
| Donnees sensibles | Aucun secret, chemin nominatif ou donnees non publiables |
| Coherence Partie 1 / Partie 2 | Les chiffres et regles de decision sont alignes |

## Preuves de Mission 2

| Preuve | Emplacement |
|---|---|
| Portfolio public | `MON-PORTFOLIO-DATA` GitHub Pages |
| Matrice portfolio | `05_matrice_portfolio_P13_partie_2.md` |
| Guide GitHub Pages | `08_guide_github_pages_portfolio.md` |
| Guide integration | `09_guide_integration_partie_2.md` |
| Guide assets/preuves | `10_guide_assets_preuves_portfolio.md` |
| Projet phare P6/P13 | `MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Amelioration_P6_IA/` |

## Phrase de soutenance

Pour la Mission 2, j'ai construit le portfolio comme une vitrine de preuves : chaque projet doit etre lisible selon le fil contexte, besoin, demarche, resultats et impact. J'ai aussi integre les resultats de veille pour montrer que les choix techniques ne sont pas arbitraires, mais relies au besoin metier, au public cible et aux contraintes de publication.