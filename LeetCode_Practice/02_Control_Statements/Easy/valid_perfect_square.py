# Problem: Valid Perfect Square
# Link: https://leetcode.com/problems/valid-perfect-square/

# Approach 1: Binary Search
# Time Complexity: O(log n), Space Complexity: O(1)
def isPerfectSquare_bs(num):
    left, right = 1, num
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == num: return True
        elif mid * mid < num: left = mid + 1
        else: right = mid - 1
    return False

# Approach 2: Math (Sum of odd numbers)
# Time Complexity: O(sqrt(n)), Space Complexity: O(1)
def isPerfectSquare_math(num):
    i = 1
    while num > 0:
        num -= i
        i += 2
    return num == 0
