def first_binary_search(nums, n, k):
    low = 0
    high = n - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == k:
            first = mid
            high = mid - 1
        elif nums[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return first
 
def last_binary_search(nums, n, k):
    low = 0
    high = n - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == k:
            last = mid
            low = mid + 1
        elif nums[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return last

def count_occurance(nums, target):
    n = len(nums)
    first = first_binary_search(nums, n, target)
    if first == -1:
        return [-1, -1]
    last = last_binary_search(nums, n, target)

    return last - first + 1

print(count_occurance([0,1,2,3,4,4,4,4,4,5,6], 4))