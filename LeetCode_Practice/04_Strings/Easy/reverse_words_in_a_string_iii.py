# Problem: Reverse Words in a String III
# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Approach 1: Split and Reverse
# Time Complexity: O(n), Space Complexity: O(n)
def reverseWords(s):
    return " ".join(word[::-1] for word in s.split(" "))
