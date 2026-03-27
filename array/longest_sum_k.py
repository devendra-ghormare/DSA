def longest_sum_k(arr, k):
    n = len(arr)
    left = 0
    right = 0
    max_len = 0
    curr_sum = arr[0]

    while right < n:
        while left < right and curr_sum > k:
            curr_sum -= arr[left]
            left += 1
        
        if curr_sum == k:
            max_len = max(max_len, right - left + 1)
        
        right += 1
        if right < n:
            curr_sum += arr[right]

    return max_len


# print(longest_sum_k([10,5,7,2,1,3], 15))

############ Brute force solution

# def longest_sum_k(arr, k):
#     n = len(arr)
#     max_len = 0

#     for i in range(n):
#         curr_sum = 0
#         for j in range(i, n):
#             curr_sum += arr[j]
#             if curr_sum == k:
#                 max_len = max(max_len, j-i+1)
#     return max_len

# print(longest_sum_k([10,5,7,2,1,3], 15))