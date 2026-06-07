def atMost(nums, k):
    left = right = 0
    count = 0
    mpp = {}

    while right < len(nums):
        mpp[nums[right]] = mpp.get(nums[right], 0) + 1

        while len(mpp) > k:
            mpp[nums[left]] -= 1

            if mpp[nums[left]] == 0:
                del mpp[nums[left]]
            
            left += 1
        
        count += right - left + 1

        right += 1
    
    return count 

def subarrayWithKDistinct(nums, k):

##################### Brute Force ##################
    # count = 0

    # for i in range(len(nums)):
    #     mpp = {}
    #     for j in range(i, len(nums)):
    #         mpp[nums[j]] = mpp.get(nums[j], 0) + 1

    #         if len(mpp) == k:
    #             count += 1
    #         elif len(mpp) > k:
    #             break
    
    # return count

    # Time: O(n²)
    # Space: O(n)


##################### Optimal solution ###################

    return atMost(nums, k) - atMost(nums, k-1)

    # Time = O(n)
    # Space = O(n)


print(subarrayWithKDistinct(nums = [1,2,1,2,3], k = 2))