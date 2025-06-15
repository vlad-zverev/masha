import random
from typing import get_args

from ..sex.profile import DominanceLevel, IncestTolerance, Sex, SexualOrientation, SexualProfile
from ..utils.consts import FEMALE_FIRST_NAMES, MALE_FIRST_NAMES
from .base import Character, T_Character


def create_random(type_: type[T_Character]) -> T_Character:  # noqa: CFQ001
    sex: Sex = random.choice(get_args(Sex))

    orientation = random.choice(
        [
            SexualOrientation.Hetero,
            SexualOrientation.Hetero,
            SexualOrientation.Hetero,
            SexualOrientation.Hetero,
            SexualOrientation.Hetero,
            SexualOrientation.Hetero,
            SexualOrientation.Hetero,
            SexualOrientation.Bi,
            SexualOrientation.Bi,
            SexualOrientation.Homo,
        ],
    )

    incest_tolerance = random.choice(
        [
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.Forbidden,
            IncestTolerance.OnlySiblings,
            IncestTolerance.OnlySiblings,
            IncestTolerance.Allowed,
        ],
    )

    interspecies_allowed = random.choice(
        [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True,
        ],
    )

    dominance_level = random.choice(
        [
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Neutral,
            DominanceLevel.Dominant,
            DominanceLevel.Submissive,
        ],
    )

    sex_profile = SexualProfile(
        sex,
        orientation,
        incest_tolerance,
        interspecies_allowed,
        dominance_level,
    )

    names_collection = MALE_FIRST_NAMES if sex == 'M' else FEMALE_FIRST_NAMES

    name = random.choice(names_collection)

    age = int(type_.age_of_consent() * random.random() * 2)

    weight = int(type_.average_weight() * random.random() * 2)

    return type_(
        name,
        age,
        weight,
        sex_profile,
    )
