def rearrange_array(arr):
    n = len(arr)
    neg, pos = [], []
    
    for i in range(n):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    
    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[2*i] = pos[i]
            arr[(2*i)+1] = neg[i]
        
        remIndex = 2 * len(neg)
        for i in range(len(neg), len(pos)):
            arr[remIndex] = pos[i]
            remIndex += 1
    else:
        for i in range(len(pos)):
            arr[2*i] = pos[i]
            arr[(2*i)+1] = neg[i]

        remIndex = 2 * len(pos)
        for i in range(len(pos), len(neg)):
            arr[remIndex] = neg[i]
            remIndex += 1
    
    return arr

print(rearrange_array([2,-1,6,-8,8,9,4,-7]))
