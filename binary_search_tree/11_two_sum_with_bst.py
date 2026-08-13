class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BSTIterator:
    def __init__(self, root, isReverse):
        self.stack = []
        self.reverse = isReverse
        self.pushAll(root)

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()

        if not self.reverse:
            self.pushAll(node.right)
        else:
            self.pushAll(node.left)

        return node.val
    
    def pushAll(self, node):
        while node:
            self.stack.append(node)

            if self.reverse:
                node = node.right
            else:
                node = node.left

def findTarget(root, k):
    if not root:
        return False

    l = BSTIterator(root, False)
    r = BSTIterator(root, True)

    i = l.next()
    j = r.next()

    while i < j:
        if i + j == k:
            return True
        elif i + j < k:
            i = l.next()
        else:
            j = r.next()

    return False

# Time = O(n)
# Space = O(h)

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(7)

k = 9

result = findTarget(root, k)

print(result)

        