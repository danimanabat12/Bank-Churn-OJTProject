"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node

from .nodes import preprocess_datasets


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_datasets,
                inputs="train",
                outputs="preprocessed_train_data",
                name="preprocess_train_data_node",
                namespace="train",
            ),
            node(
                func=preprocess_datasets,
                inputs="test",
                outputs="preprocessed_test_data",
                name="preprocess_test_data_node",
                namespace="test",
            ),
        ]
    )


# Okay but namespace is kinda interesting. Kasi parang ginagamit niya lang as index ang namespaces,
# no formatting at all, mag-refer gihapon sa output names pero ka-weird lang sa syntax kay naga
# {subtype} keme baya sa catalog pero na-gets gihapon niya. edi wow.
