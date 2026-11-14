class FlightBooking:
    def book_flight(self, origin: str, destination: str, date: str) -> None:
        print(f"[Aviachipta] {origin} -> {destination} yo'nalishiga ({date}) aviachipta bron qilindi.")

    def cancel_flight(self, origin: str, destination: str, date: str) -> None:
        print(f"[Aviachipta] {origin} -> {destination} yo'nalishidagi ({date}) aviachipta broni bekor qilindi.")
