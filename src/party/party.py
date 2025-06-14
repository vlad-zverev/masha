from ..characters import Character
from ..errors import (
    DominanceMismatchError,
    IncestForbiddenError,
    InterspeciesSexForbiddenError,
    OrientationMismatchError,
    PaedophiliaProhibitedError,
    SexForbiddenError,
)
from ..family import Family
from ..printer import printer
from ..sex.act import SexualActResult
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

    def start_group_sex(self) -> None:  # noqa: CCR001 C901
        attempts_tracker: set[tuple[Character, Character]] = set()

        for initiator in self._participants:
            for responder in self._participants:
                if (responder, initiator) in attempts_tracker:
                    continue
                try:
                    self._have_sex(initiator, responder)
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
                    printer.show_error_bolded('Some exotic thing happened')

                attempts_tracker.add((initiator, responder))

        self._stats.show()

    def _have_sex(self, dominant: 'Character', submissive: 'Character') -> None:
        match dominant.have_sex_with(submissive):
            case SexualActResult.Masturbation:
                self._stats.masturbations += 1
            case SexualActResult.Coitus:
                self._stats.coituses += 1
