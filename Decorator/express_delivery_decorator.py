from order import Order
from order_decorator import OrderDecorator


class ExpressDeliveryDecorator(OrderDecorator):
    EXPRESS_DELIVERY_PRICE = 25000.0

    def __init__(self, wrapped_order: Order) -> None:
        super().__init__(wrapped_order)

    def getDescription(self) -> str:
        return f"{super().getDescription()} + Tezkor yetkazib berish"

    def getPrice(self) -> float:
        return super().getPrice() + self.EXPRESS_DELIVERY_PRICE
