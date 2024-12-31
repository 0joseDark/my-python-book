### 9.1 Functional Programming

Functional programming is a style that treats computation as the evaluation of mathematical functions and avoids changing state or mutable data. In Python, this is often achieved using functions as first-class citizens (functions that can be passed as arguments, returned from other functions, etc.), along with tools like lambda functions, `map`, `filter`, and `reduce`.

#### Example

```python
# Example using `map`, `filter`, and lambda functions
numbers = [1, 2, 3, 4, 5, 6]

# Double each number in the list
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)

# Filter out even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

# Sum of squares of all numbers
from functools import reduce
sum_of_squares = reduce(lambda x, y: x + y**2, numbers, 0)
print("Sum of Squares:", sum_of_squares)
```

Here:
- `map` applies the lambda function to each item in `numbers`.
- `filter` keeps only even numbers.
- `reduce` applies the lambda cumulatively to get the sum of squares.

---

### 9.2 Generators and Iterators

Generators are special functions that return an iterator with a sequence of values instead of a single value. They use the `yield` keyword to produce a value, which allows for lazy evaluation (computing items one at a time and only as needed).

#### Example

```python
# Generator to yield squares of numbers from 1 up to n
def squares(n):
    for i in range(1, n + 1):
        yield i * i

# Using the generator
for square in squares(5):
    print(square)

# Using an iterator directly
iterator = iter([1, 2, 3])
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
```

With `yield`, `squares` function doesn’t compute all squares at once; it generates each square one at a time.

---

### 9.3 Advanced Exception Handling

Python’s exception handling can go beyond the typical `try-except` blocks. Advanced exception handling includes using `else` with `try`, nesting exceptions, and defining custom exception classes for more complex error handling.

#### Example

```python
class CustomError(Exception):
    """Custom exception class"""
    pass

def risky_operation(n):
    try:
        if n < 0:
            raise CustomError("Negative value error")
        print("Result:", 10 / n)
    except CustomError as ce:
        print("Custom Error:", ce)
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero")
    else:
        print("Operation completed successfully")
    finally:
        print("This always executes")

# Testing the function
risky_operation(2)
risky_operation(0)
risky_operation(-1)
```

Here:
- The `else` block executes only if there were no exceptions.
- The `finally` block always runs, which is useful for cleanup operations.
- `CustomError` demonstrates creating and handling a user-defined exception.

---

### 9.4 Context Managers

Context managers allow you to allocate and release resources precisely when you need to. The most common use case is file handling, but you can also create custom context managers with the `with` statement. Custom context managers use `__enter__` and `__exit__` methods or the `contextlib` module.

#### Example

```python
# Using the built-in file context manager
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# Creating a custom context manager using `contextlib`
from contextlib import contextmanager

@contextmanager
def custom_context():
    print("Entering context")
    yield
    print("Exiting context")

# Using the custom context manager
with custom_context():
    print("Inside context")

# Creating a custom class-based context manager
class MyContext:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")

# Using the class-based context manager
with MyContext() as mc:
    print("Doing work inside context")
```

In this example:
- The `with` statement manages resources safely, releasing them once the block is exited.
- The `contextlib` module provides an easy way to create context managers without defining a full class.
- `__enter__` and `__exit__` manage setup and cleanup.

---

These advanced features allow you to write Python code that’s efficient, clean, and expressive, often making complex operations more manageable.
