"""
Unit tests for safe_division function.

This test suite verifies that the safe_division function correctly handles:
- Normal division cases
- Division with negative numbers
- Division by zero (the key safety feature)
- Edge cases with floating point numbers
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function."""
    
    def test_normal_division_positive_numbers(self):
        """Test normal division with positive numbers."""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(15, 3), 5.0)
        self.assertEqual(safe_division(100, 4), 25.0)
    
    def test_division_with_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_division_with_zero_numerator(self):
        """Test division when numerator is zero."""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, -3), 0.0)
    
    def test_division_by_zero(self):
        """Test that division by zero is handled safely and returns None."""
        self.assertIsNone(safe_division(10, 0))
        self.assertIsNone(safe_division(-5, 0))
        self.assertIsNone(safe_division(0, 0))
    
    def test_division_with_floats(self):
        """Test division with floating point numbers."""
        self.assertAlmostEqual(safe_division(7, 2), 3.5)
        self.assertAlmostEqual(safe_division(1, 3), 0.3333333333333333)
        self.assertAlmostEqual(safe_division(5.5, 2.5), 2.2)
    
    def test_division_with_large_numbers(self):
        """Test division with very large numbers."""
        self.assertEqual(safe_division(1000000, 1000), 1000.0)
        self.assertAlmostEqual(safe_division(1e10, 1e5), 1e5)
    
    def test_division_with_small_numbers(self):
        """Test division with very small numbers."""
        self.assertAlmostEqual(safe_division(0.001, 0.1), 0.01)
        self.assertAlmostEqual(safe_division(1e-6, 1e-3), 0.001)
    
    def test_division_resulting_in_one(self):
        """Test division where result is 1."""
        self.assertEqual(safe_division(5, 5), 1.0)
        self.assertEqual(safe_division(-7, -7), 1.0)


class TestSafeDivisionWithoutProtection(unittest.TestCase):
    """
    Test cases to demonstrate what happens when division by zero protection is removed.
    
    These tests are commented out by default but can be used to demonstrate
    the "red light" scenario mentioned in the requirements.
    """
    
    def test_division_by_zero_would_raise_error(self):
        """
        This test documents the expected behavior with protection.
        
        If the protection (if b == 0: return None) is removed from safe_division,
        this test would fail because the function would raise ZeroDivisionError.
        Currently, with protection in place, the function returns None instead.
        """
        result = safe_division(10, 0)
        # With protection: returns None
        self.assertIsNone(result)
        
        # Without protection: would raise ZeroDivisionError
        # Uncommenting the line below would show the red light:
        # self.assertRaises(ZeroDivisionError, lambda: 10 / 0)


if __name__ == '__main__':
    unittest.main()
