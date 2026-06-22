# Day 16 Notes

## 1. Binary Search Tree (BST)

A Binary Search Tree is a node-based binary tree data structure with the following properties:
- The left subtree of a node contains only nodes with keys lesser than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- The left and right subtree each must also be a binary search tree.

### Searching in a BST
To search for a value in a BST:
1. Start at the root node.
2. If the tree is empty or the root node matches the search value, return the root.
3. If the search value is less than the root's value, recursively search the left subtree.
4. If the search value is greater than the root's value, recursively search the right subtree.

### Deletion in a BST
Deleting a node from a BST is more complex as it must maintain the BST properties. There are three cases:
1. **Node to be deleted is a leaf:** Simply remove it from the tree.
2. **Node to be deleted has only one child:** Copy the child to the node and delete the child.
3. **Node to be deleted has two children:** Find the inorder successor (smallest value in the right subtree) or inorder predecessor (largest value in the left subtree) of the node. Copy its value to the node, and then recursively delete the inorder successor/predecessor.

### Time Complexity
- **Search:** Average $O(\log n)$, Worst $O(n)$
- **Insertion:** Average $O(\log n)$, Worst $O(n)$
- **Deletion:** Average $O(\log n)$, Worst $O(n)$
*(Worst case occurs when the tree is skewed, e.g., inserting sorted elements)*

---

## 2. Priority Queue & Heaps

### Priority Queue
A Priority Queue is an abstract data type similar to a regular queue or stack, but each element additionally has a "priority" associated with it. Elements with high priority are served before elements with low priority. It is typically implemented using a Heap.

### Heaps
A Heap is a special Tree-based data structure that satisfies the Heap Property. It's typically implemented as a complete binary tree (usually using an array/list).

There are two main types of heaps:

#### Min Heap
- In a Min Heap, the key present at the root node must be less than or equal to the keys present at all its children. The same property must be recursively true for all sub-trees in that Binary Tree.
- The smallest element is always at the root.
- Python's `heapq` module implements a Min Heap by default.

#### Max Heap
- In a Max Heap, the key present at the root node must be greater than or equal to the keys present at all its children. The same property must be recursively true for all sub-trees in that Binary Tree.
- The largest element is always at the root.
- In Python, you can simulate a Max Heap using `heapq` by multiplying the numerical values by -1 before pushing them, and multiplying by -1 again when popping.

---

## 3. Dictionaries, Sets, and Frequency Maps

### Dictionaries
A dictionary in Python is a collection of key-value pairs. It is unordered, mutable, and indexed by keys. Keys must be immutable (strings, numbers, tuples).

#### Common Dictionary Methods
- `dict.get(key, default)`: Returns the value for `key` if `key` is in the dictionary, else `default`.
- `dict.keys()`: Returns a view object displaying a list of all the keys.
- `dict.values()`: Returns a view object displaying a list of all the values.
- `dict.items()`: Returns a view object displaying a list of dictionary's `(key, value)` tuple pairs.
- `dict.pop(key, default)`: Removes the specified `key` and returns the corresponding value.
- `dict.update([other])`: Updates the dictionary with elements from another dictionary object or from an iterable of key/value pairs.

### Frequency Maps
A frequency map (or frequency counter) is a common pattern where a dictionary is used to count the occurrences of elements in a collection.

```python
# Example of building a frequency map
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq_map = {}
for item in data:
    freq_map[item] = freq_map.get(item, 0) + 1
print(freq_map) # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# Or using collections.Counter
from collections import Counter
freq_map = Counter(data)
```

### Sets
A set is an unordered collection of unique elements. It is mutable and can be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

#### Common Set Methods
- `set.add(elem)`: Adds element to the set.
- `set.remove(elem)`: Removes element from the set. Raises `KeyError` if not found.
- `set.discard(elem)`: Removes element from the set if it is present. Does not raise an error if not found.
- `set.union(other_set)` or `set | other_set`: Returns a new set with elements from both sets.
- `set.intersection(other_set)` or `set & other_set`: Returns a new set with elements common to both sets.
- `set.difference(other_set)` or `set - other_set`: Returns a new set with elements in the set that are not in the others.
- `set.issubset(other_set)` or `set <= other_set`: Tests whether every element in the set is in `other_set`.
