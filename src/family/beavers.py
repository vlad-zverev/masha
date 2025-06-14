from ..characters import Beaver
from .base import Family


class BeaversFamily(Family[Beaver]):
    @property
    def plural_pronunciation(self) -> str:
        return 'beavers'
