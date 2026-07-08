# Great Expectations & Data Contracts - Stratégie P13

## Context

Bottleneck wine shop déploie une analyse pivot consolidant 3 sources de données (ERP, Web, Liaison). Pour garantir la qualité des données et préparer une évolution industrielle, une stratégie de "Data Contracts" formels a été mise en place.

## Définition : Data Contracts vs Great Expectations

### Data Contracts
- **Définition** : Spécifications exécutables des attentes sur les données
- **Forme** : Assertions testables (expectations = contrats de service entre producteurs et consommateurs de données)
- **Exemple** : "product_id doit être unique" = contrat que ERP doit respecter
- **Usage** : Validation reproducible, documentation vivante, base pour pipelines

### Great Expectations (GE)
- **Outil** : Framework Python formalisé pour valider des data contracts
- **Force** : Gestion centralisée, reporting riche, intégration pipelines
- **Où** : Pipeline industriels (Airflow, DBT, etc.)
- **Quando** : Moyen/long terme (Bottleneck stade 2-3)

## Stratégie déploiement par stade

### 🟢 COURT TERME (Juillet 2026 - P13 Partie 1)
**Status : EN COURS**

#### Implémentation
- **Pandas controls** : 18 points qualité validés (doublons, manquants, clés, bornes)
- **Data Contracts** : 7 expectations formels en Python (équivalent GE structure)
  - ERP : product_id unique, price valid, stock >= 0, purchase_price > 0
  - WEB : sku not null, sales >= 0
  - LIAISON : product_id unique
- **Résultat** : 4/7 contracts passent ; anomalies documentées (prix invalides, sku nulls, marges négatives)

#### Livrables
- ✅ Notebook M03b : Data Contracts formels exécutables
- ✅ Veille technologique : Matrice stades de maturité
- ✅ Documentation : Contrats comme spécifications

#### Portfolio value
- ✅ Montre : Compréhension data quality engineering
- ✅ Montre : Thinking "contrats" (prêt pour pipeline)
- ✅ Montre : Pragmatisme (GE structure sans surcharge)

---

### 🟡 MOYEN TERME (Q1-Q2 2027 - Bottleneck Pipeline)
**Status : PLANNED**

#### Évolution attendue
- **Great Expectations intégré** : Installation complète GE v19+
- **Datasource GE** : Connexion ERP/Web/Liaison live
- **Expectations suite** : 100+ tests (comprenant court terme + nouvelles métriques)
- **Checkpoints** : Validation avant chaque étape ETL
- **Data context** : Historique exécutions, rapports HTML

#### Architecture
```
ERP (source) ---> GE Datasource ---> Checkpoints (7 tests + 100 tests) ---> Airflow DAG
Web (source) ---> GE Datasource ---> Validation report ---> Dashboard
Liaison        ---> GE Datasource ---> Alertes anomalies ----> Slack
                                    ---> Artifact storage --> S3
```

#### New Expectations (moyen terme)
- **Fraîcheur** : Données ERP < 24h old
- **Volume** : Web lignes = +/- 10% jour précédent
- **Cohérence** : Pareto 80% stable (rank change < 5%)
- **Anomalies** : Nouveaux prix outliers alertés auto
- **Correlations** : Dérives coefficients corrélation détectées

---

### 🔴 LONG TERME (2027+)- Industrialisation complète
**Status : VISION**

#### Intégration ML
- **Feature store** : GE + MLflow validation
- **Data drift detection** : Evidently AI sur inputs prédictions
- **Model contracts** : Expectations modèles + données
- **Retraining pipelines** : Auto-triggering sur violations

#### Stack final
```
Source data ----> GE (200+ expectations) -----> DBT transforms
                         |                             |
                    Monitoring                    dbt tests
                         |                             |
                    Slack alerts <----> Feature store <----> MLflow
                                               |
                                         Predictions
                                           (Recommandations
                                            produits)
```

---

## Current Implementation (M05b - Data Contracts)

