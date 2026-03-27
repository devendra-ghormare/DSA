def findSquareRoot(num):
    low = 1
    high = num
    res = 1
    while low <= high:
        mid = (low + high) // 2

        ans = mid * mid
        if ans <= num:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res

print(findSquareRoot(36))
