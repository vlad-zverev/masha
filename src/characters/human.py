from .base import Character


class Human(Character):
    @property
    def age_of_consent(self) -> int:
        return 16
