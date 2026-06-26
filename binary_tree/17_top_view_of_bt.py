from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def topView(root):
    ans = []
    if not root:
        return ans
    
    q = deque()
    mpp = {}

    q.append((root, 0))

    while q:
        node, line = q.popleft()

        if line not in mpp:
            mpp[line] = node.val
        
        if node.left:
            q.append((node.left, line - 1))
        
        if node.right:
            q.append((node.right, line + 1))
    
    for key in sorted(mpp.keys()):
        ans.append(mpp[key])

    return ans

# Time = O(n)
# Space = O(n)

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)

print(topView(root))