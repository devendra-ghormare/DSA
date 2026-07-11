class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def leftHeight(node):
    height = 0

    while node:
        height += 1
        node = node.left

    return height

def rightHeight(node):
    height = 0
    while node:
        height += 1
        node = node.right

    return height


def countNode(root):
    if not root:
        return 0
    
    lh = leftHeight(root)
    rh = rightHeight(root)

    if lh == rh:
        return (2 ** lh) - 1
    
    return 1 + countNode(root.left) + countNode(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print(countNode(root))