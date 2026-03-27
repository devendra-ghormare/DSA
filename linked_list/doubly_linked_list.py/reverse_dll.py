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

##################### Brute Force #########################
def reverseDDL_stack(head):
    if not head:
        return None
    
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

#################### Optimal approach #####################
def reverseDLL(head):
    if not head or not head.next:
        return head
    
    newNode = None
    current = head

    while current:
        # swap next and back
        current.next, current.back = current.back, current.next
        
        newNode = current
        
        # move to next node (which is back after swap)
        current = current.back

    return newNode


arr = [10,20,30,40,50]
head = arrayToDLL(arr)
printDLL(head)
# reverse_stack = reverseDDL_stack(head)
# printDLL(reverse_stack)
reverse = reverseDLL(head)
printDLL(reverse)
