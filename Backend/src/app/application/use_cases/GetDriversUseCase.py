from app.application.interfaces.IDriversRepository import IDriversRepository
from app.application.use_cases.IUseCase import IUseCase


class GetDriversUseCase(IUseCase):
    def __init__(self, drivers_repo: IDriversRepository):
        self.drivers_repo = drivers_repo

    def handle(self, operation=None):
        return self.drivers_repo.get_drivers()
