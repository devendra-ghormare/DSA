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

def findMiddle(head):
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    return prev

def merge(list1, list2):
    dummyNode = Node(-1)

    temp = dummyNode

    while list1 and list2:
        if list1.data < list2.data:
            temp.next = list1 
            temp = list1
            list1 = list1.next 
        else:
            temp.next = list2
            temp = list2
            list2 = list2.next 
    
    if list1:
        temp.next = list1
    else:
        temp.next = list2
    
    return dummyNode.next 

def sortLL(head):
    if not head or not head.next:
        return head

################# Brute Force  #################### 
    # list1 = []
    # temp = head

    # while temp:
    #     list1.append(temp.data)
    #     temp = temp.next 
    
    # list1.sort()

    # temp = head
    # i = 0
    # while temp:
    #     temp.data = list1[i]
    #     i = i + 1
    #     temp = temp.next 
    
    # return head

################# Optimal solution #################### 
    middle = findMiddle(head)
    leftHead = head
    rightHead = middle.next 
    middle.next = None

    leftHead = sortLL(leftHead)
    rightHead = sortLL(rightHead)

    return merge(leftHead, rightHead)

head = arrayToLL([4,2,3,1,5])
printLL(sortLL(head))