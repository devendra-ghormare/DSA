def countMaxRowWithOne(matrix):
    n = len(matrix)
    m = len(matrix[0])

############ Brute Force ###########
    # max_cnt = 0
    # for i in range(n):
    #     cnt_one = 0
    #     for j in range(m):
    #         cnt_one += matrix[i][j]

    #     if cnt_one > max_cnt:
    #         max_cnt = cnt_one
    
    # return cnt_one

########## Optimal with binary ###########
    def lowerBound(nums, n, x): 
        low = 0
        high = n-1
        ones = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= x:
                ones = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ones

    max_cnt = 0
    index = -1

    for i in range(n):
        cnt_ones = m - lowerBound(matrix[i], m, 1)

        if cnt_ones > max_cnt:
            max_cnt = cnt_ones
            index = i

    return index

print(countMaxRowWithOne([ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]))
print(countMaxRowWithOne( [ [0, 0, 1], [0, 1, 1], [0, 1, 1] ]))