def star_pyramid(n):
################ Brute Force ################
    # for i in range(n):
    #     for _ in range(n-i+1):
    #         print(" ", end="")
    #     for _ in range(2*i+1):
    #         print("*", end="")
    #     for _ in range(n-i+1 ):
    #         print(" ", end="") 
    #     print()

################ Optimize version ################
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("*" * (2*i + 1))

    # Time = O(n²)
    # Space = O(1)

    
star_pyramid(5)