from typing import Dict, Tuple
from block_type import BlockType


class BlockFactory:
    """Flyweight Factory: HashMap (dict) yordamida yagona BlockType obyektlarini yaratadi va keshlaydi."""

    _PRESETS: Dict[str, Tuple[str, str]] = {
        "Grass": ("grass_top.png", "Yashil"),
        "Stone": ("stone.png", "Kulrang"),
        "Dirt": ("dirt.png", "Jigarrang"),
        "Water": ("water_flow.png", "Ko'k"),
    }

    def __init__(self) -> None:
        self._block_types: Dict[str, BlockType] = {}

    def get_block_type(self, name: str) -> BlockType:
        if name not in self._block_types:
            texture, color = self._PRESETS.get(name, (f"{name.lower()}.png", "Standart"))
            self._block_types[name] = BlockType(name, texture, color)
            print(f"[Factory] Yangi BlockType yaratildi: {name}")
        return self._block_types[name]

    def get_total_types(self) -> int:
        return len(self._block_types)
