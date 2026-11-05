import unittest


class Person:
    def __init__(self,name):
        self.name = name

class Worker(Person):
    pass

class TestPerson(unittest.TestCase):
    def test_case1(self):
        self.assertIsInstance(Person, type)

    def test_case2(self):
        person = Person("Danuta")
        self.assertIsInstance(person, Person)

class TestWorker(unittest.TestCase):
    def test_case1(self):
        worker = Worker("Janusz")
        self.assertIsInstance(worker, Worker)

    def test_case2(self):
        worker = Worker("Janusz")
        self.assertIsInstance(worker, Person)