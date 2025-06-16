import pygame

from ..utils import printer
from .game import Game
from .loader import Loader
from .surfaces import CharacterImagesBinder, Screen
from .types.consts import FPS, MAX_COORDINATES


class GameRunner:
    def __init__(
        self,
        screen_size: tuple[int, int] = MAX_COORDINATES,
    ) -> None:
        pygame.init()

        self._screen = Screen(screen_size)
        self._clock = pygame.time.Clock()

        self._loader = Loader()

        images = self._loader.load_all()

        self._game = Game(
            self._screen,
            self._clock,
            images=images,
        )

        self._running = True

    def run(self) -> None:
        while self._running:
            for event in pygame.event.get():
                printer.show_ok_blue(str(event))

                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_ESCAPE:
                    self._running = False
                    break

                self._game.process(event)

            pygame.display.flip()

            self._clock.tick(FPS)

        pygame.quit()
