from typing import TYPE_CHECKING

from .indicators import RelationshipsIndicators
from .rating import INITIAL_RATING, Rating
from .types import RelationshipsMap

if TYPE_CHECKING:
    from ..characters import Character


class Relationships:
    def __init__(self, source: 'Character'):
        self._source = source
        self._relationships_map: RelationshipsMap = RelationshipsMap(RelationshipsIndicators)

    @property
    def relationships_map(self) -> RelationshipsMap:
        return self._relationships_map

    def get_view(self) -> str:
        return f'\n{self._source.name} relationships:\n{self.relationships_map.get_view()}'

    def meet(self, character: 'Character', initial_rating: Rating = INITIAL_RATING) -> None:
        if character in self._relationships_map:
            return
        self._relationships_map[character] = RelationshipsIndicators(intimate_rating=initial_rating)

    def get_indicators(self, character: 'Character') -> RelationshipsIndicators:
        return self._relationships_map[character]

    def mark_as_part_of_family(self, character: 'Character') -> None:
        self._source.get_relationship_indicators(character).part_of_family = True
        character.get_relationship_indicators(self._source).part_of_family = True
