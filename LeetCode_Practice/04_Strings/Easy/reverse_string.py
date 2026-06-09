# Problem: Reverse String
# Link: https://leetcode.com/problems/reverse-string/

# Approach 1: Pythonic Built-in
# Time Complexity: O(n), Space Complexity: O(1) (in-place)
def reverseString_pythonic(s):
    s.reverse()

# Approach 2: Two Pointers (Optimal)
# Time Complexity: O(n), Space Complexity: O(1)
def reverseString_pointers(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
