
import unittest

from src.app import (
    search_destinations,
    search_hotels,
    calculate_total,
)


class TouristGuideTests(unittest.TestCase):

    def test_search_destinations(self):
        self.assertIn(
            "Marina Beach",
            search_destinations("Chennai")
        )

    def test_search_hotels(self):
        self.assertEqual(
            len(search_hotels("Ooty")),
            1
        )

    def test_calculate_total(self):
        self.assertEqual(
            calculate_total(1500, 3),
            4500
        )

    def test_invalid_duration(self):
        with self.assertRaises(ValueError):
            calculate_total(1500, 0)


if __name__ == "__main__":
    unittest.main()
