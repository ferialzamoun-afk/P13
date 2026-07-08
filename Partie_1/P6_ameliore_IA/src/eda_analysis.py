from __future__ import annotations

import pandas as pd


def add_business_features(final_dataset: pd.DataFrame) -> pd.DataFrame:
    """Add business features for EDA and KPI analysis."""
    dataframe = final_dataset.copy()

    if "total_sales" in dataframe.columns:
        dataframe["total_sales_clean"] = dataframe["total_sales"].fillna(0)
    else:
        dataframe["total_sales_clean"] = 0

    dataframe["ca_article"] = dataframe["price"] * dataframe["total_sales_clean"]

    if "purchase_price" in dataframe.columns:
        dataframe["marge_unitaire"] = dataframe["price"] - dataframe["purchase_price"]
        dataframe["taux_marge_pct"] = (dataframe["marge_unitaire"] / dataframe["price"] * 100).round(2)
        dataframe.loc[dataframe["price"] <= 0, "taux_marge_pct"] = pd.NA
    else:
        dataframe["marge_unitaire"] = pd.NA
        dataframe["taux_marge_pct"] = pd.NA

    dataframe["is_price_invalid"] = dataframe["price"] <= 0
    dataframe["is_stockout"] = dataframe["stock_quantity"] <= 0
    dataframe["has_sales"] = dataframe["total_sales_clean"] > 0
    dataframe["has_web_match"] = dataframe.get("web_disponible", 0) == 1
    dataframe["has_negative_margin"] = dataframe["marge_unitaire"] < 0

    return dataframe


def build_eda_overview(enriched_dataset: pd.DataFrame) -> pd.DataFrame:
    """Build a compact EDA overview for business interpretation."""
    rows = [
        {"metrique": "Produits analyses", "valeur": len(enriched_dataset), "unite": "produits"},
        {"metrique": "Colonnes disponibles", "valeur": enriched_dataset.shape[1], "unite": "colonnes"},
        {"metrique": "Produits avec correspondance web", "valeur": int(enriched_dataset["has_web_match"].sum()), "unite": "produits"},
        {"metrique": "Produits sans correspondance web active", "valeur": int((~enriched_dataset["has_web_match"]).sum()), "unite": "produits"},
        {"metrique": "Produits avec ventes", "valeur": int(enriched_dataset["has_sales"].sum()), "unite": "produits"},
        {"metrique": "Articles en rupture ou stock nul", "valeur": int(enriched_dataset["is_stockout"].sum()), "unite": "produits"},
        {"metrique": "Prix nuls ou negatifs", "valeur": int(enriched_dataset["is_price_invalid"].sum()), "unite": "produits"},
        {"metrique": "Marges negatives", "valeur": int(enriched_dataset["has_negative_margin"].sum()), "unite": "produits"},
        {"metrique": "Chiffre d'affaires total", "valeur": round(float(enriched_dataset["ca_article"].sum()), 2), "unite": "EUR"},
    ]
    return pd.DataFrame(rows)


def build_univariate_summary(enriched_dataset: pd.DataFrame) -> pd.DataFrame:
    """Summarize key numeric variables for univariate analysis."""
    variables = [
        "price",
        "purchase_price",
        "stock_quantity",
        "total_sales_clean",
        "ca_article",
        "marge_unitaire",
        "taux_marge_pct",
    ]
    available_variables = [variable for variable in variables if variable in enriched_dataset.columns]
    summary = enriched_dataset[available_variables].describe().T.reset_index()
    summary = summary.rename(columns={"index": "variable"})
    return summary


def build_category_summary(enriched_dataset: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales, revenue and stock by product type when available."""
    if "product_type" not in enriched_dataset.columns:
        return pd.DataFrame(columns=["product_type", "produits", "ca_total", "ventes_totales", "stock_total"])

    category_summary = (
        enriched_dataset.groupby("product_type", dropna=False)
        .agg(
            produits=("product_id", "nunique"),
            ca_total=("ca_article", "sum"),
            ventes_totales=("total_sales_clean", "sum"),
            stock_total=("stock_quantity", "sum"),
        )
        .reset_index()
        .sort_values("ca_total", ascending=False)
    )
    category_summary["ca_total"] = category_summary["ca_total"].round(2)
    return category_summary
