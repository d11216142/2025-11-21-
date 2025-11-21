"""
safe_division module
This module provides a safe division function that handles division by zero.
"""

def safe_division(a, b):
    """
    Safely divide two numbers with proper error handling.
    
    Args:
        a: The dividend (numerator)
        b: The divisor (denominator)
    
    Returns:
        The result of a / b, or None if b is zero
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
        float | None: The result of a / b as a float if b is not zero.
                      None if b is zero (to prevent ZeroDivisionError).
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(-10, 2)
        -5.0
    """
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Warning: Cannot divide {a} by zero. Returning None.")
        return None
    if b == 0:
        return None
    return a / b
