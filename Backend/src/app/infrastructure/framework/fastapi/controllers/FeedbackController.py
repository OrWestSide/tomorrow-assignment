from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import Response

from app.application.use_cases.SaveRatingUseCase import SaveRatingUseCase
from app.application.use_cases.SaveSurveyUseCase import SaveSurveyUseCase
from app.domain.operations.commands.CreateRating import CreateRating
from app.domain.operations.commands.CreateSurveyAnswers import \
    CreateSurveyAnswers
from app.infrastructure.framework.fastapi.requests.CreateRatingRequest import \
    CreateRatingRequest
from app.infrastructure.framework.fastapi.requests.CreateSurveyRequest import \
    CreateSurveyRequest
from app.infrastructure.framework.sqlalchemy.operations import SessionLocal
from app.infrastructure.repositories.RatingsRepository import RatingsRepository
from app.infrastructure.repositories.SurveysRepository import SurveysRepository
from app.infrastructure.repositories.UsersRepository import UsersRepository

router = APIRouter()


@router.post("/rating",
             summary="Create rating",
             operation_id="createRating",
             description="Create a new rating for a driver",
             response_model=None,
             status_code=status.HTTP_201_CREATED,
             responses={
                 201: {"model": None}
             })
def create_rating(payload: CreateRatingRequest):
    ratings_repo = RatingsRepository(SessionLocal())
    operation = CreateRating(
        user_id=payload.user_id,
        driver_id=payload.driver_id,
        rating=payload.rating
    )
    uc = SaveRatingUseCase(ratings_repo)
    uc.handle(operation)

    return Response(status_code=status.HTTP_201_CREATED)


@router.post("/survey",
             summary="Create survey",
             operation_id="createSurvey",
             description="Create a new survey for a user and driver",
             response_model=None,
             status_code=status.HTTP_201_CREATED,
             responses={
                 201: {"model": None}
             })
def create_survey(payload: CreateSurveyRequest):
    surveys_repo = SurveysRepository(SessionLocal())
    users_repo = UsersRepository(SessionLocal())
    operation = CreateSurveyAnswers(
        user_id=payload.user_id,
        driver_id=payload.driver_id,
        survey_id=payload.survey_id,
        survey_answers=payload.survey_answers
    )
    uc = SaveSurveyUseCase(surveys_repo, users_repo)
    uc.handle(operation)

    return Response(status_code=status.HTTP_201_CREATED)
