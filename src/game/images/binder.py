from typing import TYPE_CHECKING

from ..loader import LoadedImages
from .base import CharacterImages
from .beaver import BeaverImages

if TYPE_CHECKING:
    from ..characters import MaterializedCharacter


class CharacterImagesBinder:
    def __init__(self, images: LoadedImages):
        self._images = images

    def bind_images_to_characters_classes(self) -> None:
        from ..characters import MaterializedBeaver

        self._bind(MaterializedBeaver, BeaverImages)

    def _bind(self, character_class: type['MaterializedCharacter'], images_class: type[CharacterImages]) -> None:
        character_images = images_class.from_loaded(self._images)

        character_class.bind_images(images=character_images)
