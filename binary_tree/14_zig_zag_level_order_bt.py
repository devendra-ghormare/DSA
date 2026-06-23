from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def zigZagLevelOrder(root):
    ans = []
    if not root:
        return ans
    
    q = deque([root])
    leftToRight = True

    while q:
        size = len(q)
        level = [0] * size

        for i in range(size):
            node = q.popleft()

            index = i if leftToRight else size - 1 -i

            level[index] = node.val
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        leftToRight = not leftToRight
        ans.append(level)

    return ans

# Time = O(n)
# Space = O(n)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(zigZagLevelOrder(root))