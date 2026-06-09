# Problem: Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Approach 1: Backtracking (Optimal)
# Time Complexity: O(4^n * n), Space Complexity: O(n)
def letterCombinations(digits):
    if not digits: return []
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    res = []
    def backtrack(index, path):
        if index == len(digits):
            res.append("".join(path))
            return
        for char in mapping[digits[index]]:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()
            
    backtrack(0, [])
    return res
