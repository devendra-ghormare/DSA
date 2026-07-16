from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def serialize(root):
    if not root:
        return ""
    
    result = ""
    q = deque([root])

    while q:
        node = q.popleft()

        if node is None:
            result += "#,"
        else:
            result += str(node.val) + ","
            q.append(node.left)
            q.append(node.right)

    return result

def deserialize(data):
    if not data:
        return None
    
    nodes = data.split(",")
    root = Node(int(nodes[0]))
    q = deque([root])
    i = 1

    while q and i < len(nodes) - 1:
        curr = q.popleft()

        if nodes[i] != "#":
            left = Node(int(nodes[i]))
            curr.left = left
            q.append(left)

        i += 1

        if nodes[i] != "#":
            right = Node(int(nodes[i]))
            curr.right = right
            q.append(right)
        
        i += 1

    return root

# Time = O(n)
# Space = O(n)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

s = serialize(root)
print(s)

new_root = deserialize(s)

print(serialize(new_root))