"""
Day 13: Linked List LeetCode Problems & Solutions
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ==========================================
# 1. Reverse Linked List (Easy)
# LeetCode 206
# ==========================================
def reverseList(head: ListNode) -> ListNode:
    """
    Reverses a singly linked list.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    prev = None
    curr = head
    
    while curr:
        next = curr.next  # Store next node
        curr.next = prev       # Reverse the pointer
        prev = curr            # Move prev forward
        curr = next     # Move curr forward
        
    return prev

# ==========================================
# 2. Merge Two Sorted Lists (Easy)
# LeetCode 21
# ==========================================
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists into one sorted linked list.
    Time Complexity: O(N + M)
    Space Complexity: O(1)
    """
    dummy = ListNode(-1)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
        
    # Append any remaining elements
    current.next = list1 if list1 else list2
    
    return dummy.next

# ==========================================
# 3. Linked List Cycle (Easy)
# LeetCode 141
# ==========================================
def hasCycle(head: ListNode) -> bool:
    """
    Detects if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps
        
        if slow == fast:          # Cycle detected
            return True
            
    return False

# ==========================================
# 4. Middle of the Linked List (Easy)
# LeetCode 876
# ==========================================
def middleNode(head: ListNode) -> ListNode:
    """
    Finds the middle node of a linked list.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

# ==========================================
# 5. Remove Nth Node From End of List (Medium)
# LeetCode 19
# ==========================================
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    Removes the nth node from the end of the list and returns its head.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    dummy = ListNode(0, head)
    slow = dummy
    fast = head
    
    # Move fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next
        
    # Move both pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next
        
    # Remove the nth node
    slow.next = slow.next.next
    
    return dummy.next


# Helper function to print lists
def print_list(head):
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print(" -> ".join(elements) + " -> None")

if __name__ == "__main__":
    # Test Reverse Linked List
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original List:")
    print_list(head)
    print("Reversed List:")
    print_list(reverseList(head))
