# Problem: Final Value of Variable After Performing Operations
# Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

# Approach 1: Iterative
# Time Complexity: O(n), Space Complexity: O(1)
def finalValueAfterOperations_iter(operations):
    x = 0
    for op in operations:
        if op == "++X" or op == "X++": x += 1
        else: x -= 1
    return x

# Approach 2: Pythonic
# Time Complexity: O(n), Space Complexity: O(1)
def finalValueAfterOperations_pythonic(operations):
    return sum(1 if '+' in op else -1 for op in operations)
