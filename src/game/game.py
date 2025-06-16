import pygame

from .characters import MaterializedCharacter
from .loader import LoadedImages
from .spawn import Spawner
from .surfaces import CharacterImagesBinder, Screen
from .utils import check_in_area


class Game:
    def __init__(
        self,
        screen: Screen,
        clock: pygame.time.Clock,
        images: LoadedImages,
    ):
        self._screen = screen
        self._clock = clock
        self._images = images

        self._characters: list[MaterializedCharacter] = []

        self._spawner = Spawner(self._characters)

        CharacterImagesBinder(images).bind_images_to_characters_classes()

    def process(self, event: pygame.event.Event) -> None:
        self._set_background()

        if event.type == pygame.KEYDOWN:
            self._spawner.spawn_random()

        mouse_pos = pygame.mouse.get_pos()

        for character in self._characters:
            if check_in_area(mouse_pos, character.get_area()):
                cur_x, cur_y = character.get_pos()
                character.move_to((cur_x + 1, cur_y + 1))
                character.defend()
            else:
                character.think()

            self._screen.show_character(character)

    def _set_background(self) -> None:
        self._screen.set_background(self._images.forest)
