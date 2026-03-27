def four_sum(nums, target):
    n = len(nums)

############# Brute Force by looping #########
    # result = set()
    # for i in range(n):
    #     for j in range(i+1, n):
    #         for k in range(j+1, n):
    #             for l in range(k+1, n):
    #                 total_sum = nums[i]+nums[j]
    #                 total_sum += nums[k]
    #                 total_sum += nums[l]

    #                 if total_sum == target:
    #                     fourth = [nums[i], nums[j], nums[k], nums[l]]
    #                     fourth.sort()
    #                     result.add(tuple(fourth))
    # return [list(t) for t in result]

############# Better by hashset or set #########
    # result = set()
    # for i in range(n):
    #     for j in range(i+1, n):
    #         seen = set()
    #         for k in range(j+1, n):
    #             fourth = target - nums[i] - nums[j] - nums[k]

    #             if fourth in seen:
    #                 idx = [nums[i], nums[j], nums[k], fourth]
    #                 idx.sort()
    #                 result.add(tuple(idx))
                
    #             seen.add(nums[k])

    # return [list(t) for t in result]

############# optimum with pointers #########
    result = []
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            
            k = j + 1
            l = n - 1

            while k < l:
                total_sum = nums[i] + nums[j]
                total_sum += nums[k]
                total_sum += nums[l]

                if total_sum == target:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1
                
                elif total_sum < target:
                    k += 1
                else:
                    l -= 1
    return result



print(four_sum([1,0,-1,0,-2,2], 0))
