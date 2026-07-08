class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def childrenSumProperty(root):
    if not root:
        return 0
    
    child = 0

    if root.left:
        child += root.left.val
    
    if root.right:
        child += root.right.val
    
    if child >= root.val:
        root.val = child
    else:
        if root.left:
            root.left.val = root.val
        
        if root.right:
            root.right.val = root.val
    
    childrenSumProperty(root.left)
    childrenSumProperty(root.right)

    total = 0
    if root.left:
        total += root.left.val
    if root.right:
        total += root.right.val
    
    if root.left or root.right:
        root.val = total



def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.val, end=" ")
    inorderTraversal(root.right)

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)


print("Binary Tree before modification:", end=" ")
inorderTraversal(root)
print()


childrenSumProperty(root)

print("Binary Tree after Children Sum Property:", end=" ")
inorderTraversal(root)
print()
     