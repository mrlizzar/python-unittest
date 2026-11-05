import unittest


class TestCase(unittest.TestCase):

    def test_case1(self):
        self.assertIn("@","kliksoft@gmail.com")

    def test_case2(self):
        self.assertIn("C++,""C#","JavaScript","Java","Python")
