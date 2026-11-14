from order import Order


class OrderDecorator(Order):
    def __init__(self, wrapped_order: Order) -> None:
        self._wrapped_order = wrapped_order

    def getDescription(self) -> str:
        return self._wrapped_order.getDescription()

    def getPrice(self) -> float:
        return self._wrapped_order.getPrice()
