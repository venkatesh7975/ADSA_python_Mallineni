# Problem: Self Dividing Numbers
# Link: https://leetcode.com/problems/self-dividing-numbers/

# Approach 1: Optimal Iteration
# Time Complexity: O(N log(M)) where N is range length, M is max number, Space Complexity: O(1)
def selfDividingNumbers(left, right):
    def is_self_dividing(n):
        temp = n
        while temp > 0:
            digit = temp % 10
            if digit == 0 or n % digit != 0:
                return False
            temp //= 10
        return True
    
    return [n for n in range(left, right + 1) if is_self_dividing(n)]
