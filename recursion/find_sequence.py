def find_subsequence(i, arr, ds, n):
    if i == n:
        print(ds)
        return 
    
    # for take
    ds.append(arr[i])
    find_subsequence(i+1, arr, ds, n)
    ds.pop()

    # for not take
    find_subsequence(i+1, arr, ds, n)

find_subsequence(0, [3,2,1], [], 3)

########################################3
