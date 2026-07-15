class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build(inorder, inStart, inEnd, postorder, posStart, posEnd, inMap):
    if inStart > inEnd or posStart > posEnd:
        return None
    
    root = Node(postorder[posEnd])
    inRoot = inMap[root.val]
    numLeft = inRoot - inStart

    root.left = build(inorder, inStart, inRoot - 1, postorder, posStart, posStart + numLeft - 1, inMap)
    root.right = build(inorder, inRoot + 1, inEnd, postorder, posStart + numLeft, posEnd - 1, inMap)

    return root

def contructTree(inorder, postorder):
    if len(inorder) != len(postorder):
        return None
    
    inMap = {}

    for i in range(len(inorder)):
        inMap[inorder[i]] = i 
    
    root = build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, inMap)

    return root

# Time = O(n)
# Space = O(n)
    
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)

inorder = [40, 20, 50, 10, 60, 30]
postorder = [40, 50, 20, 60, 30, 10]

root = contructTree(inorder, postorder)
printInorder(root)
    

