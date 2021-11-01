from abc import ABC, abstractmethod


class IRatingsRepository(ABC):
    @abstractmethod
    def save(self, user_id, driver_id: int, rating: int):
        raise NotImplementedError
