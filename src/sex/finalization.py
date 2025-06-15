from typing import TYPE_CHECKING

from .types import SexualActResult

if TYPE_CHECKING:
    from ..characters import Character


class SexFinalization:
    def __init__(self, initiator: 'Character', recipient: 'Character'):
        self._initiator = initiator
        self._recipient = recipient

    def finalize(self, act_result: SexualActResult) -> SexualActResult:
        initiator_to_recipient_indicators = self._initiator.get_relationship_indicators(self._recipient)
        recipient_to_ititiator_indicators = self._recipient.get_relationship_indicators(self._initiator)

        initiator_to_recipient_indicators.intimate_rating += act_result.relationships_influence
        recipient_to_ititiator_indicators.intimate_rating += act_result.relationships_influence

        initiator_to_recipient_indicators.had_sex = True
        recipient_to_ititiator_indicators.had_sex = True

        return act_result
