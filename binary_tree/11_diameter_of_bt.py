
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height(root, maxi):
    if not root:
        return 0
    
    lh = height(root.left, maxi)
    rh = height(root.right, maxi)

    maxi[0] = max(maxi[0], rh+lh)

    return 1 + max(rh, lh)

def diameterOfBinaryTree(root):
    maxi = [0]

    height(root, maxi)

    return maxi[0]

# Time = O(n)
# Space = O(n)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(diameterOfBinaryTree(root))