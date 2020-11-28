import unittest
from points import *
import math
# Kod testujący moduł.


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.x = 0
        self.y = 0
        self.P_11 = Point(1, 1)
        self.P_11copy = Point(1, 1)
        self.P_00 = Point(0, 0)
        self.P_0min2 = Point(0, -2)
        self.P_82 = Point(8, 2)
        self.P_35 = Point(3, 5)
        self.P_24 = Point(2, 4)
        self.P_22 = Point(2, 2)
        self.P_min1min3 = Point(-1, -3)

    def test__init__(self):
        self.assertEqual(self.P_11.x, 1)
        self.assertEqual(self.P_82.y, 2)
        self.assertEqual(self.P_min1min3.x, -1)

    def test__str__(self):
        self.assertEqual(str(self.P_min1min3), '(-1, -3)')
        self.assertEqual(str(self.P_35), '(3, 5)')

    def test__repr__(self):
        self.assertEqual("Point"+repr(self.P_min1min3), 'Point(-1, -3)')
        self.assertEqual("Point"+repr(self.P_35), 'Point(3, 5)')

    def test__eq__(self):
        self.assertTrue(self.P_11 == self.P_11copy)
        self.assertFalse(self.P_11 == self.P_82)

    def test__ne__(self):
        self.assertFalse(self.P_11 != self.P_11copy)
        self.assertTrue(self.P_11 != self.P_82)

    def test__add__(self):
        self.assertEqual(self.P_11+self.P_35, Point(4, 6))
        self.assertEqual(self.P_11+self.P_min1min3, self.P_0min2)

    def test__sub__(self):
        self.assertEqual(self.P_11-self.P_35, Point(-2, -4))
        self.assertEqual(self.P_11-self.P_min1min3, self.P_24)

    def test__mul__(self):
        self.assertEqual(self.P_11*self.P_35, 8)
        self.assertEqual(self.P_22*self.P_35, 16)

    def test_cross(self):
        self.assertEqual(self.P_11.cross(self.P_35), 2)
        self.assertEqual(self.P_22.cross(self.P_35), 4)

    def test_length(self):
        self.assertEqual(self.P_11.length(), math.sqrt(2))
        self.assertEqual(self.P_22.length(), math.sqrt(8))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
