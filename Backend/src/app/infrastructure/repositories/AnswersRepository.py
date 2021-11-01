from sqlalchemy.orm import Session

from app.application.interfaces.IAnswersRepository import IAnswersRepository
from app.infrastructure.framework.sqlalchemy.dao import Answers


class AnswersRepository(IAnswersRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_by_question_id(self, question_id: int):
        return self.db.query(Answers).filter(
            Answers.question_id == question_id
        )
