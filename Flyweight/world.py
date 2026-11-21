from typing import List
from block import Block
from block_factory import BlockFactory


class World:
    """O'yin dunyosi: barcha bloklarni saqlaydi va ularni ekranga chiqaradi."""

    def __init__(self) -> None:
        self.blocks: List[Block] = []
        self.factory = BlockFactory()

    def add_block(self, x: int, y: int, z: int, block_type_name: str) -> Block:
        block_type = self.factory.get_block_type(block_type_name)
        block = Block(x, y, z, block_type)
        self.blocks.append(block)
        return block

    def render(self) -> None:
        print("\n=== Minecraft o'yin dunyosi render qilinmoqda ===")
        for block in self.blocks:
            block.render()
        print("================================================")
