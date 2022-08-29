
class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        if not self.root:
            self.root = Node(val)
        else:
            p = self.root
            pre = p
            while p:
                pre = p
                if val < p.info:
                    p = p.left
                elif val >= p.info:
                    p = p.right
            if val < pre.info:
                pre.left = Node(val)
            else:
                pre.right = Node(val)
        
            
            

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
