from order import Order


class BasicOrder(Order):
    def __init__(self, product_name: str, base_price: float) -> None:
        self._product_name = product_name
        self._base_price = base_price

    def getDescription(self) -> str:
        return self._product_name

    def getPrice(self) -> float:
        return self._base_price
