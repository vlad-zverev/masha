from dataclasses import dataclass

from ..sex.consts import MAX_RELATIONSHIPS_RATING, MIN_RELATIONSHIPS_RATING


@dataclass(frozen=True)
class Rating:
    _value: int = 0

    def __repr__(self) -> str:
        return str(self._value)

    def __add__(self, other: int) -> 'Rating':
        return Rating(self._trim_by_limits(self._value + other))

    def __sub__(self, other: int) -> 'Rating':
        return Rating(self._trim_by_limits(self._value - other))

    def _trim_by_limits(self, result: int) -> int:
        if result > MAX_RELATIONSHIPS_RATING:
            return MAX_RELATIONSHIPS_RATING
        if result < MIN_RELATIONSHIPS_RATING:
            return MIN_RELATIONSHIPS_RATING
        return result


INITIAL_RATING = Rating()
