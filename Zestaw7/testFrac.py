import unittest
from fracs import Frac


# Kod testujący moduł.


class TestFrac(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.fr12 = Frac(1, 2)
        self.fr14 = Frac(1, 4)
        self.fr41 = Frac(4, 1)
        self.fr24 = Frac(2, 4)
        self.fr34 = Frac(3, 4)
        self.fr52 = Frac(5, 2)
        self.fr81 = Frac(8, 1)

    def test__init__(self):
        self.assertEqual(self.fr12.x, 1)
        self.assertEqual(self.fr34.y, 4)
        self.assertEqual(self.fr52.x, 5)

    def test_str(self):
        self.assertEqual(str(Frac(5, 4)), "5/4")
        self.assertEqual(str(Frac(-5, 4)), "-5/4")
        self.assertEqual(str(Frac(0, -4)), "0/-4")
        self.assertEqual(str(Frac(10, 1)), "10")
        self.assertEqual(str(Frac(-10, 1)), "-10")
        self.assertEqual(str(Frac(2.5)), "5/2")

    def test_repr(self):
        self.assertEqual(repr(Frac(5, 4)), "Frac(5, 4)")
        self.assertEqual(repr(Frac(-5, 4)), "Frac(-5, 4)")
        self.assertEqual(repr(Frac(0, -4)), "Frac(0, -4)")
        self.assertEqual(repr(Frac(2.5)), "Frac(5, 2)")

    def test_eq(self):
        self.assertFalse(self.fr12 == self.fr34)
        self.assertTrue(self.fr12 == Frac(1, 2))

    def test_ne(self):
        self.assertTrue(self.fr12 != self.fr34)
        self.assertFalse(self.fr12 != Frac(1, 2))

    def test_lt(self):
        self.assertTrue(self.fr12 < self.fr34)
        self.assertFalse(self.fr12 < Frac(1, 2))

    def test_le(self):
        self.assertTrue(self.fr12 <= self.fr34)
        self.assertFalse(self.fr34 <= self.fr12)
        self.assertTrue(self.fr12 <= Frac(1, 2))

    def test_add(self):
        self.assertEqual(Frac(1, 2)+Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(1, 2)+Frac(1, 10), Frac(12, 20))
        self.assertEqual(Frac(54, 56)+Frac(87, 91), Frac(9786, 5096))
        self.assertEqual(Frac(1, 2)+5, Frac(11, 2))

    def test_sub(self):
        self.assertEqual(Frac(1, 2)-Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(123, 87)-Frac(345, 12), Frac(-28539, 1044))
        self.assertEqual(Frac(0, 2)-Frac(1, 3), Frac(-2, 6))

    def test_rsub(self):
        self.assertEqual(self.fr12, 1 - self.fr12)
        self.assertEqual(self.fr34, 1 - self.fr14)

    def test_mul(self):
        self.assertEqual(Frac(1, 2)*Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(10, 100)*Frac(345, 12), Frac(3450, 1200))
        self.assertEqual(Frac(-10, 10)*Frac(-34, 12), Frac(340, 120))
        self.assertEqual(Frac(1, 2)*5, Frac(5, 2))

    def test_truediv(self):
        try:
            self.fr12 / self.zero
        except Exception as e1:
            self.assertEqual(e1.__class__, ValueError)
        self.assertEqual(5 / self.fr34, Frac(20, 3))
        self.assertEqual(self.fr12 / self.fr34, Frac(4, 6))
        self.assertEqual(self.fr34 / 4, Frac(3, 16))

    def test_rtruediv(self):
        self.assertEqual(self.fr81, 2 / self.fr14)
        self.assertEqual(self.fr41, 2 / self.fr12)

    def test_pos(self):
        self.assertEqual(+Frac(1, 3), Frac(1, 3))
        self.assertEqual(+Frac(-2, 3), Frac(-2, 3))
        self.assertEqual(+Frac(2, -3), Frac(2, -3))

    def test_neg(self):
        self.assertEqual(-Frac(1, 3), Frac(-1, 3))
        self.assertEqual(-Frac(-2, 3), Frac(2, 3))
        self.assertEqual(-Frac(2, -3), Frac(-2, -3))

    def test_invert(self):
        self.assertEqual(~Frac(1, 3), Frac(3, 1))
        self.assertEqual(~Frac(-2, 3), Frac(3, -2))
        self.assertEqual(~Frac(-2, -3), Frac(-3, -2))
        self.assertEqual(~Frac(2, -3), Frac(-3, 2))

    def test_float(self):
        self.assertEqual(round(float(Frac(1, 4)), 2), 0.25)
        self.assertEqual(round(float(Frac(1, 3)), 2), 0.33)
        self.assertEqual(round(float(Frac(1, 3)), 2), 0.33)

    def test_hash(self):
        self.assertEqual(hash(0.5), self.fr12.__hash__())
        self.assertEqual(hash(0.75), self.fr34.__hash__())

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
