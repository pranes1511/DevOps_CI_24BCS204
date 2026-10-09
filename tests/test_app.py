
import unittest
import sys
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src")
)

from app import add, subtract, divide


class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()