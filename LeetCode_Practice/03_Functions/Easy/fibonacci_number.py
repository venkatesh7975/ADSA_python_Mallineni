# Problem: Fibonacci Number
# Link: https://leetcode.com/problems/fibonacci-number/

# Approach 1: Recursive (Brute Force)
# Time Complexity: O(2^n), Space Complexity: O(n)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Approach 2: Dynamic Programming (Optimal Space)
# Time Complexity: O(n), Space Complexity: O(1)
def fib_optimal(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
