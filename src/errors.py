from typing import TYPE_CHECKING

from .printer import printer

if TYPE_CHECKING:
    from .characters import Character


class SexForbidden(Exception):
    _type: str = 'some'

    def __init__(self, initiator: 'Character', responder: 'Character'):
        printer.show_error(
            f'{initiator.__class__.__name__} {initiator.name} tried to have sex with {responder.name}, '
            f'which is not allowed by {self._type} restrictions',
        )


class IncestForbidden(SexForbidden):
    _type: str = 'incest'


class PaedophiliaProhibited(SexForbidden):
    _type: str = 'paedophilia'


class EmptyFamily(Exception):
    def __init__(self) -> None:
        printer.show_error('Family can be created only with at least one memeber, provided empty parents and children')


class NoSexParticipants(Exception):
    def __init__(self) -> None:
        printer.show_error('Sex can not be started without participants...')
