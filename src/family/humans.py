from ..characters import Human
from .base import Family


class HumansFamily(Family[Human]):
    @property
    def plural_pronunciation(self) -> str:
        return 'peoples'
