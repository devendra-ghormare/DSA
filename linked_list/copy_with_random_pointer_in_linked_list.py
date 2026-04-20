class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

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


def printLLWithRandom(head):
    temp = head
    while temp:
        rand = temp.random.data if temp.random else None
        print(f"Data: {temp.data}, Random: {rand}")
        temp = temp.next
    print()

def insertCopyInBetween(head):
    temp = head

    while temp:
        nextNode = temp.next
        copyNode = Node(temp.data)
        copyNode.next = temp.next 
        temp.next = copyNode

        temp = nextNode

def connectRandomPointer(head):
    temp = head

    while temp:
        copyNode = temp.next 

        if temp.random:
            copyNode.random = temp.random.next 
        else:
            copyNode.random = None
        
        temp = temp.next.next 

def getDeepCopyList(head):
    temp = head
    dummyNode = Node(-1)
    res = dummyNode

    while temp:
        res.next = temp.next
        res = res.next 

        temp.next = temp.next.next 
        temp = temp.next 

    return dummyNode.next 

def copyRandomList(head):
    # temp = head
    # mpp = {}

    # while temp:
    #     newNode = Node(temp.data)
    #     mpp[temp] = newNode
    #     temp = temp.next 
    
    # temp = head
    # while temp:
    #     copyNode = mpp[temp]
    #     copyNode.next = mpp.get(temp.next)
    #     copyNode.random = mpp.get(temp.random)
    #     temp = temp.next 
    
    # return mpp[head]

######################### Optimal solution ###################
    
    insertCopyInBetween(head)
    connectRandomPointer(head)
    return getDeepCopyList(head)

arr = [1, 2, 3, 4]
head = arrayToLL(arr)

head.random = head.next.next        # 1 -> 3
head.next.random = head             # 2 -> 1
head.next.next.random = head.next.next.next  # 3 -> 4
head.next.next.next.random = head.next       # 4 -> 2

print("Original List:")
printLLWithRandom(head)

copied_head = copyRandomList(head)

print("Copied List:")
printLLWithRandom(copied_head)