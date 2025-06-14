from ..characters import Character
from ..errors import IncestForbidden, PaedophiliaProhibited, SexForbidden
from ..family import Family
from ..printer import printer
from .stats import Stats


class SwingerParty:
    def __init__(self) -> None:
        self._participants: set[Character] = set()
        self._stats = Stats()

    def join(self, character: Character) -> None:
        self._participants.add(character)

    def join_family(self, family: Family) -> None:
        for member in family.all_members:
            self._participants.add(member)

    def start_group_sex(self) -> None:
        for dominant in self._participants:
            for submissive in self._participants:
                try:
                    sex_result = dominant.have_sex_with(submissive)

                    if sex_result.success:
                        self._stats.successes += 1
                    if sex_result.is_masturbation:
                        self._stats.masturbations += 1

                except IncestForbidden:
                    self._stats.incest_attempts += 1
                except PaedophiliaProhibited:
                    self._stats.paedophilic_attempts += 1

        printer.show_header(str(self._stats))

    def leave(self, participant: Character) -> None:
        self._participants.remove(participant)
