from app.application.interfaces.ISurveysRepository import ISurveysRepository
from app.application.use_cases.IUseCase import IUseCase
from app.domain.operations.queries.GetSurvey import GetSurvey


class GetSurveyUseCase(IUseCase):
    def __init__(self, survey_repo: ISurveysRepository):
        self.survey_repo = survey_repo

    def handle(self, operation: GetSurvey):
        return self.survey_repo.get_by_id(operation.survey_id)
