from typing import Self

from ..loader import LoadedImages
from .base import CharacterImages


class BeaverImages(CharacterImages):
    @classmethod
    def from_loaded(cls, images: LoadedImages) -> Self:
        return cls(
            thinking=images.thinking_beaver,
            attacking=images.attacking_beaver,
            defending=images.defending_beaver,
        )
