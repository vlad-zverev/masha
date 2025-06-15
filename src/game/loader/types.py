from dataclasses import dataclass
from enum import Enum
from typing import Self

from pygame.surface import Surface


class Backgrounds(Enum):
    Forest = 'forest.jpg'


class Beavers(Enum):
    Thinking = 'thinking.png'
    Attacking = 'attacking.png'
    Defending = 'defending.png'


@dataclass
class LoadedImages:
    forest: Surface
    thinking_beaver: Surface
    attacking_beaver: Surface
    defending_beaver: Surface


@dataclass
class BeaversImages:
    thinking: Surface
    attacking: Surface
    defending: Surface

    @classmethod
    def from_loaded(cls, images: LoadedImages) -> Self:
        return cls(
            thinking=images.thinking_beaver,
            attacking=images.attacking_beaver,
            defending=images.defending_beaver,
        )
