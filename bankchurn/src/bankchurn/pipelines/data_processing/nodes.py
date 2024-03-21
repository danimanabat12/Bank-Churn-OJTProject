"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd


def preprocess_datasets(X: pd.DataFrame) -> pd.DataFrame:
    X = X.drop_duplicates()
    try:
        X = X.drop(columns=["id", "CustomerId", "Surname"], axis=1)
    except:
        pass
    numerical_cols = list(X.select_dtypes(include=["int64", "float64"]).columns)
    categorical_cols = list(X.select_dtypes(include=["object", "bool"]).columns)

    imputer_categorical = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
    imputer_numerical = SimpleImputer(missing_values=np.nan, strategy="mean")

    X[categorical_cols] = imputer_categorical.fit_transform(X[categorical_cols])
    X[numerical_cols] = imputer_numerical.fit_transform(X[numerical_cols])

    return X
