from collections import defaultdict
from typing import TYPE_CHECKING

from ..sex.consts import MAX_RELATIONSHIPS_RATING
from .indicators import RelationshipsIndicators

if TYPE_CHECKING:
    from ..characters import Character


class RelationshipsMap(defaultdict['Character', RelationshipsIndicators]):
    def get_view(self) -> str:
        texts: list[str] = []

        for character, indicators in self.items():
            rating_ratio_repr = f'{indicators.intimate_rating}/{MAX_RELATIONSHIPS_RATING}'
            family_repr = ' [family]' if indicators.part_of_family else ''

            texts.append(f'- finds attracting {character.name} on {rating_ratio_repr}{family_repr}')

        return '\n'.join(texts)
