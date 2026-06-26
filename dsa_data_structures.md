# Data Structures - Interview Questions

This document covers fundamental Data Structures commonly asked in technical interviews, including Arrays, Strings, Linked Lists, Stacks, Queues, Trees, Heaps, and Hash Maps.

## 1. Arrays and Strings

**Q1. What is an Array? How is it represented in memory?**
**A:** An array is a collection of items stored at contiguous memory locations. Because the elements are contiguous, you can calculate the memory address of any element instantly if you know the starting address and the size of each element. This gives arrays an $O(1)$ time complexity for accessing elements by index. 
*Note: In Python, `list` is implemented as a dynamic array.*

**Q2. What is a Dynamic Array (like Python's `list`)?**
**A:** A dynamic array automatically resizes itself when it runs out of capacity. Under the hood, it allocates a fixed-size array. When it gets full, it allocates a new array (typically double the size), copies the old elements over, and frees the old array. While appending usually takes $O(1)$ time, when a resize happens, it takes $O(n)$ time. We call this an **amortized** $O(1)$ time complexity.

**Q3. How do you reverse an array/string in place?**
**A:** You use the **Two Pointers** technique. Set one pointer at the start (index 0) and one at the end (length - 1). Swap the elements at the two pointers, increment the start pointer, decrement the end pointer, and repeat until the pointers meet or cross.
```python
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

**Q4. What is a String? Why are strings immutable in Python?**
**A:** A string is a sequence of characters. In Python, strings are immutable, meaning once created, they cannot be changed. This provides several benefits:
- **Safety:** Strings are frequently used as keys in dictionaries. Immutability guarantees the hash value won't change.
- **Memory Efficiency:** Python optimizes memory by reusing identical string objects (string interning).

## 2. Linked Lists

**Q5. What is a Linked List? What are its advantages over an Array?**
**A:** A linked list is a linear data structure where elements (nodes) are not stored contiguously. Each node points to the next node. 
- **Advantages over Arrays:** Dynamic size, no memory waste from pre-allocation. Insertions and deletions at the beginning (or at a known node) take $O(1)$ time, whereas in an array they take $O(n)$ because subsequent elements must be shifted.
- **Disadvantages:** Cannot access elements randomly by index ($O(n)$ access time). Requires extra memory to store pointers.

**Q6. What is the difference between a Singly Linked List and a Doubly Linked List?**
**A:** 
- **Singly:** Each node contains data and a single pointer to the next node. You can only traverse forward.
- **Doubly:** Each node contains data, a pointer to the next node, and a pointer to the previous node. This allows traversal in both directions and makes deleting a known node $O(1)$ (since you know its predecessor), but it requires more memory per node.

**Q7. How do you detect a cycle in a Linked List?**
**A:** Use **Floyd's Cycle-Finding Algorithm (Tortoise and Hare)**. Use two pointers moving at different speeds (one moves 1 step, the other moves 2 steps). If there is a cycle, the fast pointer will eventually catch up to the slow pointer and they will meet. If the fast pointer reaches `None`, there is no cycle.

## 3. Stacks and Queues

**Q8. What is a Stack? Where are they used?**
**A:** A Stack is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The last element added is the first one removed.
- **Use cases:** Function call stacks (recursion), Undo mechanisms in text editors, matching parentheses problems, Depth-First Search (DFS) iteratively.
- **Implementation:** In Python, a simple `list` can be used as a stack using `append()` and `pop()`.

**Q9. What is a Queue? Where are they used?**
**A:** A Queue is a linear data structure that follows the **FIFO (First In, First Out)** principle. The first element added is the first one removed.
- **Use cases:** Task scheduling, message queues, Breadth-First Search (BFS) algorithms.
- **Implementation:** In Python, use `collections.deque` (Double-Ended Queue). A standard `list` is bad for queues because removing from the front (`pop(0)`) takes $O(n)$ time. `deque.popleft()` takes $O(1)$ time.

## 4. Hash Maps / Hash Tables

**Q10. What is a Hash Table and how does it work?**
**A:** A Hash Table (implemented as `dict` in Python) is a data structure that maps keys to values for highly efficient lookups.
It uses a **Hash Function** to compute an index (hash code) into an array of buckets or slots, from which the desired value can be found. On average, it provides $O(1)$ time complexity for insertions, deletions, and lookups.

**Q11. What is a Hash Collision? How is it resolved?**
**A:** A collision occurs when the hash function maps two different keys to the same bucket index.
Common resolution techniques:
1. **Chaining:** Each bucket contains a linked list. If a collision occurs, the new key-value pair is simply appended to the linked list at that bucket.
2. **Open Addressing:** If the bucket is occupied, probe the array for the next available empty bucket (e.g., linear probing, quadratic probing).

## 5. Trees and Graphs

**Q12. What is a Binary Tree?**
**A:** A hierarchical data structure consisting of nodes. Each node has a maximum of two children, typically referred to as the left child and right child.

**Q13. What is a Binary Search Tree (BST)?**
**A:** A special type of Binary Tree that enforces a specific property: For every node, all values in its left subtree must be less than the node's value, and all values in its right subtree must be greater than the node's value. 
This allows for efficient searching, insertion, and deletion, typically taking $O(\log n)$ time (though in the worst case of a completely unbalanced tree, it can degrade to $O(n)$).

**Q14. Explain Tree Traversals (Inorder, Preorder, Postorder).**
**A:** These are Depth-First traversal strategies:
- **Inorder (Left, Root, Right):** Visits left subtree, then the node, then right subtree. In a BST, this prints nodes in sorted ascending order.
- **Preorder (Root, Left, Right):** Visits the node first, then left subtree, then right subtree. Useful for copying a tree.
- **Postorder (Left, Right, Root):** Visits left, then right, then the node itself. Useful for deleting a tree from the bottom up.

**Q15. What is a Graph? How is it represented?**
**A:** A Graph is a non-linear data structure consisting of Vertices (Nodes) connected by Edges. They can be directed or undirected, weighted or unweighted.
Representations:
- **Adjacency Matrix:** A 2D array of size $V \times V$ where $matrix[i][j]$ is 1 if there is an edge between $i$ and $j$, else 0. Good for dense graphs. Takes $O(V^2)$ space.
- **Adjacency List:** An array/dictionary where the key is a vertex, and the value is a list of its neighbors. Good for sparse graphs. Takes $O(V + E)$ space.

## 6. Heaps

**Q16. What is a Heap?**
**A:** A Heap is a specialized tree-based data structure that satisfies the heap property:
- **Max-Heap:** The value of every parent node is greater than or equal to the values of its children. The largest element is always at the root.
- **Min-Heap:** The value of every parent node is less than or equal to the values of its children. The smallest element is always at the root.
Heaps are typically implemented as complete binary trees stored in an array.

**Q17. Where are Heaps used?**
**A:** Heaps are heavily used to implement **Priority Queues** (where the highest/lowest priority element is always removed first) and in the **HeapSort** algorithm. In Python, you can use the `heapq` module (which provides a Min-Heap by default). Finding the minimum takes $O(1)$, while inserting and popping takes $O(\log n)$.
