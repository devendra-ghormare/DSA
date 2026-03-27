def quick_sort(arr):
    qs(arr, 0, len(arr) - 1)
    return arr


def qs(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)
        qs(arr, low, pIndex-1)
        qs(arr, pIndex+1, high)

def partition(arr, low, high):
    left = low
    right = high
    pivot = arr[low]

    while left < right:
        while arr[left] <= pivot and left <= high - 1:
            left += 1
        while arr[right] > pivot and right >= low:
            right -=1
        
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[low] , arr[right] = arr[right], arr[low]
    return right


print(quick_sort([1,8,6,4,2,3,9,5]))




#####################

# def quick_sort_desc(arr):
#     qs_desc(arr, 0, len(arr) - 1)
#     return arr


# def qs_desc(arr, low, high):
#     if low < high:
#         pIndex = partition_desc(arr, low, high)
#         qs_desc(arr, low, pIndex-1)
#         qs_desc(arr, pIndex+1, high)

# def partition_desc(arr, low, high):
#     left = low
#     right = high
#     pivot = arr[low]
#### for descending order we change just pivote comparision from upper
#     while left < right:
#         while arr[left] >= pivot and left <= high - 1:
#             left += 1
#         while arr[right] < pivot and right >= low:
#             right -=1
        
#         if left < right:
#             arr[left], arr[right] = arr[right], arr[left]
    
#     arr[low] , arr[right] = arr[right], arr[low]
#     return right


# print(quick_sort_desc([1,8,6,4,2,3,9,5]))