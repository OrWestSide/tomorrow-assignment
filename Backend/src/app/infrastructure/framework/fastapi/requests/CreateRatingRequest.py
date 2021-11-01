from typing import List, Optional

from pydantic import BaseModel, Field

from app.infrastructure.framework.fastapi.models.SurveyAnswer import \
    SurveyAnswer


class CreateRatingRequest(BaseModel):
    user_id: int = Field(
        None,
        title="User ID"
    )
    driver_id: int = Field(
        None,
        title="Driver ID"
    )
    rating: int = Field(
        None,
        title="Rating",
        ge=0,
        le=5
    )

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "driver_id": 2,
                "rating": 4
            }
        }
