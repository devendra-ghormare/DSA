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

################ Brute Force ################

    # if not head:
    #     return None
    
    # temp = head
    # stack = []

    # while temp:
    #     stack.append(temp.data)
    #     temp = temp.next 
    
    # temp = head
    # while temp:
    #     temp.data = stack.pop()
    #     temp = temp.next 
    
    # return head 

############### Optimal approach ##################
    # if not head or not head.next:
    #     return head
    
    # temp = head
    # prev = None

    # while temp:
    #     curr = temp.next 
    #     temp.next = prev
    #     prev = temp
    #     temp = curr

    # return prev

################ Recursive approach #################

    if not head or not head.next:
        return head 
    
    newHead = reverseLL(head.next)
    front = head.next 
    front.next = head
    head.next = None

    return newHead

head = arrayToLL([1,2,3,4,5])
printLL(reverseLL(head))