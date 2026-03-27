def sum_of_number(n, sum):
    if n < 1:
        print(sum)
        return 
    sum_of_number(n-1, sum+n)


if __name__ == '__main__':
    n = 3
    sum_of_number(n ,0)


##################################

def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n-1)
    
sum_of_numbers(3)
