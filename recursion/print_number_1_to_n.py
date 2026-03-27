def printNumber(n, i=1):
    if i > n:
        return
    print(i)
    printNumber(n, i+1)

printNumber(5)

## Print Reverse  

def print_number_reverse(n):
    
    if n <=0:
        return
    print(n)
    print_number_reverse(n-1)

print_number_reverse(5)

## print 1 to N Backtracking

def print_number_backtracking(n):
    if n == 0:
        return 
    print_number_backtracking(n-1)
    print(n)

print_number_backtracking(5)

## reverse this above backtracking

def print_reverse_number_backtracking(n):
    if n <= 0:
        return 
    print(n)
    print_reverse_number_backtracking(n-1)

print_reverse_number_backtracking(5)