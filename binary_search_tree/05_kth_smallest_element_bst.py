class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def kthSmallest(root, k):

    def inorder(node, value):
        if node:
            inorder(node.left, value)
            value.append(node.val)
            inorder(node.right, value)

    value = []
    inorder(root, value)
    return value[k-1]

root = Node(3)
root.left = Node(1)
root.left.right = Node(2)
root.right = Node(4)


print(kthSmallest(root, 3))