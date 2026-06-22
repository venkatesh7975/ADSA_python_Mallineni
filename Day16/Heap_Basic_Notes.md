# 1. Heap

A **Heap** is a **Complete Binary Tree** that follows a special property.

### Complete Binary Tree

```text
        10
       /  \
      20   30
     / \
    40  50
```

All levels are completely filled except possibly the last level, and nodes are filled from left to right.

---

## Why Heap?

Heap is used when we need:

* Fast access to Minimum element
* Fast access to Maximum element
* Priority-based processing

Examples:

* Task Scheduling
* CPU Scheduling
* Dijkstra Algorithm
* Top K Problems
* Priority Queue

---

# 2. Min Heap

### Property

Every parent is **smaller than or equal to its children**.

```text
        5
       / \
      10  20
     / \
    30 40
```

Smallest element is always at root.

### Example

Insert:

```text
10, 20, 5, 30, 40
```

Min Heap:

```text
        5
       / \
      10 20
     / \
    30 40
```

### Access Minimum

```python
import heapq

nums = [10, 20, 5, 30]

heapq.heapify(nums)

print(nums[0])
```

Output:

```text
5
```

---

## Problem: Kth Smallest Element

Given:

```python
nums = [7, 10, 4, 3, 20, 15]
k = 3
```

Sorted:

```text
3 4 7 10 15 20
```

3rd Smallest = 7

Min Heap helps efficiently find smallest elements.

---

# 3. Max Heap

### Property

Every parent is **greater than or equal to its children**.

```text
        50
       /  \
      30   40
     / \
    10 20
```

Largest element is always at root.

---

### Example

Insert:

```text
50, 30, 40, 10, 20
```

Max Heap:

```text
        50
       / \
      30 40
     / \
    10 20
```

---

### Python Max Heap

Python provides only Min Heap.

Use negative values:

```python
import heapq

max_heap = []

heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -50)
heapq.heappush(max_heap, -30)

print(-heapq.heappop(max_heap))
```

Output:

```text
50
```

---

## Problem: Kth Largest Element

Given:

```python
nums = [3,2,1,5,6,4]
k = 2
```

Sorted:

```text
6 5 4 3 2 1
```

2nd Largest = 5

Max Heap is commonly used.

LeetCode: 215

---

# 4. Priority Queue

A Priority Queue processes elements according to priority rather than insertion order.

---

### Normal Queue

```text
Insert:
10
20
30

Delete:
10
20
30
```

FIFO

---

### Priority Queue

```text
Priority 1 -> Emergency
Priority 2 -> Doctor
Priority 3 -> Patient
```

Deletion:

```text
Emergency
Doctor
Patient
```

Highest priority comes first.

---

### Python

```python
from queue import PriorityQueue

pq = PriorityQueue()

pq.put((2, "Doctor"))
pq.put((1, "Emergency"))
pq.put((3, "Patient"))

while not pq.empty():
    print(pq.get())
```

Output:

```text
(1, 'Emergency')
(2, 'Doctor')
(3, 'Patient')
```

---

## Problem: Merge K Sorted Lists

Given:

```text
List1 = 1 -> 4 -> 5
List2 = 1 -> 3 -> 4
List3 = 2 -> 6
```

Output:

```text
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

A Priority Queue always gives the smallest current node among all lists.

LeetCode: 23

---

# Interview Summary

| Data Structure | Root Contains            |
| -------------- | ------------------------ |
| Min Heap       | Smallest Element         |
| Max Heap       | Largest Element          |
| Priority Queue | Highest Priority Element |

| Structure      | Insert   | Delete Top |
| -------------- | -------- | ---------- |
| Heap           | O(log n) | O(log n)   |
| Priority Queue | O(log n) | O(log n)   |

### One-Line Memory Trick

```text
Heap → Complete Binary Tree

Min Heap → Parent ≤ Children

Max Heap → Parent ≥ Children

Priority Queue → Serve by Priority, not Arrival Time
```

### Most Important Heap Problems

1. Kth Largest Element in an Array (LeetCode 215)
2. Top K Frequent Elements (LeetCode 347)
3. Last Stone Weight (LeetCode 1046)
4. Merge K Sorted Lists (LeetCode 23)
5. Find Median from Data Stream (LeetCode 295)

These 5 problems cover nearly all beginner-to-intermediate heap concepts.
