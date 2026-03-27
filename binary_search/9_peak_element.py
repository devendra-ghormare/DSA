def peakElement(nums):
    n = len(nums)

######## Brute Force #############

    # for i in range(n):
    #     if i == 0:
    #         if n == 1 or nums[i] > nums[i+1]:
    #             return i
        
    #     elif i == n -1:
    #         if nums[i] > nums[n-2]:
    #             return i
        
    #     else:
    #         if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
    #             return i
    # return -1
##########
    # for i in range(n):
    #     if (i == 0 or nums[i] > nums[i-1]) and (i == n-1 or nums[i] > nums[i+1]):
    #         return i

################# Optimal Approch ##############
    if n == 1:
        return 0

    if nums[0] > nums[1]:
        return 0
    
    if nums[n-1] > nums[n-2]:
        return n-1
    
    low = 1
    high = n-2

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        
        elif nums[mid] > nums[mid-1]:
            low = mid + 1
        else:
            high = mid - 1
        
    return -1
print(peakElement([1,2,3,8,4,5]))
