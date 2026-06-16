# Data Structures & Queues: Interview Questions and Answers

Here is a curated list of common interview questions focusing on general Data Structures and Queues specifically.

## General Data Structures

**1. What is a Data Structure?**
**Answer:** A data structure is a specialized format for organizing, processing, retrieving and storing data. It provides a way to manage large amounts of data efficiently for uses such as large databases and internet indexing services.

**2. What is the difference between Linear and Non-Linear data structures?**
**Answer:** In a linear data structure, data elements are arranged sequentially or linearly (e.g., Arrays, Linked Lists, Stacks, Queues). In a non-linear data structure, data elements are not arranged sequentially; instead, they are arranged in a hierarchical or interconnected manner (e.g., Trees, Graphs).

**3. When would you choose a Linked List over an Array?**
**Answer:** You should choose a Linked List when you need constant-time insertions and deletions from the list (such as in the middle of the list, provided you have a pointer to the node). Arrays are better when you need fast $O(1)$ random access to elements using an index.

**4. What is a Hash Table, and how does it handle collisions?**
**Answer:** A Hash Table is a data structure that maps keys to values for highly efficient lookup, insertion, and deletion ($O(1)$ average time). It uses a hash function to compute an index. Collisions (when two keys hash to the same index) are usually handled by Chaining (using a linked list at each index) or Open Addressing (probing for the next empty slot).

**5. What is the difference between a Stack and a Queue?**
**Answer:** A Stack follows the Last-In, First-Out (LIFO) principle, where the last element added is the first one to be removed. A Queue follows the First-In, First-Out (FIFO) principle, where the first element added is the first one to be removed.

---

## Queues

**6. What is a Queue?**
**Answer:** A Queue is a linear data structure that models a real-world queue or line. It operates on a First-In, First-Out (FIFO) basis, meaning the first element inserted is the first one to be deleted.

**7. What are the primary operations of a Queue?**
**Answer:** The primary operations are:
- `Enqueue`: Adds an item to the rear of the queue.
- `Dequeue`: Removes an item from the front of the queue.
- `Peek/Front`: Returns the item at the front without removing it.
- `isEmpty`: Checks if the queue has no elements.

**8. Why is it inefficient to use a standard Python `list` as a Queue?**
**Answer:** While appending to the end of a Python `list` is $O(1)$, removing from the front using `list.pop(0)` is $O(N)$ because all subsequent elements must be shifted one position to the left in memory.

**9. What is the preferred way to implement a Queue in Python?**
**Answer:** The preferred way is to use `collections.deque` (Double-Ended Queue), which is implemented as a doubly linked list under the hood. It provides $O(1)$ time complexity for appends and pops from both ends.

**10. What is a Circular Queue and why is it useful?**
**Answer:** A Circular Queue is an array-based queue where the last position is connected back to the first position to make a circle. It is useful for overcoming the limitation of a standard array-based queue where empty spaces at the front (left after dequeuing) cannot be reused if the rear pointer has reached the end of the array.

**11. What is a Priority Queue?**
**Answer:** A Priority Queue is an abstract data type similar to a regular queue, but every element has a "priority" associated with it. Elements with high priority are dequeued before elements with low priority. It is typically implemented using a Heap data structure.

**12. What is a Deque?**
**Answer:** A Deque (Double-Ended Queue) is a queue where insertion and deletion can be performed at both the front and the rear ends.

**13. Name some real-world applications of Queues.**
**Answer:** 
- CPU scheduling (e.g., Round Robin scheduling).
- Print spooling (managing documents sent to a printer).
- Handling asynchronous requests (like web server request queues).
- Breadth-First Search (BFS) algorithms in graphs and trees.

**14. How can you implement a Queue using Stacks?**
**Answer:** You can implement a queue using two stacks (`Stack1` and `Stack2`). For the `enqueue` operation, simply push elements onto `Stack1`. For the `dequeue` operation, if `Stack2` is empty, pop all elements from `Stack1` and push them onto `Stack2` (which reverses their order), then pop from `Stack2`. If `Stack2` is not empty, simply pop from `Stack2`.

**15. What are the time complexities of Queue operations?**
**Answer:** In a proper implementation (like a linked list or `collections.deque`), `Enqueue`, `Dequeue`, `Front/Peek`, and `isEmpty` all operate in $O(1)$ constant time.
