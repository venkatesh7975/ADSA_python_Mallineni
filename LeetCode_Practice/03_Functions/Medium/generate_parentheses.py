# Problem: Generate Parentheses
# Link: https://leetcode.com/problems/generate-parentheses/

# Approach 1: Backtracking (Optimal)
# Time Complexity: O(4^n / sqrt(n)), Space Complexity: O(n) for call stack
def generateParenthesis(n):
    res = []
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            res.append(current)
            return
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return res
