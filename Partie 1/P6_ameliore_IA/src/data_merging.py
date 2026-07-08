from __future__ import annotations

import pandas as pd


def prepare_web_products(web_dataframe: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Keep valid web products and create a clean merge key."""
    web_products = web_dataframe[web_dataframe["post_type"] == "product"].copy()
    initial_rows = len(web_products)
    missing_sku_rows = int(web_products["sku"].isna().sum())

    web_products = web_products[web_products["sku"].notna()].copy()
    web_products["id_web_key"] = web_products["sku"].astype("string")

    duplicated_keys_before = int(web_products["id_web_key"].duplicated().sum())
    web_products = web_products.drop_duplicates(subset=["id_web_key"], keep="first").copy()

    preparation_report = pd.DataFrame(
        [
            {"controle": "lignes web post_type product", "resultat": initial_rows},
            {"controle": "lignes web sans sku exclues", "resultat": missing_sku_rows},
            {"controle": "doublons cle web exclus", "resultat": duplicated_keys_before},
            {"controle": "lignes web produits retenues", "resultat": len(web_products)},
        ]
    )
    return web_products, preparation_report


def build_final_dataset(
    erp_dataframe: pd.DataFrame,
    liaison_dataframe: pd.DataFrame,
    web_dataframe: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Merge ERP, liaison and web data while keeping all ERP products."""
    liaison = liaison_dataframe.copy()
    liaison["id_web_key"] = liaison["id_web"].astype("string")

    web_products, web_preparation_report = prepare_web_products(web_dataframe)

    erp_liaison = erp_dataframe.merge(
        liaison,
        on="product_id",
        how="left",
        indicator="erp_liaison_merge",
    )

    final_dataset = erp_liaison.merge(
        web_products,
        on="id_web_key",
        how="left",
        suffixes=("", "_web"),
        indicator="web_merge",
    )
    final_dataset["web_disponible"] = (final_dataset["web_merge"] == "both").astype(int)

    merge_report = pd.DataFrame(
        [
            {"controle": "produits ERP initiaux", "resultat": len(erp_dataframe)},
            {"controle": "lignes liaison", "resultat": len(liaison_dataframe)},
            {"controle": "lignes ERP apres liaison", "resultat": len(erp_liaison)},
            {"controle": "ERP sans product_id liaison", "resultat": int((erp_liaison["erp_liaison_merge"] == "left_only").sum())},
            {"controle": "ERP sans id_web", "resultat": int(erp_liaison["id_web"].isna().sum())},
            {"controle": "produits web retenus", "resultat": len(web_products)},
            {"controle": "lignes dataset final", "resultat": len(final_dataset)},
            {"controle": "produits avec correspondance web", "resultat": int((final_dataset["web_merge"] == "both").sum())},
            {"controle": "produits sans correspondance web", "resultat": int((final_dataset["web_merge"] == "left_only").sum())},
            {"controle": "produits web sans correspondance ERP", "resultat": int((~web_products["id_web_key"].isin(erp_liaison["id_web_key"].dropna())).sum())},
        ]
    )

    erp_without_web = final_dataset.loc[
        final_dataset["web_merge"] == "left_only",
        ["product_id", "id_web", "price", "stock_quantity", "stock_status"],
    ].copy()

    web_without_erp = web_products.loc[
        ~web_products["id_web_key"].isin(erp_liaison["id_web_key"].dropna()),
        ["sku", "post_title", "post_type", "total_sales"],
    ].copy()

    return final_dataset, merge_report, web_preparation_report, erp_without_web, web_without_erp
