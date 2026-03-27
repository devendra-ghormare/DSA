def subarrayWithSumK(nums, l):
    n = len(nums)
###### Brute Force with loops ###########
    # count = 0
    # for i in range(n):
    #     for j in range(i, n):
    #         XOR = 0
    #         for k in range(i, j+1):
    #             XOR = XOR ^ nums[k]

    #         if XOR == l:
    #             count += 1
    
    # return count

###### Better with 1 loop less ###########
    # count = 0
    # for i in range(n):
    #     XOR = 0
    #     for j in range(i, n):
    #         XOR = XOR ^ nums[j]
        
    #         if XOR == l:
    #             count += 1
    
    # return count

###### Optimal with hashmap ###########
    mpp = {0:1}
    count = 0
    xr = 0
    for i in range(n):
        xr = xr ^ nums[i]

        x = xr ^ l
        if x in mpp:
            count += mpp[x]

        if xr in mpp:
            mpp[xr] += 1
        else:
            mpp[xr] = 1
    return count


print(subarrayWithSumK([4, 2, 2, 6, 4], 6))
