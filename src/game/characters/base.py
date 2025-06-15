import random
from abc import ABC, abstractmethod
from typing import Generic, Self

from pygame.surface import Surface

from ...characters import T_Character
from ..images import T_CharacterImages
from ..types import Area, Coordinates
from ..types.consts import MIN_COORDINATES
from ..utils.randomizer import get_random_coordinates


class MaterializedCharacter(ABC, Generic[T_Character, T_CharacterImages]):
    images: T_CharacterImages
    _subclasses: list[type['MaterializedCharacter']] = []

    def __init_subclass__(cls) -> None:
        cls._subclasses.append(cls)

    def __init__(
        self,
        character: T_Character,
        coordinates: Coordinates = MIN_COORDINATES,
    ):
        self._character = character
        self._coordinates = coordinates

        self._image = self.images.thinking

    @classmethod
    @abstractmethod
    def character_soul_class(cls) -> type[T_Character]:
        pass

    @classmethod
    def from_random_soul(cls) -> Self:
        return cls(cls.character_soul_class().create_random())

    @classmethod
    def get_random_subclass(cls) -> type['MaterializedCharacter']:
        return random.choice(cls._subclasses)

    @classmethod
    def bind_images(cls, images: T_CharacterImages) -> None:
        cls.images = images

    def get_area(self) -> Area:
        return Area(self.get_pos(), self.get_size())

    def get_pos(self) -> Coordinates:
        return self._coordinates

    def get_size(self) -> Coordinates:
        return self._image.get_size()

    def move_to(self, pos: Coordinates) -> None:
        self._coordinates = pos

    def move_to_random(self) -> None:
        self._coordinates = get_random_coordinates()

    def think(self) -> None:
        self._change_image(self.images.thinking)

    def attack(self) -> None:
        self._change_image(self.images.attacking)

    def defend(self) -> None:
        self._change_image(self.images.defending)

    def _change_image(self, image: Surface) -> None:
        self._image = image
