from __future__ import annotations

import pandas as pd


def build_kpi_summary(enriched_dataset: pd.DataFrame) -> pd.DataFrame:
    """Build core business KPIs for the final Bottleneck dataset."""
    total_revenue = float(enriched_dataset["ca_article"].sum())
    products_with_revenue = int((enriched_dataset["ca_article"] > 0).sum())
    top_product = enriched_dataset.sort_values("ca_article", ascending=False).head(1)

    rows = [
        {"kpi": "Chiffre d'affaires total", "valeur": round(total_revenue, 2), "unite": "EUR"},
        {"kpi": "Produits avec CA positif", "valeur": products_with_revenue, "unite": "produits"},
        {"kpi": "Panier CA moyen par produit vendu", "valeur": round(total_revenue / products_with_revenue, 2) if products_with_revenue else 0, "unite": "EUR/produit"},
        {"kpi": "Articles en rupture ou stock nul", "valeur": int(enriched_dataset["is_stockout"].sum()), "unite": "produits"},
        {"kpi": "Prix nuls ou negatifs", "valeur": int(enriched_dataset["is_price_invalid"].sum()), "unite": "produits"},
        {"kpi": "Marges negatives", "valeur": int(enriched_dataset["has_negative_margin"].sum()), "unite": "produits"},
    ]

    if not top_product.empty:
        rows.append(
            {
                "kpi": "Premier produit par CA",
                "valeur": int(top_product["product_id"].iloc[0]),
                "unite": "product_id",
            }
        )
        rows.append(
            {
                "kpi": "CA du premier produit",
                "valeur": round(float(top_product["ca_article"].iloc[0]), 2),
                "unite": "EUR",
            }
        )

    return pd.DataFrame(rows)


def build_top_revenue_products(enriched_dataset: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Return the top products by revenue."""
    columns = [
        "product_id",
        "post_title",
        "product_type",
        "price",
        "total_sales_clean",
        "ca_article",
        "stock_quantity",
        "marge_unitaire",
    ]
    available_columns = [column for column in columns if column in enriched_dataset.columns]
    return enriched_dataset.sort_values("ca_article", ascending=False)[available_columns].head(top_n).copy()


def build_pareto_revenue(enriched_dataset: pd.DataFrame) -> pd.DataFrame:
    """Build a Pareto table for product revenue."""
    pareto = enriched_dataset.loc[enriched_dataset["ca_article"] > 0, ["product_id", "ca_article"]].copy()
    pareto = pareto.sort_values("ca_article", ascending=False).reset_index(drop=True)
    total_revenue = pareto["ca_article"].sum()
    pareto["ca_cumule"] = pareto["ca_article"].cumsum()
    pareto["part_ca_cumule_pct"] = (pareto["ca_cumule"] / total_revenue * 100).round(2)
    pareto["rang"] = pareto.index + 1
    return pareto


def build_anomaly_summary(enriched_dataset: pd.DataFrame) -> pd.DataFrame:
    """Summarize business anomalies that need human validation."""
    rows = [
        {
            "anomalie": "prix_nul_ou_negatif",
            "nombre": int(enriched_dataset["is_price_invalid"].sum()),
            "decision_attendue": "Verifier la saisie prix avant correction automatique",
        },
        {
            "anomalie": "marge_negative",
            "nombre": int(enriched_dataset["has_negative_margin"].sum()),
            "decision_attendue": "Verifier prix achat, prix vente et contexte metier",
        },
        {
            "anomalie": "rupture_ou_stock_nul",
            "nombre": int(enriched_dataset["is_stockout"].sum()),
            "decision_attendue": "Prioriser selon ventes et contribution CA",
        },
        {
            "anomalie": "sans_correspondance_web_active",
            "nombre": int((~enriched_dataset["has_web_match"]).sum()),
            "decision_attendue": "Exclure des analyses web ou documenter le statut",
        },
    ]
    return pd.DataFrame(rows)


def build_category_kpis(enriched_dataset: pd.DataFrame) -> pd.DataFrame:
    """Aggregate category KPIs for storytelling."""
    if "product_type" not in enriched_dataset.columns:
        return pd.DataFrame(columns=["product_type", "produits", "ca_total", "part_ca_pct", "ventes_totales", "stock_total"])

    category_kpis = (
        enriched_dataset.groupby("product_type", dropna=False)
        .agg(
            produits=("product_id", "nunique"),
            ca_total=("ca_article", "sum"),
            ventes_totales=("total_sales_clean", "sum"),
            stock_total=("stock_quantity", "sum"),
        )
        .reset_index()
    )
    total_revenue = category_kpis["ca_total"].sum()
    category_kpis["part_ca_pct"] = (category_kpis["ca_total"] / total_revenue * 100).round(2)
    category_kpis["ca_total"] = category_kpis["ca_total"].round(2)
    return category_kpis.sort_values("ca_total", ascending=False)
