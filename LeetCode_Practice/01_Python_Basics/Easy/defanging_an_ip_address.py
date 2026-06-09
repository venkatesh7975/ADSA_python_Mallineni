# Problem: Defanging an IP Address
# Link: https://leetcode.com/problems/defanging-an-ip-address/

# Approach 1: Iterative Replacement
# Time Complexity: O(n), Space Complexity: O(n)
def defangIPaddr_iter(address):
    res = ""
    for char in address:
        if char == '.': res += "[.]"
        else: res += char
    return res

# Approach 2: Built-in Method
# Time Complexity: O(n), Space Complexity: O(n)
def defangIPaddr_optimal(address):
    return address.replace('.', '[.]')
