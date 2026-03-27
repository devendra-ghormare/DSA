def two_sum(arr, target):
    n = len(arr)
    
    ######### Brute Force solution #############
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if arr[i] + arr[j] == target:
    #             return [i, j]

    ######### Better solution we will use dict #############

    # mydict = {}
    # for i in range(n):
    #     a = arr[i]
    #     more = target - a

    #     if more in mydict:
    #         return [mydict[more], i]

    #     mydict[a] = i
    
    ######### Optimum Solution by two pointer ########

    arr = sorted(arr)
    left = 0
    right = n-1

    while left < right :
        curr_sum = arr[left] + arr[right]

        if curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1
        else:
            return "YES"
    return "NO"


print(two_sum([2,7,11,15], 9))