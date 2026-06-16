# Introduction to Data Structures

A **Data Structure** is a specialized format for organizing, processing, retrieving, and storing data. It is a way of arranging data on a computer so that it can be accessed and updated efficiently.

Choosing the right data structure is crucial for designing efficient algorithms and software. The choice depends heavily on what operations you need to perform (like searching, sorting, inserting, or deleting data) and how fast those operations need to be.

---

## 1. Types of Data Structures

Data structures are broadly classified into two main categories: **Primitive** and **Non-Primitive** (or Composite).

### A. Primitive Data Structures
These are the fundamental data types built directly into the programming language. They hold a single value and are the building blocks for more complex structures.
*   **Integer:** Represents whole numbers (e.g., `-5`, `0`, `42`).
*   **Float/Double:** Represents numbers with fractional parts (e.g., `3.14`, `-0.001`).
*   **Character/String:** Represents textual data (e.g., `'A'`, `"Hello World"`).
*   **Boolean:** Represents logical values (`True` or `False`).

### B. Non-Primitive Data Structures
These are more complex structures constructed from primitive data types. They are used to store and manage groups of related data. Non-primitive data structures are further divided into **Linear** and **Non-Linear** types.

#### I. Linear Data Structures
In linear data structures, elements are arranged sequentially, one after another. Each element is connected to its previous and next element. Because the data is laid out linearly, it is easy to traverse (visit every element), but operations like insertion or deletion might be slow.

1.  **Arrays (Lists in Python):**
    *   A collection of elements stored at contiguous memory locations.
    *   Elements can be accessed randomly using their index (e.g., `array[2]`).
    *   *Best for:* Fast access by index.
    *   *Downside:* Fixed size in many languages; inserting/deleting elements in the middle is slow because elements must be shifted.

2.  **Linked Lists:**
    *   A sequence of elements called "nodes." Each node contains data and a pointer (or link) to the next node in the sequence.
    *   Memory is not contiguous.
    *   *Types:* Singly Linked List, Doubly Linked List, Circular Linked List.
    *   *Best for:* Frequent insertions and deletions since elements don't need to be shifted.
    *   *Downside:* No random access; you must traverse from the beginning to reach a specific element.

3.  **Stacks:**
    *   Follows the **LIFO (Last In, First Out)** principle.
    *   The last element added is the first one to be removed.
    *   *Operations:* `push` (add), `pop` (remove), `peek` (view top).
    *   *Examples:* Undo feature in text editors, browser history, function call stack.

4.  **Queues:**
    *   Follows the **FIFO (First In, First Out)** principle.
    *   The first element added is the first one to be removed.
    *   *Operations:* `enqueue` (add to rear), `dequeue` (remove from front).
    *   *Examples:* Printer spooling, CPU task scheduling, waiting lines.

#### II. Non-Linear Data Structures
In non-linear data structures, elements are not arranged sequentially. Instead, elements are connected in a hierarchical or network-like manner. A single element can be connected to multiple other elements.

1.  **Trees:**
    *   A hierarchical structure consisting of nodes connected by edges. It has a single root node, and every node has zero or more child nodes.
    *   *Types:* Binary Tree, Binary Search Tree (BST), AVL Tree, Heap.
    *   *Best for:* Hierarchical data (like file systems), fast searching/sorting (like BSTs).
    *   *Example:* HTML DOM, File explorer directories.

2.  **Graphs:**
    *   A collection of nodes (called vertices) and the connections between them (called edges). Trees are actually a restricted type of graph.
    *   *Types:* Directed vs. Undirected, Weighted vs. Unweighted.
    *   *Best for:* Representing networks.
    *   *Example:* Social networks (friends), maps (navigation/GPS), computer networks.

3.  **Hash Tables (Dictionaries in Python):**
    *   Stores data in key-value pairs. It uses a "hash function" to compute an index into an array of buckets or slots, from which the desired value can be found.
    *   *Best for:* Extremely fast lookups, insertions, and deletions ($O(1)$ average time complexity).
    *   *Example:* Database indexing, caching, frequency counting.

---

## 2. Summary Table

| Data Structure | Type | Key Characteristic | Typical Use Case |
| :--- | :--- | :--- | :--- |
| **Array** | Linear | Fixed size, contiguous memory, random access | Storing sequential data |
| **Linked List** | Linear | Dynamic size, nodes with pointers | Frequent insertion/deletion |
| **Stack** | Linear | LIFO (Last In, First Out) | Undo mechanisms, Call stack |
| **Queue** | Linear | FIFO (First In, First Out) | Task scheduling, Buffers |
| **Tree** | Non-Linear | Hierarchical relationship | File systems, fast searching |
| **Graph** | Non-Linear | Vertices and edges representing networks | Social networks, Maps/Routing |
| **Hash Table** | Non-Linear (Key-Value) | Fast lookups using hash functions | Caching, Dictionaries |

Understanding these fundamental data structures and their trade-offs is the key to writing efficient and optimized code!
