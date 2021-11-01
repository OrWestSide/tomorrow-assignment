from typing import List

from pydantic import BaseModel, Field

from app.infrastructure.framework.fastapi.models.SurveyQuestion import \
    SurveyQuestion


class Survey(BaseModel):
    survey_id: int = Field(
        None,
        title="Survey ID"
    )
    questions: List[SurveyQuestion] = Field(
        None,
        title='List of questions'
    )
