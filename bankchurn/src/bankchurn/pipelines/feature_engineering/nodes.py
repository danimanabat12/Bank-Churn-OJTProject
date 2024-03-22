"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.19.3
"""

import pandas as pd


def feature_encoding(df: pd.DataFrame) -> pd.DataFrame:
    df["Gender"] = df["Gender"] == "Female"
    df = pd.get_dummies(df, columns=["Geography"])
    bool_cols = [column for column in df.columns if df[column].dtype == bool]
    df[bool_cols] = df[bool_cols].astype(int)

    return df
