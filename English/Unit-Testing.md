### 10.1 Introduction to Unit Testing
Unit testing involves testing small, isolated parts of code (usually functions or methods) to ensure they perform as expected. It helps catch bugs early and makes code easier to maintain. A "unit" is the smallest testable part of a program, and unit tests are often automated to validate functionality every time the code is changed.

#### Example:
```python
def add(a, b):
    return a + b

# Unit test for the `add` function
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

### 10.2 Testing with unittest
Python’s `unittest` module provides tools to create and run tests in a more structured way. With `unittest`, tests are organized into classes, each containing methods that test specific aspects of code.

#### Example:
```python
import unittest

def multiply(a, b):
    return a * b

class TestMathOperations(unittest.TestCase):
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 3), -3)
        self.assertEqual(multiply(0, 5), 0)
        
if __name__ == '__main__':
    unittest.main()
```

### 10.3 Debugging with pdb
The Python Debugger (`pdb`) helps developers examine and control code execution, making it easier to find and fix errors. `pdb` provides commands to set breakpoints, step through code, inspect variables, and evaluate expressions during runtime.

#### Example:
```python
import pdb

def divide(a, b):
    pdb.set_trace()  # This sets a breakpoint
    return a / b

result = divide(10, 0)  # This will raise an error, which we can inspect with pdb
```

Using `pdb` commands:
- `n` (next): Execute the next line
- `c` (continue): Continue execution until the next breakpoint
- `p <variable>`: Print the value of `<variable>`

### 10.4 Logging
Logging provides a way to track events that happen while the code runs, often useful for debugging, monitoring applications, and understanding the flow of execution. Python’s `logging` module allows developers to output information to the console, files, or other outputs, with various log levels (e.g., `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

#### Example:
```python
import logging

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

def subtract(a, b):
    logging.debug(f"Subtracting {b} from {a}")
    return a - b

result = subtract(10, 5)
logging.info(f"Result: {result}")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
```

This example demonstrates various logging levels:
- `DEBUG`: Detailed information, typically used for diagnosing problems.
- `INFO`: General information about program execution.
- `WARNING`: An indication of potential issues.
- `ERROR`: A more serious problem that has caused part of the program to fail.
- `CRITICAL`: A severe issue causing the program to stop running.
