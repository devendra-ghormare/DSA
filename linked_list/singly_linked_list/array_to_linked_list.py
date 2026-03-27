class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def array_to_linkedList(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

def print_linkedList(head):
    temp = head
    while(temp):
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

def length_linkedList(head):
    count = 0
    temp = head
    while(temp):
        count += 1
        temp = temp.next
     
    return count

def search_linkedList(head, val):
    temp = head
    while(temp):
        if temp.data == val:
            return True
        temp = temp.next
    
    return False

arr = [10, 20, 30, 40]
head = array_to_linkedList(arr)
print_linkedList(head)
print(length_linkedList(head))
print(search_linkedList(head, 302))