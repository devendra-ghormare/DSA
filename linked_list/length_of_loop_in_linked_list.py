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

def findLength(slow, fast):
    count = 1
    fast = fast.next
    while slow != fast:
        count += 1
        fast = fast.next 
    
    return count

def lenOfLoopInLL(head):

############## Brute Force ##############
    # mpp = {}
    # count = 1
    # temp = head

    # while temp:

    #     if temp in mpp:
    #         value = mpp[temp]
    #         return count - value
        
    #     mpp[temp] = count
    #     count += 1
    #     temp = temp.next 
    
    # return 0

    # Time = O(n)
    # Space = O(n)
################ Optimal Approach #############
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 

        if slow == fast:
            return findLength(slow, fast)
    
    return 0

# Time = O(n)
# Space = O(1)

head = arrayToLL([1,2,3,4,5])

temp = head 
second = head.next 

while temp.next:
    temp = temp.next

temp.next = second

print(lenOfLoopInLL(head))

        
