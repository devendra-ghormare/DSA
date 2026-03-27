
def findMissingRepeatingNumbers(nums):
    n = len(nums)
############### Brute Force ######  
    # repeat = -1
    # missing = -1

    # for i in range(1, n+1):
    #     count = 0
    #     for j in range(n):
    #         if nums[j] == i:
    #             count += 1
        
    #     if count == 2:
    #         repeat = i
    #     elif count == 0:
    #         missing = i
        
    #     if repeat != -1 and missing != -1:
    #         break

############### Better solution ######
    # mpp = [0] * (n+1)

    # for num in nums:
    #     mpp[num] += 1

    # repeat = -1
    # missing = -1

    # for i in range(1, n+1):
    #     if mpp[i] == 2:
    #         repeat = i
    #     elif mpp[i] == 0:
    #         missing = i

    #     if repeat != -1 and missing != -1:
    #         break
    
    # return [repeat, missing]

############### optimal with equation ######
    Sn = (n * (n+1)) // 2
    S2n = (n * (n+1) * (2*n+1)) // 6
    S = 0
    S2 = 0

    for i in range(n):
        S += nums[i]
        S2 += nums[i] * nums[i]
    
    val1 = S - Sn   # x - y 
    val2 = S2 - S2n # x^2 - y^2 = val2 - (x-y)(x+y) =  val2  then  x+y = val2 //(x-y)
    val2 = val2 // val1  # x+y 
    x = (val1 + val2) // 2 # from equation formula 
    y = x - val1

    return [x, y]

print(findMissingRepeatingNumbers([1, 2, 3, 6, 7, 5, 7]))
