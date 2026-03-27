class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

def arrayToDLL(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        prev.next = temp
        temp.back = prev
        prev = temp
    
    return head

def printDLL(head):
    if not head:
        return None
    
    temp = head
    while(temp):
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

def deleteHead(head):
    if head is None or head.next is None:
        return None
    
    prev = head
    head = head.next 
    head.back = None
    prev.next = None

    return head

def deleteTail(head):
    if head is None or head.next is None:
        return None
    
    tail = head

    while tail.next != None:
        tail = tail.next 
    
    prev = tail.back
    prev.next = None
    tail.back = None

    return head

def deletePosition(head, k):
    if not head:
        return None
    
    temp = head
    count = 0

    while temp:
        count += 1
        if count == k:
            break
        temp = temp.next 
    
    prev = temp.back
    front = temp.next 

    if prev is None and front is None:
        return None
    elif prev is None:
        return deleteHead(head)
    elif front is None:
        return deleteTail(head)
    else:
        prev.next = front
        front.back = prev
        temp.next = None
        temp.back = None
    
    return head

def deleteNode(head, node):
    if head is None:
        return None
    
    prev = node.back
    front = node.next 

    if front is None:
        prev.next = None
        node.back = None
        return head
    
    prev.next = front
    front.back = prev
    node.back = None
    node.next = None

    return head

def insertBeforeHead(head, val):
    newHead = Node(val)

    if head is None:
        return newHead
    
    head.back = newHead
    newHead.next = head

    return newHead

def insertBeforeTail(head, val):
    if head in None:
        return Node(val)
    
    if head.next is None:
        return insertBeforeHead(head, val)

    tail = head
    while tail.next:
        tail = tail.next 

    prev = tail.back
    newNode = Node(val)
    newNode.next = tail
    newNode.back = prev
    prev.next = newNode
    tail.back = newNode

    return head
 
def insertBeforeKthNode(head, k, val):
    if head is None:
        return Node(val)
    
    if k == 1:
        return insertBeforeHead(head, val)
    
    temp = head
    count = 0

    while temp:
        count += 1

        if count == k:
            break
        temp = temp.next 
    
    prev = temp.back
    newNode = Node(val)
    newNode.next = temp
    newNode.back = prev
    prev.next = newNode
    temp.back = newNode

    return head

def insertBeforeNode(head, node, val):
    prev = node.back
    newNode = Node(val)
    newNode.next = node
    newNode.back = prev
    prev.next = newNode
    node.back = newNode

    return head


arr = [2,4,6,8,10,12,14,16,18,20]
head = arrayToDLL(arr)
printDLL(head)
# head_del = deleteHead(head)
# printDLL(head_del)
# tail_del = deleteTail(head)
# printDLL(tail_del)
# position_del = deletePosition(head, 4)
# printDLL(position_del)
# node_del = deleteNode(head, head.next.next)
# printDLL(node_del)
# ibh = insertBeforeHead(head,0)
# printDLL(ibh)
# ibt = insertBeforeTail(head, 19)
# printDLL(ibt)
# ibkn = insertBeforeKthNode(head, 10, 9)
# printDLL(ibkn)
ibn = insertBeforeNode(head, head.next, 3)
printDLL(ibn)