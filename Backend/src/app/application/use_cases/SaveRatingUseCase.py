from app.application.interfaces.IRatingsRepository import IRatingsRepository
from app.application.use_cases.IUseCase import IUseCase
from app.domain.operations.commands.CreateRating import CreateRating


class SaveRatingUseCase(IUseCase):
    def __init__(self, ratings_repo: IRatingsRepository):
        self.ratings_repo = ratings_repo

    def handle(self, operation: CreateRating):
        self.ratings_repo.save(
            operation.user_id,
            operation.driver_id,
            operation.rating
        )
