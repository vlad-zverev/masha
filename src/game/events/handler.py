from typing import Optional

from ..characters import MaterializedCharacter
from ..spawn import Spawner
from .types import MappedEvent


class EventsHandler:
    def __init__(self, characters: list[MaterializedCharacter], spawner: Spawner):
        self._characters = characters
        self._spawner = spawner

    def handle_events(self, events: list[MappedEvent]) -> None:
        for event in events:
            self._handle_event(event)

    def _handle_event(self, event: MappedEvent) -> Optional[MappedEvent]:
        match event:
            case MappedEvent.SpawnRandom:
                self._spawner.spawn_random()
            case MappedEvent.MouseClicked:
                self._handle_mouse_clicked()

    def _handle_mouse_clicked(self) -> None:
        for character in self._characters:
            if character.is_under_mouse():
                character.click()
