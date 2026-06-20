"""
Day 15: 50 Coding Problems on Hashing, Sets, Frequency Maps & BSTs
A massive collection of top LeetCode patterns that reduce O(N^2) time complexities down to O(N) or O(N log N) using Hash Maps, Sets, and BST logic.
"""
from collections import Counter, defaultdict
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ==========================================
# Hashing & Sets Core Patterns
# ==========================================
# 1. Two Sum
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

# 2. Contains Duplicate
def contains_duplicate(nums):
    return len(set(nums)) != len(nums)

# 3. Valid Anagram
def is_anagram(s, t):
    return Counter(s) == Counter(t)

# 4. Group Anagrams
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# 5. Top K Frequent Elements
def top_k_frequent(nums, k):
    return [item for item, count in Counter(nums).most_common(k)]

# 6. Longest Consecutive Sequence
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set: # start of a sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

# 7. Intersection of Two Arrays
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

# 8. Intersection of Two Arrays II
def intersect_ii(nums1, nums2):
    counts = Counter(nums1)
    res = []
    for num in nums2:
        if counts[num] > 0:
            res.append(num)
            counts[num] -= 1
    return res

# 9. First Unique Character in a String
def first_uniq_char(s):
    counts = Counter(s)
    for i, char in enumerate(s):
        if counts[char] == 1:
            return i
    return -1

# 10. Ransom Note
def can_construct(ransomNote, magazine):
    mag_count = Counter(magazine)
    for char in ransomNote:
        if mag_count[char] == 0:
            return False
        mag_count[char] -= 1
    return True

# 11. Jewels and Stones
def num_jewels_in_stones(jewels, stones):
    j_set = set(jewels)
    return sum(1 for s in stones if s in j_set)

# 12. Find All Numbers Disappeared in an Array
def find_disappeared_numbers(nums):
    num_set = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in num_set]

# 13. Majority Element
def majority_element(nums):
    return Counter(nums).most_common(1)[0][0]

# 14. Single Number
def single_number(nums):
    # Using Hashing (though XOR is better O(1) space)
    counts = Counter(nums)
    for k, v in counts.items():
        if v == 1: return k

# 15. Isomorphic Strings
def is_isomorphic(s, t):
    if len(s) != len(t): return False
    map_st, map_ts = {}, {}
    for c1, c2 in zip(s, t):
        if (c1 in map_st and map_st[c1] != c2) or (c2 in map_ts and map_ts[c2] != c1):
            return False
        map_st[c1] = c2
        map_ts[c2] = c1
    return True

# 16. Word Pattern
def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words): return False
    char_to_word, word_to_char = {}, {}
    for c, w in zip(pattern, words):
        if (c in char_to_word and char_to_word[c] != w) or (w in word_to_char and word_to_char[w] != c):
            return False
        char_to_word[c] = w
        word_to_char[w] = c
    return True

# 17. Subarray Sum Equals K (Prefix Sum + Hash Map)
def subarray_sum(nums, k):
    count, prefix_sum = 0, 0
    prefix_map = defaultdict(int)
    prefix_map[0] = 1
    for num in nums:
        prefix_sum += num
        count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] += 1
    return count

# 18. Contiguous Array (Equal 0s and 1s)
def find_max_length(nums):
    max_len, count = 0, 0
    count_map = {0: -1}
    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        if count in count_map:
            max_len = max(max_len, i - count_map[count])
        else:
            count_map[count] = i
    return max_len

# 19. Find the Difference
def find_the_difference(s, t):
    counts = Counter(s)
    for char in t:
        if counts[char] == 0:
            return char
        counts[char] -= 1

# 20. Sort Characters By Frequency
def frequency_sort(s):
    counts = Counter(s)
    return "".join(char * count for char, count in counts.most_common())

# ==========================================
# BST specific Algorithms
# ==========================================
# 21. Minimum Absolute Difference in BST
def get_minimum_difference(root):
    vals = []
    def inorder(node):
        if not node: return
        inorder(node.left)
        vals.append(node.val)
        inorder(node.right)
    inorder(root)
    return min(vals[i] - vals[i-1] for i in range(1, len(vals)))

# 22. Find Mode in Binary Search Tree
def find_mode_bst(root):
    counts = defaultdict(int)
    def inorder(node):
        if not node: return
        inorder(node.left)
        counts[node.val] += 1
        inorder(node.right)
    inorder(root)
    max_freq = max(counts.values())
    return [k for k, v in counts.items() if v == max_freq]

# 23. Two Sum IV - Input is a BST
def find_target(root, k):
    seen = set()
    def dfs(node):
        if not node: return False
        if k - node.val in seen: return True
        seen.add(node.val)
        return dfs(node.left) or dfs(node.right)
    return dfs(root)

# 24. Kth Smallest Element in a BST
def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0: return root.val
        root = root.right

# 25. Lowest Common Ancestor of a Binary Search Tree
def lowest_common_ancestor_bst(root, p, q):
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val: curr = curr.left
        elif p.val > curr.val and q.val > curr.val: curr = curr.right
        else: return curr

# 26. Validate Binary Search Tree
def is_valid_bst(root):
    def validate(node, low=-float('inf'), high=float('inf')):
        if not node: return True
        if node.val <= low or node.val >= high: return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root)

# 27. Insert into a Binary Search Tree
def insert_into_bst(root, val):
    if not root: return TreeNode(val)
    if val < root.val: root.left = insert_into_bst(root.left, val)
    else: root.right = insert_into_bst(root.right, val)
    return root

