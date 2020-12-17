import unittest


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise IndexError("Stos jes pełny!!!")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stos jest pusty!!")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(5)

    def test(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(5)
        self.stack.push(8)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.pop(), 8)
        self.stack.push(10)
        self.stack.push(6)
        self.stack.push(7)
        self.stack.push(8)
        self.assertEqual(self.stack.n, 5)
        self.assertTrue(self.stack.is_full())

        try:
            self.stack.push(67)
        except Exception as e:
            self.assertEqual(IndexError, e.__class__)

        self.assertEqual(self.stack.pop(), 8)
        self.assertEqual(self.stack.pop(), 7)
        self.assertEqual(self.stack.pop(), 6)
        self.assertEqual(self.stack.pop(), 10)
        self.assertEqual(self.stack.pop(), 5)

        try:
            self.stack.pop()
        except Exception as e:
            self.assertEqual(IndexError, e.__class__)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