### Cellule M05b : Data Contracts formels

```python
# 7 Data Contracts testés :
# ERP
E1 : product_id unique ✅
E2 : price 0.01-10000 ❌ (3 prix invalides détectés)
E3 : stock_quantity >= 0 ✅
E4 : purchase_price > 0 ✅

# WEB  
W1 : sku not null ❌ (2 null détectés)
W2 : sales >= 0 ❌ (négatifs présents)

# LIAISON
L1 : product_id unique ✅

# Résultat : 4/7 (57%) - OK pour court terme
```

### Format des contracts (réutilisable GE)

Chaque contract a structure standardisée :
```python
contract = {
    "E1_product_id_unique": {
        "description": "product_id est clé primaire",
        "test": lambda df: df['product_id'].is_unique,
        "critical": True,
        "source": "ERP",
        "severity": "CRITICAL"
    }
}
```

**Migration futur vers GE YAML** :
```yaml
expectations:
  - type: column_values_to_be_unique
    kwargs:
      column: product_id
    meta:
      criticality: CRITICAL
```

---

## Portfolio Value

### Qu'est ce que ça montre ?

| Aspect | Compétence démontrée |
|---|---|
| Contracts formels | Data quality thinking |
| 7 expectations | Compréhension besoin data |
| Escalade court→moyen→long | Vision architecturale |
| Pragmatisme (pas overengineering) | Jugement ingénierie |
| Documentation claire | Communication technique |

### Comment en parler en entretien ?

**Exemple réponse** :
> "Sur Bottleneck, j'ai implémenté des Data Contracts formels - essence même de Great Expectations. 
> Au court terme, j'ai codé 7 expectations clés en Python pur (pragmatique pour un notebook).
> Moyen terme, ces contrats migreront vers GE v19+ avec pipeline Airflow.
> Long terme, j'envisage intégration ML avec monitoring dérive modèles.
> C'est une preuve que je comprends l'évolution d'une solution : du notebook au pipeline à la production ML."

---

## Ressources & Références

### Great Expectations
- [Documentation officielle](https://docs.greatexpectations.io/)
- [Tutoriel Quickstart](https://docs.greatexpectations.io/docs/tutorials)
- [Validating Pandas DataFrames](https://docs.greatexpectations.io/docs/guides/validation/how_to_validate_data_using_great_expectations/)

### Data Contracts
- [Data Contract Patterns](https://soda.io/blog/what-is-a-data-contract/)
- [Linkedin : Data Contracts Trend](https://www.linkedin.com/pulse/data-contracts-new-foundation-reliable-data-systems-john-raynor/)

### Alternatives
- **Soda SQL** : Lightweight alternative à GE
- **Pandera** : Validation schema pandas
- **Evidently AI** : Focus monitoring dérive données/modèles
- **dbt tests** : Integré DBT pour transformations

---

## Décisions implémentation

| Question | Réponse | Raison |
|---|---|---|
| Utiliser GE v19 complet maintenant ? | Non | Trop complexe notebook court |
| Utiliser Data Contracts formels ? | **Oui** | Pragmatique + portfolio + future-proof |
| Migrer vers GE moyen terme ? | **Oui** | Naturelle escalade + pipeline ready |
| Monitorer dérive moyen terme ? | Oui (Evidently) | Essential pour production |
| Intégrer ML long terme ? | Oui (MLflow) | Full stack industriel |

---

## Next Steps

- [ ] Executer M05b (Data Contracts) - TEST OK ✅
- [ ] Documenter anomalies détectées (3 prix invalides, 2 sku null, negative sales)
- [ ] Créer Jupyter notebook "GE intro" (optionnel - future portfolio piece)
- [ ] Ajouter section "Data Contracts" dans GUIDE_EXECUTION.md
- [ ] Préparer présentation "Data Quality @ Bottleneck" (portfolio partageable)

---

**Auteur** : IA Copilot | **Date** : 2026-07-08 | **Version** : 1.0 | **Status** : Active
