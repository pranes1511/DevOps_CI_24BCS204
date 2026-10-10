
import unittest
import sys
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src")
)

from hotel_booking import HotelBooking


class TestHotelBooking(unittest.TestCase):

    def test_booking(self):
        booking = HotelBooking()
        self.assertEqual(
            booking.book_hotel("Ooty", 2),
            "Booking Successful! Total: Rs.6000"
        )

    def test_invalid_hotel(self):
        booking = HotelBooking()
        self.assertEqual(
            booking.book_hotel("Unknown", 2),
            "Hotel not found"
        )


if __name__ == "__main__":
    unittest.main()
