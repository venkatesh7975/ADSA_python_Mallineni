# Problem: N-th Tribonacci Number
# Link: https://leetcode.com/problems/n-th-tribonacci-number/

# Approach 1: DP Array
# Time Complexity: O(n), Space Complexity: O(n)
def tribonacci_array(n):
    if n == 0: return 0
    if n <= 2: return 1
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

# Approach 2: DP State Optimization (Optimal)
# Time Complexity: O(n), Space Complexity: O(1)
def tribonacci_optimal(n):
    if n == 0: return 0
    if n <= 2: return 1
    t0, t1, t2 = 0, 1, 1
    for _ in range(3, n + 1):
        t0, t1, t2 = t1, t2, t0 + t1 + t2
    return t2
