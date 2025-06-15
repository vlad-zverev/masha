from typing import TYPE_CHECKING

from ..utils import NoSexParticipantsError, printer
from .types import SexualActResult, SexualActType

if TYPE_CHECKING:
    from ..characters import Character


class SexualAct:
    def __init__(self, *participants: 'Character'):
        if not participants:
            raise NoSexParticipantsError()

        self._participants = list(participants)
        self._relationships_influence = 10

    @property
    def is_masturbation(self) -> bool:
        return len(self._participants) == 1 or self._participants[0] == self._participants[-1]

    @property
    def is_homo(self) -> bool:
        return self._participants[0].profile.sex == self._participants[-1].profile.sex

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
            printer.show_ok_green(f'{self.initiator.name} successfully masturbated')
            return SexualActResult(type=SexualActType.Masturbation)

        printer.show_bold(f'{"[HOMO] " if self.is_homo else ""}{self.initiator.name} successfully fucked with {self.others_repr}')
        return SexualActResult(type=SexualActType.Coitus, relationships_influence=self._relationships_influence)
