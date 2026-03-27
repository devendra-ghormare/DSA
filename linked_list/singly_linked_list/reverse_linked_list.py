class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def arrToLL(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    move = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        move.next = temp
        move = temp
    
    return head

def printLL(head):
    if not head:
        return None
    
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    
    print("None")

#################### Brute Force ######################
def reverseLL(head):
    if not head:
        return head
    
    stack = []

    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next 
    
    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next
    
    return head

#################### Optimal #######################
def reverseOpLL(head):
    if not head or not head.next:
        return head
    
    temp = head
    prev = None

    while temp:
        curr = temp.next 
        temp.next = prev
        prev = temp
        temp = curr
    
    return prev

arr=[5,14,25,36,47,58]
head = arrToLL(arr)
printLL(head)
# revHead = reverseLL(head)
# printLL(revHead)
opRev = reverseOpLL(head)
printLL(opRev)