# Kod testujący moduł.
import unittest
from rectangles import Rectangle
from points import Point


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rec1 = Rectangle(1, 2, 5, 4)
        self.rec2 = Rectangle(0, 2, 2, 4)
        self.rec3 = Rectangle(-1, -1, 1, 1)

    def test_str(self):
        self.assertEqual(str(self.rec1), "[(1, 2), (5, 4)]",)
        self.assertEqual(str(self.rec3), "[(-1, -1), (1, 1)]",)

    def test_repr(self):
        self.assertEqual(repr(self.rec1), "Rectangle(1, 2, 5, 4)")
        self.assertEqual(repr(self.rec3), "Rectangle(-1, -1, 1, 1)")

    def test_eq(self):
        self.assertFalse(self.rec1 == self.rec2)
        self.assertTrue(self.rec3 == self.rec3)
        self.assertTrue(self.rec2 == self.rec2)

    def test_ne(self):
        self.assertTrue(self.rec1 != self.rec2)
        self.assertFalse(self.rec3 != self.rec3)
        self.assertFalse(self.rec2 != self.rec2)

    def test_center(self):
        self.assertEqual(self.rec1.center(), Point(3, 3))
        self.assertEqual(self.rec2.center(), Point(1, 3))

    def test_area(self):
        self.assertEqual(self.rec1.area(), 8)
        self.assertEqual(self.rec2.area(), 4)

    def test_move(self):
        self.assertEqual(self.rec1.move(1, 1), Rectangle(2, 3, 6, 5))
        self.assertEqual(self.rec2.move(0, -1), Rectangle(0, 1, 2, 3))

    def test_intersection(self):
        self.assertEqual(self.rec1.intersection(
            self.rec2), Rectangle(1, 2, 2, 4))

    def test_cover(self):
        self.assertEqual(self.rec1.cover(self.rec2), Rectangle(0, 2, 5, 4))
        self.assertEqual(self.rec1.cover(self.rec3), Rectangle(-1, -1, 5, 4))

    def test_make4(self):
        self.assertEqual(self.rec1.make4(), [Rectangle(1, 2, 3, 3), Rectangle(1, 3, 3, 4), Rectangle(
            3, 2, 5, 3), Rectangle(3, 3, 5, 4)])

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
