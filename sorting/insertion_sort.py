def insertion_sort(arr):

    for i in range(len(arr)):
        j = i

        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr
        
print(insertion_sort([1, 4, 6, 2, 3, 8, 9, 5]))