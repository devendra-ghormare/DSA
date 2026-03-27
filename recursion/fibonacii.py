def fibonacii_with_recursion(n):
    if n <= 1:
        return n
    last = fibonacii_with_recursion(n-1)
    slast = fibonacii_with_recursion(n-2)
    return last + slast

print(fibonacii_with_recursion(4))

# time complecity - n^2 (Exponential)