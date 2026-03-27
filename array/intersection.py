def intersection(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    ans = []

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            ans.append(arr1[i])
            i += 1
            j += 1
    
    return ans

print(intersection([1,2,3,5], [1,3,5,7]))