# MASTER PRACTICE PROBLEMS COLLECTION
# ======================================


# ==================================================
# --- Day1 : fix_me_day1.py ---
# ==================================================

# Debugging Exercise: Day 1
# This file contains several intentional errors. 
# Your task is to find them, fix them, and make the script run successfully!

print("Welcome to the Day 1 Debugging Challenge!)

# 1. Variable Assignment Errors
1st_name = "Alice"
last-name = "Smith"
print(f"User: {1st_name} {last-name}")

# 2. Data Type Errors
age = 25
message = "I am " + age + " years old."
print(message)

# 3. List Errors
favorite_colors = ["Red", "Blue", "Green"
print(favorite_colors)

# 4. Math and Operator Errors
# We want to calculate the average of 3 test scores
score1 = 80
score2 = 90
score3 = 100
average_score = score1 + score2 + score3 / 3
print(f"The average score is: {average_score}")

# 5. Logic error
# Check if the user is an adult
is_adult = Age >= 18
print("Is adult?", is_adult)

print("If you see this, you fixed all the errors! Great job!")


# ==================================================
# --- Day2 : Day2_StarPatterns.py ---
# ==================================================

# Day 2 Star Patterns: common star pattern codes

# 1. Solid square pattern
size = 5
for i in range(size):
    print("* " * size)

print()

# 2. Left-aligned right-angle triangle (increasing)
for i in range(1, 6):
    print("* " * i)

print()

# 3. Left-aligned inverted right-angle triangle
for i in range(5, 0, -1):
    print("* " * i)

print()

# 4. Right-aligned right-angle triangle
n = 5
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

print()

# 5. Right-aligned inverted right-angle triangle
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

print()

# 6. Centered pyramid pattern
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))

print()

# 7. Inverted centered pyramid pattern
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * (2 * i - 1))

print()

# 8. Diamond pattern
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print("  " * (n - i) + "* " * (2 * i - 1))

print()

# 9. Hollow square pattern
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "* ")

print()

# 10. Hollow left-aligned triangle
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("* " + "  " * (i - 2) + "* ")

print()

# 11. Hollow centered pyramid
for i in range(1, n + 1):
    if i == 1:
        print("  " * (n - 1) + "*")
    elif i == n:
        print("* " * (2 * n - 1))
    else:
        print("  " * (n - i) + "* " + "  " * (2 * i - 3) + "* ")

print()

# 12. Hourglass / diamond outline
for i in range(n, 0, -1):
    if i == n:
        print("* " * (2 * i - 1))
    else:
        print("  " * (n - i) + "* " + "  " * (2 * i - 3) + "* ")
for i in range(2, n + 1):
    if i == n:
        print("* " * (2 * i - 1))
    else:
        print("  " * (n - i) + "* " + "  " * (2 * i - 3) + "* ")


# ==================================================
# --- Day2 : fix_me_day2.py ---
# ==================================================

# Debugging Exercise: Day 2
# This file contains intentional logic and syntax errors involving loops and conditionals.
# Find them and fix them!

print("Welcome to the Day 2 Debugging Challenge!")

# 1. Syntax error in if statement
temperature = 30
if temperature > 25
    print("It's a hot day!")
else:
    print("It's not too hot.")

# 2. Infinite Loop Error
# Warning: If you run this without fixing it, press Ctrl+C in your terminal to stop it!
count = 5
while count > 0:
    print("Countdown:", count)
    # Hint: Something is missing here that causes the loop to never end

# 3. Logic Error in loop range
# We want to print numbers from 1 to 5 (inclusive)
print("Numbers 1 to 5:")
for i in range(1, 5):
    print(i)

# 4. Indentation Error
# We want to print the multiplication table for 3
for j in range(1, 6):
result = 3 * j
print(f"3 x {j} = {result}")

# 5. Logic error in condition order
# We want to print "Fizz" for multiples of 3, "Buzz" for 5, and "FizzBuzz" for both (like 15).
# Right now, 15 is printing "Fizz". Fix the logic!
num = 15
if num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
else:
    print(num)

print("If you see this and the outputs look correct, you fixed all the errors! Great job!")


# ==================================================
# --- Day3 : Day3_Practice_Problems.py ---
# ==================================================

