class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findFloor(root, key):
    floor = -1

    while root:
        if root.val == key:
            floor = root.val
            return floor

        if key > root.val:
            floor = root.val
            root = root.right
        else:
            root = root.left

    return floor

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)

print(findFloor(root, 6))
print(findFloor(root, 3))