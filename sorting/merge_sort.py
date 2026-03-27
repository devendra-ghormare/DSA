def merge_sort(arr, low, high):

    if low >= high:
        return

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1  

    while left  <= right and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low, high+1):
        arr[i] = temp[i-low]


nums = [1,8,6,4,2,3,9,5]
merge_sort(nums, 0, len(nums) - 1)
print(nums)