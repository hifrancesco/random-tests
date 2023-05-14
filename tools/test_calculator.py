import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        result = self.calc.addition(4, 3)
        self.assertEqual(result, 7)

    def test_subtraction(self):
        result = self.calc.subtraction(4, 3)
        self.assertEqual(result, 1)

    def test_multiplication(self):
        result = self.calc.multiplication(4, 3)
        self.assertEqual(result, 12)

    def test_division(self):
        result = self.calc.division(4, 2)
        self.assertEqual(result, 2)

    def test_modulus(self):
        result = self.calc.modulus(7, 3)
        self.assertEqual(result, 1)

    def test_exponentiation(self):
        result = self.calc.exponentiation(2, 3)
        self.assertEqual(result, 8)

    def test_floor_division(self):
        result = self.calc.floor_division(7, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()