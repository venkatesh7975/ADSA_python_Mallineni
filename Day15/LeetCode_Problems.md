# Day 15: Binary Search Tree (BST) LeetCode Practice

Here are essential LeetCode problems related to Binary Search Trees to master the concepts of insertion, search, and validation.

---

### [Task 1] 700. Search in a Binary Search Tree
**Difficulty:** Easy

**Problem Statement:** You are given the `root` of a binary search tree (BST) and an integer `val`. Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

**Python Solution:**
```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: root is null or we found the target value
        if not root or root.val == val:
            return root
        
        # If the target is smaller, search the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If the target is larger, search the right subtree
        return self.searchBST(root.right, val)
```

---

### [Task 2] 701. Insert into a Binary Search Tree
**Difficulty:** Medium

**Problem Statement:** You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

**Python Solution:**
```python
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root
```

---

### [Task 3] 98. Validate Binary Search Tree
**Difficulty:** Medium

**Problem Statement:** Given the `root` of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys strictly less than the node's key.
- The right subtree of a node contains only nodes with keys strictly greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

**Python Solution:**
```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            # An empty tree is a valid BST
            if not node:
                return True
                
            # The current node's value must be between low and high
            if node.val <= low or node.val >= high:
                return False
                
            # The left subtree must be < node.val, right subtree must be > node.val
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root)
```

---

### [Task 4] 108. Convert Sorted Array to Binary Search Tree
**Difficulty:** Easy

**Problem Statement:** Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

**Python Solution:**
```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(left, right):
            if left > right:
                return None
            
            # Always choose the middle element to keep tree balanced
            mid = (left + right) // 2
            
            root = TreeNode(nums[mid])
            root.left = buildTree(left, mid - 1)
            root.right = buildTree(mid + 1, right)
            
            return root
            
        return buildTree(0, len(nums) - 1)
```

---

### [Task 5] 235. Lowest Common Ancestor of a Binary Search Tree
**Difficulty:** Medium

**Problem Statement:** Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

**Python Solution:**
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If both p and q are greater than root, LCA is in the right subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
            
        # If both p and q are lesser than root, LCA is in the left subtree
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
            
        # We have found the split point (or one of the nodes is the root)
        else:
            return root
```
