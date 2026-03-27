# def rotate_right_with_k_place(arr, k):
#     n= len(arr)
#     k = k % n

#     # get the values of k
#     temp = []
#     for i in range(n-k, n):
#         temp.append(arr[i])
    
#     # move remaning elemnt to right by k places
#     for i in range(n-k-1, -1, -1):
#         arr[i + k ] = arr[i]
      
#     for i in range(0, k):
#         arr[i] = temp[i]

#     return arr

# print(rotate_right_with_k_place([1,2,3,4], 2))

########## Optimal solution ##############

def rotate_right_with_k_place(arr, k):
    n = len(arr)
    k = k % n

    def reverse(arr, left, right):
        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1 
            right -= 1
    
    reverse(arr, n-k, n-1)
    reverse(arr, 0, n-k-1)
    reverse(arr, 0, n-1)

    return arr


print(rotate_right_with_k_place([1,2,3,4], 2))