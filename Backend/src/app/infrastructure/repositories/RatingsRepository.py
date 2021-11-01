import datetime

from sqlalchemy.orm import Session

from app.application.interfaces.IRatingsRepository import IRatingsRepository
from app.infrastructure.framework.sqlalchemy.dao import Rating


class RatingsRepository(IRatingsRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, user_id, driver_id: int, rating: int):
        self.db.add(Rating(
                user_id=user_id,
                driver_id=driver_id,
                rating=str(rating),
                rated_at=datetime.datetime.utcnow()
        ))

        self.db.commit()
