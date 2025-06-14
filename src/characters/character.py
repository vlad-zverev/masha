from abc import ABC, abstractmethod
from typing import TypeVar

from ..printer import printer
from ..sex.consent import consent_checker
from ..sex.profile import SexualProfile

T_Character = TypeVar('T_Character', bound='Character')


class Character(ABC):
    def __init__(
        self,
        name: str,
        age: int,
        weight: int,
        profile: SexualProfile,
    ):
        self._name = name
        self._age = age
        self._weight = weight
        self._profile = profile

        self._children: set[Character] = set()
        self._parents: set[Character] = set()
        self._siblings: set[Character] = set()

    def __str__(self) -> str:
        return f'- {self._name} [{self._profile.sex}] (age: {self._age}, weight: {self._weight})'

    @property
    def name(self) -> str:
        return self._name

    @property
    def profile(self) -> SexualProfile:
        return self._profile

    @property
    def family_members(self) -> set['Character']:
        return self._children.union(self._parents).union(self._siblings)

    @property
    def is_infant(self) -> bool:
        return self._age < self.age_of_consent

    @property
    @abstractmethod
    def age_of_consent(self) -> int:
        pass

    def is_sibling(self, other: 'Character') -> bool:
        return other in self._siblings

    def is_parent_or_child(self, other: 'Character') -> bool:
        return other in self._parents or other in self._children

    def add_child(self, child: 'Character') -> None:
        self._children.add(child)

    def add_parent(self, parent: 'Character') -> None:
        self._parents.add(parent)

    def add_sibling(self, sibling: 'Character') -> None:
        self._siblings.add(sibling)

    def have_sex_with(self, character: 'Character') -> None:
        consent_checker.validate_sex_initiative(self, character)

        if self == character:
            printer.show_ok(f'{self._name} successfully masturbated')
            return

        printer.show_bold(f'{self._name} successfully fucked {character._name}')

    def masturbate(self) -> None:
        self.have_sex_with(self)
