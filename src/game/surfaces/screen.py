from typing import TYPE_CHECKING

import pygame
from pygame.surface import Surface

from ..loader.utils import resize
from ..types.consts import MAX_COORDINATES, MIN_COORDINATES

if TYPE_CHECKING:
    from ..characters import MaterializedCharacter


class Screen:
    def __init__(
        self,
        size: tuple[int, int] = MAX_COORDINATES,
    ) -> None:
        self._screen = pygame.display.set_mode(size)

    def set_background(self, image: Surface) -> None:
        screen_size = self._screen.get_size()

        if image.get_size() != screen_size:
            image = resize(image, new_x=screen_size[0])

        self._screen.blit(image, MIN_COORDINATES)

    def show_characters(self, *characters: 'MaterializedCharacter') -> None:
        for character in characters:
            self._screen.blit(
                character.image,
                character.get_pos(),
            )
