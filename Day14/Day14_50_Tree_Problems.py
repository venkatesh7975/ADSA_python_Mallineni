"""
Day 14: 50 Binary Tree Problems & Solutions
A comprehensive collection of 50 core Binary Tree and Binary Search Tree (BST) algorithms.
"""
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ==========================================
# Traversal Algorithms
# ==========================================
# 1. Inorder Traversal (Recursive)
def inorder(root):
    res = []
    def dfs(node):
        if not node: return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res

# 2. Preorder Traversal (Recursive)
def preorder(root):
    res = []
    def dfs(node):
        if not node: return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res

# 3. Postorder Traversal (Recursive)
def postorder(root):
    res = []
    def dfs(node):
        if not node: return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
    dfs(root)
    return res

# 4. Level Order Traversal (BFS)
def level_order(root):
    if not root: return []
    res, q = [], collections.deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res

# 5. Inorder Traversal (Iterative)
def inorder_iterative(root):
    res, stack, curr = [], [], root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

# 6. Preorder Traversal (Iterative)
def preorder_iterative(root):
    if not root: return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return res

# 7. Postorder Traversal (Iterative)
def postorder_iterative(root):
    if not root: return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return res[::-1]

# ==========================================
# Core Tree Properties
# ==========================================
# 8. Maximum Depth of Binary Tree
def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# 9. Minimum Depth of Binary Tree
def min_depth(root):
    if not root: return 0
    if not root.left: return 1 + min_depth(root.right)
    if not root.right: return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))

# 10. Diameter of Binary Tree
def diameter(root):
    res = [0]
    def height(node):
        if not node: return 0
        left = height(node.left)
        right = height(node.right)
        res[0] = max(res[0], left + right)
        return 1 + max(left, right)
    height(root)
    return res[0]

