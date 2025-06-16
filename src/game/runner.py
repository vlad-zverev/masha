import pygame
from pygame.font import Font

from .events import EventsMapper
from .exceptions import Exit
from .game import Game
from .loader import Loader
from .surfaces import Screen
from .text import TextRenderer
from .types.consts import FPS, MAX_COORDINATES


class GameRunner:
    def __init__(
        self,
        screen_size: tuple[int, int] = MAX_COORDINATES,
    ) -> None:
        self._running = False

        pygame.init()

        self._clock = pygame.time.Clock()

        self._text_renderer = TextRenderer()
        self._screen = Screen(self._text_renderer, screen_size)
        self._loader = Loader()

        images = self._loader.load_all()

        self._game = Game(
            self._screen,
            self._clock,
            images=images,
        )

        self._events_mapper = EventsMapper()

    def run(self) -> None:
        self._running = True

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
