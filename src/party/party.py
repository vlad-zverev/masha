from ..characters import Character
from ..errors import SexForbidden
from ..family import Family
from ..printer import printer


class SwingerParty:
    def __init__(self) -> None:
        self._participants: set[Character] = set()

    def join(self, character: Character) -> None:
        self._participants.add(character)

    def join_family(self, family: Family) -> None:
        for member in family.all_members:
            self._participants.add(member)

    def start_group_sex(self) -> None:
        for dominant in self._participants:
            for submissive in self._participants:
                try:
                    dominant.have_sex_with(submissive)
                except SexForbidden:
                    printer.show_error_bolded('Police have been called')

    def leave(self, participant: Character) -> None:
        self._participants.remove(participant)
