class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

def interativePostorder(root):
    postorder = []
    if not root:
        return postorder
    
    stack = []
    
    curr = root

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[-1].right
            if not temp:
                temp = stack.pop()
                postorder.append(temp.val)

                while len(stack) > 0 and temp == stack[-1].right:
                    temp = stack.pop()
                    postorder.append(temp.val)
            else:
                curr = temp
    return postorder

# Time = O(n)
# Space = O(2n) = O(n)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(interativePostorder(root))
