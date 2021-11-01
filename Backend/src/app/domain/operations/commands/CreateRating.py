from dataclasses import dataclass


@dataclass
class CreateRating:
    user_id: int = None
    driver_id: int = None
    rating: int = None
