def removeDuplicate(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
    

    return i+1


print(removeDuplicate([1,1,2,3,3,4]))