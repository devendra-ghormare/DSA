def findKRotation(nums):
    n = len(nums)
    low = 0
    high = n - 1
    index = -1
    ans = float('inf')

    while low <= high:
        mid = (low + high) // 2

        if nums[low] == nums[mid] == nums[high]:
            if nums[low] < ans:
                index = low
                ans = nums[low]
            low += 1
            high -= 1
            continue

        if nums[low] <= nums[mid]:
            if nums[low] < ans:
                index = low
                ans = nums[low]
            low = mid + 1
        else:
            if nums[mid] < ans:
                index = mid
                ans = nums[mid]
            high = mid - 1
    return index

print(findKRotation([7,8,1,2,3,4,5,6]))