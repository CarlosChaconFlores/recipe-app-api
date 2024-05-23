"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(calc.add(1, 1), 2)

    def test_substract(self):
        res = calc.substract(10, 15)
        self.assertEqual(res, 5)
