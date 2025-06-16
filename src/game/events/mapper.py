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

            if handled_event := self._map_event(event):
                mapped_events.append(handled_event)

        return mapped_events

    def _map_event(self, event: Event) -> Optional[MappedEvent]:
        match event.type:
            case pygame.QUIT:
                raise Exit
            case pygame.KEYDOWN:
                return self._map_key_down(event)
            case pygame.MOUSEBUTTONDOWN:
                return MappedEvent.MouseClicked

    def _map_key_down(self, event: Event) -> Optional[MappedEvent]:
        match event.dict['key']:
            case pygame.K_ESCAPE:
                raise Exit
            case _:
                return MappedEvent.SpawnRandom
