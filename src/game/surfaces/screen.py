from typing import TYPE_CHECKING

import pygame
from pygame.surface import Surface

from ..loader.utils import resize
from ..text import TextRenderer
from ..types.consts import MAX_COORDINATES, MIN_COORDINATES

if TYPE_CHECKING:
    from ..characters import MaterializedCharacterType


class Screen:
    def __init__(
        self,
        text_renderer: TextRenderer,
        size: tuple[int, int] = MAX_COORDINATES,
    ) -> None:
        self._screen = pygame.display.set_mode(size)
        self._text_renderer = text_renderer

    def set_background(self, image: Surface) -> None:
        screen_size = self._screen.get_size()

        if image.get_size() != screen_size:
            image = resize(image, new_x=screen_size[0])

        self._screen.blit(image, MIN_COORDINATES)

    def show_characters(self, *characters: 'MaterializedCharacterType') -> None:
        for character in characters:
            self._screen.blit(
                character.image,
                character.get_pos(),
            )

    def show_texts(self, *characters: 'MaterializedCharacterType') -> None:
        for character in characters:
            self._screen.blit(
                self._text_renderer.render(
                    character.soul.name,
                    character.name_color,
                ),
                character.get_pos(),
            )
