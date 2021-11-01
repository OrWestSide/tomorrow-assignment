from sqlalchemy.orm import Session

from app.application.interfaces.IUsersRepository import IUsersRepository
from app.infrastructure.framework.sqlalchemy.dao import User


class UsersRepository(IUsersRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def update_survey_by_user_id(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        user.survey_id = None
        self.db.commit()
