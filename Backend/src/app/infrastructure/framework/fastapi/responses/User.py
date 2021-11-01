from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    user_id: int = Field(
        None,
        title="User ID"
    )
    username: str = Field(
        None,
        title="Username"
    )
    survey_id: Optional[int] = Field(
        None,
        title="Survey ID to be presented"
    )
