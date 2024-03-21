"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import feature_encoding

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=feature_encoding,
            inputs="preprocessed_train_data",
            outputs="engineered_train_data", 
            name="feature_encoding_node",
            namespace="train"
        ),
        node(
            func=feature_encoding,
            inputs="preprocessed_test_data",
            outputs="engineered_test_data",
            name="feature_encoding_node",
            namespace="test",
        )
    ])
