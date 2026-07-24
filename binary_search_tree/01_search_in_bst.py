class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def searchBST(root, target):

    while root and root.val != target:
        if target > root.val:
            root = root.right
        else:
            root = root.left

    return root

# Time = O(h)
# Space = O(1)

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)


print(searchBST(root, 8))
print(searchBST(root, 1))