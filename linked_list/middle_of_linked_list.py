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

def middleOfLL(head):

############ Brute Force #############
    # if not head:
    #     return None
    
    # temp = head
    # count = 0

    # while temp:
    #     count += 1
    #     temp = temp.next 
    
    # middleNode = (count // 2) + 1
    # temp = head

    # while temp:
    #     middleNode -= 1

    #     if middleNode == 0:
    #         break

    #     temp = temp.next 
    
    # return temp

################# Optimal Approach ###############

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    
    return slow

head = arrayToLL([1,2,3,4,5,6])
printLL(middleOfLL(head))
    