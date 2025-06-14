from typing import TYPE_CHECKING

from ..errors import IncestForbidden, PaedophiliaProhibited
from ..sex.profile import IncestTolerance

if TYPE_CHECKING:
    from ..characters import Character


class SexualConsentChecker:
    def validate_sex_initiative(self, initiator: 'Character', responder: 'Character') -> None:
        if initiator == responder:
            return

        if initiator.is_infant or responder.is_infant:
            raise PaedophiliaProhibited(initiator, responder)

        if initiator in responder.family_members:
            accepted_tolerance: tuple[IncestTolerance, ...]

            if initiator.is_sibling(responder):
                accepted_tolerance = (IncestTolerance.Allowed, IncestTolerance.OnlySiblings)

            if initiator.is_parent_or_child(responder):
                accepted_tolerance = (IncestTolerance.Allowed,)

            if initiator.profile.incest_tolerance not in accepted_tolerance or responder.profile.incest_tolerance not in accepted_tolerance:
                raise IncestForbidden(initiator, responder)


consent_checker = SexualConsentChecker()
