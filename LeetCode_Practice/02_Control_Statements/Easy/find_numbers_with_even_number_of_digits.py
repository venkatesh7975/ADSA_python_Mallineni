# Problem: Find Numbers with Even Number of Digits
# Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

# Approach 1: String Conversion
# Time Complexity: O(n), Space Complexity: O(n)
def findNumbers_string(nums):
    return sum(1 for num in nums if len(str(num)) % 2 == 0)

# Approach 2: Optimal Math (Log10)
# Time Complexity: O(n), Space Complexity: O(1)
import math
def findNumbers_optimal(nums):
    return sum(1 for num in nums if (int(math.log10(num)) + 1) % 2 == 0)
