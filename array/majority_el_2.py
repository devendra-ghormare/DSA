def majority_el_2(nums):
    n = len(nums)

######### Brute Force #######
    # ls = []
    # for i in range(n):
    #     if len(ls) == 0 or ls[0] != nums[i]:
    #         count = 0
    #         for j in range(n):
    #             if nums[j] == nums[i]:
    #                 count += 1
                
    #         if count > n//3:
    #             ls.append(nums[i])
    
    #     if len(ls) == 2:
    #         break
    
    # return ls

############### Better with hashmap ###########
    mn = n // 3 + 1
    mpp = {}
    ls = []

    for num in nums:
        if num in mpp:
            mpp[num] += 1
        else:
            mpp[num] = 1
        
        if mpp[num] == mn:
            ls.append(num)
    return ls

print(majority_el_2([2,2,1,1,1,2,2]))