from collections import defaultdict
from typing import TYPE_CHECKING

from .indicators import RelationshipsIndicators

if TYPE_CHECKING:
    from ..characters import Character


RelationshipsMap = defaultdict['Character', RelationshipsIndicators]
