from typing import TYPE_CHECKING

from ..errors import IncestForbiddenError, InterspeciesSexForbiddenError, OrientationMismatchError, PaedophiliaProhibitedError
from ..sex.profile import IncestTolerance

if TYPE_CHECKING:
    from ..characters import Character


class SexualConsentChecker:
    def __init__(self, initiator: 'Character', responder: 'Character') -> None:
        self._initiator = initiator
        self._responder = responder

    def validate_sex_initiative(self) -> None:
        if self._is_masturbation():
            return
        self._check_orientation()
        self._check_paedophilia()
        self._check_interspecies()
        self._check_incest()

    def _is_masturbation(self) -> bool:
        return self._initiator == self._responder

    def _check_orientation(self) -> None:
        if self._initiator.profile.sex == self._responder.profile.sex:
            if self._initiator.is_hetero or self._responder.is_hetero:
                raise OrientationMismatchError(self._initiator, self._responder)

    def _check_paedophilia(self) -> None:
        if self._initiator.is_infant or self._responder.is_infant:
            raise PaedophiliaProhibitedError(self._initiator, self._responder)

    def _check_interspecies(self) -> None:
        if self._initiator.__class__ != self._responder.__class__:
            if not self._initiator.profile.interspecies_allowed or not self._responder.profile.interspecies_allowed:
                raise InterspeciesSexForbiddenError(self._initiator, self._responder)

    def _check_incest(self) -> None:
        if self._initiator.is_infant or self._responder.is_infant:
            raise PaedophiliaProhibitedError(self._initiator, self._responder)

        if self._initiator in self._responder.family_members:
            accepted_tolerance: tuple[IncestTolerance, ...]

            if self._initiator.is_sibling(self._responder):
                accepted_tolerance = (IncestTolerance.Allowed, IncestTolerance.OnlySiblings)

            if self._initiator.is_parent_or_child(self._responder):
                accepted_tolerance = (IncestTolerance.Allowed,)

            if (
                self._initiator.profile.incest_tolerance not in accepted_tolerance
                or self._responder.profile.incest_tolerance not in accepted_tolerance
            ):
                raise IncestForbiddenError(self._initiator, self._responder)
