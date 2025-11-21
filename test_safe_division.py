"""
Unit tests for the safe_division module
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function"""
    
    def test_normal_division(self):
        """Test normal division operations"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(15, 3), 5.0)
        self.assertEqual(safe_division(9, 3), 3.0)
    
    def test_division_with_float(self):
        """Test division with floating point numbers"""
        self.assertAlmostEqual(safe_division(7, 2), 3.5)
        self.assertAlmostEqual(safe_division(10, 3), 3.333333, places=5)
    
    def test_negative_numbers(self):
        """Test division with negative numbers"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_division_by_zero(self):
        """Test that division by zero raises ValueError"""
        with self.assertRaises(ValueError) as context:
            safe_division(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_zero_numerator(self):
        """Test division when numerator is zero"""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, -3), 0.0)


if __name__ == "__main__":
    unittest.main()
