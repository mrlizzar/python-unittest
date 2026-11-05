import unittest


class TestCase(unittest.TestCase):
    def test_case1(self):
        self.assertGreater(0.2,0.2)

    def test_case3(self):
        self.assertLess(0.3,0.4)

    def test_case2(self):
        self.assertGreaterEqual(0.2,0.2)

    def test_case4(self):
        self.assertLessEqual(0.4,0.4)