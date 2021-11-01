from pydantic import BaseModel, Field


class Driver(BaseModel):
    id: int = Field(
        None,
        title="Driver ID"
    )
    name: str = Field(
        None,
        title="Driver name"
    )

    class Config:
        orm_mode = True
