def right_angle_triangle_number_2(n):

    for i in range(1, n+1):
        for _ in range(i):
            print(i, end=" ")
           
        print()
    
    # Time = O(n²)
    # Space = O(1)

right_angle_triangle_number_2(5)