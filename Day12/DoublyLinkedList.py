"""
Day 12: Doubly Linked List Implementation
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
            
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
        new_node.prev = last

    def deleteNode(self, key):
        """Delete the first occurrence of a key in the list."""
        temp = self.head

        # Find the node with the matching key
        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next

        # If key was not found
        if temp is None:
            print(f"Value {key} not found in the list.")
            return

        # If the node to be deleted is the head node
        if temp == self.head:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
        else:
            # Change the next pointer of the previous node
            temp.prev.next = temp.next
            
            # Change the prev pointer of the next node
            if temp.next is not None:
                temp.next.prev = temp.prev
                
        temp = None # Free memory (handled by GC in Python)

    def displayForward(self):
        """Print all elements from Head to Tail."""
        elements = []
        temp = self.head
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print("Forward: " + " <-> ".join(elements) + " -> None")

    def displayBackward(self):
        """Print all elements from Tail to Head."""
        elements = []
        temp = self.head
        
        if temp is None:
            print("Backward: None")
            return
            
        # Go to the last node
        while temp.next:
            temp = temp.next
            
        # Traverse backwards
        while temp:
            elements.append(str(temp.data))
            temp = temp.prev
        print("Backward: " + " <-> ".join(elements) + " -> None")


if __name__ == "__main__":
    print("Testing Doubly Linked List:")
    dll = DoublyLinkedList()
    
    dll.insertAtEnd(100)
    dll.insertAtEnd(200)
    dll.insertAtBeginning(50)
    dll.insertAtEnd(300)
    
    print("\nList after insertions:")
    dll.displayForward()   # Expected: 50 <-> 100 <-> 200 <-> 300 -> None
    dll.displayBackward()  # Expected: 300 <-> 200 <-> 100 <-> 50 -> None
    
    dll.deleteNode(200)
    print("\nList after deleting 200:")
    dll.displayForward()   # Expected: 50 <-> 100 <-> 300 -> None
    
    dll.deleteNode(50)
    print("\nList after deleting head (50):")
    dll.displayForward()   # Expected: 100 <-> 300 -> None
    dll.displayBackward()  # Expected: 300 <-> 100 -> None
