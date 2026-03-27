def possible(nums, days, m, k):
    count = 0
    bouquet = 0

    for num in nums:
        if num <= days:
            count += 1
        else:
            bouquet += (count // k)
            count = 0
    bouquet += (count // k)

    if bouquet >= m:
        return True
    else:
        return False

def minDays(bloomDay, m, k):
    n = len(bloomDay)

    if m*k > n:
        return -1
    
    low = min(bloomDay)
    high = max(bloomDay)

################ Brute force ##########
    # for i in range(low, high+1):
    #     if possible(bloomDay, i, m, k):
    #         return i
    # return -1
################ Optimal solution with binary search ##########
    while low <= high:
        mid = (low + high) // 2

        if possible(bloomDay, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1
    
    return low

print(minDays([1,10,3,10,2], m = 3, k = 1))
    
