import unittest


class TestCase(unittest.TestCase):

    def test_case1(self):
        self.assertTrue(isinstance('agh',str))

    def test_case2(self):
        self.assertTrue(isinstance('agh',int))

    def test_case3(self):
        self.assertFalse(isinstance('agh',str))

    def test_case4(self):
        self.assertFalse(isinstance('agh',int))