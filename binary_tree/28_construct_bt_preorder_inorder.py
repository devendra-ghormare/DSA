class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
    if preStart > preEnd or inStart > inEnd:
        return None
    
    root = Node(preorder[preStart])

    inRoot = inMap[root.val]
    numLeft = inRoot - inStart

    root.left = buildTree(preorder, preStart + 1, preStart + numLeft, inorder, inStart, inRoot - 1, inMap)
    root.right = buildTree(preorder, preStart + numLeft + 1, preEnd, inorder, inRoot+ 1, inEnd, inMap)

    return root


def contructTree(preorder, inorder):
    inMap = {}

    for i in range(len(inorder)):
        inMap[inorder[i]] = i

    root = buildTree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inMap)

    return root

# Time = O(n)
# Space = O(n)

def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)

inorder = [9, 3, 15, 20, 7]
preorder = [3, 9, 20, 15, 7]

root = contructTree(preorder, inorder)
printInorder(root)