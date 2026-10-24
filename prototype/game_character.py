from copyable import Copyable


class GameCharacter(Copyable):
    def __init__(self, char_id: int, name: str, level: int, weapon: str):
        self._id = char_id
        self._name = name
        self._level = level
        self._weapon = weapon

   
    def get_id(self) -> int:
        return self._id

    def set_id(self, char_id: int) -> None:
        self._id = char_id

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_level(self) -> int:
        return self._level

    def set_level(self, level: int) -> None:
        self._level = level

    def get_weapon(self) -> str:
        return self._weapon

    def set_weapon(self, weapon: str) -> None:
        self._weapon = weapon


    def clone(self) -> "GameCharacter":
        return GameCharacter(self._id, self._name, self._level, self._weapon)


    def __str__(self) -> str:
        return (
            f"GameCharacter(id={self._id}, name='{self._name}', "
            f"level={self._level}, weapon='{self._weapon}')"
        )