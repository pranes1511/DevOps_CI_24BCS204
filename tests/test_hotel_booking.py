
import unittest
from unittest.mock import patch
from io import StringIO
import src.hotel_booking as app

class TestHotelBooking(unittest.TestCase):

    def test_hotel_list_not_empty(self):
        self.assertGreater(len(app.hotels), 0)

    def test_hotel_has_required_details(self):
        hotel = app.hotels[0]
        self.assertIn("name", hotel)
        self.assertIn("city", hotel)
        self.assertIn("price", hotel)
        self.assertIn("available", hotel)

    def test_booking_total(self):
        hotel = app.hotels[0]
        self.assertEqual(hotel["price"] * 2, 4000)

    def test_invalid_hotel_number(self):
        with patch("builtins.input", side_effect=["99", "1"]):
            with patch("sys.stdout", new_callable=StringIO) as output:
                app.book_hotel()
                self.assertIn("Invalid hotel number", output.getvalue())

if __name__ == "__main__":
    unittest.main()
