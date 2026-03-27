def findMaxRowInx(mat, n, m, col):
    maxValue = -1
    index = -1

    for i in range(n):
        if mat[i][col] > maxValue:
            maxValue = mat[i][col]
            index = i
    return index

def peakElement(matrix):
    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = m - 1

    while low <= high:
        mid = (low + high) // 2

        maxRowInx = findMaxRowInx(matrix, n, m, mid)

        left = matrix[maxRowInx][mid-1] if mid - 1 >= 0 else -1
        right = matrix[maxRowInx][mid+1] if mid + 1 < m else -1

        if matrix[maxRowInx][mid] > left and matrix[maxRowInx][mid] > right:
            return [maxRowInx, mid]
        elif matrix[maxRowInx][mid] < left:
            high = mid - 1
        else:
            low = mid + 1
    return [-1, -1]

print(peakElement([[10,20,15],[21,30,14],[7,16,32]]))