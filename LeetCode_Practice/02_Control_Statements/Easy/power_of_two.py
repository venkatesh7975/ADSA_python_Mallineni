# Problem: Power of Two
# Link: https://leetcode.com/problems/power-of-two/

# Approach 1: Iterative Division
# Time Complexity: O(log n), Space Complexity: O(1)
def isPowerOfTwo_iter(n):
    if n <= 0: return False
    while n % 2 == 0:
        n //= 2
    return n == 1

# Approach 2: Optimal (Bit Manipulation)
# Time Complexity: O(1), Space Complexity: O(1)
def isPowerOfTwo_optimal(n):
    return n > 0 and (n & (n - 1)) == 0
