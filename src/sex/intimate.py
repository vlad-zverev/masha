from typing import TYPE_CHECKING

from ..utils import SexForbiddenError
from .act import SexualAct
from .consent import SexualConsentChecker
from .consts import DEFAULT_REJECTED_SEX_RESULT, REJECTED_SEX_RELATIONSHIPS_INFLUENCE
from .finalization import SexFinalization
from .types import SexualActResult, SexualActType

if TYPE_CHECKING:
    from ..characters import Character


class IntimateProcess:
    def __init__(self, initiator: 'Character', recipient: 'Character'):
        self._initiator = initiator
        self._recipient = recipient

        self._consent_checker = SexualConsentChecker(self._initiator, self._recipient)
        self._sexual_act = SexualAct(self._initiator, self._recipient)
        self._sex_finalization = SexFinalization(self._initiator, self._recipient)

    def start(self) -> SexualActResult:
        try:
            self._consent_checker.validate_sex_initiative()
            act_result = self._sexual_act.start()
        except SexForbiddenError:
            act_result = DEFAULT_REJECTED_SEX_RESULT
            raise
        finally:
            self._sex_finalization.finalize(act_result)

        return act_result
