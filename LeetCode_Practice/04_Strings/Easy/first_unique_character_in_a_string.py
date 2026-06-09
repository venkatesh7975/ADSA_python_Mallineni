# Problem: First Unique Character in a String
# Link: https://leetcode.com/problems/first-unique-character-in-a-string/

# Approach 1: Hash Map Frequency Count
# Time Complexity: O(n), Space Complexity: O(1) (26 characters)
def firstUniqChar(s):
    from collections import Counter
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1
