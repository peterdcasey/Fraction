"""
    Test code for Fraction class
"""

import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):
    """
        Unit test class for Fraction class
    """

    def setUp(self):
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(1, 4)
        self.f3 = Fraction(1, 4)
        self.f4 = Fraction(-1, 5)
        self.f5 = Fraction(1, -6)
        self.f6 = Fraction(-1, -4)

    def tearDown(self):
        pass

    def test_init(self):
        fail = False
        try:
            f = Fraction(1, 0)
        except ValueError:
            fail = True
        self.assertTrue(fail)
        self.assertTrue(self.f6.num == 1)
        self.assertTrue(self.f6.den == 4)

    def test_add(self):
        self.assertEqual(self.f1 + self.f2, Fraction(3, 4))
        self.assertEqual(self.f3 + self.f6, Fraction(1, 2))
        self.assertEqual(self.f1 + self.f2, Fraction(1, 2))

    def test_eq(self):
        self.assertNotEqual(self.f1, self.f2)
        self.assertEqual(self.f2, self.f3)

    def test_mul(self):
        self.assertEqual(self.f1 * self.f2, Fraction(1, 8))


if __name__ == "__main__":
    unittest.main()
