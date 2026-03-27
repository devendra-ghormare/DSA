def findMax(piles):
    maxi = float('-inf')
    for num in piles:
        maxi = max(maxi, num)
    return maxi

def calculateTotalHours(piles, mid):
    n = len(piles)
    total_hours = 0

    for i in range(n):
        total_hours += (piles[i] + mid-1) // mid
    return total_hours

def kokoEatingBanana(piles, h):

########### Brute Force #############
    # maxi = findMax(piles)
    # for i in range(1, maxi+1):
    #     reqtime = calculateTotalHours(piles, i)

    #     if reqtime <= h:
    #         return i

########### Optimal with binary search #############

    low = 1
    high = findMax(piles)

    while low <= high:
        mid = (low + high) // 2

        total = calculateTotalHours(piles, mid)

        if total <= h:
            high = mid - 1
        else:
            low = mid + 1

    return low

print(kokoEatingBanana([30,11,23,4,20], 5)) 