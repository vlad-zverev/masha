from enum import Enum
from typing import Literal, NamedTuple

Sex = Literal['M', 'F']


class SexualOrientation(Enum):
    Hetero = 0
    Homo = 1
    Bi = 2


class IncestTolerance(Enum):
    Forbidden = 0
    OnlySiblings = 1
    Allowed = 2


class DominanceLevel(Enum):
    Dominant = 0
    Submissive = 1
    Neutral = 2


class SexualProfile(NamedTuple):
    sex: Sex
    orientation: SexualOrientation = SexualOrientation.Hetero
    incest_tolerance: IncestTolerance = IncestTolerance.Forbidden
    interspecies_allowed: bool = False
    dominance_level: DominanceLevel = DominanceLevel.Neutral

    @property
    def is_neutral_dominance(self) -> bool:
        return self.dominance_level == DominanceLevel.Neutral
