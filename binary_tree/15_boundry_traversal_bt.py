class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isLeaf(root):
    return not root.left and not root.right

def addLeftBoundry(root, res):
    curr = root.left

    while curr:
        if not isLeaf(curr):
            res.append(curr.val)
        
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

def addRightBoundry(root, res):
    curr = root.right
    temp = []

    while curr:
        if not isLeaf(curr):
            temp.append(curr.val)
        
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    
    for i in range(len(temp) - 1, -1, -1):
        res.append(temp[i])

def addLeaves(root, res):
    if isLeaf(root):
        res.append(root.val)
        return

    if root.left:
        addLeaves(root.left, res)
    
    if root.right:
        addLeaves(root.right, res)

def boundaryTraversal(root): 
    res = []
    if not root:
        return res
    
    if not isLeaf(root):
        res.append(root.val)
    
    addLeftBoundry(root, res)
    addLeaves(root, res)
    addRightBoundry(root, res)

    return res

# Time = O(n)
# Space = O(n)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(boundaryTraversal(root))