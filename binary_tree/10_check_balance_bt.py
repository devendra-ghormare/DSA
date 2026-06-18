
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
def isBalanced( root) -> bool:
    def height(root):
        if not root:
            return 1
    
        lh = height(root.left)
        if lh == -1:
            return -1
        
        rh = height(root.right)
        if rh == -1:
            return -1
        
        if abs(lh-rh) > 1:
            return -1 
        
        return max(lh, rh) + 1

    return height(root) != -1

# Time = O(n)
# Space = O(n)
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.left.right.left = Node(6)
# root.left.right.right = Node(7)

print(isBalanced(root))