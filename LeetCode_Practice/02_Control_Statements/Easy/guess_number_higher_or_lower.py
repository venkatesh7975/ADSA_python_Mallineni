# Problem: Guess Number Higher or Lower
# Link: https://leetcode.com/problems/guess-number-higher-or-lower/

# Approach 1: Optimal Binary Search
# Time Complexity: O(log n), Space Complexity: O(1)
def guessNumber(n):
    # def guess(num): pass # Provided by LeetCode
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        res = guess(mid)
        if res == 0: return mid
        elif res == -1: right = mid - 1
        else: left = mid + 1
