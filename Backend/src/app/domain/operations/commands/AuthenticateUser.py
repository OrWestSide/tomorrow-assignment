from dataclasses import dataclass


@dataclass
class AuthenticateUser:
    username: str = None
    passwd: str = None
