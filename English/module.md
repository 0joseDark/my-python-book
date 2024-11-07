In Python, importing modules and creating packages helps in organizing and reusing code effectively. Let’s break down each concept with examples.

### 1. **Importing Modules**

A **module** in Python is simply a file containing Python definitions and statements. It can include functions, variables, and classes. You can import these modules into other scripts to use their functions without rewriting code.

#### Example of Creating and Importing a Module

1. **Create a Module**  
   Suppose we create a file called `math_functions.py` with the following content:

   ```python
   # math_functions.py

   def add(a, b):
       return a + b

   def subtract(a, b):
       return a - b
   ```

2. **Import and Use the Module in Another File**  
   Now, we can create a new file, say `main.py`, and import `math_functions` to use its functions.

   ```python
   # main.py
   import math_functions

   result_add = math_functions.add(5, 3)
   result_subtract = math_functions.subtract(5, 3)
   print("Addition:", result_add)
   print("Subtraction:", result_subtract)
   ```

   **Output:**
   ```
   Addition: 8
   Subtraction: 2
   ```

#### Importing Specific Functions
If you only need certain functions, you can import them directly.

```python
# main.py
from math_functions import add

result = add(5, 3)
print("Addition:", result)
```

### 2. **Creating and Using Packages**

A **package** is a way of organizing multiple modules. It’s essentially a directory with an `__init__.py` file and other modules. This allows you to organize related modules into a single namespace.

#### Example of Creating a Package

1. **Create a Package Directory Structure**  
   Suppose we want a package called `calculator` with modules for basic and advanced operations. Create the following directory structure:

   ```
   calculator/
   ├── __init__.py
   ├── basic.py
   └── advanced.py
   ```

2. **Define Modules in the Package**

   - `basic.py`:

     ```python
     # basic.py

     def add(a, b):
         return a + b

     def subtract(a, b):
         return a - b
     ```

   - `advanced.py`:

     ```python
     # advanced.py

     def multiply(a, b):
         return a * b

     def divide(a, b):
         if b == 0:
             return "Cannot divide by zero"
         return a / b
     ```

3. **Importing and Using the Package**  
   You can now use `calculator` as a package by importing it in a script.

   ```python
   # main.py
   from calculator import basic, advanced

   print("Addition:", basic.add(5, 3))
   print("Subtraction:", basic.subtract(5, 3))
   print("Multiplication:", advanced.multiply(5, 3))
   print("Division:", advanced.divide(5, 3))
   ```

   **Output:**
   ```
   Addition: 8
   Subtraction: 2
   Multiplication: 15
   Division: 1.6666666666666667
   ```

#### Using `__init__.py` to Control Imports
The `__init__.py` file can be used to define what is available when you import the package. For instance, if you want to make `basic` and `advanced` accessible directly, you could add the following to `__init__.py`:

```python
# __init__.py
from .basic import add, subtract
from .advanced import multiply, divide
```

Now you can import directly from `calculator`:

```python
# main.py
from calculator import add, multiply

print("Addition:", add(5, 3))
print("Multiplication:", multiply(5, 3))
```

### Summary
- **Modules** organize code into files you can import.
- **Packages** group related modules, helping manage larger projects.
