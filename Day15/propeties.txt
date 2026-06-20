# Binary Search Tree (BST) Properties Cheat Sheet

## 1. Maximum Nodes at Level `i`

For any binary tree (including BST):

[
\text{Max Nodes at Level } i = 2^i
]

| Level | Max Nodes |
| ----- | --------- |
| 0     | 1         |
| 1     | 2         |
| 2     | 4         |
| 3     | 8         |

---

## 2. Maximum Nodes in a BST of Height `h`

[
\text{Max Nodes} = 2^{h+1} - 1
]

Example:

Height = 3

[
2^4 - 1 = 15
]

---

## 3. Minimum Nodes in a BST of Height `h`

A skewed BST has the minimum number of nodes.

[
\text{Min Nodes} = h + 1
]

Example:

Height = 4

[
4 + 1 = 5
]

---

## 4. Number of Edges

For any BST:

[
\text{Edges} = N - 1
]

Where:

* N = Total Nodes

Example:

Nodes = 10

Edges = 9

---

## 5. Number of NULL Links

For any BST:

[
\text{NULL Links} = N + 1
]

Example:

Nodes = 7

NULL Links = 8

---

## 6. Height from Number of Nodes

For a complete BST:

[
h = \lfloor \log_2 N \rfloor
]

Example:

[
N = 15
]

[
h = \lfloor \log_2 15 \rfloor = 3
]

---

## 7. Minimum Possible Height for N Nodes

[
h = \lceil \log_2 (N + 1) \rceil - 1
]

Example:

[
N = 31
]

[
h = 4
]

---

## 8. Perfect BST Properties

A Perfect BST has all levels completely filled.

### Total Nodes

[
\text{Nodes} = 2^{h+1} - 1
]

### Leaf Nodes

[
\text{Leaf Nodes} = 2^h
]

---

## 9. Full BST Property

A Full BST is a BST where every node has:

* 0 children, or
* 2 children

No node has exactly one child.

---

## 10. Complete BST Property

A Complete BST satisfies:

* Every level is completely filled except possibly the last level.
* Last level nodes are filled from left to right.

---

## 11. Balanced BST Property

For every node:

[
|Height(Left) - Height(Right)| \le 1
]

Examples:

* AVL Tree ✅
* Red-Black Tree (approximately balanced) ✅

---

## 12. BST Ordering Property (Most Important)

For every node:

[
Left\ Subtree < Root < Right\ Subtree
]

Example:

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

For node `8`:

* Left subtree values < 8
* Right subtree values > 8

---

## 13. Inorder Traversal Property

The inorder traversal of a BST always produces values in sorted order.

Example:

```
        5
       / \
      3   7
     / \ / \
    2  4 6  8
```

Inorder:

```
2 3 4 5 6 7 8
```

---

## 14. Best, Average and Worst Height

### Best Case (Perfect BST)

[
h = O(\log N)
]

### Average Case

[
h = O(\log N)
]

### Worst Case (Skewed BST)

[
h = O(N)
]

Example:

```
1
 \
  2
   \
    3
     \
      4
```

Height = N - 1

---

# BST Interview Quick Revision

| Property               | Formula                    |
| ---------------------- | -------------------------- |
| Max Nodes at Level i   | (2^i)                      |
| Max Nodes for Height h | (2^{h+1}-1)                |
| Min Nodes for Height h | (h+1)                      |
| Edges                  | (N-1)                      |
| NULL Links             | (N+1)                      |
| Height from N Nodes    | (\lfloor \log_2 N \rfloor) |
| Perfect BST Nodes      | (2^{h+1}-1)                |
| Perfect BST Leaves     | (2^h)                      |
| Full BST               | 0 or 2 children            |
| Complete BST           | Last level left-filled     |
| Balanced BST           | Height Difference ≤ 1      |
| BST Property           | Left < Root < Right        |
| Inorder Traversal      | Sorted Order               |
| Best/Average Height    | O(log N)                   |
| Worst Height           | O(N)                       |

### Important Interview Tip

A BST is useful because Search, Insert, and Delete operations take:

* **O(log N)** in a balanced BST
* **O(N)** in a skewed BST
