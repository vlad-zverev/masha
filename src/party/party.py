from ..characters import Character
from ..errors import (
    IncestForbiddenError,
    InterspeciesSexForbiddenError,
    OrientationMismatchError,
    PaedophiliaProhibitedError,
    SexForbiddenError,
)
from ..family import Family
from ..printer import printer
from .stats import Stats


class SwingerParty:
    def __init__(self) -> None:
        self._participants: set[Character] = set()
        self._stats = Stats()

    @property
    def dominants(self) -> list[Character]:
        return [participant for participant in self._participants if participant.profile.is_dominant]

    def join(self, character: Character) -> None:
        self._participants.add(character)

    def join_family(self, family: Family) -> None:
        for member in family.all_members:
            self._participants.add(member)

    def leave(self, participant: Character) -> None:
        self._participants.remove(participant)

    def start_group_sex(self) -> None:  # noqa: CCR001
        attempts_tracker: set[tuple[int, ...]] = set()

        for initiator in self._participants:
            for responder in self._participants:
                if tuple(sorted((id(initiator), id(responder)))) in attempts_tracker:
                    printer.show_ok(f'{initiator.name} and {responder.name} already tried to fuck')
                    continue
                try:
                    self._have_sex(initiator, responder)
                except OrientationMismatchError:
                    self._stats.homo_refused_attempts += 1
                except IncestForbiddenError:
                    self._stats.incest_refused_attempts += 1
                except InterspeciesSexForbiddenError:
                    self._stats.interspecies_sex_refused_attempts += 1
                except PaedophiliaProhibitedError:
                    self._stats.paedophilic_incidents += 1
                except SexForbiddenError:
                    printer.show_error_bolded('Some exotic thing happened')

                attempts_tracker.add(tuple(sorted((id(initiator), id(responder)))))

        self._stats.show()

    def _have_sex(self, dominant: 'Character', submissive: 'Character') -> None:
        sex_result = dominant.have_sex_with(submissive)

        if sex_result.success:
            self._stats.successes += 1
        if sex_result.is_masturbation:
            self._stats.masturbations += 1
