def max_subarray_sum(nums):
    n = len(nums)
    max_sum  = nums[0]

###  Brute and better solution #######
    # for i in range(n):
    #     curr_sum = 0
    #     for j in range(i, n):
    #         curr_sum += nums[j]
    #         max_sum = max(max_sum, curr_sum)
    
    # return max_sum

###### Optimal by kandane's algo ########
    curr_sum = 0
    for i in range(n):
        curr_sum += nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0
    
    return max_sum

print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
        