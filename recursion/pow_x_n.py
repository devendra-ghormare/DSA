def powXN(x, n):
    ans = 1
    temp = n 

    if temp < 0:
        temp = temp * -1

    while temp > 0:
        if temp % 2 == 1:
            ans = ans * x
            temp = temp - 1
        else:
            x = x * x
            temp = temp // 2
    
    if n < 0:
        ans  = 1 / ans

    return ans 

    # Time = O(log n)
    # Space = O(1)


print(powXN(2, 10))