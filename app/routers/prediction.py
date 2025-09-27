"""Test router."""

from typing import Literal
from fastapi import APIRouter, Body, Depends

from app.core.users import current_active_user
from app.models.users import User
from app.schemas.ml_models import MLModelInput, PredictionResponse
from app.services.prediction import predict_survival

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(
    model_name: Literal["KNN", "LR", "NB", "SVM"],
    features: MLModelInput = Body(...),
    user: User = Depends(current_active_user),
) -> PredictionResponse:
    prediction = predict_survival(model_name, features)
    if prediction == 1.0:
        return {"prediction": "Survived"}
    else:
        return {"prediction": "Not Survived"}
