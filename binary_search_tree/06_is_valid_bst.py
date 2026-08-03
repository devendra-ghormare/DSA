class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isValidBST(root):
    def isBST(root, minVal, maxVal):
        if not root:
            return True

        if root.val >= maxVal or root.val <= minVal:
            return False

        return (isBST(root.left, minVal, root.val) and isBST(root.right, root.val, maxVal))

    return isBST(root, float('-inf'), float('inf'))

# Time = O(n)
# Space = O(h)

root = Node(3)
root.left = Node(1)
root.left.right = Node(2)
root.right = Node(4)

print(isValidBST(root))