# Python Core Concepts - Interview Questions

This document covers fundamental Python concepts, syntax, data types, control flow, functions, and error handling.

## 1. Basics & Syntax

**Q1. What is Python? What are its key features?**
**A:** Python is a high-level, interpreted, general-purpose programming language. Its key features include:
- **Interpreted:** Code is executed line-by-line, which makes debugging easier.
- **Dynamically Typed:** You don't need to declare the variable type; it is determined at runtime.
- **Object-Oriented:** Supports classes, encapsulation, inheritance, and polymorphism.
- **Extensive Standard Library:** Provides modules for everything from regular expressions to web servers.
- **Readable Syntax:** Uses indentation to define code blocks, emphasizing readability.

**Q2. What is the difference between a compiled and an interpreted language?**
**A:** 
- **Compiled:** Source code is translated entirely into machine code before execution (e.g., C, C++). This generally results in faster execution times.
- **Interpreted:** Source code is translated into bytecode or machine code line-by-line during execution (e.g., Python, Ruby). This allows for easier debugging and platform independence but is generally slower. *Note: Python actually compiles code to bytecode first (.pyc files) and then interprets it using the Python Virtual Machine (PVM).*

**Q3. Is Python dynamically typed or statically typed? What does that mean?**
**A:** Python is **dynamically typed**. This means that variable types are checked during execution (runtime), not during compilation. You can reassign a variable to a different data type without errors:
```python
x = 5       # x is an int
x = "Hello" # x is now a string
```

**Q4. What is PEP 8?**
**A:** PEP 8 is the official style guide for Python code. It outlines best practices for writing readable and consistent Python code, covering naming conventions (e.g., `snake_case` for functions/variables, `CamelCase` for classes), indentation (4 spaces), line length (max 79 characters), and more.

## 2. Data Types & Variables

**Q5. What are the built-in data types in Python?**
**A:** 
- **Numeric:** `int`, `float`, `complex`
- **Text:** `str`
- **Sequence:** `list`, `tuple`, `range`
- **Mapping:** `dict`
- **Set:** `set`, `frozenset`
- **Boolean:** `bool`
- **Binary:** `bytes`, `bytearray`, `memoryview`
- **NoneType:** `None`

**Q6. What is the difference between a List and a Tuple?**
**A:**
- **List:** Mutable (can be modified after creation), defined with square brackets `[]`, slightly slower, consumes more memory. Use when data needs to change.
- **Tuple:** Immutable (cannot be modified after creation), defined with parentheses `()`, faster, consumes less memory. Use for fixed collections of items (like coordinates or returning multiple values from a function).

**Q7. What is a dictionary in Python? How is it implemented?**
**A:** A dictionary (`dict`) is an unordered (ordered in Python 3.7+), mutable collection of key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, tuples). Under the hood, dictionaries are implemented using **Hash Tables**, which provides O(1) average time complexity for lookups, insertions, and deletions.

**Q8. What are Sets? When would you use them?**
**A:** A set is an unordered collection of unique elements. It is defined using curly braces `{}` or the `set()` constructor. Sets are highly optimized for checking if a specific element is contained in the set (membership testing, O(1) time complexity). Use sets to remove duplicates from a list or to perform mathematical set operations like union, intersection, and difference.

**Q9. Explain `list` vs `tuple` vs `set` vs `dict` at a glance.**
**A:**
- `list`: Ordered, mutable, allows duplicates. `[1, 2, 2]`
- `tuple`: Ordered, immutable, allows duplicates. `(1, 2, 2)`
- `set`: Unordered, mutable, unique elements only. `{1, 2}`
- `dict`: Ordered (Python 3.7+), mutable, key-value pairs, keys must be unique. `{'a': 1, 'b': 2}`

**Q10. What is type conversion in Python?**
**A:** Converting one data type to another. 
- **Implicit:** Python does it automatically (e.g., adding an `int` and a `float` results in a `float`).
- **Explicit:** Using built-in functions like `int()`, `float()`, `str()`, `list()`, `set()`.

## 3. Operators and Control Flow

**Q11. Explain `is` vs `==` in Python.**
**A:** 
- `==` checks for **value equality**. Do the objects have the same value?
- `is` checks for **identity** (reference equality). Do the variables point to the exact same object in memory?
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b) # True (values are the same)
print(a is b) # False (different objects in memory)
print(a is c) # True (point to the same object)
```

**Q12. How does the `range()` function work?**
**A:** `range(start, stop, step)` generates a sequence of numbers. It is typically used in `for` loops.
- `start`: (Optional, default 0) Starting number.
- `stop`: (Required) Generates numbers up to, but not including, this number.
- `step`: (Optional, default 1) The increment.
`range()` returns a range object (an iterator), not a list, meaning it generates numbers lazily, saving memory.

**Q13. Explain list comprehensions with an example.**
**A:** List comprehensions provide a concise way to create lists. They consist of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses.
```python
# Traditional way:
squares = []
for i in range(10):
    if i % 2 == 0:
        squares.append(i**2)

