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
    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next 
    
    print("None")

def collisionPoint(t1, t2, d):

    while d:
        d -= 1
        t2 = t2.next 
    
    while t1 != t2:
        t1 = t1.next 
        t2 = t2.next 
    
    return t1

def getIntersectionNode(headA, headB):
############### Brute Force ###############

    # mpp = {}
    # temp = headA

    # while temp:
    #     mpp[temp] = 1
    #     temp = temp.next 
    
    # temp = headB
    # while temp:
    #     if temp in mpp:
    #         return temp

    #     temp = temp.next 

    # return None

    # Time = O(n + m)
    # Space = O(n)

################ Better solution #############
    # t1 = headA
    # n1 = 0
    # t2 = headB
    # n2 = 0

    # while t1:
    #     n1 += 1
    #     t1 = t1.next 
    
    # while t2:
    #     n2 += 1
    #     t2 = t2.next 
    
    # t1 = headA
    # t2 = headB

    # if n1 < n2:
    #     return collisionPoint(t1, t2, n2-n1)
    # else:
    #     return collisionPoint(t2, t1, n1-n2)

    # Time = O(n + m)
    # Space = O(1)
######################### Optimal Solution ##################
    t1 = headA
    t2 = headB

    while t1 != t2:
        t1 = t1.next if t1 else headB
        t2 = t2.next if t2 else headA

    return t1

    # Time = O(n + m)
    # Space = O(1)
# ---------------- DRIVER CODE ---------------- #

# Step 1: Create common part
common = arrayToLL([8, 10, 12])

# Step 2: Create List A
headA = arrayToLL([1, 2, 3])
temp = headA
while temp.next:
    temp = temp.next
temp.next = common   

# Step 3: Create List B
headB = arrayToLL([5, 6])
temp = headB
while temp.next:
    temp = temp.next
temp.next = common   

# Step 4: Print both lists
print("List A:")
printLL(headA)

print("List B:")
printLL(headB)

# Step 5: Find intersection
intersection = getIntersectionNode(headA, headB)

# Step 6: Output result
if intersection:
    print("Intersection at node with value:", intersection.data)
else:
    print("No intersection")
