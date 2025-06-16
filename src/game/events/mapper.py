from typing import Optional

import pygame
from pygame.event import Event

from ...utils import printer
from ..exceptions import Exit
from .types import MappedEvent


class EventsMapper:
    def map_events(self, events: list[Event]) -> list[MappedEvent]:
        mapped_events = []

        for event in events:
            printer.show_ok_blue(str(event))

            if self._is_exit(event):
                raise Exit

            if handled_event := self._map_event(event):
                mapped_events.append(handled_event)

        return mapped_events

    def _map_event(self, event: Event) -> Optional[MappedEvent]:
        match event.type:
            case pygame.KEYDOWN:
                return MappedEvent.SpawnRandom

    def _is_exit(self, event: Event) -> bool:
        return event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_ESCAPE
