# Day 15 Tasks

Here is the checklist of tree-based problems to complete for Day 15. Each task includes the LeetCode link, Python solution, and interactive visualization link where available.

---

### [ ] 1. Valid BST
**LeetCode 98**: [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
**Visualization**: [https://bounds-of-order.lovable.app](https://bounds-of-order.lovable.app)

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node: return True
            if not (left < node.val < right): return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float('-inf'), float('inf'))
```

---

### [ ] 2. Max Depth of Binary Tree
**LeetCode 104**: [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
**Visualization**: [https://maxdepth.lovable.app](https://maxdepth.lovable.app)

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

---

### [ ] 3. Min Depth of Binary Tree
**LeetCode 111**: [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
*(No specific visualizer available)*

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left: return 1 + self.minDepth(root.right)
        if not root.right: return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```

---

### [ ] 4. Lowest Common Ancestor (LCA)
**LeetCode 236**: [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
*(No specific visualizer available)*

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        return l if l else r
```

---

### [ ] 5. Boundary Traversal
**LeetCode 545**: [Boundary of Binary Tree (Premium)](https://leetcode.com/problems/boundary-of-binary-tree/)
*(No specific visualizer available)*

```python
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = [root.val]
        
        def is_leaf(node):
            return node and not node.left and not node.right
            
        def add_left_boundary(node):
            while node:
                if not is_leaf(node): res.append(node.val)
                node = node.left if node.left else node.right
                
        def add_leaves(node):
            if not node: return
            if is_leaf(node) and node != root: res.append(node.val)
            add_leaves(node.left)
            add_leaves(node.right)
            
        def add_right_boundary(node):
            stack = []
            while node:
                if not is_leaf(node): stack.append(node.val)
                node = node.right if node.right else node.left
            res.extend(stack[::-1])
            
        add_left_boundary(root.left)
        add_leaves(root)
        add_right_boundary(root.right)
        
        return res
```

---

### [ ] 6. Mirror Trees (Symmetric Tree)
**LeetCode 101**: [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
**Visualization**: [https://synapse-recurs.lovable.app](https://synapse-recurs.lovable.app)

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right: return True
            if not left or not right or left.val != right.val: return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right) if root else True
```

---

### [ ] 7. Left View Traversal
**GeeksforGeeks**: [Left View of Binary Tree](https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1)
**Visualization**: [https://algo-inevitable-flow.lovable.app](https://algo-inevitable-flow.lovable.app)

```python
class Solution:
    def LeftView(self, root):
        if not root: return []
        res = []
        q = [root]
        
        while q:
            # The first node in the queue at the current level is the left view node
            res.append(q[0].val)
            next_level = []
            for node in q:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            q = next_level
            
        return res
```

---

### [ ] 8. BFS Traversal (Level Order)
**LeetCode 102**: [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
**Visualization**: [https://bfstraversal.lovable.app](https://bfstraversal.lovable.app)

```python
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
```
