# 2025-11-21-

## Safe Division Function

This repository contains a Python implementation of a `safe_division` function that prevents division by zero errors.

### Features

- **Division by zero protection**: Raises a `ValueError` when attempting to divide by zero
- **Comprehensive error handling**: Provides clear error messages
- **Full test coverage**: Includes unit tests for various scenarios

### Usage

```python
from safe_division import safe_division

# Normal division
result = safe_division(10, 2)  # Returns 5.0

# Division by zero (raises ValueError)
try:
    result = safe_division(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Prints: Error: Cannot divide by zero
```

### Running the Code

To run the example:
```bash
python3 safe_division.py
```

To run the tests:
```bash
python3 -m unittest test_safe_division.py -v
```

### Files

- `safe_division.py`: Main module containing the safe division function
- `test_safe_division.py`: Unit tests for the safe division function