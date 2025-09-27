from pathlib import Path

BASEPATH = Path(__file__).resolve().parent


def get_model_path(model: str) -> Path:
    return BASEPATH / f"{model}.pkl"


knn_loaded = get_model_path("titanic_KNN_model")
lr_loaded = get_model_path("titanic_LR_model")
nb_loaded = get_model_path("titanic_NB_model")
