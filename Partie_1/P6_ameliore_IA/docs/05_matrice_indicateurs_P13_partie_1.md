# Matrice des indicateurs - P13 Partie 1

## Mission

**Piloter un projet data augmenté par l'IA** a partir du livrable du projet 6 : notebook Python d'analyse du stock et des ventes du site Bottleneck.

Narration retenue pour la restitution dashboard: **detecter -> expliquer -> prioriser -> decider**.

Arbitrage methodes:

- Decision immediate: Isolation Forest + SHAP.
- Priorisation avancee: K-Means/kNN en complement.

Cette matrice sert de tableau de suivi pour relier chaque indicateur attendu a une preuve concrete, un statut et des metriques de validation.

## Objectif poursuivi (dashboard anomalies)

- Detecter les anomalies prioritaires (qualite + score IF).
- Expliquer les alertes (SHAP) pour faciliter la decision.
- Prioriser les investigations (K-Means/kNN).
- Decider et suivre via dashboard et GitHub Project.

## Legende des statuts

- [ ] A faire
- [~] En cours
- [x] Realise

## 1. Veille metier et technologique

| Indicateur | Ma preuve | Metriques possibles | Statut |
|---|---|---|---|
| Ma veille selectionne, evalue et justifie les choix des solutions techniques. | Tableau comparatif des solutions : Controles Pandas, Isolation Forest, SHAP, K-Means/kNN, Great Expectations, Aikido. Criteres : qualite, robustesse, temps, reproductibilite, securite, conformite, sobriete. | Nombre d'outils compares ; nombre de criteres ; decision argumentee. | [x] |
| Ma veille soutient une demarche d'optimisation et d'amelioration continue. | Section pistes d'amelioration : automatiser les controles qualite, securiser le repo, clarifier le notebook, reduire le temps d'execution. | Nombre de pistes identifiees ; nombre de pistes retenues ; priorite court/moyen terme. | [x] |
| Les informations sont fiables et sourcees. | Liste de sources datees : documentation officielle Pandas, Great Expectations, Ruff, Aikido, GitHub Docs, articles reconnus. | Nombre de sources officielles ; date de consultation ; liens verifies. | [~] |
| Les informations sont coherentes avec les principes de developpement durable. | Critere sobriete numerique dans le tableau comparatif : dependances limitees, execution locale, reutilisation du notebook existant, temps de calcul. | Nombre de dependances ajoutees ; temps d'execution avant/apres ; choix d'outils legers. | [x] |
| Le systeme de veille contient au moins un element d'automatisation. | Capture ou preuve : alerte GitHub, Dependabot, newsletter, flux RSS, alerte Google, scan Aikido automatique. | Nombre d'alertes configurees ; frequence ; exemple de notification. | [ ] |
| Au moins un outil/methode selectionne est pertinent et adapte aux besoins des utilisateurs. | Justification du choix : controles qualite data pour fiabiliser l'analyse Bottleneck ; Aikido comme controle complementaire avant publication GitHub. | Besoin utilisateur couvert ; gain attendu ; limites identifiees. | [x] |
| Les besoins en formation des publics non techniques sont identifies, y compris les collaborateurs en situation de handicap. | Mini-plan formalise en 4 modules (lecture KPI, lecture graphiques, interpretation anomalies, passage a l'action), duree totale 1h40, supports accessibles (contraste eleve, police lisible, vocabulaire non technique, alt text des visuels, version PDF et version orale). | Nombre de modules ; duree estimee ; adaptations accessibilite. | [x] |
| Les impacts des nouveaux outils/methodes issus de la veille sont identifies, evalues, experimentes et documentes. | POC de notebook P6 ameliore : comparaison avant/apres, prompts IA, resultats conserves/ecartes, decisions. | Nombre d'essais IA ; variantes comparees ; resultats avant/apres ; temps gagne estime. | [~] |

## 2. Identification du besoin metier

| Indicateur | Ma preuve | Metriques possibles | Statut |
|---|---|---|---|
| La prise en compte d'un environnement complexe et changeant est demontree. | Analyse du contexte Bottleneck : donnees ERP, web et liaison ; qualite variable ; stocks ; ventes ; anomalies possibles ; contraintes de rapprochement. | Nombre de sources de donnees ; contraintes listees ; risques identifies. | [x] |
| Le besoin metier est reformule en tenant compte des contraintes internes/externes et des specificites fonctionnelles. | Reformulation synthetique du besoin : fiabiliser l'analyse des ventes et stocks pour identifier les incoherences, le chiffre d'affaires, les produits a forte valeur et les anomalies de prix. | Nombre de contraintes integrees ; validation du besoin ; criteres d'acceptation. | [x] |
| Les elements prioritaires du projet sont identifies. | Liste priorisee : qualite des donnees, jointures fiables, chiffre d'affaires, stocks, detection d'anomalies, restitution claire. | Priorite MoSCoW ; dependances ; charge estimee. | [x] |
| L'analyse du besoin clarifie les objectifs et les enjeux et permet de cadrer le projet. | Section objectifs et enjeux dans le cahier des charges : valeur metier, limites, livrables, criteres de reussite. | Objectifs formules ; KPI projet ; livrables valides. | [x] |

## 3. Cahier des charges fonctionnel

| Indicateur | Ma preuve | Metriques possibles | Statut |
|---|---|---|---|
| Le cahier des charges decrit l'etat actuel, les specificites fonctionnelles, les ressources et le budget. | Sections du CDC : etat initial du notebook P6, donnees disponibles, ressources, outils, budget nul ou limite, delai de 4 jours. | Nombre de ressources listees ; contraintes budget/delai ; outils identifies. | [x] |
| Le cahier des charges decrit le perimetre : jalons, livrables, planning. | Retroplanning 4 jours, jalons, livrables : notebook ameliore, veille, traces IA, plan projet, documentation, portfolio. | Nombre de jalons ; livrables attendus ; respect du planning. | [x] |
| Le document est clair et synthetique. | Structure avec sommaire, sections courtes, tableaux, decisions explicites. | Nombre de pages cible ; nombre de tableaux ; relecture effectuee. | [x] |
| Le document respecte les bonnes pratiques bureautiques de redaction. | Mise en page propre : titres hierarchises, pagination si PDF, annexes, liens, versioning. | Presence page de garde ; annexes ; numerotation ; version du document. | [ ] |

## 4. Organisation et pilotage du projet data

| Indicateur | Ma preuve | Metriques possibles | Statut |
|---|---|---|---|
| Le projet est decoupe en lots coherents. | Lots : cadrage, veille, audit notebook, amelioration data, experimentation IA, validation, documentation, restitution. | Nombre de lots ; livrables par lot ; dependances. | [x] |
| Un backlog de taches est formalise. | Tableau de taches avec estimation, priorite, dependances et definition de Done. | Nombre de taches ; charge estimee ; taux d'avancement. | [x] |
| Le planning est realiste et suit des jalons. | Planning par jalons (sans duree fixe) et suivi GitHub Project. | Jalons respectes ; ecart planning ; reste a faire. | [x] |
| Les risques projet sont identifies et suivis. | Mini registre des risques : qualite data, fuite de donnees, biais, temps de calcul, liens GitHub, reproductibilite. | Nombre de risques ; criticite ; actions de mitigation. | [x] |
| Le pilotage des anomalies est suivi dans un outil de projet. | GitHub Projects (board kanban + taches T13-T18). | Nombre de taches anomalies ; statut par colonne ; avancement global. | [~] |

## 5. Documentation, IA et reproductibilite

| Indicateur | Ma preuve | Metriques possibles | Statut |
|---|---|---|---|
| Les essais IA sont traces. | Journal des prompts : objectif, prompt, variante, resultat, decision humaine, limites. | Nombre de prompts ; nombre de variantes ; decisions documentees. | [x] |
| Les prompts IA en lien direct avec l'objectif dashboard sont quantifies. | Section focus BC05 dans le journal IA (9.1-9.3 + narration). | Nombre de prompts focus ; ratio focus/total ; couverture des etapes detecter/expliquer/prioriser. | [x] |
| Les choix techniques sont justifies. | Justifications dans le notebook et la documentation : nettoyage, jointures, controles, visualisations, seuils d'anomalies. | Nombre de choix explicites ; criteres utilises ; arbitrages. | [~] |
| Les controles qualite sont relies de facon coherente entre notebook et pipeline. | Articulation formalisee : Pandera en controle amont (blocage analyse) puis Great Expectations en controle aval (blocage publication). | Nombre de regles partagees (Q001, Q002, Q003...) ; taux de runs conformes ; nombre de diffusions bloquees. | [x] |
| Les limites et biais sont documentes. | Section limites : donnees manquantes, jointures incertaines, interpretation des anomalies, dependance aux sources. | Nombre de limites ; impacts ; recommandations. | [~] |
| La reproductibilite est prise en compte. | Instructions d'execution, versions, structure de dossier, chemins relatifs, seed si necessaire. | Temps d'installation ; versions listees ; execution notebook complete. | [~] |
| Une synthese recruteur/client est produite. | Synthese courte : resultats, impact, recommandations, prochaines etapes. | Nombre de recommandations ; KPI presentes ; clarte du rendu. | [~] |

## Actions immediates

| Priorite | Action | Livrable cible | Statut |
|---|---|---|---|
| 1 | Rediger le besoin metier reformule du projet Bottleneck. | Cahier des charges | [x] |
| 2 | Construire le tableau de veille comparant au moins 2 solutions. | Veille technologique | [x] |
| 3 | Documenter 2 essais IA minimum sur le notebook P6. | Tracabilite IA | [x] |
| 4 | Ajouter ou formaliser des controles qualite data et detection IF dans le notebook. | Notebook P6 ameliore | [x] |
| 5 | Ajouter explicabilite SHAP et priorisation K-Means/kNN dans la restitution dashboard. | Notebook + documentation | [x] |
| 6 | Suivre les taches anomalies dans GitHub Project (T13-T18). | Plan projet | [~] |