# 28. Delete Node in a BST
def delete_node(root, key):
    if not root: return None
    if key < root.val: root.left = delete_node(root.left, key)
    elif key > root.val: root.right = delete_node(root.right, key)
    else:
        if not root.left: return root.right
        if not root.right: return root.left
        curr = root.right
        while curr.left: curr = curr.left
        root.val = curr.val
        root.right = delete_node(root.right, root.val)
    return root

# 29. Convert Sorted Array to Binary Search Tree
def sorted_array_to_bst(nums):
    if not nums: return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    return root

# 30. Trim a Binary Search Tree
def trim_bst(root, low, high):
    if not root: return None
    if root.val < low: return trim_bst(root.right, low, high)
    if root.val > high: return trim_bst(root.left, low, high)
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)
    return root

# 31. Range Sum of BST
def range_sum_bst(root, low, high):
    if not root: return 0
    if root.val < low: return range_sum_bst(root.right, low, high)
    if root.val > high: return range_sum_bst(root.left, low, high)
    return root.val + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)

# ==========================================
# Mixed Hash/BST & Fast Lookup Algorithms
# ==========================================
# 32. Design HashMap (Implementation simulation)
class MyHashMap:
    def __init__(self):
        self.map = [-1] * 1000001
    def put(self, key: int, value: int) -> None:
        self.map[key] = value
    def get(self, key: int) -> int:
        return self.map[key]
    def remove(self, key: int) -> None:
        self.map[key] = -1

# 33. Design HashSet (Implementation simulation)
class MyHashSet:
    def __init__(self):
        self.set = [False] * 1000001
    def add(self, key: int) -> None:
        self.set[key] = True
    def contains(self, key: int) -> bool:
        return self.set[key]
    def remove(self, key: int) -> None:
        self.set[key] = False

# 34. Contains Duplicate II
def contains_nearby_duplicate(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False

# 35. Find All Duplicates in an Array
def find_duplicates(nums):
    res = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            res.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1
    return res

# 36. Word Subsets
def word_subsets(words1, words2):
    max_freq = Counter()
    for w in words2:
        for char, count in Counter(w).items():
            max_freq[char] = max(max_freq[char], count)
    res = []
    for w in words1:
        w_freq = Counter(w)
        if all(w_freq[char] >= count for char, count in max_freq.items()):
            res.append(w)
    return res

# 37. Sum of Unique Elements
def sum_of_unique(nums):
    counts = Counter(nums)
    return sum(k for k, v in counts.items() if v == 1)

# 38. Destination City
def dest_city(paths):
    outgoing = {path[0] for path in paths}
    for path in paths:
        if path[1] not in outgoing:
            return path[1]

# 39. Missing Number
def missing_number(nums):
    return sum(range(len(nums) + 1)) - sum(nums)

# 40. Largest Unique Number
def largest_unique_number(nums):
    counts = Counter(nums)
    uniques = [k for k, v in counts.items() if v == 1]
    return max(uniques) if uniques else -1

# 41. Valid Sudoku (HashSet technique)
def is_valid_sudoku(board):
    seen = set()
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val != '.':
                if (i, val) in seen or (val, j) in seen or (i//3, j//3, val) in seen:
                    return False
                seen.add((i, val))
                seen.add((val, j))
                seen.add((i//3, j//3, val))
    return True

# 42. Check if Array Pairs Are Divisible by k
def can_arrange(arr, k):
    rem_counts = [0] * k
    for num in arr:
        rem_counts[num % k] += 1
    if rem_counts[0] % 2 != 0: return False
    for i in range(1, k // 2 + 1):
        if rem_counts[i] != rem_counts[k - i]: return False
    return True

# 43. Least Number of Unique Integers after K Removals
def find_least_num_of_unique_ints(arr, k):
    counts = sorted(Counter(arr).values())
    unique = len(counts)
    for count in counts:
        if k >= count:
            k -= count
            unique -= 1
        else:
            break
    return unique

# 44. First Missing Positive
def first_missing_positive(nums):
    num_set = set(nums)
    i = 1
    while i in num_set:
        i += 1
    return i

# 45. Find Players With Zero or One Losses
def find_winners(matches):
    losses = defaultdict(int)
    for winner, loser in matches:
        if winner not in losses: losses[winner] = 0
        losses[loser] += 1
    zero_loss = sorted([k for k, v in losses.items() if v == 0])
    one_loss = sorted([k for k, v in losses.items() if v == 1])
    return [zero_loss, one_loss]

# 46. Determine if Two Strings Are Close
def close_strings(word1, word2):
    if set(word1) != set(word2): return False
    return sorted(Counter(word1).values()) == sorted(Counter(word2).values())

# 47. Minimum Number of Steps to Make Two Strings Anagram
def min_steps(s, t):
    counts = Counter(s)
    for char in t:
        if counts[char] > 0: counts[char] -= 1
    return sum(counts.values())

# 48. Find the Prefix Common Array of Two Arrays
def find_the_prefix_common_array(A, B):
    seen = set()
    res, common = [], 0
    for a, b in zip(A, B):
        if a in seen: common += 1
        seen.add(a)
        if b in seen: common += 1
        seen.add(b)
        res.append(common)
    return res

# 49. Find the Number of Good Pairs
def num_identical_pairs(nums):
    counts = Counter(nums)
    return sum(val * (val - 1) // 2 for val in counts.values())

# 50. Happy Number
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(char)**2 for char in str(n))
    return n == 1
