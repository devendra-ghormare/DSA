# def leftRotationByKPlaces(arr, k):
#     n = len(arr)
#     k = k % n

#     temp = []
#     for i in range(k):
#         temp.append(arr[i])
    
#     for i in range(k, n):
#         arr[i-k] = arr[i]
    
#     for i in range(n-k, n):
#         arr[i] = temp[i - (n-k)]
    
#     return arr

# print(leftRotationByKPlaces([1,2,3,4], 3))

############# Optimal solution ###################
def leftRotationByKPlaces(arr, k):
    n = len(arr)
    k = k % n

    def reverse_array(arr, left, right):
        while left <= right:
            arr[left], arr[right] = arr[right], arr[left] 
            left += 1
            right -= 1
    
    reverse_array(arr, 0, k-1)
    reverse_array(arr, k, n-1)
    reverse_array(arr, 0, n-1)

    return arr

print(leftRotationByKPlaces([1,2,3,4], 3))