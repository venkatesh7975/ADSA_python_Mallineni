"""
Day 12: Singly Linked List Implementation
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        """Delete the first occurrence of a key in the list."""
        temp = self.head

        # If head node itself holds the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp == None:
            print(f"Value {key} not found in the list.")
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    def display(self):
        """Print all elements in the linked list."""
        elements = []
        temp = self.head
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements) + " -> None")


if __name__ == "__main__":
    print("Testing Singly Linked List:")
    sll = SinglyLinkedList()
    
    sll.insertAtEnd(10)
    sll.insertAtEnd(20)
    sll.insertAtBeginning(5)
    sll.insertAtEnd(30)
    
    print("List after insertions:")
    sll.display()  # Expected: 5 -> 10 -> 20 -> 30 -> None
    
    sll.deleteNode(20)
    print("List after deleting 20:")
    sll.display()  # Expected: 5 -> 10 -> 30 -> None
    
    sll.deleteNode(5)
    print("List after deleting head (5):")
    sll.display()  # Expected: 10 -> 30 -> None
