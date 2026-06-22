# Min-Heap (and Max-Heap) Array Index Properties

A Heap is almost always implemented using an array (or a list in Python) because a **Complete Binary Tree** can be mapped directly to an array continuously without any gaps or wasted space.

Depending on whether you start placing elements at index `0` or index `1`, the mathematical formulas to traverse the tree (finding parents and children) change slightly.

---

## 1. Zero-Indexed Array (Standard in Python, Java, C++)

If the root element is placed at index `0` (which is the default way lists work in Python):

For any given node at index `i`:
* **Left Child Index:** `(2 * i) + 1`
* **Right Child Index:** `(2 * i) + 2`
* **Parent Index:** `(i - 1) // 2`  *(using floor division)*

### Example (0-Indexed)
```text
Array:   [5, 10, 20, 30, 40]
Indices:  0,  1,  2,  3,  4

Tree representation:
          5  (idx 0)
         / \
(idx 1) 10  20 (idx 2)
       /  \
(idx 3)30 40 (idx 4)
```
* Left child of root (`i = 0`): `(2 * 0) + 1 = 1` ➔ Value `10`
* Right child of root (`i = 0`): `(2 * 0) + 2 = 2` ➔ Value `20`
* Parent of node `40` (`i = 4`): `(4 - 1) // 2 = 1` ➔ Value `10`

---

## 2. One-Indexed Array (Often used in textbooks to simplify math)

If the root element is placed at index `1` (usually achieved in code by putting a dummy value like `None` or `0` at index `0`):

For any given node at index `i`:
* **Left Child Index:** `2 * i`
* **Right Child Index:** `(2 * i) + 1`
* **Parent Index:** `i // 2`  *(using floor division)*

### Example (1-Indexed)
```text
Array:   [None, 5, 10, 20, 30, 40]
Indices:   0,   1,  2,  3,  4,  5

Tree representation:
          5  (idx 1)
         / \
(idx 2) 10  20 (idx 3)
       /  \
(idx 4)30 40 (idx 5)
```
* Left child of root (`i = 1`): `2 * 1 = 2` ➔ Value `10`
* Right child of root (`i = 1`): `(2 * 1) + 1 = 3` ➔ Value `20`
* Parent of node `40` (`i = 5`): `5 // 2 = 2` ➔ Value `10`

---

## 3. Additional Key Properties

1. **Leaf Nodes (0-Indexed):** All nodes starting from index `(n // 2)` all the way to `(n - 1)` are strictly leaf nodes (where `n` is the total number of elements in the heap). They have no children.
2. **Internal Nodes:** Conversely, nodes from index `0` to `(n // 2) - 1` are internal nodes and have at least one child.
3. **Height:** The height of a heap with `n` elements is `floor(log2(n))`. Because it is a complete binary tree, the tree is perfectly balanced, which guarantees `O(log n)` time complexity for insertions (`heappush`) and deletions (`heappop`).
