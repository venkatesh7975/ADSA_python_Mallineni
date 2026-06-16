"""
Day 11: Queue Practice Problems
"""
from collections import deque

# Problem 1: Implement a basic Queue class using collections.deque
class SimpleQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Problem 2: Reverse a Queue
# Given a queue, write a function to reverse it using a stack
def reverse_queue(q):
    stack = []
    
    # 1. Dequeue all elements and push onto stack
    while not q.is_empty():
        stack.append(q.dequeue())
        
    # 2. Pop all elements from stack and enqueue back to queue
    while stack:
        q.enqueue(stack.pop())
        
    return q

# Problem 3: Generate Binary Numbers from 1 to N using a Queue
def generate_binary_numbers(n):
    result = []
    q = deque()
    q.append("1")
    
    while n > 0:
        n -= 1
        s1 = q.popleft()
        result.append(s1)
        
        s2 = s1
        q.append(s1 + "0")
        q.append(s2 + "1")
        
    return result

if __name__ == "__main__":
    print("--- Problem 1: Simple Queue ---")
    sq = SimpleQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    print("Dequeue:", sq.dequeue()) # 10
    print("Front:", sq.front())     # 20
    
    print("\n--- Problem 2: Reverse Queue ---")
    q2 = SimpleQueue()
    for i in range(1, 6): q2.enqueue(i)
    reverse_queue(q2)
    print("Front after reverse:", q2.front()) # 5
    
    print("\n--- Problem 3: Binary Numbers ---")
    print(generate_binary_numbers(5)) # ['1', '10', '11', '100', '101']
