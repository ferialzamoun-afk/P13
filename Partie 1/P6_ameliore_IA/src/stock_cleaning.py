from __future__ import annotations

import pandas as pd


def add_stock_features(erp_dataframe: pd.DataFrame) -> pd.DataFrame:
    """Add stock-control features used before and after correction."""
    dataframe = erp_dataframe.copy()
    dataframe["stock_status_expected"] = dataframe["stock_quantity"].apply(
        lambda stock_quantity: "outofstock" if stock_quantity <= 0 else "instock"
    )
    dataframe["is_negative_stock"] = dataframe["stock_quantity"] < 0
    dataframe["has_stock_status_gap"] = dataframe["stock_status"] != dataframe["stock_status_expected"]
    dataframe["needs_stock_correction"] = dataframe["is_negative_stock"] | dataframe["has_stock_status_gap"]
    return dataframe


def build_stock_diagnostic(erp_dataframe: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Build stock diagnostics with the summation method on boolean features."""
    dataframe = add_stock_features(erp_dataframe)
    diagnostic_rows = [
        {
            "controle": "incoherences stock_status",
            "resultat": int(dataframe["has_stock_status_gap"].sum()),
            "methode": "sommation booleenne",
        },
        {
            "controle": "stocks negatifs",
            "resultat": int(dataframe["is_negative_stock"].sum()),
            "methode": "sommation booleenne",
        },
        {
            "controle": "lignes a corriger",
            "resultat": int(dataframe["needs_stock_correction"].sum()),
            "methode": "sommation booleenne",
        },
    ]
    diagnostic_report = pd.DataFrame(diagnostic_rows)
    anomaly_details = dataframe.loc[
        dataframe["needs_stock_correction"],
        [
            "product_id",
            "stock_quantity",
            "stock_status",
            "stock_status_expected",
            "is_negative_stock",
            "has_stock_status_gap",
        ],
    ].copy()
    return diagnostic_report, anomaly_details


def apply_stock_corrections(
    erp_dataframe: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Correct stock anomalies and return corrected data plus audit reports."""
    before = add_stock_features(erp_dataframe)
    diagnostic_report, anomaly_details = build_stock_diagnostic(erp_dataframe)

    corrected = before.copy()
    corrected["stock_quantity_before_correction"] = corrected["stock_quantity"]
    corrected["stock_status_before_correction"] = corrected["stock_status"]

    corrected.loc[corrected["stock_quantity"] < 0, "stock_quantity"] = 0
    corrected["stock_status_expected"] = corrected["stock_quantity"].apply(
        lambda stock_quantity: "outofstock" if stock_quantity <= 0 else "instock"
    )
    corrected["stock_status"] = corrected["stock_status_expected"]

    corrected["stock_quantity_was_corrected"] = (
        corrected["stock_quantity"] != corrected["stock_quantity_before_correction"]
    )
    corrected["stock_status_was_corrected"] = (
        corrected["stock_status"] != corrected["stock_status_before_correction"]
    )
    corrected["stock_was_corrected"] = (
        corrected["stock_quantity_was_corrected"] | corrected["stock_status_was_corrected"]
    )
    corrected["is_negative_stock"] = corrected["stock_quantity"] < 0
    corrected["has_stock_status_gap"] = corrected["stock_status"] != corrected["stock_status_expected"]

    validation_report = pd.DataFrame(
        [
            {
                "controle": "stock_status modifies",
                "resultat": int(corrected["stock_status_was_corrected"].sum()),
                "methode": "sommation booleenne",
            },
            {
                "controle": "stock_quantity modifies",
                "resultat": int(corrected["stock_quantity_was_corrected"].sum()),
                "methode": "sommation booleenne",
            },
            {
                "controle": "stocks negatifs restants",
                "resultat": int(corrected["is_negative_stock"].sum()),
                "methode": "sommation booleenne",
            },
            {
                "controle": "ecarts stock_status restants",
                "resultat": int(corrected["has_stock_status_gap"].sum()),
                "methode": "sommation booleenne",
            },
        ]
    )

    correction_details = corrected.loc[
        corrected["stock_was_corrected"],
        [
            "product_id",
            "stock_quantity_before_correction",
            "stock_quantity",
            "stock_status_before_correction",
            "stock_status",
            "stock_quantity_was_corrected",
            "stock_status_was_corrected",
        ],
    ].copy()

    return corrected, diagnostic_report, anomaly_details, validation_report, correction_details
