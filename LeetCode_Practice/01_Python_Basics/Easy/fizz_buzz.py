# Problem: Fizz Buzz
# Link: https://leetcode.com/problems/fizz-buzz/

# Approach 1: Conditionals
# Time Complexity: O(n), Space Complexity: O(1)
def fizzBuzz_standard(n):
    res = []
    for i in range(1, n + 1):
        if i % 15 == 0: res.append("FizzBuzz")
        elif i % 3 == 0: res.append("Fizz")
        elif i % 5 == 0: res.append("Buzz")
        else: res.append(str(i))
    return res

# Approach 2: String Concatenation
# Time Complexity: O(n), Space Complexity: O(1)
def fizzBuzz_optimal(n):
    res = []
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0: s += "Fizz"
        if i % 5 == 0: s += "Buzz"
        res.append(s if s else str(i))
    return res
