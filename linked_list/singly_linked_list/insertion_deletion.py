class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def convertArr2LL(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    
    return head

def printLL(head):
    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    
    print("None")

def deleteHead(head):
    if head is None:
        return None
    
    head = head.next

    return head

def deleteTail(head):
    if head is None or head.next is None:
        return None

    temp = head
    
    while(temp.next.next != None):
        temp = temp.next 
    
    temp.next = None

    return head

def deletePosition(head, k):
    if not head:
        return head
    
    if k==1:
        return head.next
    
    temp = head
    prev = None
    count = 0
    
    while temp:
        count += 1

        if count == k:
            prev.next = prev.next.next
            break
        
        prev = temp
        temp = temp.next 

    return head

def deleteValue(head, val):
    if not head:
        return head

    if head.data == val:
        return head.next

    temp = head
    prev = None

    while temp:
        if temp.data == val:
            prev.next = prev.next.next
            break
        prev = temp
        temp = temp.next 
    
    return head

def insertHead(head, val):
    newhead =  Node(val)
    newhead.next = head
    return newhead

def insertTail(head, val):
    if not head:
        return Node(val)
    
    temp = head
    while temp.next != None:
        temp = temp.next
    newhead = Node(val)
    temp.next = newhead
    return head

def insertPosition(head, el, k):
    if not head:
        if k == 1:
            return Node(el)
        else:
            return None
    
    if k==1:
        newhead = Node(el)
        newhead.next = head
        return newhead
    
    temp = head
    count = 0

    while temp:
        count += 1
        if count == k-1:
            newNode = Node(el)
            newNode.next = temp.next
            temp.next = newNode
            break

        temp = temp.next 
    
    return head

def insertBeforeValue(head, el, val):
    if not head:
        return None
    
    if head.data == val:
        newhead = Node(el)
        newhead.next = head

        return newhead
    
    temp = head
    found = False
    while temp.next:
        if temp.next.data == val:
            newNode = Node(el)
            newNode.next = temp.next
            temp.next = newNode
            found = True
            break

        temp = temp.next 
    
    if found == False:
        raise ValueError(f"{val} not found")

    return head

arr = [5,10,15,20]
head = convertArr2LL(arr)
printLL(head)   
# newhead = deleteHead(head)
# printLL(newhead)
# taildel = deleteTail(head)
# printLL(taildel)
# positiondel = deletePosition(head, 2)
# printLL(positiondel)
# value_del = deleteValue(head, 10)
# printLL(value_del)
# newhead = insertHead(head, 1)
# printLL(newhead)
# tail = insertTail(head, 25)
# printLL(head)
# inserPo = insertPosition(head, 18, 4)
# printLL(head)
isertVal = insertBeforeValue(head, 12, 15)
printLL(head)