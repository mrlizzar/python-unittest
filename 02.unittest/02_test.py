
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

    def test_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, area, '4', 5)
        self.assertRaises(TypeError, area, 4, '5')

    def test_area_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, area, -4, 5)
        self.assertRaises(ValueError, area, 4, -5)

if __name__ == "__main__":
    unittest.main(verbosity=2)
