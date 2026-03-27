
def sum_k_subsequence(i, arr, ds, n, sum_k, s):

    if i == n:
        if s==sum_k:
            print(ds)
        return
    
    ds.append(arr[i])
    s += arr[i]
    sum_k_subsequence(i+1, arr, ds, n, sum_k, s)
    s -= arr[i]
    ds.pop()

    # Not pick
    sum_k_subsequence(i+1, arr, ds, n, sum_k, s)


if __name__ == '__main__':
    arr = [1,1,2]
    sum_k = 2
    n = len(arr)
    ds = []
    i = 0
    s=0
    sum_k_subsequence(i, arr, ds, n, sum_k, s)


############### IF ask to print only any one sunsequence #######


def any_one_sum_k_subsequence(i, arr, ds, n, sum_k, s):

    if i == n:
        if s==sum_k:
            print(ds)
            return True
        else:
            return False
    
    ds.append(arr[i])
    s += arr[i]
    if(any_one_sum_k_subsequence(i+1, arr, ds, n, sum_k, s) == True):
        return True
    s -= arr[i]
    ds.pop()

    # Not pick
    if(any_one_sum_k_subsequence(i+1, arr, ds, n, sum_k, s) == True):
        return True
    
    return False


if __name__ == '__main__':
    arr = [1,1,2]
    sum_k = 2
    n = len(arr)
    ds = []
    i = 0
    s=0
    any_one_sum_k_subsequence(i, arr, ds, n, sum_k, s)