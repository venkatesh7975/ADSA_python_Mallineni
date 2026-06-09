# Problem: Count Odd Numbers in an Interval Range
# Link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

# Approach 1: Optimal Math
# Time Complexity: O(1), Space Complexity: O(1)
def countOdds(low, high):
    total_nums = high - low + 1
    if low % 2 != 0 and high % 2 != 0:
        return total_nums // 2 + 1
    else:
        return total_nums // 2
