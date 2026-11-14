class HotelBooking:
    def book_hotel(self, city: str, nights: int) -> None:
        print(f"[Mehmonxona] {city} shahridagi mehmonxonadan {nights} kechaga xona bron qilindi.")

    def cancel_hotel(self, city: str, nights: int) -> None:
        print(f"[Mehmonxona] {city} shahridagi mehmonxona xonasi ({nights} kecha) broni bekor qilindi.")
