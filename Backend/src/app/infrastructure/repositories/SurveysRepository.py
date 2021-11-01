import datetime

from sqlalchemy.orm import Session

from app.application.interfaces.ISurveysRepository import ISurveysRepository
from app.infrastructure.framework.sqlalchemy.dao import Survey, \
    SurveyQuestions, Questions, UserAnswers


class SurveysRepository(ISurveysRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_surveys(self):
        return self.db.query(Survey).all()

    def get_by_id(self, survey_id: int):
        return self.db.query(Survey).filter(Survey.id == survey_id).first()

    def get_survey_questions(self, survey_id: int):
        return self.db.query(SurveyQuestions, Questions).filter(
            SurveyQuestions.question_id == Questions.id
        ).filter(
            SurveyQuestions.survey_id == survey_id
        )

    def save_survey_responses(self,
                              user_id: int,
                              driver_id: int,
                              survey_id: int,
                              question_id: int,
                              answer: str):
        self.db.add(UserAnswers(
            user_id=user_id,
            driver_id=driver_id,
            survey_id=survey_id,
            question_id=question_id,
            answer_text=answer,
            answered_at=datetime.datetime.utcnow()
        ))

        self.db.commit()