# Day 3: 50 Basic Practice Problems and Solutions
# Topics: Strings, Lists, Loop Control, Functions, Scope, and Recursion

# ==========================================
# SECTION 1: STRING OPERATIONS (1 - 10)
# ==========================================

# 1. Print the first character of the string "Python".
s1 = "Python"
print("1.", s1[0])

# 2. Print the last character of the string "Data" using negative indexing.
s2 = "Data"
print("2.", s2[-1])

# 3. Slice the first 3 characters from "Programming".
s3 = "Programming"
print("3.", s3[0:3])

# 4. Reverse the string "Hello" using slicing.
s4 = "Hello"
print("4.", s4[::-1])

# 5. Concatenate "Good" and "Morning" with a space in between.
print("5.", "Good" + " " + "Morning")

# 6. Repeat the string "Hi" 4 times.
print("6.", "Hi" * 4)

# 7. Print the characters from index 2 to 5 in "Developer".
s7 = "Developer"
print("7.", s7[2:6])

# 8. Use negative slicing to get the last two characters of "World".
s8 = "World"
print("8.", s8[-2:])

# 9. Extract every second character from "abcdefgh".
s9 = "abcdefgh"
print("9.", s9[::2])

# 10. Check the length of the string "OpenAI" using len().
s10 = "OpenAI"
print("10.", len(s10))

# ==========================================
# SECTION 2: LIST OPERATIONS (11 - 20)
# ==========================================

# 11. Create a list of 3 colors and print the second color.
colors = ["Red", "Green", "Blue"]
print("11.", colors[1])

# 12. Print the last element of [10, 20, 30, 40] using negative indexing.
nums12 = [10, 20, 30, 40]
print("12.", nums12[-1])

# 13. Slice the middle two elements from [1, 2, 3, 4].
nums13 = [1, 2, 3, 4]
print("13.", nums13[1:3])

# 14. Reverse the list [1, 2, 3, 4, 5] using slicing.
nums14 = [1, 2, 3, 4, 5]
print("14.", nums14[::-1])

# 15. Concatenate two lists: [1, 2] and [3, 4].
print("15.", [1, 2] + [3, 4])

# 16. Extract the first 3 elements of [10, 20, 30, 40, 50].
nums16 = [10, 20, 30, 40, 50]
print("16.", nums16[:3])

# 17. Extract all elements except the first and last in [10, 20, 30, 40].
nums17 = [10, 20, 30, 40]
print("17.", nums17[1:-1])

# 18. Repeat the list [0] 5 times.
print("18.", [0] * 5)

# 19. Find the length of the list [5, 10, 15, 20, 25].
nums19 = [5, 10, 15, 20, 25]
print("19.", len(nums19))

# 20. Slice the last three elements of [1, 2, 3, 4, 5, 6].
nums20 = [1, 2, 3, 4, 5, 6]
print("20.", nums20[-3:])


# ==========================================
# SECTION 3: LOOP CONTROL & EXCEPTIONS (21 - 30)
# ==========================================

# 21. Write a for loop from 1 to 5, but break when reaching 3.
print("21.")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# 22. Write a for loop from 1 to 4, and skip 2 using continue.
print("22.")
for i in range(1, 5):
    if i == 2:
        continue
    print(i)

# 23. Create an empty for loop using pass.
for i in range(3):
    pass
print("23. Empty loop executed with pass.")

# 24. Write a while loop from 1 to 5, breaking if the number is 4.
print("24.")
w24 = 1
while w24 <= 5:
    if w24 == 4:
        break
    print(w24)
    w24 += 1

# 25. Use a while loop to print 1 to 4, but skip 3.
print("25.")
w25 = 0
while w25 < 4:
    w25 += 1
    if w25 == 3:
        continue
    print(w25)

# 26. Write an if-statement that uses pass.
if True:
    pass
print("26. If-statement executed with pass.")

# 27. Intentionally cause an IndexError and catch it with try/except.
print("27.")
try:
    print([1, 2][5])
except IndexError as e:
    print("Caught:", e)

# 28. Print characters in "Cat", break if 'a' is found.
print("28.")
for char in "Cat":
    if char == 'a':
        break
    print(char)

# 29. Print characters in "Dog", continue if 'o' is found.
print("29.")
for char in "Dog":
    if char == 'o':
        continue
    print(char)

