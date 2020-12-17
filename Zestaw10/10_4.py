import unittest


class Queue:

    def __init__(self, size=5):
        # faktyczny rozmiar tablicy, aby tail i head byly rozne przy pelnej tablicy
        self.n = size + 1
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania(poczatek kolejki)
        self.tail = 0           # pierwsze wolne(koniec kolejki)

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):  # wstaw element
        if self.is_full():
            raise IndexError("Kolejka jest pełna!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):  # pobierz element
        if self.is_empty():
            raise IndexError("Kolejka jest pusta!")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue(5)

    def test(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.put(5)
        self.queue.put(8)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.get(), 5)
        self.queue.put(10)
        self.queue.put(6)
        self.queue.put(7)
        self.queue.put(8)
        self.assertEqual(self.queue.n, 6)
        self.assertTrue(self.queue.is_full())

        try:
            self.queue.put(67)
        except Exception as e:
            self.assertEqual(IndexError, e.__class__)

        self.assertEqual(self.queue.get(), 8)
        self.assertEqual(self.queue.get(), 10)
        self.assertEqual(self.queue.get(), 6)
        self.assertEqual(self.queue.get(), 7)
        self.assertEqual(self.queue.get(), 8)

        try:
            self.queue.get()
        except Exception as e:
            self.assertEqual(IndexError, e.__class__)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
