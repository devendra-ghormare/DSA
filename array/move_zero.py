def move_zero_last(arr):
    n = len(arr)

#### Brute force approch ######

    # temp = []

    # for i in range(n):
    #     if arr[i] != 0:
    #         temp.append(arr[i])
    
    # for i in range(len(temp)):
    #     arr[i]=temp[i]

    # for i in range(n-len(temp)+1 , n):
    #     arr[i] = 0

    # return arr

######### Optimal approch ##########

    non_zero_index = 0

    for i in range(n):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1
    return arr

print(move_zero_last([1,0,2,0,3,0,4]))