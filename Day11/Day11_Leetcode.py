"""
Day 11: Queue LeetCode Problems

1. Implement Stack using Queues (LeetCode 225)
2. Implement Queue using Stacks (LeetCode 232)
"""
from collections import deque

# ---------------------------------------------------------
# LeetCode 225: Implement Stack using Queues
# ---------------------------------------------------------
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # Rotate the queue to make the newly added element the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

# ---------------------------------------------------------
# LeetCode 232: Implement Queue using Stacks
# ---------------------------------------------------------
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

if __name__ == "__main__":
    print("Testing MyStack (Queue as Stack):")
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print("Top should be 2:", stack.top())
    print("Pop should be 2:", stack.pop())
    print("Is empty?:", stack.empty())
    
    print("\nTesting MyQueue (Stack as Queue):")
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print("Peek should be 1:", queue.peek())
    print("Pop should be 1:", queue.pop())
    print("Is empty?:", queue.empty())
