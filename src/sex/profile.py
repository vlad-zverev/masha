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


class SexualProfile(NamedTuple):
    sex: Sex
    orientation: SexualOrientation = SexualOrientation.Hetero
    incest_tolerance: IncestTolerance = IncestTolerance.Forbidden
    interspecies_allowed: bool = False


DEFAULT_MALE = SexualProfile('M')
DEFAULT_FEMALE = SexualProfile('F')
INCEST_FULL_TOLERANT_BI_MALE = SexualProfile(
    'M',
    incest_tolerance=IncestTolerance.Allowed,
    orientation=SexualOrientation.Bi,
)
