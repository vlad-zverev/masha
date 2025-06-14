from collections import defaultdict
from typing import TYPE_CHECKING

from .indicators import RelationshipsIndicators

if TYPE_CHECKING:
    from ..characters import Character


class Relationships:
    def __init__(self, source: 'Character'):
        self._source = source
        self._relationships: dict[Character, RelationshipsIndicators] = defaultdict(RelationshipsIndicators)

    def meet(self, character: 'Character', initial_rating: int = 0) -> None:
        if character in self._relationships:
            return
        self._relationships[character] = RelationshipsIndicators(rating=initial_rating)

    def get_indicators(self, character: 'Character') -> RelationshipsIndicators:
        return self._relationships[character]
