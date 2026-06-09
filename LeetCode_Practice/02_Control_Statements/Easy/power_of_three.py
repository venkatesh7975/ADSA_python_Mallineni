# Problem: Power of Three
# Link: https://leetcode.com/problems/power-of-three/

# Approach 1: Iterative Division
# Time Complexity: O(log3 n), Space Complexity: O(1)
def isPowerOfThree_iter(n):
    if n <= 0: return False
    while n % 3 == 0:
        n //= 3
    return n == 1

# Approach 2: Optimal (Math - Max Power of 3 for 32-bit integer)
# Time Complexity: O(1), Space Complexity: O(1)
def isPowerOfThree_optimal(n):
    return n > 0 and 1162261467 % n == 0