# 11. Balanced Binary Tree
def is_balanced(root):
    def height(node):
        if not node: return 0
        left = height(node.left)
        right = height(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1: return -1
        return 1 + max(left, right)
    return height(root) != -1

# 12. Same Tree
def is_same_tree(p, q):
    if not p and not q: return True
    if not p or not q or p.val != q.val: return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# 13. Symmetric Tree
def is_symmetric(root):
    def mirror(t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2 or t1.val != t2.val: return False
        return mirror(t1.left, t2.right) and mirror(t1.right, t2.left)
    return mirror(root, root) if root else True

# 14. Invert Binary Tree
def invert_tree(root):
    if not root: return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

# ==========================================
# Binary Search Tree (BST) Properties
# ==========================================
# 15. Search in a BST
def search_bst(root, val):
    if not root or root.val == val: return root
    return search_bst(root.left, val) if val < root.val else search_bst(root.right, val)

# 16. Insert into a BST
def insert_bst(root, val):
    if not root: return TreeNode(val)
    if val < root.val: root.left = insert_bst(root.left, val)
    else: root.right = insert_bst(root.right, val)
    return root

# 17. Validate Binary Search Tree
def is_valid_bst(root):
    def valid(node, min_val, max_val):
        if not node: return True
        if not (min_val < node.val < max_val): return False
        return valid(node.left, min_val, node.val) and valid(node.right, node.val, max_val)
    return valid(root, float('-inf'), float('inf'))

# 18. Lowest Common Ancestor of a BST
def lca_bst(root, p, q):
    if p.val < root.val and q.val < root.val: return lca_bst(root.left, p, q)
    if p.val > root.val and q.val > root.val: return lca_bst(root.right, p, q)
    return root

# 19. Convert Sorted Array to BST
def sorted_array_to_bst(nums):
    if not nums: return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    return root

# 20. Two Sum IV - Input is a BST
def find_target_bst(root, k):
    seen = set()
    def dfs(node):
        if not node: return False
        if k - node.val in seen: return True
        seen.add(node.val)
        return dfs(node.left) or dfs(node.right)
    return dfs(root)

# 21. Minimum Absolute Difference in BST
def get_min_diff_bst(root):
    vals = inorder(root)
    return min(vals[i] - vals[i-1] for i in range(1, len(vals)))

# 22. Kth Smallest Element in a BST
def kth_smallest_bst(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0: return root.val
        root = root.right

# ==========================================
# Path and Sum Problems
# ==========================================
# 23. Path Sum (Root to Leaf)
def has_path_sum(root, targetSum):
    if not root: return False
    if not root.left and not root.right: return targetSum == root.val
    return has_path_sum(root.left, targetSum - root.val) or has_path_sum(root.right, targetSum - root.val)

# 24. Sum of Left Leaves
def sum_left_leaves(root):
    if not root: return 0
    res = 0
    if root.left and not root.left.left and not root.left.right:
        res += root.left.val
    return res + sum_left_leaves(root.left) + sum_left_leaves(root.right)

# 25. Root Equals Sum of Children
def check_tree(root):
    return root.val == root.left.val + root.right.val

# 26. Evaluate Boolean Binary Tree
def evaluate_tree(root):
    if not root.left and not root.right: return root.val == 1
    if root.val == 2: return evaluate_tree(root.left) or evaluate_tree(root.right)
    return evaluate_tree(root.left) and evaluate_tree(root.right)

# 27. Find Mode in Binary Search Tree
def find_mode(root):
    counts = collections.Counter(inorder(root))
    max_count = max(counts.values())
    return [k for k, v in counts.items() if v == max_count]

# 28. Merge Two Binary Trees
def merge_trees(t1, t2):
    if not t1: return t2
    if not t2: return t1
    root = TreeNode(t1.val + t2.val)
    root.left = merge_trees(t1.left, t2.left)
    root.right = merge_trees(t1.right, t2.right)
    return root

# 29. Subtree of Another Tree
def is_subtree(root, subRoot):
    if not subRoot: return True
    if not root: return False
    if is_same_tree(root, subRoot): return True
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)

# ==========================================
# View & Structure Problems
# ==========================================
# 30. Binary Tree Right Side View
def right_side_view(root):
    res = []
    def dfs(node, depth):
        if not node: return
        if depth == len(res): res.append(node.val)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)
    dfs(root, 0)
    return res

# 31. Binary Tree Paths
def binary_tree_paths(root):
    res = []
    def dfs(node, path):
        if not node: return
        path += str(node.val)
        if not node.left and not node.right:
            res.append(path)
        else:
            dfs(node.left, path + "->")
            dfs(node.right, path + "->")
    dfs(root, "")
    return res

# 32. Count Complete Tree Nodes
def count_nodes(root):
    return 1 + count_nodes(root.left) + count_nodes(root.right) if root else 0

# 33. Sum of Root To Leaf Binary Numbers
def sum_root_to_leaf(root):
    def dfs(node, val):
        if not node: return 0
        val = (val << 1) | node.val
        if not node.left and not node.right: return val
        return dfs(node.left, val) + dfs(node.right, val)
    return dfs(root, 0)

# 34. Univalued Binary Tree
def is_unival_tree(root):
    val = root.val
    def dfs(node):
        if not node: return True
        if node.val != val: return False
        return dfs(node.left) and dfs(node.right)
    return dfs(root)

# 35. Construct String from Binary Tree
def tree2str(root):
    if not root: return ""
    res = str(root.val)
    if root.left or root.right: res += f"({tree2str(root.left)})"
    if root.right: res += f"({tree2str(root.right)})"
    return res

# 36. Cousins in Binary Tree
def is_cousins(root, x, y):
    def dfs(node, parent, depth, val):
        if not node: return None
        if node.val == val: return (parent, depth)
        return dfs(node.left, node, depth + 1, val) or dfs(node.right, node, depth + 1, val)
    px, dx = dfs(root, None, 0, x)
    py, dy = dfs(root, None, 0, y)
    return dx == dy and px != py

# ==========================================
# Modification & Construction
# ==========================================
# 37. Flatten Binary Tree to Linked List
def flatten(root):
    curr = root
    while curr:
        if curr.left:
            runner = curr.left
            while runner.right: runner = runner.right
            runner.right = curr.right
            curr.right = curr.left
            curr.left = None
        curr = curr.right

# 38. Delete Leaves With a Given Value
def remove_leaf_nodes(root, target):
    if not root: return None
    root.left = remove_leaf_nodes(root.left, target)
    root.right = remove_leaf_nodes(root.right, target)
    if not root.left and not root.right and root.val == target: return None
    return root

# 39. Leaf-Similar Trees
def leaf_similar(root1, root2):
    def get_leaves(node):
        if not node: return []
        if not node.left and not node.right: return [node.val]
        return get_leaves(node.left) + get_leaves(node.right)
    return get_leaves(root1) == get_leaves(root2)

# 40. Second Minimum Node In a Binary Tree
def find_second_minimum_value(root):
    res = [float('inf')]
    min_val = root.val
    def dfs(node):
        if not node: return
        if min_val < node.val < res[0]: res[0] = node.val
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res[0] if res[0] != float('inf') else -1

# 41-50. Additional Fundamental BST/Tree Helpers
# 41. Average of Levels in Binary Tree
def average_of_levels(root):
    q = collections.deque([root])
    res = []
    while q:
        level_sum = 0
        level_len = len(q)
        for _ in range(level_len):
            node = q.popleft()
            level_sum += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level_sum / level_len)
    return res

