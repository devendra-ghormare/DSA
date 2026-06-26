class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def arrayToLL(arr):
    n = len(arr)
    head = Node(arr[0])
    temp = head

    for i in range(1, n):
        curr = Node(arr[i])
        temp.next = curr
        temp = temp.next 
    
    return head

def printLL(head):
    temp = head

    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next 
    print("None")

def mergeTwoSortedLL(list1, list2):
    dummy = Node(-1)
    temp = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next

        temp = temp.next
    
    if list1:
        temp.next = list1
    
    if list2:
        temp.next = list2
    
    return dummy.next

l1 = arrayToLL([1,2,3])
l2 = arrayToLL([2,4,5])

printLL(mergeTwoSortedLL(l1, l2))