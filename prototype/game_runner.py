from game_character import GameCharacter
from character_factory import CharacterFactory


class GameRunner:
    @staticmethod
    def main() -> None:

        original = GameCharacter(1, "Arthur", 10, "Excalibur")


        factory = CharacterFactory(original)

        clone1 = factory.clone_character()
        clone2 = factory.clone_character()


        clone1.set_name("Lancelot")
        clone1.set_level(12)
        clone1.set_weapon("Longsword")

        clone2.set_name("Merlin")
        clone2.set_level(20)
        clone2.set_weapon("Magic Staff")


        print("Original :", original)
        print("Clone 1  :", clone1)
        print("Clone 2  :", clone2)

  
        print("\n--- Qo'shimcha talab tekshiruvi ---")
        print("original == clone2 :", original == clone2)  
        print("clone1 == clone2   :", clone1 == clone2)    
        print("original == clone1 :", original == clone1)  


if __name__ == "__main__":
    GameRunner.main()