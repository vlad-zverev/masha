from ..characters import Character
from ..family import Family
from ..sex.types import SexualActType
from ..utils import (
    DominanceMismatchError,
    IncestForbiddenError,
    InterspeciesSexForbiddenError,
    OrientationMismatchError,
    PaedophiliaProhibitedError,
    SexForbiddenError,
    printer,
)
from .stats import Stats


class SwingerParty:
    def __init__(self) -> None:
        self._participants: set[Character] = set()
        self._stats = Stats()

    def join(self, character: Character) -> None:
        if character.is_infant:
            printer.show_error_bold('Kids not allowed')
            return

        self._participants.add(character)

    def join_family(self, family: Family) -> None:
        for member in family.all_adults:
            self.join(member)

    def leave(self, participant: Character) -> None:
        self._participants.remove(participant)

    def start_group_sex(self) -> None:  # noqa: CCR001 C901
        attempts_tracker: set[tuple[Character, Character]] = set()

        for initiator in self._participants:
            for recipient in self._participants:
                if (recipient, initiator) in attempts_tracker:
                    continue
                try:
                    self._have_sex(initiator, recipient)
                except OrientationMismatchError:
                    self._stats.homo_refused_attempts += 1
                except PaedophiliaProhibitedError:
                    self._stats.paedophilic_incidents += 1
                except IncestForbiddenError:
                    self._stats.incest_refused_attempts += 1
                except InterspeciesSexForbiddenError:
                    self._stats.interspecies_sex_refused_attempts += 1
                except DominanceMismatchError:
                    self._stats.dominance_mismatch_cases += 1
                except SexForbiddenError:
                    self._stats.exotic_things_occurances += 1
                    printer.show_error_bold('Some exotic thing happened')

                attempts_tracker.add((initiator, recipient))

        self._stats.show()

    def _have_sex(self, initiator: 'Character', recipient: 'Character') -> None:
        sex_result = initiator.have_sex_with(recipient)

        match sex_result.type:
            case SexualActType.Masturbation:
                self._stats.masturbations += 1
            case SexualActType.Coitus:
                self._stats.coituses += 1
