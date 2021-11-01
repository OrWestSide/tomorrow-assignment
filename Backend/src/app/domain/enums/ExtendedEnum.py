from enum import Enum


class ExtendedEnum(Enum):
    def __str__(self) -> str:
        return self.value

    @classmethod
    def all(cls) -> list:
        return [c for c in list(cls)]

    @classmethod
    def keys(cls) -> list:
        return [c.name for c in list(cls)]

    @classmethod
    def to_list(cls) -> list:
        return [c.value for c in list(cls)]

    @classmethod
    def to_dict(cls) -> dict:
        return dict(zip(cls.keys(), [c.value for c in list(cls)]))
