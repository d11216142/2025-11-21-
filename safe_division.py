"""
safe_division module - Provides a division function with zero-division protection.

This module contains the safe_division function that prevents division by zero errors.
"""


def safe_division(a, b):
    """
    Safely divides two numbers with protection against division by zero.
    
    Args:
        a: The numerator (dividend)
        b: The denominator (divisor)
    
    Returns:
        The result of a / b if b is not zero.
        None if b is zero (to prevent ZeroDivisionError).
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(-10, 2)
        -5.0
    """
    if b == 0:
        return None
    return a / b
