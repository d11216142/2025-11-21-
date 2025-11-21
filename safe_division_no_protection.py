"""
safe_division module WITHOUT division by zero protection.

This version is used to demonstrate the RED LIGHT scenario.
When you run tests with this version, they will FAIL.

DO NOT USE THIS IN PRODUCTION - This is for demonstration purposes only!
"""


def safe_division(a, b):
    """
    Division WITHOUT protection - will raise ZeroDivisionError.
    
    This version demonstrates what happens when the fail-safe mechanism is removed.
    
    Args:
        a: The numerator (dividend)
        b: The denominator (divisor)
    
    Returns:
        The result of a / b
    
    Raises:
        ZeroDivisionError: If b is zero (NOT SAFE!)
    """
    # Protection removed - this will crash on division by zero!
    # if b == 0:
    #     return None
    return a / b
