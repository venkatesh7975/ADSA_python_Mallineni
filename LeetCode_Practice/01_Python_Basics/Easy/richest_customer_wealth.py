# Problem: Richest Customer Wealth
# Link: https://leetcode.com/problems/richest-customer-wealth/

# Approach 1: Nested Loops
# Time Complexity: O(m*n), Space Complexity: O(1)
def maximumWealth_loops(accounts):
    max_wealth = 0
    for customer in accounts:
        current_wealth = 0
        for bank in customer:
            current_wealth += bank
        max_wealth = max(max_wealth, current_wealth)
    return max_wealth

# Approach 2: Optimal (Pythonic)
# Time Complexity: O(m*n), Space Complexity: O(1)
def maximumWealth_pythonic(accounts):
    return max(sum(customer) for customer in accounts)
