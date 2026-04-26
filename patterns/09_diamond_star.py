def diamond_star(n):
    # for i in range(n):
    #     for j in range(n-i-1):
    #         print(" ", end=" ")
    #     for j in range(2*i+1):
    #         print("*", end=" ")
    #     for j in range(n-i-1):
    #         print(" ", end=" ") 
    #     print()
    # for i in range(1, n):
    #     for j in range(i):
    #         print(" ", end=" ")
    #     for j in range(2*n- (2*i+1) ):
    #         print("*", end=" ")
    #     for j in range(i):
    #         print(" ", end=" ")
    #     print()

#################### Optimize #################
    for i in range(2*n - 1):
        if i < n:
            spaces = n - i - 1
            stars = 2*i + 1
        else:
            j = i - n + 1
            spaces = j
            stars = 2*(n - j) - 1
        
        print(" " * spaces + "*" * stars)

diamond_star(5)