class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findCeil(root, key):
    ceil = -1

    while root:
        if key == root.val:
            ceil = root.val
            return ceil
        
        if key > root.val:
            root = root.right
        else:
            ceil = root.val
            root = root.left

    return ceil

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
print(findCeil(root, 6))