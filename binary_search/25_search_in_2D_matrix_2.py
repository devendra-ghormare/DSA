def searchIn2DMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = m-1
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return [row, col]
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return [-1, -1]

print(searchIn2DMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))