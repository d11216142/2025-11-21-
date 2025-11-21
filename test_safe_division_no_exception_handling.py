"""
Unit tests for safe_division WITHOUT exception handling
This test suite demonstrates what happens when exception handling is removed.
"""

import unittest
from safe_division_no_exception_handling import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function without exception handling"""
    
    def test_normal_division(self):
        """Test normal division with positive numbers"""
        result = safe_division(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_negative_division(self):
        """Test division with negative numbers"""
        result = safe_division(-10, 2)
        self.assertEqual(result, -5.0)
        
        result = safe_division(10, -2)
        self.assertEqual(result, -5.0)
        
        result = safe_division(-10, -2)
        self.assertEqual(result, 5.0)
    
    def test_division_by_zero(self):
        """Test division by zero - This test will FAIL without exception handling"""
        result = safe_division(10, 0)
        self.assertIsNone(result)
    
    def test_zero_divided_by_number(self):
        """Test zero divided by a number"""
        result = safe_division(0, 5)
        self.assertEqual(result, 0.0)
    
    def test_decimal_division(self):
        """Test division with decimal results"""
        result = safe_division(7, 2)
        self.assertEqual(result, 3.5)
    
    def test_large_numbers(self):
        """Test division with large numbers"""
        result = safe_division(1000000, 1000)
        self.assertEqual(result, 1000.0)
    
    def test_small_numbers(self):
        """Test division with small decimal numbers"""
        result = safe_division(0.1, 0.2)
        self.assertAlmostEqual(result, 0.5, places=7)


if __name__ == '__main__':
    unittest.main()
