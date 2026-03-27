def power(n, m, mid):
    val = 1
    for _ in range(1, n+1):
        val = val * mid
        if val > m:
            return val
    return val 


def nthSquareRoot(n, m):
    low = 1
    high = m

    while low <= high:
        mid = (low + high) // 2

        ans = power(n, m, mid)

        if ans == m:
            return mid
        elif ans > m:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(nthSquareRoot(3, 27))