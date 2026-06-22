# Day 16 Interview Questions & Answers

## Binary Search Trees (BST)
**Q1: What is a Binary Search Tree and what are its key properties?**
**A1:** A BST is a node-based binary tree data structure where each node has at most two children. The key property is that the left subtree of a node contains only nodes with keys lesser than the node's key, and the right subtree contains only nodes with keys greater than the node's key.

**Q2: What are the time complexities for searching, inserting, and deleting in a BST?**
**A2:** In an average (balanced) case, all three operations take O(log n) time. In the worst case (when the tree is completely skewed, like a linked list), they take O(n) time.

**Q3: How does deletion work in a BST?**
**A3:** There are three cases:
1. Node is a leaf: simply remove it.
2. Node has one child: replace the node with its child.
3. Node has two children: find its in-order successor (smallest node in the right subtree) or in-order predecessor (largest node in the left subtree), copy its value to the node, and then recursively delete the successor/predecessor.

## Priority Queues and Heaps
**Q4: What is the difference between a Priority Queue and a Heap?**
**A4:** A Priority Queue is an abstract data type where each element has a priority, and elements with higher priority are served first. A Heap is a concrete data structure (usually an array representing a complete binary tree) that is most commonly used to implement a Priority Queue efficiently.

**Q5: Explain the difference between a Min-Heap and a Max-Heap.**
**A5:** In a Min-Heap, the root node has the minimum value, and every parent node is less than or equal to its children. In a Max-Heap, the root node has the maximum value, and every parent node is greater than or equal to its children.

**Q6: What are the time complexities of Heap operations?**
**A6:** 
- Getting the min/max (peek): O(1)
- Inserting an element: O(log n)
- Extracting (removing) the min/max: O(log n)
- Building a heap from an unordered array (heapify): O(n)

## Dictionaries, Sets, and Hashing
**Q7: How is a Dictionary (Hash Map) implemented in Python, and what are its time complexities?**
**A7:** It is implemented using a hash table. The average time complexity for lookup, insertion, and deletion is O(1). In the worst-case scenario (due to hash collisions), it can degrade to O(n), though this is rare with good hash functions.

**Q8: When would you use a Set instead of a Dictionary?**
**A8:** A Set is used when you only need to store unique elements and check for their existence (membership testing), without associating a specific value with them.

**Q9: What is a frequency map?**
**A9:** A frequency map is a hash map (dictionary) where the keys represent elements from a collection, and the values represent the number of times each element appears in the collection.

**Q10: Why must dictionary keys be immutable in Python?**
**A10:** Dictionary keys must be hashable, meaning their hash value must never change during their lifetime. If keys were mutable (like lists), modifying them would change their hash value, breaking the internal mapping of the hash table and making the elements unretrievable.
