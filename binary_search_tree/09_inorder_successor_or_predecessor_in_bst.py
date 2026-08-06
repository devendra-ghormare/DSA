class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorderSuccessor(root, p):
    successor = None

    while root:
        if p.val >= root.val:
            root = root.right
        else:
            successor = root.val
            root = root.left 
    
    return successor

def inorderPredecessor(root, p):
    predecessor = None

    while root:
        if p.val <= root.val:
            root = root.left
        else:
            predecessor = root.val
            root = root.right

    return predecessor

# Time = O(h)
# Space = (1)

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(7)

p = root.left.right

print(inorderSuccessor(root, p))
print(inorderPredecessor(root, p))