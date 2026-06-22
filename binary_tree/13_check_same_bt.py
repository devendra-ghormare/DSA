class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isSameTree(p, q):
    if not p or not q:
        return p==q
    
    return (p.val==q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Time = O(n)
# Space = O(n)

p = Node(1)
p.left = Node(2)
p.right = Node(3)
p.right.left = Node(4)
p.right.right = Node(5)


q = Node(1)
q.left = Node(2)
q.right = Node(3)
q.right.left = Node(4)
q.right.right = Node(5)


print(isSameTree(p, q))