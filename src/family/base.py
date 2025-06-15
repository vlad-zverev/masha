from abc import ABC, abstractmethod
from typing import Generic, Optional

from ..characters import T_Character
from ..utils import EmptyFamilyError, printer


class Family(ABC, Generic[T_Character]):
    def __init__(
        self,
        parents: Optional[list[T_Character]] = None,
        children: Optional[list[T_Character]] = None,
    ):
        if not parents and not children:
            raise EmptyFamilyError()

        self._parents = parents or []
        self._children = children or []

        self.register_family_ties()

        printer.show_ok_blue(f'\nNew family of {self.plural_pronunciation}')
        printer.show_header(self.show_all())

    def register_family_ties(self) -> None:
        for parent in self._parents:
            for child in self._children:
                parent.add_child(child)
                child.add_parent(parent)

                for sibling in self._children:
                    if child == sibling:
                        continue  # noqa: WPS220

                    sibling.add_sibling(child)
                    child.add_sibling(sibling)

    @property
    @abstractmethod
    def plural_pronunciation(self) -> str:
        pass

    @property
    def all_members(self) -> list[T_Character]:
        return self._parents + self._children

    @property
    def all_adults(self) -> list[T_Character]:
        return list(filter(lambda member: member.is_adult, self.all_members))

    def show_all(self) -> str:
        names = [str(member) for member in self.all_members]
        joined_names = '\n'.join(names)
        return f'Family contains of:\n\n{joined_names}'
