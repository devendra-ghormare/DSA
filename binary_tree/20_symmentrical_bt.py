class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isSymmetricHelp(left, right):
    if not left or not right:
        return left == right

    if left.val != right.val:
        return False
    
    return isSymmetricHelp(left.left, right.right) and isSymmetricHelp(left.right, right.left)

def isSymmetric(root):
    if not root:
        return False
    
    return isSymmetricHelp(root.left, root.right)

# Time = O(n)
# Space = O(h) where h is height of tree

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right.right = Node(10)
root.right.left = Node(9)

print(isSymmetric(root))