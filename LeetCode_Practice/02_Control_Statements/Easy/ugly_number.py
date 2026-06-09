# Problem: Ugly Number
# Link: https://leetcode.com/problems/ugly-number/

# Approach 1: Optimal Iteration
# Time Complexity: O(log n), Space Complexity: O(1)
def isUgly(n):
    if n <= 0: return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1
