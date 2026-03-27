def findDays(weights, cap):
    days = 1
    load = 0

    for w in weights:
        if load + w > cap:
            days = days + 1
            load = w
        else:
            load += w
    
    return days
########### Brute Force #############

# def leastWeightCapacity(weights, days):
#     n = len(weights)
#     low = max(weights)
#     high = sum(weights)

#     for i in range(low, high+1):
#         if findDays(weights, i) <= days:
#             return i
#     return -1

########## Optimal with binary search ##############

def leastWeightCapacity(weights, days):
    low = max(weights)
    high = sum(weights)

    while low <= high:
        mid = (low + high) // 2

        if findDays(weights, mid) <= days:
            high = mid - 1
        else:
            low = mid + 1
    
    return low
print(leastWeightCapacity(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))