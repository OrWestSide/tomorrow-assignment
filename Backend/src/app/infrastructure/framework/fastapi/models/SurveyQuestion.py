from typing import Optional, List

from pydantic import BaseModel, Field

from app.domain.enums.QuestionType import QuestionType


class SurveyQuestion(BaseModel):
    question_id: int = Field(
        None,
        title='Question ID'
    )
    question_type: QuestionType = Field(
        None,
        title='Question type'
    )
    question_text: str = Field(
        None,
        title='Question text'
    )
    answers: Optional[List[str]] = Field(
        [],
        title='List of answers'
    )
