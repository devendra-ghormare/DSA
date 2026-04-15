class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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


def printLL(head):
    if not head:
        return None
    
    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next 
    
    print("None")

def findNthNode(head, k):
    count = 1
    temp = head

    while temp:
        if count == k:
            return temp
        count += 1
        temp = temp.next 
    
    return temp

def rotateLL(head, k):
    if not head or k==0:
        return head
    
    length = 1
    tail = head

    while tail.next:
        tail = tail.next 
        length += 1
    
    k = k % length
    if k == 0:
        return head
    
    tail.next = head

    steps = length - k 
    temp = head

    for _ in range(steps - 1):
        temp = temp.next 
    
    new_head = temp.next 
    temp.next = None 

    return new_head

#################### OR ##################
    # tail.next = head
    # newNode = findNthNode(head, length-k)
    # head = newNode.next 
    # newNode.next = None

    # return head

    # Time = O(n) + O(n) = O(n)
    # Space = O(1)



head = arrayToLL([1,2,3,4,5])
printLL(rotateLL(head, 4))