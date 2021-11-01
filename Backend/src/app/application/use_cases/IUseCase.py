from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')
R = TypeVar('R')


class IUseCase(ABC, Generic[T, R]):
    @abstractmethod
    def handle(self, operation: T) -> R:
        pass
