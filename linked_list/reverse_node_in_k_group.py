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
def reverseLL(head):
    temp = head
    prev = None

    while temp:
        curr = temp.next 
        temp.next = prev
        prev = temp
        temp = curr
    
    return prev

def getKthNode(head, k):
    k -= 1
    temp = head 
    while temp and k > 0:
        k -= 1
        temp = temp.next

    return temp
 
def reverseKGroup(head, k):
    temp = head
    prevNode = None

    while temp:
        kThNode = getKthNode(temp, k)

        if kThNode is None:
            if prevNode:
                prevNode.next = temp

            break

        nextNode = kThNode.next 
        kThNode.next = None
        newHead = reverseLL(temp)

        if temp == head:
            head = newHead
        else:
            prevNode.next = newHead
        
        prevNode = temp
        temp = nextNode
    
    return head

    # Time - O(n) + O(n) = O(n)
    # Space - O(1)


head = arrayToLL([1,2,3,4,5])
printLL(reverseKGroup(head, 2))