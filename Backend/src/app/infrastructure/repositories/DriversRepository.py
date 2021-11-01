from sqlalchemy.orm import Session

from app.application.interfaces.IDriversRepository import IDriversRepository
from app.infrastructure.framework.sqlalchemy.dao import Driver


class DriversRepository(IDriversRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_drivers(self):
        return self.db.query(Driver).all()
