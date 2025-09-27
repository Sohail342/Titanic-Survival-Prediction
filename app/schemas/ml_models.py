from typing import Annotated, Optional

from pydantic import BaseModel, Field


class MLModelInput(BaseModel):
    """Schema for input data for ML model prediction"""

    Pclass: Annotated[int, Field(ge=1, le=3)] = Field(
        ..., description="Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)"
    )
    Sex: Annotated[int, Field(ge=0, le=1)] = Field(
        ..., description="Gender of the passenger (0 = male, 1 = female)"
    )
    Age: Annotated[Optional[float], Field(ge=0)] = Field(
        None, description="Age of the passenger in years"
    )
    SibSp: Annotated[int, Field(ge=0)] = Field(
        ..., description="Number of siblings/spouses aboard the Titanic"
    )
    Parch: Annotated[int, Field(ge=0)] = Field(
        ..., description="Number of parents/children aboard the Titanic"
    )
    Fare: Annotated[float, Field(ge=0)] = Field(..., description="Passenger fare")
    Embarked_C: Annotated[
        int,
        Field(
            ...,
            description="Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)",
        ),
    ]
    Embarked_Q: Annotated[
        int,
        Field(
            ...,
            description="Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)",
        ),
    ]
    Embarked_S: Annotated[
        int,
        Field(
            ...,
            description="Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)",
        ),
    ]


class PredictionResponse(BaseModel):
    prediction: str = Field(..., description="Predicted survival probability (0-100)")

    class Config:
        json_schema_extra = {"example": {"prediction": "Survived"}}
