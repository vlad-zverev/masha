from dataclasses import dataclass

from .rating import INITIAL_RATING, Rating


@dataclass
class RelationshipsIndicators:
    attraction_level: Rating = INITIAL_RATING
    had_sex: bool = False
