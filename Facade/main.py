from travel_facade import TravelFacade


def main() -> None:
    # ####Asosiy dasturda faqat TravelFacade obyektidan foydalaniladi
    travel_facade = TravelFacade()

    # #### 1. Sayohatni bron qilish
    travel_facade.book_trip(
        origin="toshkent",
        destination="istanbul",
        date="2026-12-10",
        nights=5,
        total_amount=8500000.0,
    )

    # #### Sayohatni bekor qilish
    travel_facade.cancel_trip(
        origin="toshkent",
        destination="istanbul",
        date="2026-12-10",
        nights=5,
        total_amount=8500000.0,
    )


if __name__ == "__main__":
    main()
