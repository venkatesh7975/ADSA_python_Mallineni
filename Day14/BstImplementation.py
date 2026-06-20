class Node:
    def __init__(self,data):
        self.val=data 
        self.left=None 
        self.right=None 

class BST:
    def __init__(self):
        self.root=None 
    
    def insert(self,root,val):
        if root is None:
            return Node(val)
        if val<root.val:
            root.left=self.insert(root.left,val)
        elif val>root.val:
            root.right=self.insert(root.right,val)
        return root 
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
        
bst=BST()
root=None
for i in [50,30,40,20,70,60,80] :
    root=bst.insert(root,i) 

bst.inorder(root)