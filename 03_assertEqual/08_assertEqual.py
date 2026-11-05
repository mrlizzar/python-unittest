import unittest

class TestClass(unittest.TestCase):
    def test_case1(self):
        self.assertEqual("aws".upper(), "AWS")

    @unittest.skip("Always skiping ..")
    def test_case2(self):
        self.assertEqual("aws".upper(), "AWS")