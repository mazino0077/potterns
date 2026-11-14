from abc import ABC, abstractmethod


class Order(ABC):
    @abstractmethod
    def getDescription(self) -> str:
        pass

    @abstractmethod
    def getPrice(self) -> float:
        pass
