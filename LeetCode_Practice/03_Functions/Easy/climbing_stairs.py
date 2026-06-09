# Problem: Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/

# Approach 1: Recursion with Memoization
# Time Complexity: O(n), Space Complexity: O(n)
def climbStairs_memo(n, memo=None):
    if memo is None: memo = {}
    if n in memo: return memo[n]
    if n <= 2: return n
    memo[n] = climbStairs_memo(n - 1, memo) + climbStairs_memo(n - 2, memo)
    return memo[n]

# Approach 2: Dynamic Programming (Optimal Space)
# Time Complexity: O(n), Space Complexity: O(1)
def climbStairs_optimal(n):
    if n <= 2: return n
    prev1, prev2 = 1, 2
    for _ in range(3, n + 1):
        prev1, prev2 = prev2, prev1 + prev2
    return prev2
