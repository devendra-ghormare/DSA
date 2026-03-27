def find_largest(arr):
    largest = arr[0]

    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest

print(find_largest([4,1,2,3,6,8]))