from typing import List

from pydantic import BaseModel, Field

from app.infrastructure.framework.fastapi.models.SurveyAnswer import \
    SurveyAnswer


class CreateSurveyRequest(BaseModel):
    user_id: int = Field(
        None,
        title="User ID"
    )
    driver_id: int = Field(
        None,
        title="Driver ID"
    )
    survey_id: int = Field(
        None,
        title="Survey ID"
    )
    survey_answers: List[SurveyAnswer] = Field(
        None,
        title="Survey Answers"
    )

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "driver_id": 2,
                "survey_id": 1,
                "survey_answers": [
                    {
                        "question_id": 1,
                        "answer": ["Male"]
                    }
                ]
            }
        }
