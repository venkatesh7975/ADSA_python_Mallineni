# Problem: Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/

# Approach 1: Filter and Compare
# Time Complexity: O(n), Space Complexity: O(n)
def isPalindrome_filter(s):
    clean = [c.lower() for c in s if c.isalnum()]
    return clean == clean[::-1]

# Approach 2: Two Pointers (Optimal, In-place)
# Time Complexity: O(n), Space Complexity: O(1)
def isPalindrome_optimal(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum(): left += 1
        while left < right and not s[right].isalnum(): right -= 1
        if s[left].lower() != s[right].lower(): return False
        left += 1
        right -= 1
    return True
