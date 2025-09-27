import joblib
import pandas as pd

from app.ml_models.model__loader import knn_loaded, lr_loaded, nb_loaded
from app.schemas.ml_models import MLModelInput

knn_model = joblib.load(knn_loaded)
lr_model = joblib.load(lr_loaded)
nb_model = joblib.load(nb_loaded)

models = {"KNN": knn_model, "LR": lr_model, "NB": nb_model}

FEATURE_COLUMNS = [
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked_C",
    "Embarked_Q",
    "Embarked_S",
]


def predict_survival(model_name: str, features: MLModelInput) -> float:
    model = models.get(model_name)
    if model is None:
        raise ValueError(f"Model '{model_name}' not found.")

    feature_values = list(features.model_dump().values())
    X = pd.DataFrame([feature_values], columns=FEATURE_COLUMNS)
    prediction = model.predict(X)
    return float(prediction[0])
