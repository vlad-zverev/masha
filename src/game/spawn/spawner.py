import random

import pygame
from pygame.time import Clock

from ..characters import MaterializedCharacter
from ..types.consts import SPAWN_FREQUANCY_MS


class Spawner:
    def __init__(self, characters: list[MaterializedCharacter], clock: Clock):
        self._characters = characters
        self._clock = clock
        self._last_spawn_tick = 0

    def spawn_random(self) -> None:
        newborn = MaterializedCharacter.get_random_subclass().from_random_soul()

        newborn.move_to_random()

        self._characters.append(newborn)

    def spawn_random_by_timer(self) -> None:
        ticks = pygame.time.get_ticks()

        if ticks - self._last_spawn_tick > SPAWN_FREQUANCY_MS * random.uniform(0.5, 2):
            self.spawn_random()
            self._last_spawn_tick = ticks