# 30. Access a string out of bounds and catch IndexError.
print("30.")
try:
    print("Hi"[10])
except IndexError:
    print("String index out of range!")


# ==========================================
# SECTION 4: FUNCTIONS (31 - 40)
# ==========================================

# 31. Write a function that prints "Hello, World!" and call it.
print("31.")
def say_hello():
    print("Hello, World!")
say_hello()

# 32. Write a function that takes a name and prints a greeting.
print("32.")
def greet(name):
    print(f"Hi, {name}!")
greet("Venkatesh")

# 33. Write a function that returns the sum of two numbers.
print("33.")
def add(a, b):
    return a + b
print(add(5, 7))

# 34. Write a function with a default parameter for message.
print("34.")
def show_msg(msg="Default message"):
    print(msg)
show_msg()
show_msg("Custom message")

# 35. Write a function that returns the square of a number.
print("35.")
def square(n):
    return n * n
print(square(4))

# 36. Write a function that accepts *args and returns their sum.
print("36.")
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4, 5))

# 37. Write a function that accepts **kwargs and prints them.
print("37.")
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Alice", age=25)

# 38. Write a function with both positional and *args.
print("38.")
def show_first_and_rest(first, *rest):
    print("First:", first, "Rest:", rest)
show_first_and_rest(10, 20, 30, 40)

# 39. Write a function that returns the first character of a string.
print("39.")
def first_char(s):
    return s[0]
print(first_char("Python"))

# 40. Write a function that checks if a list is empty.
print("40.")
def is_empty(lst):
    return len(lst) == 0
print(is_empty([]))


# ==========================================
# SECTION 5: VARIABLE SCOPE (41 - 45)
# ==========================================

# 41. Define a global variable and access it inside a function.
print("41.")
g_var = 100
def access_global():
    print(g_var)
access_global()

# 42. Define a local variable and print it inside the function.
print("42.")
def access_local():
    l_var = 50
    print(l_var)
access_local()

# 43. Modify a global variable inside a function using the 'global' keyword.
print("43.")
count = 0
def increment():
    global count
    count += 1
increment()
print(count)

# 44. Create a local variable with the same name as a global variable.
print("44.")
x = "Global"
def shadow_var():
    x = "Local"
    print("Inside:", x)
shadow_var()
print("Outside:", x)

# 45. Demonstrate that a local variable is destroyed after function exits.
print("45.")
def temp_func():
    temp_var = 99
# temp_var is not accessible here
print("temp_var is only accessible inside temp_func")


# ==========================================
# SECTION 6: RECURSION (46 - 50)
# ==========================================

# 46. Write a recursive function to print numbers from N down to 1.
print("46.")
def countdown(n):
    if n <= 0:
        return
    print(n, end=" ")
    countdown(n - 1)
countdown(3)
print()

# 47. Write a recursive function to calculate the factorial of N.
print("47.")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(4))

# 48. Write a recursive function to find the sum of numbers from 1 to N.
print("48.")
def sum_n(n):
    if n <= 1:
        return 1
    return n + sum_n(n - 1)
print(sum_n(5))

# 49. Write a recursive function to find the Nth Fibonacci number.
print("49.")
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print("Fib(5) =", fibonacci(5))

# 50. Write a recursive function to reverse a string.
print("50.")
def reverse_str(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_str(s[:-1])
print(reverse_str("hello"))

# --- End of Practice Problems ---


# ==================================================
# --- Day3 : Day3_Test_Driven_Practice.py ---
# ==================================================

# Day 3: Test-Driven Practice
# Complete the functions below so that all assert statements pass!

def find_max_in_list(lst):
    """
    Return the maximum number in the list without using the built-in max() function.
    """
    # YOUR CODE HERE
    pass

def remove_duplicates(lst):
    """
    Return a new list with duplicates removed, preserving the original order.
    """
    # YOUR CODE HERE
    pass

def sum_even_numbers(lst):
    """
    Return the sum of all even numbers in the list.
    """
    # YOUR CODE HERE
    pass

# ==========================================
# 🛑 DO NOT MODIFY THE CODE BELOW THIS LINE 
# ==========================================
if __name__ == "__main__":
    print("Running tests...")
    
    # Test find_max_in_list
    try:
        assert find_max_in_list([1, 5, 3, 9, 2]) == 9
        assert find_max_in_list([-10, -5, -20]) == -5
        print("✅ find_max_in_list tests passed!")
    except AssertionError:
        print("❌ find_max_in_list tests failed!")

    # Test remove_duplicates
    try:
        assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
        assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]
        print("✅ remove_duplicates tests passed!")
    except AssertionError:
        print("❌ remove_duplicates tests failed!")

    # Test sum_even_numbers
    try:
        assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
        assert sum_even_numbers([1, 3, 5]) == 0
        print("✅ sum_even_numbers tests passed!")
    except AssertionError:
        print("❌ sum_even_numbers tests failed!")

    print("Test run complete.")


