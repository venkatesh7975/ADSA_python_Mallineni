# Problem: Number of Good Pairs
# Link: https://leetcode.com/problems/number-of-good-pairs/

# Approach 1: Brute Force
# Time Complexity: O(n^2), Space Complexity: O(1)
def numIdenticalPairs_brute(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count

# Approach 2: Optimal (Hash Map)
# Time Complexity: O(n), Space Complexity: O(n)
def numIdenticalPairs_optimal(nums):
    count = 0
    freq = {}
    for num in nums:
        if num in freq:
            count += freq[num]
            freq[num] += 1
        else:
            freq[num] = 1
    return count
