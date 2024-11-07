In programming, operators are symbols or keywords used to perform operations on variables and values. These operations can include arithmetic, comparisons, logical tests, bit manipulations, and more. Here are the main types of operators with examples in Python:

### 1. **Arithmetic Operators**
   - These perform basic mathematical operations.

   | Operator | Description             | Example                   |
   |----------|-------------------------|---------------------------|
   | `+`      | Addition                | `3 + 2` → `5`            |
   | `-`      | Subtraction             | `5 - 3` → `2`            |
   | `*`      | Multiplication          | `4 * 2` → `8`            |
   | `/`      | Division                | `8 / 2` → `4.0`          |
   | `//`     | Floor Division          | `7 // 2` → `3`           |
   | `%`      | Modulus (remainder)     | `7 % 2` → `1`            |
   | `**`     | Exponentiation          | `3 ** 2` → `9`           |

### 2. **Comparison Operators**
   - These compare two values and return a Boolean result (`True` or `False`).

   | Operator | Description              | Example                   |
   |----------|--------------------------|---------------------------|
   | `==`     | Equal                    | `3 == 3` → `True`        |
   | `!=`     | Not equal                | `3 != 4` → `True`        |
   | `>`      | Greater than             | `5 > 3` → `True`         |
   | `<`      | Less than                | `2 < 5` → `True`         |
   | `>=`     | Greater than or equal to | `3 >= 3` → `True`        |
   | `<=`     | Less than or equal to    | `4 <= 5` → `True`        |

### 3. **Logical Operators**
   - These operators are used for combining conditional statements.

   | Operator | Description      | Example                          |
   |----------|------------------|----------------------------------|
   | `and`    | Logical AND      | `(3 > 2) and (4 > 1)` → `True`  |
   | `or`     | Logical OR       | `(3 < 2) or (4 > 1)` → `True`   |
   | `not`    | Logical NOT      | `not(3 > 2)` → `False`          |

### 4. **Assignment Operators**
   - These are used to assign values to variables and combine them with arithmetic operations.

   | Operator | Description            | Example                    |
   |----------|------------------------|----------------------------|
   | `=`      | Simple assignment      | `x = 5`                   |
   | `+=`     | Add and assign         | `x += 3`  (equivalent to `x = x + 3`) |
   | `-=`     | Subtract and assign    | `x -= 2`  (equivalent to `x = x - 2`) |
   | `*=`     | Multiply and assign    | `x *= 4`  (equivalent to `x = x * 4`) |
   | `/=`     | Divide and assign      | `x /= 2`  (equivalent to `x = x / 2`) |
   | `//=`    | Floor divide and assign| `x //= 2` (equivalent to `x = x // 2`) |
   | `%=`     | Modulus and assign     | `x %= 2`  (equivalent to `x = x % 2`) |
   | `**=`    | Exponent and assign    | `x **= 2` (equivalent to `x = x ** 2`) |

### 5. **Bitwise Operators**
   - These operate on binary representations of integers.

   | Operator | Description        | Example               |
   |----------|--------------------|-----------------------|
   | `&`      | Bitwise AND        | `5 & 3` → `1`        |
   | `|`      | Bitwise OR         | `5 | 3` → `7`        |
   | `^`      | Bitwise XOR        | `5 ^ 3` → `6`        |
   | `~`      | Bitwise NOT        | `~5` → `-6`          |
   | `<<`     | Bitwise left shift | `5 << 1` → `10`      |
   | `>>`     | Bitwise right shift| `5 >> 1` → `2`       |

### 6. **Membership Operators**
   - These check for membership in sequences like strings, lists, or tuples.

   | Operator | Description                | Example                      |
   |----------|----------------------------|------------------------------|
   | `in`     | Returns `True` if exists   | `"a" in "apple"` → `True`    |
   | `not in` | Returns `True` if not exists| `"b" not in "apple"` → `True`|

### 7. **Identity Operators**
   - These check if two variables reference the same object.

   | Operator | Description                  | Example                      |
   |----------|------------------------------|------------------------------|
   | `is`     | Returns `True` if same object| `a is b`                     |
   | `is not` | Returns `True` if not same object | `a is not b`
