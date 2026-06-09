# Problem: Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/

# Approach 1: Single Pass (Optimal)
# Time Complexity: O(n), Space Complexity: O(1)
def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total
