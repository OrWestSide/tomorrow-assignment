from typing import List

from dataclasses import dataclass

from app.infrastructure.framework.fastapi.models.SurveyAnswer import \
    SurveyAnswer


@dataclass
class CreateSurveyAnswers:
    user_id: int = None
    driver_id: int = None
    survey_id: int = None
    survey_answers: List[SurveyAnswer] = None
