"""
safe_division module WITHOUT exception handling
This version demonstrates what happens when we don't handle division by zero.
This file is for demonstration purposes only to show red light test results.
"""

def safe_division(a, b):
    """
    Division function WITHOUT proper error handling.
    This will raise ZeroDivisionError when b is zero.
    
    Args:
        a: The dividend (numerator)
        b: The divisor (denominator)
    
    Returns:
        The result of a / b
    
    Warning:
        This function does NOT handle division by zero and will crash!
    """
    # Exception handling commented out to demonstrate test failure
    # try:
    return a / b
    # except ZeroDivisionError:
    #     print(f"Warning: Cannot divide {a} by zero. Returning None.")
    #     return None