# ==================================================
# --- Day4 : Day4_Practice_Problems.py ---
# ==================================================

# Day 4: 50 Basic Practice Problems and Solutions
# Topics: String Methods, Anagrams, Recursion

# ==========================================
# SECTION 1: STRING METHODS (1 - 20)
# ==========================================

# 1. Convert the string "hello" to uppercase.
print("1.", "hello".upper())

# 2. Convert the string "WORLD" to lowercase.
print("2.", "WORLD".lower())

# 3. Remove the leading and trailing spaces from "  python  ".
print("3.", "  python  ".strip())

# 4. Remove the trailing spaces from "data   ".
print("4.", "data   ".rstrip())

# 5. Replace "cat" with "dog" in the string "The cat sat".
print("5.", "The cat sat".replace("cat", "dog"))

# 6. Split the string "a,b,c,d" by comma.
print("6.", "a,b,c,d".split(","))

# 7. Split the string "Hello World" by space.
print("7.", "Hello World".split())

# 8. Join the list ["a", "b", "c"] with a dash "-".
print("8.", "-".join(["a", "b", "c"]))

# 9. Find the index of "y" in "Python".
print("9.", "Python".find("y"))

# 10. Check if the string "12345" consists only of digits.
print("10.", "12345".isdigit())

# 11. Check if the string "hello" consists only of alphabetic characters.
print("11.", "hello".isalpha())

# 12. Count the number of 'a's in "banana".
print("12.", "banana".count("a"))

# 13. Convert "this is a title" to title case.
print("13.", "this is a title".title())

# 14. Check if "Hello World" starts with "Hello".
print("14.", "Hello World".startswith("Hello"))

# 15. Check if "report.pdf" ends with ".pdf".
print("15.", "report.pdf".endswith(".pdf"))

# 16. Replace all spaces in "a b c" with underscores.
print("16.", "a b c".replace(" ", "_"))

# 17. Find the index of 'z' in "hello". (Should return -1).
print("17.", "hello".find("z"))

# 18. Split the string "apple-orange-grape" by "-".
print("18.", "apple-orange-grape".split("-"))

# 19. Join ["I", "love", "Python"] with spaces.
print("19.", " ".join(["I", "love", "Python"]))

# 20. Count how many times "in" appears in "interesting".
print("20.", "interesting".count("in"))

# ==========================================
# SECTION 2: ANAGRAM LOGIC (21 - 30)
# ==========================================

# 21. Check if "cat" and "act" are anagrams using sorting.
print("21.", sorted("cat") == sorted("act"))

# 22. Check if "hello" and "olleh" are anagrams.
print("22.", sorted("hello") == sorted("olleh"))

# 23. Do "test" and "tast" match using sorting?
print("23.", sorted("test") == sorted("tast"))

# 24. Write a snippet to sort characters in the string "python".
print("24.", sorted("python"))

# 25. Check anagram ignoring spaces: "dormitory" and "dirty room".
s1 = "dormitory".replace(" ", "")
s2 = "dirty room".replace(" ", "")
print("25.", sorted(s1) == sorted(s2))

# 26. Count the frequency of characters in "apple" using a dictionary.
freq = {}
for char in "apple":
    freq[char] = freq.get(char, 0) + 1
print("26.", freq)

# 27. Compare character frequencies of "tea" and "eat".
freq1 = {'t':1, 'e':1, 'a':1}
freq2 = {'e':1, 'a':1, 't':1}
print("27.", freq1 == freq2)

# 28. If len(s1) != len(s2), can they be anagrams?
print("28.", "False, they must be the same length.")

