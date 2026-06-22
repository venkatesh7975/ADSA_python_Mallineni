class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Delete from beginning
    def delete_start(self):
        if self.head is None:
            print("List is empty")
            return

        print(f"Deleted: {self.head.data}")
        self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            print(f"Deleted: {self.head.data}")
            self.head = None
            return

        prev = None
        temp = self.head

        while temp.next:
            prev = temp
            temp = temp.next

        print(f"Deleted: {temp.data}")
        prev.next = None

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")

            temp = temp.next

        print("None")


# Driver Code
ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.insert_start(5)

print("Linked List:")
ll.display()

ll.delete_start()
ll.display()

ll.delete_end()
ll.display()