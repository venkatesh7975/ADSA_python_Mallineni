l1 = [4, 5, 3, 7, 6]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createList(l1):
    head = None
    temp = None

    for i in l1:
        newNode = Node(i)

        if head is None:
            head = newNode
            temp = head
        else:
            temp.next = newNode
            temp = newNode

    return head


def display(head):
    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


head = createList(l1)
display(head)