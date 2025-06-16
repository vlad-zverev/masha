from ..characters import MaterializedCharacter


class CharactersBehavior:
    def __init__(self, characters: list[MaterializedCharacter]):
        self._characters = characters

    def behave(self) -> None:
        for character in self._characters:
            if character.clicked:
                character.shake()
                character.attack()
            elif character.is_under_mouse():
                character.shake()
                character.defend()
            else:
                character.think()
