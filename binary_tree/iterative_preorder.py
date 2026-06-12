class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def iterativePreorder(root):
    preoder = []
    if not root:
        return preoder

    stack = [root]

    while stack:
        node = stack.pop()
        preoder.append(node.val)

        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)
    
    return preoder

    # Time = O(n)
    # Space = O(H) where H is the height of the binary tree. The space is used by the stack to store nodes during traversal. 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(iterativePreorder(root))
    

