# Problem: Pow(x, n)
# Link: https://leetcode.com/problems/powx-n/

# Approach 1: Recursive Binary Exponentiation
# Time Complexity: O(log n), Space Complexity: O(log n)
def myPow_recursive(x, n):
    if n == 0: return 1.0
    if n < 0: return 1.0 / myPow_recursive(x, -n)
    half = myPow_recursive(x, n // 2)
    if n % 2 == 0: return half * half
    return half * half * x

# Approach 2: Iterative Binary Exponentiation (Optimal)
# Time Complexity: O(log n), Space Complexity: O(1)
def myPow_optimal(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    res = 1
    while n:
        if n % 2 == 1: res *= x
        x *= x
        n //= 2
    return res
