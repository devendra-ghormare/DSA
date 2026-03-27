def checkArraySorted(arr):


    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
        
print(checkArraySorted([1,2,3]))