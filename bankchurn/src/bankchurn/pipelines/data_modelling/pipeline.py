"""
This is a boilerplate pipeline 'data_modelling'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node

from .nodes import (
    split_train,
    undersample_train,
    scale_sets,
    train_model,
    evaluate_model,
)


def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance = pipeline(
        [
            node(
                func=split_train,
                inputs=["engineered_train_data", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_train_node",
            ),
            node(
                func=undersample_train,
                inputs=["X_train", "y_train", "params:model_options"],
                outputs=["X_train_undersampled", "y_train_undersampled"],
                name="undersample_train_node",
            ),
            node(
                func=scale_sets,
                inputs=["X_train_undersampled", "X_test", "params:model_options"],
                outputs=["X_train_scaled", "X_test_scaled"],
                name="scale_sets_node",
            ),
            node(
                func=train_model,
                inputs=[
                    "X_train_scaled",
                    "y_train_undersampled",
                    "params:model_options",
                ],
                outputs="model",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["model", "X_test_scaled", "y_test"],
                outputs=None,
                name="evaluate_model_node",
            ),
        ]
    )

    ds_pipeline_1 = pipeline(
        pipe=pipeline_instance,
        inputs="engineered_train_data",
        namespace="active_modelling_pipeline",
    )
    ds_pipeline_2 = pipeline(
        pipe=pipeline_instance,
        inputs="engineered_train_data",
        namespace="candidate_modelling_pipeline",
    )

    return ds_pipeline_1 + ds_pipeline_2
