from abc import ABC, abstractmethod


class IDriversRepository(ABC):
    @abstractmethod
    def get_drivers(self):
        raise NotImplementedError
