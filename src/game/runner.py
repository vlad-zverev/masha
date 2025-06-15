import pygame

from .game import Game
from .images import CharacterImagesBinder
from .loader import Loader
from .types.consts import MAX_COORDINATES


class GameRunner:
    def __init__(
        self,
        screen_size: tuple[int, int] = MAX_COORDINATES,
    ) -> None:
        pygame.init()

        self._screen = pygame.display.set_mode(screen_size)
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
                if event.type == pygame.QUIT:
                    self._running = False

                self._game.process(event)

            pygame.display.flip()

            self._clock.tick(60)

        pygame.quit()
