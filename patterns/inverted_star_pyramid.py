def inverted_star_pyramind(n):
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(2*n- (2*i+ 1) ):
            print("*", end=" ")
        for j in range(i):
            print(" ", end=" ")
        
        print()
            
inverted_star_pyramind(5)
        