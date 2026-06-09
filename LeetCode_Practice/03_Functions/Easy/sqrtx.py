# Problem: Sqrt(x)
# Link: https://leetcode.com/problems/sqrtx/

# Approach 1: Linear Search (Brute Force)
# Time Complexity: O(sqrt(x)), Space Complexity: O(1)
def mySqrt_linear(x):
    i = 0
    while i * i <= x:
        i += 1
    return i - 1

# Approach 2: Binary Search (Optimal)
# Time Complexity: O(log x), Space Complexity: O(1)
def mySqrt_optimal(x):
    if x < 2: return x
    left, right = 2, x // 2
    while left <= right:
        mid = (left + right) // 2
        num = mid * mid
        if num == x: return mid
        elif num < x: left = mid + 1
        else: right = mid - 1
    return right
