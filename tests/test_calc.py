import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(calc.plus(3,5), 8)
    def test_minus(self):
        self.assertEqual(calc.minus(10,3), 7)
    def test_times(self):
        self.assertEqual(calc.times(4,8), 32)
