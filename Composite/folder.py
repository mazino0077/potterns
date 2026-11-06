from typing import List
from file_system import FileSystem


class Folder(FileSystem):
    def __init__(self, name: str):
        self.name = name
        self.children: List[FileSystem] = []

    def add(self, item: FileSystem) -> None:
        self.children.append(item)

    def remove(self, item: FileSystem) -> None:
        if item in self.children:
            self.children.remove(item)

    def show(self, indent: str = "") -> None:
        print(f"{indent}Folder: {self.name}")
        for item in self.children:
            item.show(indent + "    ")