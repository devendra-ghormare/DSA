def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
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

def countPairs(arr, low, mid, high):
    right = mid + 1
    count = 0
    for i in range(low, mid+1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        count += (right - (mid+1))      
    return count 
    
def merge_sort(arr, low, high):
    count = 0
    if low >= high:
        return count
    
    mid = (low + high) // 2

    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid+1, high)
    count += countPairs(arr, low, mid, high)
    merge(arr, low, mid, high)

    return count 
        


def reversePairs(nums):
    n = len(nums)
####### Brute Force #########

    # count = 0
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if nums[i] > 2 * nums[j]:
    #             count += 1
    
    # return count

########## Optimal with merge sort ###########

    return merge_sort(nums, 0, n-1)


print(reversePairs([2, 3, 7, 1, 3, 5]))
