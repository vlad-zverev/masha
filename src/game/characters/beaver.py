from ...characters import Beaver
from ..surfaces import BeaverImages
from .base import MaterializedCharacter


class MaterializedBeaver(MaterializedCharacter[Beaver, BeaverImages]):
    @classmethod
    def character_soul_class(cls) -> type[Beaver]:
        return Beaver
