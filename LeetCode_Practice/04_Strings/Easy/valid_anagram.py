# Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/

# Approach 1: Sorting
# Time Complexity: O(n log n), Space Complexity: O(1) or O(n) depending on sort
def isAnagram_sort(s, t):
    return sorted(s) == sorted(t)

# Approach 2: Hash Map / Frequency Array (Optimal)
# Time Complexity: O(n), Space Complexity: O(1) since there are 26 chars
def isAnagram_optimal(s, t):
    if len(s) != len(t): return False
    freq = [0] * 26
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1
    return all(f == 0 for f in freq)
