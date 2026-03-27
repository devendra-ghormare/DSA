def symmentric_void_pattern(n):
    space = 0
    
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")

        for j in range(space):
            print(" ", end=" ")
        
        for j in range(n-i):
            print("*", end=" ")
        space += 2
        print()

    space = 2*n - 2
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")

        for j in range(space):
            print(" ", end=" ")
        
        for j in range(i+1):
            print("*", end=" ")
        space -= 2
        print()

symmentric_void_pattern(6)