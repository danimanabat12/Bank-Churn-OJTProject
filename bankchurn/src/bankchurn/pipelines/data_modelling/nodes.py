"""
This is a boilerplate pipeline 'data_modelling'
generated using Kedro 0.19.3
"""

import pandas as pd
import typing as t
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import roc_auc_score, recall_score
from lightgbm import LGBMClassifier
import logging

logger = logging.getLogger(__name__)


def split_train(df: pd.DataFrame, parameters: t.Dict) -> t.Tuple:
    X = df[parameters["features"]]
    y = df["Exited"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def undersample_train(
    X_train: pd.DataFrame, y_train: pd.Series, parameters: t.Dict
) -> t.Tuple:
    undersampler = RandomUnderSampler(
        sampling_strategy=parameters["sampling_strategy"],
        random_state=parameters["random_state"],
    )
    X_train, y_train = undersampler.fit_resample(X_train, y_train)
    return X_train, y_train


# Scale dataset appropriately. Parameterized the features to be scaled
def scale_sets(
    X_train: pd.DataFrame, X_test: pd.DataFrame, parameters: t.Dict
) -> t.Tuple:
    scaler = MinMaxScaler()
    X_train[parameters["scale_features"]] = scaler.fit_transform(
        X_train[parameters["scale_features"]]
    )
    X_test[parameters["scale_features"]] = scaler.transform(
        X_test[parameters["scale_features"]]
    )
    return X_train, X_test


# parameterized random_state for this model.
def train_model(
    X_train: pd.DataFrame, y_train: pd.Series, parameters: t.Dict
) -> LGBMClassifier:
    lightgbm = LGBMClassifier(
        objective="binary", random_state=parameters["random_state"]
    )
    lightgbm.fit(X_train, y_train)
    return lightgbm


def evaluate_model(model: LGBMClassifier, X_test: pd.DataFrame, y_test: pd.Series):
    y_pred = model.predict(X_test)
    roc = roc_auc_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    logger.info(
        "Model has a ROC AUC score of %.3f and Recall score of %.3f on test data.",
        roc * 100,
        recall * 100,
    )
