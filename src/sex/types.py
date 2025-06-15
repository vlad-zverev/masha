from enum import Enum
from typing import NamedTuple


class SexualActType(Enum):
    Masturbation = 0
    Coitus = 1
    Reject = 2


class SexualActResult(NamedTuple):
    type: SexualActType
    relationships_influence: int = 0
