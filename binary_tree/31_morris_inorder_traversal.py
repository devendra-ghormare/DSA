class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorderTraversal(root):
    inorder = []
    curr = root
    while curr:
        if curr.left is None:
            inorder.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
            
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                inorder.append(curr.val)
                curr = curr.right
    
    return inorder

# Time = O(n)
# Space = O(1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)

print(inorderTraversal(root))

