from abc import abstractmethod, ABC


class IAnswersRepository(ABC):
    @abstractmethod
    def get_by_question_id(self, question_id: int):
        raise NotImplementedError
