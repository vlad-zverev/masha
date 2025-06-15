from dataclasses import dataclass

from .rating import INITIAL_RATING, Rating


@dataclass
class RelationshipsIndicators:
    intimate_rating: Rating = INITIAL_RATING
    had_sex: bool = False
