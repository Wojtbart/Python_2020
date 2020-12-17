import unittest
import random


class RandomQueue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def insert(self, item):
        self.items.append(item)

    def remove(self):    # zwraca losowy element
        if self.is_empty():
            raise IndexError("Kolejka jest pusta!")
        rand = random.randint(0, len(self.items)-1)

        # teraz zamieniamy self.items[len(self.items)-1] i self.items[rand]
        self.items[len(
            self.items)-1], self.items[rand] = self.items[rand], self.items[len(self.items)-1]
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return False

    def clear(self):     # czyszczenie listy
        self.items.length = 0


class TestRandomQueue(unittest.TestCase):

    def setUp(self):
        self.randQueue = RandomQueue()

    def test(self):
        self.assertTrue(self.randQueue.is_empty())
        self.randQueue.insert(5)
        self.randQueue.insert(8)
        self.assertFalse(self.randQueue.is_empty())
        self.randQueue.insert(10)
        self.randQueue.insert(6)
        self.randQueue.insert(7)
        self.randQueue.insert(8)
        self.assertFalse(self.randQueue.is_full())

        for i in range(5):
            # self.randQueue.remove()
            print("Usuwam:", self.randQueue.remove())

        try:
            self.randQueue.remove()
        except Exception as e:
            self.assertEqual(IndexError, e.__class__)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
