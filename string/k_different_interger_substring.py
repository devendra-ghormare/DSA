def subarrayWithKDiff(nums, k):
    n = len(nums)
    count = 0

    for i in range(n):
        mpp = {}
        for j in range(i, n):
            mpp[nums[j]] = mpp.get(nums[j], 0) + 1

            if len(mpp) == k:
                count += 1
            elif len(mpp) > k:
                break
    
    return count 

print(subarrayWithKDiff(nums = [1,2,1,2,3], k = 2))