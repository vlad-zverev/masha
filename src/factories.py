from .characters import Beaver
from .family import Family
from .sex.profile import DEFAULT_FEMALE, DEFAULT_MALE, INCEST_FULL_TOLERANT_BI_MALE, SexualProfile


def create_beavers_family() -> Family[Beaver]:
    papa = Beaver('Igor', 6, 15, DEFAULT_MALE)
    mama = Beaver('Helga', 6, 12, DEFAULT_FEMALE)

    daughter = Beaver('Sveta', 4, 5, DEFAULT_FEMALE)
    son = Beaver('Filip', 4, 6, INCEST_FULL_TOLERANT_BI_MALE)
    middle_son = Beaver('Paul', 3, 2, INCEST_FULL_TOLERANT_BI_MALE)
    little_son = Beaver('Boka', 1, 2, INCEST_FULL_TOLERANT_BI_MALE)

    return Family[Beaver](
        parents=[papa, mama],
        children=[daughter, son, middle_son, little_son],
    )
