from collections import defaultdict
from typing import TYPE_CHECKING

from ..sex.consts import MAX_RELATIONSHIPS_RATING
from .indicators import RelationshipsIndicators

if TYPE_CHECKING:
    from ..characters import Character


class RelationshipsMap(defaultdict['Character', RelationshipsIndicators]):
    def __str__(self) -> str:
        texts = [f'- finds attracting {ch.name} on {rel.intimate_rating}/{MAX_RELATIONSHIPS_RATING}' for ch, rel in self.items()]
        return '\n'.join(texts)
