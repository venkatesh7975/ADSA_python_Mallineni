# Day 11 Detailed Notes: Queues

## What is a Queue?

A **Queue** is a linear data structure that follows a particular order in which the operations are performed. The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first.

Unlike stacks, a queue is open at both its ends. One end is always used to insert data (enqueue) and the other is used to remove data (dequeue).

### The FIFO Principle
**FIFO** stands for **First In, First Out**. 
Think of a line at a ticket counter:
- The first person to join the line is the first one to get a ticket and leave.
- If you join the line last, you will be served last.

### Key Operations of a Queue:
1. **Enqueue:** Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
2. **Dequeue:** Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.
3. **Front:** Get the front item from queue.
4. **Rear:** Get the last item from queue.

---

## 1. Implementing a Queue in Python

In Python, a queue can be implemented in several ways:

### Method 1: Using `list`
While lists in Python can be used as queues, they are highly inefficient for this purpose. 
Using `append()` to enqueue is fast ($O(1)$), but using `pop(0)` to dequeue is slow ($O(N)$) because all other elements have to be shifted by one position.

```python
queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Initial queue:", queue)

# Dequeue
print("Dequeued:", queue.pop(0))
print("Queue after dequeue:", queue)
```

### Method 2: Using `collections.deque`
`deque` (Double Ended Queue) is the preferred way to implement a queue in Python. It provides $O(1)$ time complexity for append and pop operations from both ends.

```python
from collections import deque

queue = deque()

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Initial queue:", queue)

# Dequeue
print("Dequeued:", queue.popleft())
print("Queue after dequeue:", queue)
```

---

## 2. Advanced Queue Types

### Circular Queue
In a standard queue, if the rear reaches the end, we cannot insert more elements even if there is empty space at the front (due to dequeuing). A circular queue overcomes this by connecting the last position back to the first position, making a circle. It is also called a "Ring Buffer".

### Deque (Double Ended Queue)
In a deque, insertion and deletion can occur at both the front and the rear ends. It does not strictly follow FIFO.

### Priority Queue
A priority queue is a special type of queue in which each element is associated with a priority value. Elements are served on the basis of their priority rather than their order in the queue.

---

## 3. Real-world Applications of Queues

1. **CPU Scheduling:** Operating systems use queues to schedule tasks for the CPU to execute.
2. **Print Spooling:** Documents sent to a printer are queued and printed in the order they were received.
3. **Handling asynchronous requests:** In web servers, incoming requests are often placed in a queue.
4. **Breadth-First Search (BFS):** Graph algorithms like BFS use queues to keep track of nodes to visit next.
