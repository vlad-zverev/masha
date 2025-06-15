from abc import ABC, abstractmethod
from typing import TypeVar

from ..relationships import Relationships, RelationshipsIndicators
from ..sex.act import SexualActResult
from ..sex.intimate import IntimateProcess
from ..sex.profile import SexualOrientation, SexualProfile
from .registry import registry

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

        self._relationships = Relationships(self)

        self._children: set[Character] = set()
        self._parents: set[Character] = set()
        self._siblings: set[Character] = set()

        registry.register(self)

    def __str__(self) -> str:
        return f'- {self._name} [{self._profile.sex}] (age: {self._age}, weight: {self._weight})'

    @property
    def name(self) -> str:
        return self._name

    @property
    def profile(self) -> SexualProfile:
        return self._profile

    @property
    def is_adult(self) -> bool:
        return self._age >= self.age_of_consent

    @property
    def is_infant(self) -> bool:
        return not self.is_adult

    @property
    def is_hetero(self) -> bool:
        return self._profile.orientation == SexualOrientation.Hetero

    @property
    def family_members(self) -> set['Character']:
        return self._children.union(self._parents).union(self._siblings)

    @property
    @abstractmethod
    def age_of_consent(self) -> int:
        pass

    def is_sibling(self, other: 'Character') -> bool:
        return other in self._siblings

    def is_parent_or_child(self, other: 'Character') -> bool:
        return other in self._parents or other in self._children

    def is_relative(self, other: 'Character') -> bool:
        return other in self.family_members

    def is_same_species(self, other: 'Character') -> bool:
        return self.__class__ == other.__class__

    def add_child(self, child: 'Character') -> None:
        self._children.add(child)

    def add_parent(self, parent: 'Character') -> None:
        self._parents.add(parent)

    def add_sibling(self, sibling: 'Character') -> None:
        self._siblings.add(sibling)

    def get_relationships_view(self) -> str:
        return self._relationships.get_view()

    def get_relationship_indicators(self, character: 'Character') -> RelationshipsIndicators:
        return self._relationships.get_indicators(character)

    def masturbate(self) -> None:
        self.have_sex_with(self)

    def have_sex_with(self, character: 'Character') -> SexualActResult:
        return IntimateProcess(self, character).start()
