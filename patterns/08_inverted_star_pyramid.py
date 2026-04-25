def inverted_star_pyramind(n):
################ Brute Force ################
   
    # for i in range(n):
    #     for j in range(i):
    #         print(" ", end=" ")
    #     for j in range(2*n- (2*i+ 1) ):
    #         print("*", end=" ")
    #     for j in range(i):
    #         print(" ", end=" ")
        
    #     print()

################ Optimize ################

    for i in range(n):
        print(" " * i, end="")
        print("*" * (2*n - (2*i + 1)))
    
    # Time = O(n²)
    # Space = O(1)

inverted_star_pyramind(5)
        