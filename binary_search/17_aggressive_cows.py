def canWePlace(stalls, dis, cows):
    n = len(stalls)
    cnt_cows = 1
    last = stalls[0]

    for i in range(n):
        if stalls[i] - last >= dis:
            cnt_cows += 1
            last = stalls[i]
    
    if cnt_cows >= cows:
        return True
    else:
        return False

############ Brute Force ############
def aggressiveCows(stalls, k):
    stalls.sort()
    n = len(stalls)
    maxi = stalls[n-1] - stalls[0]

    for i in range(1, maxi):
        if canWePlace(stalls,i, k):
            continue
        else:
            return i - 1
    
############ Optimal with binary ############

# def aggressiveCows(stalls, k):
#     stalls.sort()
#     n = len(stalls)
#     low = 1
#     high = stalls[n-1] - stalls[0]

#     while low <= high:
#         mid = (low + high) // 2

#         if canWePlace(stalls, mid, k):
#             low = mid + 1
#         else:
#             high = mid - 1
#     return high

print(aggressiveCows([0,3,4,7,9,10],4))