def maxScore(nums, k):
    n = len(nums)
    lSum = 0
    rSum = 0
    maxSum = 0

    for i in range(k):
        lSum += nums[i]
    
    maxSum = lSum

    right = n-1
    for i in range(k-1, -1, -1):
        lSum -= nums[i]
        rSum += nums[right]
        right -= 1
        maxSum = max(maxSum, lSum+rSum)

    return maxSum


print(maxScore([6,2,3,4,7,2,1,7,1], 4))