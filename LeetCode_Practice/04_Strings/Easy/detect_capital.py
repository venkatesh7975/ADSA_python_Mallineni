# Problem: Detect Capital
# Link: https://leetcode.com/problems/detect-capital/

# Approach 1: Built-in string methods
# Time Complexity: O(n), Space Complexity: O(1)
def detectCapitalUse(word):
    return word.isupper() or word.islower() or word.istitle()

# Approach 2: Count Capitals
# Time Complexity: O(n), Space Complexity: O(1)
def detectCapitalUse_count(word):
    caps = sum(1 for c in word if c.isupper())
    if caps == len(word) or caps == 0: return True
    return caps == 1 and word[0].isupper()
