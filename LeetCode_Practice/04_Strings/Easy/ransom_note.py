# Problem: Ransom Note
# Link: https://leetcode.com/problems/ransom-note/

# Approach 1: Frequency Array / Hash Map
# Time Complexity: O(m + n), Space Complexity: O(1) (26 characters)
def canConstruct(ransomNote, magazine):
    from collections import Counter
    mag_count = Counter(magazine)
    for char in ransomNote:
        if mag_count[char] <= 0:
            return False
        mag_count[char] -= 1
    return True
