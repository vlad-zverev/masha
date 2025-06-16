import pygame

from .events import EventsMapper
from .exceptions import Exit
from .game import Game
from .loader import Loader
from .surfaces import Screen
from .types.consts import FPS, MAX_COORDINATES


class GameRunner:
    def __init__(
        self,
        screen_size: tuple[int, int] = MAX_COORDINATES,
    ) -> None:
        pygame.init()

        self._clock = pygame.time.Clock()

        self._screen = Screen(screen_size)
        self._loader = Loader()

        images = self._loader.load_all()

        self._game = Game(
            self._screen,
            self._clock,
            images=images,
        )

        self._events_mapper = EventsMapper()

        self._running = True

    def run(self) -> None:
        while self._running:
            events = pygame.event.get()

            try:
                mapped_events = self._events_mapper.map_events(events)
            except Exit:
                self._running = False
                break

            self._game.process(mapped_events)

            pygame.display.flip()

            self._clock.tick(FPS)

        pygame.quit()
