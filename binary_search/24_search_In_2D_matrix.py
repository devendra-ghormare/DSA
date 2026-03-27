def searchIn2DMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

########### Brute Force ############
    # for i in range(n):
    #     for j in range(m):
    #         if matrix[i][j] == target:
    #             return True
    
    # return False

########### Better  ############
    # def binary_search(nums, k):
    #     low = 0
    #     high = len(nums) - 1

    #     while low <= high:
    #         mid = (low + high) // 2

    #         if nums[mid] == k:
    #             return True
    #         elif nums[mid] < k:
    #             low = mid + 1
    #         else:
    #             high = mid - 1
    #     return False
    
    # for i in range(n):
    #     if binary_search(matrix[i], target):
    #         return True
    # return False

########### Optimal ############
    low = 0
    high = n*m - 1

    while low <=  high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False



print(searchIn2DMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))