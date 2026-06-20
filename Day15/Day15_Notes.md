# Day 15: Hashing, Sets, Frequency Maps & BST Mastery

Welcome to Day 15! Today we focus on some of the most powerful and frequently used tools in technical interviews: **Hash Maps (Dictionaries)**, **Sets**, and **Binary Search Trees (BST)**.

---

## 1. Hashing & Dictionaries (Hash Maps)

### What is Hashing?
Hashing is the process of converting a given key into a specific index in a data array (called a hash table) using a **hash function**. It allows for $O(1)$ average time complexity for lookups, insertions, and deletions.

### Dictionaries in Python
In Python, Hash Maps are implemented via the built-in `dict` type.
- **Lookup/Insert/Delete**: $O(1)$ average time.
- **Under the Hood**: Uses open addressing to resolve collisions.
- **Best For**: Counting occurrences, caching/memoization, pairing values (e.g., Two Sum).

### Frequency Maps
A **Frequency Map** is a dictionary where the keys are elements from a collection, and the values are the counts of those elements.
```python
from collections import Counter
# Example: Counting frequencies in one line
freq = Counter([1, 2, 2, 3, 3, 3]) 
# freq -> {3: 3, 2: 2, 1: 1}
```

---

## 2. Sets

A **Set** is a collection of distinct (unique) elements. In Python, it is implemented using a hash table where the values are dummy objects.
- **Operations**: Add, Remove, Check Membership (`in`).
- **Time Complexity**: $O(1)$ average time.
- **Best For**: Removing duplicates, rapid existence checks, set math (Unions, Intersections, Differences).

```python
seen = set()
seen.add(5)
if 5 in seen:  # O(1) time
    print("Found!")
```

---

## 3. Binary Search Tree (BST) Problem Solving

While we introduced BSTs yesterday, today we focus on solving advanced LeetCode problems with them.

### Core BST Properties to Remember
1. **In-order Traversal**: Left -> Root -> Right **always yields a strictly sorted array**.
2. **Search Logic**: Every decision discards half the tree (in a balanced BST), yielding $O(\log N)$ time.
3. **Successor/Predecessor**: The in-order successor of a node is the minimum value in its right subtree. The predecessor is the maximum value in its left subtree.

### Combining BSTs and Hash Maps
Often, we use a Hash Map (like a frequency map or cache) while traversing a BST to solve complex problems like:
- **Two Sum IV (Input is a BST)**: Traverse the BST and use a `set` to check if `target - current_node.val` exists.
- **Find Mode in BST**: Use an in-order traversal to populate a `Counter` dictionary, then extract the mode(s).

### Hash Collisions
When two different keys hash to the same index, a collision occurs.
- **Chaining**: Using a Linked List at each index to hold multiple values.
- **Open Addressing**: Finding the next available slot in the array (Python uses a form of this called random probing).
