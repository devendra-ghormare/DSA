class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def rightView(root):
    def recursion(node, level, ans):
        if not node:
            return 

        if level == len(ans):
            ans.append(node.val)

        recursion(node.right, level + 1, ans)
        recursion(node.left, level + 1, ans)
    
    ans = []
    recursion(root, 0, ans)

    return ans

# Time = O(n)
# Space = O(h) where h is the height of the tree

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)


print(rightView(root))