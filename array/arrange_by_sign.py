def arrange_by_sign(arr):
    n = len(arr)
     
############  Brute Force #############
    # pos  = []
    # neg = []

    # for i in range(n):
    #     if arr[i] > 0:
    #         pos.append(arr[i])
    #     else:
    #         neg.append(arr[i])
    
    # for i in range(0, n//2):
    #     arr[2*i] = pos[i]
    #     arr[(2*i)+1] = neg[i]

    # return arr

############  Optimal #############
    ans = [0] * n
    posIndex = 0
    negIndex = 1

    for i in range(n):
        if arr[i] < 0:
            ans[negIndex] = arr[i]
            negIndex += 2
        else:
            ans[posIndex] = arr[i]
            posIndex += 2
    
    return ans


print(arrange_by_sign([3,1,-2,-5,2,-4]))