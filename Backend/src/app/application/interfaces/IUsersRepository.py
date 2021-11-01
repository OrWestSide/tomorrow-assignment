from abc import ABC, abstractmethod


class IUsersRepository(ABC):
    @abstractmethod
    def find_by_username(self, username: str):
        raise NotImplementedError

    @abstractmethod
    def update_survey_by_user_id(self, user_id: int):
        raise NotImplementedError
