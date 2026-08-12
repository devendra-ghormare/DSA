class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.pushAll(root)

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()

        if node.right:
            self.pushAll(node.right)

        return node.val

    def hasNext(self):
        return len(self.stack) > 0

root = Node(7)
root.left = Node(3)
root.right = Node(15)
root.right.left = Node(9)
root.right.right = Node(20)

# Create iterator
iterator = BSTIterator(root)

# Iterate through BST
while iterator.hasNext():
    print(iterator.next())
    
