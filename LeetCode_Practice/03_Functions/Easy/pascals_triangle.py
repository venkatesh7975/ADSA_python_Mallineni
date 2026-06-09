# Problem: Pascal's Triangle
# Link: https://leetcode.com/problems/pascals-triangle/

# Approach 1: Dynamic Programming (Optimal)
# Time Complexity: O(numRows^2), Space Complexity: O(numRows^2) for the output
def generate(numRows):
    res = [[1]]
    for i in range(1, numRows):
        prev_row = res[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        res.append(new_row)
    return res
