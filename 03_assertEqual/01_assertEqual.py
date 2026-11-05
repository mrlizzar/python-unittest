import unittest
class TestClass1(unittest.TestCase):
    def test_case1(self):
        self.assertEqual('aws'.upper(), 'AWS')



    def test_case3(self):
        self.assertEqual('3.9.0'.split('.'),['3','9','0'])



    def test_case5(self):
        self.assertEqual({3,4},{4,3})

    def test_case6(self):
        self.assertNotEqual('agh'.upper(),'agh')