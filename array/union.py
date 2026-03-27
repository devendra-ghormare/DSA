def union(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0

    ans = []

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if len(ans) == 0 or ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i += 1
        else:
            if len(ans) == 0 or ans[-1] != arr2[j]:
                ans.append(arr2[j])
            j += 1
        
    while i < n:
        if len(ans) == 0 or ans[-1] != arr1[i]:
            ans.append(arr1[i])
        i += 1
    while j < m:
        if len(ans) == 0 or ans[-1] != arr2[j]:
            ans.append(arr2[j])
        j += 1
    return ans

print(union([1,2,3,4], [1,1,2,3,3,5]))

