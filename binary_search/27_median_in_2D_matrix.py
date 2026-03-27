def medianIn2DMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
########### Brute Force ############
    # mat = []
    # req = n*m // 2

    # for i in range(n):
    #     for j in range(m):
    #         mat.append(matrix[i][j])
    
    # mat.sort()

    # return mat[req]

############## Optimal approach ##########
    def upperBound(nums, n, x):
        low = 0
        high = n-1
        ans = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def countSmallElement(nums, n, m, x):
        count = 0
        for i in range(n):
            count += upperBound(nums[i], m, x)
        return count

    req = n*m // 2

    low = float('inf')
    high = float('-inf')

    for i in range(n):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][m-1])
    
    while low <= high:
        mid = (low + high) // 2
        smallEqual = countSmallElement(matrix, n, m, mid)

        if smallEqual <= req:
            low = mid + 1
        else:
            high = mid - 1
    return low 



print(medianIn2DMatrix([ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] ))