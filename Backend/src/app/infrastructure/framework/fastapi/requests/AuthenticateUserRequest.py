from pydantic import BaseModel, Field


class AuthenticateUserRequest(BaseModel):
    username: str = Field(
        title="Username"
    )
    password: str = Field(
        title="Password"
    )

