def alpha_traingle(n):
    start = ord('A') + n-1
    for i in range(n):
        for j in range(i+1):
            print(chr(start-j), end=" ")
        print()

alpha_traingle(5)