def leftRotate(nums):
    n = len(nums)
    temp = nums[0]
    for i in range(1, len(nums)):
        nums[i-1] = nums[i]
    nums[n - 1] = temp
    


print(leftRotate([1,2,3,4]))