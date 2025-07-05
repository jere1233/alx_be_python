import unittest
from robust_division_calculator import safe_divide

class TestRobustDivisionCalculator(unittest.TestCase):

    def test_normal_division(self):
        self.assertEqual(safe_divide("10", "5"), "The result of the division is 2.0")

    def test_division_by_zero(self):
        self.assertEqual(safe_divide("10", "0"), "Error: Cannot divide by zero.")

    def test_non_numeric_numerator(self):
        self.assertEqual(safe_divide("ten", "5"), "Error: Please enter numeric values only.")

    def test_non_numeric_denominator(self):
        self.assertEqual(safe_divide("10", "five"), "Error: Please enter numeric values only.")

if __name__ == "__main__":
    unittest.main()
