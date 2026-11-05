import unittest

class TestClass1(unittest.TestCase):
    def test_case1(self):
        self.assertEqual("Yaroslav Lukash".split(),
                         ["Yaroslav","Lukash"])

class TestClass2(unittest.TestCase):
    def test_case1(self):
        self.assertEqual("192.168.0.1".split("."),
                         ["192","168","0","1"])

class TestClass3(unittest.TestCase):
    def test_case1(self):
        self.assertEqual("#".join(["Testy","jednostkowe"]),
                         "Testy#jednostkowe")

if __name__ == "__main__":
    unittest.main()