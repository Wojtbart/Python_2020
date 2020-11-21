import unittest
from fracs import *

# assertEqual sprawdza pożądany rezultat, metody setUp i tearDown pozwalaja zdefiniowac kod ktory bedzie wykonywany przed i po kazdym tescie


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 1], [1, 18]), [37, 18])
        self.assertEqual(add_frac([-2, 1], [2, 1]), self.zero)

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 3], [1, 2]), [-1, 6])
        self.assertEqual(sub_frac([1, 3], [-1, 3]), [2, 3])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6],)
        self.assertEqual(mul_frac([4, 5], [5, 4]), [1, 1])
        self.assertEqual(mul_frac([1, -2], [-1, 4]), [1, 8])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([2, 10], [1, 12]), [12, 5])
        self.assertEqual(div_frac([2, 3], [5, 6]), [4, 5])

    def test_is_positive(self):
        self.assertEqual(True, is_positive([1, 5]))
        self.assertEqual(False, is_positive([-1, 3]))
        self.assertEqual(False, is_positive([0, 3]))

    def test_is_zero(self):
        self.assertEqual(True, is_zero([0, 3]))
        self.assertEqual(False, is_zero([1, 3]))
        self.assertEqual(False, is_zero([-1, 3]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([-1, 3], [1, 3]), -1)
        self.assertEqual(cmp_frac([1, 3], [1, 3]), 0)
        self.assertEqual(cmp_frac([1, 3], [-1, 3]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 4]), 0.25)
        self.assertEqual(frac2float([1, 2]), 0.5)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
