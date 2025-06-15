from .characters import Beaver, Human, registry
from .family import BeaversFamily, HumansFamily
from .party import SwingerParty
from .sex.consts import DEFAULT_FEMALE, DEFAULT_MALE, INCEST_FULL_TOLERANT_BI_MALE


def create_beavers_family() -> BeaversFamily:
    papa = Beaver('Igor', 6, 15, DEFAULT_MALE)
    mama = Beaver('Helga', 6, 12, DEFAULT_FEMALE)

    daughter = Beaver('Sveta', 4, 5, DEFAULT_FEMALE)
    son = Beaver('Filip', 4, 6, INCEST_FULL_TOLERANT_BI_MALE)
    middle_son = Beaver('Paul', 3, 2, INCEST_FULL_TOLERANT_BI_MALE)
    little_son = Beaver('Boka', 1, 2, INCEST_FULL_TOLERANT_BI_MALE)

    return BeaversFamily(
        parents=[papa, mama],
        children=[daughter, son, middle_son, little_son],
    )


def create_humans_family() -> HumansFamily:
    return HumansFamily(
        parents=[
            Human('Vadim', 30, 100, DEFAULT_MALE),
            Human('Margaret', 38, 66, DEFAULT_FEMALE),
        ],
    )


def create_other_humans_family() -> HumansFamily:
    return HumansFamily(
        parents=[
            Human('Max', 40, 70, INCEST_FULL_TOLERANT_BI_MALE),
            Human('Alla', 38, 66, DEFAULT_FEMALE),
        ],
        children=[
            Human('Egor', 16, 60, INCEST_FULL_TOLERANT_BI_MALE),
        ],
    )


def create_families_and_throw_a_party() -> None:
    beavers_family = create_beavers_family()
    humans_family = create_humans_family()
    other_humans_family = create_other_humans_family()

    party = SwingerParty()

    party.join_family(beavers_family)
    party.join_family(humans_family)
    party.join_family(other_humans_family)

    party.start_group_sex()

    registry.show_all_relationships()
