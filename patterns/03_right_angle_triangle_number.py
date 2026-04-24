def right_angle_triangle_number(n):
    # for i in range( n):
    #     num = 1
    #     for j in range(i+1):
    #         print(num, end=" ")
    #         num += 1
    #     print()
    
################# Optimized version #############

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    
    # Time - O(n²)
    # Space - O(1)

right_angle_triangle_number(5)




