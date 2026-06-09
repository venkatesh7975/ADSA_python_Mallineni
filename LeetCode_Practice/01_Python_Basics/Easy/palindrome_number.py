# Problem: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/

# Approach 1: String Reversal
# Time Complexity: O(n), Space Complexity: O(n)
def isPalindrome_string(x):
    return str(x) == str(x)[::-1]

# Approach 2: Optimal (Revert Half)
# Time Complexity: O(log10(x)), Space Complexity: O(1)
def isPalindrome_optimal(x):
    if x < 0 or (x % 10 == 0 and x != 0): return False
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x //= 10
    return x == reverted or x == reverted // 10
