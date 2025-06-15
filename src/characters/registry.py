from typing import TYPE_CHECKING

from ..utils import printer

if TYPE_CHECKING:
    from .base import Character


class CharactersRegistry:
    def __init__(self) -> None:
        self._registry: set['Character'] = set()

    def register(self, character: 'Character') -> None:
        self._registry.add(character)

    def show_all_relationships(self) -> None:
        for character in self._registry:
            printer.show_ok_blue(
                character.get_relationships_view(),
                with_surrounding_underline=True,
            )


registry = CharactersRegistry()
