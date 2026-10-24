from game_character import GameCharacter


class CharacterFactory:
    def __init__(self, character: GameCharacter):
        self._character = character

    def set_character(self, character: GameCharacter) -> None:
        self._character = character

    def clone_character(self) -> GameCharacter:
        return self._character.clone()