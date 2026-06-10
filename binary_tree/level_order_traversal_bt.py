from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
    ans = []

    if not root:
        return ans 
    
    q = deque([root])

    while q:
        level = []

        for _ in range(len(q)):
            node = q.popleft()

            level.append(node.val)

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        
        ans.append(level)
    
    return ans

def printList(lst):
    for num in lst:
        print(num, end=' ')
    print()



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = levelOrder(root)

for level in result:
        printList(level)

# Time = O(n)
# Space = O(n)