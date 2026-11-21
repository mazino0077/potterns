class BlockType:
    """Flyweight klassi: barcha bir xil bloklar uchun umumiy (o'zgarmas) ma'lumotlarni saqlaydi."""

    def __init__(self, name: str, texture: str, color: str) -> None:
        self.name = name
        self.texture = texture
        self.color = color

    def render(self, x: int, y: int, z: int) -> None:
        print(
            f"Blok: {self.name:<6} | Koordinata: ({x}, {y}, {z}) | "
            f"Tekstura: {self.texture:<15} | Rang: {self.color}"
        )
