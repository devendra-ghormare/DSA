def longest_sunarray_with_sum_k(nums, k):
    n = len(nums)
    max_len = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == k:
                max_len = max(max_len, j-i+1)

                
    return max_len

print(longest_sunarray_with_sum_k([10, 5, 2, 7, 1, 9], 15))