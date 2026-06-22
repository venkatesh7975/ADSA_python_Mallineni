# Binary Search Tree Implementation
# Operations: Creation, Insertion, Search, Deletion, Inorder Traversal

# Define Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a node into BST
def insert(node, value):

    if node is None:
        return Node(value)

    if value < node.data:
        node.left = insert(node.left, value)

    elif value > node.data:
        node.right = insert(node.right, value)

    return node


# Search a value in BST
def search(node, value):

    if node is None:
        return False

    if node.data == value:
        return True

    if value < node.data:
        return search(node.left, value)

    return search(node.right, value)


# Find minimum value node
def find_min(node):

    while node.left is not None:
        node = node.left

    return node


# Delete a node from BST
def delete_node(node, value):

    if node is None:
        return node

    if value < node.data:
        node.left = delete_node(node.left, value)

    elif value > node.data:
        node.right = delete_node(node.right, value)

    else:

        # Case 1 & 2: No child or One child
        if node.left is None:
            return node.right

        elif node.right is None:
            return node.left

        # Case 3: Two children
        temp = find_min(node.right)

        node.data = temp.data

        node.right = delete_node(node.right, temp.data)

    return node


# Inorder Traversal
def inorder(node):

    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# ---------------- Main Program ----------------

root = None

values = [50, 30, 70, 20, 40, 60, 80]

# Creation / Insertion
for value in values:
    root = insert(root, value)

print("Inorder Traversal after insertion:")
inorder(root)

print("\n")

# Search Operation
key = 60

if search(root, key):
    print(f"{key} Found")
else:
    print(f"{key} Not Found")

key = 90

if search(root, key):
    print(f"{key} Found")
else:
    print(f"{key} Not Found")

print()

# Deletion Operations
root = delete_node(root, 20)  # Leaf Node
root = delete_node(root, 30)  # Node with One Child
root = delete_node(root, 50)  # Node with Two Children

print("\nInorder Traversal after deletion:")
inorder(root)