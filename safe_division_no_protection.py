"""
safe_division module WITHOUT division by zero protection.

⚠️ WARNING ⚠️
THIS FILE IS FOR DEMONSTRATION PURPOSES ONLY!
DO NOT USE THIS IN PRODUCTION CODE!

This version is used to demonstrate the RED LIGHT scenario.
When you run tests with this version, they will FAIL with ZeroDivisionError.

This file intentionally removes the fail-safe mechanism to show what happens
when proper error handling is not implemented.

FOR PRODUCTION USE: Use safe_division.py instead, which has proper protection.
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
