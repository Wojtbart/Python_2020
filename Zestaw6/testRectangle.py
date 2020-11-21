from points import Point
from rectangles import Rectangle
import unittest

# Kod testujący moduł.


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rec1 = Rectangle(1, 2, 5, 4)
        self.rec2 = Rectangle(2, 0, 0, 2)
        self.rec3 = Rectangle(1, 1, -1, -1)
        self.rec4 = Rectangle(6, 4, 1, 2)

    def test__init__(self):
        self.assertEqual(self.rec1, Rectangle(1, 2, 5, 4))
        self.assertEqual(self.rec2, Rectangle(2, 0, 0, 2))

    def test__str__(self):
        self.assertEqual(str(self.rec1), "[(1, 2), (5, 4)]")
        self.assertEqual(str(self.rec2), "[(2, 0), (0, 2)]")

    def test__repr__(self):
        self.assertEqual(repr(self.rec1), "Rectangle[(1, 2), (5, 4)]")
        self.assertEqual(repr(self.rec2), "Rectangle[(2, 0), (0, 2)]")

    def test__eq__(self):
        self.assertFalse(self.rec1 == self.rec2)
        self.assertTrue(self.rec1 == self.rec1)

    def test__ne__(self):
        self.assertTrue(self.rec1 != self.rec2)
        self.assertFalse(self.rec1 != self.rec1)

    def test__center(self):
        self.assertEqual(self.rec1.center(), Point(3, 3))
        self.assertEqual(self.rec2.center(), Point(1, 1))

    def test__area(self):
        self.assertEqual(self.rec1.area(), 8)
        self.assertEqual(self.rec2.area(), 4)

    def test__move(self):
        self.assertEqual(self.rec1.move(3, 1), Rectangle(4, 3, 8, 5))
        self.assertEqual(self.rec2.move(-1, 2), Rectangle(1, 2, -1, 4))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
