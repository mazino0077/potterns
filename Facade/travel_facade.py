from flight_booking import FlightBooking
from hotel_booking import HotelBooking
from payment import Payment


class TravelFacade:
    def __init__(self) -> None:
        self._flight_booking = FlightBooking()
        self._hotel_booking = HotelBooking()
        self._payment = Payment()

    def book_trip(
        self,
        origin: str,
        destination: str,
        date: str,
        nights: int,
        total_amount: float,
    ) -> None:
        print("=== Sayohatni bron qilish jarayoni boshlandi ===")
        self._flight_booking.book_flight(origin, destination, date)
        self._hotel_booking.book_hotel(destination, nights)
        self._payment.process_payment(total_amount)
        print("=== Sayohat muvaffaqiyatli bron qilindi! ===\n")

    def cancel_trip(
        self,
        origin: str,
        destination: str,
        date: str,
        nights: int,
        total_amount: float,
    ) -> None:
        print("=== Sayohatni bekor qilish jarayoni boshlandi ===")
        self._flight_booking.cancel_flight(origin, destination, date)
        self._hotel_booking.cancel_hotel(destination, nights)
        self._payment.refund_payment(total_amount)
        print("=== Sayohat to'liq bekor qilindi va mablag' qaytarildi! ===")
