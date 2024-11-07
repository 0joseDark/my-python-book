In Python, decorators are a powerful tool that allows you to modify the behavior of functions or classes without changing their code. They are functions that take another function (or method) as an argument and extend or modify its behavior, returning a new function. Decorators are commonly used for logging, access control, memoization, and more.

## How Decorators Work

In Python, functions are first-class objects, meaning they can be passed around as arguments, returned from other functions, and assigned to variables. Decorators make use of this feature by taking a function as input and returning another function that wraps the original one.

### Basic Structure of a Decorator

A decorator is just a function that takes another function as an argument and returns a new function that typically calls the original function:

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()  # Call the original function
        print("Something after the function runs")
    return wrapper
```

### Using a Decorator

To apply a decorator, you can use the `@decorator_name` syntax above the function you want to modify:

```python
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**
```
Something before the function runs
Hello!
Something after the function runs
```

Here’s what happens:
1. `@my_decorator` applies `my_decorator` to `say_hello`.
2. When `say_hello` is called, it’s actually calling `wrapper`, which prints additional lines before and after running the original function.

### Example 1: Logging Decorator

A decorator for logging function calls can be useful for debugging.

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)
```

**Output:**
```
Calling add with arguments (3, 5) and keyword arguments {}
add returned 8
```

### Example 2: Access Control Decorator

This decorator restricts access to a function based on user role.

```python
def require_admin(func):
    def wrapper(user_role):
        if user_role != 'admin':
            print("Access denied. Admins only.")
            return
        return func(user_role)
    return wrapper

@require_admin
def restricted_area(user_role):
    print("Welcome to the admin area!")

restricted_area('user')  # Output: Access denied. Admins only.
restricted_area('admin')  # Output: Welcome to the admin area!
```

### Example 3: Timing Decorator

This decorator measures how long a function takes to execute, useful for performance profiling.

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Function completed")

slow_function()
```

**Output:**
```
Function completed
slow_function took 2.0001 seconds
```

### Example 4: Caching Decorator

A caching decorator stores results of expensive function calls to avoid recalculating.

```python
def cache(func):
    memo = {}
    def wrapper(*args):
        if args in memo:
            print(f"Returning cached result for {args}")
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result
    return wrapper

@cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Calculated
print(factorial(5))  # Cached result
```

### Using Multiple Decorators

You can stack multiple decorators on a single function, applying them in order from the top down:

```python
@timer
@log_decorator
def multiply(a, b):
    return a * b

multiply(4, 5)
```

In this example, `multiply` is first passed through `log_decorator` and then through `timer`.
