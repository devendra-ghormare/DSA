class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def iterativeInorder(root):
    inorder = []
    if not root:
        return inorder
    
    stack = []
    node = root
    while True:
        if node:
            stack.append(node)
            node = node.left
        else:
            if not stack:
                break
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
    
    return inorder

# Time = O(n)
# Space = O(h) where h is the height of the binary tree. This is the space required for the stack to store the nodes during traversal.

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

print(iterativeInorder(root))
