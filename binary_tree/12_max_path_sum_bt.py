class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxPathDown(root, maxi):
    if not root:
        return 0
    
    leftSum = max(0, maxPathDown(root.left, maxi))
    rightSum = max(0, maxPathDown(root.right, maxi))
    maxi[0] = max(maxi[0], leftSum + rightSum + root.val)

    return root.val + max(leftSum, rightSum)


def maxPathSum(root):
    maxi = [float('-inf')]
    maxPathDown(root, maxi)
    return maxi[0]

# Time = O(n)
# Space = O(h)

root = Node(-10)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(maxPathSum(root))

