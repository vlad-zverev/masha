from typing import TYPE_CHECKING

from ..sex.consts import MAX_RELATIONSHIPS_RATING
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

    def meet(self, character: 'Character', initial_rating: Rating = INITIAL_RATING) -> None:
        if character in self._relationships_map:
            return
        self._relationships_map[character] = RelationshipsIndicators(attraction_level=initial_rating)

    def get_indicators(self, character: 'Character') -> RelationshipsIndicators:
        return self._relationships_map[character]

    def get_view(self) -> str:
        texts: list[str] = []

        for character, indicators in self._relationships_map.items():
            rating_ratio_repr = f'{indicators.attraction_level}/{MAX_RELATIONSHIPS_RATING}'
            family_repr = ' [family]' if self._source.is_relative(character) else ''

            texts.append(f'- finds attracting {character.name} on {rating_ratio_repr}{family_repr}')

        joined_texts = '\n'.join(texts)

        if joined_texts:
            return f'\n{self._source.name} relationships:\n{joined_texts}'
        return f'\n{self._source.name} has no relationships'
