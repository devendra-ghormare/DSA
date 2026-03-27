def symmentric_butterfly_pattern(n):
    # space = 2 * n - 2

    # for i in range(n):
    #     for j in range(i+1):
    #         print("*", end=" ")
    #     for j in range(space):
    #         print(" ", end=" ")
    #     for j in range(i+1):
    #         print("*", end=" ")
    #     space -= 2
    #     print()
    
    # space = 2
    # for i in range(n):
    #     for j in range(n-i-1):
    #         print("*", end=" ")
    #     for j in range(space):
    #         print(" ", end=" ")
    #     for j in range(n-i-1):
    #         print("*", end=" ")
    #     space += 2
    #     print()

    spaces = 2*n - 2
    for i in range(2*n - 1):
        if i < n:
            star = i + 1
        else:
            star = 2 * n - i - 1
            
        for j in range(star):
            print("*", end=" ")
        for j in range(spaces):
            print(" ", end=" ")
        for j in range(star):
            print("*", end=" ")
        print()
        if i < n-1:
            spaces -= 2 
        else:
            spaces += 2




symmentric_butterfly_pattern(5)