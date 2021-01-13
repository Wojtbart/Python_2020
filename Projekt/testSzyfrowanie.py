import unittest
from szyfrowanie import *


# Kod testujący moduł.
class TestSszyfrowanie(unittest.TestCase):
    def setUp(self):
        self.number1 = 100
        self.number2 = 40
        self.number3 = 683
        self.number4 = 881
        self.number5 = 491
        self.number6 = 71

    def test__gcd(self):
        self.assertEqual(gcd(self.number1, self.number2), 20)
        self.assertEqual(gcd(self.number3, self.number4), 1)
        self.assertEqual(gcd(self.number5, self.number6), 1)

    def test__extGcd(self):
        self.assertEqual(extGcd(self.number1, self.number2), (20, 1, -2))
        self.assertEqual(extGcd(self.number3, self.number4), (1, 396, -307))
        self.assertEqual(extGcd(self.number5, self.number6), (1, -12, 83))

    def test__isPrime(self):
        self.assertFalse(isPrime(self.number1))
        self.assertFalse(isPrime(self.number2))
        self.assertTrue(isPrime(self.number3))
        self.assertTrue(isPrime(self.number4))
        self.assertTrue(isPrime(self.number5))
        self.assertTrue(isPrime(self.number6))

    def test__drawPrimeNumber(self):
        # drawPrime number zwraca liste, więc sprawdza dlugosc listy
        self.assertTrue(len(drawPrimeNumber()), 2)
        self.assertTrue(False if drawPrimeNumber()[
                        0] < 2 and drawPrimeNumber()[0] > 1000 else True)
        self.assertTrue(False if drawPrimeNumber()[
                        0] < 2 and drawPrimeNumber()[0] > 1000 else True)

    # def test__generateKeyPair(self):
    #     self.assertEqual(generateKeyPair(self.number3, self.number4),
    #                      ((432027, 601723), (172563, 601723))) ???????????????

    # def test__encrypt(self):
    #     self.assertEqual(encrypt((68557, 601723), "tekst"),
    #                      555660229530485995187204555660)

    # def test__decrypt(self):
    #     self.assertEqual(decrypt((23357, 601723), 49611814641126308209010496118),
    #                      "tekst")

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
