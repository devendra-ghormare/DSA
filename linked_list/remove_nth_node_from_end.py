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

def removeNthFromEnd(head, n):
    
############# Brute Force ##############
    # if not head:
    #         return None

    # count = 0
    # temp = head

    # while temp:
    #     count += 1
    #     temp = temp.next 
    
    # if count == n:
    #     return head.next 

    # result = count - n 
    # temp = head

    # while temp:
    #     result -= 1

    #     if result == 0:
    #         break

    #     temp = temp.next 
    
    # delNode = temp.next 
    # temp.next = temp.next.next 

    # return head

#################### Optimal approach ############

    fast = head

    for i in range(n):
        fast = fast.next 
    
    if fast is None:
        return head.next 
    
    slow = head 

    while fast.next:
        slow = slow.next
        fast = fast.next 
    
    delNode = slow.next 
    slow.next = slow.next.next 

    return head 


head = arrayToLL([1,2,3,4,5])
# head = arrayToLL([1])
res = removeNthFromEnd(head, n=2)
printLL(res)