# 42. Increasing Order Search Tree
def increasing_bst(root):
    vals = inorder(root)
    dummy = TreeNode(0)
    curr = dummy
    for val in vals:
        curr.right = TreeNode(val)
        curr = curr.right
    return dummy.right

# 43. Search in a Binary Search Tree (Iterative)
def search_bst_iter(root, val):
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root

# 44. Range Sum of BST
def range_sum_bst(root, low, high):
    if not root: return 0
    if root.val > high: return range_sum_bst(root.left, low, high)
    if root.val < low: return range_sum_bst(root.right, low, high)
    return root.val + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)

# 45. Find Corresponding Node of a Binary Tree in a Clone of That Tree
def get_target_copy(original, cloned, target):
    if not original: return None
    if original == target: return cloned
    return get_target_copy(original.left, cloned.left, target) or get_target_copy(original.right, cloned.right, target)

# 46. Deepest Leaves Sum
def deepest_leaves_sum(root):
    q = collections.deque([root])
    while q:
        res = 0
        for _ in range(len(q)):
            node = q.popleft()
            res += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return res

# 47. Sum of Nodes with Even-Valued Grandparent
def sum_even_grandparent(root):
    res = 0
    def dfs(node, p, gp):
        nonlocal res
        if not node: return
        if gp and gp.val % 2 == 0: res += node.val
        dfs(node.left, node, p)
        dfs(node.right, node, p)
    dfs(root, None, None)
    return res

# 48. Insert into a Binary Search Tree (Iterative)
def insert_into_bst_iter(root, val):
    if not root: return TreeNode(val)
    curr = root
    while True:
        if val < curr.val:
            if not curr.left:
                curr.left = TreeNode(val)
                break
            curr = curr.left
        else:
            if not curr.right:
                curr.right = TreeNode(val)
                break
            curr = curr.right
    return root

# 49. Delete Node in a BST
def delete_node(root, key):
    if not root: return None
    if key < root.val: root.left = delete_node(root.left, key)
    elif key > root.val: root.right = delete_node(root.right, key)
    else:
        if not root.left: return root.right
        elif not root.right: return root.left
        # Find min from right subtree
        curr = root.right
        while curr.left: curr = curr.left
        root.val = curr.val
        root.right = delete_node(root.right, root.val)
    return root

# 50. Validate Binary Tree Nodes (Single Root Check)
def has_single_root(nodes):
    # Abstract helper: true if there is exactly 1 node with no incoming edges
    in_degrees = {n: 0 for n in nodes}
    for n in nodes:
        if n.left: in_degrees[n.left] += 1
        if n.right: in_degrees[n.right] += 1
    roots = [n for n, deg in in_degrees.items() if deg == 0]
    return len(roots) == 1

# ... End of Day 14 Binary Tree problems!
