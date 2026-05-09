def summeryRanges(nums):
    n = len(nums)
    ans = []
    i = 0

    while i < n:
        start = nums[i]

        while i + 1 < n and nums[i] + 1 == nums[i+1]:
            i += 1
        
        end = nums[i]
        
        if start == end:
            ans.append(str(start))
        else:
            ans.append(f"{start}->{end}")
        
        i += 1
    
    return ans

print(summeryRanges([0,1,2,4,5,7]))