# List comprehension:
squares = [i**2 for i in range(10) if i % 2 == 0]
```

**Q14. What are `break`, `continue`, and `pass`?**
**A:**
- `break`: Terminates the nearest enclosing loop immediately.
- `continue`: Skips the rest of the code inside the current loop iteration and moves to the next iteration.
- `pass`: A null operation. It does nothing. It's used as a placeholder when a statement is required syntactically but you don't want any command or code to execute (e.g., an empty function or class).

**Q15. Can a `for` loop or `while` loop have an `else` clause?**
**A:** Yes. The `else` block executes *only* if the loop completes normally (i.e., it is not terminated by a `break` statement).
```python
for i in range(5):
    if i == 3:
        break
else:
    print("Loop finished normally") # Won't print because of break
```

## 4. Functions & Scope

**Q16. What is a function in Python? How is it defined?**
**A:** A function is a block of reusable code that performs a specific task. It is defined using the `def` keyword, followed by the function name, parentheses (for optional arguments), and a colon.
```python
def greet(name):
    return f"Hello, {name}"
```

**Q17. Explain `*args` and `**kwargs`.**
**A:** They allow a function to accept a variable number of arguments.
- `*args`: Passes a variable number of non-keyword (positional) arguments to a function. The arguments are gathered into a **tuple**.
- `**kwargs`: Passes a variable number of keyword arguments (key-value pairs) to a function. The arguments are gathered into a **dictionary**.
```python
def func(*args, **kwargs):
    print(args)   # (1, 2)
    print(kwargs) # {'name': 'Alice', 'age': 30}
func(1, 2, name="Alice", age=30)
```

**Q18. What are lambda functions?**
**A:** Lambda functions are small, anonymous (unnamed) functions defined using the `lambda` keyword. They can take any number of arguments but can only have one expression. They are often used as short, throwaway functions (e.g., passing as an argument to `map()`, `filter()`, or `sort()`).
```python
add = lambda x, y: x + y
print(add(2, 3)) # Output: 5
```

**Q19. What are Local and Global variables? (LEGB Rule)**
**A:** Python resolves variable scope using the LEGB rule:
1. **L**ocal: Variables defined within the current function.
2. **E**nclosing: Variables in the local scope of enclosing functions (e.g., nested functions).
3. **G**lobal: Variables defined at the top level of a module.
4. **B**uilt-in: Names preassigned in Python (e.g., `len`, `print`).
If you want to modify a global variable inside a function, you must use the `global` keyword.

**Q20. What is a docstring?**
**A:** A docstring (documentation string) is a multi-line string (enclosed in triple quotes `"""`) placed immediately after a function, class, or module definition to describe what it does. It can be accessed at runtime using the `__doc__` attribute.

## 5. File Handling & Error Handling

**Q21. How do you open a file in Python? What does the `with` statement do?**
**A:** You open a file using the `open()` function. The `with` statement (Context Manager) is the recommended way to handle files because it ensures that the file is automatically closed when the block of code is exited, even if an exception occurs.
```python
with open('file.txt', 'r') as f:
    content = f.read()
```

**Q22. What is the difference between `read()`, `readline()`, and `readlines()`?**
**A:**
- `read()`: Reads the entire file into a single string.
- `readline()`: Reads a single line from the file.
- `readlines()`: Reads all lines and returns a list of strings, where each string is a line.

**Q23. How do you handle exceptions in Python?**
**A:** Exceptions are handled using `try`, `except`, `else`, and `finally` blocks.
- `try`: Code that might raise an exception.
- `except`: Code that executes if an exception occurs in the try block.
- `else`: (Optional) Code that executes if no exception occurs.
- `finally`: (Optional) Code that executes regardless of whether an exception occurred or not (useful for cleanup, like closing connections).
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution complete.")
```

**Q24. Can you catch multiple exceptions in one except block?**
**A:** Yes, by passing a tuple of exceptions to the `except` statement.
```python
try:
    pass
except (TypeError, ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
```

**Q25. How do you raise an exception manually?**
**A:** Using the `raise` keyword.
```python
if age < 0:
    raise ValueError("Age cannot be negative.")
```
