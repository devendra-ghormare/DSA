def alpha_ramp_tringle(n):
    for i in range(1, n+1):
        for j in range(i):
            print(chr(ord('A') + i - 1), end=" ")
        print()

alpha_ramp_tringle(5)