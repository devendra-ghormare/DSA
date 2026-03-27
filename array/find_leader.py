def find_leader(arr):
    n = len(arr)
    leader = []

    for i in range(n):
        is_leader = True
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                is_leader = False
                break
        if is_leader:
            leader.append(arr[i])
    return leader


print(find_leader([10,22,12,0,3,6]))