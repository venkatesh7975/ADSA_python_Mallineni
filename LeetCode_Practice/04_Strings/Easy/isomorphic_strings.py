# Problem: Isomorphic Strings
# Link: https://leetcode.com/problems/isomorphic-strings/

# Approach 1: Two Hash Maps
# Time Complexity: O(n), Space Complexity: O(1)
def isIsomorphic(s, t):
    map_s_t, map_t_s = {}, {}
    for c1, c2 in zip(s, t):
        if c1 in map_s_t and map_s_t[c1] != c2: return False
        if c2 in map_t_s and map_t_s[c2] != c1: return False
        map_s_t[c1] = c2
        map_t_s[c2] = c1
    return True
