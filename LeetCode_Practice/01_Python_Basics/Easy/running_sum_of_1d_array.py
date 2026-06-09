# Problem: Running Sum of 1d Array
# Link: https://leetcode.com/problems/running-sum-of-1d-array/

# Approach 1: New Array
# Time Complexity: O(n), Space Complexity: O(n)
def runningSum_new(nums):
    res = [nums[0]]
    for i in range(1, len(nums)):
        res.append(res[-1] + nums[i])
    return res

# Approach 2: Optimal (In-place)
# Time Complexity: O(n), Space Complexity: O(1)
def runningSum_optimal(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
