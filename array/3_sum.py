def three_sum(nums):
    n = len(nums)

####### Brute force ########

    # st = set()
    # for i in range(n):
    #     for j in range(i+1, n):
    #         for k in range(j+1, n):
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 temp = [nums[i], nums[j], nums[k]]
    #                 temp = sorted(temp)
    #                 st.add(tuple(temp))

    # return [list(t) for t in st]

######### Better with set #######

    # st = set()
    # for i in range(n):
    #     seen = set()
    #     for j in range(i+1, n):
    #         third = - (nums[i] + nums[j])

    #         if third in seen:
    #             triplet = [nums[i], nums[j], third]
    #             triplet.sort()
    #             st.add(tuple(triplet))
            
    #         seen.add(nums[j])

    # return [list(t) for t in st]
    
######### Optimal solution  with two pointer #######

    res = []
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            curr_sum = nums[i] + nums[j] + nums[k]

            if curr_sum == 0:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j-1]:
                    j += 1  
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            
            elif curr_sum < 0:
                j += 1
            else:
                k -= 1

    return res



print(three_sum([-1,0,1,2,-1,-4]))



