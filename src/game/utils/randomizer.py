import random

from ..types import Coordinates
from ..types.consts import MAX_COORDINATES, MIN_COORDINATES


def get_random_coordinates(
    between_from: Coordinates = MIN_COORDINATES,
    between_to: Coordinates = MAX_COORDINATES,
) -> Coordinates:
    between_from_x, between_from_y = between_from
    between_to_x, between_to_y = between_to

    rand_x = random.randint(between_from_x, between_to_x)
    rand_y = random.randint(between_from_y, between_to_y)

    print('OOO', rand_x, rand_y)

    return rand_x, rand_y
