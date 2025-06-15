from .base import Character


class Beaver(Character):
    @classmethod
    def age_of_consent(cls) -> int:
        return 3

    @classmethod
    def average_weight(cls) -> int:
        return 10
