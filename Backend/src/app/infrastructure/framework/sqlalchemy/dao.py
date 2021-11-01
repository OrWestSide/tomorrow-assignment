from sqlalchemy import Column, Integer, String, DateTime

from app.infrastructure.framework.sqlalchemy.operations import Base


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def dict(self):
        return dict(
            id=self.id,
            name=self.name
        )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    passwd = Column(String)
    survey_id = Column(Integer)

    def dict(self):
        return dict(
            id=self.id,
            username=self.username,
            passwd=self.passwd,
            survey_id=self.survey_id
        )


class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True)
    survey_name = Column(String)

    def dict(self):
        return dict(
            id=self.id,
            name=self.survey_name
        )


class SurveyQuestions(Base):
    __tablename__ = "survey_questions"

    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer)
    question_id = Column(Integer)

    def dict(self):
        return dict(
            id=self.id,
            survey_id=self.survey_id,
            question_id=self.question_id
        )


class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question_type = Column(String)
    question_text = Column(String)

    def dict(self):
        return dict(
            id=self.id,
            question_type=self.question_type,
            question_text=self.question_text
        )


class Answers(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer)
    answer_text = Column(String)

    def dict(self):
        return dict(
            id=self.id,
            question_id=self.question_id,
            answer_text=self.answer_text
        )


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    driver_id = Column(Integer)
    rating = Column(Integer)
    rated_at = Column(DateTime)

    def dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            driver_id=self.driver_id,
            rating=self.rating,
            rated_at=self.rated_at
        )


class UserAnswers(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    driver_id = Column(Integer)
    survey_id = Column(Integer)
    question_id = Column(Integer)
    answer_text = Column(String)
    answered_at = Column(DateTime)

    def dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            driver_id=self.driver_id,
            survey_id=self.survey_id,
            question_id=self.question_id,
            answer_text=self.answer_text,
            answered_at=self.answered_at
        )
