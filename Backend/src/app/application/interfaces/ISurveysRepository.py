from abc import ABC, abstractmethod


class ISurveysRepository(ABC):
    @abstractmethod
    def get_surveys(self):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, survey_id: int):
        raise NotImplementedError

    @abstractmethod
    def get_survey_questions(self, survey_id: int):
        raise NotImplementedError

    @abstractmethod
    def save_survey_responses(self,
                              user_id: int,
                              driver_id: int,
                              survey_id: int,
                              question_id: int,
                              answer: str):
        raise NotImplementedError
