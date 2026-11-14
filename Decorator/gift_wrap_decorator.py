from order import Order
from order_decorator import OrderDecorator


class GiftWrapDecorator(OrderDecorator):
    GIFT_WRAP_PRICE = 15000.0

    def __init__(self, wrapped_order: Order) -> None:
        super().__init__(wrapped_order)

    def getDescription(self) -> str:
        return f"{super().getDescription()} + Sovg'a qadoqlash"

    def getPrice(self) -> float:
        return super().getPrice() + self.GIFT_WRAP_PRICE
