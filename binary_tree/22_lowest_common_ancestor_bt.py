class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if not left:
        return right
    elif not right:
        return left
    else:
        return root

# Time = O(n)
# Space = O(H) where H is height of tree

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right.right = Node(10)
root.right.left = Node(9)

p = root.left  
q = root.right

lca = lowestCommonAncestor(root, p, q)
print(lca.val)


