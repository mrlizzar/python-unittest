import unittest

def get_value(index,container):
    return container[index]

class TestCase(unittest.TestCase):
    def test_case(self):
        self.assertRaises(IndexError,get_value,7,"klasa4")

    def test_case2(self):
        self.assertRaises(Exception, get_value, 6,"klasa4")

    def test_case3(self):
        with self.assertRaises(IndexError):
            get_value(3,"klasa4")