def bubble_sort(arr):

    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
        
    return arr

print(bubble_sort([1,4,6,2,3,8,9,5]))