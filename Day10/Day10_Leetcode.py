# Day 10 Leetcode Problems: Introduction to Linked Lists
# These problems test your ability to traverse a Linked List.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ==================================================
# Problem 1: Leetcode 1290 - Convert Binary Number in a Linked List to Integer
# Difficulty: Easy
# ==================================================
# Given `head` which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

def getDecimalValue(head: ListNode) -> int:
    # We traverse the linked list and shift our result bitwise
    # (or multiply by 2) for each new digit we encounter.
    
    num = 0
    current = head
    while current:
        num = num * 2 + current.val
        current = current.next
        
    return num

# Dry Run for list: 1 -> 0 -> 1 (which is binary for 5)
# num = 0
# Node(1): num = 0 * 2 + 1 = 1
# Node(0): num = 1 * 2 + 0 = 2
# Node(1): num = 2 * 2 + 1 = 5
# Return 5.


# ==================================================
# Problem 2: Leetcode 876 - Middle of the Linked List
# Difficulty: Easy
# ==================================================
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

def middleNode(head: ListNode) -> ListNode:
    # Approach 1: Count all nodes (O(n)), then traverse to count // 2.
    # Approach 2: "Tortoise and Hare" (Fast & Slow Pointers).
    # The fast pointer moves 2 steps, slow moves 1 step. 
    # When fast reaches the end, slow is exactly in the middle!
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # moves 1 step
        fast = fast.next.next     # moves 2 steps
        
    return slow

# Dry Run for list: 1 -> 2 -> 3 -> 4 -> 5 -> None
# Init: slow=1, fast=1
# Step 1: slow=2, fast=3
# Step 2: slow=3, fast=5
# Step 3: fast.next is None. Loop ends.
# Return slow (Node 3).


# ==================================================
# Problem 3: Valid Parentheses (Easy)
# ==================================================
# Opening brackets go into stack. Closing brackets must match top.
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack: return False
            if stack.pop() != mapping[ch]: return False
    return len(stack) == 0

# ==================================================
# Problem 4: Baseball Game (Easy)
# ==================================================
# Integer -> Push, C -> Remove last, D -> Double last, + -> Sum last two
def calPoints(operations: list[str]) -> int:
    stack = []
    for op in operations:
        if op == "C": stack.pop()
        elif op == "D": stack.append(stack[-1] * 2)
        elif op == "+": stack.append(stack[-1] + stack[-2])
        else: stack.append(int(op))
    return sum(stack)

# ==================================================
# Problem 5: Backspace String Compare (Easy)
# ==================================================
# Character -> Push, # -> Pop
def backspaceCompare(s: str, t: str) -> bool:
    def build(string):
        stack = []
        for ch in string:
            if ch == "#":
                if stack: stack.pop()
            else: stack.append(ch)
        return "".join(stack)
    return build(s) == build(t)

# ==================================================
# Problem 6: Remove Outermost Parentheses (Easy)
# ==================================================
def removeOuterParentheses(s: str) -> str:
    result = []
    count = 0
    for ch in s:
        if ch == '(':
            if count > 0: result.append(ch)
            count += 1
        else:
            count -= 1
            if count > 0: result.append(ch)
    return "".join(result)

# ==================================================
# Problem 7: Make The String Great (Easy)
# ==================================================
# Remove adjacent uppercase/lowercase pair.
def makeGood(s: str) -> str:
    stack = []
    for ch in s:
        if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
            stack.pop()
        else: stack.append(ch)
    return "".join(stack)

# ==================================================
# Problem 8: Removing Stars From a String (Medium but Easy)
# ==================================================
def removeStars(s: str) -> str:
    stack = []
    for ch in s:
        if ch == '*': stack.pop()
        else: stack.append(ch)
    return "".join(stack)

# ==================================================
# Problem 9: Next Greater Element I (Easy)
# ==================================================
# Pattern: Monotonic decreasing stack.
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    nge = {}
    for num in nums2:
        while stack and stack[-1] < num:
            nge[stack.pop()] = num
        stack.append(num)
    while stack:
        nge[stack.pop()] = -1
    return [nge[num] for num in nums1]

# ==================================================
# Problem 10: Daily Temperatures (Medium)
# ==================================================
# Pattern: Store indexes in a monotonic stack.
def dailyTemperatures(temp: list[int]) -> list[int]:
    stack = []
    result = [0] * len(temp)
    for i in range(len(temp)):
        while stack and temp[stack[-1]] < temp[i]:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)
    return result

# ==================================================
# Problem 11: Evaluate Reverse Polish Notation (Medium)
# ==================================================
def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+": stack.append(a + b)
            elif token == "-": stack.append(a - b)
            elif token == "*": stack.append(a * b)
            else: stack.append(int(a / b))
    return stack[0]

# ==================================================
# Problem 12: Decode String (Medium)
# ==================================================
def decodeString(s: str) -> str:
    stack = []
    curr = ""
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            stack.append((curr, num))
            curr = ""
            num = 0
        elif ch == ']':
            prev, count = stack.pop()
            curr = prev + curr * count
        else: curr += ch
    return curr

if __name__ == "__main__":
    # Test Problem 1 (Linked List)
    ll1 = ListNode(1, ListNode(0, ListNode(1)))
    print("Decimal Value (101):", getDecimalValue(ll1))
    
    # Test Problem 2 (Linked List)
    ll2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Middle Node (1->2->3->4->5):", middleNode(ll2).val)
    
    # Test Stack Problems
    print("Valid Parentheses '()[]{}':", isValid("()[]{}"))
    print("Daily Temps [73,74,75,71,69,72,76,73]:", dailyTemperatures([73,74,75,71,69,72,76,73]))
