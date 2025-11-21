"""
Safe Division Module

This module provides a safe division function that prevents division by zero errors.
"""


def safe_division(a, b):
    """
    Safely divide two numbers, preventing division by zero.
    
    Args:
        a: The numerator (dividend)
        b: The denominator (divisor)
    
    Returns:
        The result of a divided by b, or None if b is zero
    
    Raises:
        ValueError: If the divisor (b) is zero
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero
        >>> safe_division(7, 3)
        2.3333333333333335
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    # Example usage
    print("Testing safe_division function:")
    print(f"safe_division(10, 2) = {safe_division(10, 2)}")
    print(f"safe_division(15, 3) = {safe_division(15, 3)}")
    print(f"safe_division(7, 2) = {safe_division(7, 2)}")
    
    try:
        print(f"safe_division(10, 0) = {safe_division(10, 0)}")
    except ValueError as e:
        print(f"Caught expected error: {e}")
