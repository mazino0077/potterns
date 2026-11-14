from basic_order import BasicOrder
from express_delivery_decorator import ExpressDeliveryDecorator
from gift_wrap_decorator import GiftWrapDecorator
from order import Order


def main() -> None:
    # Oddiy buyurtma yaratamiz
    order: Order = BasicOrder("Simsiz quloqchin", 350000.0)
    print(f"Tavsif: {order.getDescription()}")
    print(f"Narxi: {order.getPrice()} so'm\n")

    # Sovg'a qadoqlash xizmatini qo'shamiz
    order = GiftWrapDecorator(order)
    print(f"Tavsif: {order.getDescription()}")
    print(f"Narxi: {order.getPrice()} so'm\n")

    # Tezkor yetkazib berish xizmatini ham qo'shamiz
    order = ExpressDeliveryDecorator(order)
    print(f"Tavsif: {order.getDescription()}")
    print(f"Narxi: {order.getPrice()} so'm")


if __name__ == "__main__":
    main()
