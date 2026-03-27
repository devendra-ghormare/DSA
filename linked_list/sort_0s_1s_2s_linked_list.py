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



def sortList(head):
    if not head or not head.next:
        return head

########## Brute Force ###############

    # temp = head
    # cnt1 = cnt2 = cnt3 = 0

    # while temp:
    #     if temp.data == 0:
    #         cnt1 += 1
    #     elif temp.data == 1:
    #         cnt2 += 1
    #     else:
    #         cnt3 += 1
        
    #     temp = temp.next
    
    # temp = head
    # while temp:
    #     if cnt1:
    #         temp.data = 0
    #         cnt1 -= 1
    #     elif cnt2:
    #         temp.data = 1
    #         cnt2 -= 1
    #     else:
    #         temp.data = 2
    #         cnt3 -= 1

    #     temp = temp.next
    
    # return head

###################### Optimal approach ####################

    zeroHead = Node(-1)
    oneHead = Node(-1)
    twoHead = Node(-1)

    zero = zeroHead
    one = oneHead
    two = twoHead
    temp = head

    while temp:
        if temp.data == 0:
            zero.next = temp
            zero = zero.next
        elif temp.data == 1:
            one.next = temp
            one = one.next
        else:
            two.next = temp
            two = two.next
        
        temp = temp.next 
    
    zero.next = oneHead.next if oneHead.next else twoHead.next
    one.next = twoHead.next
    two.next = None

    return zeroHead.next


ll =  [1, 0, 2, 0 , 1]
head = arrayToLL(ll)
printLL(sortList(head))