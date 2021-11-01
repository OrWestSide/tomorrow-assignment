from app.application.interfaces.IUsersRepository import IUsersRepository
from app.application.use_cases.IUseCase import IUseCase
from app.domain.exceptions.UnauthenticatedException import \
    UnauthenticatedException
from app.domain.operations.commands.AuthenticateUser import AuthenticateUser


class AuthenticateUserUseCase(IUseCase):
    def __init__(self, user_repo: IUsersRepository):
        self.user_repo = user_repo

    @staticmethod
    def _authenticate(_user, operation):
        if _user is None or _user.dict()['passwd'] != operation.passwd:
            raise UnauthenticatedException("Unauthenticated")

    def handle(self, operation: AuthenticateUser):
        user = self.user_repo.find_by_username(operation.username)
        try:
            self._authenticate(user, operation)
        except UnauthenticatedException:
            raise UnauthenticatedException()

        return user
