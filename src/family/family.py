from typing import Generic, Optional

from src.printer import printer

from ..characters import T_Character
from ..errors import EmptyFamily, SexForbidden


class Family(Generic[T_Character]):
    def __init__(
        self,
        parents: Optional[list[T_Character]] = None,
        children: Optional[list[T_Character]] = None,
    ):
        if not parents and not children:
            raise EmptyFamily()

        self._parents = parents or []
        self._children = children or []

        self.register_relationships()

        printer.show_header(self.show_all())

    def register_relationships(self) -> None:
        for parent in self._parents:
            for child in self._children:
                parent.add_child(child)
                child.add_parent(parent)

                for sibling in self._children:
                    sibling.add_sibling(child)
                    child.add_sibling(sibling)

    @property
    def all_members(self) -> list[T_Character]:
        return self._parents + self._children

    def show_all(self) -> str:
        names = [str(member) for member in self.all_members]
        joined_names = ',\n'.join(names)
        return f'Family conains of:\n{joined_names}'

    def start_group_sex(self) -> None:
        for dominant in self.all_members:
            for submissive in self.all_members:
                try:
                    dominant.have_sex_with(submissive)
                except SexForbidden:
                    printer.show_error_bolded('Police have been called')
