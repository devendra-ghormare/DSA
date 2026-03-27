def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid+1
        else:
            high = mid - 1
    
    return -1

print(binary_search([1,2,3,4,5,6,7,8,9], 5))


def recursive_binary_search(nums, low, high, target):
    if low > high:
        return -1 

    mid = (low+high) // 2

    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        return recursive_binary_search(nums, mid+1, high, target)

    return recursive_binary_search(nums, low, mid-1, target)

arr = [1,2,3,4,5,6,7,8,9]
print(recursive_binary_search(arr, 0, len(arr)-1,  5))
