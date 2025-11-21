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
