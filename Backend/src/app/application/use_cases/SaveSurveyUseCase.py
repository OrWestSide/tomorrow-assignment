from app.application.interfaces.ISurveysRepository import ISurveysRepository
from app.application.interfaces.IUsersRepository import IUsersRepository
from app.application.use_cases.IUseCase import IUseCase
from app.domain.operations.commands.CreateSurveyAnswers import \
    CreateSurveyAnswers


class SaveSurveyUseCase(IUseCase):
    def __init__(self,
                 survey_repo: ISurveysRepository,
                 user_repo: IUsersRepository):
        self.survey_repo = survey_repo
        self.user_repo = user_repo

    def _save_survey_responses(self, operation: CreateSurveyAnswers):
        for answer in operation.survey_answers:
            for answer_ in answer.answer:
                self.survey_repo.save_survey_responses(
                    operation.user_id,
                    operation.driver_id,
                    operation.survey_id,
                    answer.question_id,
                    answer_
                )

    def _update_user_survey(self, user_id: int):
        self.user_repo.update_survey_by_user_id(user_id)

    def handle(self, operation: CreateSurveyAnswers) -> None:
        self._save_survey_responses(operation)
        self._update_user_survey(operation.user_id)
