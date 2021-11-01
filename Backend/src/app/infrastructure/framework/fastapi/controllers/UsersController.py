from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import Response

from app.application.use_cases.AuthenticateUserUseCase import \
    AuthenticateUserUseCase
from app.domain.exceptions.UnauthenticatedException import \
    UnauthenticatedException
from app.domain.operations.commands.AuthenticateUser import AuthenticateUser
from app.infrastructure.framework.fastapi.models.ErrorModel import ErrorModel
from app.infrastructure.framework.fastapi.requests.AuthenticateUserRequest import \
    AuthenticateUserRequest
from app.infrastructure.framework.fastapi.responses.User import User
from app.infrastructure.framework.sqlalchemy.operations import SessionLocal
from app.infrastructure.repositories.UsersRepository import UsersRepository

router = APIRouter()


@router.post("/authenticate",
             summary="Authenticate",
             operation_id="authenticate",
             description="Dummy authentication",
             response_model=None,
             status_code=status.HTTP_200_OK,
             responses={
                 200: {"model": User},
                 401: {"model": ErrorModel}
             })
def authenticate(payload: AuthenticateUserRequest) -> User:
    user_repo = UsersRepository(SessionLocal())

    uc = AuthenticateUserUseCase(user_repo)
    operation = AuthenticateUser(
        username=payload.username,
        passwd=payload.password
    )

    try:
        user = uc.handle(operation)
    except UnauthenticatedException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )

    return User(
        user_id=user.dict()['id'],
        username=user.dict()['username'],
        survey_id=user.dict()['survey_id']
    )
