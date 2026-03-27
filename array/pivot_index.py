def pivot_index(nums):

    n = len(nums)
    
    # for i in range(n):
    #     left_sum = 0
    #     right_sum = 0

    #     for j in range(i):
    #         left_sum += nums[j]
        
    #     for j in range(i+1, n):
    #         right_sum += nums[j]

    #     if left_sum == right_sum:
    #         return i 
    # return -1

    ###### Better ##########

    total_sum = sum(nums)
    
    left_sum = 0
    for i in range(n):
        if left_sum == total_sum - left_sum - nums[i]:
            return i
        
        left_sum += nums[i]


print(pivot_index([1, 7, 3, 6, 5, 6]))