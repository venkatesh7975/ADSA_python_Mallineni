# Problem: Build Array from Permutation
# Link: https://leetcode.com/problems/build-array-from-permutation/

# Approach 1: Extra Space
# Time Complexity: O(n), Space Complexity: O(n)
def buildArray_extra(nums):
    return [nums[nums[i]] for i in range(len(nums))]

# Approach 2: Optimal (In-place using Math)
# Time Complexity: O(n), Space Complexity: O(1)
def buildArray_optimal(nums):
    q = len(nums)
    for i in range(len(nums)):
        nums[i] = nums[i] + (nums[nums[i]] % q) * q
    for i in range(len(nums)):
        nums[i] = nums[i] // q
    return nums
# Change to buildArray_extra to use the extra space approach
print(buildArray_extra([0,2,1,5,3,4]))  # Output: [0,1,2,4,5,3]
