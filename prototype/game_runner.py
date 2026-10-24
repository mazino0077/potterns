from game_character import GameCharacter
from character_factory import CharacterFactory


class GameRunner:
    @staticmethod
    def main() -> None:
        # 1. Bitta qahramon yaratish
        original = GameCharacter(1, "Arthur", 10, "Excalibur")

        # 2. Uni CharacterFactory ga uzatish
        factory = CharacterFactory(original)

        # 3. Prototipdan ikkita nusxa yaratish
        clone1 = factory.clone_character()
        clone2 = factory.clone_character()

        # 4. Nusxalarning nomi, darajasi va qurolini o'zgartirish
        clone1.set_name("Lancelot")
        clone1.set_level(12)
        clone1.set_weapon("Longsword")

        clone2.set_name("Merlin")
        clone2.set_level(20)
        clone2.set_weapon("Magic Staff")

        # 5. Original qahramon o'zgarmaganini tekshirish
        print("Original :", original)
        print("Clone 1  :", clone1)
        print("Clone 2  :", clone2)

        # Qo'shimcha talab: original == clone natijasi False bo'lishi lozim
        print("\n--- Qo'shimcha talab tekshiruvi ---")
        print("original == clone1 :", original == clone1)  # False
        print("original == clone2 :", original == clone2)  # False
        print("clone1 == clone2   :", clone1 == clone2)    # False


if __name__ == "__main__":
    GameRunner.main()