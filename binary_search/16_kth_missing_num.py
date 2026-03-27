def kthMissingNum(nums, k):
    n = len(nums)

####### Brute Force #########
    
    # for num in nums:
    #     if num <= k:
    #         k += 1
    #     else:
    #         break
    # return k

######### Optimal solution #########
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2

        missing = nums[mid] - (mid+1)

        if missing < k:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return low + k
print(kthMissingNum([5,7,10], 4))
