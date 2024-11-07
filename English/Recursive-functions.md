Recursive functions are functions that call themselves in order to solve a problem by breaking it down into smaller, more manageable subproblems. Each call to a recursive function should progress toward a base case, which is a condition that stops the recursion. Without a base case, the recursion would continue indefinitely, potentially causing a stack overflow.

### How Recursive Functions Work

1. **Base Case:** The function stops calling itself when a specific condition is met.
2. **Recursive Case:** The function calls itself with a smaller or simpler version of the original problem.

### Benefits of Recursion
- Simplifies the code for problems that can naturally be divided into subproblems (e.g., factorials, Fibonacci sequences).
- Avoids complex looping structures by delegating the repeated task to recursive calls.

### Example 1: Factorial Function

The factorial of a number \( n \), written as \( n! \), is the product of all positive integers up to \( n \). Factorials are commonly implemented with recursion.

**Definition:**
\[
n! = n \times (n - 1)!
\]
where \( 0! = 1 \) (this is the base case).

**Python Implementation:**

```python
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial(n - 1)
    else:
        return n * factorial(n - 1)
```

**Usage:**

```python
print(factorial(5))  # Output: 120
```

**Explanation:**
- `factorial(5)` calls `factorial(4)`.
- `factorial(4)` calls `factorial(3)`, and so on.
- Eventually, `factorial(1)` returns `1` (base case), which then allows all recursive calls to resolve and return their results.

### Example 2: Fibonacci Sequence

In the Fibonacci sequence, each number is the sum of the two preceding ones, typically starting with 0 and 1.

**Definition:**
\[
F(n) = F(n - 1) + F(n - 2)
\]
where \( F(0) = 0 \) and \( F(1) = 1 \) (base cases).

**Python Implementation:**

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

**Usage:**

```python
print(fibonacci(6))  # Output: 8
```

**Explanation:**
- `fibonacci(6)` calls `fibonacci(5)` and `fibonacci(4)`.
- Each of these calls continues until it reaches the base cases `fibonacci(0)` or `fibonacci(1)`.
  
### Example 3: Sum of a List

A recursive function can also calculate the sum of a list.

**Definition:**
Sum of list \([x_1, x_2, ..., x_n]\) can be calculated as:
\[
\text{sum}(L) = x_1 + \text{sum}(L[1:])
\]
where \(\text{sum}([]) = 0\) (base case).

**Python Implementation:**

```python
def sum_list(lst):
    # Base case: empty list
    if not lst:
        return 0
    # Recursive case: first element + sum of the rest
    else:
        return lst[0] + sum_list(lst[1:])
```

**Usage:**

```python
print(sum_list([1, 2, 3, 4]))  # Output: 10
```

**Explanation:**
- `sum_list([1, 2, 3, 4])` returns `1 + sum_list([2, 3, 4])`.
- This continues until `sum_list([])` is reached, which returns `0`, allowing the function to resolve by adding up all the elements.
