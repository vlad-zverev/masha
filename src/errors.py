from typing import TYPE_CHECKING

from .printer import printer

if TYPE_CHECKING:
    from .characters import Character


class LocalError(Exception):
    """Root for custom exceptions"""


class SexForbiddenError(LocalError):
    _type: str = 'some'

    def __init__(self, initiator: 'Character', responder: 'Character'):
        printer.show_error(
            f'{initiator.__class__.__name__} {initiator.name} tried to have sex with {responder.name}, '
            f'which is not allowed by [{self._type}] restrictions',
        )


class OrientationMismatchError(SexForbiddenError):
    _type: str = 'orientation'


class PaedophiliaProhibitedError(SexForbiddenError):
    _type: str = 'paedophilia'


class IncestForbiddenError(SexForbiddenError):
    _type: str = 'incest'


class InterspeciesSexForbiddenError(SexForbiddenError):
    _type: str = 'interspecies sex'


class EmptyFamilyError(LocalError):
    def __init__(self) -> None:
        printer.show_error('Family can be created only with at least one memeber, provided empty parents and children')


class NoSexParticipantsError(LocalError):
    def __init__(self) -> None:
        printer.show_error('Sex can not be started without participants...')
