# def first_last_occurance(nums, target):
#     n = len(nums)
#     first = -1
#     last = -1

#     for i in range(n):
#         if nums[i]  == target:
#             if first == -1:
#                 first = i
#             last = i
#     return [first, last]


########## With lower and upper Bounds #########

# def lowerBound(nums, n, k):
#     low = 0
#     high = n - 1
#     first = n

#     while low <= high:
#         mid = (low + high) // 2

#         if nums[mid] >= k:
#             first = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return first

# def upperBound(nums, n, k):
#     low = 0
#     high = n - 1
#     last = n

#     while low <= high:
#         mid = (low + high) // 2

#         if nums[mid] > k:
#             last = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return last

# def first_last_occurance(nums, target):
#     n = len(nums)
#     lb = lowerBound(nums, n, target)
#     if lb == n or nums[lb] != target:
#         return [-1, -1]
#     ub = upperBound(nums, n, target)

#     return [lb, ub-1]


##************** With binary search normal **************##

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

def first_last_occurance(nums, target):
    n = len(nums)
    first = first_binary_search(nums, n, target)
    if first == -1:
        return [-1, -1]
    last = last_binary_search(nums, n, target)

    return [first, last]

print(first_last_occurance([1,2,3,4,4,5,5,6,7,8], 5))