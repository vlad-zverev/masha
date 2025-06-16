from typing import Optional

from ..spawn import Spawner
from .types import MappedEvent


class EventsHandler:
    def __init__(self, spawner: Spawner):
        self._spawner = spawner

    def handle_events(self, events: list[MappedEvent]) -> None:
        for event in events:
            self._handle_event(event)

    def _handle_event(self, event: MappedEvent) -> Optional[MappedEvent]:
        match event:
            case MappedEvent.SpawnRandom:
                self._spawner.spawn_random()
