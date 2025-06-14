from .base import Character


class Beaver(Character):
    @property
    def age_of_consent(self) -> int:
        return 3
