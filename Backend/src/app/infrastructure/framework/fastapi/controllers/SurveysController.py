from fastapi import APIRouter
from starlette import status

from app.application.use_cases.GetSurveyQuestionsAndAnswersUseCase import \
    GetSurveyQuestionsAndAnswersUseCase
from app.application.use_cases.GetSurveyUseCase import GetSurveyUseCase
from app.domain.operations.queries.GetSurvey import GetSurvey
from app.domain.operations.queries.GetSurveyQuestionsAndAnswersOperation import \
    GetSurveyQuestionsAndAnswersOperation
from app.infrastructure.framework.fastapi.models.SurveyQuestion import \
    SurveyQuestion
from app.infrastructure.framework.fastapi.responses.Survey import Survey
from app.infrastructure.framework.sqlalchemy.operations import SessionLocal
from app.infrastructure.repositories.AnswersRepository import AnswersRepository
from app.infrastructure.repositories.SurveysRepository import SurveysRepository

router = APIRouter()


@router.get("/{survey_id}",
            summary="Get random survey",
            operation_id="getRandomSurvey",
            description="Get a random survey",
            response_model=Survey,
            status_code=status.HTTP_200_OK,
            responses={
                200: {"model": Survey}
            })
def get_random_survey(survey_id: int):
    loc_session = SessionLocal()

    survey_repo = SurveysRepository(loc_session)
    uc = GetSurveyUseCase(survey_repo)
    operation = GetSurvey(survey_id=survey_id)
    survey = uc.handle(operation)

    answers_repo = AnswersRepository(loc_session)
    uc = GetSurveyQuestionsAndAnswersUseCase(survey_repo, answers_repo)
    operation = GetSurveyQuestionsAndAnswersOperation(
        survey_id=survey.dict()['id']
    )
    questions = uc.handle(operation)

    return Survey(
        survey_id=survey.dict()['id'],
        questions=[SurveyQuestion(**question) for question in questions]
    )
