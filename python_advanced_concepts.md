# Python Advanced Concepts - Interview Questions

This document covers Object-Oriented Programming (OOP), Decorators, Generators, Iterators, Memory Management, and Concurrency in Python.

## 1. Object-Oriented Programming (OOP)

**Q1. What are the four pillars of OOP?**
**A:**
1. **Encapsulation:** Bundling data (attributes) and methods that operate on the data into a single unit (class) and restricting direct access to some of the object's components (using private/protected access modifiers).
2. **Abstraction:** Hiding complex implementation details and showing only the essential features of an object.
3. **Inheritance:** A mechanism where a new class derives properties and characteristics from an existing class, promoting code reusability.
4. **Polymorphism:** The ability of different objects to respond to the same method call in their own specific way (e.g., method overriding).

**Q2. Explain `__init__` and `self` in Python.**
**A:**
- `__init__` is a special constructor method that is automatically called when an object of the class is instantiated. It is used to initialize the object's attributes.
- `self` represents the instance of the class itself. It binds the attributes with the given arguments and must be the first parameter of any instance method.

**Q3. How do you implement private variables in a Python class?**
**A:** Python does not have strict access modifiers like Java or C++. Instead, it relies on naming conventions:
- **Protected:** Prefix with a single underscore `_var`. (It's a convention indicating it's for internal use, but it can still be accessed).
- **Private:** Prefix with a double underscore `__var`. This invokes **name mangling**, where the interpreter changes the variable name to `_ClassName__var` to make it harder (but not impossible) to access from outside.

**Q4. What is the difference between Class Methods, Static Methods, and Instance Methods?**
**A:**
- **Instance Methods:** Take `self` as the first parameter. They can modify object instance state and class state.
- **Class Methods (`@classmethod`):** Take `cls` as the first parameter instead of `self`. They can modify class state that applies across all instances of the class (e.g., updating a class-level variable or creating alternative constructors).
- **Static Methods (`@staticmethod`):** Don't take `self` or `cls` as the first parameter. They behave like plain functions that happen to live in a class's namespace. They cannot access or modify class or instance state directly.

**Q5. Explain Multiple Inheritance and the MRO (Method Resolution Order).**
**A:** Multiple inheritance is when a class inherits from more than one parent class. When resolving methods or attributes, Python uses the Method Resolution Order (MRO), specifically the C3 linearization algorithm. It searches the class itself first, then goes left-to-right through the base classes specified in the definition, recursively, without repeating classes. You can view the MRO of a class using `ClassName.mro()` or `ClassName.__mro__`.

**Q6. What are Magic/Dunder Methods?**
**A:** "Dunder" stands for "Double Under" (e.g., `__init__`, `__str__`, `__len__`, `__add__`). These special methods allow you to implement operator overloading and define how objects of your custom classes behave with built-in Python operations.
- `__str__(self)`: Defines the informal/readable string representation (called by `print()` and `str()`).
- `__len__(self)`: Defines behavior for the `len()` function.

## 2. Iterators and Generators

**Q7. What is the difference between an Iterable and an Iterator?**
**A:**
- **Iterable:** An object that can be looped over (e.g., lists, strings, tuples). It implements the `__iter__()` method, which returns an Iterator.
- **Iterator:** An object that represents a stream of data. It implements both `__iter__()` and `__next__()` methods. You use `next(iterator)` to get the next item. When no more items are available, it raises a `StopIteration` exception.

**Q8. What is a Generator?**
**A:** A generator is a special type of iterator, defined using a standard function, but instead of returning values, it `yields` them one at a time. It pauses execution until the next value is requested, making it highly memory-efficient for large datasets.
```python
def my_generator():
    yield 1
    yield 2

gen = my_generator()
print(next(gen)) # 1
```

**Q9. Explain the difference between `yield` and `return`.**
**A:**
- `return`: Terminates the function entirely and sends a specified value back to its caller. All local state is destroyed.
- `yield`: Pauses the function, saves all its states (local variables), and later continues from there on successive calls.

## 3. Decorators

**Q10. What is a Decorator? Write an example.**
**A:** A decorator is a design pattern in Python that allows a user to add new functionality to an existing object (typically a function or method) without modifying its structure. Decorators are functions that take another function as an argument and extend its behavior.
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## 4. Memory Management

**Q11. How is memory managed in Python?**
**A:** Memory management in Python involves a private heap containing all Python objects and data structures. The management of this heap is ensured internally by the Python memory manager. Python uses two primary mechanisms:
1. **Reference Counting:** Every object keeps a count of references pointing to it. When an object's reference count drops to zero, the memory is immediately deallocated.
2. **Garbage Collection (GC):** Reference counting cannot handle reference cycles (e.g., object A references object B, and object B references object A). The Garbage Collector runs periodically to find and clean up these cyclic references.

**Q12. What is the Global Interpreter Lock (GIL)?**
**A:** The GIL is a mutex (lock) used in CPython (the standard implementation of Python) that allows only one thread to hold the control of the Python interpreter at any given time. This means that even in a multi-threaded architecture, only one thread can execute Python bytecodes at once.
- **Impact:** It makes standard multithreading ineffective for CPU-bound tasks. However, multithreading is still useful for I/O-bound tasks (like network requests or reading files), because threads release the GIL while waiting for I/O.

## 5. Concurrency and Async

**Q13. What is the difference between Multiprocessing and Multithreading in Python?**
**A:**
- **Multithreading:** Uses `threading` module. Multiple threads run in the same memory space. Good for **I/O-bound** tasks (due to the GIL). Lightweight, shares memory (requires synchronization locks).
- **Multiprocessing:** Uses `multiprocessing` module. Spawns entirely new processes, each with its own memory space and its own Python interpreter/GIL. Good for **CPU-bound** tasks (heavy math, data processing) because it truly achieves parallelism. Heavier, does not share memory natively.

**Q14. What is `asyncio` and how does it differ from multithreading?**
**A:** `asyncio` is a library to write concurrent code using the `async` and `await` syntax. It uses an **event loop** to run asynchronous tasks. It achieves concurrency using a single thread (cooperative multitasking). It is incredibly efficient for network I/O-bound applications (like web servers or web scraping) because context switching is handled at the application level rather than by the OS, making it much lighter than OS threads.
