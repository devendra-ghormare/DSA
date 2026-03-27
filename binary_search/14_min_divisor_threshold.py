################ Brute Force #############

# def smallestDivisor(nums, threshhold):
#     n = len(nums)

#     if n > threshhold:
#         return -1
    
#     for i in range(1, max(nums)+1):
#         sum = 0
#         for j in range(n):
#             sum += ((nums[j] + i-1) // i) 
#         if sum <= threshhold:
#             return i



################ OPtimal Approach #############
def sumByD(nums, div):
    n = len(nums)
    res = 0

    for i in range(n):
        res += ((nums[i] + div -1) // div)
    
    return res

def smallestDivisor(nums, threshold):
    if len(nums) > threshold:
            return -1
    low = 1
    high = max(nums)
    ans = 0

    while(low <= high):
        mid = (low + high) // 2

        if sumByD(nums, mid) <= threshold:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

print(smallestDivisor([1,2,5,9], 6))