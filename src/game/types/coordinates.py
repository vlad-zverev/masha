from typing import NamedTuple

Coordinates = tuple[int, int]


class Area(NamedTuple):
    position: Coordinates
    size: Coordinates
