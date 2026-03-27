def lower_bound(nums, x):
    n = len(nums)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans 

print(lower_bound([1,2,3,4,4,5,6,7], 4))