from printer import printer


class IncestForbidden(Exception):
    def __init__(self, dominant: 'Beaver', submissive: 'Beaver'):
        printer.show_error(f'Beaver {dominant.name} tried to have sex with {submissive.name}, which not allowed by out incest restrictions')


class Beaver:
    def __init__(self, name: str, age: int, weight: int, sex: str):
        self.name = name
        self.age = age
        self.weight = weight
        self.sex = sex
        self.children: list[Beaver] = []
        self.parents: list[Beaver] = []
        self.siblings: list[Beaver] = []

    def __str__(self) -> str:
        return f'- {self.name} [{self.sex}] (age: {self.age}, weight: {self.weight})'

    def add_child(self, child: 'Beaver') -> None:
        self.children.append(child)

    def add_parent(self, parent: 'Beaver') -> None:
        self.parents.append(parent)

    def add_sibling(self, sibling: 'Beaver') -> None:
        self.siblings.append(sibling)

    def have_sex_with(self, beaver: 'Beaver') -> None:
        if beaver in self.parents + self.children + self.siblings:
            raise IncestForbidden(self, beaver)
        if self == beaver:
            printer.show_ok(f'{self.name} successfully masturbated')
            return
        printer.show_bold(f'{self.name} successfully fucked {beaver.name}')


class BeaversFamily:
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
                except IncestForbidden:
                    printer.show_error_bolded('Police have been called')


def create_beavers_family() -> BeaversFamily:
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

    return BeaversFamily(beavers=[papa, mama, son, daughter, little_son])


family = create_beavers_family()

family.have_group_sex()
