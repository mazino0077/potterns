from world import World


def main() -> None:
    world = World()

    world.add_block(0, 0, 0, "Grass")
    world.add_block(1, 0, 0, "Grass")
    world.add_block(2, 0, 0, "Stone")
    world.add_block(3, 0, 0, "Grass")
    world.add_block(4, 0, 0, "Dirt")


    world.render()


    grass_1 = world.blocks[0]
    grass_2 = world.blocks[1]
    stone = world.blocks[2]
    grass_3 = world.blocks[3]

    print("\n=== Xotira va obyektlar tekshiruvi (== operatori) ===")
    print(f"grass_1.block_type == grass_2.block_type : {grass_1.block_type == grass_2.block_type}")
    print(f"grass_1.block_type == grass_3.block_type : {grass_1.block_type == grass_3.block_type}")
    print(f"grass_1.block_type == stone.block_type   : {grass_1.block_type == stone.block_type}")

    total_blocks = len(world.blocks)
    unique_types = world.factory.get_total_types()
    print(f"\nNatija: {total_blocks} ta blok, lekin faqat {unique_types} ta noyob BlockType obyekti.")


if __name__ == "__main__":
    main()
