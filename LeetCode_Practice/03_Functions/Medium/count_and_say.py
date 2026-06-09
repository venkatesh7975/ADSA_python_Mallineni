# Problem: Count and Say
# Link: https://leetcode.com/problems/count-and-say/

# Approach 1: Iterative Counting (Optimal)
# Time Complexity: O(4^(n/3)), Space Complexity: O(4^(n/3)) due to string lengths
def countAndSay(n):
    res = "1"
    for _ in range(n - 1):
        next_res = ""
        count = 1
        for j in range(len(res)):
            if j + 1 < len(res) and res[j] == res[j + 1]:
                count += 1
            else:
                next_res += str(count) + res[j]
                count = 1
        res = next_res
    return res
