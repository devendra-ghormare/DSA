class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def arrayToDLL(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        prev.next = temp
        temp.prev = prev
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

def deleteAllOccurance(head, val):
    temp = head

    while temp:
        if temp.data == val:
            if temp == head:
                head = temp.next 
            
            nextNode = temp.next 
            prevNode = temp.prev

            if nextNode:
                nextNode.prev = prevNode
            
            if prevNode:
                prevNode.next = nextNode
            
            temp = nextNode
        else:
            temp = temp.next 
    
    return head

head = arrayToDLL([1,2,3,3,4,5,6,3,7,8])
printDLL(deleteAllOccurance(head, 3))