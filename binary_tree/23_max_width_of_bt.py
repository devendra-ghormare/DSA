from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxWidth(root):
    if not root:
        return 0
    
    q = deque()
    ans = 0
    q.append((root, 0))

    while q:
        size = len(q)
        mini = q[0][1]
        first = 0
        last = 0
        for i in range(size):
            node, id = q.popleft()
            curr_id = id - mini

            if i == 0:
                first = curr_id
            
            if i == size - 1:
                last = curr_id
            
            if node.left:
                q.append((node.left, curr_id * 2+1))

            if node.right:
                q.append((node.right, curr_id * 2 + 2))
        
        ans = max(ans, last - first + 1)
    
    return ans 


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right.right = Node(10)
root.right.left = Node(9)


print(maxWidth(root))