class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getPath(root, ans, x):
    if not root:
        return False
    
    ans.append(root.val)

    if root.val == x:
        return True
    
    if getPath(root.left, ans, x) or getPath(root.right, ans, x):
        return True
    
    ans.pop()
    return False


def rootNodePath(root, x):
    ans = []

    if not root:
        return ans
    
    getPath(root, ans, x) 
    return ans

# Time = O(n)
# Space = O(h) 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right.right = Node(10)
root.right.left = Node(9)

print(rootNodePath(root, 6))