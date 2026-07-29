class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertNode(root, val):
    if not root:
        return Node(val)

    temp = root

    while True:
        if temp.val <= val:
            if temp.right:
                temp = temp.right
            else:
                temp.right = Node(val)
                break
        else:
            if temp.left:
                temp = temp.left
            else:
                temp.left = Node(val)
                break

    return root

# Time = O(log n)
# Space = O(1)

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

root = insertNode(root, 5)
inorder(root)
