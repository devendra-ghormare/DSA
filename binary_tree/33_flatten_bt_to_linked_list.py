class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def flatten(root):

######################## Recursice way #############33
    prev = None

    def dfs(node):
        nonlocal prev

        if not node:
            return 
        
        dfs(node.right)
        dfs(node.left)

        node.right = prev
        node.left = None
        prev = node
    
    dfs(root)

# Time = O(n) 
# Space = O(h)

################## Stack way ##################
    if not root:
        return
    
    stack = [root]

    while stack:
        curr = stack.pop()

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
        
        if stack:
            curr.right = stack[-1]

        curr.left = None
    
    # Time = O(n)
    # Space = O(h)


root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.right = Node(6)

flatten(root)

curr = root
while curr:
    print(curr.val, end=" -> ")
    curr = curr.right

print("None")