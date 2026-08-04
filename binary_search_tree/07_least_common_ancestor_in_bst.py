class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    if not root:
        return None

    curr = root.val

    if curr < p.val and curr < q.val:
        return lowestCommonAncestor(root.right, p, q)
    if curr > p.val and curr > q.val:
        return lowestCommonAncestor(root.left, p, q)

    return root


root = Node(3)
root.left = Node(1)
root.left.right = Node(2)
root.right = Node(4)


p = root.left.right  
q = root.right       

lca_node = lowestCommonAncestor(root, p, q)
print(lca_node.val if lca_node else "No LCA found")