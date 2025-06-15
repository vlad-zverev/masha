import pygame

from ..characters import Beaver
from ..sex.consts import DEFAULT_MALE
from .characters import MaterializedBeaver, MaterializedCharacter
from .images import CharacterImagesBinder
from .loader import LoadedImages
from .spawn import Spawner
from .types.consts import MIN_COORDINATES
from .utils import check_in_area


class Game:
    def __init__(
        self,
        screen: pygame.surface.Surface,
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
        print(event)
        self._screen.blit(self._images.forest, MIN_COORDINATES)

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

            self._screen.blit(character._image, character.get_pos())
