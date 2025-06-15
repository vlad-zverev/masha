from abc import ABC, abstractmethod
from typing import Self, TypeVar

from pygame.surface import Surface

from ..loader import LoadedImages

T_CharacterImages = TypeVar('T_CharacterImages', bound='CharacterImages')


class CharacterImages(ABC):
    def __init__(
        self,
        thinking: Surface,
        attacking: Surface,
        defending: Surface,
    ) -> None:
        self._thinking = thinking
        self._attacking = attacking
        self._defending = defending

    @property
    def thinking(self) -> Surface:
        return self._thinking

    @property
    def attacking(self) -> Surface:
        return self._attacking

    @property
    def defending(self) -> Surface:
        return self._defending

    @classmethod
    @abstractmethod
    def from_loaded(cls, images: LoadedImages) -> Self:
        pass
