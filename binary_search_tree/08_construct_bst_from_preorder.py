class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bstFromPreorder(preorder):
    def build(arr, i, bound):
        if i[0] == len(arr) or arr[i[0]] > bound:
            return None
        
        root = Node(arr[i[0]])
        i[0] += 1

        root.left = build(arr, i, root.val)
        root.right = build(arr, i, bound)
        return root
    
    i = [0]
    return build(preorder, i, float('inf'))

# Time = O(n)
# Space = O(n)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Driver code
preorder = [8, 5, 1, 7, 10, 12]

root = bstFromPreorder(preorder)

print("Inorder Traversal:")
inorder(root)