# 29. Check anagram ignoring case: "Tea" and "Eat".
print("29.", sorted("Tea".lower()) == sorted("Eat".lower()))

# 30. How do you convert a sorted list of characters back to a string?
print("30.", "".join(sorted("apple")))

# ==========================================
# SECTION 3: RECURSION (31 - 50)
# ==========================================

# 31. Write a recursive function to print "Hello" N times.
print("31.")
def print_hello(n):
    if n == 0: return
    print("Hello", end=" ")
    print_hello(n-1)
print_hello(3); print()

# 32. Recursive function to find the sum of numbers from 1 to 5.
print("32.")
def sum_n(n):
    if n == 1: return 1
    return n + sum_n(n-1)
print(sum_n(5))

# 33. Factorial of 5 using recursion.
print("33.")
def fact(n):
    if n == 0 or n == 1: return 1
    return n * fact(n-1)
print(fact(5))

# 34. Fibonacci number at position 6 using recursion.
print("34.")
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
print(fib(6))

# 35. Recursive function to count down from 3 to 1.
print("35.")
def count_down(n):
    if n == 0: return
    print(n, end=" ")
    count_down(n-1)
count_down(3); print()

# 36. Recursive function to reverse a string "abc".
print("36.")
def rev_str(s):
    if len(s) == 0: return s
    return s[-1] + rev_str(s[:-1])
print(rev_str("abc"))

# 37. Recursive function to find the length of a string.
print("37.")
def str_len(s):
    if s == "": return 0
    return 1 + str_len(s[1:])
print(str_len("python"))

# 38. Recursive function to check if a string is a palindrome.
print("38.")
def is_pal(s):
    if len(s) <= 1: return True
    if s[0] != s[-1]: return False
    return is_pal(s[1:-1])
print(is_pal("radar"))

# 39. Count occurrences of a character in a string recursively.
print("39.")
def count_char(s, char):
    if not s: return 0
    return (1 if s[0] == char else 0) + count_char(s[1:], char)
print(count_char("apple", "p"))

# 40. Calculate 2^3 using recursion.
print("40.")
def power(base, exp):
    if exp == 0: return 1
    return base * power(base, exp-1)
print(power(2, 3))

# 41. Sum of elements in a list recursively.
print("41.")
def sum_list(lst):
    if not lst: return 0
    return lst[0] + sum_list(lst[1:])
print(sum_list([1, 2, 3, 4]))

# 42. Find the max element in a list recursively.
print("42.")
def max_list(lst):
    if len(lst) == 1: return lst[0]
    m = max_list(lst[1:])
    return lst[0] if lst[0] > m else m
print(max_list([1, 5, 3, 9, 2]))

# 43. Print elements of a list recursively.
print("43.")
def print_list(lst):
    if not lst: return
    print(lst[0], end=" ")
    print_list(lst[1:])
print_list([1,2,3]); print()

# 44. Print elements of a list in reverse order recursively.
print("44.")
def print_rev_list(lst):
    if not lst: return
    print_rev_list(lst[1:])
    print(lst[0], end=" ")
print_rev_list([1,2,3]); print()

# 45. Find GCD of two numbers using Euclidean algorithm recursively.
print("45.")
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
print(gcd(48, 18))

# 46. Check if an array is sorted recursively.
print("46.")
def is_sorted(lst):
    if len(lst) <= 1: return True
    if lst[0] > lst[1]: return False
    return is_sorted(lst[1:])
print(is_sorted([1, 2, 3, 4]))

# 47. Recursive function to multiply two numbers without using '*'.
print("47.")
def mult(a, b):
    if b == 0: return 0
    return a + mult(a, b-1)
print(mult(5, 4))

