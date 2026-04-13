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

def findTail(head):
    tail = head

    while tail.next:
        tail = tail.next 
    
    return tail

def pairOfGivenSum(head, val):
    pairs = []

    if not head:
        return pairs

    left = head
    right = findTail(head)

    while left.data < right.data:
        if left.data + right.data == val:
            pairs.append((left.data, right.data))
            left = left.next
            right = right.back 
        elif left.data + right.data > val:
            right = right.back
        else:
            left = left.next 
        
    return pairs

    # Time = O(n)
    # Space = O(n)


head = arrayToDLL([1,2,3,4,5,6])
print(pairOfGivenSum(head, 5))