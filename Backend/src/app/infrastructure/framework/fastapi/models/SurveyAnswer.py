from typing import List

from pydantic import BaseModel, Field


class SurveyAnswer(BaseModel):
    question_id: int = Field(
        None,
        title="Question ID"
    )
    answer: List[str] = Field(
        None,
        title="Answer"
    )
