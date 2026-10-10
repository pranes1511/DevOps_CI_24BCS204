
class HotelBooking:

    def __init__(self):
        self.hotels = {
            "Chennai": 2500,
            "Ooty": 3000,
            "Kodaikanal": 3500
        }

    def display_hotels(self):
        for hotel, price in self.hotels.items():
            print(f"{hotel}: Rs.{price} per night")

    def book_hotel(self, hotel, days):
        if hotel not in self.hotels:
            return "Hotel not found"

        if not isinstance(days, int) or days <= 0:
            return "Invalid number of days"

        total = self.hotels[hotel] * days
        return f"Booking Successful! Total: Rs.{total}"


if __name__ == "__main__":
    booking = HotelBooking()
    booking.display_hotels()
    print(booking.book_hotel("Ooty", 2))
