from typing import TYPE_CHECKING, NamedTuple

from ..errors import NoSexParticipantsError
from ..printer import printer

if TYPE_CHECKING:
    from ..characters import Character


class SexualActResult(NamedTuple):
    success: bool = True
    is_masturbation: bool = False


class SexualAct:
    def __init__(self, *participants: 'Character'):
        if not participants:
            raise NoSexParticipantsError()

        self._participants = list(participants)

    @property
    def is_masturbation(self) -> bool:
        return len(self._participants) == 1 or self._participants[0] == self._participants[-1]

    @property
    def initiator(self) -> 'Character':
        return self._participants[0]

    @property
    def others_repr(self) -> str:
        return ', '.join([ch.name for ch in self._participants[1:]])

    def join(self, character: 'Character') -> None:
        self._participants.append(character)

    def start(self) -> SexualActResult:
        if self.is_masturbation:
            printer.show_ok(f'{self.initiator.name} successfully masturbated')
            return SexualActResult(is_masturbation=True)

        printer.show_bold(f'{self.initiator.name} successfully fucked with {self.others_repr}')
        return SexualActResult()
