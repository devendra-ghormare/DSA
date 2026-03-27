def number_crown(n):
    space = 2 * (n-1)
    for i in range(n):
        # number
        for j in range(1, i+1):
            print(j, end=" ")
        
        #space
        for j in range(space):
            print(" ", end=" ")

        #number
        for j in range(i,0, -1):
            print(j, end=" ")

        print()
        space -= 2

    
    


number_crown(5)