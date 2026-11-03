import unittest

class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3)