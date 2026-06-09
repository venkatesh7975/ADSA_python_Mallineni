# Problem: Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/

# Approach 1: Vertical Scanning
# Time Complexity: O(S) where S is sum of chars, Space Complexity: O(1)
def longestCommonPrefix_vertical(strs):
    if not strs: return ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    return strs[0]

# Approach 2: Sorting (Optimal)
# Time Complexity: O(N log N * M), Space Complexity: O(1)
def longestCommonPrefix_optimal(strs):
    strs.sort()
    first, last = strs[0], strs[-1]
    res = []
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]: break
        res.append(first[i])
    return "".join(res)
