from typing import Optional

from pydantic import BaseModel, Field

from app.infrastructure.framework.fastapi.responses.Survey import Survey


class Rating(BaseModel):
    survey: Optional[Survey] = Field(
        None,
        title='Optional survey'
    )
