# Day 14: Introduction to Trees

## 1. What is a Tree?
A Tree is a non-linear, hierarchical data structure consisting of nodes connected by edges. Unlike Arrays or Linked Lists which are linear (one element follows another), a tree can have multiple paths and branches.

### Key Terminology
- **Node**: An entity that contains a key/value and pointers to child nodes.
- **Root**: The topmost node of the tree. It has no parent.
- **Edge**: The link between any two nodes.
- **Parent**: Any node that has at least one child.
- **Child**: A node extending from another node.
- **Leaf**: A node with no children (also called an external node).
- **Internal Node**: A node with at least one child.
- **Depth of a Node**: The number of edges from the root to the node.
- **Height of a Node**: The number of edges on the longest path from the node to a leaf.
- **Height of a Tree**: The height of its root node.

## 2. Why Trees?
1. **Hierarchical Data**: Perfect for representing folder structures, organizational charts, HTML DOM, etc.
2. **Efficient Searching**: Binary Search Trees (BST) allow for $O(\log N)$ search, insertion, and deletion times.
3. **Prefix Routing**: Tries (Prefix Trees) are incredibly fast for dictionary implementations and autocomplete systems.
4. **Network Routing**: Spanning trees are used in routers to prevent loops (e.g., STP).

## 3. Types of Trees
### General Tree
A tree where each node can have either zero or many child nodes. There is no restriction on the degree of a node.

### Binary Tree
A tree where each node can have a maximum of **two children** (typically named `left` and `right`).

### Binary Search Tree (BST)
A specialized Binary Tree where:
- The left child's value is **less than** the parent's value.
- The right child's value is **greater than** the parent's value.
- This property applies recursively to all subtrees.

### Balanced Trees (AVL, Red-Black)
Self-balancing binary search trees that automatically adjust their height to remain $O(\log N)$ even after multiple skewed insertions.

## 4. Tree Traversal
Because trees are non-linear, they can be traversed in multiple ways:

### Depth-First Search (DFS)
Traverses deep into a branch before backtracking.
1. **In-Order (Left, Root, Right)**: Yields elements in sorted order for a BST.
2. **Pre-Order (Root, Left, Right)**: Useful for cloning/copying a tree.
3. **Post-Order (Left, Right, Root)**: Useful for deleting a tree.

### Breadth-First Search (BFS)
Traverses the tree level by level.
- **Level-Order**: Uses a Queue. Visits the root, then its children, then its grandchildren, etc.

## 5. Python Implementation Basics
A typical node in a Binary Tree is implemented using a class:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
