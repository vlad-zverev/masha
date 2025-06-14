from printer import printer
from errors import IncestForbiddenError


class Character:
    def __init__(self, name: str, age: int, weight: int, sex: str):
        self.name = name
        self.age = age
        self.weight = weight
        self.sex = sex
        self.children: list[Character] = []
        self.parents: list[Character] = []
        self.siblings: list[Character] = []

    def __str__(self) -> str:
        return f'- {self.name} [{self.sex}] (age: {self.age}, weight: {self.weight})'

    def add_child(self, child: 'Character') -> None:
        self.children.append(child)

    def add_parent(self, parent: 'Character') -> None:
        self.parents.append(parent)

    def add_sibling(self, sibling: 'Character') -> None:
        self.siblings.append(sibling)

    def have_sex_with(self, character: 'Character') -> None:
        if character in self.parents + self.children + self.siblings:
            raise IncestForbiddenError(self, character)
        if self == character:
            printer.show_ok(f'{self.name} successfully masturbated')
            return
        printer.show_bold(f'{self.name} successfully fucked {character.name}')


class Family:
    def __init__(self, beavers: list[Beaver]):
        self.beavers = beavers

        printer.show_header(self.show_all())

    def show_all(self) -> str:
        names = [str(beaver) for beaver in self.beavers]
        joined_names = ',\n'.join(names)
        return f'Family conains of:\n{joined_names}'

    def have_group_sex(self) -> None:
        for dominant in self.beavers:
            for submissive in self.beavers:
                try:
                    dominant.have_sex_with(submissive)
                except IncestForbiddenError:
                    printer.show_error_bolded('Police have been called')


def create_beavers_family() -> Family:
    papa = Beaver('Igor', 6, 15, 'M')
    mama = Beaver('Helga', 6, 12, 'F')
    son = Beaver('Filip', 3, 6, 'M')
    daughter = Beaver('Sveta', 4, 5, 'F')
    little_son = Beaver('Boka', 1, 2, 'M')

    papa.add_child(son)
    papa.add_child(little_son)
    papa.add_child(daughter)
    mama.add_child(son)
    mama.add_child(little_son)
    mama.add_child(daughter)
    daughter.add_parent(papa)
    daughter.add_parent(mama)
    daughter.add_sibling(son)
    daughter.add_sibling(little_son)
    son.add_parent(papa)
    son.add_parent(mama)
    son.add_sibling(daughter)
    son.add_sibling(little_son)
    little_son.add_parent(papa)
    little_son.add_parent(mama)
    little_son.add_sibling(daughter)
    little_son.add_sibling(son)

    return Family(beavers=[papa, mama, son, daughter, little_son])


family = create_beavers_family()

family.have_group_sex()
