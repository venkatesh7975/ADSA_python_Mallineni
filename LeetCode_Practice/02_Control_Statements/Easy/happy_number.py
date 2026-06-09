# Problem: Happy Number
# Link: https://leetcode.com/problems/happy-number/

# Approach 1: Hash Set to detect cycle
# Time Complexity: O(log n), Space Complexity: O(log n)
def isHappy_set(n):
    def get_next(num):
        return sum(int(char) ** 2 for char in str(num))
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1

# Approach 2: Optimal (Floyd's Cycle-Finding Algorithm)
# Time Complexity: O(log n), Space Complexity: O(1)
def isHappy_optimal(n):
    def get_next(num):
        total = 0
        while num > 0:
            num, digit = divmod(num, 10)
            total += digit ** 2
        return total
    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return fast == 1
