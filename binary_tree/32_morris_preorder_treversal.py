class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorderTraversal(root):
    preorder = []
    curr = root
    while curr:
        if curr.left is None:
            preorder.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
            
            if prev.right is None:
                prev.right = curr
                preorder.append(curr.val)
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
    
    return preorder

# Time = O(n)
# Space = O(1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)

print(preorderTraversal(root))

