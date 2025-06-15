from .profile import DominanceLevel, IncestTolerance, SexualOrientation, SexualProfile
from .types import SexualActResult, SexualActType

SUCCESS_SEX_RELATIONSHIPS_INFLUENCE = 10
REJECTED_SEX_RELATIONSHIPS_INFLUENCE = -50
MAX_RELATIONSHIPS_RATING = 100
MIN_RELATIONSHIPS_RATING = -100

DEFAULT_MALE = SexualProfile('M', dominance_level=DominanceLevel.Dominant)
DEFAULT_FEMALE = SexualProfile('F', dominance_level=DominanceLevel.Submissive)
INCEST_FULL_TOLERANT_BI_MALE = SexualProfile(
    'M',
    incest_tolerance=IncestTolerance.Allowed,
    orientation=SexualOrientation.Bi,
)

DEFAULT_REJECTED_SEX_RESULT = SexualActResult(
    type=SexualActType.Reject,
    relationships_influence=REJECTED_SEX_RELATIONSHIPS_INFLUENCE,
)
