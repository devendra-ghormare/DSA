def alpha_hill_triangle(n):
    for i in range(n):

        for j in range(n-i):
            print(" ", end=" ")

        ch = 'A'
        breakpoint = (2*i + 1) // 2

        for j in range(2*i + 1):
            print(ch, end=" ")
            if j < breakpoint:
                ch = chr(ord(ch) + 1)
            else:
                ch = chr(ord(ch) - 1) 


        print()

alpha_hill_triangle(5)