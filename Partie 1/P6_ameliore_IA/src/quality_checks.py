from __future__ import annotations

from pathlib import Path
from typing import Mapping

import pandas as pd


EXPECTED_COLUMNS: dict[str, set[str]] = {
    "ERP": {"product_id", "onsale_web", "price", "stock_quantity", "stock_status"},
    "WEB": {"sku", "total_sales"},
    "LIAISON": {"product_id", "id_web"},
}

KEY_COLUMNS: dict[str, list[str]] = {
    "ERP": ["product_id"],
    "WEB": ["sku"],
    "LIAISON": ["product_id", "id_web"],
}


def build_quality_report(
    dataframes: Mapping[str, pd.DataFrame],
    expected_columns: Mapping[str, set[str]] | None = None,
    key_columns: Mapping[str, list[str]] | None = None,
) -> pd.DataFrame:
    """Build a compact quality report for ERP, WEB and LIAISON sources."""
    expected_columns = expected_columns or EXPECTED_COLUMNS
    key_columns = key_columns or KEY_COLUMNS
    quality_rows: list[dict[str, object]] = []

    for source_name, dataframe in dataframes.items():
        columns = set(map(str, dataframe.columns))
        missing_expected_columns = sorted(expected_columns[source_name] - columns)
        duplicated_rows = int(dataframe.duplicated().sum())
        missing_values = int(dataframe.isna().sum().sum())

        quality_rows.extend(
            [
                {
                    "source": source_name,
                    "controle": "volumetrie",
                    "resultat": f"{dataframe.shape[0]} lignes / {dataframe.shape[1]} colonnes",
                    "statut": "OK" if dataframe.shape[0] > 0 and dataframe.shape[1] > 0 else "A verifier",
                },
                {
                    "source": source_name,
                    "controle": "colonnes attendues",
                    "resultat": ", ".join(missing_expected_columns) if missing_expected_columns else "Toutes presentes",
                    "statut": "OK" if not missing_expected_columns else "A verifier",
                },
                {
                    "source": source_name,
                    "controle": "valeurs manquantes",
                    "resultat": missing_values,
                    "statut": "OK" if missing_values == 0 else "A documenter",
                },
                {
                    "source": source_name,
                    "controle": "lignes dupliquees",
                    "resultat": duplicated_rows,
                    "statut": "OK" if duplicated_rows == 0 else "A verifier",
                },
            ]
        )

        for key_column in key_columns[source_name]:
            if key_column in dataframe.columns:
                duplicated_keys = int(dataframe[key_column].duplicated().sum())
                quality_rows.append(
                    {
                        "source": source_name,
                        "controle": f"unicite cle {key_column}",
                        "resultat": duplicated_keys,
                        "statut": "OK" if duplicated_keys == 0 else "A verifier",
                    }
                )

    erp_dataframe = dataframes.get("ERP")
    if erp_dataframe is not None and "stock_quantity" in erp_dataframe.columns:
        negative_stock_count = int((erp_dataframe["stock_quantity"] < 0).sum())
        quality_rows.append(
            {
                "source": "ERP",
                "controle": "stocks negatifs",
                "resultat": negative_stock_count,
                "statut": "OK" if negative_stock_count == 0 else "A corriger",
            }
        )

    if erp_dataframe is not None and "price" in erp_dataframe.columns:
        invalid_price_count = int((erp_dataframe["price"] <= 0).sum())
        quality_rows.append(
            {
                "source": "ERP",
                "controle": "prix nuls ou negatifs",
                "resultat": invalid_price_count,
                "statut": "OK" if invalid_price_count == 0 else "A verifier",
            }
        )

    return pd.DataFrame(quality_rows)


def summarize_quality_report(quality_report: pd.DataFrame) -> pd.Series:
    """Return the number of controls by status."""
    return quality_report["statut"].value_counts()


def load_sources(data_dir: Path) -> dict[str, pd.DataFrame]:
    """Load ERP, WEB and LIAISON Excel sources from a data directory."""
    return {
        "ERP": pd.read_excel(data_dir / "erp.xlsx"),
        "WEB": pd.read_excel(data_dir / "web.xlsx"),
        "LIAISON": pd.read_excel(data_dir / "liaison.xlsx"),
    }