# 48. Print the binary representation of a number recursively.
print("48.")
def dec_to_bin(n):
    if n == 0: return
    dec_to_bin(n // 2)
    print(n % 2, end="")
dec_to_bin(10); print()

# 49. Check if a number is even recursively.
print("49.")
def is_even(n):
    if n == 0: return True
    if n == 1: return False
    return is_even(n - 2)
print(is_even(10))

# 50. Remove all vowels from a string recursively.
print("50.")
def rem_vowels(s):
    if not s: return ""
    first = "" if s[0].lower() in "aeiou" else s[0]
    return first + rem_vowels(s[1:])
print(rem_vowels("hello world"))

# --- End of Practice Problems ---


# ==================================================
# --- Day4 : Day4_Test_Driven_Practice.py ---
# ==================================================

# Day 4: Test-Driven Practice
# Complete the functions below so that all assert statements pass without errors!

def is_anagram(s1, s2):
    """
    Return True if s1 and s2 are anagrams, ignoring case and spaces.
    Otherwise return False.
    """
    # YOUR CODE HERE
    pass

def count_vowels_recursive(s):
    """
    Return the number of vowels (a, e, i, o, u) in the string s using RECURSION.
    """
    # YOUR CODE HERE
    pass

def reverse_string_recursive(s):
    """
    Return the reversed version of string s using RECURSION.
    """
    # YOUR CODE HERE
    pass

# ==========================================
# 🛑 DO NOT MODIFY THE CODE BELOW THIS LINE 
# ==========================================
if __name__ == "__main__":
    print("Running tests...")
    
    # Test is_anagram
    try:
        assert is_anagram("Listen", "Silent") == True
        assert is_anagram("hello", "world") == False
        assert is_anagram("Astronomer", "Moon starer") == True
        print("✅ is_anagram tests passed!")
    except AssertionError:
        print("❌ is_anagram tests failed!")

    # Test count_vowels_recursive
    try:
        assert count_vowels_recursive("hello") == 2
        assert count_vowels_recursive("xyz") == 0
        assert count_vowels_recursive("education") == 5
        print("✅ count_vowels_recursive tests passed!")
    except AssertionError:
        print("❌ count_vowels_recursive tests failed!")

    # Test reverse_string_recursive
    try:
        assert reverse_string_recursive("hello") == "olleh"
        assert reverse_string_recursive("Python") == "nohtyP"
        assert reverse_string_recursive("") == ""
        print("✅ reverse_string_recursive tests passed!")
    except AssertionError:
        print("❌ reverse_string_recursive tests failed!")

    print("Test run complete.")


# ==================================================
# --- Day5 : Day5_Practice_Problems.py ---
# ==================================================

# Day 5 Practice Problems

# Problem 1: Sum all numbers in a list
def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

# Problem 2: Product of all numbers in a list
def product_list(nums):
    if not nums:
        return 0
    product = 1
    for num in nums:
        product *= num
    return product

# Problem 3: Frequencies count of values
def count_frequencies(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Problem 4: Sum of squares
def sum_of_squares(nums):
    total = 0
    for num in nums:
        total += num * num
    return total

# Problem 5: Printing squares
def print_squares(nums):
    squares = [num * num for num in nums]
    print("Squares:", squares)
    return squares

# Problem 6: Printing all combination pairs in a given list
def print_combination_pairs(nums):
    pairs = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((nums[i], nums[j]))
    return pairs

if __name__ == "__main__":
    test_list = [1, 2, 3, 4]
    print("Sum:", sum_list(test_list))
    print("Product:", product_list(test_list))
    print("Frequencies:", count_frequencies([1, 2, 2, 3, 1, 4]))
    print("Sum of Squares:", sum_of_squares(test_list))
    print_squares(test_list)
    print("Combination Pairs:", print_combination_pairs(test_list))


# ==================================================
# --- Day5 : Day5_Test_Driven_Practice.py ---
# ==================================================

import unittest

def sum_all_numbers(nums):
    return sum(nums)

def product_all_numbers(nums):
    if not nums: return 0
    res = 1
    for n in nums: res *= n
    return res

def count_frequencies(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    return freq

class TestDay5Methods(unittest.TestCase):

    def test_sum_all_numbers(self):
        self.assertEqual(sum_all_numbers([1, 2, 3]), 6)
        self.assertEqual(sum_all_numbers([10, -10, 5]), 5)

    def test_product_all_numbers(self):
        self.assertEqual(product_all_numbers([1, 2, 3, 4]), 24)
        self.assertEqual(product_all_numbers([]), 0)
        self.assertEqual(product_all_numbers([5, 0, 2]), 0)

    def test_count_frequencies(self):
        self.assertEqual(count_frequencies([1, 1, 2]), {1: 2, 2: 1})
        self.assertEqual(count_frequencies(["a", "b", "a"]), {"a": 2, "b": 1})

if __name__ == '__main__':
    unittest.main()

