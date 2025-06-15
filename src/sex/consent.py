from typing import TYPE_CHECKING

from ..sex.profile import IncestTolerance
from ..utils import (
    DominanceMismatchError,
    IncestForbiddenError,
    InterspeciesSexForbiddenError,
    OrientationMismatchError,
    PaedophiliaProhibitedError,
)

if TYPE_CHECKING:
    from ..characters import Character


class SexualConsentChecker:
    def __init__(self, initiator: 'Character', recipient: 'Character') -> None:
        self._initiator = initiator
        self._recipient = recipient

    def validate_sex_initiative(self) -> None:
        if self._is_masturbation():
            return
        self._check_paedophilia()
        self._check_orientation()
        self._check_dominance()
        self._check_interspecies()
        self._check_incest()

    def _is_masturbation(self) -> bool:
        return self._initiator == self._recipient

    def _check_orientation(self) -> None:
        if self._initiator.profile.sex == self._recipient.profile.sex:
            if self._initiator.is_hetero or self._recipient.is_hetero:
                raise OrientationMismatchError(self._initiator, self._recipient)

    def _check_dominance(self) -> None:
        if not self._initiator.profile.is_matched_dominance_level(self._recipient.profile):
            raise DominanceMismatchError(self._initiator, self._recipient)

    def _check_paedophilia(self) -> None:
        if self._initiator.is_infant or self._recipient.is_infant:
            raise PaedophiliaProhibitedError(self._initiator, self._recipient)

    def _check_interspecies(self) -> None:
        if self._initiator.is_same_species(self._recipient):
            if not self._initiator.profile.interspecies_allowed or not self._recipient.profile.interspecies_allowed:
                raise InterspeciesSexForbiddenError(self._initiator, self._recipient)

    def _check_incest(self) -> None:
        if self._initiator.is_relative(self._recipient):
            accepted_tolerance: tuple[IncestTolerance, ...]

            if self._initiator.is_sibling(self._recipient):
                accepted_tolerance = (IncestTolerance.Allowed, IncestTolerance.OnlySiblings)

            if self._initiator.is_parent_or_child(self._recipient):
                accepted_tolerance = (IncestTolerance.Allowed,)

            if (
                self._initiator.profile.incest_tolerance not in accepted_tolerance
                or self._recipient.profile.incest_tolerance not in accepted_tolerance
            ):
                raise IncestForbiddenError(self._initiator, self._recipient)
