from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildParentMap(root, target):
    parent = {}
    q = deque([root])
    targetNode = None

    while q:
        node = q.popleft()

        if node.val == target:
            targetNode = node
        
        if node.left:
            parent[node.left] = node
            q.append(node.left)
        
        if node.right:
            parent[node.right] = node
            q.append(node.right)
        
    return parent, targetNode

def burnTree(targetNode, parent):
    visited = set()
    q = deque([targetNode])
    visited.add(targetNode)

    time = 0

    while q:
        size = len(q)
        burned = False

        for _ in range(size):
            node = q.popleft()

            if node.left and node.left not in visited:
                visited.add(node.left)
                q.append(node.left)
                burned = True
            
            if node.right and node.right not in visited:
                visited.add(node.right)
                q.append(node.right)
                burned = True
            
            if node in parent and parent[node] not in visited:
                visited.add(parent[node])
                q.append(parent[node])
                burned = True
        
        if burned:
            time += 1
    
    return time


def minTimeToBurn(root, target):
    parent, targetNode = buildParentMap(root, target)

    return burnTree(targetNode, parent)

# Time = O(n)
# Space = O(n)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.left.left.right = Node(7)

print(minTimeToBurn(root, 1))

