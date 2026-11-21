from block_type import BlockType


class Block:
    """Kontekst klassi: har bir blokning noyob koordinatalari va umumiy BlockType havolasini saqlaydi."""

    def __init__(self, x: int, y: int, z: int, block_type: BlockType) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.block_type = block_type

    def render(self) -> None:
        self.block_type.render(self.x, self.y, self.z)
