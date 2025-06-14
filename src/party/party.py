from ..characters import Character
from ..errors import IncestForbidden, InterspeciesSexProhibited, OrientationMismatch, PaedophiliaProhibited, SexForbidden
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

    def leave(self, participant: Character) -> None:
        self._participants.remove(participant)

    def start_group_sex(self) -> None:  # noqa: CCR001
        for dominant in self._participants:
            for submissive in self._participants:
                try:
                    self._have_sex(dominant, submissive)
                except IncestForbidden:
                    self._stats.incest_refused_attempts += 1
                except PaedophiliaProhibited:
                    self._stats.paedophilic_incidents += 1
                except OrientationMismatch:
                    self._stats.homo_refused_attempts += 1
                except InterspeciesSexProhibited:
                    self._stats.interspecies_sex_refused_attempts += 1
                except SexForbidden:
                    printer.show_error_bolded('Some exotic thing happened')

        self._stats.show()

    def _have_sex(self, dominant: 'Character', submissive: 'Character') -> None:
        sex_result = dominant.have_sex_with(submissive)

        if sex_result.success:
            self._stats.successes += 1
        if sex_result.is_masturbation:
            self._stats.masturbations += 1
