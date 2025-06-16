import pygame

from .behavior import CharactersBehavior
from .characters import MaterializedCharacter
from .events import EventsHandler, MappedEvent
from .loader import LoadedImages
from .spawn import Spawner
from .surfaces import CharacterImagesBinder, Screen


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
        self._behavior = CharactersBehavior(self._characters)
        self._events_handler = EventsHandler(self._spawner)

        CharacterImagesBinder(images).bind_images_to_characters_classes()

    def process(self, events: list[MappedEvent]) -> None:
        self._set_background()

        self._events_handler.handle_events(events)

        self._behavior.behave()

        self._screen.show_characters(*self._characters)

    def _set_background(self) -> None:
        self._screen.set_background(self._images.forest)
