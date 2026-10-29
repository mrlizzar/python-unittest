
import unittest

def area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("width and height must be integers or floats")

    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive")

    return width * height


class RectangleTest(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5, 5), 25)


if __name__ == "__main__":
    unittest.main(verbosity=2)
