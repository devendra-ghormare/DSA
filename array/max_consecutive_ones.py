def findMaxConsecutive(arr):
    max_num = 0
    count = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            max_num = max(max_num, count)
        else:
            count = 0

    return max_num

print(findMaxConsecutive([1,1,0,1,1,1,2,1,1]))