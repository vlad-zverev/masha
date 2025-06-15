from ..characters import MaterializedCharacter


class Spawner:
    def __init__(self, characters: list[MaterializedCharacter]):
        self._characters = characters

    def spawn_random(self) -> None:
        newborn = MaterializedCharacter.get_random_subclass().from_random_soul()

        newborn.move_to_random()

        self._characters.append(newborn)
