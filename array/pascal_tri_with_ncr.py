def ncr(n, r):

    result = 1

    for i in range(r):
        result = result * (n-i)
        result = result // (i+1)
    
    return result

# print(ncr(5,2))


def print_complete_row(n):

    # for i in range(1,n+1):
    #     print(ncr(n-1, i-1), end=" ")

    ans = 1
    row=[]
    row.append(ans)

    for i in range(1, n):
        ans = ans * (n-i)
        ans = ans // i
        row.append(ans)
    return row

print(print_complete_row(5))


def print_pascal_triangle(n):
    
    ans = []
    for i in range(1, n+1):
        temp = []
        for j in range(1, i+1):
            temp.append(ncr(i-1, j-1))
        ans.append(temp)
    return ans

print(print_pascal_triangle(5))