class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxDepth(root):
    if not root:
        return 0
    
    lh = maxDepth(root.left)
    rh = maxDepth(root.right)
    return 1 + max(lh, rh)

# Time = O(n)
# Space = O(n)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

print(maxDepth(root))