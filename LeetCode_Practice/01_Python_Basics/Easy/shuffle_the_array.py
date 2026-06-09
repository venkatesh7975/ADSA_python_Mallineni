# Problem: Shuffle the Array
# Link: https://leetcode.com/problems/shuffle-the-array/

# Approach 1: Extra Space
# Time Complexity: O(n), Space Complexity: O(n)
def shuffle_extra(nums, n):
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i + n])
    return res

# Approach 2: Bit Manipulation (In-place - Advanced)
# Time Complexity: O(n), Space Complexity: O(1)
def shuffle_inplace(nums, n):
    for i in range(n):
        nums[i + n] = (nums[i + n] << 10) | nums[i]
    for i in range(n):
        num1 = nums[i + n] & 1023
        num2 = nums[i + n] >> 10
        nums[2 * i] = num1
        nums[2 * i + 1] = num2
    return nums
