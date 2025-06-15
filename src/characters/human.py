from .base import Character


class Human(Character):
    @classmethod
    def age_of_consent(cls) -> int:
        return 16

    @classmethod
    def average_weight(cls) -> int:
        return 60
