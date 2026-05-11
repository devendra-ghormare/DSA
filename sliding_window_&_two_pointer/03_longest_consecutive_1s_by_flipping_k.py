def longestConsecutiveOnes(nums, k):
    n = len(nums)
    maxLen = 0

################### Brute Force ###############

    # for i in range(n):
    #     zeros = 0
    #     for j in range(i, n):
    #         if nums[j] == 0:
    #             zeros += 1
            
    #         if zeros <= k:
    #             maxLen = max(maxLen, j-i+1)
    #         else:
    #             break
        
    # return maxLen

    # Time: O(n²)
    # Space: O(1)

################ Optimal-1 approach #######################

    # left = right = 0
    # zeros = 0

    # while right < n:
    #     if nums[right] == 0:
    #         zeros += 1
        
    #     while zeros > k:
    #         if nums[left] == 0:
    #             zeros -= 1
            
    #         left += 1
        
        
    #     maxLen = max(maxLen, right-left + 1)
    #     right += 1
    
    # return maxLen

    # Time = O(2n)
    # Space = O(1)

#################### Optimal-2 approach #####################

    left = right = 0
    zeros = 0
    
    while right < n:
        if nums[right] == 0:
            zeros += 1 
        
        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            
            left += 1
        
        maxLen = max(maxLen, right-left+1)
        right += 1
    
    return maxLen

    # Time = O(n)
    # Space = O(1)
    
print(longestConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2))