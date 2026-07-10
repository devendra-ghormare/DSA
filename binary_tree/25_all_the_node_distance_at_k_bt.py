from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildParentMap(root, parent):
    q = deque([root])

    while q:
        node = q.popleft()

        if node.left:
            parent[node.left] = node
            q.append(node.left)
        
        if node.right:
            parent[node.right] = node
            q.append(node.right)

def bfs(target, parent_map, k):
    q = deque([target])
    visited = set([target])
    level = 0

    while q:
        if level == k:
            break

        size = len(q)

        for _ in range(size):
            node = q.popleft()

            if node.left and node.left not in visited:
                visited.add(node.left)
                q.append(node.left)
            
            if node.right and node.right not in visited:
                visited.add(node.right)
                q.append(node.right)
            
            if node in parent_map and parent_map[node] not in visited:
                visited.add(parent_map[node])
                q.append(parent_map[node])

        level += 1
    
    return [node.val for node in q]


def distance(root, target, k):
    if not root:
        return []
    
    parent_map = {}

    buildParentMap(root, parent_map)

    return bfs(target, parent_map, k)

# Time = O(n)
# Space = O(n)

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)

target = root.left      
k = 2

print(distance(root, target, k))