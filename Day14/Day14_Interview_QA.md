# Day 14: Interview Questions and Answers on Trees

## Basics & Properties
1. **What is a Tree?** A hierarchical, non-linear data structure consisting of nodes and edges.
2. **What is a Binary Tree?** A tree where every node has at most two children.
3. **What is a Binary Search Tree (BST)?** A binary tree where the left child is smaller and the right child is greater than the parent.
4. **What is the maximum number of nodes at level `L` of a binary tree?** $2^L$ (where root is at level 0).
5. **What is the maximum number of nodes in a binary tree of height `H`?** $2^{H+1} - 1$.
6. **What is a Full Binary Tree?** Every node has exactly 0 or 2 children.
7. **What is a Complete Binary Tree?** All levels are completely filled except possibly the last, which is filled from left to right.
8. **What is a Perfect Binary Tree?** All internal nodes have two children and all leaves are at the same level.
9. **What is a Degenerate (or Pathological) Tree?** A tree where every internal node has only one child (essentially a linked list).

## Traversals
10. **What is In-order Traversal?** Left, Root, Right.
11. **What is Pre-order Traversal?** Root, Left, Right.
12. **What is Post-order Traversal?** Left, Right, Root.
13. **Which traversal yields a sorted sequence for a BST?** In-order traversal.
14. **Which traversal is used to delete a tree?** Post-order, because you must delete children before the parent.
15. **Which traversal is used to copy a tree?** Pre-order.
16. **What is Level-order Traversal?** Visiting nodes level by level using Breadth-First Search (BFS) and a Queue.
17. **Can you uniquely reconstruct a binary tree from In-order and Pre-order traversals?** Yes.
18. **Can you reconstruct it from Pre-order and Post-order?** No, except if it's a Full Binary Tree.

## Complexities
19. **What is the time complexity to search in a BST?** $O(\log N)$ on average, $O(N)$ in the worst case (degenerate tree).
20. **How do you prevent the $O(N)$ worst-case in a BST?** By using Self-Balancing trees like AVL or Red-Black trees.
21. **What is the space complexity of DFS traversals?** $O(H)$ where $H$ is the height of the tree (for the recursion stack).
22. **What is the space complexity of BFS?** $O(W)$ where $W$ is the maximum width of the tree.
23. **Is recursion always best for trees?** While elegant, recursion can cause stack overflows on very deep trees. Iterative approaches using an explicit stack are safer.

## Algorithmic Scenarios
24. **How to find the lowest common ancestor (LCA) in a BST?** Traverse down; the first node whose value is between the two target nodes is the LCA.
25. **How to find LCA in a standard Binary Tree?** Recursively search left and right. If a node has targets in both subtrees, it is the LCA.
26. **How to invert/reverse a Binary Tree?** Recursively swap the left and right children of every node.
27. **How to check if two trees are identical?** Recursively verify that current nodes match, and both left and right subtrees match.
28. **How to check if a tree is a subtree of another?** Find the root of the subtree in the main tree, then check if they are identical.
29. **What is a Threaded Binary Tree?** A binary tree where `Null` right pointers are replaced by threads pointing to the in-order successor, eliminating the need for a stack during in-order traversal.
30. **How do you serialize and deserialize a binary tree?** Serialization converts it to a string using pre-order or level-order traversal with `Null` markers. Deserialization parses the string back into a tree.
