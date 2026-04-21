class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None

def arrayToLL(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    curr = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        curr.next = temp
        curr = curr.next

    return head

def printFlattened(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.child
    print("None")

def merge(list1, list2):
    dummyNode = Node(-1)
    res = dummyNode

    while list1 and list2:
        if list1.data < list2.data:
            res.child = list1
            res = list1
            list1 = list1.child
        else:
            res.child = list2
            res = list2
            list2 = list2.child
        
        res.next = None
    
    if list1:
        res.child = list1
    else:
        res.child = list2
    
    if dummyNode.child:
        dummyNode.child.next = None
    
    return dummyNode.child

def flatteningLinkedList(head):
    if not head or not head.next:
        return head
    
    head.next = flatteningLinkedList(head.next)
    head = merge(head, head.next)

    return head

    # Time = O(n*m)
    # Space = O(n) -- recursive stack space


if __name__ == "__main__":
    # Create main linked list: 5 -> 10 -> 19 -> 28
    head = Node(5)
    head.next = Node(10)
    head.next.next = Node(19)
    head.next.next.next = Node(28)

    # Attach child lists (sorted)

    # 5 -> 7 -> 8 -> 30
    head.child = Node(7)
    head.child.child = Node(8)
    head.child.child.child = Node(30)

    # 10 -> 20
    head.next.child = Node(20)

    # 19 -> 22 -> 50
    head.next.next.child = Node(22)
    head.next.next.child.child = Node(50)

    # 28 -> 35 -> 40 -> 45
    head.next.next.next.child = Node(35)
    head.next.next.next.child.child = Node(40)
    head.next.next.next.child.child.child = Node(45)

    flattened_head = flatteningLinkedList(head)

    print("Flattened list:")
    printFlattened(flattened_head)