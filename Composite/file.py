from file_system import FileSystem


class File(FileSystem):
    def __init__(self, name: str):
        self.name = name

    def show(self, indent: str = "") -> None:
        print(f"{indent}|---- {self.name}")