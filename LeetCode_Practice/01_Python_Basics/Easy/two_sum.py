# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/

# Approach 1: Brute Force
# Time Complexity: O(n^2), Space Complexity: O(1)
def twoSum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Approach 2: Optimal (Hash Map)
# Time Complexity: O(n), Space Complexity: O(n)
def twoSum_optimal(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
